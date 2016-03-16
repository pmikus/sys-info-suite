#!/usr/bin/env python
"""Script for comparing captured information"""

# Modules
import SysInfoDiffXml
import SysInfoPrinter
import logging
import sys
try:
    import argparse
except ImportError:
    sys.stderr.write('Argparse library is required to run the script.\n' \
                     'To install the library run the following command:\n' \
                     '\tUbuntu/Debian: apt-get install python-argparse\n' \
                     '\tFedora/RHEL/CentOS: yum install python-argparse\n')
    sys.exit(2)

# Module information
__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "1.1.1"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

# Logging settings
LOGGER = logging.getLogger()
#LOGGER.setLevel(logging.INFO)
LOGHANDLER = logging.StreamHandler()
LOGHANDLER.setLevel(logging.DEBUG)
LOGFORMAT = logging.Formatter('%(asctime)s: %(levelname)-8s - %(name)s' \
                                  + '- %(threadName)-12s - %(message)s')
LOGHANDLER.setFormatter(LOGFORMAT)
LOGGER.addHandler(LOGHANDLER)

def get_args():
    """Handles command line arguments."""

    parser = argparse.ArgumentParser(description='Script for comparing \
                                     captured information')
    parser.add_argument('--first',
                        metavar='FILE1',
                        type=argparse.FileType('r'),
                        help='First file to compare',
                        required=True)
    parser.add_argument('--second',
                        metavar='FILE2',
                        type=argparse.FileType('r'),
                        help='Second file to compare',
                        required=True)
    parser.add_argument('--section',
                        action='store',
                        help='Display specific section',
                        default='')
    parser.add_argument('--function',
                        action='store',
                        help='Display specific function',
                        default='')
    parser.add_argument('--xpath',
                        action='store',
                        help='XPath expression filter',
                        default='')
    parser.add_argument('--significance',
                        action='store',
                        help='Display specific function',
                        default='')
    parser.add_argument('--listing',
                        action='store_true',
                        help='Display available functions')
    parser.add_argument('--width',
                        action='store',
                        help='Set the width of the columns',
                        default='230')
    parser.add_argument('--changes',
                        action='store_true',
                        help='Display only changes')
    parser.add_argument('--output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        help='Redirect the output to a file')
    parser.add_argument('--version', action='version',
                        version='Script version: '+__version__)
    try:
        return parser.parse_args()
    except IOError as msg:
        parser.error(str(msg))


if __name__ == "__main__":
    D_ARG = get_args()
    D_PRINTER = SysInfoPrinter.SysInfoPrinter(D_ARG.output)
    D_XML = SysInfoDiffXml.SysInfoDiffXml(D_ARG.first, D_ARG.second)

    if D_ARG.listing:
        sys.stderr.write('First file:\n')
        D_PRINTER.print_xml_function_list(D_XML.first)
        sys.stderr.write('Second file:\n')
        D_PRINTER.print_xml_function_list(D_XML.second)
    else:
        D_XML.diff_process(D_ARG)
