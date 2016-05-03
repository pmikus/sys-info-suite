# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_proc_meminfo(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets Memmory information"
        self.author = "Peter Mikus"
        self.cmd = "cat /proc/meminfo"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 1
        self.output = ""
        self.status = ""
