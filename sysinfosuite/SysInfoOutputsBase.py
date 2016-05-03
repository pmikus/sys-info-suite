"""Parent class for modules implements the behavior"""

__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

class SysInfoOutputsBase(object):
    """Parent class for modules implements the behavior."""
    description = ""
    cmd = ""
    version = ""
    section = 0
    significance = 0
    output = ""
    status = ""

    def __init__(self, pc):
        self.pce = pc

    def run(self):
        """Runs the execution of funtion and returns output and stat."""
        self.pce.execute_process(self.cmd, "")
        self.status = self.pce.get_process_status()
        self.output = self.pce.get_process_output()

    def get_command(self):
        """Return command to run."""
        return self.cmd

    def get_version(self):
        """Return version."""
        return self.version

    def get_status(self):
        """Return status."""
        return self.status

    def get_description(self):
        """Return description of command."""
        return self.description

    def get_section(self):
        """Return section of stack."""
        return self.section

    def get_significance(self):
        """Return significance of function."""
        return self.significance

    def get_output(self):
        """Return output of command. Try to parse to xml."""
        if not self.status:
            self.parse_to_xml()
        return self.output

    def parse_to_xml(self):
        """Parse output to XML."""
        pass
