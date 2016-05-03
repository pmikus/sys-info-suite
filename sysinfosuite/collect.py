#!/usr/bin/env python
"""Script to gather information from local or remote system"""

import logging
import sys
try:
    import argparse
except ImportError:
    sys.stderr.write('Argparse library is required to run the script.\n' \
                     'To install the library run the following command:\n' \
                     '\tUbuntu/Debian: apt-get install python-argparse\n' \
                     '\tFedora/RHEL/CentOS: yum install python-argparse\n')
    sys.exit(2)

from sysinfosuite.SysInfoConfiguration import SysInfoConfiguration
from sysinfosuite.SysInfoOutputSuite import SysInfoOutputSuite
from sysinfosuite.SysInfoPrinter import SysInfoPrinter

# Script information
__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

# Logging settings
LOGGER = logging.getLogger()
#LOGGER.setLevel(logging.INFO)
LOGHANDLER = logging.StreamHandler()
LOGHANDLER.setLevel(logging.DEBUG)
LOGFORMAT = logging.Formatter('%(asctime)s: %(levelname)-8s - %(name)s' \
                              + '- %(threadName)-12s - %(message)s')
LOGHANDLER.setFormatter(LOGFORMAT)
LOGGER.addHandler(LOGHANDLER)

# VNET SLA output suite
G_SUITE = ["linux_cpupower_frequency_info",
           "linux_cpupower_idle_info",
           "linux_ethtool",
           "linux_lscpu",
           "linux_lspci",
           "linux_meminfo",
           "linux_proc_cpuinfo",
           "linux_proc_meminfo",
           "linux_bridges_status",
           "linux_centos_release",
           "linux_grub",
           "linux_cgroup_cpuset",
           "linux_grub_alt",
           "linux_installed_packages_dpkg",
           "linux_installed_packages_yum",
           "linux_kernel_version",
           "linux_links_status",
           "linux_linux_version",
           "linux_lsblk",
           "linux_lsmod",
           "linux_os_release",
           "linux_proc_cmdline",
           "linux_proc_mounts",
           "linux_ps",
           "linux_rhel_release",
           "linux_service",
           "linux_sysctl",
           "linux_sched_features",
           "linux_dtime",
           "linux_virsh_capabilities",
           "linux_virsh_domains",
           "linux_virsh_domains_xml",
           "linux_ovs_bridges_status",
           "linux_ovs_version",
           "linux_vpp_conf"]

# CIMC inventory output
G_SUITE_UCS_FULL = ["cimc_compute_rack_unit"]
G_SUITE_UCS = ["cimc_network_adapter_unit",
               "cimc_equipment_psu",
               "cimc_equipment_fan_module",
               "cimc_compute_board",
               "cimc_mgmt_controller",
               "cimc_bios_unit",
               "cimc_pci_equip_slot"]

def get_args():
    """Command line arguments handling"""
    parser = argparse.ArgumentParser(description='Script for gathering \
                                     the running configuration from host')
    device = parser.add_argument_group('Authentication for device')
    device.add_argument('--device', action='store',
                        help='HOST device to get the information from',
                        default='')
    device.add_argument('--cimc', action='store',
                        help='CIMC device to get the BIOS information',
                        default='')
    device.add_argument('--user', action='store', default='')
    device.add_argument('--password', action='store', default='')
    parser.add_argument('--check', action='store_true',
                        help='check if functions are supported',
                        default=False)
    parser.add_argument('--interactive', action='store_true',
                        help='run script in interactive mode',
                        default=False)
    parser.add_argument('--listing', action='store_true',
                        help='list abvailable functions',
                        default=False)
    parser.add_argument('--hashing', action='store_true',
                        help='print hash of output',
                        default=False)
    parser.add_argument('--output', action='store', metavar='FILE',
                        help='redirect the output to a file')
    parser.add_argument('--keyfile', action='store', metavar='FILE',
                        help='specify SSH key file for authentication')
    parser.add_argument('--json', action='store',
                        help='json configuration file',
                        default='')
    parser.add_argument('--version', action='version',
                        version='Script version: '+__version__)
    try:
        return parser.parse_args()
    except IOError as msg:
        parser.error(str(msg))


def run_interactive():
    """Interactive mode handling"""
    config = ''
    device = raw_input("Enter the host [leave blank for localhost]: ")
    if device:
        keyfile = raw_input("Enter the keyfile [leave blank if N/A]: ")
        user = raw_input("Enter the username for host: ")
        password = raw_input("Enter the password: ")
    else:
        user = ''
        password = ''
        keyfile = ''
    sys.stdout.write('Please select type of device:\n')
    sys.stdout.write('1. Cisco CIMC BIOS\n')
    sys.stdout.write('2. Linux host\n')
    choice = raw_input('Enter your choice [1-2] : ')
    if choice == "1":
        device_type = "cimc"
        suite = G_SUITE_UCS
    else:
        device_type = "linux"
        suite = G_SUITE
    output = raw_input("Enter the output file [leave blank for stdout]: ")
    save = raw_input("Save configuration file? [Yes/No]: ")
    config = {device_type+"_"+device: {'device': device,
                                       'device_type': device_type,
                                       'user': user,
                                       'password': password,
                                       'output': output,
                                       'keyfile': keyfile,
                                       'suite': suite}}
    if save == "Yes" or save == "Y" or save == "y" or save == "yes":
        jfile = raw_input("Enter name of configuration file: ")
        SysInfoConfiguration('').save_json_config(config, jfile)
    return config


def run_config(arg, config):
    """Run config"""
    for device in config:
        config[device].setdefault('device', '')
        config[device].setdefault('user', '')
        config[device].setdefault('password', '')
        config[device].setdefault('keyfile', '')
        config[device].setdefault('device_type', 'linux')
        config[device].setdefault('suite', '')
        config[device].setdefault('output', '')

        suite = SysInfoOutputSuite(config[device]['device'],
                                   config[device]['user'],
                                   config[device]['password'],
                                   config[device]['keyfile'])
        printer = SysInfoPrinter(config[device]['output'])

        if arg.check:
            suite.run_module(config[device]['suite'])
            printer.print_function_check(suite)
        elif arg.listing:
            suite.list_modules()
            printer.print_function_list(suite)
        else:
            suite.run_module(config[device]['suite'])
            printer.print_full_xml_stack(suite)
#        if arg.hashing:
#            printer.print_hash()

if __name__ == "__main__":
    C_ARG = get_args()
    if C_ARG.cimc:
        C_CONF = {"cimc_"+C_ARG.cimc: {'device': C_ARG.cimc,
                                       'device_type': "cimc",
                                       'user': C_ARG.user,
                                       'password': C_ARG.password,
                                       'output': C_ARG.output,
                                       'keyfile': C_ARG.keyfile,
                                       'suite': G_SUITE_UCS}}
    else:
        C_CONF = {"host_"+C_ARG.device: {'device': C_ARG.device,
                                         'device_type': "linux",
                                         'user': C_ARG.user,
                                         'password': C_ARG.password,
                                         'output': C_ARG.output,
                                         'keyfile': C_ARG.keyfile,
                                         'suite': G_SUITE}}
    if C_ARG.interactive:
        C_CONF = run_interactive()
    if C_ARG.json:
        C_CONF = SysInfoConfiguration('').load_json_config(C_ARG.json)
    run_config(C_ARG, C_CONF)
