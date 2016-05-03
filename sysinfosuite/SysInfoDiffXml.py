"""Module for comparing two xml files"""

import logging
import os
import sys
import tempfile
try:
    import lxml.etree
except ImportError:
    sys.stderr.write('LXML library is required to run the script.\n' \
                     'To install the library run the following command:\n' \
                     '\tUbuntu/Debian: apt-get install python-lxml\n' \
                     '\tFedora/RHEL/CentOS: yum install python-lxml\n')
    sys.exit(2)

from sysinfosuite.SysInfoProcessCall import SysInfoProcessCall

__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

class SysInfoDiffXml(object):
    """Handles comparision of two files."""
    cmd = ""

    def __init__(self, first, second):
        self.first = lxml.etree.parse(first).getroot()
        self.second = lxml.etree.parse(second).getroot()
        self.pce = SysInfoProcessCall()
        self.diff_output = []

    def get_diff_output(self):
        """Return result of diff.

        :return: result of diff
        :rtype: string
        """
        return self.diff_output

    def diff_process(self, arg):
        """Process the diff.

        :param arg: arguments from command line
        :type arg: object
        :return: nothing
        """
        try:
            if arg.section:
                sel_first = self.first.xpath("//section[contains(@id, \
                                             '"+arg.section+"')]")
                sel_second = self.second.xpath("//section[contains(@id \
                                               , '"+arg.section+"')]")
            elif arg.function:
                sel_first = self.first.xpath("//section/function[contains \
                                             (@id, '"+arg.function+"')]")
                sel_second = self.second.xpath("//section/function[contains \
                                               (@id, '"+arg.function+"')]")
            elif arg.significance:
                sel_first = self.first.xpath("//section/function[contains \
                                     (@significance, '"+arg.significance+"')]")
                sel_second = self.second.xpath("//section/function[contains \
                                     (@significance, '"+arg.significance+"')]")
            elif arg.xpath:
                sel_first = self.first.xpath(arg.xpath)
                sel_second = self.second.xpath(arg.xpath)
            else:
                sel_first = self.first.xpath("//section/function")
                sel_second = self.second.xpath("//section/function")

            for elem1 in sel_first:
                fd1, temp_path1 = tempfile.mkstemp(text=True)
                file1 = os.fdopen(fd1, 'w+t')
                fd2, temp_path2 = tempfile.mkstemp(text=True)
                file2 = os.fdopen(fd2, 'w+t')
                file1.write(lxml.etree.tostring(elem1))
                file1.read()
                for elem2 in sel_second:
                    if elem1.attrib['id'] == elem2.attrib['id']:
                        file2.write(lxml.etree.tostring(elem2))
                file2.read()
                if arg.changes:
                    self.cmd = "sdiff -s -t -w "+arg.width\
                               +" "+temp_path1+" "+temp_path2
                else:
                    self.cmd = "sdiff -t -w "+arg.width\
                               +" "+temp_path1+" "+temp_path2
                self.pce.execute_process(self.cmd)
                self.diff_output.append(self.pce.get_process_stdout())
                os.remove(temp_path1)
                os.remove(temp_path2)
        except lxml.etree.XPathSyntaxError as ex_error:
            LOGGER.exception('XPath syntax error: {}'.format(ex_error))
        except lxml.etree.XPathEvalError as ex_error:
            LOGGER.exception('XPath evaluation error: {}'.format(ex_error))
