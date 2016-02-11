# Cisco UCS 240 series BIOS settings

Following namespace and terminology is derived from documentation of Cisco UCS E-series. Output is obtained from Cisco Integrated Management Controller via [XML API](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/e/api/guide/b_cimc_api_book.html). To get the BIOS settings from Cisco UCS 240 series the script is using 'configResolveClass' method from API: `<configResolveClass cookie='cookie_value' inHierarchical='true' classId='__scope__'/>`, where '__scope__' is section to get. Supported scopes are 'biosSettings' and 'computeRackUnit'. Response is requested managed object in a given class.

- **Intel Hyper-Threading Technology**: Whether the processor uses Intel Hyper-Threading Technology, which allows multithreaded software applications to execute threads in parallel within each processor. This can be one of the following: 
	- *Disabled* — The processor does not permit hyperthreading.
	- *Enabled* — The processor allows for the parallel execution of multiple threads.

	`<biosVfIntelHyperThreadingTech rn="Intel-HyperThreading-Tech" vpIntelHyperThreadingTech="disabled" />`

- **Number of Enabled Cores**: Allows you to disable one or more of the physical cores on the server. This can be one of the following:
	- *All* — Enables all physical cores. This also enables Hyper Threading on the associated logical processor cores.
	- *1 through n* — Specifies the number of physical processor cores that can run on the server. Each physical core has an associated logical core.

	`<biosVfCoreMultiProcessing rn="Core-MultiProcessing" vpCoreMultiProcessing="all" />`

- **Execute Disable**: Classifies memory areas on the server to specify where application code can execute. As a result of this classification, the processor disables code execution if a malicious worm attempts to insert code in the buffer. This setting helps to prevent damage, worm propagation, and certain classes of malicious buffer overflow attacks. This can be one of the following:
	- *Disabled* — The processor does not classify memory areas.
	- *Enabled* — The processor classifies memory areas.

	`<biosVfExecuteDisableBit rn="Execute-Disable-Bit" vpExecuteDisableBit="enabled" />`

- **Intel VT**: Whether the processor uses Intel Virtualization Technology (VT), which allows a platform to run multiple operating systems and applications in independent partitions. This can be one of the following:
	- *Disabled* — The processor does not permit virtualization.
	- *Enabled* — The processor allows multiple operating systems in independent partitions.

	`<biosVfIntelVirtualizationTechnology rn="Intel-Virtualization-Technology" vpIntelVirtualizationTechnology="enabled" />`

- **Intel VT-d**: Whether the processor uses Intel Virtualization Technology for Directed I/O (VT-d). This can be one of the following:
	- *Disabled* — The processor does not use virtualization technology.
	- *Enabled* — The processor uses virtualization technology.

	`<biosVfIntelVTForDirectedIO rn="Intel-VT-for-directed-IO" vpIntelVTDATSSupport="enabled" vpIntelVTDCoherencySupport="disabled" vpIntelVTForDirectedIO="enabled" />`

- **Intel VT-d Coherency Support**: Whether the processor supports Intel VT-d Coherency. This can be one of the following:
	- *Disabled* — The processor does not support coherency.
	- *Enabled* — The processor uses VT-d Coherency as required.

	`<biosVfIntelVTForDirectedIO rn="Intel-VT-for-directed-IO" vpIntelVTDATSSupport="enabled" vpIntelVTDCoherencySupport="disabled" vpIntelVTForDirectedIO="enabled" />`

- **Intel VT-d ATS Support**: Whether the processor supports Intel VT-d Address Translation Services (ATS). This can be one of the following:
	- *Disabled* — The processor does not support ATS.
	- *Enabled* — The processor uses VT-d ATS as required.
 
	`<biosVfIntelVTForDirectedIO rn="Intel-VT-for-directed-IO" vpIntelVTDATSSupport="enabled" vpIntelVTDCoherencySupport="disabled" vpIntelVTForDirectedIO="enabled" />`

- **CPU Performance**: Sets the CPU performance profile for the server. The performance profile consists of the following options:
	- DCU Streamer Prefetcher
	- DCU IP Prefetcher
	- Hardware Prefetcher
	- Adjacent Cache-Line Prefetch

	This can be one of the following:
	- *Enterprise* — All options are enabled.
	- *High Throughput* — Only the DCU IP Prefetcher is enabled. The rest of the options are disabled.
	- *HPC* — All options are enabled. This setting is also known as high performance computing.
	- *Custom* — All performance profile options can be configured from the BIOS setup on the server. In addition, the Hardware Prefetcher and Adjacent Cache-Line Prefetch options can be configured in the fields below.

	`<biosVfCPUPerformance rn="CPU-Performance" vpCPUPerformance="enterprise" />`

