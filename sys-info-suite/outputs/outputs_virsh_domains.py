# Modules
import xml.etree.cElementTree as ET
import collect

class outputs_virsh_domains(collect.OutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the list of running KVM domains from"
        self.author = "Peter Mikus"
        self.cmd = "virsh list | grep -E -v \"Id.*Name.*State\" | grep \"^ \" | awk '{print $2}'"
        self.version = "1.0.0"
        self.section = 4
        self.significance = 2
        self.output = ""
        self.status = ""

