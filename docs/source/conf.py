# SPDX-License-Identifier: GPL-3.0-or-later
# Configuration file for the Sphinx documentation builder.

import os
import sys
import subprocess
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'mag-xiao-s3'
author = 'David Witten and contributors'
current_year = str(datetime.now().year)
copyright = f"{current_year}, {author}"

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'breathe',
]

myst_enable_extensions = [
    'colon_fence',
    'substitution',
]

# Templates path
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']

# -- Doxygen / Breathe integration ------------------------------------------
# Try to run Doxygen to generate XML for Breathe if available.
this_dir = os.path.abspath(os.path.dirname(__file__))
repo_root = os.path.abspath(os.path.join(this_dir, '..', '..'))
doxyfile_path = os.path.join(repo_root, 'Doxyfile')
doxygen_out = os.path.join(repo_root, 'docs', 'doxygen')

if os.path.exists(doxyfile_path):
    try:
        subprocess.run(['doxygen', doxyfile_path], check=False)
    except Exception:
        # Silently ignore in local builds without doxygen
        pass

breathe_projects = {
    'mag-xiao-s3': os.path.join(doxygen_out, 'xml')
}
breathe_default_project = 'mag-xiao-s3'
