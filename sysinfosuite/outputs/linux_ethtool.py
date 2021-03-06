# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_ethtool(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets Ethtool show-features information"
        self.author = "Peter Mikus"
        self.cmd = "for x in `ifconfig | grep Ethernet | awk '{print $1}'`; do ethtool -k $x; done"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 1
        self.output = ""
        self.status = ""
