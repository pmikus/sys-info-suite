# Modules
import lxml.etree

from sysinfosuite.SysInfoOutputsBase import SysInfoOutputsBase

class cimc_pci_equip_slot(SysInfoOutputsBase):
    def __init__(self, pc):
        self.pce = pc
        self.description = "Gets the UCS PCI information"
        self.author = "Peter Mikus"
        self.cmd = "pciEquipSlot"
        self.version = "1.0.0"
        self.section = 1
        self.significance = 2
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
