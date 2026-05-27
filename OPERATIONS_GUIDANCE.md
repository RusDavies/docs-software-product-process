# Operations Guidance

Operations guidance defines how a product behaves after launch, when users and entropy both become stakeholders.

## Purpose

Every operated product should define:

- ownership
- monitoring
- alerting
- automation
- backups and recovery
- maintenance
- vulnerability handling
- incident response
- post-launch iteration

## Operating Ideal

The ideal state is that the system mostly looks after itself. Routine monitoring, maintenance, recovery, reporting, and housekeeping should be automated. Human intervention should be exceptional: approvals, ambiguous decisions, incidents, major changes, product direction, and risk acceptance.

A useful test: could one competent person operate 50 projects like this?

## Minimum Expectations

At minimum, capture:

1. Owner/operator
2. Health checks
3. Monitoring/logging
4. Alerting rules
5. Backup/restore expectations
6. Maintenance tasks
7. Vulnerability update process
8. Incident path
9. Automation opportunities

## Full Operations Checklist

### 1. Ownership and Support Model

Capture:

- product owner
- technical owner
- operator
- support path
- escalation path
- approval boundaries

### 2. Monitoring and Observability

Capture:

- health checks
- readiness checks
- logs
- metrics
- traces where useful
- audit events
- dashboards/status pages

### 3. Alerting

Alerts should be actionable. Noise is just denial-of-service with a ringtone.

Capture:

- alert conditions
- severity levels
- routing
- expected response
- suppression rules
- escalation thresholds

### 4. Operational Automation

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

### 5. Safe Automation Boundaries

Define:

- what automation can do without approval
- what needs human approval
- what must never be automated
- required audit logs
- rollback/undo options
- least-privilege credentials

### 6. Backups and Recovery

Capture:

- what is backed up
- backup frequency
- retention
- restore procedure
- restore testing schedule
- recovery time/recovery point expectations where relevant

### 7. Maintenance

Capture:

- dependency update cadence
- platform patching
- data retention jobs
- housekeeping tasks
- access reviews
- certificate/domain renewals
- documentation reviews

### 8. Vulnerability and Security Operations

Capture:

- vulnerability intake path
- dependency monitoring
- severity triage
- patch expectations
- incident criteria
- audit review cadence
- abuse monitoring

### 9. Incident Response

Capture:

- incident triggers
- roles/responsibilities
- first-response checklist
- communication path
- containment steps
- evidence preservation
- recovery steps
- post-incident review

### 10. Post-Launch Feedback and Iteration

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
2. Health check/logging note
3. Backup note
4. Maintenance checklist
5. Incident contact/path
6. Automation wishlist

## Recommended Project Files

- `docs/operations/runbook.md`
- `docs/operations/monitoring.md`
- `docs/operations/alerts.md`
- `docs/operations/backup-restore.md`
- `docs/operations/maintenance.md`
- `docs/operations/vulnerability-management.md`
- `docs/operations/incident-response.md`
- `docs/operations/automation.md`
- `docs/operations/post-launch-review.md`

## Definition of Operations-Ready

A product is operations-ready when:

- ownership is clear
- health/monitoring exists
- alerts are actionable
- backups/recovery are defined where relevant
- routine automation is planned or implemented
- incident path exists
- maintenance responsibilities are known

## Definition of Operations-Done

Operations is never truly done, because entropy has tenure. For a release, operations is done when:

- monitoring and alerts are live
- routine tasks are automated or scheduled
- runbooks exist
- maintenance/security review cadence is defined
- post-launch findings are added to the backlog
