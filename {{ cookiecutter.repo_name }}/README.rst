{% for i in range(0, cookiecutter.project_name|count) %}={% endfor %}
{{ cookiecutter.project_name }}
{% for i in range(0, cookiecutter.project_name|count) %}={% endfor %}

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

{{ cookiecutter.project_short_description }}

Documentation
-------------

The full documentation is at https://{{ cookiecutter.repo_name }}.readthedocs.io.

Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.repo_name }}

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}.apps.{{ cookiecutter.app_class_name }}Config',
        ...
    )


Features
--------

* TODO


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `Cookiecutter Django Package`_ by jmfederico_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Cookiecutter Django Package`: https://github.com/jmfederico/cookiecutter-djangopackage
.. _jmfederico: https://github.com/jmfederico
