### Information Stack architecture

This information stack abstraction is focused on organizing the configuration information to aid the understanding and enable simpler impact assessment on system performance and operation. The configuration information is collected by running the script on a target platform. It also enables a structured comparison (DIFF) of the config information by allowing to focus on particular system layer or information significance class.

```
+----------------------------------------------------+-------------------------+---+
|                                                    | compute_board           | 1 |
+                                                    +-------------------------+---+
|                                                    | compute_rack_unit       | 1 |
+                                                    +-------------------------+---+
|                                                    | network_adapter_unit    | 1 |
+                                                    +-------------------------+---+
|               Physical Infrastructure              | equipment_fan_module    | 2 |
+                                                    +-------------------------+---+
|                                                    | equipment_psu           | 2 |
+                                                    +-------------------------+---+
|                                                    | pci_equip_slot          | 2 |
+                                                    +-------------------------+---+
|                                                    | mgmt_controller         | 2 |
+----------------------------------------------------+-------------------------+---+
|                                                    | lspci                   | 2 |
+                                                    +-------------------------+---+
|                                                    | lscpu                   | 1 |
+                                                    +-------------------------+---+
|                                                    | lsblk                   | 2 |
+                                                    +-------------------------+---+
|                                                    | meminfo                 | 1 |
+                                                    +-------------------------+---+
|                                                    | ethtool                 | 1 |
+                                                    +-------------------------+---+
|                  Compute Hardware                  | proc_cpuinfo            | 1 |
+                                                    +-------------------------+---+
|                                                    | proc_meminfo            | 1 |
+                                                    +-------------------------+---+
|                                                    | cpupower_idle_info      | 1 |
+                                                    +-------------------------+---+
|                                                    | cpupower_frequency_info | 1 |
+                                                    +-------------------------+---+
|                                                    | bios_settings           | 1 |
+                                                    +-------------------------+---+
|                                                    | bios_unit               | 1 |
+                                                    +-------------------------+---+
|                                                    | cgroup_cpuset           | 2 |
+----------------------------------------------------+-------------------------+---+
|                                                    | linux_version           | 1 |
+                                                    +-------------------------+---+
|                                                    | kernel_version          | 1 |
+                                                    +-------------------------+---+
|                                                    | centos_release          | 1 |
+                                                    +-------------------------+---+
|                                                    | rhel_release            | 1 |
+                                                    +-------------------------+---+
|                                                    | os_release              | 1 |
+                                                    +-------------------------+---+
|                                                    | installed_packages_dpkg | 2 |
+                                                    +-------------------------+---+
|                                                    | installed_packages_yum  | 2 |
+                                                    +-------------------------+---+
|                                                    | grub_alt                | 3 |
+                                                    +-------------------------+---+
|              Compute Operating System              | grub                    | 3 |
+                                                    +-------------------------+---+
|                                                    | proc_cmdline            | 1 |
+                                                    +-------------------------+---+
|                                                    | proc_mounts             | 1 |
+                                                    +-------------------------+---+
|                                                    | lsmod                   | 2 |
+                                                    +-------------------------+---+
|                                                    | links_status            | 3 |
+                                                    +-------------------------+---+
|                                                    | bridges_status          | 3 |
+                                                    +-------------------------+---+
|                                                    | service                 | 3 |
+                                                    +-------------------------+---+
|                                                    | ps                      | 3 |
+                                                    +-------------------------+---+
|                                                    | sysctl                  | 2 |
+                                                    +-------------------------+---+
|                                                    | sched_features          | 2 |
+----------------------------------------------------+-------------------------+---+
|                                                    | virsh_domains           | 2 |
+ Compute Virtualization Infrastructure / Hypervisor +-------------------------+---+
|                                                    | virsh_capabilities      | 1 |
+----------------------------------------------------+-------------------------+---+
|       Compute Virtualization Functions / VMs       | virsh_domains_xml       | 1 |
+----------------------------------------------------+-------------------------+---+
|                                                    | ovs_version             | 1 |
+                                                    +-------------------------+---+
|   Network Virtualization Infastructure / vSwitch   | ovs_bridges_status      | 1 |
+                                                    +-------------------------+---+
|                                                    | vpp_conf                | 1 |
+----------------------------------------------------+-------------------------+---+
```

