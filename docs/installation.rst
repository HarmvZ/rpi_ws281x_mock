.. highlight:: shell

============
Installation
============


Stable release
--------------

To install rpi-ws281x mock, run this command in your terminal:

.. code-block:: console

    $ pip install rpi_ws281x_mock

This is the preferred method to install rpi-ws281x mock, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for rpi-ws281x mock can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/HarmvZ/rpi_ws281x_mock

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/HarmvZ/rpi_ws281x_mock/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/HarmvZ/rpi_ws281x_mock
.. _tarball: https://github.com/HarmvZ/rpi_ws281x_mock/tarball/master


In a docker container
---------------------

You can also install this library into a docker container. This allows you to build a development/testing environment for applications using `rpi_ws281x`.

Example `Dockerfile`

.. code-block:: dockerfile

    # Pull Raspberry Pi 3 image
    FROM balenalib/raspberrypi3-debian-python:latest
    # Install python and update
    RUN apt-get update && apt-get install -y python3 python3-dev python3-pip python3-virtualenv

    # Activate virtualenv
    ENV VIRTUAL_ENV=/opt/venv
    RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
    ENV PATH="$VIRTUAL_ENV/BIN:$PATH"

    # Install rpi_ws281x_mock
    RUN python3 -m pip install rpi_ws281x_mock
