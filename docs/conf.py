# conf.py – Konfigurationsdatei für Sphinx
import os
import sys
# Falls du Zugriff auf deine Integration benötigst:
sys.path.insert(0, os.path.abspath('../custom_components/divera247'))

# -- Projektinformationen -----------------------------------------------------
project = 'Divera 24/7 Home Assistant Integration'
author = 'Loony2392'
copyright = '2025, Loony2392'
# Versionen
release = '1.0.0'

# -- Allgemeine Konfiguration -------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Für Google- oder NumPy-Style Docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# -- Optionen für HTML-Ausgabe ------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
