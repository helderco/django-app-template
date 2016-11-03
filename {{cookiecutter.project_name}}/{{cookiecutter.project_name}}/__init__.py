# -*- coding: utf-8 -*-
"""
{{ cookiecutter.project_title }}
{{ '=' * cookiecutter.project_title|length }}

{{ cookiecutter.project_description }}

:copyright: (c) {% now 'utc', '%Y' %} by {{ cookiecutter.author }}.
"""

from __future__ import unicode_literals

import logging


__version__ = '0.1.0-dev'

default_app_config = '{{ cookiecutter.project_name }}.apps.{{ cookiecutter.project_name|replace('_', ' ')|title|replace(' ', '') }}Config'
logger = logging.getLogger(__name__)
