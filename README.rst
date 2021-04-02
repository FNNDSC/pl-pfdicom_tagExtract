pl-pfdicom_tagExtract
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-pfdicom_tagExtract?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-pfdicom_tagExtract

.. image:: https://img.shields.io/github/license/fnndsc/pl-pfdicom_tagExtract
    :target: https://github.com/FNNDSC/pl-pfdicom_tagExtract/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-pfdicom_tagExtract/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-pfdicom_tagExtract/actions


.. contents:: Table of Contents


Abstract
--------

This app performs a recursive walk down an input tree, and for each location with a DICOM file, will generate a report in the corresponding location in the output tree.


Description
-----------

``dcm_tagExtract`` is a ChRIS-based application that...


Usage
-----

.. code::

    python dcm_tagExtract.py
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-pfdicom_tagExtract dcm_tagExtract --man

Run
~~~

You need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-pfdicom_tagExtract dcm_tagExtract                        \
        /incoming /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-pfdicom_tagExtract .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-pfdicom_tagExtract nosetests

Examples
--------

Put some examples here!


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
