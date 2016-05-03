# Modules
import lxml.etree

from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_dtime(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the current date and time"
        self.author = "Peter Mikus"
        self.cmd = "date +'%b %d %Y %H:%M:%S %Z'"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 1
        self.output = ""
        self.status = ""

    def parse_to_xml(self):
        root = lxml.etree.Element("time")
        root.text = str(self.output).rstrip()
        self.output = root