### Global variables

`G_VNET_SLA_SUITE` - List of strings. Representing names of funtions to run. Each function to run is defined in named module in package 'outputs' and same named class. For more convient way the prefix 'output' is omitted and is automatically added when function is called from class `OutputSuite`.

`G_VNET_SLA_SUITE_BIOS` - List contains only bios related funtion names to run. Bios functions to run are defined in named module in package 'outputs' and same named class. For more convient way the prefix 'output' is omitted and is automatically added when function is called from class `OutputSuite`.

### Functions
##### dtime
Gets the current date and time from target device. Linux command to run: `date +'%b %d %Y %H:%M:%S %Z'`

##### linux_version
Gets the distribution specific information from target device. Linux command to run: `lsb_release -a`

##### centos_release
Gets CentOS release information from target device (CentOS version and release). Linux command to run: `rpm -q centos-release`

##### rhel_release
Gets RHEL release information from target device (RHEL version and release). Linux command to run: `cat /etc/redhat-release`

##### os_release
Gets generic release information from target device. Linux command to run: `cat /etc/os-release`

##### kernel_version
Gets various system information from target device (kernel version and release, name, hardware platform, operating system, machine name). Linux command to run: `uname -a`

##### installed_packages_dpkg
Gets the list of installed packages (DPKG) from target device. Linux command to run: `dpkg -l`

##### installed_packages_yum
Gets the list of installed packages (YUM) from target device. Linux command to run: `yum list installed`

##### grub
Gets grub configuration from target device. Linux command to run: `cat /etc/default/grub`

##### grub_alt
Gets grub configuration from target device. Linux command to run: `sudo cat /boot/grub/grub.conf`. Command may need to run with higher privilege (sudo).

##### proc_cmdline
Gets CMD line options from target device. Linux command to run: `cat /proc/cmdline`

##### proc_cpuinfo
Gets CPU information from target device. Linux command to run: `cat /proc/cpuinfo`

##### proc_meminfo
Gets Memmory information from target device. Linux command to run: `cat /proc/meminfo`

##### proc_mounts
Gets mounted FS information from target device. Linux command to run: `cat /proc/mounts`

##### meminfo
Gets extended memmory intormation from target device. Linux command to run: `cat /sys/devices/system/node/node*/meminfo`

##### lscpu
Gathers  CPU architecture information from sysfs and /proc/cpuinfo from target device. Linux command to run: `lscpu`

##### lspci
Gets PCI information from target device. Linux command to run: `lspci`

##### lsblk
Lists information about all or the specified block devices from target device. Linux command to run: `lsblk`

##### lsmod
Show the status of modules in the Linux Kernel from target device. Linux command to run: `lsmod`

##### links_status
Gets network device information from target device. Linux command to run: `ip link list`

##### bridges_status
Inspect the ethernet bridge configuration in the linux kernel from target device. Linux command to run: `brctl show`

##### ovs_version
Gets the version of OpenVSwitch running on target device. Linux command to run: `ovs-vsctl --version`

##### ovs_bridges_status
Gets the topology information of OpenVSwitch from target device. Linux command to run: `sudo ovs-vsctl show`. Command needs to run with higher privilege (sudo).

##### virsh_domains
Gets the list of running KVM domains from target device. Linux command to run: `virsh list | grep -E -v \"Id.*Name.*State\" | grep \"^ \" | awk '{print $2}'`

##### virsh_capabilities
Gets the XML of KVM capabilities from target device. Linux command to run: `virsh list | grep -E -v \"Id.*Name.*State\" | grep \"^ \" | awk '{print $2}'`

##### virsh_domains_xml
Gets the configuration of running KVM domains from target device. Function iterates over the list of running Virtual Domains and contruct the XML tree from raw data. XML objects are then appended into one XML element and returned as XML object. Linux command to run: `virsh dumpxml _name_`

