# Modules
import xml.etree.cElementTree as ET
import collect

class outputs_lspci(collect.OutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets PCI information"
        self.author = "Peter Mikus"
        self.cmd = "lspci"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 2
        self.output = ""
        self.status = ""

