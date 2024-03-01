keep_github_workflows_active
============================


Version v1.1.0 as of 2024-03-01 see `Changelog`_

|build_badge| |codeql| |license| |jupyter| |pypi|
|pypi-downloads| |black| |codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/keep_github_workflows_active/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/keep_github_workflows_active/actions/workflows/python-package.yml


.. |codeql| image:: https://github.com/bitranox/keep_github_workflows_active/actions/workflows/codeql-analysis.yml/badge.svg?event=push
   :target: https://github.com//bitranox/keep_github_workflows_active/actions/workflows/codeql-analysis.yml

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/keep_github_workflows_active/master?filepath=keep_github_workflows_active.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/keep-github-workflows-active?label=PyPI%20Package
   :target: https://badge.fury.io/py/keep_github_workflows_active

.. badge until 2023-10-08:
.. https://img.shields.io/codecov/c/github/bitranox/keep_github_workflows_active
.. badge from 2023-10-08:
.. |codecov| image:: https://codecov.io/gh/bitranox/keep_github_workflows_active/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/keep_github_workflows_active

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/keep_github_workflows_active?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/keep_github_workflows_active/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/keep_github_workflows_active?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/keep_github_workflows_active/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/keep_github_workflows_active?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/keep_github_workflows_active/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://snyk.io/test/github/bitranox/keep_github_workflows_active/badge.svg
   :target: https://snyk.io/test/github/bitranox/keep_github_workflows_active

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/keep-github-workflows-active
   :target: https://pypi.org/project/keep-github-workflows-active/
   :alt: PyPI - Downloads

GitHub Workflow Management Script
==================================

This manual guides you through the execution of a Python script designed to manage GitHub workflows across all repositories of a user. The script performs two main functions:

1. **Keep All Workflows Active**: Ensures that all workflows in each repository of the user remain in an active state.

2. **Delete Old Workflow Runs**: For each repository, this function retains a specified number of the most recent workflow runs and deletes all older runs.


Access Key
-----------

In order to access the repository workflows, you will need a fine-grained personal test token. Follow the link to generate the token:

- [Generate Fine-Grained Personal Test Token](https://github.com/settings/personal-access-tokens)

Permissions
~~~~~~~~~~~

Ensure the access key has the following permissions:

- Action: Read/Write
- Metadata: Read

Test Token Details
------------------

The current test token is valid until 2025-01-19 and needs to be renewed annually.


Token Storage for testing
-------------------------

The token is stored as a secret in the repository's "repository secrets." Navigate to the following link to manage repository secrets:

- [Repository Secrets](https://github.com/bitranox/keep_github_workflows_active/settings/secrets/actions)

Secrets Information
~~~~~~~~~~~~~~~~~~~

The following secrets need to be set:

- `SECRET_GITHUB_OWNER`: the GitHub username
- `SECRET_GITHUB_TOKEN`: The fine-grained access key

----

automated tests, Github Actions, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.8.0 or newer

tested on recent linux with python 3.12 - architectures: amd64

`100% code coverage <https://codeclimate.com/github/bitranox/keep_github_workflows_active/test_coverage>`_, flake8 style checking ,mypy static type checking ,tested under `Linux <https://github.com/bitranox/keep_github_workflows_active/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/keep_github_workflows_active/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/keep_github_workflows_active/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/keep_github_workflows_active/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=keep_github_workflows_active.ipynb>`_

Usage
-----------

- example for including docstrings

.. code-block:: text

    def main() -> None:
        """
        enable all workflows in all repositories for the given owner
        >>> # we actually don't do that here AGAIN because of GitHub Rate limits
        >>> # those functions are called anyway already by doctest
        >>> # main()

        """

Usage from Commandline
------------------------

.. code-block::

   Usage: keep_github_workflows_active [OPTIONS] COMMAND [ARGS]...

     keep gitgub workflows active

   Options:
     --version                     Show the version and exit.
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

   Commands:
     info  get program informations

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip:


.. code-block::

    python -m pip --upgrade pip

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade keep_github_workflows_active


- to install the latest release from PyPi via pip, including test dependencies:

.. code-block::

    python -m pip install --upgrade keep_github_workflows_active[test]

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/keep_github_workflows_active.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    keep_github_workflows_active

    # for the latest development version :
    keep_github_workflows_active @ git+https://github.com/bitranox/keep_github_workflows_active.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version, including test dependencies from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/keep_github_workflows_active.git
    $ cd keep_github_workflows_active
    python -m pip install -e .[test]

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/keep_github_workflows_active.git
    $ cd keep_github_workflows_active

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    cli_exit_tools
    lib_detect_testenv
    lib_log_utils
    toml
    requests

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/keep_github_workflows_active/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes


v1.1.0
--------
2024-02-29:
    - disable windows and osx tests to avoid hitting API limits
    - omit mypy option --no-implicit-reexport
    - github actions/checkout@v4
    - github actions/setup-python@v5
    - use requests instead of urllib
    - delete old Workflow runs

v1.0.0
--------
2024-01-20: initial release

