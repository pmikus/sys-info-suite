# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_lspci(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets PCI information"
        self.author = "Peter Mikus"
        self.cmd = "lspci"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 2
        self.output = ""
        self.status = ""
