# Lab 2 — A Windows guest, and a network between them

Pair: Mirdzhalilov / Katranov Driver first half: Mirdzhalilov
Machine: Windows 11 Host, 16 GB RAM, 6 cores / 12 threads, guests Ubuntu Server + Windows 11 Enterprise eval
Date: 10.11.2026

## What I did

1. Downloaded Windows 11 Enterprise evaluation. Licence: [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/download-windows-11-enterprise)
2. Created `lab02-windows`: 2 vCPU, 4 GB RAM, 64 GB thin disk, UEFI + Secure Boot, vTPM.
3. Network mode: `NAT Network`, both guests. Why: Standard NAT isolates each VM behind its own router so they cannot communicate, Bridged mode is often blocked by campus Wi-Fi, and Host-Only lacks internet. NAT Network puts both guests in a single shared subnet so they can reach each other while maintaining routed internet access.
4. Ping Ubuntu → Windows timed out because Windows Defender Firewall blocks incoming ICMP echo requests by default. Fixed with: `New-NetFirewallRule -DisplayName "Allow ping in (ICMPv4)" -Protocol ICMPv4 -IcmpType 8 -Direction Inbound -Action Allow`
5. Overcommitment: set  GB + 20 GB on a 16 GB host.

## Network diagram
```
          Internet
             |
  Host laptop 192.168.100.10
             |
 [VirtualBox NAT Network · 10.0.2.0/24]
      /                        \
lab01-ubuntu               lab02-windows
10.0.2.3                   10.0.2.4
```
## Result

|                       | Before  | After                                                                                                      |
| --------------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| Host RAM in use       | 7.9 GB  | 15.7 GB                                                                                                    |
| Available             | 24.0 GB | 1.1 GB                                                                                                     |
| Committed / Swap used | 10.8/15.7 GB | 57.7/58.8 GB                                                                                                    |
| What I noticed        | —       | Significant system sluggishness, UI lag, mouse stuttering, and heavy memory compression/paging on the host |

## What did not work the first time

When attempting to capture the Ubuntu IP address and test SSH connection from the host using `ssh -p 2222 bao@127.0.0.1`, the connection returned a `Connection refused` error because the Guest IP in the VirtualBox port forwarding rule was incorrectly set to the network address (`10.0.2.0`) instead of the actual guest IP (`10.0.2.3`). This was resolved by checking the real IP via `ip -br a` inside Ubuntu and correcting the rule configuration in VirtualBox.

## Evidence

- [evidence/ipconfig-windows.txt](evidence/ipconfig-windows.txt) — Windows address
- [evidence/ip-addr-linux.txt](evidence/ip-addr-linux.txt) — Ubuntu address
- [evidence/ping-both-ways.txt](evidence/ping-both-ways.txt) — both directions and the internet
- [evidence/host-memory-before.png](evidence/host-memory-before.png) — host memory, guests off
- [evidence/host-memory-after.png](evidence/host-memory-after.png) — host memory, both guests overcommitted
