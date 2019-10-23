import sys

project = 'aiosteamworksweb'
# noinspection PyShadowingBuiltins
copyright = '2019, insurgency.gg'
author = 'insurgency.gg'
extensions = [
    'sphinx.ext.autodoc',
    # See: https://github.com/agronholm/sphinx-autodoc-typehints#installation-and-setup
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
intersphinx_mapping = {
    'py': ('https://docs.python.org/{0.major}.{0.minor}'.format(sys.version_info), None),
}
autodoc_member_order = 'bysource'

