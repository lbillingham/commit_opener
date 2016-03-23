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
* Documentation: https://commit_opener.readthedocs.org.

Features
--------

* Scrapes your local `git` repository to find who committed what and when
* Finds the dependencies of the code in your master branch
* Searches literature databases for mentions of your software

* Saves all the results to `JSON`

* TODO
1. Plugin to [depsy](depsy.org) to expose results
2. Support the `import` scraping for languages other than python

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
