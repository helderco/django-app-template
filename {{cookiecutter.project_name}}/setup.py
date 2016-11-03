#!/usr/bin/env python
from __future__ import unicode_literals

import os
from codecs import open

from setuptools import setup, find_packages

from {{ cookiecutter.project_name }} import __version__

requires = []

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='{{ cookiecutter.project_name }}',
    version=__version__,
    description='{{ cookiecutter.project_description }}',
    long_description=readme,
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    url='https://readthedocs.morfose.net/{{ cookiecutter.project_name }}/',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    setup_requires=(),
    install_requires=(),
    extras_require={},
    license='Proprietary',
    platforms=['OS Independent'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