- **Hardware Prefetcher**: Whether the processor allows the Intel hardware prefetcher to fetch streams of data and instruction from memory into the unified second-level cache when necessary. This can be one of the following:
	- *Disabled* — The hardware prefetcher is not used.
	- *Enabled* — The processor uses the hardware prefetcher when cache issues are detected.

	`<biosVfHardwarePrefetch rn="Hardware-Prefetch" vpHardwarePrefetch="enabled" />`

- **Adjacent Cache Line Prefetcher**: Whether the processor fetches cache lines in even/odd pairs instead of fetching just the required line. This can be one of the following:
	- *Disabled* — The processor only fetches the required line.
	- *Enabled* — The processor fetches both the required line and its paired line.
 
	`<biosVfAdjacentCacheLinePrefetch rn="Adjacent-Cache-Line-Prefetch" vpAdjacentCacheLinePrefetch="enabled" />`

- **DCU Streamer Prefetch**: Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache. This can be one of the following:
	- *Disabled* — The processor does not try to anticipate cache read requirements and only fetches explicitly requested lines.
	- *Enabled* — The DCU prefetcher analyzes the cache read pattern and prefetches the next line in the cache if it determines that it may be needed.

	`<biosVfDCUPrefetch rn="DCU-Prefetch" vpIPPrefetch="enabled" vpStreamerPrefetch="enabled" />`

- **DCU IP Prefetcher**: Whether the processor uses the DCU IP Prefetch mechanism to analyze historical cache access patterns and preload the most relevant lines in the L1 cache. This can be one of the following:
	- *Disabled* — The processor does not preload any cache data.
	- *Enabled* — The DCU IP prefetcher preloads the L1 cache with the data it determines to be the most relevant.

	`<biosVfDCUPrefetch rn="DCU-Prefetch" vpIPPrefetch="enabled" vpStreamerPrefetch="enabled" />`

- **Direct Cache Access Support**: Allows processors to increase I/O performance by placing data from I/O devices directly into the processor cache. This setting helps to reduce cache misses. This can be one of the following:
	- *Disabled* — Data from I/O devices is not placed directly into the processor cache.
	- *Enabled* — Data from I/O devices is placed directly into the processor cache.

	`<biosVfDirectCacheAccess rn="Direct-Cache-Access" vpDirectCacheAccess="enabled" />`

- **Power Technology**: Enables you to configure the CPU power management settings for the following options:
	- *Enhanced Intel Speedstep Technology*
	- *Intel Turbo Boost Technology*
	- *Processor Power State C6*

	Power Technology can be one of the following:
	- *Custom* — The server uses the individual settings for the BIOS parameters mentioned above. You must select this option if you want to change any of these BIOS parameters.
	- *Disabled* — The server does not perform any CPU power management and any settings for the BIOS parameters mentioned above are ignored.
	- *Energy Efficient* — The server determines the best settings for the BIOS parameters mentioned above and ignores the individual settings for these parameters.

	` <biosVfCPUPowerManagement rn="CPU-PowerManagement" vpCPUPowerManagement="disabled" />`

- **Enhanced Intel Speedstep Technology**: Whether the processor uses Enhanced Intel SpeedStep Technology, which allows the system to dynamically adjust processor voltage and core frequency. This technology can result in decreased average power consumption and decreased average heat production. This can be one of the following:
	- *Disabled* — The processor never dynamically adjusts its voltage or frequency.
	- *Enabled* — The processor utilizes Enhanced Intel SpeedStep Technology and enables all supported processor sleep states to further conserve power.
	
	'Note':
	Power Technology must be set to Custom or the server ignores the setting for this parameter.

	`<biosVfEnhancedIntelSpeedStepTech rn="Enhanced-Intel-SpeedStep-Tech" vpEnhancedIntelSpeedStepTech="disabled" />`

- **Intel Turbo Boost Technology**: Whether the processor uses Intel Turbo Boost Technology, which allows the processor to automatically increase its frequency if it is running below power, temperature, or voltage specifications. This can be one of the following:
	- *Disabled* — The processor does not increase its frequency automatically.
	- *Enabled* — The processor utilizes Turbo Boost Technology if required.
	
	'Note':
	Power Technology must be set to Custom or the server ignores the setting for this parameter.

	`<biosVfIntelTurboBoostTech rn="Intel-Turbo-Boost-Tech" vpIntelTurboBoostTech="disabled" />`

- **Processor Power State C6**: Whether the BIOS sends the C6 report to the operating system. When the OS receives the report, it can transition the processor into the lower C6 power state to decrease energy usage while maintaining optimal processor performance. This can be one of the following:
	- *Disabled* — The BIOS does not send the C6 report.
	- *Enabled* — The BIOS sends the C6 report, allowing the OS to transition the processor to the C6 low power state.
	
	'Note':
	Power Technology must be set to Custom or the server ignores the setting for this parameter.

	`<biosVfProcessorC6Report rn="Processor-C6-Report" vpProcessorC6Report="disabled" />`

