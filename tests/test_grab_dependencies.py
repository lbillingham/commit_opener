#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_commit_opener
----------------------------------

Tests for `commit_opener` module.
"""

import commit_opener.grab_dependencies as co_grab


def test_import_search(self):
    text = """
import os
import scipy
import pandas
from numpy import something
import matplotlib.pyplot as plt
"""
    expected = ['os', 'scipy', 'numpy', 'matplotlib']
    assert expected == co_grab.find_imports(text)
    
def test_commented(self):
    text = """
import os
#import scipy
"""
    expected = ['os']
    assert expected == co_grab.find_imports(text)
    
def test_indented(self):
    text = """
import os
import scipy
"""
    expected = ['os']
    assert expected == find_imports(text)
    