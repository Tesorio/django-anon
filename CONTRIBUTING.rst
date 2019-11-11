Contributing to django-anon
###########################

As an open source project, **django-anon** welcomes contributions of many forms.

Examples of contributions include:

* Code patches
* Documentation improvements
* Bug reports and code reviews


Table of Contents
#################

.. contents::
   :local:
   

Code of conduct
===============

Please keep the tone polite & professional. First impressions count, so let's try to make everyone feel welcome.

Be mindful in the language you choose. As an example, in an environment that is heavily male-dominated, posts that start 'Hey guys,' can come across as unintentionally exclusive. It's just as easy, and more inclusive to use gender neutral language in those situations. (e.g. 'Hey folks,')

The `Django code of conduct <https://www.djangoproject.com/conduct/>`_ gives a fuller set of guidelines for participating in community forums.


Issues
======

Some tips on good issue reporting:

* When describing issues try to phrase your ticket in terms of the behavior you think needs changing rather than the code you think need changing.
* Search the issue list first for related items, and make sure you're running the latest version of **django-anon** before reporting an issue.
* If reporting a bug, then try to include a pull request with a failing test case. This will help us quickly identify if there is a valid issue, and make sure that it gets fixed more quickly if there is one.
* Closing an issue doesn't necessarily mean the end of a discussion. If you believe your issue has been closed incorrectly, explain why and we'll consider if it needs to be reopened.


Development
===========

To start developing on **django-anon**, clone the repo:

.. code::

   git clone https://github.com/Tesorio/django-anon

Changes should broadly follow the PEP 8 style conventions, and we recommend you set up your editor to automatically indicate non-conforming styles.


Coding Style
============

`The Black code style <https://github.com/psf/black#the-black-code-style>`_ is used across the whole codebase. Ideally, you should configure your editor to auto format the code. This means you can use **88 characters per line**, rather than 79 as defined by PEP 8.

Use `isort` to automate import sorting using the guidelines below:

* Put imports in these groups: future, stdlib, deps, local
* Sort lines in each group alphabetically by the full module name
* On each line, alphabetize the items with the upper case items grouped before the lowercase items

Don't be afraid, all specifications for linters are defined in ``pyproject.toml`` and ``.flake8``


Testing
=======

To run the tests, clone the repository, and then:

.. code::

   # Setup the virtual environment
   python3 -m venv env
   source env/bin/activate
   pip install django
   pip install -r tests/requirements.txt

   # Run the tests
   ./runtests.py


Running against multiple environments
=====================================

You can also use the excellent tox testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

.. code::

   tox


Using pre-commit hook
=====================

CI will perform some checks during the build, but to save time, most of the checks can be ran locally beforing pushing code. To do this, we use `pre-commit <https://pre-commit.com/#install>`_ hooks. All you need to do, is to install and configure pre-commit:

.. code:: bash

   pre-commit install --hook-type pre-push -f


Pull requests
=============

It's a good idea to make pull requests early on. A pull request represents the start of a discussion, and doesn't necessarily need to be the final, finished submission.

It's also always best to make a new branch before starting work on a pull request. This means that you'll be able to later switch back to working on another separate issue without interfering with an ongoing pull requests.

It's also useful to remember that if you have an outstanding pull request then pushing new commits to your GitHub repo will also automatically update the pull requests.

GitHub's documentation for working on pull requests is `available here. <https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests>`_

Always run the tests before submitting pull requests, and ideally run tox in order to check that your modifications are compatible on all supported versions of Python and Django.

Once you've made a pull request take a look at the CircleCI build status and make sure the tests are running as you'd expect.


Documentation
=============

**django-anon** uses the Sphinx documentation system and is built from the ``.rst`` source files in the ``docs/`` directory.

To build the documentation locally, install Sphinx:

.. code::

   pip install Sphinx
   
Then from the ``docs/`` directory, build the HTML:

.. code::

   make html
   
To get started contributing, you’ll want to read the `reStructuredText reference. <http://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html#rst-index>`_


Language style
==============

Documentation should be in American English. The tone of the documentation is very important - try to stick to a simple, plain, objective and well-balanced style where possible.

Some other tips:

* Keep paragraphs reasonably short.
* Don't use abbreviations such as 'e.g.' but instead use the long form, such as 'For example'.


References
==========

* https://github.com/encode/django-rest-framework/blob/master/CONTRIBUTING.md
* https://docs.djangoproject.com/en/dev/internals/contributing/
