# Modules
import xml.etree.cElementTree as ET
import collect

class linux_lsblk(collect.OutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Lists information about all or the specified block devices"
        self.author = "Peter Mikus"
        self.cmd = "lsblk"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 2
        self.output = ""
        self.status = ""
