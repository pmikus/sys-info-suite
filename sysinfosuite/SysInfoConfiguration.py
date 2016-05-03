"""Module for parsing and saving configuration file"""

import json
import logging
import sys

__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

class SysInfoConfiguration(object):
    """Handles parsing and saving configuration file."""

    def __init__(self, config):
        self.config = config

    def load_json_config(self, jfile):
        """Load configuration from file.

        :param jfile: file name
        :type jfile: string
        :return: configuration from file
        :rtype: list
        """

        try:
            self.config = json.load(open(jfile, 'r'))
            return self.config
        except IOError as ex_error:
            LOGGER.exception('Cannot load configuration: {}'.format(ex_error))
            sys.exit(2)
        except ValueError as ex_error:
            LOGGER.exception('Cannot load configuration: {}'.format(ex_error))
            sys.exit(2)
        except TypeError as ex_error:
            LOGGER.exception('Cannot load configuration: {}'.format(ex_error))
            sys.exit(2)

    def save_json_config(self, config, jfile):
        """Save configuration to file.

        :param config: configuration
        :param jfile: file name
        :type config: list
        :type jfile: string
        :return: nothing
        """

        self.config = config
        try:
            json.dump(self.config, open(jfile, 'w'))
        except IOError as ex_error:
            LOGGER.exception('Cannot write configuration file: {}'.format(
                ex_error))
            sys.exit(2)

