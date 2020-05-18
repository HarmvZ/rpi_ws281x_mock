===============
rpi-ws281x mock
===============


.. image:: https://img.shields.io/pypi/v/rpi_ws281x_mock.svg
        :target: https://pypi.python.org/pypi/rpi_ws281x_mock

.. image:: https://img.shields.io/travis/HarmvZ/rpi_ws281x_mock.svg
        :target: https://travis-ci.org/HarmvZ/rpi_ws281x_mock

.. image:: https://readthedocs.org/projects/rpi-ws281x-mock/badge/?version=latest
        :target: https://rpi-ws281x-mock.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/HarmvZ/rpi_ws281x_mock/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/HarmvZ/rpi_ws281x_mock

.. image:: https://pyup.io/repos/github/HarmvZ/rpi_ws281x_mock/shield.svg
        :target: https://pyup.io/repos/github/HarmvZ/rpi_ws281x_mock/
        :alt: Updates



This package mocks the behavior of the `rpi_ws281x`_ Python library. This is used for testing a project that uses `rpi_ws281x`_ on non-Raspbian systems. Simply replace the pip installation of `rpi_ws281x` with `rpi_ws281x_mock` in your development environment to start using it.


* Free software: MIT license
* Documentation: https://rpi-ws281x-mock.readthedocs.io.


Features
--------

* Implements all methods from `rpi_ws281x`_ without calling any of the hardware functions

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _`rpi_ws281x`: https://github.com/rpi-ws281x/rpi-ws281x-python
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
