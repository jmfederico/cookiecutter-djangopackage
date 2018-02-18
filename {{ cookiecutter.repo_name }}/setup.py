"""Setup script for {{ cookiecutter.app_name }}."""
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieve the version from given file."""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version('{{ cookiecutter.app_name }}', '__init__.py')

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='{{ cookiecutter.repo_name }}',
    version=version,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.app_name }}',
    ],
    include_package_data=True,
    install_requires=['django~={{ django_version }}.0'],
    license="BSD License",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: {{ django_version }}'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: {{ python_version.major }}',
        'Programming Language :: Python :: {{ python_version }}',
    ],
)
