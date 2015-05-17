from __future__ import print_function
from six.moves import StringIO
from numpy import (array, searchsorted, array_equal, setdiff1d, int64, argsort,
                   arange, ndarray, asarray, int64)
from pyNastran.utils import object_attributes

class VectorizedCard(object):
    type = 'VectorizedCard'
    def __init__(self, model):
        self.model = model
        self.n = 0
        self.i = 0
        self._comments = {}
        if self.type in model._element_name_to_element_type_mapper:
            self.op2_id = model._element_name_to_element_type_mapper[self.type]
        else:
            if self.type.startswith('C'):
                print('there is no op2_id to apply for element=%r' % self.type)

    def __len__(self):
        return self.n

    def shrink(self, refcheck=True):
        raise NotImplementedError()

    def resize(self, n, refcheck=True):
        names = object_attributes(self, mode="public")
        for name in names:
            attr = getattr(self, name)
            if isinstance(attr, ndarray):
                #self.model.log.info('resizing %r; shape=%s; size=%s' % (name, attr.shape, attr.size))
                # resize the array
                shape2 = list(attr.shape)
                shape2[0] = n
                attr.resize(tuple(shape2), refcheck=refcheck)

                if n > self.n:
                    # TODO: fill the data with nan values ideally, but it's not working
                    if attr.ndim == 1:
                        attr[self.n:] = 0
                    elif attr.ndim == 2:
                        attr[self.n:, :] = 0
                    elif attr.ndim == 3:
                        attr[self.n:, :, :] = 0
                    else:
                        raise NotImplementedError(attr.shape)
                    #print(attr)
            else:
                # metadata
                pass
        if self.i >= n:
            self.i = n
        self.n = n

    def get_stats(self):
        msg = []
        if self.n:
            msg.append('  %-8s: %i' % (self.type, self.n))
        return msg

    def __repr__(self):
        f = StringIO()
        self.write_bdf(f)
        return f.getvalue().rstrip()

    def write_bdf(self, f, size=8, is_double=False):
        raise NotImplementedError(self.type)

    def _verify(self, xref=True):
        raise NotImplementedError(self.type)

    def _validate_slice(self, i):
        if self.n == 0:
            raise RuntimeError('%s has not been allocated or built' % self.type)
        if isinstance(i, int) or isinstance(i, int64):
            i2 = array([i], dtype='int32')
        elif isinstance(i, list):
            i2 = asarray(i)
        elif i is None:
            i2 = None  # slice(None)
        elif len(i.shape) == 1:
            i2 = i
        else:
            #print(i, type(i), i.shape)
            i2 = i
        #print('shape=%s' % str(i2.shape))
        return i2

    def _get_sorted_index(self, sorted_array, unsorted_array, n, field_name, msg, check=True):
        if not array_equal(argsort(sorted_array), arange(len(sorted_array))):
            msg2 = '%s is not sorted\nsorted_array=%s' % (msg, sorted_array)
            raise RuntimeError(msg2)
        assert isinstance(n, int64) or isinstance(n, int), 'field_name=%s n=%s type=%s' % (field_name, n, type(n))
        assert isinstance(check, bool)
        if unsorted_array is None:
            i = slice(None)
            if n == 1:
                i = array([0], dtype='int32')
            return i
        else:
            i = searchsorted(sorted_array, unsorted_array)
            i.astype('int32')
            if check:
                try:
                    sorted_array_i = sorted_array[i]
                except IndexError:
                    msg = 'sorted_array_i = sorted_array[i] - %s\n' % field_name
                    msg += 'sorted_array=%s\n' % sorted_array
                    msg += 'i=%s' % (i)
                    raise IndexError(msg)

                if not array_equal(sorted_array_i, unsorted_array):
                    # undefined nodes/elements
                    #print('unsorted %s' % unsorted_array)
                    #print('sorted %s' % sorted_array)
                    #pass
                    msg2 = 'Undefined %s\n' % msg
                    msg2 += 'diff=%s\n' % setdiff1d(unsorted_array, sorted_array)
                    msg2 += 'sorted %s= %s; n=%s\n' % (field_name, str(sorted_array), len(sorted_array))
                    msg2 += 'unsorted %s = %s\n' % (field_name, unsorted_array)
                    msg2 += 'sorted %s[i]= %s\n' % (field_name, sorted_array[i])
                    msg2 += 'i=%s\n' % i
                    raise RuntimeError(msg2)
        if isinstance(i, int64) or isinstance(i, int):
            i = array([i], dtype='int32')
        return i

def by_converter(value, default):
    """
    For use in:
        - get_index_by_?
        - get_?_by_index

    INPUT:
      - list
      - int
      - 1d-array
      - None
    OUTPUT
      - 1d-array

    Assumes dtype='int32'
    """
    if value is None:
        return default
    if isinstance(value, int):
        return array([value], dtype='int32')
    else:
        return asarray(value)