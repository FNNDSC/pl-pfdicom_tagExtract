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

``dcm_tagExtract`` is a ChRIS-based application that generates reports in various formats (txt, html, etc) based on parsing DICOM meta data (i.e. DICOM tags).


Usage
-----

.. code::

    python dcm_tagExtract.py
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [-i|--inputFile <inputFile>]                                
        [-e|--extension <extension>]                                
        [-F|--tagFile <tags>]                                       
        [-T|--tagList <list_of_tags>]                               
        [-r]                                                        
        [-m|--imageFile <imageFile>]                                
        [-s|--imageScale <imageScale>]                              
        [-o|--outputFileStem <outputFileStem>]                      
        [-t|--outputFileType <list_of_output_types>]                
        [--printElapsedTime]                                        
        [--useIndexhtml]                                            
        [-p|--printToScreen]                                        
        [-y|--synopsis]                                             
        [--threads]                                                 
        [--outputLeafDir]                                           
        [--followLinks]                                             
        [--jsonReturn]                                              
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
    
    [-i|--inputFile <inputFile>]   
                                 
    [-e|--extension <extension>]  
                                  
    [-F|--tagFile <tags>]          
                                 
    [-T|--tagList <list_of_tags>]   
                                
    [-r]                     
                                       
    [-m|--imageFile <imageFile>]    
                                
    [-s|--imageScale <imageScale>]  
                                
    [-o|--outputFileStem <outputFileStem>]   
                       
    [-t|--outputFileType <list_of_output_types>]    
                
    [--printElapsedTime]     
                                       
    [--useIndexhtml]             
                                   
    [-p|--printToScreen]  
                                          
    [-y|--synopsis]      
                                           
    [--threads]      
                                               
    [--outputLeafDir]    
                                           
    [--followLinks]     
                                            
    [--jsonReturn]   
          
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

.. code-block:: bash

    docker run -it --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            -v $(pwd)/dcm_tagExtract/dcm_tagExtract.py:/usr/src/dcm_tagExtract/dcm_tagExtract.py  \
            -v $(pwd)/dcm_tagExtract/pfdicom_tagExtract.py:/usr/local/lib/python3.5/dist-packages/pfdicom_tagExtract/pfdicom_tagExtract.py \
            fnndsc/pl-pfdicom_tagextract dcm_tagExtract.py                  \
            -o '%_md5|6_PatientID-%PatientAge'                              \
            -m 'm:%_nospc|-_ProtocolName.jpg'                               \
            -s 3:none --useIndexhtml                                        \
            -t raw,json,html,dict,col,csv                                   \
            --threads 0 -v 2 -e .dcm                                        \
            /incoming /outgoing


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
