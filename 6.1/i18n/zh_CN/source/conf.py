# -*- coding: utf-8 -*-

import sys, os
from docutils import nodes

# openobject-doc documentation build configuration file, created by
# sphinx-quickstart on Tue Dec  9 11:16:22 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.

# WARNING: if you want to generate the OpenERP ORM docstrings
# you need to make sure that OpenERP server is in the python path
# by setting a PYTHONPATH environment variable containing the path
# to the server's 'bin' directory, or by explicitly adding it below.
# sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
  'sphinx.ext.todo',
  'sphinx.ext.ifconfig',
  'sphinx.ext.autodoc'
]
todo_include_todos = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '6.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d %H:%M:%S'

# List of documents that shouldn't be included in the build.
unused_docs = [
  'contribute/10_irc_meeting', #Out of date? IRC meetings not held anymore?
  'contribute/summary_of_ressources',
  'customize/index', #empty
  'developer/17_Web_services/index', #Should be merged with 6_21_web_services?
  'developer/7_School/index',
  'features/example',
  'features/repairs',
  'install/windows/allinone',
]

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = [
   #'bi',
   #'book',
   #'customize',
   #'install',
   #'contribute',
   #'developer',
   #'features',
   #'exercice',
   #'technical_guide',
   'verticalisations',
   'developer/old_dev', # Tmp fix while refactoring dev book
]

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

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'OpenERP v6'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.

html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'openobject-doc'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '9pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
#latex_documents = [
#  ('index', 'openobject-doc.tex', ur'openobject Documentation',
#   ur'OpenObject Community', 'manual'),
#]

