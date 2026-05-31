# Proxmox Homelab — Virtualisation, Backup & Disaster Recovery

> Companion lab for the portfolio's *Proxmox Virtualisation & Backup* card.
> Demonstrates the same stack I run in production — on my own hardware — so the
> capability is publicly verifiable.

![Architecture diagram](docs/architecture.png) <!-- [add: draw.io / Excalidraw export] -->

## Overview

A single-node (or small cluster) Proxmox VE lab that runs:
- A Linux VM and an LXC container
- A small Active Directory / Samba-AD domain controller
- Proxmox Backup Server (PBS) with scheduled backups, snapshots, and a
  **tested restore**

**Goal:** prove I can provision, isolate, back up, and *recover* virtualised
workloads — not just claim "zero data loss".

## Hardware / environment

| Item | Spec |
|------|------|
| Host | `[mini-PC / old desktop / nested Proxmox VM]` |
| CPU / RAM | `[e.g. 4 cores / 16 GB]` |
| Storage | `[e.g. 1× SSD local-lvm, 1× HDD backup target]` |
| Proxmox VE | `[version]` |
| PBS | `[version — VM or separate node]` |

## Architecture

`[Describe nodes → storage → VMs/LXC → PBS. Embed the diagram above.]`

## Build steps

1. **Install Proxmox VE** — `[notes]`
2. **Provision workloads** — Linux VM + LXC container — `[notes]`
3. **Active Directory** — stand up a Samba-AD / Windows Server DC — `[notes]`
4. **Networking & isolation** — storage pools, resource limits, firewall rules
   to isolate the "production" VMs — `[notes]`
5. **Proxmox Backup Server** — install, add datastore, attach to PVE — `[notes]`
6. **Backup schedule** — automated backups + snapshots — see `[backup-job.md]`

## Backup & disaster-recovery test ⭐ (the part that matters)

> This is what turns "I do backups" into evidence.

- Backup job: `[schedule, retention/prune policy]`
- Replication: `[between nodes / interval]`
- **Restore drill:** `[date]` — restored `[which VM]` from PBS.
  - **RPO** (max data loss): `[e.g. ≤ 24h]`
  - **RTO** (time to restore): `[e.g. 18 min]`
  - Screenshots: `docs/restore-*.png`

## Screenshots

- [ ] Datacenter / node view
- [ ] VM + LXC list
- [ ] PBS datastore + backup job
- [ ] Successful restore

## Scripts

`[link any helper scripts — e.g. snapshot prune cron, healthcheck]`

## Lessons learned

`[2–4 bullets — e.g. an untested backup isn't a backup; replication interval vs RPO trade-off]`

## Skills demonstrated

`Proxmox VE` · `PBS` · `Virtualisation` · `Active Directory` · `Linux` · `Backup/DR`