- **Processor Power State C1 Enhanced**: Whether the CPU transitions to its minimum frequency when entering the C1 state. This can be one of the following:
	- *Disabled* — The CPU continues to run at its maximum frequency in C1 state.
	- *Enabled* — The CPU transitions to its minimum frequency. This option saves the maximum amount of power in C1 state.

	`<biosVfProcessorC1E rn="Processor-C1E" vpProcessorC1E="disabled" />`

- **Frequency Floor Override**: Whether the CPU is allowed to drop below the maximum non-turbo frequency when idle. This can be one of the following:
	- *Disabled* — The CPU can drop below the maximum non-turbo frequency when idle. This option decreases power consumption but may reduce system performance.
	- *Enabled* — The CPU cannot drop below the maximum non-turbo frequency when idle. This option improves system performance but may increase power consumption.

	`<biosVfCPUFrequencyFloor rn="CPU-FreqFloor" vpCPUFrequencyFloor="enabled" />`

- **P-STATE Coordination**: Allows you to define how BIOS communicates the P-state support model to the operating system. There are 3 models as defined by the Advanced Configuration and Power Interface (ACPI) specification.
	- *HW_ALL*—The processor hardware is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a package).
	- *SW_ALL*—The OS Power Manager (OSPM) is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a physical package), and must initiate the transition on all of the logical processors.
	- *SW_ANY*—The OS Power Manager (OSPM) is responsible for coordinating the P-state among logical processors with dependencies (all logical processors in a package), and may initiate the transition on any of the logical processors in the domain.
	
	'Note':
	Power Technology must be set to Custom or the server ignores the setting for this parameter.

	`<biosVfPStateCoordType rn="p-state-coord" vpPStateCoordType="HW ALL" />`

- **Energy Performance**: Allows you to determine whether system performance or energy efficiency is more important on this server. This can be one of the following: 
	- *Balanced Energy*
	- *Balanced Performance*
	- *Energy Efficient*
	- *Performance*

	`<biosVfCPUEnergyPerformance rn="CPU-EngPerfBias" vpCPUEnergyPerformance="performance" />`

- **Select Memory RAS**: How the memory reliability, availability, and serviceability (RAS) is configured for the server. This can be one of the following:
	- *Maximum Performance* — System performance is optimized.
	- *Mirroring* — System reliability is optimized by using half the system memory as backup.
	- *Lockstep* — If the DIMM pairs in the server have an identical type, size, and organization and are populated across the SMI channels, you can enable lockstep mode to minimize memory access latency and provide better performance. This option offers better system performance than Mirroring and better reliability than Maximum Performance but lower reliability than Mirroring and lower system performance than Maximum Performance.

	`<biosVfSelectMemoryRASConfiguration rn="SelectMemory-RAS-configuration" vpSelectMemoryRASConfiguration="maximum-performance" />`

- **DRAM Clock Throttling**: Allows you to tune the system settings between the memory bandwidth and power consumption. This can be one of the following:
	- *Balanced* — DRAM clock throttling is reduced, providing a balance between performance and power.
	- *Performance* — DRAM clock throttling is disabled, providing increased memory bandwidth at the cost of additional power.
	- *Energy Efficient* — DRAM clock throttling is increased to improve energy efficiency.

	`<biosVfDRAMClockThrottling rn="DRAM-Clock-Throttling" vpDRAMClockThrottling="Balanced" />`

- **NUMA**: Whether the BIOS supports NUMA. This can be one of the following:
	- *Disabled* — The BIOS does not support NUMA.
	- *Enabled* — The BIOS includes the ACPI tables that are required for NUMA-aware operating systems. If you enable this option, the system must disable Inter-Socket Memory interleaving on some platforms.

	`<biosVfNUMAOptimized rn="NUMA-optimized" vpNUMAOptimized="enabled" />`

- **Low Voltage DDR Mode**: Whether the system prioritizes low voltage or high frequency memory operations. This can be one of the following:
	- *Power Saving Mode* — The system prioritizes low voltage memory operations over high frequency memory operations. This mode may lower memory frequency in order to keep the voltage low.
	- *Performance Mode* — The system prioritizes high frequency operations over low voltage operations.

	`<biosVfNUMAOptimized rn="NUMA-optimized" vpNUMAOptimized="enabled" />`

- **DRAM Refresh rate**: Allows you to set the rate at which the DRAM cells are refreshed. This can be one of the following: 
	- 1x—DRAM cells are refreshed every 64ms.
	- 2x—DRAM cells are refreshed every 32ms.
	- 3x—DRAM cells are refreshed every 21ms.
	- 4x—DRAM cells are refreshed every 16ms.
	Auto—DRAM cells refresh rate is automatically chosen by the BIOS based on the system configuration. This is the recommended setting for this parameter.

	`<biosVfDramRefreshRate rn="dram-refresh-rate" vpDramRefreshRate="2x" />`

