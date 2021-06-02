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
    An optional <inputFile> specified relative to the <inputDir>. If
    specified, then do not perform a directory walk, but convert only
    this file.
                          
    [-e|--extension <extension>]  
    An optional extension to filter the DICOM files of interest from the
    <inputDir>.
                              
    [-F|--tagFile <tags>]          
    Read the tags, one-per-line in <tagFile>, and print the
    corresponding tag information in the DICOM <inputFile>.
                           
    [-T|--tagList <list_of_tags>]   
    Read the list of comma-separated tags in <tagList>, and print the
    corresponding tag information parsed from the DICOM <inputFile>.  
                              
    [-r]                     
    If specified, display raw tags      
                                
    [-m|--imageFile <imageFile>]    
    If specified, also convert the <inputFile> to <imageFile>. If the
    name is preceded by an index and colon, then convert this indexed
    file in the particular <inputDir>.  
                              
    [-s|--imageScale <imageScale>]  
    If an image conversion is specified, this flag will scale the image
    by <factor> and use an interpolation <order>. This is useful in
    increasing the size of images for the html output.

    Note that certain interpolation choices can result in a significant
    slowdown!

        interpolation order:

        'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
        'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
        'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'

    [-o|--outputFileStem <outputFileStem>]
    The output file stem to store data. This should *not* have a file
    extension, or rather, any "." in the name are considered part of
    the stem and are *not* considered extensions.                            
                       
    [-t|--outputFileType <list_of_output_types>]    
    A comma specified list of output types. These can be:

    	o <type>    <ext>       <desc>
    	o raw       -raw.txt    the raw internal dcm structure to string
    	o json      .json       a json representation
    	o html      .html       an html representation with optional image
    	o dict      -dict.txt   a python dictionary
    	o col       -col.txt    a two-column text representation (tab sep)
    	o csv       .csv        a csv representation

	Note that if not specified, a default type of 'raw' is assigned.          
	 
    [--printElapsedTime]     
    If specified, print run time
                                       
    [--useIndexhtml]             
    If specified, force html file to be called index.html   
                                    
    [-p|--printToScreen]  
    If specified, will print tags to screen.
                                          
    [-y|--synopsis]      
    Show brief help.
                                           
    [--threads]      
                                               
    [--outputLeafDir]    
    If specified, will apply the <outputLeafDirFormat> to the output
    directories containing data. This is useful to blanket describe
    final output directories with some descriptive text, such as
    'anon' or 'preview'.

    This is a formatting spec, so

        --outputLeafDir 'preview-%s'

    where %s is the original leaf directory node, will prefix each
    final directory containing output with the text 'preview-' which
    can be useful in describing some features of the output set.
                                     
    [--followLinks]     
    If specified, follow symbolic links.
                                            
    [--jsonReturn]   
    If specified, output a JSON dump of final return.  
       
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
