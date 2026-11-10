# Ticket 1: New developer starts Monday, needs a test machine

## 1. What was asked

> From: Aigerim T. (Office Manager)
> Subject: test machine for new dev
>
> Hi, we have someone starting on Monday and he needs a test computer set up. Nothing special, just so he can try things without breaking anything. Can you write down how to do it so I can do the next one myself? Thanks

## 2. What was actually needed

"A test computer" is too vague to build from. A usable test environment needs named operating systems, resource limits, network access, and a way to recover. The request leaves out several choices: which operating systems and tasks the developer needs, how much CPU, memory, and disk the host can spare, and whether the guests need internet access and a connection to each other. "Without breaking anything" also doesn't say what has to be protected or how the machine should be restored.

I would ask Aigerim:

- Which operating systems and development tasks does the new developer need?
- How much CPU, memory, and free disk space does the host have, and where should the VM files be stored?
- Do the guests need internet access and a connection to each other?
- Does the office have a hypervisor preference or licence requirement?

I assumed the existing Windows host would run VirtualBox with one Ubuntu Server guest and one Windows 11 Enterprise Evaluation guest. I also assumed both guests need internet access, need to reach each other, and should have a recovery snapshot. Because Aigerim is not an IT specialist, BUILD.md gives clear steps and checks.

## 3. What I did

