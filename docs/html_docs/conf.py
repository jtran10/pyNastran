# -*- coding: utf-8 -*-
#
# pyNastran documentation build configuration file, created by
# sphinx-quickstart on Sun Jan 07 19:17:52 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os.path

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

cwd = os.getcwd()
if on_rtd:
    pkg_path = os.path.join(os.path.dirname(cwd), 'pyNastran')
else:
    import pyNastran
    pkg_path = pyNastran.__path__[0]

print ("cwd", cwd)
print ("pkg_path", pkg_path)
sys.stdout.flush()

sys.path.append(os.path.dirname(cwd))
sys.path.append(os.path.dirname(pkg_path))
sys.path.append(pkg_path)
sys.path.append(os.path.join(pkg_path, 'bdf'))
sys.path.append(os.path.join(pkg_path, 'op2'))
sys.path.append(os.path.join(pkg_path, 'f06'))


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# ---3rd party modules don't work, so we hack them in --------------------------
MOCK_MODULES = [
    #'numpy', 'numpy.linalg','numpy.__version__',
    'pandas',
    #'numpydoc',
    'PySide',
    'numpy.distutils.core',
    'numpy.distutils',
    'matplotlib',
    'wx',
    #'vtk', 'PyQt4', 'PySide',
    'docopt',
    #'numpydoc',
    #'openmdao',
    #'openmdao.main.api',
    #'openmdao.util',
    #'openmdao.util.doctools',
    #'openmdao.lib.datatypes.api',
    #'openmdao.lib.components',
    #'openmdao.lib.drivers.api',
    #'openmdao.lib.components.nastran.nastran',
    #'openmdao.examples.bar3simulation.bar3',
    #'openmdao.examples.bar3simulation.bar3_wrap_f',
    #'nastranwrapper.nastran',
    #'nastranwrapper',
    #'nastranwrapper.test.nastranwrapper_test_utils',
    ]
try:
    import scipy
except ImportError:
    MOCK_MODULES += [
        'scipy', 'scipy.linalg', 'scipy.sparse',
        'scipy.integrate', 'scipy.interpolate', 'scipy.spatial',
    ]

#try:
#    import imageio
#except ImportError:
#    MOCK_MODULES += ['imageio']
#
#try:
#    import qtpy
#except ImportError:
#    MOCK_MODULES += ['qtpy']

MOCK_MODULES += ['qtpy', 'qtpy.QtWidgets', 'qtpy.QtCore', 'qtpy.Qsci', 'qtpy.compat',
                 'qtpy.QtGui', 'imageio']
#MOCK_MODULES += ['pygtk', 'gtk', 'gobject', 'argparse', 'numpy', 'pandas']

## requires the mock module in Python 2.x
# pip install mock
# conda install mock
load_mock = True
if load_mock:
    from six import PY2
    if PY2:
        from mock import MagicMock
    else:
        from unittest.mock import MagicMock

    class Mock(MagicMock):
        @classmethod
        def __getattr__(cls, name):
            if name in ['__path__', 'pi', '_string', '__get__', '__set__']:
                return Mock()
            #print('MOCK cls=%r name=%r' % (cls, name))
            return MagicMock()
    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

if not on_rtd:
    MOCK_MODULES = []

#if 0:
    #class Mock(object):
        #def __init__(self, *args, **kwargs):
            #pass

        #def __call__(self, *args, **kwargs):
            #return Mock()

        ##def __len__(self):  # for numpy arrays
        ##    return 3 #  needs to be an integer

        #@classmethod
        #def __getattr__(cls, name):
            #if name in ('__file__', '__path__'):
                #return '/dev/null'
            #elif name[0] == name[0].upper():
                #mockType = type(name, (), {})
                #mockType.__module__ = __name__
                #return mockType
            #else:
                #return Mock()

#for mod_name in MOCK_MODULES:
    #sys.modules[mod_name] = Mock()

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    #'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autosummary',
    #'sphinx.ext.napolean',
    'numpydoc',
]

# suppress warnings
numpydoc_show_class_members = False

# display todos
todo_include_todos = True

# show class docstring and __init__ docstring
autoclass_content = 'both'

# inheritance diagram should have size determined by graphviz
# with layout from top to bottom (default is left to right)
inheritance_graph_attrs = dict(size='""')
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.2-dev'
# The full version, including alpha/beta/rc tags.
release = u'1.2-dev'

# General information about the project.
project = u'pyNastran' + u' ' + version
author = u'Steven Doyle'
copyright = u'2018, ' + author

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if on_rtd:
    #html_theme = 'default'
    html_theme = 'sphinx_rtd_theme'
