# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_installed_packages_yum(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the list of installed packages (YUM)"
        self.author = "Peter Mikus"
        self.cmd = "yum list installed"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 2
        self.output = ""
        self.status = ""
