# Modules
import lxml.etree

from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class cimc_bios_unit(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the UCS bios information"
        self.author = "Peter Mikus"
        self.cmd = "biosUnit"
        self.version = "1.0.0"
        self.section = 2
        self.significance = 1
        self.output = ""
        self.status = ""

    def run(self):
        self.pce.get_bios_from_ucs240(self.cmd)
        self.output = self.pce.get_process_output()
        self.status = self.pce.get_process_status()

    def parse_to_xml(self):
        try:
            parser = lxml.etree.XMLParser(remove_blank_text=True)
            self.output = lxml.etree.fromstring(self.output, parser)
        except Exception:
            pass
