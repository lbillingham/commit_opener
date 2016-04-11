===============================
commit_opener
===============================

We have open access research papers and open data.
Open source research software is coming next.
However, it is going to take time before we can all open-source our contributions.

In the meantime, `commit_opener` lets the world see your contributions, even if
we can't see your code.

It also gives credit to the open-source authors whose code you use.


* Free software: GPL license
* Documentation: will be at https://commit_opener.readthedocs.org.

Features
--------

* Command line app
* Scrapes your local `git` repository to find who committed what and when
* Finds the dependencies of the code in your master branch
* Searches literature databases for mentions of your software

* Saves all the results to `JSON`

TODO
----
1. Plugin to [depsy](depsy.org) to expose results
2. Support the `import` scraping for languages other than python
3. Work with `svn` and other repos
4. Find a better metric than commits.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


Notes for use on windows with `conda`
------------------
need to have both `git` and `pandas` installed. Pandas is a pain to install
on windows without `conda`, `conda` does not play very nicely with [git bash](https://github.com/conda/conda/issues/747)
```shell
# in windows `cmd.exe`
mkdir commit_opener
git clone git@github.com:lbillingham/commit_opener.git ./commit_opener
conda create -n commit_opener_env pandas
 ```
```shell
# in `git.bash`
cd commit_opener
export PATH=/c/Users/laurence/AppData/Local/Continuum/Anaconda3/envs/commit_opener_env:$PATH
export PATH=/c/Users/laurence/AppData/Local/Continuum/Anaconda3/envs/commit_opener_env/Scripts:$PATH
python setup.py install
##########
cd /c/tmp
git clone git@github.com:Turbo87/utm
commit_opener --repo ./utm
```
