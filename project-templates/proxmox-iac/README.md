# Proxmox IaC — Infrastructure as Code

> **Growth project.** Not tied to a current card — this is the level-up that
> separates a *support* engineer from an *infrastructure* engineer, and the
> single skill most conspicuously missing from the portfolio today.

## Goal

Make the `proxmox-homelab` reproducible **from code** — so the whole lab can be
rebuilt with one command instead of click-ops.

## Option A — Terraform (declarative provisioning)

Use the Proxmox provider (or AWS free tier if you want a cloud story to pair
with the AWS cert) to define VMs/containers/network as code.

```hcl
# example skeleton — fill in
resource "proxmox_vm_qemu" "lab" {
  name        = "lab-web-01"
  target_node = "[node]"
  # ...
}
```

## Option B — Ansible (configuration management)

Playbooks that configure the homelab VMs after provisioning:
- [ ] Join AD domain
- [ ] Harden SSH / baseline
- [ ] Install agents / packages
- [ ] Apply firewall rules

```yaml
# playbook.yml — fill in
- hosts: lab
  roles: [ baseline, hardening ]
```

> Ideally do a lightweight version of **both** so you can speak to declarative
> cloud *and* on-prem automation.

## Skills demonstrated

`Terraform` · `Ansible` · `IaC` · `Automation` · `Linux`
