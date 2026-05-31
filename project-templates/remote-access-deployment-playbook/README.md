# Remote Access Deployment Playbook

> Companion write-up for the portfolio's *Company-Wide Remote Access Deployment*
> card. This work can't be rebuilt in a homelab, so it becomes a **generalised,
> sanitised runbook** that shows the planning and judgment behind the rollout.
> Writing-only — no lab needed (~1 evening).

## Scenario

Rolling out a remote-support tool (e.g. Splashtop) across an organisation of
~70 endpoints spanning HQ + remote sites, to cut response time and remove
on-site visits for routine fixes. *(No employer/vendor-internal names, IPs, or
real counts beyond what's already public on the CV.)*

## Playbook

### 1. Enrolment workflow
`[How devices get enrolled — agent install, grouping, naming convention]`

### 2. Access-policy design
`[Role-based access: who can reach what; technician vs. admin scopes]`

### 3. Security hardening
- MFA enforced
- Session logging / recording
- Idle timeout + auto-disconnect
- `[other controls]`

### 4. Rollout & training
`[Phased enrolment by department; short enablement sessions; comms plan]`

### 5. Rollback / fallback plan
`[What happens if enrolment fails or a policy is wrong]`

## Diagram

![Deployment flow](docs/deployment-flow.png) <!-- [generic flow: request → enrol → policy → train] -->

## Outcome (sanitised)

- ~70 endpoints secured; routine on-site visits eliminated
- `[add response-time delta if shareable]`

## Lessons learned

`[e.g. phased enrolment reduced disruption; least-privilege policy mapping up front]`

## Skills demonstrated

`Remote Access` · `Deployment planning` · `Access policy / MFA` · `IT operations` · `Documentation`
