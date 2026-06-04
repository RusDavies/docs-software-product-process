# Operations Guidance

Operations guidance defines how a product behaves after launch, when users and entropy both become stakeholders.

## Purpose

Every operated product should define:

- ownership
- product operational estate management
- monitoring
- alerting
- automation
- AI-agent operational boundaries unless explicitly throw-away or product-owner exempted
- backups and recovery
- maintenance
- vulnerability handling
- incident response
- post-launch iteration

Pure software libraries/packages are not operated products just because they are maintained. They need maintainer ownership, vulnerability intake, release integrity, compatibility testing, and security patching, but they do not need runtime operations runbooks, monitoring, alerting, backup/restore plans, or incident operations unless they also ship an operated service, daemon, scheduled job, data store, telemetry backend, update service, or similar runtime component.

## Operating Ideal

The ideal state is that the system mostly looks after itself. Routine monitoring, maintenance, recovery, reporting, and housekeeping should be automated. Human intervention should be exceptional: approvals, ambiguous decisions, incidents, major changes, product direction, and risk acceptance.

A useful test: could one competent person operate 50 projects like this?

## Minimum Expectations

At minimum, capture:

1. Owner/operator
2. Product operational estate register
3. Health checks
4. Monitoring, observability, and debuggability
5. Alerting rules
6. Backup/restore expectations
7. Maintenance tasks
8. Vulnerability update process
9. Incident path
10. Automation and AI-agent operation opportunities

## Full Operations Checklist

### 1. Ownership and Support Model

Capture:

- product owner
- technical owner
- operator
- support path
- escalation path
- approval boundaries

### 2. Product Operational Estate Management

Capture and maintain the estate the product depends on, because “where is that hosted?” should not become a séance.

Capture:

- domains, DNS records, certificates, and renewal dates
- repositories, package registries, artifact stores, and release accounts
- cloud accounts, SaaS tenants, identity providers, and admin consoles
- environments, deployment targets, and infrastructure owners
- secrets, keys, service accounts, and credential owners
- databases, object stores, backup locations, and retention/deletion responsibilities
- third-party services, billing owners, contracts, and support contacts
- access review cadence and offboarding/handover process
- decommissioning checklist for retired services

### 3. Monitoring, Observability, and Debuggability

Use `OBSERVABILITY_DEBUGGABILITY_GUIDANCE.md` for detailed operator visibility and failure-investigation design. Capture:

- health checks
- readiness checks
- critical journeys and failure modes
- logs and diagnostic events
- metrics
- traces/correlation where useful
- audit events
- dashboards/status pages and diagnostic views
- dependency, queue, job, and data-freshness visibility
- incident evidence capture expectations
- privacy-safe diagnostics and redaction rules

### 4. Alerting

Alerts should be actionable. Noise is just denial-of-service with a ringtone.

Capture:

- alert conditions
- severity levels
- routing
- expected response
- suppression rules
- escalation thresholds

### 5. Operational Automation

Automate routine work:

- backups
- restore validation
- cleanup/retention
- dependency checks
- certificate renewal
- scheduled reports
- queue replays where safe
- self-healing restarts/retries
- access review reminders
- vulnerability intake reminders

### 6. Safe Automation and AI-Agent Boundaries

Define:

- what automation can do without approval
- what needs human approval
- what must never be automated
- required audit logs
- rollback/undo options
- least-privilege credentials
- which approved AI agents, if any, may inspect, diagnose, document, maintain, or remediate
- which interfaces agents should use, such as dashboards, APIs, CLIs, runbooks, ticketing, or deployment tools
- which agent actions are read-only, write-capable, external-facing, destructive, privacy-sensitive, or irreversible
- how human approvals are captured before risky agent actions
- how agent actions are identified in logs, audit trails, tickets, and release records
- how agent access is reviewed, revoked, and rotated

### 7. Backups and Recovery

Capture:

- what is backed up
- backup frequency
- retention
- restore procedure
- restore testing schedule
- recovery time/recovery point expectations where relevant

### 8. Maintenance

Capture:

- dependency update cadence
- platform patching
- data retention jobs
- housekeeping tasks
- access reviews
- certificate/domain renewals
- documentation reviews

### 9. Vulnerability and Security Operations

Capture:

- vulnerability intake path
- dependency monitoring
- severity triage
- patch expectations
- incident criteria
- audit review cadence
- abuse monitoring

### 10. Incident Response

Capture:

- incident triggers
- roles/responsibilities
- first-response checklist
- communication path
- containment steps
- evidence preservation
- recovery steps
- post-incident review

### 11. Post-Launch Feedback and Iteration

Review:

- usage metrics
- support requests
- incidents
- operational toil
- failed automations
- user feedback
- security findings
- cost/resource usage

Turn findings into backlog items.

## Lightweight Project Version

For small projects:

1. Owner/support note
2. Digital estate note
3. Health check/logging note
4. Backup note
5. Maintenance checklist
6. Incident contact/path
7. Automation/agent-operation wishlist

## Recommended Project Files

- `docs/operations/runbook.md`
- `docs/operations/digital-estate-register.md`
- `docs/operations/monitoring.md`
- `docs/operations/observability.md`
- `docs/operations/debugging-guide.md`
- `docs/operations/alerts.md`
- `docs/operations/backup-restore.md`
- `docs/operations/maintenance.md`
- `docs/operations/vulnerability-management.md`
- `docs/operations/incident-response.md`
- `docs/operations/automation.md`
- `docs/operations/agent-operation-boundaries.md`
- `docs/operations/post-launch-review.md`

## Definition of Operations-Ready

A product is operations-ready when:

- ownership is clear
- product operational estate inventory is maintained enough to operate, renew, transfer, or decommission the product
- health/monitoring exists
- operators can debug and scope important failures from documented signals
- alerts are actionable
- backups/recovery are defined where relevant
- routine automation is planned or implemented
- AI-agent operation boundaries are documented unless explicitly throw-away or product-owner exempted
- incident path exists
- maintenance responsibilities are known

## Definition of Operations-Done

Operations is never truly done, because entropy has tenure. For a release, operations is done when:

- monitoring, diagnostic views, and alerts are live
- estate ownership, renewals, access, and critical dependencies are known
- routine tasks are automated or scheduled
- agent-accessible operational paths are least-privilege, auditable, and approval-gated where risky
- runbooks exist
- maintenance/security review cadence is defined
- post-launch findings are added to the backlog
