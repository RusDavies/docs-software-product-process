# Observability and Debuggability Plan

## Scope

Product/component/feature:

Environments covered:

Owner:

Operator/support path:

## Operator Questions

List the questions an operator or incident team must answer quickly.

- Is the system healthy?
- Who or what is affected?
- When did the problem start?
- What changed recently?
- What is safe to do next?

## Critical Journeys

| Journey / Workflow | Success Signal | Failure Symptoms | User/Customer Impact | Diagnostic Evidence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Failure Modes

| Failure Mode | Detection Signal | Likely Cause | First Check | Safe Action | Escalation |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Logs and Diagnostic Events

Define required structured log/event fields.

Required fields:

- timestamp
- service/component
- environment
- version/build
- request/job/workflow/correlation ID
- actor type
- action/operation
- outcome/status
- stable error code/category
- dependency/result where relevant
- duration/retry count where relevant

Sensitive fields that must not be logged:

- 

Redaction/tokenization rules:

- 

## Metrics

| Metric | Purpose | Dimensions / Labels | Threshold / SLO | Dashboard / Query |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Include health, latency, error rate, throughput, queue/job state, dependency health, resource saturation, data freshness, and product/business guardrails where relevant.

## Tracing and Correlation

Correlation identifiers:

- request ID:
- trace ID:
- job/workflow ID:
- tenant/customer/user/resource IDs, if safe:

Propagation rules:

- 

Async/queue/job correlation:

- 

Support ticket / incident linkage:

- 

## Audit Events

| Event | Actor | Trigger | Required Fields | Retention | Review Path |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Cover privileged, destructive, external-facing, privacy-sensitive, approval, security, support, automation, and AI-agent actions where relevant.

## Dashboards and Status Views

| View | Audience | Questions Answered | Source Signals | Link / Location |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Alerts and Runbooks

| Alert | Condition | Severity | Route | Runbook | Evidence to Preserve | Escalation |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Dependency Visibility

| Dependency | Health Signal | Failure Symptoms | Timeout / Retry / Fallback | Quota / Rate Limit Signal | Manual Disable / Override |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Incident Evidence

Preserve during incidents:

- logs/traces/metrics time window:
- dashboards or query snapshots:
- deployment/config/feature-flag history:
- audit records:
- affected users/tenants/resources:
- dependency status evidence:
- timeline and decision log:

Retention/access controls:

- 

## Privacy and Security Boundaries

Diagnostic data allowed:

- 

Diagnostic data prohibited:

- 

Access controls:

- 

Retention/deletion:

- 

Support/debug capture approval process:

- 

## QA / Release Checks

- [ ] Critical journeys emit expected logs/events/metrics.
- [ ] Failure modes are diagnosable using documented signals.
- [ ] Correlation IDs propagate across relevant components/jobs.
- [ ] Sensitive data is redacted or excluded from logs/traces/events.
- [ ] Audit events exist for meaningful privileged/risky actions.
- [ ] Dashboards/status checks answer operator questions.
- [ ] Alerts are actionable and linked to runbooks.
- [ ] Incident evidence capture path is documented.
- [ ] Known observability gaps are tracked as risks or backlog items.

## Open Gaps / Backlog

| Gap | Impact | Owner | Target |
| --- | --- | --- | --- |
|  |  |  |  |
