# Modules
import xml.etree.cElementTree as ET
import collect

class linux_lscpu(collect.OutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gathers CPU architecture information from sysfs and /proc/cpuinfo"
        self.author = "Peter Mikus"
        self.cmd = "lscpu"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 1
        self.output = ""
        self.status = ""