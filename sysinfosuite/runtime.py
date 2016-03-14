#!/usr/bin/env python
"""Module to gather information from local system from scheduled executed
commands"""

# Modules
import SysInfoScheduler
import SysInfoPrinter
import logging
import os
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
G_LOGGER = logging.getLogger(__name__)
G_LOGGER.setLevel(logging.NOTSET)
G_LOG_HANDLER = logging.StreamHandler()
G_LOG_FORMAT = logging.Formatter("%(asctime)s: %(name)s - %(threadName)s \
                                 %(levelname)s - %(message)s")
G_LOG_HANDLER.setFormatter(G_LOG_FORMAT)
G_LOGGER.addHandler(G_LOG_HANDLER)

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
    """Main function"""
    arg = get_args()
    output = SysInfoScheduler.SysInfoScheduler()
    output.add_external_scheduler(arg.ini)
    output.run_scheduler()
    SysInfoPrinter.SysInfoPrinter('').print_scheduler_output(output)
