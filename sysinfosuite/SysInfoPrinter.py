"""Module handles printing outputs to stderr, stdout, stdin and file"""

import hashlib
from itertools import groupby
import logging
from operator import itemgetter
import sys
import re
import xml.etree.ElementTree as ET
try:
    import lxml.etree
except ImportError:
    sys.stderr.write('LXML library is required to run the script.\n' \
                     'To install the library run the following command:\n' \
                     '\tUbuntu/Debian: apt-get install python-lxml\n' \
                     '\tFedora/RHEL/CentOS: yum install python-lxml\n')
    sys.exit(2)

__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

COL_GREY = '\033[1;30m'
COL_RED = '\033[1;31m'
COL_GREEN = '\033[1;32m'
COL_YELLOW = '\033[1;33m'
COL_BLUE = '\033[1;34m'
COL_MAGENTA = '\033[1;35m'
COL_CYAN = '\033[1;36m'
COL_WHITE = '\033[1;37m'
COL_CRIMSON = '\033[1;38m'
COL_RESET = '\033[1;m'

STACK_SECTION = {1: "Physical Infrastructure",
                 2: "Compute Hardware",
                 3: "Compute Operating System",
                 4: "Compute Virtualization Infrastructure / Hypervisor",
                 5: "Compute Virtualization Functions / VMs",
                 6: "Network Virtualization Infastructure / vSwitch"}

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

class SysInfoPrinter(object):
    """Handles all outputs to stderr, stdout, stdin and file."""

    def __init__(self, file_name=''):
        if file_name:
            sys.stdout = open(file_name, 'w')
            sys.stderr = sys.__stderr__
        else:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

    @classmethod
    def print_hash(cls, string):
        """Print hash of output.

        :param string: string to hash
        :type string: string
        :return: nothing
        """
        sys.stderr.write(hashlib.sha256(string).hexdigest()+'\n')

    @classmethod
    def print_scheduler_output(cls, output):
        """Print output from scheduler.

        :param output: array of outputs to print
        :type output: array
        :return: nothing
        """
        for _, section in groupby(sorted(output.dynamic_all,
                                           key=itemgetter(0, 1)),
                                    lambda x: x[0]):
            for i in section:
                sys.stdout.write('{}\tStart: $ {}\n'.format(i[0], i[1]))
                sys.stdout.write(i[2])
                sys.stdout.write(i[3])
                sys.stdout.write('{}\tEnd: $ {}\n\n'.format(i[5], i[1]))

    @classmethod
    def print_diff_output(cls, output):
        """Print output from diff.

        :param output: output to print
        :type output: strin
        :return: nothing
        """
        for diff in output:
            sys.stdout.write(diff)
        sys.stdout.write('\n')

    @classmethod
    def print_xml_function_list(cls, xml):
        """List the functions in xml.

        :param xml: xml output to query
        :type xml: xml
        :return: nothing
        """
        try:
            selection = xml.xpath("//section/function")
            for elem1 in selection:
                sys.stdout.write('\t{}{}{}\n'.format(COL_GREEN,
                                                     elem1.attrib['id'],
                                                     COL_RESET))
                sys.stdout.write('\t\tSignificance: {}\n'.format(
                    elem1.attrib['significance']))
                sys.stdout.write('\t\tVersion: {}\n\n'.format(
                    elem1.attrib['version']))
        except lxml.etree.XPathSyntaxError as ex_error:
            LOGGER.exception('XPath syntax error: {}'.format(ex_error))
        except lxml.etree.XPathEvalError as ex_error:
            LOGGER.exception('XPath evaluation error: {}'.format(ex_error))

    @classmethod
    def print_function_list(cls, suite):
        """Print available functions

        :param suite: array of outputs to print
        :type suite: array
        :return: nothing
        """
        for key, section in groupby(sorted(suite.suite_all,
                                           key=itemgetter(1, 2)),
                                    lambda x: x[1]):
            sys.stdout.write('{}\n'.format(STACK_SECTION[key]))
            for i in section:
                sys.stdout.write('\t{}{}{} {}\n'.format(COL_GREEN, i[0],
                                                        COL_RESET, i[4]))
                sys.stdout.write('\t\t{}\n'.format(i[3]))
                sys.stdout.write('\t\t{}\n\n'.format(i[5]))

    @classmethod
    def print_function_check(cls, suite):
        """Print check outputs

        :param suite: array of outputs to print
        :type suite: array
        :return: nothing
        """
        for key in sorted(suite.suite_all, key=itemgetter(1, 2)):
            if key[6] == 0:
                sys.stdout.write('[{} OK {}]\t{}\n'.format(COL_GREEN,
                                                           COL_RESET,
                                                           key[0]))
            else:
                sys.stdout.write('[{} ERR {}]\t{}\n'.format(COL_RED,
                                                            COL_RESET,
                                                            key[0]))
                sys.stdout.write('\tCommand: {}\n'.format(key[5]))
                sys.stdout.write('\t{}\n'.format(key[7]))

    @classmethod
    def print_full_xml_stack(cls, suite):
        """Print all outputs into xml

        :param suite: array of outputs to print
        :type suite: array
        :return: nothing
        """
        if not suite.suite_host:
            root = lxml.etree.Element('stack', host='localhost',
                                      script_version=__version__)
        else:
            root = lxml.etree.Element('stack', host=suite.suite_host,
                                      script_version=__version__)

        for key, sec in groupby(sorted(suite.suite_all, key=itemgetter(1, 2)),
                                lambda x: x[1]):
            section = lxml.etree.Element('section', id='{:d}'.format(key),
                                         name=STACK_SECTION[key])
            for i in sec:
                output = lxml.etree.Element('function', id=i[0],
                                            significance='{:d}'.format(i[2]),
                                            time=i[8], version=i[4])
                exec_cmd = lxml.etree.Element('exec_command')
                exec_cmd.text = lxml.etree.CDATA('{}'.format(i[5]))
                output.append(exec_cmd)

                exec_code = lxml.etree.Element('exec_return_code')
                exec_code.text = '{:d}'.format(i[6])
                output.append(exec_code)

                if lxml.etree.iselement(i[7]):
                    exec_out = lxml.etree.Element('exec_output')
                    exec_out.append(i[7])
                    output.append(exec_out)
                else:
                    exec_out = lxml.etree.Element('exec_output')
                    exec_out.text = lxml.etree.CDATA(re.sub(r'[^\x00-\x7F]+',
                                                            '', i[7]))
                    output.append(exec_out)
                section.append(output)
            root.append(section)

        sys.stdout.write(lxml.etree.tostring(root, encoding="UTF-8",
                                             pretty_print=True))