- **Channel Interleaving**: Whether the CPU divides memory blocks and spreads contiguous portions of data across interleaved channels to enable simultaneous read operations. This can be one of the following:
	- *Auto* — The CPU determines what interleaving is done.
	- *1 Way* — Some channel interleaving is used.
	- *2 Way*
	- *3 Way*
	- *4 Way* — The maximum amount of channel interleaving is used.

	`<biosVfMemoryInterleave rn="Memory-Interleave" vpChannelInterLeave="auto" vpRankInterLeave="auto" />`

- **Rank Interleaving**: Whether the CPU interleaves physical ranks of memory so that one rank can be accessed while another is being refreshed. This can be one of the following:
	- *Auto—The CPU determines what interleaving is done.
	- *1 Way—Some rank interleaving is used.
	- *2 Way*
	- *4 Way*
	- *8 Way* — The maximum amount of rank interleaving is used.

	`<biosVfMemoryInterleave rn="Memory-Interleave" vpChannelInterLeave="auto" vpRankInterLeave="auto" />`

- **Patrol Scrub**: Whether the system actively searches for, and corrects, single bit memory errors even in unused portions of the memory on the server. This can be one of the following:
	- *Disabled* — The system checks for memory ECC errors only when the CPU reads or writes a memory address.
	- *Enabled* — The system periodically reads and writes memory searching for ECC errors. If any errors are found, the system attempts to fix them. This option may correct single bit errors before they become multi-bit errors, but it may adversely affect performance when the patrol scrub is running.

	`<biosVfPatrolScrub rn="Patrol-Scrub-Param" vpPatrolScrub="enabled" />`

- **Demand Scrub**: Whether the system corrects single bit memory errors encountered when the CPU or I/O makes a demand read. This can be one of the following:
	- *Disabled* — Single bit memory errors are not corrected.
	- *Enabled* — Single bit memory errors are corrected in memory and the corrected data is set in response to the demand read.

	`<biosVfDemandScrub rn="Demand-Scrub-Param" vpDemandScrub="enabled" />`

- **Altitude**: The approximate number of meters above sea level at which the physical server is installed. This can be one of the following:
	- *Auto* — The CPU determines the physical elevation.
	- *300 M* — The server is approximately 300 meters above sea level.
	- *900 M* — The server is approximately 900 meters above sea level.
	- *1500 M* — The server is approximately 1500 meters above sea level.
	- *3000 M* — The server is approximately 3000 meters above sea level.

	`<biosVfAltitude rn="Altitude-Param" vpAltitude="300-m" />`

- **QPI Link Frequency**: The Intel QuickPath Interconnect (QPI) link frequency, in gigatransfers per second (GT/s). This can be one of the following:
	- *Auto* — The CPU determines the QPI link frequency.
	- *6.4 GT/s*
	- *7.2 GT/s*
	- *8.0 GT/s*

	`<biosVfQPIConfig rn="QPI-Config" vpQPILinkFrequency="auto" />`

- **Onboard SCU Storage Support**: Whether the onboard software RAID controller is available to the server. This can be one of the following:
	- *Disabled* — The software RAID controller is not available.
	- *Enabled* — The software RAID controller is available.

	`<biosVfOnboardStorage rn="Onboard-Storage" vpOnboardSCUStorageSupport="disabled" />`

- **Legacy USB Support**: Whether the system supports legacy USB devices. This can be one of the following:
	- *Disabled* — USB devices are only available to EFI applications.
	- *Enabled* — Legacy USB support is always available.
	- *Auto* — Disables legacy USB support if no USB devices are connected.

	`<biosVfLegacyUSBSupport rn="LegacyUSB-Support" vpLegacyUSBSupport="enabled" />`

- **Port 60/64 Emulation**: Whether the system supports 60h/64h emulation for complete USB keyboard legacy support. This can be one of the following:
	- *Disabled* — 60h/64 emulation is not supported.
	- *Enabled* — 60h/64 emulation is supported. You should select this option if you are using a non-USB aware operating system on the server.

	`<biosVfUSBEmulation rn="USBEmulation-Support" vpUSBEmul6064="enabled" />`

- **All USB Devices**: Whether all physical and virtual USB devices are enabled or disabled. This can be one of the following:
	- *Disabled* — All USB devices are disabled.
	- *Enabled* — All USB devices are enabled.

	`<biosVfUSBPortsConfig rn="USB-Ports-Config" vpAllUsbDevices="enabled" vpUsbPortFront="enabled" vpUsbPortInternal="enabled" vpUsbPortKVM="enabled" vpUsbPortRear="enabled" vpUsbPortSDCard="enabled" vpUsbPortVMedia="enabled" />`

