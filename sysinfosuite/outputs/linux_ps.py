# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_ps(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets actual running processes from"
        self.author = "Peter Mikus"
        self.cmd = "ps -ef"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 3
        self.output = ""
        self.status = ""
