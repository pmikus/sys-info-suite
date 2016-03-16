"""Module handles printing outputs to stderr, stdout, stdin and file"""

# Modules
import hashlib
import logging
import sys
import xml.etree.ElementTree as ET
from operator import itemgetter
from itertools import groupby
try:
    import lxml.etree
except ImportError:
    sys.stderr.write('LXML library is required to run the script.\n' \
                     'To install the library run the following command:\n' \
                     '\tUbuntu/Debian: apt-get install python-lxml\n' \
                     '\tFedora/RHEL/CentOS: yum install python-lxml\n')
    sys.exit(2)

# Module information
__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "1.0.0"
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

G_STACK_SECTION = {1: "Physical Infrastructure",
                   2: "Compute Hardware",
                   3: "Compute Operating System",
                   4: "Compute Virtualization Infrastructure / Hypervisor",
                   5: "Compute Virtualization Functions / VMs",
                   6: "Network Virtualization Infastructure / vSwitch"}

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

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
    def print_hash(cls, string):
        """Print hash of output"""

        sys.stderr.write(hashlib.sha256(string).hexdigest()+'\n')

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

    @classmethod
    def print_xml_function_list(cls, xml):
        """List the functions in xml"""

        try:
            selection = xml.xpath("//section/function")
            for elem1 in selection:
                sys.stdout.write("Function: "\
                                 +G_COL_GREEN\
                                 +elem1.attrib['id']\
                                 +G_COL_RESET\
                                 +" (Significance: "\
                                 +elem1.attrib['significance']\
                                 +')\n')
        except lxml.etree.XPathSyntaxError as ex_error:
            sys.stderr.write('XPath syntax error: '+str(ex_error)+'\n')
            LOGGER.exception('XPath syntax error: %s', ex_error)
        except lxml.etree.XPathEvalError as ex_error:
            sys.stderr.write('XPath eval error: '+str(ex_error)+'\n')
            LOGGER.exception('XPath evaluation error: %s', ex_error)

    @classmethod
    def print_function_list(cls, suite):
        """Print check outputs"""

        for key, section in groupby(sorted(suite.suite_all,
                                           key=itemgetter(1, 2)),
                                    lambda x: x[1]):
            sys.stdout.write(G_STACK_SECTION[key]+'\n')
            for i in section:
                sys.stdout.write('\t\033[1;32m'+i[0]+'\033[1;m '+i[4]+'\n')
                sys.stdout.write('\t\t'+i[3]+'\n')
                sys.stdout.write('\t\t'+i[5]+'\n\n')

    @classmethod
    def print_function_check(cls, suite):
        """Print check outputs"""

        for key in sorted(suite.suite_all, key=itemgetter(1, 2)):
            if key[6] == 0:
                sys.stdout.write('[\033[1;32m OK \033[1;m]\t'+key[0]+'\n')
            else:
                sys.stdout.write('[\033[1;31m ERR \033[1;m]\t'+key[0]+'\n')
                sys.stdout.write('\tCommand: '+str(key[5])+'\n')
                sys.stdout.write('\t'+str(key[7])+'\n')

    def print_xml_stack(self, suite):
        """Print all outputs into xml"""

        root = ET.Element("stack")
        root.attrib["script_version"] = __version__
        if not suite.suite_host:
            root.attrib["host"] = "localhost"
        else:
            root.attrib["host"] = suite.suite_host

        for key, sec in groupby(sorted(suite.suite_all, key=itemgetter(1, 2)),
                                lambda x: x[1]):
            section = ET.Element("section")
            section.attrib["id"] = str(key)
            section.attrib["name"] = G_STACK_SECTION[key]
            for i in sec:
                output = ET.Element("function")
                output.attrib["id"] = i[0]
                output.attrib["significance"] = str(i[2])
                output.attrib["time"] = i[8]
                output.attrib["version"] = i[4]

                exec_cmd = ET.Element("exec_command")
                exec_cmd.text = "<![CDATA["+str(i[5]).decode('utf-8')+"]]>"
                output.append(exec_cmd)

                exec_code = ET.Element("exec_return_code")
                exec_code.text = str(i[6]).decode('utf-8')
                output.append(exec_code)

                if ET.iselement(i[7]):
                    exec_output = ET.Element("exec_output")
                    exec_output.insert(0, i[7])
                    output.append(exec_output)
                else:
                    exec_output = ET.Element("exec_output")
                    exec_output.text = "<![CDATA[\n"\
                                        +str(i[7]).decode('utf-8')+"]]>"
                    output.append(exec_output)
                section.append(output)
            root.append(section)
        self.print_xml_indent(root)
        sys.stdout.write(ET.tostring(root))

    def print_xml_indent(self, elem, level=0):
        """Handles pretty print for XML"""

        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.print_xml_indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
