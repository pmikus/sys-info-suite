# Modules
import xml.etree.cElementTree as ET
import collect

class linux_grub(collect.OutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets grub configuration"
        self.author = "Peter Mikus"
        self.cmd = "cat /etc/default/grub"
        self.version = "1.0.0"
        self.section = 3
        self.significance = 3
        self.output = ""
        self.status = ""
