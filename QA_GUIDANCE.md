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
- project knowledge accuracy and source grounding where a knowledge base exists

## Minimum Expectations

At minimum, capture:

1. Test plan/checklist
2. Functional verification
3. Security verification
4. UX/accessibility verification
5. Regression checks
6. Known issues
7. Project knowledge lint/review where applicable
8. Approval or accepted-risk note

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
- logs/metrics/traces/audit events
- failure diagnosability from documented signals
- alerts
- backups
- restore process
- scheduled jobs
- runbook accuracy
- self-healing behavior where implemented

### 9. Documentation QA

Verify:

- required user/admin/operator docs exist
- quick-start/setup steps work
- configuration guidance matches reality
- troubleshooting and recovery guidance is accurate
- release notes match the release
- links, examples, and screenshots are current where used
- security/privacy/compliance claims are accurate and approved

Guidance: [`DOCUMENTATION_GUIDANCE.md`](https://github.com/RusDavies/docs-software-product-process/blob/main/DOCUMENTATION_GUIDANCE.md)

### 10. Project Knowledge QA, Where Applicable

For projects with a `docs/knowledge/` base or equivalent LLM wiki-style context, verify:

- important claims link to sources or approved project artifacts
- generated summaries are marked draft or reviewed
- source manifest entries are sufficient to find the source again
- project knowledge does not contradict requirements, architecture, runbooks, decisions, or backlog items
- project knowledge does not replace approved specs, risk acceptances, release approvals, or QA evidence
- raw sources, caches, generated indexes, embeddings, and temporary outputs follow version-control and ignore rules
- secrets, sensitive data, and copyrighted external sources have not been committed improperly
- knowledge gaps or stale context risks are added to the backlog

Guidance: [`PROJECT_KNOWLEDGE_GUIDANCE.md`](https://github.com/RusDavies/docs-software-product-process/blob/main/PROJECT_KNOWLEDGE_GUIDANCE.md)

### 11. SEO QA, Where Applicable

For public web projects, verify:

- intended pages are indexable
- private/staging pages are not indexable
- title/meta/canonical tags are correct
- Open Graph/share previews work
- sitemap and robots.txt are correct
- structured data validates where used
- semantic HTML and headings are sensible
- mobile rendering works
- performance/Core Web Vitals checks pass or exceptions are approved

Guidance: [`SEO_GUIDANCE.md`](https://github.com/RusDavies/docs-software-product-process/blob/main/SEO_GUIDANCE.md)

## Lightweight Project Version

For small projects:

1. Manual workflow checklist
2. Automated tests where practical
3. Security smoke checks
4. Accessibility basics
5. Operational smoke checks
6. Documentation smoke check
7. Project knowledge smoke check where a knowledge base exists
8. SEO smoke check for public web projects
9. Known issues list

## Recommended Project Files

- `docs/qa/test-plan.md`
- `docs/qa/manual-test-checklist.md`
- `docs/qa/security-test-results.md`
- `docs/qa/accessibility-checks.md`
- `docs/qa/release-qa-report.md`
- `docs/documentation/documentation-qa-checklist.md`
- `docs/knowledge/project-knowledge-lint-checklist.md`
- `docs/seo/launch-seo-checklist.md`

## Definition of QA-Ready

QA is ready when:

- acceptance criteria exist
- test data/environment exists
- security/UX/operations/documentation/SEO checks are known
- project knowledge checks are known where a knowledge base exists
- risks and edge cases are identified

## Definition of QA-Done

QA is done when:

- required checks pass or exceptions are approved
- required documentation has been checked or exceptions are approved
- project knowledge has been checked or exceptions are approved where applicable
- SEO checks have passed or exceptions are approved where applicable
- known issues are documented
- release blockers are resolved
- evidence is recorded
- follow-up defects are added to backlog
