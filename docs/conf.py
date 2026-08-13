# conf.py – Sphinx configuration file
import json
import os
import sys

# Anchor on this file, not the cwd: sphinx-build is invoked from the repo root
# in CI, so a cwd-relative path resolves outside the repository.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# sphinx-apidoc documents the modules as "divera247.<name>", so the package's
# parent directory goes on the path -- not the package directory itself.
sys.path.insert(0, os.path.join(_REPO_ROOT, "custom_components"))
# coordinator.py and data.py import via the absolute "custom_components.*"
# path, which only resolves at runtime because Home Assistant puts the config
# directory on sys.path. Add the repo root so those imports resolve here too.
sys.path.insert(0, _REPO_ROOT)

# -- Project information -----------------------------------------------------
project = "Divera 24/7 Home Assistant Integration"
author = "Loony2392"
copyright = "2025, Loony2392"
# The full version, including alpha/beta/rc tags. Single source of truth is the
# integration manifest, so the docs cannot drift from the released version.
with open(
    os.path.join(_REPO_ROOT, "custom_components", "divera247", "manifest.json"),
    encoding="utf-8",
) as _manifest:
    release = json.load(_manifest)["version"]

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # For Google- or NumPy-style docstrings
]

# Home Assistant and the async HTTP stack are not installed in the docs
# environment; mock them so autodoc can import the integration modules.
autodoc_mock_imports = [
    "aiohttp",
    "homeassistant",
    "voluptuous",
    "yarl",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

# -- Internationalization (i18n) settings ------------------------------------
# Set the default language for the documentation.
language = "de"

# Specify the directory where the translation files (.po and .mo) are stored.
locale_dirs = ["locale/"]  # Relative to this conf.py file