1. Installed Oracle VM VirtualBox and used the official Ubuntu Server and Windows 11 Enterprise Evaluation images.
2. Created `lab01-ubuntu` and `lab02-windows`, each with 2 vCPUs and 4096 MB RAM. Ubuntu has a 25 GB dynamic disk and Windows has a 64 GB dynamic disk.
3. Installed Ubuntu with the wizard's unattended installation. The Windows screenshots show the setup screens and the finished desktop.
4. Stored both VM configuration files and base virtual disks in `D:\VM\VirtualBox VMs\`. D: had about 303 GB free when I checked. The two disk limits add up to 89 GB, so about 214 GB would remain if both disks reached full size. Exact paths and disk space are in [evidence/11-vm-storage-and-free-space.txt](evidence/11-vm-storage-and-free-space.txt).
5. Connected both guests to `NatNetwork` and ran ping checks between the guests and out to the internet.
6. Created a `clean-baseline` snapshot for each VM.

The first ping from Ubuntu to Windows timed out. I added this inbound ICMPv4 rule in elevated PowerShell and repeated the checks:

```powershell
New-NetFirewallRule -DisplayName "Allow ping in (ICMPv4)" -Protocol ICMPv4 -IcmpType 8 -Direction Inbound -Action Allow
```

The Ubuntu commands were:

```bash
ip -br a
ping -c 4 10.0.2.4
ping -c 4 ubuntu.com
```

The Windows commands were:

```powershell
ipconfig
ping 10.0.2.3
ping ubuntu.com
```

The successful results are in [evidence/05-ping-between-guests.txt](evidence/05-ping-between-guests.txt). I did not save the original timeout or the output from adding the firewall rule.

### Resource and configuration decisions

I considered VMware Workstation as an alternative. I chose VirtualBox because I had used it before and knew it better. VMware would probably have worked too, but learning a new interface would have taken time away from building and documenting the environment.

| Setting | Default | Mine | Why |
|---|---|---|---|
| VM file location | VirtualBox suggests `C:\Users\Admin\VirtualBox VMs` | `D:\VM\VirtualBox VMs\` | D: had about 303 GB free, and keeping both VMs there keeps them together. See [evidence/11-vm-storage-and-free-space.txt](evidence/11-vm-storage-and-free-space.txt). |
| Network adapter | [NAT is the VirtualBox default](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html#network-settings) | NAT Network (`NatNetwork`) | Both guests need internet access and a connection to each other. Bridged networking is another option, but it puts a guest directly on the physical network and may be blocked by MAC filtering. See evidence/03 and evidence/07. |
| Windows virtual disk | The Windows 11 wizard suggests 80 GB | 64 GB, dynamically allocated | A smaller maximum size, while still letting the disk grow as needed. |
| Ubuntu virtual disk | I did not record the original wizard default | 25 GB, dynamically allocated | This is the size shown in evidence/02. I can't confirm whether it differs from the default. |
| CPU and memory | The Windows 11 wizard suggests 2 vCPUs and 4096 MB; I did not record the original Ubuntu defaults | 2 vCPUs and 4096 MB per guest | Lab 0 recorded 6 cores, 12 logical processors, and 32 GB RAM ([CPU](../../labs/lab00-inventory/evidence/cpu.txt), [memory](../../labs/lab00-inventory/evidence/memory.txt)). Lab 1 recorded about 8.9 GB in use at idle. With 4 GB given to each guest, about 15.1 GB would be left for the host at that idle level, though actual use varies ([idle-memory screenshot](../../labs/lab01-first-vm/evidence/host-idle-memory.png)). |

The Windows VM has EFI, Secure Boot, and TPM 2.0 enabled, as shown in [evidence/07-windows-vm-settings.png](evidence/07-windows-vm-settings.png).

## 4. Evidence

- [evidence/01-new-vm-wizard.png](evidence/01-new-vm-wizard.png): Ubuntu VM name, selected image, unattended installation, and D: parent folder.
- [evidence/02-disk-settings.png](evidence/02-disk-settings.png): Ubuntu 25 GB virtual disk, with full-size allocation off.
- [evidence/03-network-adapter.png](evidence/03-network-adapter.png): Ubuntu adapter connected to `NatNetwork`.
- [evidence/04-guest-uname.txt](evidence/04-guest-uname.txt): `uname -a` and `lsb_release -a` commands with Ubuntu output.
- [evidence/05-ping-between-guests.txt](evidence/05-ping-between-guests.txt): successful pings between the guests and from both guests to the internet.
- [evidence/06-snapshot-list.png](evidence/06-snapshot-list.png): Ubuntu `clean-baseline` snapshot.
- [evidence/07-windows-vm-settings.png](evidence/07-windows-vm-settings.png): Windows memory, processors, disk, EFI, Secure Boot, TPM 2.0, and network adapter.
- [evidence/08-windows-boot-manager.png](evidence/08-windows-boot-manager.png): Windows boot menu and virtual CD-ROM.
- [evidence/09-windows-license-terms.png](evidence/09-windows-license-terms.png): Windows Setup license-terms screen.
- [evidence/10-windows-account-setup.png](evidence/10-windows-account-setup.png): Windows first-run account setup.
- [evidence/11-vm-storage-and-free-space.txt](evidence/11-vm-storage-and-free-space.txt): both VM paths, disk locations, and D: capacity and free space.
- [evidence/12-windows-desktop.png](evidence/12-windows-desktop.png): Windows 11 desktop in the running `lab02-windows` VirtualBox window.
- [evidence/13-windows-snapshot.png](evidence/13-windows-snapshot.png): `clean-baseline` snapshot for `lab02-windows` in VirtualBox Manager.
- [evidence/14-ubuntu-verification.png](evidence/14-ubuntu-verification.png): `uname -a` and `lsb_release -a` output in the running Ubuntu guest.
- [evidence/15-ubuntu-ping-tests.png](evidence/15-ubuntu-ping-tests.png): Ubuntu pinging Windows and `ubuntu.com`, with replies and no packet loss.
- [evidence/16-windows-ping-tests.png](evidence/16-windows-ping-tests.png): Windows pinging Ubuntu and `ubuntu.com`, with replies and no packet loss.
- [evidence/17-windows-firewall-rule.png](evidence/17-windows-firewall-rule.png): enabled inbound Windows Firewall rule allowing IPv4 ping requests.
- [evidence/18-ubuntu-iso.png](evidence/18-ubuntu-iso.png): downloaded Ubuntu Server 26.04.1 disk image.
- [evidence/19-windows-iso-download.png](evidence/19-windows-iso-download.png): downloaded Windows Enterprise Evaluation disk image, build 26300. This is a different build from the installed Windows guest in evidence/12.

## 5. What I would do differently

Next time I would export the guests as `.ova` appliances once I've confirmed they boot and use the intended network. That could make setup faster for the next person, though they would still need compatible VirtualBox settings and enough disk space.
