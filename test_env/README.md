# Launch the test environment

Simply :

```bash
./run.sh

[    0.000000] Initializing cgroup subsys cpuset
[    0.000000] Initializing cgroup subsys cpu
[    0.000000] Linux version 3.2.0 (seb@seb-AE8) (gcc version 4.9.4 (GCC) ) #19 SMP Mon May 26 16:54:16 CEST 2025
[    0.000000] Command line: console=ttyS0 console=/dev/console init=/test.sh
[    0.000000] BIOS-provided physical RAM map:
[    0.000000]  BIOS-e820: 0000000000000000 - 000000000009fc00 (usable)
[    0.000000]  BIOS-e820: 000000000009fc00 - 00000000000a0000 (reserved)
[    0.000000]  BIOS-e820: 00000000000f0000 - 0000000000100000 (reserved)
[    0.000000]  BIOS-e820: 0000000000100000 - 000000001ffdd000 (usable)
[    0.000000]  BIOS-e820: 000000001ffdd000 - 0000000020000000 (reserved)
[    0.000000]  BIOS-e820: 00000000fffc0000 - 0000000100000000 (reserved)
[    0.000000]  BIOS-e820: 000000fd00000000 - 0000010000000000 (reserved)
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] DMI not present or invalid.
[    0.000000] No AGP bridge found
[    0.000000] last_pfn = 0x1ffdd max_arch_pfn = 0x400000000
[    0.000000] x86 PAT enabled: cpu 0, old 0x7040600070406, new 0x7010600070106
[    0.000000] found SMP MP-table at [ffff8800000f5470] f5470
[    0.000000] init_memory_mapping: 0000000000000000-000000001ffdd000
[    0.000000] RAMDISK: 1f63e000 - 1ffd0000
[    0.000000] ACPI: RSDP 00000000000f5290 00014 (v00 BOCHS )
[    0.000000] ACPI: RSDT 000000001ffe1c46 00034 (v01 BOCHS  BXPC     00000001 BXPC 00000001)
[    0.000000] ACPI: FACP 000000001ffe1afa 00074 (v01 BOCHS  BXPC     00000001 BXPC 00000001)
[    0.000000] ACPI: DSDT 000000001ffe0040 01ABA (v01 BOCHS  BXPC     00000001 BXPC 00000001)
[    0.000000] ACPI: FACS 000000001ffe0000 00040
[    0.000000] ACPI: APIC 000000001ffe1b6e 00078 (v03 BOCHS  BXPC     00000001 BXPC 00000001)
[    0.000000] ACPI: HPET 000000001ffe1be6 00038 (v01 BOCHS  BXPC     00000001 BXPC 00000001)
[    0.000000] ACPI: WAET 000000001ffe1c1e 00028 (v01 BOCHS  BXPC     00000001 BXPC 00000001)
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at 0000000000000000-000000001ffdd000
[    0.000000] Initmem setup node 0 0000000000000000-000000001ffdd000
[    0.000000]   NODE_DATA [000000001ffd5000 - 000000001ffd9fff]
[    0.000000] Zone PFN ranges:
[    0.000000]   DMA      0x00000010 -> 0x00001000
[    0.000000]   DMA32    0x00001000 -> 0x00100000
[    0.000000]   Normal   empty
[    0.000000] Movable zone start PFN for each node
[    0.000000] early_node_map[2] active PFN ranges
[    0.000000]     0: 0x00000010 -> 0x0000009f
[    0.000000]     0: 0x00000100 -> 0x0001ffdd
[    0.000000] ACPI: PM-Timer IO Port: 0x608
[    0.000000] ACPI: LAPIC (acpi_id[0x00] lapic_id[0x00] enabled)
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0xff] dfl dfl lint[0x1])
[    0.000000] ACPI: IOAPIC (id[0x00] address[0xfec00000] gsi_base[0])
[    0.000000] IOAPIC[0]: apic_id 0, version 32, address 0xfec00000, GSI 0-23
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 5 global_irq 5 high level)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 10 global_irq 10 high level)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 11 global_irq 11 high level)
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a201 base: 0xfed00000
[    0.000000] SMP: Allowing 1 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: 000000000009f000 - 00000000000a0000
[    0.000000] PM: Registered nosave memory: 00000000000a0000 - 00000000000f0000
[    0.000000] PM: Registered nosave memory: 00000000000f0000 - 0000000000100000
[    0.000000] Allocating PCI resources starting at 20000000 (gap: 20000000:dffc0000)
[    0.000000] setup_percpu: NR_CPUS:64 nr_cpumask_bits:64 nr_cpu_ids:1 nr_node_ids:1
[    0.000000] PERCPU: Embedded 26 pages/cpu @ffff88001f400000 s76672 r8192 d21632 u2097152
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 128871
[    0.000000] Policy zone: DMA32
[    0.000000] Kernel command line: console=ttyS0 console=/dev/console init=/test.sh
[    0.000000] PID hash table entries: 2048 (order: 2, 16384 bytes)
[    0.000000] Checking aperture...
[    0.000000] No AGP bridge found
[    0.000000] Memory: 490828k/524148k available (7477k kernel code, 452k absent, 32868k reserved, 5506k data, 680k init)
[    0.000000] SLUB: Genslabs=15, HWalign=64, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] Hierarchical RCU implementation.
[    0.000000] NR_IRQS:4352 nr_irqs:256 16
[    0.000000] Console: colour VGA+ 80x25
[    0.000000] console [ttyS0] enabled
[    0.000000] Fast TSC calibration using PIT
[    0.000000] Detected 3792.025 MHz processor.
[    0.004334] Calibrating delay loop (skipped), value calculated using timer frequency.. 7584.05 BogoMIPS (lpj=3792025)
[    0.005092] pid_max: default: 32768 minimum: 301
[    0.006546] Security Framework initialized
[    0.007393] SELinux:  Initializing.
[    0.009665] Dentry cache hash table entries: 65536 (order: 7, 524288 bytes)
[    0.010266] Inode-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.010783] Mount-cache hash table entries: 256
[    0.015659] Initializing cgroup subsys cpuacct
[    0.015953] Initializing cgroup subsys freezer
[    0.017768] mce: CPU supports 10 MCE banks
[    0.018360] using AMD E400 aware idle routine
[    0.019046] SMP alternatives: switching to UP code
[    0.077726] Freeing SMP alternatives: 24k freed
[    0.077986] ACPI: Core revision 20110623
[    0.093991] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.104558] CPU0: AMD QEMU Virtual CPU version 2.5+ stepping 01
[    0.104990] Performance Events: Broken PMU hardware detected, using software events only.
[    0.108918] MCE: In-kernel MCE decoding enabled.
[    0.109061] Brought up 1 CPUs
[    0.109169] Total of 1 processors activated (7584.05 BogoMIPS).
[    0.118387] kworker/u:0 used greatest stack depth: 6272 bytes left
[    0.118800] RTC time: 15:45:45, date: 06/25/25
[    0.119805] NET: Registered protocol family 16
[    0.122847] kworker/u:0 used greatest stack depth: 6080 bytes left
[    0.125777] ACPI: bus type pci registered
[    0.126400] PCI: Using configuration type 1 for base access
[    0.127961] kworker/u:0 used greatest stack depth: 5760 bytes left
[    0.155694] bio: create slab <bio-0> at 0
[    0.157263] ACPI: Added _OSI(Module Device)
[    0.157375] ACPI: Added _OSI(Processor Device)
[    0.157469] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.157575] ACPI: Added _OSI(Processor Aggregator Device)
[    0.168019] ACPI: Interpreter enabled
[    0.168120] ACPI: (supports S0 S3 S4 S5)
[    0.168580] ACPI: Using IOAPIC for interrupt routing
[    0.186448] ACPI: No dock devices found.
[    0.186593] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.187733] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.188732] pci_root PNP0A03:00: host bridge window [io  0x0000-0x0cf7]
[    0.188861] pci_root PNP0A03:00: host bridge window [io  0x0d00-0xffff]
[    0.189027] pci_root PNP0A03:00: host bridge window [mem 0x000a0000-0x000bffff]
[    0.189195] pci_root PNP0A03:00: host bridge window [mem 0x20000000-0xfebfffff]
[    0.189372] pci_root PNP0A03:00: host bridge window [mem 0x100000000-0x17fffffff]
[    0.193895] pci 0000:00:01.3: quirk: [io  0x0600-0x063f] claimed by PIIX4 ACPI
[    0.194005] pci 0000:00:01.3: quirk: [io  0x0700-0x070f] claimed by PIIX4 SMB
[    0.302817]  pci0000:00: Unable to request _OSC control (_OSC support mask: 0x1e)
[    0.312568] ACPI: PCI Interrupt Link [LNKA] (IRQs 5 *10 11)
[    0.313004] ACPI: PCI Interrupt Link [LNKB] (IRQs 5 *10 11)
[    0.313272] ACPI: PCI Interrupt Link [LNKC] (IRQs 5 10 *11)
[    0.313523] ACPI: PCI Interrupt Link [LNKD] (IRQs 5 10 *11)
[    0.313713] ACPI: PCI Interrupt Link [LNKS] (IRQs *9)
[    0.314942] vgaarb: device added: PCI:0000:00:02.0,decodes=io+mem,owns=io+mem,locks=none
[    0.315004] vgaarb: loaded
[    0.315068] vgaarb: bridge control possible 0000:00:02.0
[    0.316302] SCSI subsystem initialized
[    0.317881] usbcore: registered new interface driver usbfs
[    0.318270] usbcore: registered new interface driver hub
[    0.318666] usbcore: registered new device driver usb
[    0.320267] Advanced Linux Sound Architecture Driver Version 1.0.24.
[    0.320423] PCI: Using ACPI for IRQ routing
[    0.325562] cfg80211: Calling CRDA to update world regulatory domain
[    0.327245] NetLabel: Initializing
[    0.327323] NetLabel:  domain hash size = 128
[    0.327413] NetLabel:  protocols = UNLABELED CIPSOv4
[    0.327837] NetLabel:  unlabeled traffic allowed by default
[    0.328613] HPET: 3 timers in total, 0 timers will be used for per-cpu timer
[    0.328920] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0
[    0.329052] hpet0: 3 comparators, 64-bit 100.000000 MHz counter
[    0.333381] Switching to clocksource hpet
[    0.344931] pnp: PnP ACPI init
[    0.345113] ACPI: bus type pnp registered
[    0.349476] pnp: PnP ACPI: found 11 devices
[    0.349598] ACPI: ACPI bus type pnp unregistered
[    0.365306] NET: Registered protocol family 2
[    0.366049] IP route cache hash table entries: 4096 (order: 3, 32768 bytes)
[    0.368275] TCP established hash table entries: 16384 (order: 6, 262144 bytes)
[    0.368606] TCP bind hash table entries: 16384 (order: 6, 262144 bytes)
[    0.368880] TCP: Hash tables configured (established 16384 bind 16384)
[    0.369095] TCP reno registered
[    0.369216] UDP hash table entries: 256 (order: 1, 8192 bytes)
[    0.369393] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes)
[    0.370207] NET: Registered protocol family 1
[    0.371185] RPC: Registered named UNIX socket transport module.
[    0.371338] RPC: Registered udp transport module.
[    0.371440] RPC: Registered tcp transport module.
[    0.371540] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.371752] pci 0000:00:00.0: Limiting direct PCI/PCI transfers
[    0.371930] pci 0000:00:01.0: PIIX3: Enabling Passive Release
[    0.372208] pci 0000:00:01.0: Activating ISA DMA hang workarounds
[    0.374893] Trying to unpack rootfs image as initramfs...
[    0.596786] Freeing initrd memory: 9800k freed
[    0.604828] microcode: CPU0: family 15 not supported
[    0.607637] audit: initializing netlink socket (disabled)
[    0.608138] type=2000 audit(1750866345.606:1): initialized
[    0.639440] HugeTLB registered 2 MB page size, pre-allocated 0 pages
[    0.649571] VFS: Disk quotas dquot_6.5.2
[    0.649969] Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.654295] msgmni has been set to 977
[    0.657300] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
[    0.657561] io scheduler noop registered
[    0.657645] io scheduler deadline registered
[    0.657962] io scheduler cfq registered (default)
[    0.658876] pci_hotplug: PCI Hot Plug PCI Core version: 0.5
[    0.660474] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
[    0.660943] ACPI: Power Button [PWRF]
[    0.666193] ACPI: PCI Interrupt Link [LNKD] enabled at IRQ 11
[    0.666427] virtio-pci 0000:00:04.0: PCI INT A -> Link[LNKD] -> GSI 11 (level, high) -> IRQ 11
[    0.667967] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    0.937787] serial8250: ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A
[    0.966164] 00:08: ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A
[    0.971866] Non-volatile memory driver v1.3
[    0.972356] Linux agpgart interface v0.103
[    0.975538] [drm] Initialized drm 1.1.0 20060810
[    0.975937] [drm:i915_init] *ERROR* drm/i915 can't work without intel_agp module!
[    0.992141] brd: module loaded
[    0.998931] loop: module loaded
[    1.014208]  vda: unknown partition table
[    1.021587] scsi0 : ata_piix
[    1.022294] scsi1 : ata_piix
[    1.022737] ata1: PATA max MWDMA2 cmd 0x1f0 ctl 0x3f6 bmdma 0xc0c0 irq 14
[    1.022928] ata2: PATA max MWDMA2 cmd 0x170 ctl 0x376 bmdma 0xc0c8 irq 15
[    1.026472] SSFDC read-only Flash Translation layer
[    1.026701] mtdoops: mtd device (mtddev=name/number) must be supplied
[    1.026964] L440GX flash mapping: failed to find PIIX4 ISA bridge, cannot continue
[    1.027544] physmap-flash.0: failed to claim resource 0
[    1.028150] SBC-GXx flash: IO:0x258-0x259 MEM:0xdc000-0xdffff
[    1.029147] Could not find PAR responsible for SC520CDP Flash Bank #0
[    1.029283] Trying default address 0x8400000
[    1.029383] Could not find PAR responsible for SC520CDP Flash Bank #1
[    1.029526] Trying default address 0x8c00000
[    1.029615] Could not find PAR responsible for SC520CDP DIL Flash
[    1.029744] Trying default address 0x9400000
[    1.029859] SC520 CDP flash device: 0x800000 at 0x8400000
[    1.030023] Failed to ioremap_nocache
[    1.030137] NetSc520 flash device: 0x100000 at 0x200000
[    1.030264] Failed to ioremap_nocache
[    1.030361] Failed to ioremap_nocache
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x200002AA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x200002AA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000001, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000001, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20002AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20002AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000001, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000001, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000001, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000001, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000001, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x200002AA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x200002AA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000002, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000002, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20002AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20002AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000002, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000002, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000002, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005555, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000002, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000002, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x200002AA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x200002AA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000004, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000004, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20002AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20002AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005554, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000004, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000004, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000AAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000004, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20005554, size 1, region '(null)', reason: rejected
Invalid write at addr 0x2000AAAA, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000004, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid write at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000000, size 1, region '(null)', reason: rejected
Invalid read at addr 0x20000004, size 1, region '(null)', reason: rejected
[    1.031894] SNAPGEAR: failed to ioremap() ROMCS1
[    1.032220] Generic platform RAM MTD, (c) 2004 Simtec Electronics
[    1.033073] No recognised DiskOnChip devices found
[    1.033203] slram: not enough parameters.
[    1.033328] Ramix PMC551 PCI Mezzanine Ram Driver. (C) 1999,2000 Nortel Networks.
[    1.033503] pmc551: not detected
[    1.066690] modprobe used greatest stack depth: 5672 bytes left
[    1.070703] ftl_cs: FTL header not found.
[    1.077991] Spectra MTD driver
[    1.092831] No valid DiskOnChip devices found
[    1.093718] [nandsim] warning: write_byte: command (0x90) wasn't expected, expected state is STATE_READY, ignore previous states
[    1.094012] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.094248] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.094456] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.094671] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.095029] NAND device: Manufacturer ID: 0x20, Chip ID: 0xa2 (ST Micro NAND 64MiB 1,8V 8-bit)
[    1.095521] flash size: 64 MiB
[    1.095595] page size: 2048 bytes
[    1.095674] OOB area size: 64 bytes
[    1.095757] sector size: 128 KiB
[    1.095834] pages number: 32768
[    1.095908] pages per sector: 64
[    1.095994] bus width: 8
[    1.096080] bits in sector size: 17
[    1.096167] bits in page size: 11
[    1.096237] bits in OOB size: 6
[    1.096314] flash size with OOB: 67584 KiB
[    1.096405] page address bytes: 4
[    1.096476] sector address bytes: 2
[    1.096553] options: 0x8
[    1.096955] Scanning device for bad blocks
[    1.100841] Creating 1 MTD partitions on "NAND 64MiB 1,8V 8-bit":
[    1.101147] 0x000000000000-0x000004000000 : "NAND simulator partition 0"
[    1.102448] ftl_cs: FTL header not found.
[    1.103361] usbcore: registered new interface driver alauda
[    1.148083] onenand_wait: timeout! ctrl=0x0000 intr=0x0000
[    1.148322] OneNAND 16MB 1.8V 16-bit (0x04)
[    1.148399] OneNAND version = 0x001e
[    1.148964] Scanning device for bad blocks
[    1.152171] Creating 1 MTD partitions on "OneNAND simulator":
[    1.152366] 0x000000000000-0x000001000000 : "OneNAND simulator partition"
[    1.153550] ftl_cs: FTL header not found.
[    1.154887] e100: Intel(R) PRO/100 Network Driver, 3.5.24-k2-NAPI
[    1.155075] e100: Copyright(c) 1999-2006 Intel Corporation
[    1.155340] e1000: Intel(R) PRO/1000 Network Driver - version 7.3.21-k8-NAPI
[    1.155504] e1000: Copyright (c) 1999-2006 Intel Corporation.
[    1.156206] ACPI: PCI Interrupt Link [LNKC] enabled at IRQ 10
[    1.156374] e1000 0000:00:03.0: PCI INT A -> Link[LNKC] -> GSI 10 (level, high) -> IRQ 10
[    1.403417] ata2.00: ATAPI: QEMU DVD-ROM, 2.5+, max UDMA/100
[    1.404346] ata2.00: configured for MWDMA2
[    1.409934] scsi 1:0:0:0: CD-ROM            QEMU     QEMU DVD-ROM     2.5+ PQ: 0 ANSI: 5
[    1.413002] sr0: scsi3-mmc drive: 4x/4x cd/rw xa/form2 tray
[    1.413290] cdrom: Uniform CD-ROM driver Revision: 3.20
[    1.415175] sr 1:0:0:0: Attached scsi generic sg0 type 5
[    1.429581] e1000 0000:00:03.0: eth0: (PCI:33MHz:32-bit) 52:54:00:12:34:56
[    1.429831] e1000 0000:00:03.0: eth0: Intel(R) PRO/1000 Network Connection
[    1.430317] sky2: driver version 1.30
[    1.431438] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.431790] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    1.432155] uhci_hcd: USB Universal Host Controller Interface driver
[    1.432593] usbcore: registered new interface driver usblp
[    1.432722] Initializing USB Mass Storage driver...
[    1.432934] usbcore: registered new interface driver usb-storage
[    1.433129] USB Mass Storage support registered.
[    1.433392] usbcore: registered new interface driver libusual
[    1.433997] i8042: PNP: PS/2 Controller [PNP0303:KBD,PNP0f13:MOU] at 0x60,0x64 irq 1,12
[    1.435512] serio: i8042 KBD port at 0x60,0x64 irq 1
[    1.435735] serio: i8042 AUX port at 0x60,0x64 irq 12
[    1.436657] mousedev: PS/2 mouse device common for all mice
[    1.438542] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input1
[    1.439702] rtc_cmos 00:09: RTC can wake from S4
[    1.441682] rtc_cmos 00:09: rtc core: registered rtc_cmos as rtc0
[    1.442215] rtc0: alarms up to one day, y3k, 242 bytes nvram, hpet irqs
[    1.443242] device-mapper: ioctl: 4.22.0-ioctl (2011-10-19) initialised: dm-devel@redhat.com
[    1.443829] cpuidle: using governor ladder
[    1.443964] cpuidle: using governor menu
[    1.444089] EFI Variables Facility v0.08 2004-May-17
[    1.446608] usbcore: registered new interface driver usbhid
[    1.446735] usbhid: USB HID core driver
[    1.453769] ALSA device list:
[    1.453871]   No soundcards found.
[    1.454451] Netfilter messages via NETLINK v0.30.
[    1.454773] nf_conntrack version 0.5.0 (3911 buckets, 15644 max)
[    1.455849] ctnetlink v0.93: registering with nfnetlink.
[    1.457901] ip_tables: (C) 2000-2006 Netfilter Core Team
[    1.459273] TCP cubic registered
[    1.459355] Initializing XFRM netlink socket
[    1.460276] NET: Registered protocol family 10
[    1.464010] ip6_tables: (C) 2000-2006 Netfilter Core Team
[    1.464952] IPv6 over IPv4 tunneling driver
[    1.466683] NET: Registered protocol family 17
[    1.466949] Registering the dns_resolver key type
[    1.468239] registered taskstats version 1
[    1.470222]   Magic number: 13:705:791
[    1.470600] console [netcon0] enabled
[    1.470693] netconsole: network logging started
[    1.477555] Freeing unused kernel memory: 680k freed
[    1.512066] Write protecting the kernel read-only data: 12288k
[    1.517993] Freeing unused kernel memory: 692k freed
[    1.530629] Freeing unused kernel memory: 1608k freed
====[ Init start ]====
====[ Mdev starting ]====
[    1.604399] Refined TSC clocksource calibration: 3792.881 MHz.
[    1.604619] Switching to clocksource tsc
====[ Mounting ]====
[    1.630760] EXT2-fs (vda): warning: mounting unchecked fs, running e2fsck is recommended
====[ Modifying PATH ]====
====[ Dropping to shell ]====
/bin/sh: can't access tty; job control turned off
~ #
```

