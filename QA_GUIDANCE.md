# QA Guidance

QA verifies that the product works, fails acceptably, and does not quietly betray everyone involved.

## Purpose

Every project should verify:

- functional behavior
- UX behavior
- accessibility
- security controls
- integrations
- data behavior
- performance where relevant
- operational readiness

## Minimum Expectations

At minimum, capture:

1. Test plan/checklist
2. Functional verification
3. Security verification
4. UX/accessibility verification
5. Regression checks
6. Known issues
7. Approval or accepted-risk note

## Full QA Checklist

### 1. Functional QA

Verify:

- core workflows
- edge cases
- validation rules
- errors and recovery
- notifications
- integrations
- admin actions
- destructive actions

### 2. UX QA

Verify:

- layout fidelity
- navigation
- content clarity
- empty/loading/error/success states
- responsive behavior
- role/permission states
- trust UX for risky or automated actions

### 3. Accessibility QA

Verify:

- keyboard navigation
- focus order
- screen reader labels where relevant
- contrast
- form labels/errors
- reduced motion behavior
- zoom/reflow
- touch targets

### 4. Security QA

Verify:

- authentication boundaries
- authorization boundaries
- role restrictions
- input validation
- injection risks
- sensitive logging
- destructive action safeguards
- audit events
- dependency vulnerability posture
- secrets/config handling

### 5. Privacy QA

Verify:

- data minimization
- retention behavior
- export/delete behavior where relevant
- analytics/logging redaction
- third-party sharing assumptions

### 6. Integration and Regression QA

Verify:

- external dependencies
- API contracts
- migration behavior
- backwards compatibility
- fixed bugs stay fixed, because apparently we have to say that

### 7. Performance and Reliability QA

Verify where relevant:

- response times
- throughput
- concurrency
- timeout behavior
- retry/backoff behavior
- resource usage
- failure under dependency outage

### 8. Operational QA

Verify:

- health checks
- logs/metrics
- alerts
- backups
- restore process
- scheduled jobs
- runbook accuracy
- self-healing behavior where implemented

## Lightweight Project Version

For small projects:

1. Manual workflow checklist
2. Automated tests where practical
3. Security smoke checks
4. Accessibility basics
5. Operational smoke checks
6. Known issues list

## Recommended Project Files

- `docs/qa/test-plan.md`
- `docs/qa/manual-test-checklist.md`
- `docs/qa/security-test-results.md`
- `docs/qa/accessibility-checks.md`
- `docs/qa/release-qa-report.md`

## Definition of QA-Ready

QA is ready when:

- acceptance criteria exist
- test data/environment exists
- security/UX/operations checks are known
- risks and edge cases are identified

## Definition of QA-Done

QA is done when:

- required checks pass or exceptions are approved
- known issues are documented
- release blockers are resolved
- evidence is recorded
- follow-up defects are added to backlog
