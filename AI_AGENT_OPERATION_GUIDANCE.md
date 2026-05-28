# AI-Agent Operation Guidance

AI-agent operation guidance defines how approved agents may inspect, diagnose, document, maintain, or remediate a product without becoming an unsupervised chaos raccoon with API keys.

## Purpose

Products that may be operated with AI-agent assistance should define:

- approved agent roles
- allowed and forbidden actions
- read-only versus write-capable interfaces
- least-privilege credentials and tool scopes
- human approval gates
- audit and evidence requirements
- safe rollback/undo paths
- sensitive-data exposure limits
- runbooks and interfaces designed for agent use

The goal is not to let agents “do everything”. The goal is to make routine operation legible, bounded, auditable, and safe enough that agents can help without bypassing human judgment.

## Minimum Expectations

At minimum, capture:

1. Whether AI agents may operate the product at all
2. Approved agent roles and owners
3. Read-only inspection paths
4. Write-capable actions, if any
5. Human approval requirements
6. Forbidden actions
7. Audit logging expectations
8. Rollback/undo expectations
9. Sensitive-data handling boundaries

## Full AI-Agent Operation Checklist

### 1. Agent Roles and Responsibility Model

Capture:

- approved agent identities or classes
- human owner/sponsor for agent operation
- operational tasks agents may assist
- escalation path to humans
- responsibility boundary between agent recommendation and human decision

### 2. Read-Only Operation Interfaces

Prefer safe inspection first.

Capture:

- dashboards and status pages
- logs, metrics, traces, and audit events
- health check endpoints
- dependency/security scan reports
- documentation and runbook locations
- issue/backlog/ticket access
- privacy-safe diagnostic views

### 3. Write-Capable Operation Interfaces

If agents may act, define exactly how.

Capture:

- approved APIs, CLIs, admin screens, deployment tools, or automation jobs
- scoped credentials and permissions
- rate limits and blast-radius controls
- dry-run/preview modes
- confirmation and approval mechanisms
- transaction IDs, change records, and evidence capture

### 4. Human Approval Gates

Require explicit human approval for actions that are:

- external-facing
- destructive or irreversible
- privacy-sensitive
- financially material
- privilege-changing
- production-impacting
- security-risk-accepting
- public-communication or customer-impacting

Approval records should include who approved, what was approved, when, why, and the exact action boundary. Yes, boring. Also yes, useful.

### 5. Forbidden Actions and No-Go Zones

Define what agents must not do, such as:

- bypass approval gates
- access unrelated private data
- exfiltrate secrets or sensitive data
- change identity/access policy without approval
- delete production data without a tested recovery path and approval
- post public/customer communications unless explicitly authorized
- self-expand privileges or tool access

### 6. Audit, Logging, and Evidence

Capture:

- how agent actions are identified in logs
- where observations, recommendations, approvals, and actions are recorded
- required before/after evidence
- retention expectations
- incident-review use of agent logs
- release/change-record linkage

### 7. Rollback, Recovery, and Containment

Capture:

- undo path for each write-capable action
- kill switch or access revocation path
- failed-action handling
- rollback authority
- safe retry policy
- incident containment steps for agent-caused problems

### 8. Agent-Readable Runbooks and Product Surfaces

Design operational surfaces to be usable by humans and agents:

- stable command/API names
- structured status outputs
- documented error messages
- machine-readable health and version endpoints where useful
- runbooks with prerequisites, commands, expected outputs, rollback, and escalation
- clear separation between inspect, plan, approve, execute, and verify

### 9. Security and Privacy Boundaries

Capture:

- data classes agents may view
- redaction requirements
- prompt/logging restrictions
- secret-handling rules
- tenant/customer boundary controls
- model/provider constraints where relevant
- compliance constraints on agent access

## Lightweight Project Version

For small projects:

1. State whether agents may help operate it
2. List allowed read-only checks
3. List any allowed write actions
4. Mark actions needing human approval
5. Document the log/evidence path
6. Document rollback or “do not automate” where rollback is weak

## Recommended Project Files

- `docs/operations/agent-operation-boundaries.md`
- `docs/architecture/agent-operation.md`
- `docs/operations/runbook.md`
- `docs/security/access-review.md`
- `docs/operations/automation.md`

## Definition of Agent-Operation-Ready

A product is agent-operation-ready when:

- approved agent roles and boundaries are documented
- read-only inspection paths are available
- write-capable actions are least-privilege and approval-gated where risky
- audit logs can distinguish agent actions
- rollback/undo paths exist for permitted changes
- forbidden actions and sensitive-data boundaries are explicit

## Definition of Agent-Operation-Done

For a release, agent-operation work is done when:

- runbooks and operational interfaces match the documented boundaries
- credentials/tool scopes are configured as documented
- approval and audit paths have been tested or directly inspected
- any unsafe or unresolved agent-operation gaps are tracked in the backlog
