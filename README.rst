===========================
Cookiecutter Django Package
===========================

An opinionated Cookiecutter_ template for creating reusable Django packages (installable apps) quickly.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Features
--------

* Uses Pipenv_ to manage dependencies and environments.
* Tox_ setup compatible with Pipenv.
* Travix-CI_ configuration compatible with Tox.
* Sphinx_ documentation template.
* Code Coverage_ measured.
* `BSD Clear License`_.
* Creates example project for quick development.

.. _Pipenv: https://docs.pipenv.org/
.. _Tox: https://tox.readthedocs.io/
.. _Travix-CI: https://travis-ci.org/
.. _Sphinx: http://www.sphinx-doc.org/
.. _Coverage: http://coverage.readthedocs.io/
.. _BSD Clear License: https://choosealicense.com/licenses/bsd-3-clause-clear/

Usage
-----
.. code-block:: console

    $ git clone https://github.com/jmfederico/cookiecutter-djangopackage.git
    $ cd cookiecutter-djangopackage
    $ pip install pipenv
    $ pipenv install
    $ pipenv run cookiecutter .

Now you can develop you app.

Releasing on PyPI
~~~~~~~~~~~~~~~~~

Time to release a new version? Easy!

First, use `bumpversion` to up the release number

.. code-block:: console

    $ bumpversion --current-version VERSION_NUMBER minor --config-file setup.cfg

Where `VERSION_NUMBER` is the current version, e.g. `0.1.0`.

Then run

.. code-block:: console

    $ make release

You probably want to also tag the version now

.. code-block:: console

    $ git tag -a v0.1.0 -m 'Version 0.1.0'
    $ git push --tags

Go ahead and follow those instructions.

Add to Django Packages
~~~~~~~~~~~~~~~~~~~~~~

Once you have a release just go to `Django Packages`_ and add it there.

.. _`Django Packages`: https://www.djangopackages.com/packages/add/

Credits
-------

Based on:

* `Cookiecutter Django Package`_

.. _`Cookiecutter Django Package`: https://github.com/pydanny/cookiecutter-djangopackage
