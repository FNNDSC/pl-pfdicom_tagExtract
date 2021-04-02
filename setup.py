from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'dcm_tagExtract',
    version          = '2.0.0',
    description      = 'This app performs a recursive walk down an input tree, and for each location with a DICOM file, will generate a report in the corresponding location in the output tree.',
    long_description = readme,
    author           = 'Sandip Samal',
    author_email     = 'sandip.samal@childrens.harvard.edu',
    url              = 'https://github.com/FNNDSC/pfdicom_tagExtract',
    packages         = ['dcm_tagExtract'],
    install_requires = ['chrisapp','pillow','pfdicom_tagExtract'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'dcm_tagExtract = dcm_tagExtract.__main__:main'
            ]
        }
)
