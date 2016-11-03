{{ '=' * cookiecutter.project_title|length }}
{{ cookiecutter.project_title }}
{{ '=' * cookiecutter.project_title|length }}

{{ cookiecutter.project_description }}


Installation
============

Assuming `pypi.morfose.net <https://pypi.morfose.net/>`_ is already setup in your server::

    pip install {{cookiecutter.project_name}}


If not::

    pip install --extra-index-url https://pypi.morfose.net/simple/ {{cookiecutter.project_name}}


Running Tests
=============

.. code::

    dc-run tox


Building Docs
=============

.. code::

    dc-run tox -e docs

To view the docs::

    dc up -d docs
    dc-open docs


Using django-admin.py
=====================

You can use a tox environment, which runs in the `{{cookiecutter.project_name}}` folder::

    dc-run tox -e django-admin -- <arguments>

For example, to create translations::

    dc-run tox -e django-admin -- makemessages -l pt

And to compile::

    dc-run tox -e django-admin -- compilemessages


More documentation
==================

See `included docs <https://readthedocs.morfose.net/{{cookiecutter.project_name}}/>`_ for more information.


