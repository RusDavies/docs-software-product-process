# Release Guidance

Release guidance defines how to ship deliberately instead of yeeting code into production and hoping the gods of DNS are merciful.

## Purpose

Every release should define:

- release scope
- deployment steps
- configuration changes
- verification steps
- rollback/disable plan
- monitoring
- support path
- post-launch review

## Minimum Expectations

At minimum, capture:

1. Release scope
2. Deployment checklist
3. Migration/config notes
4. Verification checks
5. Rollback/disable plan
6. Monitoring/support plan
7. Release approval

## Full Release Checklist

### 1. Release Scope

Capture:

- features/fixes included
- excluded/deferred items
- affected users
- affected systems
- known limitations
- migration impact

### 2. Pre-Release Readiness

Confirm:

- requirements met
- QA complete
- UX review complete where relevant
- security gate complete
- docs updated
- support path ready

### 3. Deployment Plan

Capture:

- deployment steps
- owners
- timing
- environment/config changes
- database migrations
- feature flags
- dependencies

### 4. Rollback and Disable Plan

Capture:

- rollback steps
- feature disable steps
- data rollback limits
- restore process
- decision threshold for rollback
- owner/approver

### 5. Release Verification

Verify:

- service health
- core workflows
- logs/metrics
- background jobs
- integrations
- permissions
- security-sensitive actions

### 6. Monitoring and Support

Capture:

- dashboards/checks
- alerts
- support contact/path
- known troubleshooting steps
- user communication where relevant

### 7. Release Notes

Include:

- what changed
- user impact
- admin/operator impact
- known limitations
- required actions
- security/privacy notes where relevant

### 8. Post-Launch Review

Schedule review of:

- incidents
- bugs
- user feedback
- metrics
- support requests
- operational toil
- security findings

## Lightweight Project Version

For small projects:

1. Release note
2. Deploy steps
3. Smoke test checklist
4. Rollback note
5. Post-launch follow-up note

## Recommended Project Files

- `docs/release/release-plan.md`
- `docs/release/deployment-checklist.md`
- `docs/release/rollback-plan.md`
- `docs/release/release-notes.md`
- `docs/release/post-launch-review.md`

## Definition of Release-Ready

A release is ready when:

- required gates are complete
- deployment steps are known
- rollback/disable path exists
- monitoring/support are ready
- risks are accepted
- approval is recorded

## Definition of Release-Done

A release is done when:

- deployment completed
- verification passed
- monitoring is healthy
- release notes are available where needed
- follow-up issues are tracked
- post-launch review is scheduled or complete
