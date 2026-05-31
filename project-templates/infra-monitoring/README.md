# Infra Monitoring — Prometheus + Grafana

> **Growth project, and your differentiator.** Almost no junior infra candidate
> pairs observability with *genuine* data-viz skill — you do. This is where the
> "analytics lens on infra reliability" stops being a tagline and becomes proof.

## Goal

Monitor the homelab (Proxmox nodes, VMs, network) and turn metrics into
dashboards + alerts + a short written analysis of what the data revealed.

## Stack

- **Prometheus** — scrape metrics
- **node_exporter** / **pve-exporter** — host + Proxmox metrics
- **Blackbox / Uptime Kuma** — uptime probes
- **Grafana** — dashboards (export JSON into `/dashboards`)

## What to publish

- [ ] Grafana dashboard screenshots (`/docs`)
- [ ] Exported dashboard JSON (`/dashboards`)
- [ ] Alert rules (e.g. node down, disk > 85%, backup job failed)
- [ ] A short **write-up**: what a metric/alert caught (capacity trend, a
      near-miss) — this is the analytics story

## Bonus (plays to your strengths)

A small Python script that pulls metrics and produces a **weekly reliability
report** (reuses your Pandas / Power BI muscle).

## Lessons learned

`[e.g. alert on symptoms not causes; what a good SLO looked like for the lab]`

## Skills demonstrated

`Prometheus` · `Grafana` · `Observability` · `Linux` · `Python` · `Data visualisation`
