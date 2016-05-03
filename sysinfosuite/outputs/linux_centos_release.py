# Modules
import lxml.etree

from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_centos_release(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets CentOS release information (CentOS version and release)"
        self.author = "Peter Mikus"
        self.cmd = "rpm -q centos-release"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 1
        self.output = ""
        self.status = ""

    def parse_to_xml(self):
        root = lxml.etree.Element("centos_release")
        root.text = str(self.output).rstrip()
        self.output = root
