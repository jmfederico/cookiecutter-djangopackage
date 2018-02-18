"""Define actions to be run previous to cookie generation."""

import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('pre_gen_project')

APP_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
APP_NAME = '{{ cookiecutter.app_name }}'

if not re.match(APP_REGEX, APP_NAME):
    logger.error('Invalid value for app_name "{}"'.format(APP_NAME))
    sys.exit(1)
