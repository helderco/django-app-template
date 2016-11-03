# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from distutils.version import LooseVersion
import django


class compat():
    # These mean "less than or equal to DJANGO_FOO_BAR"
    DJANGO_16 = LooseVersion(django.get_version()) < LooseVersion('1.7')
    DJANGO_17 = LooseVersion(django.get_version()) < LooseVersion('1.8')
    DJANGO_18 = LooseVersion(django.get_version()) < LooseVersion('1.9')
    DJANGO_19 = LooseVersion(django.get_version()) < LooseVersion('2.0')