This will boot a QEMU virtual machine simulating an embedded Linux system with a YAFFS2 NAND partition, allowing realistic file creation and extraction testing.

In the root directory, you've 2 simulations :

## simulation 1

```bash
~ # ./simul_1
```
will do all of that operation on the filesystem

- Erasing flash on /dev/mtd1
- Flashing /dev/mtd1
- Mounting /dev/mtdblock1 on /mnt/yaffs (YAFFS2)

Then :

- Create /mnt/yaffs/file1.txt
- Create chained directories /mnt/yaffs/dir1/dir2/dir3
  
   Create chained directories /mnt/yaffs/dir1/dir4/dir5
  
   Create chained directories /mnt/yaffs/dir6
- Create /mnt/yaffs/dir1/dir2/dir3/link1 -> ../../../test1.txt
- Create named pipe /mnt/yaffs/dir1/dir2/named_pipe
- Create block device /mnt/yaffs/dir1/dir4/dir5/block_device
- Create unix socket /mnt/yaffs/dir6/aSocket.sock
- Move directory /mnt/yaffs/dir1/dir4/dir5 in /mnt/yaffs/dir1/dir2
- Delete /mnt/yaffs/dir1/dir2/dir5
- Rename /mnt/yaffs/dir1/dir4 to /mnt/yaffs/dir1/dir41
- Create /mnt/yaffs/dir1/dir41/file2.txt
- Create /mnt/yaffs/dir1/lorem.txt
- Truncate /mnt/yaffs/dir1/lorem.txt to 300 bytes


## simulation 2

```bash
~ # ./simul_2
```
will do all of that operation on the filesystem

- Erasing flash on /dev/mtd1
- Flashing /dev/mtd1
- Mounting /dev/mtdblock1 on /mnt/yaffs (YAFFS2)

Then :

1- Create /mnt/yaffs/big_lorem.txt (6639 bytes)
2- Truncate /mnt/yaffs/big_lorem.txt to 2200 bytes
