# Modules
import xml.etree.cElementTree as ET
import collect

class outputs_os_release(collect.OutputsBase):
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

