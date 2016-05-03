# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_proc_cmdline(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets CMD line options"
        self.author = "Peter Mikus"
        self.cmd = "cat /proc/cmdline"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 1
        self.output = ""
        self.status = ""
