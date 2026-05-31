# IT Asset Inventory & Onboarding Toolkit

> Companion project for the portfolio's *IT Endpoint & Device Management* card.
> **Start here — it's the fastest win (~1–2 evenings)** and it fuses your data
> background with IT ops: exactly the "data-driven IT operations" angle the
> portfolio promises.

## What it does

A small script (Python or PowerShell) that:
1. Ingests a device inventory (`CSV`/`JSON`)
2. Validates fields and **flags** devices missing warranty / OS-patch / owner
3. Generates an **onboarding checklist** and an inventory **report**
   (Markdown/HTML — bonus: a small Chart.js dashboard by device type / site)

All sample data is **fabricated** — no real asset data.

## Run

```bash
python inventory_report.py --input sample/devices.csv --out report.html
# or PowerShell: ./Invoke-InventoryReport.ps1 -Input sample/devices.csv
```

## Sample data (`/sample`)

`devices.csv` (fabricated):

```csv
asset_id,type,user,site,os,last_patch,warranty_end
LAP-001,Laptop,A. Example,Site A,Win11,2026-04-01,2027-02-01
DSK-014,Desktop,,Site B,Win10,,2024-09-01
```

## Output

- [ ] `report.html` — inventory summary + flagged items
- [ ] Onboarding checklist for a new hire
- [ ] (bonus) Chart.js dashboard screenshot in `/docs`

## Why this matters

It turns the vague "device lifecycle / asset inventory / AI workflow automation"
claims into running code, and shows you eliminate toil instead of clicking
through spreadsheets.

## Skills demonstrated

`Python` *(or PowerShell)* · `Automation` · `Data analysis` · `Reporting` · `Endpoint/Asset management`
