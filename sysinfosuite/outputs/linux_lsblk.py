# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_lsblk(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Lists information about all or the specified block devices"
        self.author = "Peter Mikus"
        self.cmd = "lsblk -l"
        self.version = "1.0.1"
        self.section = 3
        self.significance = 2
        self.output = ""
        self.status = ""
