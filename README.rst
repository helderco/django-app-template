Template for morfose's Django reusable apps
===========================================

Run cookiecutter in the folder you want your new project and just answer the questions.


With Docker
-----------

First time setup::

    alias django-create='docker run -it --rm -v "$PWD:/data" helder/cookiecutter'

Usage::

    $ django-create


Without Docker
--------------

.. code-block::

    $ pip install cookiecutter
    $ cookiecutter gh:helderco/django-app-template


That's it folks!
