# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class {{ cookiecutter.project_name|replace('_', ' ')|title|replace(' ', '') }}Config(AppConfig):
    name = '{{cookiecutter.project_name}}'
    verbose_name = '{{cookiecutter.project_title}}'

    def ready(self):
        pass
