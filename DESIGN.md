### Information Stack architecture

This information stack abstraction is focused on organizing the configuration information to aid the understanding and enable simpler impact assessment on system performance and operation. The configuration information is collected by running the script on a target platform. It also enables a structured comparison (DIFF) of the information by allowing to focus on particular system layer or information significance class.

```
+----------------------------------------------------+-------------------------------+---+
|                                                    | cimc_compute_board            | 1 |
+                                                    +-------------------------------+---+
|                                                    | cimc_compute_rack_unit        | 1 |
+                                                    +-------------------------------+---+
|                                                    | cimc_network_adapter_unit     | 1 |
+                                                    +-------------------------------+---+
|               Physical Infrastructure              | cimc_equipment_fan_module     | 2 |
+                                                    +-------------------------------+---+
|                                                    | cimc_equipment_psu            | 2 |
+                                                    +-------------------------------+---+
|                                                    | cimc_pci_equip_slot           | 2 |
+                                                    +-------------------------------+---+
|                                                    | cimc_mgmt_controller          | 2 |
+----------------------------------------------------+-------------------------------+---+
|                                                    | linux_lspci                   | 2 |
+                                                    +-------------------------------+---+
|                                                    | linux_lscpu                   | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_lsblk                   | 2 |
+                                                    +-------------------------------+---+
|                                                    | linux_meminfo                 | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_ethtool                 | 1 |
+                                                    +-------------------------------+---+
|                  Compute Hardware                  | linux_proc_cpuinfo            | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_proc_meminfo            | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_cpupower_idle_info      | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_cpupower_frequency_info | 1 |
+                                                    +-------------------------------+---+
|                                                    | cimc_bios_settings            | 1 |
+                                                    +-------------------------------+---+
|                                                    | cimc_bios_unit                | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_cgroup_cpuset           | 2 |
+----------------------------------------------------+-------------------------------+---+
|                                                    | linux_linux_version           | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_kernel_version          | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_centos_release          | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_rhel_release            | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_os_release              | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_installed_packages_dpkg | 2 |
+                                                    +-------------------------------+---+
|                                                    | linux_installed_packages_yum  | 2 |
+                                                    +-------------------------------+---+
|                                                    | linux_grub_alt                | 3 |
+                                                    +-------------------------------+---+
|              Compute Operating System              | linux_grub                    | 3 |
+                                                    +-------------------------------+---+
|                                                    | linux_proc_cmdline            | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_proc_mounts             | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_lsmod                   | 2 |
+                                                    +-------------------------------+---+
|                                                    | linux_links_status            | 3 |
+                                                    +-------------------------------+---+
|                                                    | linux_bridges_status          | 3 |
+                                                    +-------------------------------+---+
|                                                    | linux_service                 | 3 |
+                                                    +-------------------------------+---+
|                                                    | linux_ps                      | 3 |
+                                                    +-------------------------------+---+
|                                                    | linux_sysctl                  | 2 |
+                                                    +-------------------------------+---+
|                                                    | linux_sched_features          | 2 |
+----------------------------------------------------+-------------------------------+---+
|                                                    | linux_virsh_domains           | 2 |
+ Compute Virtualization Infrastructure / Hypervisor +-------------------------------+---+
|                                                    | linux_virsh_capabilities      | 1 |
+----------------------------------------------------+-------------------------------+---+
|       Compute Virtualization Functions / VMs       | linux_virsh_domains_xml       | 1 |
+----------------------------------------------------+-------------------------------+---+
|                                                    | linux_ovs_version             | 1 |
+                                                    +-------------------------------+---+
|   Network Virtualization Infastructure / vSwitch   | linux_ovs_bridges_status      | 1 |
+                                                    +-------------------------------+---+
|                                                    | linux_vpp_conf                | 1 |
+----------------------------------------------------+-------------------------------+---+
```

### Global variables

`G_SUITE` - List of strings. Items of list are representing names of functions to run. Each function to run is defined in named module in package 'outputs' and same named class. Iteration through names is done in class methods `OutputSuite`. Prefix allows to group functions per criteria (e.g. Linux, CIMC).

`G_SUITE_UCS` - List contains only CIMC related function names to run. Each function to run is defined in named module in package 'outputs' and same named class. Iteration through names is done in class methods `OutputSuite`. Prefix allows to group functions per criteria (e.g. Linux, CIMC).

### Functions
##### linux_dtime
Gets the current date and time from target device. Linux command to run: `date +'%b %d %Y %H:%M:%S %Z'`

##### linux_linux_version
Gets the distribution specific information from target device. Linux command to run: `lsb_release -a`

##### linux_centos_release
Gets CentOS release information from target device (CentOS version and release). Linux command to run: `rpm -q centos-release`

##### linux_rhel_release
Gets RHEL release information from target device (RHEL version and release). Linux command to run: `cat /etc/redhat-release`

##### linux_os_release
Gets generic release information from target device. Linux command to run: `cat /etc/os-release`

##### linux_kernel_version
Gets various system information from target device (kernel version and release, name, hardware platform, operating system, machine name). Linux command to run: `uname -a`

##### linux_installed_packages_dpkg
Gets the list of installed packages (DPKG) from target device. Linux command to run: `dpkg -l`

