# Modules
from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_ovs_bridges_status(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the topology information of OpenVSwitch"
        self.author = "Peter Mikus"
        self.cmd = "sudo ovs-vsctl show"
        self.version = "1.0.0"
        self.section = 6
        self.significance = 1
        self.output = ""
        self.status = ""
