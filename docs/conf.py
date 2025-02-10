# conf.py – Sphinx configuration file
import os
import sys
# If you need access to your integration:
sys.path.insert(0, os.path.abspath('../custom_components/divera247'))

# -- Project information -----------------------------------------------------
project = 'Divera 24/7 Home Assistant Integration'
author = 'Loony2392'
copyright = '2025, Loony2392'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google- or NumPy-style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Internationalization (i18n) settings ------------------------------------
# Set the default language for the documentation.
language = 'de'

# Specify the directory where the translation files (.po and .mo) are stored.
locale_dirs = ['locale/']  # Relative to this conf.py file
gettext_compact = False    # Prevents all translations from being merged into a single file
