# Observability and Debuggability Guidance

Observability is not just graphs for people who enjoy dashboards. It is the product's ability to explain what happened, what is happening, why it is failing, who or what was affected, and what an operator can safely do next.

Debuggability is the design discipline that makes failures investigable without heroic SSH archaeology, accidental privacy leaks, or one exhausted incident lead reading tea leaves in log fragments.

## Purpose

This guidance applies when a product, service, job, workflow, API, integration, data pipeline, AI system, or user-facing feature may need to be operated, supported, investigated, or defended after release.

It covers:

- operator and incident-team visibility
- failure investigation and reconstruction
- logs, metrics, traces, events, and audit records
- correlation across components and dependencies
- dashboards, status views, and diagnostic interfaces
- privacy-safe diagnostic data
- alert-to-runbook-to-evidence flow
- observability QA and release readiness

## When This Applies

Use this guidance for:

- operated services, SaaS products, public websites, APIs, scheduled jobs, daemons, and data pipelines
- products with external dependencies, queues, background jobs, payments, identity, user data, regulated data, AI agents, AI model calls, or administrative workflows
- enterprise-targeted products where support, auditability, compliance evidence, or customer incident questions matter
- software libraries/packages only when they also ship an operated runtime component, telemetry backend, update service, hosted documentation/search service, or similar live system

For throw-away work, keep only a minimal diagnostic note: how to tell whether the experiment ran, failed, or should be deleted.

## Minimum Expectations

At minimum, define:

1. critical user journeys and operator-visible health signals
2. major failure modes and symptoms
3. logs/events needed to reconstruct important flows
4. metrics for health, capacity, latency, error rate, and key business/system outcomes
5. trace/correlation strategy where requests or jobs cross components
6. audit events for meaningful user, admin, security, automation, and AI-agent actions
7. dashboards/status checks that answer operator questions
8. alert conditions linked to runbooks
9. privacy-safe logging, redaction, and retention rules
10. incident evidence capture and preservation expectations
11. observability QA checks before release

## Full Observability and Debuggability Checklist

### 1. Operator Questions

Start with the questions operators and incident teams must answer quickly:

- Is the system healthy right now?
- Which component, dependency, queue, job, tenant, user cohort, region, or feature is affected?
- When did the problem start?
- What changed recently?
- Is this a correctness, availability, latency, capacity, security, abuse, data-quality, billing, or UX problem?
- Is customer data affected?
- Is the problem spreading, stable, or recovering?
- What is safe to retry, roll back, disable, drain, replay, or escalate?
- What evidence must be preserved before remediation?

If an on-call operator cannot answer the obvious questions in minutes, the system is not observable enough. Humans are slow; do not make them also blind.

### 2. Critical Journeys and Failure Modes

Identify the flows that matter most:

- user signup/login/session lifecycle
- payment, billing, entitlement, or quota changes
- data import/export/sync
- AI/model/tool calls and automated decisions
- admin actions and privileged workflows
- background jobs, queues, and scheduled tasks
- deployment, migration, backup, restore, and rollback paths
- third-party integrations and webhooks
- security-sensitive actions such as permission changes, secret rotation, abuse controls, and account recovery

For each critical flow, define:

- normal success signal
- expected latency or completion time
- common failure symptoms
- failure cause categories
- user/customer impact
- operator-visible evidence
- safe remediation options

### 3. Structured Logs and Diagnostic Events

Logs should be structured enough to search, aggregate, and correlate.

Capture where appropriate:

- timestamp, service/component, environment, version/build, instance/container, and host/runtime identity
- request ID, trace ID, job ID, workflow ID, tenant/customer ID, user/account ID, and correlation IDs where safe
- operation/action name
- outcome/status
- error category and stable error code
- dependency name and dependency outcome
- relevant resource identifiers, redacted or tokenized where needed
- latency/duration and retry count
- feature flag/config version where relevant
- actor type: user, admin, service account, automation, AI agent, external system

Avoid:

- passwords, API keys, session tokens, private keys, recovery codes, personal secrets, raw credentials, full payment data, or unnecessary personal content
- dumping complete prompts, documents, messages, medical/legal/financial records, or customer payloads into diagnostic logs unless the product has an explicit, approved, privacy-safe debug capture design
- unstructured panic text as the only source of truth

Diagnostic logs are not a confession booth for sensitive data. Redact like you mean it.

### 4. Metrics

Define metrics that reveal health and impact:

- availability and uptime by component or endpoint
- latency percentiles for critical paths
- error rates by stable category, endpoint, dependency, tenant/cohort, and release version
- throughput, queue depth, job age, backlog, and retry/dead-letter counts
- resource saturation: CPU, memory, disk, network, file handles, database pool, cache pressure
- data freshness, sync lag, import/export completion, and reconciliation drift
- AI/model/tool-call success, latency, token/cost usage, refusal/fallback rate, and human-approval queue age where relevant
- security/abuse indicators such as failed auth, suspicious access, permission changes, rate-limit pressure, and anomaly signals
- business/product guardrails where relevant: signup failures, checkout failures, notification delivery, successful task completion

Metrics should support slicing by version, environment, dependency, feature flag, tenant/cohort, and important workflow. If every outage graph says “some errors happened somewhere,” congratulations, you have made a weather report.

### 5. Tracing and Correlation

Use traces or equivalent correlation when work crosses components, async queues, third-party calls, model/tool calls, or background jobs.

Define:

- trace/request ID propagation rules
- job/workflow correlation IDs
- parent/child relationship for async tasks
- external call spans or equivalent timing records
- retry and idempotency correlation
- redaction rules for span attributes
- how support tickets, incident records, deployment records, and audit events link back to traces/logs

The goal is to reconstruct the path of a failing request or job without guessing which of seventeen tabs contains the clue.

