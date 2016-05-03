# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_proc_mounts(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets mounted FS information from target device"
        self.author = "Peter Mikus"
        self.cmd = "cat /proc/mounts"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 1
        self.output = ""
        self.status = ""
