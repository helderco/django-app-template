# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import VERSION


SECRET_KEY = 'fake-key'

# For test speedup
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_nose',
    '{{ cookiecutter.project_name }}',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ cookiecutter.project_name }}',
        'HOST': 'db',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

if VERSION >= (1, 8):
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
        },
    ]

USE_TZ = True

ROOT_URLCONF = 'tests.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
