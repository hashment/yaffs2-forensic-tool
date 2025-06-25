# YAFFS2 sample images

This directory contains YAFFS2 images for testing.

## Operating procedure

To generate all of them, in the /test_env, run :

```bash
cd ../test_env
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
[    0.000000] RAMDISK: 1e8db000 - 1ffd0000
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
[    0.000000] PERCPU: Embedded 26 pages/cpu @ffff88001e600000 s76672 r8192 d21632 u2097152
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 128871
[    0.000000] Policy zone: DMA32
[    0.000000] Kernel command line: console=ttyS0 console=/dev/console init=/test.sh
[    0.000000] PID hash table entries: 2048 (order: 2, 16384 bytes)
[    0.000000] Checking aperture...
[    0.000000] No AGP bridge found
[    0.000000] Memory: 477120k/524148k available (7477k kernel code, 452k absent, 46576k reserved, 5506k data, 680k init)
[    0.000000] SLUB: Genslabs=15, HWalign=64, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] Hierarchical RCU implementation.
[    0.000000] NR_IRQS:4352 nr_irqs:256 16
[    0.000000] Console: colour VGA+ 80x25
[    0.000000] console [ttyS0] enabled
[    0.000000] Fast TSC calibration using PIT
[    0.000000] Detected 3791.994 MHz processor.
[    0.005342] Calibrating delay loop (skipped), value calculated using timer frequency.. 7583.98 BogoMIPS (lpj=3791994)
[    0.005820] pid_max: default: 32768 minimum: 301
[    0.007556] Security Framework initialized
[    0.008275] SELinux:  Initializing.
[    0.010609] Dentry cache hash table entries: 65536 (order: 7, 524288 bytes)
[    0.011219] Inode-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.011758] Mount-cache hash table entries: 256
[    0.016677] Initializing cgroup subsys cpuacct
[    0.017009] Initializing cgroup subsys freezer
[    0.018851] mce: CPU supports 10 MCE banks
[    0.019479] using AMD E400 aware idle routine
[    0.020171] SMP alternatives: switching to UP code
[    0.079288] Freeing SMP alternatives: 24k freed
[    0.079526] ACPI: Core revision 20110623
[    0.095354] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.105770] CPU0: AMD QEMU Virtual CPU version 2.5+ stepping 01
[    0.106990] Performance Events: Broken PMU hardware detected, using software events only.
[    0.111185] MCE: In-kernel MCE decoding enabled.
[    0.111360] Brought up 1 CPUs
[    0.111462] Total of 1 processors activated (7583.98 BogoMIPS).
[    0.120639] kworker/u:0 used greatest stack depth: 6272 bytes left
[    0.121157] RTC time: 15:25:20, date: 06/25/25
[    0.122029] NET: Registered protocol family 16
[    0.125386] kworker/u:0 used greatest stack depth: 6080 bytes left
[    0.128289] ACPI: bus type pci registered
[    0.128800] PCI: Using configuration type 1 for base access
[    0.130342] kworker/u:0 used greatest stack depth: 5760 bytes left
[    0.156808] bio: create slab <bio-0> at 0
[    0.158736] ACPI: Added _OSI(Module Device)
[    0.158853] ACPI: Added _OSI(Processor Device)
[    0.159006] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.159125] ACPI: Added _OSI(Processor Aggregator Device)
[    0.169604] ACPI: Interpreter enabled
[    0.169718] ACPI: (supports S0 S3 S4 S5)
[    0.170214] ACPI: Using IOAPIC for interrupt routing
[    0.187472] ACPI: No dock devices found.
[    0.187625] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.188836] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.189814] pci_root PNP0A03:00: host bridge window [io  0x0000-0x0cf7]
[    0.190014] pci_root PNP0A03:00: host bridge window [io  0x0d00-0xffff]
[    0.190202] pci_root PNP0A03:00: host bridge window [mem 0x000a0000-0x000bffff]
[    0.190387] pci_root PNP0A03:00: host bridge window [mem 0x20000000-0xfebfffff]
[    0.190552] pci_root PNP0A03:00: host bridge window [mem 0x100000000-0x17fffffff]
[    0.194335] pci 0000:00:01.3: quirk: [io  0x0600-0x063f] claimed by PIIX4 ACPI
[    0.194534] pci 0000:00:01.3: quirk: [io  0x0700-0x070f] claimed by PIIX4 SMB
[    0.306730]  pci0000:00: Unable to request _OSC control (_OSC support mask: 0x1e)
[    0.315074] ACPI: PCI Interrupt Link [LNKA] (IRQs 5 *10 11)
[    0.315490] ACPI: PCI Interrupt Link [LNKB] (IRQs 5 *10 11)
[    0.315764] ACPI: PCI Interrupt Link [LNKC] (IRQs 5 10 *11)
[    0.316083] ACPI: PCI Interrupt Link [LNKD] (IRQs 5 10 *11)
[    0.316295] ACPI: PCI Interrupt Link [LNKS] (IRQs *9)
[    0.317555] vgaarb: device added: PCI:0000:00:02.0,decodes=io+mem,owns=io+mem,locks=none
[    0.317787] vgaarb: loaded
[    0.317873] vgaarb: bridge control possible 0000:00:02.0
[    0.318865] SCSI subsystem initialized
[    0.320555] usbcore: registered new interface driver usbfs
[    0.321038] usbcore: registered new interface driver hub
[    0.321470] usbcore: registered new device driver usb
[    0.323053] Advanced Linux Sound Architecture Driver Version 1.0.24.
[    0.323228] PCI: Using ACPI for IRQ routing
[    0.328417] cfg80211: Calling CRDA to update world regulatory domain
[    0.330135] NetLabel: Initializing
[    0.330226] NetLabel:  domain hash size = 128
[    0.330329] NetLabel:  protocols = UNLABELED CIPSOv4
[    0.330774] NetLabel:  unlabeled traffic allowed by default
[    0.331612] HPET: 3 timers in total, 0 timers will be used for per-cpu timer
[    0.331957] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0
[    0.332058] hpet0: 3 comparators, 64-bit 100.000000 MHz counter
[    0.337354] Switching to clocksource hpet
[    0.348959] pnp: PnP ACPI init
[    0.349166] ACPI: bus type pnp registered
[    0.353438] pnp: PnP ACPI: found 11 devices
[    0.353587] ACPI: ACPI bus type pnp unregistered
[    0.368959] NET: Registered protocol family 2
[    0.369750] IP route cache hash table entries: 4096 (order: 3, 32768 bytes)
[    0.371993] TCP established hash table entries: 16384 (order: 6, 262144 bytes)
[    0.372404] TCP bind hash table entries: 16384 (order: 6, 262144 bytes)
[    0.372714] TCP: Hash tables configured (established 16384 bind 16384)
[    0.372914] TCP reno registered
[    0.373082] UDP hash table entries: 256 (order: 1, 8192 bytes)
[    0.373272] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes)
[    0.374066] NET: Registered protocol family 1
[    0.375023] RPC: Registered named UNIX socket transport module.
[    0.375250] RPC: Registered udp transport module.
[    0.375368] RPC: Registered tcp transport module.
[    0.375483] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.375701] pci 0000:00:00.0: Limiting direct PCI/PCI transfers
[    0.375882] pci 0000:00:01.0: PIIX3: Enabling Passive Release
[    0.376150] pci 0000:00:01.0: Activating ISA DMA hang workarounds
[    0.378813] Trying to unpack rootfs image as initramfs...
[    0.904431] Freeing initrd memory: 23508k freed
[    0.916274] microcode: CPU0: family 15 not supported
[    0.919188] audit: initializing netlink socket (disabled)
[    0.919636] type=2000 audit(1750865120.918:1): initialized
[    0.949123] HugeTLB registered 2 MB page size, pre-allocated 0 pages
[    0.959802] VFS: Disk quotas dquot_6.5.2
[    0.960264] Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.964518] msgmni has been set to 977
[    0.967329] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
[    0.967589] io scheduler noop registered
[    0.967702] io scheduler deadline registered
[    0.968057] io scheduler cfq registered (default)
[    0.968934] pci_hotplug: PCI Hot Plug PCI Core version: 0.5
[    0.970578] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
[    0.971106] ACPI: Power Button [PWRF]
[    0.976499] ACPI: PCI Interrupt Link [LNKD] enabled at IRQ 11
[    0.976755] virtio-pci 0000:00:04.0: PCI INT A -> Link[LNKD] -> GSI 11 (level, high) -> IRQ 11
[    0.978337] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.247870] serial8250: ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A
[    1.275802] 00:08: ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A
[    1.281865] Non-volatile memory driver v1.3
[    1.282480] Linux agpgart interface v0.103
[    1.285979] [drm] Initialized drm 1.1.0 20060810
[    1.286560] [drm:i915_init] *ERROR* drm/i915 can't work without intel_agp module!
[    1.301236] brd: module loaded
[    1.305372] loop: module loaded
[    1.314555]  vda: unknown partition table
[    1.321838] scsi0 : ata_piix
[    1.322775] scsi1 : ata_piix
[    1.323367] ata1: PATA max MWDMA2 cmd 0x1f0 ctl 0x3f6 bmdma 0xc0c0 irq 14
[    1.323551] ata2: PATA max MWDMA2 cmd 0x170 ctl 0x376 bmdma 0xc0c8 irq 15
[    1.326964] SSFDC read-only Flash Translation layer
[    1.327215] mtdoops: mtd device (mtddev=name/number) must be supplied
[    1.327461] L440GX flash mapping: failed to find PIIX4 ISA bridge, cannot continue
[    1.327984] physmap-flash.0: failed to claim resource 0
[    1.328623] SBC-GXx flash: IO:0x258-0x259 MEM:0xdc000-0xdffff
[    1.329626] Could not find PAR responsible for SC520CDP Flash Bank #0
[    1.329772] Trying default address 0x8400000
[    1.329876] Could not find PAR responsible for SC520CDP Flash Bank #1
[    1.330009] Trying default address 0x8c00000
[    1.330129] Could not find PAR responsible for SC520CDP DIL Flash
[    1.330282] Trying default address 0x9400000
[    1.330405] SC520 CDP flash device: 0x800000 at 0x8400000
[    1.330566] Failed to ioremap_nocache
[    1.330665] NetSc520 flash device: 0x100000 at 0x200000
[    1.330790] Failed to ioremap_nocache
[    1.330892] Failed to ioremap_nocache
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
[    1.332465] SNAPGEAR: failed to ioremap() ROMCS1
[    1.332737] Generic platform RAM MTD, (c) 2004 Simtec Electronics
[    1.333651] No recognised DiskOnChip devices found
[    1.333774] slram: not enough parameters.
[    1.333892] Ramix PMC551 PCI Mezzanine Ram Driver. (C) 1999,2000 Nortel Networks.
[    1.334116] pmc551: not detected
[    1.368028] modprobe used greatest stack depth: 5672 bytes left
[    1.372438] ftl_cs: FTL header not found.
[    1.379147] Spectra MTD driver
[    1.393986] No valid DiskOnChip devices found
[    1.394897] [nandsim] warning: write_byte: command (0x90) wasn't expected, expected state is STATE_READY, ignore previous states
[    1.395259] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.395501] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.395717] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.395946] [nandsim] warning: read_byte: unexpected data output cycle, state is STATE_READY return 0x0
[    1.396342] NAND device: Manufacturer ID: 0x20, Chip ID: 0xa2 (ST Micro NAND 64MiB 1,8V 8-bit)
[    1.396854] flash size: 64 MiB
[    1.396930] page size: 2048 bytes
[    1.397014] OOB area size: 64 bytes
[    1.397141] sector size: 128 KiB
[    1.397226] pages number: 32768
[    1.397299] pages per sector: 64
[    1.397385] bus width: 8
[    1.397447] bits in sector size: 17
[    1.397532] bits in page size: 11
[    1.397616] bits in OOB size: 6
[    1.397704] flash size with OOB: 67584 KiB
[    1.397811] page address bytes: 4
[    1.397896] sector address bytes: 2
[    1.397990] options: 0x8
[    1.398425] Scanning device for bad blocks
[    1.402604] Creating 1 MTD partitions on "NAND 64MiB 1,8V 8-bit":
[    1.402877] 0x000000000000-0x000004000000 : "NAND simulator partition 0"
[    1.404262] ftl_cs: FTL header not found.
[    1.405161] usbcore: registered new interface driver alauda
[    1.450078] onenand_wait: timeout! ctrl=0x0000 intr=0x0000
[    1.450313] OneNAND 16MB 1.8V 16-bit (0x04)
[    1.450408] OneNAND version = 0x001e
[    1.450954] Scanning device for bad blocks
[    1.454486] Creating 1 MTD partitions on "OneNAND simulator":
[    1.454696] 0x000000000000-0x000001000000 : "OneNAND simulator partition"
[    1.455704] ftl_cs: FTL header not found.
[    1.457090] e100: Intel(R) PRO/100 Network Driver, 3.5.24-k2-NAPI
[    1.457209] e100: Copyright(c) 1999-2006 Intel Corporation
[    1.457466] e1000: Intel(R) PRO/1000 Network Driver - version 7.3.21-k8-NAPI
[    1.457619] e1000: Copyright (c) 1999-2006 Intel Corporation.
[    1.458309] ACPI: PCI Interrupt Link [LNKC] enabled at IRQ 10
[    1.458477] e1000 0000:00:03.0: PCI INT A -> Link[LNKC] -> GSI 10 (level, high) -> IRQ 10
[    1.479934] ata2.00: ATAPI: QEMU DVD-ROM, 2.5+, max UDMA/100
[    1.480900] ata2.00: configured for MWDMA2
[    1.709939] scsi 1:0:0:0: CD-ROM            QEMU     QEMU DVD-ROM     2.5+ PQ: 0 ANSI: 5
[    1.714676] sr0: scsi3-mmc drive: 4x/4x cd/rw xa/form2 tray
[    1.714914] cdrom: Uniform CD-ROM driver Revision: 3.20
[    1.716804] sr 1:0:0:0: Attached scsi generic sg0 type 5
[    1.735886] e1000 0000:00:03.0: eth0: (PCI:33MHz:32-bit) 52:54:00:12:34:56
[    1.736188] e1000 0000:00:03.0: eth0: Intel(R) PRO/1000 Network Connection
[    1.736639] sky2: driver version 1.30
[    1.737720] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.738084] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    1.738375] uhci_hcd: USB Universal Host Controller Interface driver
[    1.738790] usbcore: registered new interface driver usblp
[    1.738924] Initializing USB Mass Storage driver...
[    1.739186] usbcore: registered new interface driver usb-storage
[    1.739328] USB Mass Storage support registered.
[    1.739580] usbcore: registered new interface driver libusual
[    1.740267] i8042: PNP: PS/2 Controller [PNP0303:KBD,PNP0f13:MOU] at 0x60,0x64 irq 1,12
[    1.741803] serio: i8042 KBD port at 0x60,0x64 irq 1
[    1.742040] serio: i8042 AUX port at 0x60,0x64 irq 12
[    1.742967] mousedev: PS/2 mouse device common for all mice
[    1.744819] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input1
[    1.745968] rtc_cmos 00:09: RTC can wake from S4
[    1.747975] rtc_cmos 00:09: rtc core: registered rtc_cmos as rtc0
[    1.748483] rtc0: alarms up to one day, y3k, 242 bytes nvram, hpet irqs
[    1.749451] device-mapper: ioctl: 4.22.0-ioctl (2011-10-19) initialised: dm-devel@redhat.com
[    1.750097] cpuidle: using governor ladder
[    1.750224] cpuidle: using governor menu
[    1.750319] EFI Variables Facility v0.08 2004-May-17
[    1.752822] usbcore: registered new interface driver usbhid
[    1.752949] usbhid: USB HID core driver
[    1.759897] ALSA device list:
[    1.759994]   No soundcards found.
[    1.760564] Netfilter messages via NETLINK v0.30.
[    1.760899] nf_conntrack version 0.5.0 (3911 buckets, 15644 max)
[    1.761946] ctnetlink v0.93: registering with nfnetlink.
[    1.763930] ip_tables: (C) 2000-2006 Netfilter Core Team
[    1.765408] TCP cubic registered
[    1.765492] Initializing XFRM netlink socket
[    1.766522] NET: Registered protocol family 10
[    1.770357] ip6_tables: (C) 2000-2006 Netfilter Core Team
[    1.771312] IPv6 over IPv4 tunneling driver
[    1.772969] NET: Registered protocol family 17
[    1.773279] Registering the dns_resolver key type
[    1.774627] registered taskstats version 1
[    1.776498]   Magic number: 13:843:437
[    1.776887] console [netcon0] enabled
[    1.776990] netconsole: network logging started
[    1.784011] Freeing unused kernel memory: 680k freed
[    1.818814] Write protecting the kernel read-only data: 12288k
[    1.824768] Freeing unused kernel memory: 692k freed
[    1.837486] Freeing unused kernel memory: 1608k freed
====[ Init start ]====
====[ Mdev starting ]====
[    1.916410] Refined TSC clocksource calibration: 3792.848 MHz.
[    1.916628] Switching to clocksource tsc
====[ Mounting ]====
[    1.936878] EXT2-fs (vda): warning: mounting unchecked fs, running e2fsck is recommended
====[ Modifying PATH ]====
====[ Dropping to shell ]====
/bin/sh: can't access tty; job control turned off
~ #
```