- **USB Port**: Rear: Whether the rear panel USB devices are enabled or disabled. This can be one of the following: 
	- *Disabled* — Disables the rear panel USB ports. Devices connected to these ports are not detected by the BIOS and operating system.
	- *Enabled* — Enables the rear panel USB ports. Devices connected to these ports are detected by the BIOS and operating system.

	`<biosVfUSBPortsConfig rn="USB-Ports-Config" vpAllUsbDevices="enabled" vpUsbPortFront="enabled" vpUsbPortInternal="enabled" vpUsbPortKVM="enabled" vpUsbPortRear="enabled" vpUsbPortSDCard="enabled" vpUsbPortVMedia="enabled" />`

- **USB Port: Front**: Whether the front panel USB devices are enabled or disabled. This can be one of the following: 
	- *Disabled* — Disables the front panel USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
	- *Enabled* — Enables the front panel USB ports. Devices connected to these ports are detected by the BIOS and operating system. 

	`<biosVfUSBPortsConfig rn="USB-Ports-Config" vpAllUsbDevices="enabled" vpUsbPortFront="enabled" vpUsbPortInternal="enabled" vpUsbPortKVM="enabled" vpUsbPortRear="enabled" vpUsbPortSDCard="enabled" vpUsbPortVMedia="enabled" />`

- **USB Port: Internal**: Whether the internal USB devices are enabled or disabled. This can be one of the following: 
	- *Disabled* — Disables the internal USB ports. Devices connected to these ports are not detected by the BIOS and operating system. 
	- *Enabled* — Enables the internal USB ports. Devices connected to these ports are detected by the BIOS and operating system.

	`<biosVfUSBPortsConfig rn="USB-Ports-Config" vpAllUsbDevices="enabled" vpUsbPortFront="enabled" vpUsbPortInternal="enabled" vpUsbPortKVM="enabled" vpUsbPortRear="enabled" vpUsbPortSDCard="enabled" vpUsbPortVMedia="enabled" />`

- **USB Port: KVM**: Whether the KVM ports are enabled or disabled. This can be one of the following:
	- *Disabled* — Disables the KVM keyboard and/or mouse devices. Keyboard and/or mouse will not work in the KVM window.
	- *Enabled* — Enables the KVM keyboard and/or mouse devices.

	`<biosVfUSBPortsConfig rn="USB-Ports-Config" vpAllUsbDevices="enabled" vpUsbPortFront="enabled" vpUsbPortInternal="enabled" vpUsbPortKVM="enabled" vpUsbPortRear="enabled" vpUsbPortSDCard="enabled" vpUsbPortVMedia="enabled" />`

- **USB Port: VMedia**: Whether the virtual media devices are enabled or disabled. This can be one of the following:
	- *Disabled* — Disables the vMedia devices.
	- *Enabled* — Enables the vMedia devices.

	`<biosVfUSBPortsConfig rn="USB-Ports-Config" vpAllUsbDevices="enabled" vpUsbPortFront="enabled" vpUsbPortInternal="enabled" vpUsbPortKVM="enabled" vpUsbPortRear="enabled" vpUsbPortSDCard="enabled" vpUsbPortVMedia="enabled" />`

- **USB Port: SD Card**: Whether the SD card drives are enabled or disabled. This can be one of the following:
	- *Disabled* — Disables the SD card drives. The SD card drives are not detected by the BIOS and operating system.
	- *Enabled* — Enables the SD card drives.

	`<biosVfUSBPortsConfig rn="USB-Ports-Config" vpAllUsbDevices="enabled" vpUsbPortFront="enabled" vpUsbPortInternal="enabled" vpUsbPortKVM="enabled" vpUsbPortRear="enabled" vpUsbPortSDCard="enabled" vpUsbPortVMedia="enabled" />`

- **Memory Mapped I/O Above 4GB**: Whether to enable or disable MMIO above 4GB or not. This can be one of the following:
	- *Disabled* — The server does not map I/O of 64-bit PCI devices to 4GB or greater address space.
	- *Enabled* — The server maps I/O of 64-bit PCI devices to 4GB or greater address space.
	Note
	PCI devices that are 64-bit compliant but use a legacy option ROM may not function correctly with this setting enabled.

	`<biosVfMemoryMappedIOAbove4GB rn="Memory-mapped-IO-above-4GB" vpMemoryMappedIOAbove4GB="disabled" />`

- **MMCFG BASE**: Sets the low base address for PCIe adapters within 4GB. This can be one of the following: 
	- *1 GB*
	- *2 GB*
	- *2.5 GB*
	- *3 GB*
	- *Auto* — Automatically sets the low base address for PCIe adapters.
	Note
	This is valid for C240 servers only.

	`<biosVfMMCFGBase rn="MMCFG-Base" vpMMCFGBase="1 GB" />`

