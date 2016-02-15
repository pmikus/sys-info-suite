# Modules
import xml.etree.cElementTree as ET
import collect

class linux_cpupower_frequency_info(collect.OutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the power policy information"
        self.author = "Peter Mikus"
        self.cmd = "sudo cpupower -c all frequency-info"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 1
        self.output = ""
        self.status = ""