### 6. Audit Events

Audit events are not general debug logs. They record meaningful actions and decisions that may need review, evidence, or accountability.

Capture audit events for:

- login, logout, failed login, MFA/recovery, and session revocation where relevant
- permission, role, team, tenant, entitlement, and ownership changes
- admin actions and privileged support actions
- destructive, irreversible, external-facing, privacy-sensitive, or high-risk actions
- data export/import/delete/restore and retention overrides
- security setting changes and abuse-control actions
- approval requests, approvals, denials, risk acceptances, and overrides
- AI-agent observations, recommendations, tool calls, human approvals, actions, and rollback/undo steps where applicable

Specify retention, access control, tamper resistance, and review cadence. Audit data should help after an incident; it should not become a new incident.

### 7. Dashboards, Status Views, and Diagnostic Interfaces

Design dashboards around operator questions, not vendor-widget aesthetics.

Useful views include:

- executive/service health summary
- critical journey health
- deployment/release comparison
- dependency status and error contribution
- queue/job health
- database/cache/storage health
- tenant/customer/cohort impact view where relevant
- security/abuse watch view
- AI/model/tool-call operations view where relevant
- support/debug lookup view by request ID, job ID, user/account ID, tenant, release, or time window

Status pages and diagnostic CLIs/APIs should be read-only by default. Write-capable remediation interfaces need approval gates, least privilege, audit logs, rollback paths, and clear blast-radius controls.

### 8. Alerting and Runbook Linkage

Every alert should answer:

- What condition fired?
- Why does it matter?
- What is the likely impact?
- What dashboard or query should the responder open?
- What runbook should they follow?
- What is safe to do immediately?
- When should they escalate?
- What evidence should they preserve?

Avoid alerts that merely announce entropy. Alert on user impact, security risk, data risk, or imminent resource exhaustion. Page humans for action, not vibes.

### 9. Dependency and Integration Visibility

For each important dependency, capture:

- health/status check or external status source
- timeout, retry, backoff, circuit-breaker, and fallback behavior
- error categories and stable codes
- quota/rate-limit visibility
- webhook/event delivery status
- sync lag and reconciliation state
- customer/user impact of dependency failure
- manual override or disable path

Dependency failures should be visible as dependency failures, not as mysterious internal moral weakness.

### 10. Incident Evidence and Forensics Readiness

Define what to preserve during incidents:

- logs, traces, metrics snapshots, dashboards, and query results
- deployment, configuration, feature flag, and migration history
- audit events and approval records
- dependency status evidence
- affected users/tenants/resources and scope estimates
- timeline of detection, decisions, remediation, and communication
- suspected root cause and discarded hypotheses

Document retention windows and access controls before the incident. During the incident is traditionally a poor time to discover the logs expired yesterday.

### 11. Privacy, Security, and Compliance Boundaries

Define:

- what diagnostic data may be collected
- what must be redacted, tokenized, hashed, minimized, or excluded
- who can access diagnostic data
- how support/debug access is approved and audited
- retention/deletion schedules
- customer/regulatory commitments affecting observability data
- whether debug capture can be enabled per tenant/user/request, by whom, and for how long
- how screenshots, recordings, prompts, transcripts, payload samples, and exported evidence are handled

Observability should improve safety. If it quietly turns into surveillance or data exfiltration with nicer charts, stop.

### 12. Build and QA Expectations

Implementation should include:

- stable error codes and useful error categories
- structured logging helpers or conventions
- metric naming conventions
- trace/correlation propagation tests where relevant
- log redaction tests for sensitive flows
- health/readiness endpoint tests
- audit event tests for important actions
- dashboard/query smoke checks where possible
- incident-runbook drills for serious products

QA should verify that failure is diagnosable, not merely that the happy path smiles politely.

### 13. Release and Operations Handoff

Before launch, confirm:

- required dashboards/status checks exist
- alerts are actionable and routed
- runbooks link to the right dashboards, log queries, commands, and escalation paths
- operators know how to identify affected users, tenants, features, components, and dependencies
- sensitive diagnostic data is protected
- incident evidence capture is documented
- rollback/disable paths are observable
- post-launch review will look at real incidents, near misses, support tickets, alert noise, and operational toil

## Lightweight Project Version

For small projects:

1. health check or smoke-check command
2. where logs go and what they contain
3. top 3 likely failures and how to identify them
4. basic alert or manual check if operated
5. privacy note for diagnostic data
6. owner/escalation note

## Recommended Project Files

- `docs/architecture/observability.md`
- `docs/operations/monitoring.md`
- `docs/operations/alerts.md`
- `docs/operations/incident-response.md`
- `docs/operations/runbook.md`
- `docs/operations/debugging-guide.md`

Use [`templates/observability-debuggability-plan.md`](https://github.com/RusDavies/docs-software-product-process/blob/main/templates/observability-debuggability-plan.md) as a starter artifact.

## Definition of Observability-Ready

A product is observability-ready when:

- critical journeys and failure modes are instrumented or explicitly exempted
- logs, metrics, traces/correlation, and audit events answer real operator questions
- dashboards/status checks show health, impact, dependencies, and recent changes
- alerts are actionable and linked to runbooks
- operators can scope impact and preserve evidence during incidents
- diagnostic data respects privacy, security, and retention requirements
- QA has verified important failures are diagnosable

## Definition of Observability-Done for Release

For a release, observability is done when:

- new or changed flows have appropriate signals
- dashboards/queries/runbooks are updated
- alerts are tested or deliberately disabled with accepted rationale
- audit events and redaction tests pass where relevant
- incident evidence paths are known
- any observability gaps are tracked as release risks or backlog items

The standard is not “we have logs.” The standard is “a competent operator can understand and respond to failure without becoming part of the failure.”
