"""Define actions to be run after cookie generation."""

import logging
import os
import shutil

from django.core import management

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('post_gen_project')

APP_NAME = '{{ cookiecutter.app_name }}'


def generate_django_app(app_name):
    """Generate Django app."""
    try:
        shutil.rmtree(app_name)
    except FileNotFoundError:
        pass

    management.call_command('startapp', app_name)

    with open('{}/__init__.py'.format(app_name), 'a') as init_file:
        init_file.write("__version__ = '{{ cookiecutter.version }}'\n")


def generate_example_django_project():
    """Generate example Django project."""
    project_name = 'example'
    project_directory = 'example'

    try:
        shutil.rmtree('{}/{}'.format(project_directory, project_name))
    except FileNotFoundError:
        pass

    try:
        os.remove('{}/manage.py'.format(project_directory))
    except FileNotFoundError:
        pass

    management.call_command('startproject', project_name, project_directory)

    with open('{}/{}/settings.py'.format(project_directory, project_name), 'a') as settings_file:
        settings_file.write("""
# Start: added by cookiecutter.
INSTALLED_APPS.append('{{ cookiecutter.app_name }}')
# End: added by cookiecutter.
""")


def remove_test_file_from_app(app_directory):
    """
    Remove redudant tests.py file.

    Tests are written in the tests folder outside the app.
    """
    try:
        os.remove('{}/tests.py'.format(app_directory))
    except FileNotFoundError:
        pass


generate_django_app(APP_NAME)
remove_test_file_from_app(APP_NAME)
generate_example_django_project()
