# Lab 3 — Teardown, and the same machine from the command line

Pair: Tair and Robert                    Driver first half: Tair
Machine: Personal laptop
Date: 11/8/2026

## What I did

Copied the text from the table and opened each and every company website to acquire the specs and the images in the png format. After that i composed a description of each component and cross-referenced it with Claude LLM to ensure legitimate and format-faithful descriptions. I edited my descriptions accordingly and lightly formatted the text.

## Result

# Processors

AMD Ryzen 5 7600
“6 cores / 12 threads, 3.8 GHz base and up to 5.1 GHz boost, 38 MB cache (32 MB L3 + 6 MB L2), 65 W TDP. Connects to the AM5 socket; its memory controller supports DDR5. Limit: only AM5 boards, and only DDR5 memory.”

Intel Core i5-13400
“10 cores (6 P + 4 E) / 16 threads, up to 4.6 GHz boost, 20 MB L3 cache, 65 W base power. Connects to the LGA1700 socket; its memory controller supports DDR4 and DDR5. Limit: only LGA1700 boards, and the board decides which memory type you can use.”

# Motherboards

ASUS PRIME B650M-A
“Micro-ATX, B650 chipset. Connects to an AM5 socket, 4 DDR5 DIMM slots, 2 M.2 slots, and 4 SATA ports. Limit: only Ryzen 7000/8000/9000-series CPUs from its CPU Support list (the 7600 is on it), and only DDR5.”

MSI PRO B760M-A WIFI DDR4
“Micro-ATX, B760 chipset. Connects to an LGA1700 socket, 4 DDR4 DIMM slots, 2 M.2 slots, and 4 SATA ports. Limit: only 12th/13th/14th-gen Intel CPUs from its CPU Support list (the 13400 is on it), and only DDR4.”

# Memory

Kingston FURY Beast DDR5-5600, 16 GB
“DDR5 DIMM, 16 GB, 5600 MT/s. Connects to the DIMM slots of a board that takes DDR5, such as the ASUS PRIME B650M-A. Limit: only boards of the same DDR generation, so it won’t fit the MSI DDR4 board.”

Crucial DDR4-3200, 16 GB
“DDR4 DIMM, 16 GB, 3200 MT/s. Connects to the DIMM slots of a board that takes DDR4, such as the MSI PRO B760M-A WIFI DDR4. Limit: only boards of the same DDR generation, so it won’t fit the ASUS DDR5 board.”

# SSDs

Samsung 990 PRO 1 TB
“1 TB, NVMe PCIe 4.0 x4, M.2 2280, up to about 7,450 MB/s read. Connects to an M.2 slot on the board, with no cables. Limit: the bus: PCIe 4.0 x4 tops out near 7,500 MB/s, and in a PCIe 3.0 slot it runs at roughly half that.”

Samsung 870 EVO 1 TB
“1 TB, SATA interface, 2.5″ form factor, up to about 560 MB/s read. Connects to a SATA port on the board with a SATA data cable, plus a power cable from the PSU. Limit: the bus: SATA tops out at about 550 MB/s.”

# Power and cooling

Corsair RM750e
“750 W, 80 PLUS Gold, ATX 3.x (check the box for your revision), fully modular. Connects to the board (24-pin and CPU 8-pin), drives, and a graphics card. Limit: total watts: 750 W is the ceiling for the whole system.”

AMD Wraith Stealth (stock cooler for the Ryzen 5 7600)
“Low-profile top-down air cooler for the AM5 socket. Connects to the processor’s socket, with a 4-pin fan cable to the CPU fan header. Limit: about 65 W of heat, enough for the 7600 at stock settings but not for overclocking.”

Intel Laminar RM1 (stock cooler for the Core i5-13400)
“Low-profile top-down air cooler for the LGA1700 socket. Connects to the processor’s socket, with a 4-pin fan cable to the CPU fan header. Limit: about 65 W of heat, adequate for the 13400 at stock speeds but loud under sustained load.”

# The  builds

## Overview

