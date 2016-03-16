#!/usr/bin/env python
"""Module to gather information from local system from scheduled executed
commands"""

# Modules
import SysInfoScheduler
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
__version__ = "1.0.0"
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
    """Command line arguments handling"""
    parser = argparse.ArgumentParser(description='Module to gather information \
                                                  from local system from \
                                                  scheduled executed commands')
    parser.add_argument('--ini', required=True, action='store', metavar='FILE',
                        help='ini configuration file')
    parser.add_argument('--output', action='store', metavar='FILE',
                        help='redirect the output to a file')
    parser.add_argument('--version', action='version',
                        version='Module version: '+__version__)
    try:
        return parser.parse_args()
    except IOError as ex_error:
        parser.error(str(ex_error))


if __name__ == "__main__":
    R_ARG = get_args()
    R_PRINTER = SysInfoPrinter.SysInfoPrinter(R_ARG.output)
    R_SCHED = SysInfoScheduler.SysInfoScheduler()
    R_SCHED.add_external_scheduler(R_ARG.ini)
    R_SCHED.run_scheduler()
    R_PRINTER.print_scheduler_output(R_SCHED)