else:
    # old
    #html_theme = 'napoleon' # classic/alabaster/numpydoc/napolean

    #extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.napoleon']

    # new
    # napolean is now called sphinx_rtd_theme

    if 0:
        html_theme = 'napolean' # classic/alabaster/numpydoc/sphinx_rtd_theme
        html_theme_path = []
    elif 0:
        html_theme = 'default'
    else:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme' # classic/alabaster/numpydoc/sphinx_rtd_theme
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    #html_theme = 'alabaster'

    # napolean handles mixed sphinx (alabaster) and numpydoc docstring formats

#print('html_theme =', html_theme)
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.

#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyNastrandoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    #'papersize': 'a4',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (master_doc, 'pyNastran.tex', u'pyNastran Documentation',
     u'Steven Doyle', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pynastran', u'pyNastran Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pyNastran', u'pyNastran Documentation',
     author, 'pyNastran', 'Nastran BDF/F06/OP2/OP4 '
     'File reader/editor/writer/viewer.', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'pyNastran'
epub_author = u'Steven Doyle'
epub_publisher = u'pyNastran'
epub_copyright = u'2018, Steven Doyle'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

def passer(app, what, name, obj, options, lines):
    pass

def purge_todos(app, env, docname):
    """http://www.sphinx-doc.org/en/stable/extdev/tutorial.html"""
    if not hasattr(env, 'todo_all_todos'):
        return
    env.todo_all_todos = [todo for todo in env.todo_all_todos
                          if todo['docname'] != docname]


