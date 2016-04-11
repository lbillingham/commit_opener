===============================
commit_opener
===============================

We have open access research papers and open data.
Open source research software is coming next.
However, it is going to take time before we can all open-source our contributions.

In the meantime, :code:`commit_opener` lets the world see your contributions, even if
we can't see your code.

It also gives credit to the open-source authors whose code you use.


* Free software: GPL license
* Documentation: will be at https://commit_opener.readthedocs.org.

Features
--------

* Command line app
* Scrapes your local :code:`git` repository to find who committed what and when
* Finds the dependencies of the code in your master branch
* Searches literature databases for mentions of your software

* Saves all the results to `JSON`

TODO
----
1. Plugin to [depsy](depsy.org) to expose results
2. Support the :code:`import` scraping for languages other than python
3. Work with :code:`svn` and other repos
4. Find a better metric than commits.


Notes for use on windows with `conda` and `git-bash`
----------------------------------------------------
need to have both :code:`git` and :code:`pandas` installed. Pandas is a pain to
install on windows without :code:`conda`,
:code:`conda` does not play very nicely with
`git bash <https://github.com/conda/conda/issues/747>`_.


make a conda environment:
:code:`pandas` (probably :code:`numpy.sclapak`, actually)
and normal `virtualenv` do not play too happily together on windows.

.. code-block:: bat

   REM in windows `cmd.exe`
    mkdir commit_opener
    conda create -n commit_opener_env pandas
    activate commit_opener_env
    echo %CONDA_DEFAULT_ENV%



if :code:`git` is  not integrated into :code:`cmd.exe`,
we mush switch to using a :code:`git` aware shell
before installing :code:`commit_opener` into the :code:`conda env`.
Note the output of :code:`echo %CONDA_DEFAULT_ENV`
from the :code:`cmd.exe` step above.

.. code-block:: bash

   # in `git.bash`
    CONDA_ENV_HOME=<output of echo %CONDA_DEFAULT_ENV% from above>
    cd commit_opener
    git clone git@github.com:lbillingham/commit_opener.git ./commit_opener
    PRE_CONDA_PATH=$PATH
    export PATH=$CONDA_ENV_HOME:$PATH
    export PATH=$CONDA_ENV_HOME/Scripts:$PATH
    python setup.py install
    # run the `commit_opener` we just installed
    cd /c/tmp
    git clone git@github.com:Turbo87/utm
    commit_opener --repo ./utm
    export PATH=$PRE_CONDA_PATH


to uninstall

.. code-block:: bash

   # in `git.bash`
    cd commit_opener
    PRE_CONDA_PATH=$PATH
    export PATH=/c/Users/laurence/AppData/Local/Continuum/Anaconda3/envs/commit_opener_env:$PATH
    python setup.py --dry-run --record files.txt
    cat files.txt | sed 's/\\/\//g' | sed 's/['Cc']:/\/c/' | xargs rm -rf
    export PATH=$PRE_CONDA_PATH

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