| Role |  Build B: AMD (AM5, DDR5) |  Build A: Intel (LGA1700, DDR4) |
|:--|:--|:--|
| **CPU** | AMD Ryzen 5 7600 | Intel Core i5-13400 |
| **Motherboard** | ASUS PRIME B650M-A | MSI PRO B760M-A WIFI DDR4 |
| **Memory** | Kingston FURY Beast DDR5-5600, 16 GB | Crucial DDR4-3200, 16 GB |
| **Storage** | Samsung 990 PRO 1 TB (NVMe, M.2) | Samsung 870 EVO 1 TB (SATA, 2.5″) |
| **Cooler** | AMD Wraith Stealth (boxed) | Intel Laminar RM1 (boxed) |
| **Power supply** | Corsair RM750e (750 W) |  Not included |

---


##  Build A: Intel (LGA1700, DDR4)

| Part | Component | Why it goes in this build |
|:--|:--|:--|
| CPU | **Core i5-13400** | LGA1700 CPU that works with DDR4 or DDR5, depending on the board. |
| Motherboard | **MSI PRO B760M-A WIFI DDR4** | The only LGA1700 board in the list; DDR4 only; the 13400 is on its CPU Support list. |
| Memory | **Crucial DDR4-3200, 16 GB** | The only DDR4 module, and the board can't take DDR5. |
| Storage | **Samsung 870 EVO 1 TB** | The leftover drive; SATA works on any board, and ~550 MB/s is fine for general use. |
| Cooler | **Intel Laminar RM1** | Ships with the non-F 13400, fits LGA1700, and suits a 65 W-class chip at stock speeds. |

##  Build B: AMD (AM5, DDR5)

| Part | Component | Why it goes in this build |
|:--|:--|:--|
| CPU | **Ryzen 5 7600** | AM5 CPU that matches the ASUS board's socket and supports only DDR5. |
| Motherboard | **ASUS PRIME B650M-A** | The only AM5 board in the list; DDR5 only; the 7600 is on its CPU Support list. |
| Memory | **Kingston FURY Beast DDR5-5600, 16 GB** | The only DDR5 module, and AM5 can't use DDR4. |
| Storage | **Samsung 990 PRO 1 TB** | The board has M.2 slots, and a PCIe 4.0 NVMe drive can use the full bus. |
| Cooler | **AMD Wraith Stealth** | Ships with the 7600, fits AM5, and handles 65 W at stock settings. |
| Power supply | **Corsair RM750e** | Has the 24-pin and CPU 8-pin connectors; 750 W leaves room for a graphics card later. |

# Links to the parts

# PC parts: maker links

