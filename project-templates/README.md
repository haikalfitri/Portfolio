# Project templates (staging)

These are **starter READMEs** for the public proof projects that back the
infrastructure work on the portfolio. They exist to fix the core gap: the
infra cards describe real Cypark work that can't be published, so each one
gets a **companion homelab/lab repo** that demonstrates the same skill in a
way anyone can verify.

## How to use

1. Pick a folder below and create a **new GitHub repo** with the same name
   (e.g. `proxmox-homelab`).
2. Copy that folder's `README.md` into the new repo and fill in the
   `[bracketed]` placeholders, diagrams, and screenshots as you build.
3. Back in the portfolio, find the matching infra card in `index.html`, and
   **uncomment the `projects-icon` footer** (each card has a `TODO` block) so
   the card links to your new repo.
4. On your GitHub profile: pin these repos and use the topics
   `proxmox`, `pfsense`, `m365`, `homelab`, `networking`, `automation`.

## The projects (priority order)

| # | Repo | Backs which card | Effort |
|---|------|------------------|--------|
| 1 | `it-asset-inventory-toolkit` | IT Endpoint & Device Management | ~1–2 evenings (do first) |
| 2 | `proxmox-homelab` | Proxmox Virtualisation & Backup | ~1–2 weekends (flagship) |
| 3 | `pfsense-network-lab` | Network Infrastructure & SCADA | ~1 weekend |
| 4 | `m365-entra-lab` | Microsoft 365 & SharePoint | ~1 weekend |
| 5 | `remote-access-deployment-playbook` | Company-Wide Remote Access | ~1 evening (write-up) |
| — | `proxmox-iac` *(growth)* | — (level-up: IaC) | ~1 weekend |
| — | `infra-monitoring` *(growth)* | — (level-up: observability) | ~1 weekend |

## Redaction rules (for any sanitised case study)

- No client/vendor-internal names beyond the employer already on your CV.
- No real IPs, hostnames, subnets, or topology that maps to real sites.
- No credentials or raw config dumps.
- Diagrams use generic boxes ("Site A", "Core Switch", "Firewall").
- If unsure whether something is shareable, ask your manager first.

> This folder is staging — once each repo is live you can delete the folder
> (or keep it as drafts). It does not need to ship on the portfolio site.
