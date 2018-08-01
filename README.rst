################################
pl-pfdicom_tagExtract
################################


Abstract
********

This app performs a recursive walk down an input tree, and for each location with a DICOM file, will generate a report in the corresponding location in the output tree. This page is not the canonical reference for ``pfdicom_tagExtract`` on which this plugin is based. Please see https://github.com/FNNDSC/pfdicom_tagExtract for detail about the actual tag extraction process and the pattern of command line flags. 

Note that the only different between this plugin and the reference ``pfdicom_tagExtract`` is that the reference has explicit flags for ``inputDir`` and ``outputDir`` while this plugin uses positional arguments for the same.

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an "output" directory to ``/outgoing``

.. code-block:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            fnndsc/pl-pfdicom_tagextract dcm_tagExtract.py              \
            -o '%_md5|6_PatientID-%PatientAge'                          \
            -m 'm:%_nospc|-_ProtocolName.jpg'                           \
            -s 3:none --useIndexhtml                                    \
            -t raw,json,html,dict,col,csv                               \
            --threads 0 -v 2 -e dcm                                     \
            /incoming /outgoing

Assuming that ``$(pwd)/in`` contains a tree of DICOM files, then the above will generate, for each leaf directory node in ``$(pwd)/in`` that contains files satisfying the search constraint of ending in ``.dcm``, a set of text file reports based on the DICOM tags. Also, an ``index.html`` will be generated containing an image of the best guess of the center of the image space in that particular directory.

Debug
*****

Invariably, some debugging will be required. In order to debug efficiently, map the following into their respective locations in the container:

.. code-block:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing          \
            -v dcm_tagExtract.py:/usr/src/dcm_tagExtract/dcm_tagExtract.py  \
            -v pfdicom_tagExtract.py:/usr/local/lib/python3.5/dist-packages/pfdicom_tagExtract/pfdicom_tagExtract.py \
            fnndsc/pl-pfdicom_tagextract dcm_tagExtract.py                  \
            -o '%_md5|6_PatientID-%PatientAge'                              \
            -m 'm:%_nospc|-_ProtocolName.jpg'                               \
            -s 3:none --useIndexhtml                                        \
            -t raw,json,html,dict,col,csv                                   \
            --threads 0 -v 2 -e dcm                                         \
            /incoming /outgoing

This assumes that the source code the underlying ``pfdicom_tagExtract.py`` module is accessible as shown.
