# pfSense Network Lab — Segmentation, Firewall Rules & Packet Analysis

> Companion lab for the portfolio's *Network Infrastructure & SCADA Security*
> card. A safe, public stand-in for confidential OT/network work — it proves
> segmentation and packet-level competence without touching any real system.

![Network topology](docs/topology.png) <!-- [add: VLAN topology diagram] -->

## Overview

A pfSense (or OPNsense) firewall running as a VM, with multiple VLANs that
emulate a segmented enterprise network — including an **isolated "OT/SCADA-like"
segment** kept separate from corporate IT. Firewall rules are documented and
validated with Wireshark.

## Segments

| VLAN | Purpose | Example subnet |
|------|---------|----------------|
| 10 | Corporate LAN | `[10.10.10.0/24]` |
| 20 | Servers | `[10.10.20.0/24]` |
| 30 | OT / SCADA-like (isolated) | `[10.10.30.0/24]` |

## Firewall ruleset

`[Document allow/deny rules between segments. Key intent:
corporate → servers limited; nothing → OT except explicitly allowed; OT → internet denied.]`

| From | To | Ports | Action | Why |
|------|----|-------|--------|-----|
| LAN | Servers | `[443, 3389…]` | allow | `[reason]` |
| LAN | OT | any | **deny** | IT/OT isolation |
| OT | WAN | any | **deny** | OT stays offline |

## Validation with Wireshark

- [ ] Capture showing an **allowed** flow (e.g. LAN → Servers:443)
- [ ] Capture showing a **blocked** flow (e.g. LAN → OT, dropped at firewall)
- [ ] Annotated screenshots in `docs/`

## Build steps

1. pfSense/OPNsense VM on `[Proxmox / VirtualBox]` — `[notes]`
2. Create VLAN interfaces + DHCP per segment — `[notes]`
3. Write and order firewall rules — `[notes]`
4. Capture + annotate traffic with Wireshark — `[notes]`

## Lessons learned

`[e.g. rule ordering matters; default-deny between segments; logging blocked traffic]`

## Skills demonstrated

`pfSense / Firewall` · `Network Config` · `Network Security` · `Wireshark` · `VLAN segmentation` · `IT/OT isolation`

> Doubles as hands-on prep for **CompTIA Network+**.
