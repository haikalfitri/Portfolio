# Microsoft 365 / Entra Identity Lab

> Companion lab for the portfolio's *Microsoft 365 & SharePoint Administration*
> card. Built entirely in a **free Microsoft 365 Developer tenant** — zero
> connection to any employer data.

## Overview

Demonstrates the identity and collaboration admin tasks from the infra card:
users, groups, licensing, RBAC, Conditional Access + MFA, and a scoped
SharePoint site — plus **PowerShell / Microsoft Graph scripts** that automate
the repetitive parts.

## Setup

1. Join the **Microsoft 365 Developer Program** → get a free, renewable E5
   sandbox tenant: https://developer.microsoft.com/microsoft-365/dev-program
2. `[note your sandbox tenant name — not a real org]`

## What's demonstrated

- [ ] Create users and groups
- [ ] Assign licences (prefer **group-based licensing**)
- [ ] Admin roles / RBAC (least privilege)
- [ ] Conditional Access policy + MFA
- [ ] A SharePoint site with scoped, role-based permissions

## Scripts (`/scripts`)

> Microsoft Graph PowerShell SDK. These make the "I automate identity admin"
> claim concrete.

| Script | Does |
|--------|------|
| `New-BulkUsers.ps1` | Create users from a CSV | `[status]` |
| `Set-GroupLicensing.ps1` | Assign licences via group membership | `[status]` |
| `Get-LicenceReport.ps1` | Export assigned/available licences | `[status]` |

```powershell
# example — fill in with your working snippet
Connect-MgGraph -Scopes "User.ReadWrite.All","Group.ReadWrite.All"
# ...
```

## Screenshots (`/docs`)

- [ ] Entra users + groups
- [ ] Conditional Access policy
- [ ] Role assignment
- [ ] Script output (sanitised)

## Lessons learned

`[e.g. group-based licensing scales better than per-user; CA policies need a break-glass account]`

## Skills demonstrated

`Microsoft 365` · `Entra ID` · `SharePoint` · `RBAC` · `Conditional Access` · `PowerShell / Graph`

> Doubles as study evidence for **MS-900** (and a stepping stone to **AZ-104**).
