# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_meminfo(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets extended memmory intormation"
        self.author = "Peter Mikus"
        self.cmd = "cat /sys/devices/system/node/node*/meminfo"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 1
        self.output = ""
        self.status = ""