- **ASPM Support**: Allows you to set the level of ASPM (Active Power State Management) support in the BIOS. This can be one of the following:
	- *Disabled* — ASPM support is disabled in the BIOS.
	- *Force L0s* — Force all links to L0 standby (L0s) state.
	- *Auto* — The CPU determines the power state.

	`<biosVfASPMSupport rn="ASPM-Support" vpASPMSupport="Disabled" />`

- **VGA Priority**: Allows you to set the priority for VGA graphics devices if multiple VGA devices are found in the system. This can be one of the following:
	- *Onboard* — Priority is given to the onboard VGA device. BIOS post screen and OS boot are driven through the onboard VGA port.
	- *Offboard* — Priority is given to the PCIE Graphics adapter. BIOS post screen and OS boot are driven through the external graphics adapter port.
	- *Onboard VGA Disabled* — Priority is given to the PCIE Graphics adapter, and the onboard VGA device is disabled.
	Note
	The vKVM does not function when the onboard VGA is disabled.

	`<biosVfVgaPriority rn="VgaPriority" vpVgaPriority="Onboard" />`

- **Console Redirection**: Allows a serial port to be used for console redirection during POST and BIOS booting. After the BIOS has booted and the operating system is responsible for the server, console redirection is irrelevant and has no effect. This can be one of the following:
	- *Disabled* — No console redirection occurs during POST.
	- *COM 0* — Enables console redirection on COM port 0 during POST.
        - *COM 1* — Enables console redirection on COM port 1 during POST.
 
	`<biosVfConsoleRedirection rn="Console-redirection" vpBaudRate="115200" vpConsoleRedirection="disabled" vpFlowControl="none" vpPuttyKeyPad="ESCN" vpRedirectionAfterPOST="Always Enable" vpTerminalType="vt100" />`

- **Terminal Type**: What type of character formatting is used for console redirection. This can be one of the following: 
	- *PC-ANSI* — The PC-ANSI terminal font is used.
	- *VT100* — A supported vt100 video terminal and its character set are used.
	- *VT100+* — A supported vt100-plus video terminal and its character set are used.
	- *VT-UTF8* — A video terminal with the UTF-8 character set is used.
	Note
	This setting must match the setting on the remote terminal application.
 
	`<biosVfConsoleRedirection rn="Console-redirection" vpBaudRate="115200" vpConsoleRedirection="disabled" vpFlowControl="none" vpPuttyKeyPad="ESCN" vpRedirectionAfterPOST="Always Enable" vpTerminalType="vt100" />`

- **Bits per second**: What BAUD rate is used for the serial port transmission speed. If you disable Console Redirection, this option is not available. This can be one of the following:
 	- *9600* — A 9,600 BAUD rate is used.
	- *19200* — A 19,200 BAUD rate is used.
	- *38400* — A 38,400 BAUD rate is used.
	- *57600* — A 57,600 BAUD rate is used.
	- *115200* — A 115,200 BAUD rate is used.
	Note
	This setting must match the setting on the remote terminal application.

	`<biosVfConsoleRedirection rn="Console-redirection" vpBaudRate="115200" vpConsoleRedirection="disabled" vpFlowControl="none" vpPuttyKeyPad="ESCN" vpRedirectionAfterPOST="Always Enable" vpTerminalType="vt100" />`

- **Flow Control**: Whether a handshake protocol is used for flow control. Request to Send / Clear to Send (RTS/CTS) helps to reduce frame collisions that can be introduced by a hidden terminal problem. This can be one of the following:
	- *None* — No flow control is used.
	- *Hardware RTS/CTS* — RTS/CTS is used for flow control.
	Note
	This setting must match the setting on the remote terminal application.

	`<biosVfConsoleRedirection rn="Console-redirection" vpBaudRate="115200" vpConsoleRedirection="disabled" vpFlowControl="none" vpPuttyKeyPad="ESCN" vpRedirectionAfterPOST="Always Enable" vpTerminalType="vt100" />`