##### linux_installed_packages_yum
Gets the list of installed packages (YUM) from target device. Linux command to run: `yum list installed`

##### linux_grub
Gets grub configuration from target device. Linux command to run: `cat /etc/default/grub`

##### linux_grub_alt
Gets grub configuration from target device. Linux command to run: `sudo cat /boot/grub/grub.conf`. Command may need to run with higher privilege (sudo).

##### linux_proc_cmdline
Gets CMD line options from target device. Linux command to run: `cat /proc/cmdline`

##### linux_proc_cpuinfo
Gets CPU information from target device. Linux command to run: `cat /proc/cpuinfo`

##### linux_proc_meminfo
Gets Memmory information from target device. Linux command to run: `cat /proc/meminfo`

##### linux_proc_mounts
Gets mounted FS information from target device. Linux command to run: `cat /proc/mounts`

##### linux_meminfo
Gets extended memmory intormation from target device. Linux command to run: `cat /sys/devices/system/node/node*/meminfo`

##### linux_lscpu
Gathers  CPU architecture information from sysfs and /proc/cpuinfo from target device. Linux command to run: `lscpu`

##### linux_lspci
Gets PCI information from target device. Linux command to run: `lspci`

##### linux_lsblk
Lists information about all or the specified block devices from target device. Linux command to run: `lsblk`

##### linux_lsmod
Show the status of modules in the Linux Kernel from target device. Linux command to run: `lsmod`

##### linux_links_status
Gets network device information from target device. Linux command to run: `ip link list`

##### linux_bridges_status
Inspect the ethernet bridge configuration in the linux kernel from target device. Linux command to run: `brctl show`

##### linux_ovs_version
Gets the version of OpenVSwitch running on target device. Linux command to run: `ovs-vsctl --version`

##### linux_ovs_bridges_status
Gets the topology information of OpenVSwitch from target device. Linux command to run: `sudo ovs-vsctl show`. Command needs to run with higher privilege (sudo).

##### linux_virsh_domains
Gets the list of running KVM domains from target device. Linux command to run: `virsh list | grep -E -v \"Id.*Name.*State\" | grep \"^ \" | awk '{print $2}'`

##### linux_virsh_capabilities
Gets the XML of KVM capabilities from target device. Linux command to run: `virsh list | grep -E -v \"Id.*Name.*State\" | grep \"^ \" | awk '{print $2}'`

##### linux_virsh_domains_xml
Gets the configuration of running KVM domains from target device. Function iterates over the list of running Virtual Domains and contruct the XML tree from raw data. XML objects are then appended into one XML element and returned as XML object. Linux command to run: `virsh dumpxml _name_`

##### linux_sysctl
Gets actual kernel parameters at runtime from target device. Linux command to run: `sysctl -a`

##### linux_ps
Gets actual running processes from target device. Linux command to run: `ps -ef`

##### linux_vpp_conf
Gets Cisco VPE configuration from target device. Linux command to run: `cat /opt/cisco/vpe/etc/qn.conf`

##### linux_services
Gets services status from target device. Linux command to run: `services -status-all`

##### linux_ethtool
Gets ethtool information from target device. Linux command to run: `for x in ``ifconfig | grep Ethernet | awk '{print $1}'``; do ethtool -k $x; done`

##### linux_cpupower_frequency_info
Gets CPU power/frequency info and governance settings from target device. Linux command to run: `sudo cpupower -c all frequency-info`

##### linux_cpupower_idle_info
Gets CPU idle info from target device. Linux command to run: `sudo cpupower -c all idle-info`

##### linux_services
Gets services status from target device. Linux command to run: `services -status-all`

##### linux_sched_features
Gets scheduler information from target device. Linux command to run: `cat /sys/kernel/debug/sched_features`

##### linux_cgroup_cpuset
Gets cgroup CPU information from target device. Linux command to run: `for a in $(find /sys/fs/cgroup/cpuset -type d) ; do echo $a ; echo -n "CPUs = " ; cat $a/cpuset.cpus ; echo -n "MEMs = " ; cat $a/cpuset.mems ; echo -n "PIDs/TIDs = " ; cat $a/tasks | tr '\012' ',' ; echo ; echo ; done`

##### cimc_compute_rack_unit
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `computeRackUnit`

##### cimc_network_adapter_unit
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `networkAdapterUnit`

##### cimc_equipment_psu
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `equipmentPsu`

##### cimc_equipment_fan_module
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `equipmentFanModule`

##### cimc_compute_board
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `computeBoard`

##### cimc_mgmt_controller
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `mgmtController`

##### cimc_bios_unit
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `biosUnit`

##### cimc_pci_equip_slot
Gets information from Cisco CIMC device via XML API. XML API method is configResolveClass and classId is `pciEquipSlot`


### Modular support
Script does support external output function definition. External modules have to be specified in sub-folder outputs (from python perspective 'package'). This folder has to contain the empty `__init__.py` file so python interpret will recognize it as package. Each external output function definition has to be placed in separate file. File name must match the class name inside the file and can also contain prefix 'prefix_'. Function class is inherited from parent 'OutputsBase' class.

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