latex_documents = [
   ('book/index', 'openerp-book.tex', ur'Open ERP, a modern approach to integrated business management', ur'Fabien Pinckaers\\Geoff Gardiner\\Els Van Vossel', 'manual'),
   #('bi/index', 'openobject-bi.tex', ur'Open Object Business Intelligence', ur'OpenERP SA', 'manual'),
   #('customize', 'openobject-customize.tex', ur'Open Object Customization Book', ur'OpenERP SA', 'manual'),
   ('install/index', 'openobject-install.tex', ur'Open Object Installation Manuals', ur'OpenERP SA', 'manual'),
   #('contribute/index', 'openobject-contribute.tex', ur'Open Object Community Book', ur'OpenERP SA', 'manual'),
   ('developer/index', 'openobject-developer.tex', ur'Open Object Developer Book', ur'OpenERP SA', 'manual'),
   #('features/index', 'openobject-features.tex', ur'Open ERP Features', ur'OpenERP SA', 'manual'),
   #('verticalisations', 'openobject-verticalisations.tex', ur'Open Object verticalisations', ur'OpenERP SA', 'manual'),
   ('technical_guide/index', 'openobject-technical_guide.tex', ur'Open Object Technical Guide', ur'OpenERP SA', 'manual'),
   ('training_material/user_training/v5/exercises/index', 'openerp-user-training-v5-exercises.tex', ur'User Training - Exercises', ur'OpenERP', 'howto'),
   ('training_material/user_training/v5/solutions/index', 'openerp-user-training-v5-solutions.tex', ur'User Training - Solutions', ur'OpenERP', 'howto'),
   #('training_material/user_training/v6/exercises/index', 'openerp-user-training-v6-exercises.tex', ur'User Training - Exercises', ur'OpenERP', 'howto'),
   #('training_material/user_training/v6/solutions/index', 'openerp-user-training-v6-solutions.tex', ur'User Training - Solutions', ur'OpenERP', 'howto'),
   #('training_material/technical_training/v5/exercises/index', 'openerp-technical-training-v5-exercises.tex', ur'Technical Training - Exercises', ur'OpenERP', 'howto'),
   #('training_material/technical_training/v5/solutions/index', 'openerp-technical-training-v5-solutions.tex', ur'Technical Training - Solutions', ur'OpenERP', 'howto'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '.static/openerp.jpg'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# Additional stuff for the LaTeX preamble.
#latex_preamble = '' # DEPRECATED sinc sphinx 0.5 (use 'latex_elements')

tiny_latex_include = r"""
\usepackage{flowfram}

\DeclareUnicodeCharacter{00A0}{~}

\definecolor{MyGray}{rgb}{0.80,0.80,0.80}

\makeatletter\newenvironment{graybox}{%
   \begin{lrbox}{\@tempboxa}\begin{minipage}{\columnwidth}}{\end{minipage}\end{lrbox}%
   \colorbox{MyGray}{\usebox{\@tempboxa}}
}\makeatother

\makeatletter
\renewenvironment{notice}[2]{
  \begin{graybox}
  \bf\it
  \def\py@noticetype{#1}
  \par\strong{#2}
  \csname py@noticestart@#1\endcsname
}
{
  \csname py@noticeend@\py@noticetype\endcsname
  \end{graybox}
}
\makeatother

\renewenvironment{figure}[6]{
  \begin{staticfigure}
}{
  \end{staticfigure}
}

%% Stupid workaround for stuff that is defined in howto.cls but
%% overwritten by sphinx.sty!!

\makeatletter
%\let\py@OldTableofcontents=\tableofcontents
\renewcommand{\tableofcontents}{
  \begingroup
    \parskip = 0mm
    \py@OldTableofcontents
  \endgroup
  \newpage
  %\rule{\textwidth}{1pt}
  %\vspace{12pt}
}
\makeatother

\pagestyle{plain}
\pagenumbering{arabic}
\thispagestyle{empty}

"""

latex_elements = {
    'preamble': tiny_latex_include,
    'papersize': 'a4paper',
}

# Documents to append as an appendix to all manuals.
#latex_appendices = ['doc_copyright.rst']

# If false, no module index is generated.
#latex_use_modindex = True

def end_foreword_directive(name, arguments, options, content, lineno,
                           content_offset, block_text, state, state_machine):
    return [nodes.Text('')]

def begin_conclusion_directive(name, arguments, options, content, lineno,
                               content_offset, block_text, state, state_machine):
    return [nodes.Text('')]

# add js-kit comments or not
# Disabled by ODO on 2012-10-22 as Echo service as been discontinued, and comments
# were rarely useful anyhow
js_kit_comments = False

def setup(app):
    from sphinx import __version__
    revisions = map(lambda x: x.isdigit() and int(x) or 0, __version__.split('.'))
    major, minor = revisions[0], revisions[1]
    if major*10+minor < 6:
        raise Exception("You should upgrade Sphinx to version 0.6 or higher")

    from sphinx.writers.html import HTMLTranslator, BaseTranslator
    import pickle

    # load unique_path dict:
    comments_path_pickle_filename = "comments_path.pickle"
    if os.path.exists(comments_path_pickle_filename):
        comments_path_pickle_file = open(comments_path_pickle_filename, 'r')
        comments_path_dict = pickle.load(comments_path_pickle_file)
        comments_path_pickle_file.close()
    else:
        comments_path_dict = {}
    this_build_comments_path_dict = {}

    def save_comments_path_dict():
        comments_path_pickle_file = open(comments_path_pickle_filename, 'w')
        pickle.dump(comments_path_dict, comments_path_pickle_file)
        comments_path_pickle_file.close()

    import atexit
    atexit.register(save_comments_path_dict)

    def depart_title_new(self, node):
        res = old_depart_title(self, node) # call the original depart_title.

        if self.builder.globalcontext.get('builder') == 'html':
            parent_class_name = node.parent.__class__.__name__
            if parent_class_name == 'section' and self.section_level == 2:
                title_id = "/" + node.parent.attributes['ids'][0]
                link_anchor = "#" + node.parent.attributes['ids'][0]
                ## paths should be unique:
                ## -> build a database (pickled dict) with already used paths and
                ## create a new unique path if already used.
                title_path = self.document['source']
                path_start = title_path.find('%ssource%s' % (os.sep, os.sep))
                title_path = title_path[path_start+8:].replace('.rst', '')

                if title_id not in this_build_comments_path_dict: # first time we process this path
                    title_id = comments_path_dict.get(title_id, title_id)
                    this_build_comments_path_dict[title_id] = title_id
                    comments_path_dict[title_id] = title_id
                else: # it's a double
                    title_id = u"""/%s%s""" % (title_path, title_id, )
                    this_build_comments_path_dict[title_id] = title_id
                    comments_path_dict[title_id] = title_id

                # we need a uniq attribute that never changes, but the permalink will be computed after rendering
                # the page so we can figure out the final URL, up to the correct anchor (Echo generates a default
                # permalink using the document.location if it's missing, but that will cause twitter post etc. to
                # appear on each section, as it is not able to distinguish sections on the same page!
                # See http://wiki.js-kit.com/Echo+-+Install+-+A+custom+website#Settinguptheuniqandpermalinkattributes
                # See the runtime computation in source/.templates/layout.html
                self.body.append(u"""<div class="js-kit-comments" uniq="%s" permalink_anchor="%s" ></div>""" % (title_id, link_anchor))

        return res

    if js_kit_comments:
        old_depart_title = HTMLTranslator.depart_title
        HTMLTranslator.depart_title = depart_title_new

    app.add_directive('end_foreword', end_foreword_directive, 1, (0, 0, 0))
    app.add_directive('begin_conclusion', begin_conclusion_directive, 1, (0, 0, 0))

