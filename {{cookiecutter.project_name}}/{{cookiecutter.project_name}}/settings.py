# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


{{ cookiecutter.project_name|upper }}_SETTING = getattr(settings, '{{ cookiecutter.project_name|upper }}_SETTING', 'default')
