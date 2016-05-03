# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_bridges_status(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Inspect the ethernet bridge configuration in the linux kernel"
        self.author = "Peter Mikus"
        self.cmd = "brctl show"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 3
        self.output = ""
        self.status = ""
