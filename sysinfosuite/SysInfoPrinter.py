"""Module handles printing outputs to stderr, stdout, stdin and file"""

# Modules
import logging
import sys
from operator import itemgetter
from itertools import groupby

# Module information
__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

# Logging settings
G_LOGGER = logging.getLogger(__name__)
G_LOGGER.setLevel(logging.INFO)
G_LOG_HANDLER = logging.StreamHandler()
G_LOG_FORMAT = logging.Formatter("%(asctime)s: %(name)s - %(threadName)s \
                                 %(levelname)s - %(message)s")
G_LOG_HANDLER.setFormatter(G_LOG_FORMAT)
G_LOGGER.addHandler(G_LOG_HANDLER)

class SysInfoPrinter(object):
    """Handles all outputs to stderr, stdout, stdin and file"""

    def __init__(self, file_name=''):
        if file_name:
            sys.stdout = open(file_name, 'w')
            sys.stderr = sys.__stderr__
        else:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

    @classmethod
    def print_scheduler_output(cls, output):
        """Print output from scheduler"""
        for key, section in groupby(sorted(output.dynamic_all,
                                           key=itemgetter(0, 1)),
                                    lambda x: x[0]):
            for i in section:
                sys.stdout.write(i[0]+'\tStart: $ '+i[1]+'\n')
                sys.stdout.write(i[2])
                sys.stdout.write(i[3])
                sys.stdout.write(i[5]+'\tEnd: $ '+i[1]+'\n\n')
