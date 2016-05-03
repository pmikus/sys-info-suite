# Modules
import lxml.etree

from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class linux_virsh_domains_xml(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Show the status of modules in the Linux Kernel"
        self.author = "Peter Mikus"
        self.cmd = "virsh dumpxml"
        self.cmd1 = "virsh list | grep -E -v \"Id.*Name.*State\" | grep \"^ \" | awk '{print $2}'"
        self.version = "1.0.0"
        self.section = 5
        self.significance = 1
        self.output = ""
        self.status = ""

    def run(self):
        self.pce.execute_process(self.cmd1, "")
        self.output = self.pce.get_process_output()
        self.status = self.pce.get_process_status()
        root = lxml.etree.Element("virsh_domains")
        if not self.status:
            for domain in self.output.split():
                self.pce.execute_process(self.cmd+" "+domain, "")
                try:
                    root.insert(0, lxml.etree.XML(self.pce.get_process_output()))
                except:
                    pass
        self.output = root
