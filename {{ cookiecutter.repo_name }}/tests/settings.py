"""Minimum settings to run tests."""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{% for i in range(0, 50) %}{{ "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)" | random }}{% endfor %}'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',

    '{{ cookiecutter.app_name }}.apps.{{ cookiecutter.app_class_name }}Config',
]

MIDDLEWARE = []

ROOT_URLCONF = "tests.urls"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

USE_TZ = True
