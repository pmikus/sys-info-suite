# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_linux_version(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the distribution specific information."
        self.author = "Peter Mikus"
        self.cmd = "lsb_release -a"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 1
        self.output = ""
        self.status = ""
