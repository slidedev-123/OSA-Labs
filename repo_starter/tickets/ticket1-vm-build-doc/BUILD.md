# Build Document: Setting Up Test Virtual Machines

**For:** Aigerim T. (Office Manager)  
**Goal:** Set up Ubuntu Server and Windows 11 Enterprise Evaluation virtual machines in VirtualBox.

## Before you start

1. Download and install VirtualBox from the [official website](https://www.virtualbox.org/). The main VirtualBox package is licensed under GPLv3. The Extension Pack is optional and has a separate license; see the [licensing overview](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/Introduction.html#virtualbox-components).
2. Download Ubuntu Server from the [official Ubuntu page](https://ubuntu.com/download/server).
3. Download Windows 11 Enterprise Evaluation from the [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/download-windows-11-enterprise).

The evaluation edition is intended for trying Windows without buying a regular license for this test machine.

**Download screenshots:** [Ubuntu Server ISO](evidence/18-ubuntu-iso.png) and [Windows Enterprise Evaluation ISO](evidence/19-windows-iso-download.png). The Windows download shown is build 26300; the installed guest in evidence/12 is build 26100, so this screenshot records a separate download.

## Step 1 — Create the Ubuntu VM

In VirtualBox Manager, choose **New**. Name the VM `lab01-ubuntu`, select the Ubuntu Server ISO and Ubuntu 64-bit profile, set **Machine Folder** to `D:\VM\VirtualBox VMs`, and leave **Proceed with Unattended Installation** enabled. Assign 2 processors, 4096 MB RAM, and a 25 GB dynamically allocated virtual disk.

**Why:** The wizard repeats the setup choices for this Ubuntu VM. Keeping both VMs in the same D: folder makes them easier to find, and a dynamic disk grows as it is used.  
**Check:** The summary shows the VM name, ISO, resources, disk size, and D: folder.  
**Evidence:** [evidence/01-new-vm-wizard.png](evidence/01-new-vm-wizard.png) shows the Ubuntu choices and folder. [evidence/02-disk-settings.png](evidence/02-disk-settings.png) shows the disk size and dynamic allocation. The saved VM paths and D: free space are listed in [evidence/11-vm-storage-and-free-space.txt](evidence/11-vm-storage-and-free-space.txt).

## Step 2 — Start Ubuntu and check it

Start `lab01-ubuntu` and let the unattended installation finish. Sign in using the account details entered in the wizard, then run:

```bash
uname -a
lsb_release -a
```

**Why:** These commands show the Ubuntu release and kernel running in the VM.  
**Check:** Both commands return Ubuntu and kernel information.  
**Evidence:** [evidence/04-guest-uname.txt](evidence/04-guest-uname.txt) contains the commands and their output; [evidence/14-ubuntu-verification.png](evidence/14-ubuntu-verification.png) shows the commands in the running Ubuntu VM.

## Step 3 — Connect Ubuntu to the shared network

Shut down `lab01-ubuntu`. In VirtualBox Manager, open **Tools → Network → NAT Networks**. If `NatNetwork` does not exist, create it, name it `NatNetwork`, set the IPv4 prefix to `10.0.2.0/24`, and enable DHCP.

Open `lab01-ubuntu` **Settings → Network → Adapter 1**. Set **Attached to** to **NAT Network** and choose `NatNetwork`.

**Why:** NAT Network lets both VMs communicate with each other and reach the internet. Standard NAT provides internet access but does not connect the guests to each other. Bridged networking puts a guest directly on the physical network and may be restricted by MAC filtering.  
**Check:** Adapter 1 shows **NAT Network** and `NatNetwork`.  
**Evidence:** [evidence/03-network-adapter.png](evidence/03-network-adapter.png) shows the Ubuntu network setting.

## Step 4 — Create the Windows VM

Choose **New** in VirtualBox Manager. Name the VM `lab02-windows`, select the Windows 11 Enterprise Evaluation ISO, and set **Machine Folder** to `D:\VM\VirtualBox VMs`. Assign 2 processors, 4096 MB RAM, and a 64 GB dynamically allocated disk. Enable EFI, Secure Boot, and TPM 2.0.

**Why:** Two processors and 4 GB RAM give Windows resources for setup while leaving host resources for Ubuntu; allocating more would leave less CPU and memory for the host and the other VM. EFI, Secure Boot, and TPM 2.0 provide the firmware and security features expected by Windows 11. D: had about 303 GB free when checked, and both virtual disks can use up to 89 GB in total.
**Check:** The summary shows the selected resources, firmware, and disk.  
**Evidence:** [evidence/07-windows-vm-settings.png](evidence/07-windows-vm-settings.png) shows the Windows settings and its `NatNetwork` adapter. The VM paths and disk space are in [evidence/11-vm-storage-and-free-space.txt](evidence/11-vm-storage-and-free-space.txt).

## Step 5 — Install Windows

Start `lab02-windows`. If the boot menu appears, choose the virtual CD-ROM. Follow Windows Setup, accept the displayed terms, select the VM's unallocated virtual disk, and finish the first-run setup.

**Why:** The virtual CD-ROM starts the installer from the Windows ISO; selecting the virtual disk installs Windows inside the VM.  
**Check:** Complete Windows setup until the desktop appears.  
**Evidence:** [evidence/08-windows-boot-manager.png](evidence/08-windows-boot-manager.png) shows the boot menu, [evidence/09-windows-license-terms.png](evidence/09-windows-license-terms.png) shows the license screen, and [evidence/10-windows-account-setup.png](evidence/10-windows-account-setup.png) shows the first-run account setup; [evidence/12-windows-desktop.png](evidence/12-windows-desktop.png) shows the completed desktop.

## Step 6 — Connect Windows to the shared network

Shut down `lab02-windows`, then open its **Settings → Network → Adapter 1**. Set **Attached to** to **NAT Network** and choose `NatNetwork`.

**Why:** Both VMs need the same NAT Network to communicate.  
**Check:** Adapter 1 shows `NatNetwork`.  
**Evidence:** The Windows network setting is visible in [evidence/07-windows-vm-settings.png](evidence/07-windows-vm-settings.png).

## Step 7 — Check network access

In Ubuntu, check the address with `ip -br a`; in Windows, use `ipconfig`. Then run the guest-to-guest and internet checks:

```bash
ping -c 4 10.0.2.4
ping -c 4 ubuntu.com
```

```powershell
ping 10.0.2.3
ping ubuntu.com
```

If DHCP assigned different addresses, use the addresses shown by the address commands.

**Why:** The checks confirm that the VMs can reach each other and the internet.  
**Check:** Each ping receives replies without packet loss.  
**Evidence:** [evidence/05-ping-between-guests.txt](evidence/05-ping-between-guests.txt) contains the full command output. [evidence/15-ubuntu-ping-tests.png](evidence/15-ubuntu-ping-tests.png) shows Ubuntu's successful pings to Windows and the internet; [evidence/16-windows-ping-tests.png](evidence/16-windows-ping-tests.png) shows the corresponding Windows checks.

## Step 8 — Allow ping through Windows Firewall if needed

If Ubuntu cannot ping Windows but the other network checks work, open PowerShell as Administrator in Windows and run:

```powershell
New-NetFirewallRule -DisplayName "Allow ping in (ICMPv4)" -Protocol ICMPv4 -IcmpType 8 -Direction Inbound -Action Allow
```

Then verify the rule in PowerShell:

```powershell
Get-NetFirewallRule -DisplayName "Allow ping in (ICMPv4)" |
  Format-List DisplayName,Enabled,Direction,Action
```

Repeat the Ubuntu-to-Windows ping.

**Why:** This rule allows incoming IPv4 ping requests when Windows Defender Firewall is blocking them.  
**Check:** The repeated ping receives replies.  
**Evidence:** The network checks are in [evidence/05-ping-between-guests.txt](evidence/05-ping-between-guests.txt). [evidence/17-windows-firewall-rule.png](evidence/17-windows-firewall-rule.png) shows the enabled inbound allow rule.

## If the VMs cannot reach each other

Before changing the firewall, power off both VMs and check in each VM's **Settings → Network → Adapter 1** that **Attached to** is **NAT Network** and the selected name is `NatNetwork`. Start both VMs and check their addresses with `ip -br a` in Ubuntu and `ipconfig` in Windows. Both addresses should be in the same subnet. If they are, use Step 8 only if Windows still blocks Ubuntu's ping.

**Why:** Standard NAT and NAT Network can both provide internet access, but only guests on the same NAT Network can communicate directly. Checking the network first avoids changing firewall rules when the VMs are attached to different networks.
**Check:** Both guests show addresses in the same subnet and can ping each other.

## Step 9 — Save and restore an Ubuntu snapshot

Shut down `lab01-ubuntu`, open its **Snapshots** view, choose **Take**, and name the snapshot `clean-baseline`.

To return to this saved state later, right-click `clean-baseline`, choose **Restore**, confirm, and start the VM.

**Why:** The snapshot gives Ubuntu a recovery point after experiments.  
**Check:** `clean-baseline` appears in the snapshot list.  
**Evidence:** [evidence/06-snapshot-list.png](evidence/06-snapshot-list.png) shows the snapshot.


## Step 10 — Save and restore a Windows snapshot

Shut down `lab02-windows`, open its **Snapshots** view, choose **Take**, and name the snapshot `clean-baseline`.

To return to this saved state later, right-click `clean-baseline`, choose **Restore**, confirm, and start the VM.

**Why:** This gives the Windows guest its own recovery point before testing.  
**Check:** `clean-baseline` appears under `lab02-windows` in the snapshot list.  
**Evidence:** [evidence/13-windows-snapshot.png](evidence/13-windows-snapshot.png) shows the Windows VM and its `clean-baseline` snapshot.
