"""Module is calling outputs in iteration by dynamically loading modules"""

import datetime as DT
import logging
import os
import pkgutil
import sys

from sysinfosuite.SysInfoProcessCall import SysInfoProcessCall

__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

class SysInfoOutputSuite(object):
    """Handles calling outputs in iteration by dynamically loading modules."""

    def __init__(self, host, username, password, keyfile):
        self.suite_host = host
        self.suite_all = ()
        self.pce = SysInfoProcessCall(host, username, password, keyfile)

    def list_modules(self):
        """List the package modules.

        :return: nothing
        """

        path = os.path.join(os.path.dirname(__file__), "outputs")
        modules = pkgutil.iter_modules(path=[path])
        for _, mod_name, _ in modules:
            if mod_name not in sys.modules:
                try:
                    loaded_mod = __import__("sysinfosuite.outputs."+mod_name,
                                            fromlist=[mod_name])
                    loaded_class = getattr(loaded_mod, mod_name)(self.pce)
                    self.suite_all += ((mod_name,
                                        loaded_class.get_section(),
                                        loaded_class.get_significance(),
                                        loaded_class.get_description(),
                                        loaded_class.get_version(),
                                        loaded_class.get_command(),
                                        loaded_class.get_status(),
                                        loaded_class.get_output(),
                                        str(DT.datetime.utcnow())+" UTC"),)
                # pylint: disable=W0703
                except Exception:
                    LOGGER.exception('Execution error: {}'.format(mod_name))

    def run_module(self, modules):
        """Run the suite by calling modules from package.

        :param modules: list of module names
        :type modules: list
        :return: nothing
        """
        for mod_name in modules:
            if mod_name not in sys.modules:
                try:
                    loaded_mod = __import__("sysinfosuite.outputs."+mod_name,
                                            fromlist=[mod_name])
                    loaded_class = getattr(loaded_mod, mod_name)(self.pce)
                    loaded_class.run()
                    self.suite_all += ((mod_name,
                                        loaded_class.get_section(),
                                        loaded_class.get_significance(),
                                        loaded_class.get_description(),
                                        loaded_class.get_version(),
                                        loaded_class.get_command(),
                                        loaded_class.get_status(),
                                        loaded_class.get_output(),
                                        str(DT.datetime.utcnow())+" UTC"),)
                    LOGGER.debug('Return code: {}'.format(
                        loaded_class.get_status()))
                # pylint: disable=W0703
                except Exception:
                    LOGGER.exception('Execution error: {}'.format(mod_name))

    def run_all_linux_modules(self):
        """Run all linux modules from package.

        :return: nothing
        """

        path = os.path.join(os.path.dirname(__file__), "outputs")
        modules = pkgutil.iter_modules(path=[path])
        for _, mod_name, _ in modules:
            if mod_name not in sys.modules and mod_name.startswith("linux"):
                try:
                    loaded_mod = __import__("sysinfosuite.outputs."+mod_name,
                                            fromlist=[mod_name])
                    loaded_class = getattr(loaded_mod, mod_name)(self.pce)
                    loaded_class.run()
                    self.suite_all += ((mod_name,
                                        loaded_class.get_section(),
                                        loaded_class.get_significance(),
                                        loaded_class.get_description(),
                                        loaded_class.get_version(),
                                        loaded_class.get_command(),
                                        loaded_class.get_status(),
                                        loaded_class.get_output(),
                                        str(DT.datetime.utcnow())+" UTC"),)
                    LOGGER.debug('Return code: {}'.format(
                        loaded_class.get_status()))
                # pylint: disable=W0703
                except Exception:
                    LOGGER.exception('Execution error: {}'.format(mod_name))

    def run_all_cimc_modules(self):
        """Run all cimc modules from package.

        :return: nothing
        """

        path = os.path.join(os.path.dirname(__file__), "outputs")
        modules = pkgutil.iter_modules(path=[path])
        for _, mod_name, _ in modules:
            if mod_name not in sys.modules and mod_name.startswith("cimc"):
                try:
                    loaded_mod = __import__("sysinfosuite.outputs."+mod_name,
                                            fromlist=[mod_name])
                    loaded_class = getattr(loaded_mod, mod_name)(self.pce)
                    loaded_class.run()
                    self.suite_all += ((mod_name,
                                        loaded_class.get_section(),
                                        loaded_class.get_significance(),
                                        loaded_class.get_description(),
                                        loaded_class.get_version(),
                                        loaded_class.get_command(),
                                        loaded_class.get_status(),
                                        loaded_class.get_output(),
                                        str(DT.datetime.utcnow())+" UTC"),)
                    LOGGER.debug('Return code: {}'.format(
                        loaded_class.get_status()))
                # pylint: disable=W0703
                except Exception:
                    LOGGER.exception('Execution error: {}'.format(mod_name))

    def run_all_modules(self):
        """Run all modules from package.

        :return: nothing
        """

        path = os.path.join(os.path.dirname(__file__), "outputs")
        modules = pkgutil.iter_modules(path=[path])
        for _, mod_name, _ in modules:
            if mod_name not in sys.modules:
                try:
                    loaded_mod = __import__("sysinfosuite.outputs."+mod_name,
                                            fromlist=[mod_name])
                    loaded_class = getattr(loaded_mod, mod_name)(self.pce)
                    loaded_class.run()
                    self.suite_all += ((mod_name,
                                        loaded_class.get_section(),
                                        loaded_class.get_significance(),
                                        loaded_class.get_description(),
                                        loaded_class.get_version(),
                                        loaded_class.get_command(),
                                        loaded_class.get_status(),
                                        loaded_class.get_output(),
                                        str(DT.datetime.utcnow())+" UTC"),)
                    LOGGER.debug('Return code: {}'.format(
                        loaded_class.get_status()))
                # pylint: disable=W0703
                except Exception:
                    LOGGER.exception('Execution error: {}'.format(mod_name))

