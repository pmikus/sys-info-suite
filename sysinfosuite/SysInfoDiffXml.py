"""Module for comparing two xml files"""

# Modules
import sys
import os
import logging
import subprocess
import tempfile
try:
    import lxml.etree
except ImportError:
    sys.stderr.write('LXML library is required to run the script.\n' \
                     'To install the library run the following command:\n' \
                     '\tUbuntu/Debian: apt-get install python-lxml\n' \
                     '\tFedora/RHEL/CentOS: yum install python-lxml\n')
    sys.exit(2)

# Script information
__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "1.1.1"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

# Color settings
G_COL_GREY = '\033[1;30m'
G_COL_RED = '\033[1;31m'
G_COL_GREEN = '\033[1;32m'
G_COL_YELLOW = '\033[1;33m'
G_COL_BLUE = '\033[1;34m'
G_COL_MAGENTA = '\033[1;35m'
G_COL_CYAN = '\033[1;36m'
G_COL_WHITE = '\033[1;37m'
G_COL_CRIMSON = '\033[1;38m'
G_COL_RESET = '\033[1;m'

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

class SysInfoDiffXml(object):
    """Handles comparision of two files."""
    cmd = ""

    def __init__(self, first, second):
        self.first = lxml.etree.parse(first).getroot()
        self.second = lxml.etree.parse(second).getroot()

    @classmethod
    def sdiff_exec(cls, cmd):
        """Executes the diff"""

        try:
            LOGGER.info('Running sdiff (subprocess open): %s', cmd)
            proc_open = subprocess.Popen(cmd,
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         close_fds=False)
            child_stdout, _ = proc_open.communicate()
            return child_stdout
        except OSError as ex_error:
            LOGGER.exception('Subprocess open exception: %s', ex_error)
            sys.exit(2)

    def diff_process(self, arg):
        """Process the diff"""

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
                sys.stdout.write(self.sdiff_exec(self.cmd)+'\n')
                os.remove(temp_path1)
                os.remove(temp_path2)
        except lxml.etree.XPathSyntaxError as ex_error:
            sys.stderr.write('XPath syntax error: '+str(ex_error)+'\n')
            LOGGER.exception('XPath syntaxt error: %s', ex_error)
        except lxml.etree.XPathEvalError as ex_error:
            sys.stderr.write('XPath eval error: '+str(ex_error)+'\n')
            LOGGER.exception('XPath evaluation error: %s', ex_error)