- **Putty KeyPad**: Allows you to change the action of the PuTTY function keys and the top row of the numeric keypad. This can be one of the following:
	- *VT100* — The function keys generate ESC OP through ESC O[.
	- *LINUX* — Mimics the Linux virtual console. Function keys F6 to F12 behave like the default mode, but F1 to F5 generate ESC [[A through ESC [[E.
	- *XTERMR6* — Function keys F5 to F12 behave like the default mode. Function keys F1 to F4 generate ESC OP through ESC OS, which are the sequences produced by the top row of the keypad on Digital terminals.
	- *SCO* — The function keys F1 to F12 generate ESC [M through ESC [X. The function and shift keys generate ESC [Y through ESC [j. The control and function keys generate ESC [k through ESC [v. The shift, control and function keys generate ESC [w through ESC [{.
	- *ESCN* — The default mode. The function keys match the general behavior of Digital terminals. The function keys generate sequences such as ESC [11~ and ESC [12~.
	- *VT400* — The function keys behave like the default mode. The top row of the numeric keypad generates ESC OP through ESC OS.
 
	`<biosVfConsoleRedirection rn="Console-redirection" vpBaudRate="115200" vpConsoleRedirection="disabled" vpFlowControl="none" vpPuttyKeyPad="ESCN" vpRedirectionAfterPOST="Always Enable" vpTerminalType="vt100" />`

- **Redirection After BIOS POST**: Whether BIOS console redirection should be active after BIOS POST is complete and control given to the OS bootloader. This can be one of the following:
	- *Always Enable* — BIOS Legacy console redirection is active during the OS boot and run time.
	- *Bootloader* — BIOS Legacy console redirection is disabled before giving control to the OS boot loader.
 
	`<biosVfConsoleRedirection rn="Console-redirection" vpBaudRate="115200" vpConsoleRedirection="disabled" vpFlowControl="none" vpPuttyKeyPad="ESCN" vpRedirectionAfterPOST="Always Enable" vpTerminalType="vt100" />`

- **Out-of-Band Mgmt Port**: Allows you to configure the COM port 0 that can be used for Windows Emergency Management services. ACPI SPCR table is reported based on this setup option. This can be one of the following:
	- *Disabled* — Configures the COM port 0 as a general purpose port for use with the Windows Operating System.
	- *Enabled* — Configures the COM port 0 as a remote management port for Windows Emergency Management services.

	`<biosVfOutOfBandMgmtPort rn="OoB-MgmtPort" vpOutOfBandMgmtPort="Enabled" />`

- **All Onboard LOM Ports**: Whether all LOM ports are enabled or disabled. This can be one of the following:
	- *Disabled* — All LOM ports are disabled.
	- *Enabled* — All LOM ports are enabled.

- **LOM Port n OptionROM**: Whether Option ROM is available on the LOM port designated by n. This can be one of the following:
	- *Disabled* — The expansion slot n is not available.
	- *Enabled* — The expansion slot n is available.
	- *UEFI Only* — The expansion slot n is available for UEFI only.
	- *Legacy Only* — The expansion slot n is available for legacy only.

	`<biosVfLOMPortOptionROM rn="LOMPort-OptionROM" vpLOMPort0State="Enabled" vpLOMPort1State="Enabled" vpLOMPort2State="Enabled" vpLOMPort3State="Enabled" vpLOMPortsAllState="Enabled" />`

- **All PCIe Slots OptionROM**: Whether the server can use the PCIe Option ROM expansion slots. This can be one of the following:
	- *Disabled* — The expansion slot n is not available.
	- *Enabled* — The expansion slot n is available.
	- *UEFI Only* — The expansion slot n is available for UEFI only.
	- *Legacy Only* — The expansion slot n is available for legacy only.

	`<biosVfPCIOptionROMs rn="PCI-OptionROMs" vpPCIOptionROMs="Enabled" />`

- **PCIe Slot:n OptionROM**: Whether PCIe expansion slot n is available to the server. This can be one of the following:
	- *Disabled* — The expansion slot n is not available.
	- *Enabled* — The expansion slot n is available.
	- *UEFI Only* — The expansion slot n is available for UEFI only.
	- *Legacy Only* — The expansion slot n is available for legacy only.

	`<biosVfPCISlotOptionROMEnable rn="PCI-Slot-OptionROM-Enable" vpSlot1LinkSpeed="GEN3" vpSlot1State="Enabled" vpSlot2LinkSpeed="GEN3" vpSlot2State="Enabled" vpSlot3LinkSpeed="GEN3" vpSlot3State="Enabled" vpSlot4LinkSpeed="GEN3" vpSlot4State="Enabled" vpSlot5LinkSpeed="GEN3" vpSlot5State="Enabled" vpSlotMezzState="Enabled" />`

- **PCIe Mezzanine OptionROM**: Whether the PCIe mezzanine slot expansion ROM is available to the server. This can be one of the following:
	- *Disabled* — The expansion slot n is not available.
	- *Enabled* — The expansion slot n is available.
	- *UEFI Only* — The expansion slot n is available for UEFI only.
	- *Legacy Only* — The expansion slot n is available for legacy only.

	`<biosVfPCISlotOptionROMEnable rn="PCI-Slot-OptionROM-Enable" vpSlot1LinkSpeed="GEN3" vpSlot1State="Enabled" vpSlot2LinkSpeed="GEN3" vpSlot2State="Enabled" vpSlot3LinkSpeed="GEN3" vpSlot3State="Enabled" vpSlot4LinkSpeed="GEN3" vpSlot4State="Enabled" vpSlot5LinkSpeed="GEN3" vpSlot5State="Enabled" vpSlotMezzState="Enabled" />`

- **PCIe Slot:n Link Speed**: This option allows you to restrict the maximum speed of an adapter card installed in PCIe slot n. This can be one of the following:
	- *GEN1* — 2.5GT/s (gigatransfers per second) is the maximum speed allowed.
	- *GEN2* — 5GT/s is the maximum speed allowed.
	- *GEN3* — 8GT/s is the maximum speed allowed.
	- *Disabled* — The maximum speed is not restricted.
	For example, if you have a 3rd generation adapter card in PCIe slot 2 that you want to run at a maximum of 5GT/s instead of the 8GT/s that card supports, set the PCIe Slot 2 Link Speed to GEN2. The system then ignores the card's supported maximum speed of 8GT/s and forces it to run at a maximum of 5 GT/s.

	`<biosVfPCISlotOptionROMEnable rn="PCI-Slot-OptionROM-Enable" vpSlot1LinkSpeed="GEN3" vpSlot1State="Enabled" vpSlot2LinkSpeed="GEN3" vpSlot2State="Enabled" vpSlot3LinkSpeed="GEN3" vpSlot3State="Enabled" vpSlot4LinkSpeed="GEN3" vpSlot4State="Enabled" vpSlot5LinkSpeed="GEN3" vpSlot5State="Enabled" vpSlotMezzState="Enabled" />`

- **CDN**: Whether the Ethernet Network naming convention is according to Consistent Device Naming (CDN) or the traditional way of naming conventions. This can be one of the following:
	- *Disabled* — OS Ethernet Networking Identifier is named in a default convention as ETH0, ETH1 etc. By default, CDN option is disabled.
	- *Enabled* — OS Ethernet Network identifier is named in a consistent device naming (CDN) according to the physical LAN on Motherboard(LOM) port numbering; LOM Port 0, LOM Port 1, etc.
	Note
	CDN is enabled for LOM ports and works with Windows 2012 or the latest OS only.

	`<biosVfCDNSupport rn="CDN-Support" vpCDNSupport="Disabled" />`

- **TPM Support**: TPM (Trusted Platform Module) is a microchip designed to provide basic security-related functions primarily involving encryption keys. This option allows you to control the TPM Security Device support for the system. It can be one of the following:
	- *Disabled* — The server does not use the TPM.
	- *Enabled* — The server uses the TPM.
	Note
	We recommend that you contact your operating system vendor to make sure the operating system supports this feature.
 
 	`<biosVfTPMSupport rn="TPM-Support" vpTPMSupport="disabled" />`

- **FRB-2 Timer**: Whether the FRB2 timer is used by Cisco IMC to recover the system if it hangs during POST. This can be one of the following:
	- *Disabled* — The FRB2 timer is not used.
	- *Enabled* — The FRB2 timer is started during POST and used to recover the system if necessary.

	`<biosVfFRB2Enable rn="FRB2-Enable" vpFRB2Enable="enabled" />`

- **OS Watchdog Timer**: Whether the BIOS programs the watchdog timer with a specified timeout value. This can be one of the following:
	- *Disabled* — The watchdog timer is not used to track how long the server takes to boot.
	- *Enabled* — The watchdog timer tracks how long the server takes to boot. If the server does not boot within the length of time specified in the OS Boot Watchdog Timer Timeout field, the Cisco IMC logs an error and takes the action specified in the OS Boot Watchdog Policy field.

	`<biosVfOSBootWatchdogTimer rn="OS-Boot-Watchdog-Timer-Param" vpOSBootWatchdogTimer="disabled" />`

- **OS Watchdog Timer Timeout**: What timeout value the BIOS uses to configure the watchdog timer. This can be one of the following:
	- *5 Minutes* — The watchdog timer expires 5 minutes after the OS begins to boot.
	- *10 Minutes* — The watchdog timer expires 10 minutes after the OS begins to boot.
	- *15 Minutes* — The watchdog timer expires 15 minutes after the OS begins to boot.
	- *20 Minutes* — The watchdog timer expires 20 minutes after the OS begins to boot. 
	Note
	This option is only applicable if you enable the OS Boot Watchdog Timer.

	`<biosVfOSBootWatchdogTimerTimeout rn="OS-Boot-Watchdog-Timer-Time-Out" vpOSBootWatchdogTimerTimeout="10-minutes" />`

- **OS Watchdog Timer Policy**: What action the system takes if the watchdog timer expires. This can be one of the following:
	- *Do Nothing* — The server takes no action if the watchdog timer expires during OS boot.
	- *Power Down* — The server is powered off if the watchdog timer expires during OS boot.
	- *Reset* — The server is reset if the watchdog timer expires during OS boot.
	Note
	This option is only applicable if you enable the OS Boot Watchdog Timer.

	`<biosVfOSBootWatchdogTimerPolicy rn="OS-Boot-Watchdog-Timer-Policy" vpOSBootWatchdogTimerPolicy="power-off" />`