exclusions = (
    '__weakref__',  # special-members
    '__doc__', '__module__', '__dict__',  # undoc-members
    '__builtins__', 'zip', 'range',
    '_field_map',

    'BDF_', 'AddMethods', 'WriteMesh', 'BDFMethods', 'BDFAttributes',
    'SafeXrefMesh', 'XrefMesh', 'GetMethods', 'AddCards', 'UnXrefMesh',

    'TestCoords',
    'TestNodes',
    'TestAero',
    'TestConstraints',
    'TestSets',
    'TestDEQATN',
    'TestDynamic',
    'TestRods',
    'TestBars',
    'TestBeams',
    'TestContact',
    'TestDMIG',
    'TestElements',
    'TestMassElements',
    'TestMethods',
    'TestNsm',
    'TestLoads',
    'TestMaterials',
    'TestOther',
    'TestOpt',
    'TestRigid',
    'TestSprings',
    'TestDampers',
    'TestSolids',
    'TestShells',
    'TestTables',
    'TestThermal',
    'TestAxi',

    'TestBdfUtils',
    'Testfield_writer_8',
    'TestBaseCard',
    'CaseControlTest',
    'TestMeshUtils',
    'TestConvert',
    'TestRenumber',
    'TestRemoveUnused',
    'TestMass',
    'TestLoadSum',
    'TestPatran',
    'TestReadWrite',
    'TestOpenMDAO',
    'TestAssignType',
    'DevUtils',

    'TestFastGUI',
    'TestNastranGUI',
    'TestUgridGui',
    'TestMsgMesh',

    '_make_card_parser',
    '_reduce_dload_case',
    '_reduce_load_case',
    '_parse_primary_file_header',
    '_set_pybdf_attributes',
    '_verify_bdf',
    '_verify',

    '_add_aecomp_object',
    '_add_aefact_object',
    '_add_aelink_object',
    '_add_aelist_object',
    '_add_aeparm_object',
    '_add_aero_object',
    '_add_aeros_object',
    '_add_aestat_object',
    '_add_aesurf_object',
    '_add_aesurfs_object',
    '_add_ao_object',
    '_add_aset_object',
    '_add_axic_object',
    '_add_bcrpara_object',
    '_add_bctadd_object',
    '_add_bctpara_object',
    '_add_bctset_object',
    '_add_bset_object',
    '_add_bsurf_object',
    '_add_bsurfs_object',
    '_add_caero_object',
    '_add_axif_object',
    '_add_baror_object',
    '_add_bconp_object',
    '_add_beamor_object',
    '_add_blseg_object',
    '_add_csuper_object',
    '_add_csupext_object',
    '_add_gridb_object',
    '_add_normal_object',
    '_add_radcav_object',
    '_add_radmtx_object',
    '_add_radset_object',
    '_add_ringfl_object',
    '_add_sebndry_object',
    '_add_sebulk_object',
    '_add_seconct_object',
    '_add_seelt_object',
    '_add_seexcld_object',
    '_add_selabel_object',
    '_add_seload_object',
    '_add_seloc_object',
    '_add_sempln_object',
    '_add_senqset_object',
    '_add_setree_object',
    '_add_view3d_object',
    '_add_view_object',
    '_add_card_hdf5',
    '_add_card_helper',
    '_add_card_helper_hdf5',
    '_add_cmethod_object',
    '_add_constraint_mpc_object',
    '_add_constraint_mpcadd_object',
    '_add_constraint_spc_object',
    '_add_constraint_spcadd_object',
    '_add_constraint_spcoff_object',
    '_add_convection_property_object'
    '_add_coord_object',
    '_add_creep_material_object',
    '_add_cset_object',
    '_add_csschd_object',
    '_add_damper_object',
    '_add_darea_object',
    '_add_dconstr_object',
    '_add_ddval_object',
    '_add_delay_object',
    '_add_deqatn_object',
    '_add_desvar_object',
    '_add_diverg_object',
    '_add_dlink_object',
    '_add_dload_entry',
    '_add_dload_object',
    '_add_dmi_object',
    '_add_dmig_object',
    '_add_dmij_object',
    '_add_dmiji_object',
    '_add_dmik_object',
    '_add_doptprm_object',
    '_add_dphase_object',
    '_add_dresp_object',
    '_add_dscreen_object',
    '_add_dtable_object',
    '_add_dti_object',
    '_add_dvcrel_object',
    '_add_dvgrid_object',
    '_add_dvmrel_object',
    '_add_dvprel_object',
    '_add_element_object',
    '_add_epoint_object',
    '_add_flfact_object',
    '_add_flutter_object',
    '_add_freq_object',
    '_add_gust_object',
    '_add_hyperelastic_material_object',
    '_add_load_combination_object',
    '_add_load_object',
    '_add_lseq_object',
    '_add_mass_object',
    '_add_material_dependence_object',
    '_add_method_object',
    '_add_mkaero_object',
    '_add_monpnt_object',
    '_add_nlparm_object',
    '_add_nlpci_object',
    '_add_node_object',
    '_add_nsm_object',
    '_add_nsmadd_object',
    '_add_nxstrat_object'
    '_add_omit_object',
    '_add_paero_object',
    '_add_param_object',
    '_add_pbusht_object',
    '_add_pdampt_object',
    '_add_pelast_object',
    '_add_phbdy_object',
    '_add_plotel_object',
    '_add_point_object',
    '_add_property_mass_object',
    '_add_property_object',
    '_add_qset_object',
    '_add_random_table_object',
    '_add_rigid_element_object',
    '_add_ringax_object',
    '_add_rotor_object',
    '_add_sebset_object',
    '_add_secset_object',
    '_add_seqgp_object',
    '_add_seqset_object',
    '_add_seset_object',
    '_add_sesuport_object',
    '_add_set_object',
    '_add_seuset_object',
    '_add_spline_object',
    '_add_spoint_object',
    '_add_structural_material_object',
    '_add_suport1_object',
    '_add_suport_object',
    '_add_table_object',
    '_add_table_sdamping_object',
    '_add_tabled_object',
    '_add_tablem_object',
    '_add_tempd_object',
    '_add_tf_object',
    '_add_thermal_bc_object',
    '_add_thermal_element_object',
    '_add_thermal_load_object',
    '_add_thermal_material_object',
    '_add_tic_object',
    '_add_trim_object',
    '_add_tstep_object',
    '_add_tstepnl_object',
    '_add_uset_object',
    '_add_convection_property_object',
    '_add_coord_object',
    '_add_nxstrat_object',
    '_add_omit_object',

    '_cross_reference_aero',
    '_cross_reference_constraints',
    '_cross_reference_coordinates',
    '_cross_reference_elements',
    '_cross_reference_loads',
    '_cross_reference_masses',
    '_cross_reference_materials',
    '_cross_reference_nodes',
    '_cross_reference_nodes_with_elements',
    '_cross_reference_optimization',
    '_cross_reference_properties',
    '_cross_reference_sets',
    '_find_aero_location',
    '_get_bdf_stats_loads',
    '_get_card_name',
    '_get_coords_to_update',

    '_uncross_reference_aero',
    '_uncross_reference_constraints'
    '_uncross_reference_coords',
    '_uncross_reference_elements',
    '_uncross_reference_loads',
    '_uncross_reference_masses',
    '_uncross_reference_materials',
    '_uncross_reference_nodes',
    '_uncross_reference_optimization',
    '_uncross_reference_properties',
    '_uncross_reference_sets',
    '_uncross_reference_constraints',
    '_uncross_reference_coords',

    '_prepare_bctset',
    '_prepare_cdamp4',
    '_prepare_chexa',
    '_prepare_cmass4',
    '_prepare_conv',
    '_prepare_convm',
    '_prepare_cord1c',
    '_prepare_cord1r',
    '_prepare_cord1s',
    '_prepare_cpenta',
    '_prepare_cpyram',
    '_prepare_ctetra',
    '_prepare_dequatn',
    '_prepare_dmi',
    '_prepare_dmig',
    '_prepare_dmij',
    '_prepare_dmiji',
    '_prepare_dmik',
    '_prepare_dmix',
    '_prepare_dti',
    '_prepare_grdset',
    '_prepare_nsm',
    '_prepare_nsml',
    '_prepare_pdamp',
    '_prepare_pelas',
    '_prepare_pmass',
    '_prepare_pvisc',
    '_prepare_radbc',
    '_prepare_radm',
    '_prepare_tempax',
    '_prepare_tempd',
    '_format_comment',
    '_parse_pynastran_header',
    '_node_ids',
    '_update_field_helper',
    '_is_same_fields',
    '_get_field_helper',
    '_test_update_fields',
    '_clean_comment',
    '_clean_comment_bulk',
    '_parse_pynastran_header',
    '_prep_comment',
    '_get_dvprel_ndarrays',
    '_get_forces_moments_array',
    '_get_maps',
    '_get_npoints_nids_allnids',
    '_get_rigid',
    '_get_temperatures_array',
    '_mass_properties_new',
    '_output_helper',
    '_parse_cards',
    '_parse_cards_hdf5',
    '_parse_dynamic_syntax',
    '_read_bdf_cards',
    '_read_bdf_helper',
    '_reset_type_to_slot_map',
    '_safe_cross_reference_aero',
    '_safe_cross_reference_constraints',
    '_safe_cross_reference_elements',
    '_safe_cross_reference_loads',
    '_transform',
    '_write_aero',
    '_write_aero_control',
    '_write_case_control_deck',
    '_write_common',
    '_write_constraints',
    '_write_contact',
    '_write_coords',
    '_write_dloads',
    '_write_dmigs',
    '_write_dynamic',
    '_write_elements',
    '_write_elements_interspersed',
    '_write_executive_control_deck',
    '_write_flutter',
    '_write_grids',
    '_write_gust',
    '_write_header',
    '_write_loads',
    '_write_masses',
    '_write_materials',
    '_write_nodes',
    '_write_nsm',
    '_write_optimization',
    '_write_params',
    '_write_properties',
    '_write_reject_message',
    '_write_rejects',
    '_write_rigid_elements',
    '_write_sets',
    '_write_static_aero',
    '_write_superelements',
    '_write_tables',
    '_write_thermal',
    '_write_thermal_materials',

    '_eq_nodes_build_tree',
    '_eq_nodes_find_pairs',
    '_eq_nodes_setup',
    '_transform_node_to_global_array',
    '_transform_node_to_local',
    '_transform_node_to_local_array',
    'transform_node_from_local_to_local',
    'transform_node_from_local_to_local_array',
    'transform_node_to_global',
    'transform_node_to_global_assuming_rectangular',
    'transform_node_to_global_no_xref',
    'transform_node_to_local',
    'transform_node_to_local_array',
    'transform_vector_to_global',
    'transform_vector_to_global_array',
    'transform_vector_to_global_assuming_rectangular',
    'transform_vector_to_global_no_xref',
    'transform_vector_to_local',

    'add_op2_data',
    'deprecated',
    '_add_column',
    '_add_column_uaccel',
    '_get_dtype',
    '_reset_indices',
    '_write_sort1_as_sort1',
    '_write_sort1_as_sort2',
    '_write_sort2_as_sort1',
    '_write_sort2_as_sort2',
    'OP2Common', 'Op2Codes', 'F06Writer', 'OP2_Scalar',
    'deprecated',
    'print_raw_card',
    'print_repr_card',
    'TestF06Formatting',
    '_parse_results',
    '_read_inviscid_pressure',
    '_fill_abaqus_case',
    'add_sort1',
    'add_sort2',
    'add_new_transient',
)

def maybe_skip_member(app, what, name, obj, skip, options):
    exclude = name in exclusions
    if not on_rtd and not exclude:
        #print(app, what, name, obj, skip, options)
        print(what, name, obj, skip, options)
    return skip or exclude

def setup(app):
    app.connect('autodoc-process-docstring', passer)
    app.connect('env-purge-doc', purge_todos)
    app.connect('autodoc-skip-member', maybe_skip_member)