| Part | Maker | Build | Link type | Link | How to find the exact page |
|:--|:--|:--|:--|:--|:--|
| **AMD Ryzen 5 7600** | AMD | A (AMD) |  Official product page | [Open](https://www.amd.com/de/products/processors/desktops/ryzen/7000-series/amd-ryzen-5-7600.html) | German-language page; use the site's country/language selector. Boxed cooler (Wraith Stealth) is covered here. |
| **Intel Core i5-13400** | Intel | B (Intel) |  Official product page | [Open](https://ark.intel.com/content/www/us/en/ark/products/230495/intel-core-i513400-processor-20m-cache-up-to-4-60-ghz.html) | Intel ARK page; also confirms the boxed cooler (Laminar RM1) for the non-F chip. |
| **ASUS PRIME B650M-A** | ASUS | A (AMD) |  Official product page | [Open](https://asus.com/motherboards-components/motherboards/prime/prime-b650m-a/techspec) | Tech specs page. Check the CPU Support list there. |
| **Samsung 990 PRO 1 TB** | Samsung | A (AMD) |  Official product page | [Open](https://www.samsung.com/in/memory-storage/nvme-ssd/990-pro-1tb-nvme-pcie-gen-4-mz-v9p1t0bw) | India store page; use the country selector. Part number MZ-V9P1T0BW. |
| **MSI PRO B760M-A WIFI DDR4** | MSI | B (Intel) |  Maker site only | [Open](https://www.msi.com) | Search the full model name. Part numbers seen: 7D99-001R, 911-7D99-001. |
| **Kingston FURY Beast DDR5-5600, 16 GB** | Kingston | A (AMD) |  Maker site only | [Open](https://www.kingston.com) | Search 'FURY Beast DDR5'. Several variants exist (e.g. KF556C40BBA-16, KF556C40BB-16, both CL40); match your exact part number. |
| **Crucial DDR4-3200, 16 GB** | Crucial | B (Intel) |  Maker site only | [Open](https://www.crucial.com) | Search 'DDR4-3200 16GB'. Not checked: Crucial consumer brand may redirect or have limited support. |
| **Samsung 870 EVO 1 TB** | Samsung | B (Intel) |  Maker site only | [Open](https://samsung.com/ssd) | Open 870 EVO and pick the 1 TB model. Part number MZ-77E1T0B. |
| **Corsair RM750e (750 W)** | Corsair | A (AMD) |  Maker site only | [Open](https://www.corsair.com) | Search 'RM750e'. |
| **AMD Wraith Stealth cooler** | AMD | A (AMD) |  See CPU page | [Open](https://www.amd.com/de/products/processors/desktops/ryzen/7000-series/amd-ryzen-5-7600.html) | Bundled with the boxed Ryzen 5 7600; not sold as a separate listing. |
| **Intel Laminar RM1 cooler** | Intel | B (Intel) |  See CPU page | [Open](https://ark.intel.com/content/www/us/en/ark/products/230495/intel-core-i513400-processor-20m-cache-up-to-4-60-ghz.html) | Bundled with the boxed (non-F) Core i5-13400; not sold as a separate listing. |

## Part 2 — Same facts from the command line

| Fact | Windows host — command and result | Ubuntu VM — command and result | macOS |
| --- | --- | --- | --- |
| CPU model | `Get-CimInstance Win32_Processor | Select Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed` → AMD Ryzen 5 PRO 5650G with Radeon Graphics | `lscpu` → AMD Ryzen 5 PRO 5650G with Radeon Graphics | Not run; include if a Mac was available in the pair. |
| Cores / threads | Same `Get-CimInstance Win32_Processor` command → 6 cores, 12 logical processors | `lscpu` → 2 CPUs, 2 cores, 1 thread per core exposed to the VM | Not run; include if a Mac was available in the pair. |
| Total memory | `Get-CimInstance Win32_PhysicalMemory | Select DeviceLocator, Capacity, Speed, ConfiguredClockSpeed, SMBIOSMemoryType, FormFactor` → four 8 GiB records, 32 GiB total; `DIMM 0` and `DIMM 1` labels repeat | `free -h` → 3.3 GiB total assigned to the VM | Not run; include if a Mac was available in the pair. |
| Memory modules / speed | Same `Get-CimInstance Win32_PhysicalMemory` command → DDR4, 3200 MT/s reported | `sudo dmidecode -t memory` → no module entries or memory speed exposed | Not run; include if a Mac was available in the pair. |
| Disk model / type | `Get-PhysicalDisk | Select FriendlyName, MediaType, BusType, Size` → WDC 1 TB HDD (SATA) and Apacer 512 GB SSD (NVMe) | `lsblk -d -o NAME,MODEL,ROTA,TRAN,SIZE` → `VBOX HARDDISK`, 25 GB, SATA; virtual CD-ROM also listed | Not run; include if a Mac was available in the pair. |
| Free space | `Get-Volume C` → 53.59 GB free of 475.95 GB | `df -h /` → 21 GB available on the 25 GB root filesystem | Not run; include if a Mac was available in the pair. |
| Architecture | `$env:PROCESSOR_ARCHITECTURE` → AMD64 | `uname -m` → x86_64 | Not run; include if a Mac was available in the pair. |

Windows reports the physical host, while Ubuntu reports the virtual machine. The VM exposes two CPUs, 3.3 GiB of memory and a 25 GB virtual disk; it reports the host CPU model but does not expose the host's physical memory-module details to `dmidecode`. The Linux output reports hypervisor vendor KVM and disk model `VBOX HARDDISK`; both are preserved as the guest reported them.


## What did not work the first time

I saved most of the pictures for the evidence file in the file type they came in, which made me change the file types by hand. For my second attempt i added the two builds that would owrk the best with the parts, links to the parts makers sites, the second part and added images for the coolers.

## Evidence

- [evidence/](evidence/) — one line per file on what it proves