##### sysctl
Gets actual kernel parameters at runtime from target device. Linux command to run: `sysctl -a`

##### ps
Gets actual running processes from target device. Linux command to run: `ps -ef`

##### vpp_conf
Gets Cisco VPE configuration from target device. Linux command to run: `cat /opt/cisco/vpe/etc/qn.conf`

##### services
Gets services status from target device. Linux command to run: `services -status-all`

##### ethtool
Gets ethtool information from target device. Linux command to run: `for x in ``ifconfig | grep Ethernet | awk '{print $1}'``; do ethtool -k $x; done`

##### cpupower_frequency_info
Gets CPU power/frequency info and governance settings from target device. Linux command to run: `sudo cpupower -c all frequency-info`

##### cpupower_idle_info
Gets CPU idle info from target device. Linux command to run: `sudo cpupower -c all idle-info`

##### services
Gets services status from target device. Linux command to run: `services -status-all`

##### sched_features
Gets scheduler information from target device. Linux command to run: `cat /sys/kernel/debug/sched_features`

##### cgroup_cpuset
Gets cgroup CPU information from target device. Linux command to run: `for a in $(find /sys/fs/cgroup/cpuset -type d) ; do echo $a ; echo -n "CPUs = " ; cat $a/cpuset.cpus ; echo -n "MEMs = " ; cat $a/cpuset.mems ; echo -n "PIDs/TIDs = " ; cat $a/tasks | tr '\012' ',' ; echo ; echo ; done`

##### bios_settings
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `biosSettings`

##### compute_rack_unit
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `computeRackUnit`

##### network_adapter_unit
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `networkAdapterUnit`

##### equipment_psu
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `equipmentPsu`

##### equipment_fan_module
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `equipmentFanModule`

##### compute_board
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `computeBoard`

##### mgmt_controller
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `mgmtController`

##### bios_unit
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `biosUnit`

##### pci_equip_slot
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and scope is `pciEquipSlot`


### Modular support
Script does support external output function definition. External modules have to be specified in subfolder outputs (from python perspective 'package'). This folder has to contain the empty `__init__.py` file so python interpret will recognize it as package. Each external output function definition has to be placed in separate file. File name must match the class name inside the file and also contain prefix 'output_'. Function class is inherited from parent 'OutputsBase' class.

Each class must contain properties including:
- `cmd`			Command to run
- `description`		Description of function
- `version`		Version of the function
- `output`		Output of command run. It could be either type of string or instance of xml.etree.cElementTree.
- `status`		Return code from command run.
- `section`		Section in stack
- `significance`	Significance  of function

Override methods:
- `run()`		Runs the command and save the output (stdout/stderr) into property `output`
- `get_command()`	Returns command from property `cmd`
- `get_version()`	Returns version of function from property `version`
- `get_status()`	Returns exit code from property `status`
- `get_description()`	Returns description from property `description`
- `get_section()`	Returns exit code from property `section`
- `get_significance()`	Returns description from property `significance`
- `get_output()`	Returns output from property `output`. It could be string or instance of xml.etree.cElementTree
- `parse_to_xml()`	Parses output into XML format of xml.etree.cElementTree instance

Parent class definition:
```python
class OutputsBase(object):
    """Parent class for modules implements the behavior"""
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
        """Runs the execution of funtion and returns output and stat"""
        self.pce.proc_exec(self.cmd, "")
        self.status = self.pce.proc_stat()
        self.output = self.pce.proc_output()

    def get_command(self):
        """Return command to run"""
        return self.cmd

    def get_version(self):
        """Return version"""
        return self.version

    def get_status(self):
        """Return status"""
        return self.status

    def get_description(self):
        """Return description of command"""
        return self.description

    def get_section(self):
        """Return section of stack"""
        return self.section

    def get_significance(self):
        """Return significance of function"""
        return self.significance

    def get_output(self):
        """Return output of command. Try to parse to xml"""
        if not self.status:
            self.parse_to_xml()
        return self.output

    def parse_to_xml(self):
        """Parse output to XML"""
        pass
```