When the system is started, there will have a /mnt/disk partition (ext2) mounted.

Then simply run :

```bash
~ # ./simul_1
====[ Erasing flash on /dev/mtd1 ]====
[   37.309787] ====[ Erasing flash on /dev/mtd1 ]====
Erasing 65536 Kibyte @ 0 -- 100 % complete 
====[ Flashing /dev/mtd1 ]====
[   37.330954] ====[ Flashing /dev/mtd1 ]====
Writing data to block 0 at offset 0x0
Writing data to block 1 at offset 0x20000
Writing data to block 2 at offset 0x40000
Writing data to block 3 at offset 0x60000
Writing data to block 4 at offset 0x80000
Writing data to block 5 at offset 0xa0000
Writing data to block 6 at offset 0xc0000
Writing data to block 7 at offset 0xe0000
Writing data to block 8 at offset 0x100000
Writing data to block 9 at offset 0x120000
Writing data to block 10 at offset 0x140000
Writing data to block 11 at offset 0x160000
Writing data to block 12 at offset 0x180000
Writing data to block 13 at offset 0x1a0000
Writing data to block 14 at offset 0x1c0000
Writing data to block 15 at offset 0x1e0000
Writing data to block 16 at offset 0x200000
Writing data to block 17 at offset 0x220000
Writing data to block 18 at offset 0x240000
Writing data to block 19 at offset 0x260000
Writing data to block 20 at offset 0x280000
Writing data to block 21 at offset 0x2a0000
Writing data to block 22 at offset 0x2c0000
Writing data to block 23 at offset 0x2e0000
Writing data to block 24 at offset 0x300000
Writing data to block 25 at offset 0x320000
Writing data to block 26 at offset 0x340000
Writing data to block 27 at offset 0x360000
Writing data to block 28 at offset 0x380000
Writing data to block 29 at offset 0x3a0000
Writing data to block 30 at offset 0x3c0000
Writing data to block 31 at offset 0x3e0000
Writing data to block 32 at offset 0x400000
Writing data to block 33 at offset 0x420000
Writing data to block 34 at offset 0x440000
Writing data to block 35 at offset 0x460000
Writing data to block 36 at offset 0x480000
Writing data to block 37 at offset 0x4a0000
Writing data to block 38 at offset 0x4c0000
Writing data to block 39 at offset 0x4e0000
Writing data to block 40 at offset 0x500000
Writing data to block 41 at offset 0x520000
Writing data to block 42 at offset 0x540000
Writing data to block 43 at offset 0x560000
Writing data to block 44 at offset 0x580000
Writing data to block 45 at offset 0x5a0000
Writing data to block 46 at offset 0x5c0000
Writing data to block 47 at offset 0x5e0000
Writing data to block 48 at offset 0x600000
Writing data to block 49 at offset 0x620000
Writing data to block 50 at offset 0x640000
Writing data to block 51 at offset 0x660000
Writing data to block 52 at offset 0x680000
Writing data to block 53 at offset 0x6a0000
Writing data to block 54 at offset 0x6c0000
Writing data to block 55 at offset 0x6e0000
Writing data to block 56 at offset 0x700000
Writing data to block 57 at offset 0x720000
Writing data to block 58 at offset 0x740000
Writing data to block 59 at offset 0x760000
Writing data to block 60 at offset 0x780000
Writing data to block 61 at offset 0x7a0000
Writing data to block 62 at offset 0x7c0000
Writing data to block 63 at offset 0x7e0000
Writing data to block 64 at offset 0x800000
Writing data to block 65 at offset 0x820000
Writing data to block 66 at offset 0x840000
Writing data to block 67 at offset 0x860000
Writing data to block 68 at offset 0x880000
Writing data to block 69 at offset 0x8a0000
Writing data to block 70 at offset 0x8c0000
Writing data to block 71 at offset 0x8e0000
Writing data to block 72 at offset 0x900000
Writing data to block 73 at offset 0x920000
Writing data to block 74 at offset 0x940000
Writing data to block 75 at offset 0x960000
Writing data to block 76 at offset 0x980000
Writing data to block 77 at offset 0x9a0000
Writing data to block 78 at offset 0x9c0000
Writing data to block 79 at offset 0x9e0000
Writing data to block 80 at offset 0xa00000
Writing data to block 81 at offset 0xa20000
Writing data to block 82 at offset 0xa40000
Writing data to block 83 at offset 0xa60000
Writing data to block 84 at offset 0xa80000
Writing data to block 85 at offset 0xaa0000
Writing data to block 86 at offset 0xac0000
Writing data to block 87 at offset 0xae0000
Writing data to block 88 at offset 0xb00000
Writing data to block 89 at offset 0xb20000
Writing data to block 90 at offset 0xb40000
Writing data to block 91 at offset 0xb60000
Writing data to block 92 at offset 0xb80000
Writing data to block 93 at offset 0xba0000
Writing data to block 94 at offset 0xbc0000
Writing data to block 95 at offset 0xbe0000
Writing data to block 96 at offset 0xc00000
Writing data to block 97 at offset 0xc20000
Writing data to block 98 at offset 0xc40000
Writing data to block 99 at offset 0xc60000
Writing data to block 100 at offset 0xc80000
Writing data to block 101 at offset 0xca0000
Writing data to block 102 at offset 0xcc0000
Writing data to block 103 at offset 0xce0000
Writing data to block 104 at offset 0xd00000
Writing data to block 105 at offset 0xd20000
Writing data to block 106 at offset 0xd40000
Writing data to block 107 at offset 0xd60000
Writing data to block 108 at offset 0xd80000
Writing data to block 109 at offset 0xda0000
Writing data to block 110 at offset 0xdc0000
Writing data to block 111 at offset 0xde0000
Writing data to block 112 at offset 0xe00000
Writing data to block 113 at offset 0xe20000
Writing data to block 114 at offset 0xe40000
Writing data to block 115 at offset 0xe60000
Writing data to block 116 at offset 0xe80000
Writing data to block 117 at offset 0xea0000
Writing data to block 118 at offset 0xec0000
Writing data to block 119 at offset 0xee0000
Writing data to block 120 at offset 0xf00000
Writing data to block 121 at offset 0xf20000
Writing data to block 122 at offset 0xf40000
Writing data to block 123 at offset 0xf60000
Writing data to block 124 at offset 0xf80000
Writing data to block 125 at offset 0xfa0000
Writing data to block 126 at offset 0xfc0000
Writing data to block 127 at offset 0xfe0000
Writing data to block 128 at offset 0x1000000
Writing data to block 129 at offset 0x1020000
Writing data to block 130 at offset 0x1040000
Writing data to block 131 at offset 0x1060000
Writing data to block 132 at offset 0x1080000
Writing data to block 133 at offset 0x10a0000
Writing data to block 134 at offset 0x10c0000
Writing data to block 135 at offset 0x10e0000
Writing data to block 136 at offset 0x1100000
Writing data to block 137 at offset 0x1120000
Writing data to block 138 at offset 0x1140000
Writing data to block 139 at offset 0x1160000
Writing data to block 140 at offset 0x1180000
Writing data to block 141 at offset 0x11a0000
Writing data to block 142 at offset 0x11c0000
Writing data to block 143 at offset 0x11e0000
Writing data to block 144 at offset 0x1200000
Writing data to block 145 at offset 0x1220000
Writing data to block 146 at offset 0x1240000
Writing data to block 147 at offset 0x1260000
Writing data to block 148 at offset 0x1280000
Writing data to block 149 at offset 0x12a0000
Writing data to block 150 at offset 0x12c0000
Writing data to block 151 at offset 0x12e0000
Writing data to block 152 at offset 0x1300000
Writing data to block 153 at offset 0x1320000
Writing data to block 154 at offset 0x1340000
Writing data to block 155 at offset 0x1360000
Writing data to block 156 at offset 0x1380000
Writing data to block 157 at offset 0x13a0000
Writing data to block 158 at offset 0x13c0000
Writing data to block 159 at offset 0x13e0000
Writing data to block 160 at offset 0x1400000
Writing data to block 161 at offset 0x1420000
Writing data to block 162 at offset 0x1440000
Writing data to block 163 at offset 0x1460000
Writing data to block 164 at offset 0x1480000
Writing data to block 165 at offset 0x14a0000
Writing data to block 166 at offset 0x14c0000
Writing data to block 167 at offset 0x14e0000
Writing data to block 168 at offset 0x1500000
Writing data to block 169 at offset 0x1520000
Writing data to block 170 at offset 0x1540000
Writing data to block 171 at offset 0x1560000
Writing data to block 172 at offset 0x1580000
Writing data to block 173 at offset 0x15a0000
Writing data to block 174 at offset 0x15c0000
Writing data to block 175 at offset 0x15e0000
Writing data to block 176 at offset 0x1600000
Writing data to block 177 at offset 0x1620000
Writing data to block 178 at offset 0x1640000
Writing data to block 179 at offset 0x1660000
Writing data to block 180 at offset 0x1680000
Writing data to block 181 at offset 0x16a0000
Writing data to block 182 at offset 0x16c0000
Writing data to block 183 at offset 0x16e0000
Writing data to block 184 at offset 0x1700000
Writing data to block 185 at offset 0x1720000
Writing data to block 186 at offset 0x1740000
Writing data to block 187 at offset 0x1760000
Writing data to block 188 at offset 0x1780000
Writing data to block 189 at offset 0x17a0000
Writing data to block 190 at offset 0x17c0000
Writing data to block 191 at offset 0x17e0000
Writing data to block 192 at offset 0x1800000
Writing data to block 193 at offset 0x1820000
Writing data to block 194 at offset 0x1840000
Writing data to block 195 at offset 0x1860000
Writing data to block 196 at offset 0x1880000
Writing data to block 197 at offset 0x18a0000
Writing data to block 198 at offset 0x18c0000
Writing data to block 199 at offset 0x18e0000
Writing data to block 200 at offset 0x1900000
Writing data to block 201 at offset 0x1920000
Writing data to block 202 at offset 0x1940000
Writing data to block 203 at offset 0x1960000
Writing data to block 204 at offset 0x1980000
Writing data to block 205 at offset 0x19a0000
Writing data to block 206 at offset 0x19c0000
Writing data to block 207 at offset 0x19e0000
Writing data to block 208 at offset 0x1a00000
Writing data to block 209 at offset 0x1a20000
Writing data to block 210 at offset 0x1a40000
Writing data to block 211 at offset 0x1a60000
Writing data to block 212 at offset 0x1a80000
Writing data to block 213 at offset 0x1aa0000
Writing data to block 214 at offset 0x1ac0000
Writing data to block 215 at offset 0x1ae0000
Writing data to block 216 at offset 0x1b00000
Writing data to block 217 at offset 0x1b20000
Writing data to block 218 at offset 0x1b40000
Writing data to block 219 at offset 0x1b60000
Writing data to block 220 at offset 0x1b80000
Writing data to block 221 at offset 0x1ba0000
Writing data to block 222 at offset 0x1bc0000
Writing data to block 223 at offset 0x1be0000
Writing data to block 224 at offset 0x1c00000
Writing data to block 225 at offset 0x1c20000
Writing data to block 226 at offset 0x1c40000
Writing data to block 227 at offset 0x1c60000
Writing data to block 228 at offset 0x1c80000
Writing data to block 229 at offset 0x1ca0000
Writing data to block 230 at offset 0x1cc0000
Writing data to block 231 at offset 0x1ce0000
Writing data to block 232 at offset 0x1d00000
Writing data to block 233 at offset 0x1d20000
Writing data to block 234 at offset 0x1d40000
Writing data to block 235 at offset 0x1d60000
Writing data to block 236 at offset 0x1d80000
Writing data to block 237 at offset 0x1da0000
Writing data to block 238 at offset 0x1dc0000
Writing data to block 239 at offset 0x1de0000
Writing data to block 240 at offset 0x1e00000
Writing data to block 241 at offset 0x1e20000
Writing data to block 242 at offset 0x1e40000
Writing data to block 243 at offset 0x1e60000
Writing data to block 244 at offset 0x1e80000
Writing data to block 245 at offset 0x1ea0000
Writing data to block 246 at offset 0x1ec0000
Writing data to block 247 at offset 0x1ee0000
Writing data to block 248 at offset 0x1f00000
Writing data to block 249 at offset 0x1f20000
Writing data to block 250 at offset 0x1f40000
Writing data to block 251 at offset 0x1f60000
Writing data to block 252 at offset 0x1f80000
Writing data to block 253 at offset 0x1fa0000
Writing data to block 254 at offset 0x1fc0000
Writing data to block 255 at offset 0x1fe0000
Writing data to block 256 at offset 0x2000000
Writing data to block 257 at offset 0x2020000
Writing data to block 258 at offset 0x2040000
Writing data to block 259 at offset 0x2060000
Writing data to block 260 at offset 0x2080000
Writing data to block 261 at offset 0x20a0000
Writing data to block 262 at offset 0x20c0000
Writing data to block 263 at offset 0x20e0000
Writing data to block 264 at offset 0x2100000
Writing data to block 265 at offset 0x2120000
Writing data to block 266 at offset 0x2140000
Writing data to block 267 at offset 0x2160000
Writing data to block 268 at offset 0x2180000
Writing data to block 269 at offset 0x21a0000
Writing data to block 270 at offset 0x21c0000
Writing data to block 271 at offset 0x21e0000
Writing data to block 272 at offset 0x2200000
Writing data to block 273 at offset 0x2220000
Writing data to block 274 at offset 0x2240000
Writing data to block 275 at offset 0x2260000
Writing data to block 276 at offset 0x2280000
Writing data to block 277 at offset 0x22a0000
Writing data to block 278 at offset 0x22c0000
Writing data to block 279 at offset 0x22e0000
Writing data to block 280 at offset 0x2300000
Writing data to block 281 at offset 0x2320000
Writing data to block 282 at offset 0x2340000
Writing data to block 283 at offset 0x2360000
Writing data to block 284 at offset 0x2380000
Writing data to block 285 at offset 0x23a0000
Writing data to block 286 at offset 0x23c0000
Writing data to block 287 at offset 0x23e0000
Writing data to block 288 at offset 0x2400000
Writing data to block 289 at offset 0x2420000
Writing data to block 290 at offset 0x2440000
Writing data to block 291 at offset 0x2460000
Writing data to block 292 at offset 0x2480000
Writing data to block 293 at offset 0x24a0000
Writing data to block 294 at offset 0x24c0000
Writing data to block 295 at offset 0x24e0000
Writing data to block 296 at offset 0x2500000
Writing data to block 297 at offset 0x2520000
Writing data to block 298 at offset 0x2540000
Writing data to block 299 at offset 0x2560000
Writing data to block 300 at offset 0x2580000
Writing data to block 301 at offset 0x25a0000
Writing data to block 302 at offset 0x25c0000
Writing data to block 303 at offset 0x25e0000
Writing data to block 304 at offset 0x2600000
Writing data to block 305 at offset 0x2620000
Writing data to block 306 at offset 0x2640000
Writing data to block 307 at offset 0x2660000
Writing data to block 308 at offset 0x2680000
Writing data to block 309 at offset 0x26a0000
Writing data to block 310 at offset 0x26c0000
Writing data to block 311 at offset 0x26e0000
Writing data to block 312 at offset 0x2700000
Writing data to block 313 at offset 0x2720000
Writing data to block 314 at offset 0x2740000
Writing data to block 315 at offset 0x2760000
Writing data to block 316 at offset 0x2780000
Writing data to block 317 at offset 0x27a0000
Writing data to block 318 at offset 0x27c0000
Writing data to block 319 at offset 0x27e0000
Writing data to block 320 at offset 0x2800000
Writing data to block 321 at offset 0x2820000
Writing data to block 322 at offset 0x2840000
Writing data to block 323 at offset 0x2860000
Writing data to block 324 at offset 0x2880000
Writing data to block 325 at offset 0x28a0000
Writing data to block 326 at offset 0x28c0000
Writing data to block 327 at offset 0x28e0000
Writing data to block 328 at offset 0x2900000
Writing data to block 329 at offset 0x2920000
Writing data to block 330 at offset 0x2940000
Writing data to block 331 at offset 0x2960000
Writing data to block 332 at offset 0x2980000
Writing data to block 333 at offset 0x29a0000
Writing data to block 334 at offset 0x29c0000
Writing data to block 335 at offset 0x29e0000
Writing data to block 336 at offset 0x2a00000
Writing data to block 337 at offset 0x2a20000
Writing data to block 338 at offset 0x2a40000
Writing data to block 339 at offset 0x2a60000
Writing data to block 340 at offset 0x2a80000
Writing data to block 341 at offset 0x2aa0000
Writing data to block 342 at offset 0x2ac0000
Writing data to block 343 at offset 0x2ae0000
Writing data to block 344 at offset 0x2b00000
Writing data to block 345 at offset 0x2b20000
Writing data to block 346 at offset 0x2b40000
Writing data to block 347 at offset 0x2b60000
Writing data to block 348 at offset 0x2b80000
Writing data to block 349 at offset 0x2ba0000
Writing data to block 350 at offset 0x2bc0000
Writing data to block 351 at offset 0x2be0000
Writing data to block 352 at offset 0x2c00000
Writing data to block 353 at offset 0x2c20000
Writing data to block 354 at offset 0x2c40000
Writing data to block 355 at offset 0x2c60000
Writing data to block 356 at offset 0x2c80000
Writing data to block 357 at offset 0x2ca0000
Writing data to block 358 at offset 0x2cc0000
Writing data to block 359 at offset 0x2ce0000
Writing data to block 360 at offset 0x2d00000
Writing data to block 361 at offset 0x2d20000
Writing data to block 362 at offset 0x2d40000
Writing data to block 363 at offset 0x2d60000
Writing data to block 364 at offset 0x2d80000
Writing data to block 365 at offset 0x2da0000
Writing data to block 366 at offset 0x2dc0000
Writing data to block 367 at offset 0x2de0000
Writing data to block 368 at offset 0x2e00000
Writing data to block 369 at offset 0x2e20000
Writing data to block 370 at offset 0x2e40000
Writing data to block 371 at offset 0x2e60000
Writing data to block 372 at offset 0x2e80000
Writing data to block 373 at offset 0x2ea0000
Writing data to block 374 at offset 0x2ec0000
Writing data to block 375 at offset 0x2ee0000
Writing data to block 376 at offset 0x2f00000
Writing data to block 377 at offset 0x2f20000
Writing data to block 378 at offset 0x2f40000
Writing data to block 379 at offset 0x2f60000
Writing data to block 380 at offset 0x2f80000
Writing data to block 381 at offset 0x2fa0000
Writing data to block 382 at offset 0x2fc0000
Writing data to block 383 at offset 0x2fe0000
Writing data to block 384 at offset 0x3000000
Writing data to block 385 at offset 0x3020000
Writing data to block 386 at offset 0x3040000
Writing data to block 387 at offset 0x3060000
Writing data to block 388 at offset 0x3080000
Writing data to block 389 at offset 0x30a0000
Writing data to block 390 at offset 0x30c0000
Writing data to block 391 at offset 0x30e0000
Writing data to block 392 at offset 0x3100000
Writing data to block 393 at offset 0x3120000
Writing data to block 394 at offset 0x3140000
Writing data to block 395 at offset 0x3160000
Writing data to block 396 at offset 0x3180000
Writing data to block 397 at offset 0x31a0000
Writing data to block 398 at offset 0x31c0000
Writing data to block 399 at offset 0x31e0000
Writing data to block 400 at offset 0x3200000
Writing data to block 401 at offset 0x3220000
Writing data to block 402 at offset 0x3240000
Writing data to block 403 at offset 0x3260000
Writing data to block 404 at offset 0x3280000
Writing data to block 405 at offset 0x32a0000
Writing data to block 406 at offset 0x32c0000
Writing data to block 407 at offset 0x32e0000
Writing data to block 408 at offset 0x3300000
Writing data to block 409 at offset 0x3320000
Writing data to block 410 at offset 0x3340000
Writing data to block 411 at offset 0x3360000
Writing data to block 412 at offset 0x3380000
Writing data to block 413 at offset 0x33a0000
Writing data to block 414 at offset 0x33c0000
Writing data to block 415 at offset 0x33e0000
Writing data to block 416 at offset 0x3400000
Writing data to block 417 at offset 0x3420000
Writing data to block 418 at offset 0x3440000
Writing data to block 419 at offset 0x3460000
Writing data to block 420 at offset 0x3480000
Writing data to block 421 at offset 0x34a0000
Writing data to block 422 at offset 0x34c0000
Writing data to block 423 at offset 0x34e0000
Writing data to block 424 at offset 0x3500000
Writing data to block 425 at offset 0x3520000
Writing data to block 426 at offset 0x3540000
Writing data to block 427 at offset 0x3560000
Writing data to block 428 at offset 0x3580000
Writing data to block 429 at offset 0x35a0000
Writing data to block 430 at offset 0x35c0000
Writing data to block 431 at offset 0x35e0000
Writing data to block 432 at offset 0x3600000
Writing data to block 433 at offset 0x3620000
Writing data to block 434 at offset 0x3640000
Writing data to block 435 at offset 0x3660000
Writing data to block 436 at offset 0x3680000
Writing data to block 437 at offset 0x36a0000
Writing data to block 438 at offset 0x36c0000
Writing data to block 439 at offset 0x36e0000
Writing data to block 440 at offset 0x3700000
Writing data to block 441 at offset 0x3720000
Writing data to block 442 at offset 0x3740000
Writing data to block 443 at offset 0x3760000
Writing data to block 444 at offset 0x3780000
Writing data to block 445 at offset 0x37a0000
Writing data to block 446 at offset 0x37c0000
Writing data to block 447 at offset 0x37e0000
Writing data to block 448 at offset 0x3800000
Writing data to block 449 at offset 0x3820000
Writing data to block 450 at offset 0x3840000
Writing data to block 451 at offset 0x3860000
Writing data to block 452 at offset 0x3880000
Writing data to block 453 at offset 0x38a0000
Writing data to block 454 at offset 0x38c0000
Writing data to block 455 at offset 0x38e0000
Writing data to block 456 at offset 0x3900000
Writing data to block 457 at offset 0x3920000
Writing data to block 458 at offset 0x3940000
Writing data to block 459 at offset 0x3960000
Writing data to block 460 at offset 0x3980000
Writing data to block 461 at offset 0x39a0000
Writing data to block 462 at offset 0x39c0000
Writing data to block 463 at offset 0x39e0000
Writing data to block 464 at offset 0x3a00000
Writing data to block 465 at offset 0x3a20000
Writing data to block 466 at offset 0x3a40000
Writing data to block 467 at offset 0x3a60000
Writing data to block 468 at offset 0x3a80000
Writing data to block 469 at offset 0x3aa0000
Writing data to block 470 at offset 0x3ac0000
Writing data to block 471 at offset 0x3ae0000
Writing data to block 472 at offset 0x3b00000
Writing data to block 473 at offset 0x3b20000
Writing data to block 474 at offset 0x3b40000
Writing data to block 475 at offset 0x3b60000
Writing data to block 476 at offset 0x3b80000
Writing data to block 477 at offset 0x3ba0000
Writing data to block 478 at offset 0x3bc0000
Writing data to block 479 at offset 0x3be0000
Writing data to block 480 at offset 0x3c00000
Writing data to block 481 at offset 0x3c20000
Writing data to block 482 at offset 0x3c40000
Writing data to block 483 at offset 0x3c60000
Writing data to block 484 at offset 0x3c80000
Writing data to block 485 at offset 0x3ca0000
Writing data to block 486 at offset 0x3cc0000
Writing data to block 487 at offset 0x3ce0000
Writing data to block 488 at offset 0x3d00000
Writing data to block 489 at offset 0x3d20000
Writing data to block 490 at offset 0x3d40000
Writing data to block 491 at offset 0x3d60000
Writing data to block 492 at offset 0x3d80000
Writing data to block 493 at offset 0x3da0000
Writing data to block 494 at offset 0x3dc0000
Writing data to block 495 at offset 0x3de0000
Writing data to block 496 at offset 0x3e00000
Writing data to block 497 at offset 0x3e20000
Writing data to block 498 at offset 0x3e40000
Writing data to block 499 at offset 0x3e60000
Writing data to block 500 at offset 0x3e80000
Writing data to block 501 at offset 0x3ea0000
Writing data to block 502 at offset 0x3ec0000
Writing data to block 503 at offset 0x3ee0000
Writing data to block 504 at offset 0x3f00000
Writing data to block 505 at offset 0x3f20000
Writing data to block 506 at offset 0x3f40000
Writing data to block 507 at offset 0x3f60000
Writing data to block 508 at offset 0x3f80000
Writing data to block 509 at offset 0x3fa0000
Writing data to block 510 at offset 0x3fc0000
Writing data to block 511 at offset 0x3fe0000
Written 32768 blocks containing only 0xff bytes
Those block may be incorrectly treated as empty!
====[ Mounting /dev/mtdblock1 on /mnt/yaffs ]====
[   39.686733] ====[ Mounting /dev/mtdblock1 on /mnt/yaffs ]====
[   39.688538] yaffs: dev is 32505857 name is "mtdblock1" rw
[   39.688687] yaffs: passed flags ""
====[ Dumping initial / on /dev/mtd1 ]====
[   39.694917] ====[ Dumping initial / on /dev/mtd1 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating /mnt/yaffs/file1.txt ]====
[   41.517285] ====[ Creating /mnt/yaffs/file1.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating chained directories /mnt/yaffs/dir1/dir2/dir3 ]====
[   48.250692] ====[ Creating chained directories /mnt/yaffs/dir1/dir2/dir3 ]====
====[ Creating chained directories /mnt/yaffs/dir1/dir4/dir5 ]====
[   48.261146] ====[ Creating chained directories /mnt/yaffs/dir1/dir4/dir5 ]====
====[ Creating chained directories /mnt/yaffs/dir6 ]====
[   48.268315] ====[ Creating chained directories /mnt/yaffs/dir6 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating /mnt/yaffs/dir1/dir2/dir3/link1 -> ../../../test1.txt ]====
[   54.999888] ====[ Creating /mnt/yaffs/dir1/dir2/dir3/link1 -> ../../../test1.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating named pipe /mnt/yaffs/dir1/dir2/named_pipe ]====
[   61.743501] ====[ Creating named pipe /mnt/yaffs/dir1/dir2/named_pipe ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating block device /mnt/yaffs/dir1/dir4/dir5/block_device ]====
[   68.488485] ====[ Creating block device /mnt/yaffs/dir1/dir4/dir5/block_device ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating unix socket /mnt/yaffs/dir6/aSocket.sock ]====
[   75.240688] ====[ Creating unix socket /mnt/yaffs/dir6/aSocket.sock ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Moving directory /mnt/yaffs/dir1/dir4/dir5 in /mnt/yaffs/dir1/dir2 ]====
[   81.977201] ====[ Moving directory /mnt/yaffs/dir1/dir4/dir5 in /mnt/yaffs/dir1/dir2 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Delete /mnt/yaffs/dir1/dir2/dir5 ]====
[   88.714167] ====[ Delete /mnt/yaffs/dir1/dir2/dir5 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Rename /mnt/yaffs/dir1/dir4 in /mnt/yaffs/dir1/dir41 ]====
[   95.453234] ====[ Rename /mnt/yaffs/dir1/dir4 in /mnt/yaffs/dir1/dir41 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating /mnt/yaffs/dir1/dir41/file2.txt ]====
[  102.215981] ====[ Creating /mnt/yaffs/dir1/dir41/file2.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Copying /mnt/yaffs/dir1/lorem.txt ]====
[  108.938022] ====[ Copying /mnt/yaffs/dir1/lorem.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Truncating /mnt/yaffs/dir1/lorem.txt ]====
[  115.669385] ====[ Truncating /mnt/yaffs/dir1/lorem.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Fin ]====
[  122.403254] ====[ Fin ]====

```

All snapshots are saved in /mnt/disk/result/simul_1

Then exit the QEMU emulation with 

```bash
~ # halt -f
```
If you want to explore one of them, *do not forget* to unzip it first before running nand.py tools




