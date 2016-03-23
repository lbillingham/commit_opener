#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [GitPython, git-pandas, numpy, pandas, click, sphinx, flake, sphinx]
test_requirements = [pytest, tox]

setup(
    name='commit_opener',
    version='0.1.0',
    description="let people see your contributions, even if you can't open-source them",
    long_description=readme + '\n\n' + history,
    author="Laurence Billingham",
    author_email='laurence@bgs.ac.uk',
    url='https://github.com/lbillingham/commit_opener',
    packages=[
        'commit_opener',
    ],
    package_dir={'commit_opener':
                 'commit_opener'},
    include_package_data=True,
    install_requires=requirements,
    license="GPL",
    zip_safe=False,
    keywords='commit_opener',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
