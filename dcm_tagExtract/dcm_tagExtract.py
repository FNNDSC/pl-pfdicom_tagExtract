#                                                            _
# dcm_tagExtract ds app
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os

# import the Chris app superclass
from chrisapp.base import ChrisApp


# import the pfdicom_tagExtract module
import  pfdicom_tagExtract
import  pudb
import  sys

class Dcm_tagExtract(ChrisApp):
    """
    This app performs a recursive walk down an input tree, and for each location with a DICOM file, will generate a report in the corresponding location in the output tree..
    """
    AUTHORS                 = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'A DICOM tag extractor/reporting tool. Generates reports based on DICOM header information.'
    CATEGORY                = 'DICOM'
    TYPE                    = 'ds'
    DESCRIPTION             = 'This app performs a recursive walk down an input tree, and for each location with a DICOM file, will generate a report in the corresponding location in the output tree.'
    DOCUMENTATION           = 'https://github.com/FNNDSC/pfdicom_tagExtract'
    VERSION                 = '1.0.4'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {}
 
    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
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
        self.add_argument("-x", "--man",
                            help        = "man",
                            type        = bool,
                            dest        = 'man',
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
        self.add_argument("-v", "--verbosity",
                            help        = "verbosity level for app",
                            type        = str,
                            dest        = 'verbosity',
                            optional    = True,
                            default     = "0")
        self.add_argument('--version',
                            help        = 'if specified, print version number',
                            type        = bool,
                            dest        = 'b_version',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
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
        if options.b_version:
            print('Plugin Version: %s' % Dcm_tagExtract.VERSION)
            print('Internal pfdicom_tagExtract Version: %s' % pf_dicom_tagExtract.str_version)
            sys.exit(0)

        d_pfdicom_tagExtract = pf_dicom_tagExtract.run(timerStart = True)

        if options.printElapsedTime: 
            pf_dicom_tagExtract.dp.qprint(
                                "Elapsed time = %f seconds" % 
                                d_pfdicom_tagExtract['runTime']
                            )


# ENTRYPOINT
if __name__ == "__main__":
    app = Dcm_tagExtract()
    app.launch()
