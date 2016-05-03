# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_os_release(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets generic release information from target device"
        self.author = "Peter Mikus"
        self.cmd = "cat /etc/os-release"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 1
        self.output = ""
        self.status = ""
