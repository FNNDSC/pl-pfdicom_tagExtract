#
# dcm_tagExtract ds ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp

# import the pfdicom_tagExtract module
import  pfdicom_tagExtract
import  pudb
import  sys
import os

Gstr_title = r"""

     _                 _              _____     _                  _   
    | |               | |            |  ___|   | |                | |  
  __| | ___ _ __ ___  | |_ __ _  __ _| |____  _| |_ _ __ __ _  ___| |_ 
 / _` |/ __| '_ ` _ \ | __/ _` |/ _` |  __\ \/ / __| '__/ _` |/ __| __|
| (_| | (__| | | | | || || (_| | (_| | |___>  <| |_| | | (_| | (__| |_ 
 \__,_|\___|_| |_| |_| \__\__,_|\__, \____/_/\_\\__|_|  \__,_|\___|\__|
                   ______        __/ |                                 
                  |______|      |___/                                  

"""

Gstr_synopsis = """



    NAME

       dcm_tagExtract.py 

    SYNOPSIS

        dcm_tagExtract                                                  \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [-i|--inputFile <inputFile>]                                \\
            [-e|--extension <extension>]                                \\
            [-F|--tagFile <tags>]                                       \\
            [-T|--tagList <list_of_tags>]                               \\
            [-r]                                                        \\
            [-m|--imageFile <imageFile>]                                \\
            [-s|--imageScale <imageScale>]                              \\
            [-o|--outputFileStem <outputFileStem>]                      \\
            [-t|--outputFileType <list_of_output_types>]                \\
            [--printElapsedTime]                                        \\
            [--useIndexhtml]                                            \\
            [-p|--printToScreen]                                        \\
            [-y|--synopsis]                                             \\
            [--threads]                                                 \\
            [--outputLeafDir]                                           \\
            [--followLinks]                                             \\
            [--jsonReturn]                                              \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-pfdicom_tagExtract dcm_tagExtract                        \
                /incoming /outgoing

    DESCRIPTION

        `dcm_tagExtract.py` is a ChRIS-based application
         that generates reports in various formats (txt, html, etc) 
         based on parsing DICOM meta data (i.e. DICOM tags).

    ARGS

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
"""


class Dcm_tagExtract(ChrisApp):
    """
    This app performs a recursive walk down an input tree, and for each location
    with a DICOM file, generates a report in the corresponding location in the output tree.
    """
    PACKAGE                 = __package__
    TITLE                   = 'A DICOM tag extractor/reporting tool. Generates reports based on DICOM header information.'
    CATEGORY                = 'DICOM'
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 2000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument("-i", "--inputFile",
                            help        = "input file",
                            type        = str,
                            dest        = 'inputFile',
                            optional    = True,
                            default     = '')
        self.add_argument("-e", "--extension",
                            help        = "DICOM file extension",
                            type        = str,
                            dest        = 'extension',
                            optional    = True,
                            default     = '')
        self.add_argument("-F", "--tagFile",
                            help        = "file containing tags to parse",
                            type        = str,
                            dest        = 'tagFile',
                            optional    = True,
                            default     = '')
        self.add_argument("-T", "--tagList",
                            help        = "comma-separated tag list",
                            type        = str,
                            dest        = 'tagList',
                            optional    = True,
                            default     = '')
        self.add_argument("-r",
                            help        = "display raw tags",
                            type        = str,
                            dest        = 'rawType',
                            optional    = True,
                            default     = 'raw')
        self.add_argument("-m", "--imageFile",
                            help        = "image file to convert DICOM input",
                            type        = str,
                            dest        = 'imageFile',
                            optional    = True,
                            default     = '')
        self.add_argument("-s", "--imageScale",
                            help        = "scale images with factor and optional :interpolation",
                            type        = str,
                            dest        = 'imageScale',
                            optional    = True,
                            default     = '')
        self.add_argument("-o", "--outputFileStem",
                            help        = "output file",
                            optional    = False,
                            type        = str,
                            default     = "",
                            dest        = 'outputFileStem')
        self.add_argument("-t", "--outputFileType",
                            help        = "list of output report types",
                            type        = str,
                            dest        = 'outputFileType',
                            optional    = True,
                            default     = 'raw')
        self.add_argument("--printElapsedTime",
                            help        = "print program run time",
                            type        = bool,
                            dest        = 'printElapsedTime',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
        self.add_argument("--useIndexhtml",
                            help        = "force html file to be called 'index.html'",
                            type        = bool,
                            dest        = 'useIndexhtml',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
        self.add_argument("-p", "--printToScreen",
                            help        = "print output to screen",
                            type        = bool,
                            dest        = 'printToScreen',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
        self.add_argument("-y", "--synopsis",
                            help        = "short synopsis",
                            type        = bool,
                            dest        = 'synopsis',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
        self.add_argument("--threads",
                            help        = "number of threads for innermost loop processing",
                            type        = str,
                            dest        = 'threads',
                            optional    = True,
                            default     = "0")
        self.add_argument("--outputLeafDir",
                            help        = "formatting spec for output leaf directory",
                            type        = str,
                            dest        = 'outputLeafDir',
                            optional    = True,
                            default     = "")
        self.add_argument("--followLinks",
                            help        = "follow symbolic links",
                            dest        = 'followLinks',
                            action      = 'store_true',
                            type        = bool,
                            optional    = True,
                            default     = False)                            
        self.add_argument("--jsonReturn",
                            help        = "output final return in json",
                            type        = bool,
                            dest        = 'jsonReturn',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)


    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        pf_dicom_tagExtract = pfdicom_tagExtract.pfdicom_tagExtract(
                        inputDir            = options.inputdir,
                        inputFile           = options.inputFile,
                        extension           = options.extension,
                        outputDir           = options.outputdir,
                        outputFileStem      = options.outputFileStem,
                        outputLeafDir       = options.outputLeafDir,
                        useIndexhtml        = options.useIndexhtml,
                        outputFileType      = options.outputFileType,
                        tagFile             = options.tagFile,
                        tagList             = options.tagList,
                        printToScreen       = options.printToScreen,
                        threads             = options.threads,
                        imageFile           = options.imageFile,
                        imageScale          = options.imageScale,
                        verbosity           = options.verbosity,
                        followLinks         = options.followLinks,
                        json                = options.jsonReturn   
                    )
        if options.version:
            print('Plugin Version: %s' % Dcm_tagExtract.VERSION)
            print('Internal pfdicom_tagExtract Version: %s' % pf_dicom_tagExtract.str_version)
            sys.exit(0)

        d_pfdicom_tagExtract = pf_dicom_tagExtract.run(timerStart = True)

        if options.printElapsedTime: 
            pf_dicom_tagExtract.dp.qprint(
                                "Elapsed time = %f seconds" % 
                                d_pfdicom_tagExtract['runTime']
                            )

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
