# This file is here for compatibility because the
# theme changed his name to pdsback_theme

"""Docs Italia theme"""

import os

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__) + '../pdsback_theme')
    return cur_dir

def setup(app):
    pass
