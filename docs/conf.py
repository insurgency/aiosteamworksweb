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
    'sphinx.ext.extlinks',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
intersphinx_mapping = {
    'py': ('https://docs.python.org/{0.major}.{0.minor}'.format(sys.version_info), None),
    'aiohttp': ('https://docs.aiohttp.org/en/stable/', None),
    'yarl': ('https://yarl.rtfd.io/en/stable/', None),
}
autodoc_member_order = 'bysource'
extlinks = {
    'github-branch': (f'https://github.com/insurgency/{project}/tree/branches/%s', 'name'),
    'issue': (f'https://github.com/insurgency/{project}/issues/%s', 'gh-'),
    'valve-wiki': ('https://developer.valvesoftware.com/wiki/%s', 'page'),
    'wikipedia': ('https://wikipedia.org/wiki/%s', 'page'),
    'steam-app': ('https://store.steampowered.com/app/%s', 'app-id')
}
