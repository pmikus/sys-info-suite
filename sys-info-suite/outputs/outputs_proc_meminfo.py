# Modules
import xml.etree.cElementTree as ET
import collect

class outputs_proc_meminfo(collect.OutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets Memmory information"
        self.author = "Peter Mikus"
        self.cmd = "cat /proc/meminfo"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 1
        self.output = ""
        self.status = ""

