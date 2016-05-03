# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_kernel_version(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets various system information"
        self.author = "Peter Mikus"
        self.cmd = "uname -a"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 1
        self.output = ""
        self.status = ""
