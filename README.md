# System information suite

- [What is it?](#what-is-it)
- [The Latest Version](#the-latest-version)
- [Downloading](#downloading)
- [Prerequisities](#prerequisities)
- [Implementation](#implementation)
- [Configuration file](#configuration-file)
- [Output](#output)
- [Usage](#usage)
- [Changes](#changes)
- [License](#license)
- [Author and contacts](#author-and-contacts)
- [Version](#version)


##  What is it?
Collect system information suite is Python written collection of scripts to gather, collect and analyze system information from local or remote system running Linux operating system. Output of the script is XML structured information stack of running environment.


## The Latest Version
Details of the latest version can be found on this [GitHub](https://github.com/pmikus/sys-info-suite).


## Downloading
Script can be downloaded from this [GitHub](https://github.com/pmikus/sys-info-suite).


## Prerequisities
To be able to run the script at its latest version, following applications and libraries are essential:

- Python version 2.6.6+
	- Installation under Ubuntu/Debian: `sudo apt-get install python`
	- Installation under Fedora/RHEL/CentOS: `sudo yum install python`

- [Paramiko SSH library](https://github.com/paramiko/paramiko/)
	- Installation via PIP:	`pip install paramiko`
	- Installation under Ubuntu/Debian: `sudo apt-get install python-paramiko`
	- Installation under Fedora/RHEL/CentOS: `sudo yum install pyhton-paramiko`

- Argparse (required for Python version less than 2.7)
	- Installation via PIP:	`pip install argparse`
	- Installation under Ubuntu/Debian: `sudo apt-get install python-argparse`
	- Installation under Fedora/RHEL/CentOS: `sudo apt-get install python-argparse`


## Implementation
Implementation and design details can be found in [DESIGN.md](https://github.com/pmikus/sys-info-suite/blob/master/DESIGN.md).


## Configuration file
Script does support load/save configuration from/to file. Running script in interactive mode with parameter `--interactive` allows user to answer questions regarding setup and this setup could be saved to file. Running script with parameter `--json` will load JSON format file with configuration. Configuration can contain more devices specified. For running on local host leave the 'device' field empty. Sample configuration file:

```json
{
	"device_name1": {
		"user": "user_name",
		"device_type": "linux|cimc",
		"suite": [
			"function1",
			"function2"
			],
		"keyfile": "path_to_keyfile",
		"device": "device_name_or_IP (blank for localhost)",
		"output": "output_file.xml",
		"password": "user_password"
	}
}
```


## Output
### XML format
Format of output is XML. Root element is called 'stack' and has attribute 'host' and 'script_version'. Functions are categorized into sections, sorted by significance and appended into section element. Each function element has id attribute of function name, significance (number) time of execution (in UTC) and implementation version. It contains subelements execution shell exit code, execution command and standard output or standard error output (std.out, std.err). Outputs from commands and commands itself are escaped in CDATA as per [XML specification](http://www.w3schools.com/XML/dom_cdatasection.asp). Purpose of this escapement is to do not parse the content.
```
<stack host="localhost" script_version="n.n.n">
  <section id="n" name="__name__">
    <function id="_name_" significance="_n_" time="yyyy-mm-dd HH:MM:SS.MMMMM UTC" version="1.0.0">
      <exec_command>&lt;![CDATA[data]]&gt;</exec_command>
      <exec_return_code>0</exec_return_code>
      <exec_output>&lt;![CDATA[data]]&gt;</exec_output>
    </function>
  </section>
  ...
</stack>
 ```

### CIMC inventory output
Following name-space and terminology is derived from documentation of Cisco UCS E-series. Output is obtained from Cisco Integrated Management Controller via [XML API](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/e/api/guide/b_cimc_api_book.html). To get the CIMC inventory from Cisco UCS 240 series the script is using 'configResolveClass' method from API: `<configResolveClass cookie='cookie_value' inHierarchical='true' classId='__scope__'/>`, where '__scope__' is section to get. Supported scopes are 'network_adapter_unit', 'equipment_psu', 'equipment_fan_module', 'compute_board', 'mgmt_controller', 'bios_unit, 'pci_equip_slot, and full inventory stack 'compute_rack_unit'. Response is requested managed object in a given class.

Name-space documentation and description can be found in [CIMC.md](https://github.com/pmikus/sys-info-suite/blob/master/CIMC.md).

## Usage
### Collect.py
```
usage: collect.py [-h] [--device DEVICE] [--cimc CIMC] [--user USER]
                  [--password PASSWORD] [--check] [--interactive] [--listing]
                  [--hashing] [--output FILE] [--keyfile FILE] [--json JSON]
                  [--version]

Script for gathering the running configuration from host

optional arguments:
  -h, --help           show this help message and exit
  --check              check if functions are supported
  --interactive        run script in interactive mode
  --listing            list abvailable functions
  --hashing            print hash of output
  --output FILE        redirect the output to a file
  --keyfile FILE       specify SSH key file for authentication
  --json JSON          json configuration file
  --version            show program's version number and exit

Authentication for device:
  --device DEVICE      HOST device to get the information from
  --cimc CIMC          CIMC device to get the BIOS information
  --user USER
  --password PASSWORD
```

Example of getting info from local host:
```
./collect.py
```
Example of getting info from remote host via SSH (host.remote.com):
```
./collect.py --device host.remote.com --user user --password Pass123
```
Example of getting info from remote host and authenticate with private key:
```
./collect.py --device host.remote.com --user user --keyfile ~/.ssh/custom_id_rsa
```
Example of getting bios information from remote CIMC (host.remote.com) and redirect output to file called output.xml:
```
./collect.py --cimc host.remote.com --user user --password Pass123 --output output.xml
```
Example of checking the commands availability and its return codes:
```
./collect.py --device host.remote.com --user user123 --password Pass123 --check
```
Example of running script in interactive mode with check option:
```
./collect.py --interactive --check
```
Example of running script and loading configuration from file:
```
./collect.py --json file.json
```
Example of running script and list all available functions:
```
./collect.py --listing
```


### Diff.py:
```
usage: diff.py [-h] --first FILE1 --second FILE2 [--section SECTION]
               [--function FUNCTION] [--xpath XPATH]
               [--significance SIGNIFICANCE] [--listing] [--width WIDTH]
               [--changes] [--output FILE] [--version]

Script for comparing captured information

optional arguments:
  -h, --help            show this help message and exit
  --first FILE1         First file to compare
  --second FILE2        Second file to compare
  --section SECTION     Display specific section
  --function FUNCTION   Display specific function
  --xpath XPATH         XPath expression filter
  --significance SIGNIFICANCE
                        Display specific function
  --listing             Display available functions
  --width WIDTH         Set the width of the columns
  --changes             Display only changes
  --output FILE         Redirect the output to a file
  --version             show program's version number and exit
```

Example of running diff.py script to compare two files:
```
./diff.py --first host1.xml --second host2.xml
```
Example of running diff.py script to compare two files and write output to file:
```
./diff.py --first host1.xml --second host2.xml --output out.xml
```
Example of running diff.py script to compare two files and set column width to 600c (default value is 230):
```
./diff.py --first host1.xml --second host2.xml --width 600
```
Example of running diff.py script to compare two files: select section 1:
```
./diff.py --first host1.xml --second host2.xml --section 1
```
Example of running diff.py script to compare two files: select all functions that have id=lscpu
```
./diff.py --first host1.xml --second host2.xml --function lscpu
```
Example of running diff.py script to compare two files: select all function elements which are child of section and have significance 1
```
./sys_info/diff.py --first host1.xml --second host2.xml --xpath "//section/function[contains(@significance, '1')]"
```

## Changes
For the full list of changes please read the [NEWS](https://github.com/pmikus/sys-info-suite/blob/master/NEWS) file.

## License
Contect of this repository is licensed under GPLv3. Please read the file called [LICENSE](https://github.com/pmikus/sys-info-suite/blob/master/LICENSE) for full version.

## Author and contacts
Peter Mikus <pmikus@cisco.com>. Complete list of contributors and co-authors is located in file [AUTHORS.md](https://github.com/pmikus/sys-info-suite/blob/master/AUTHORS.md)

## Version
Collect system information script 2.1.0, released May 2016.
