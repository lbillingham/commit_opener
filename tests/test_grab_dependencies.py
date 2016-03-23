#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_commit_opener
----------------------------------

Tests for `commit_opener` module.
"""

import commit_opener.grab_dependencies as co_grab


def test_import_search():
    text = """
import os
import scipy
import pandas
from numpy import something
import matplotlib.pyplot as plt
"""
    # Ordering matters here. Normal imports done first, then froms.
    expected = ['os', 'scipy', 'pandas', 'matplotlib', 'numpy']
    assert expected == co_grab.find_imports(text)
    
def test_commented():
    text = """
import os
#import scipy
"""
    expected = ['os']
    assert expected == co_grab.find_imports(text)
    
def test_indented():
    text = """
import os
    import scipy
"""
    expected = ['os', 'scipy']
    assert expected == co_grab.find_imports(text)
    
