# Architecture Guidance

Architecture defines the system shape before implementation gives every bad assumption a mortgage.

## Purpose

Every serious project should define:

- system boundaries
- components and responsibilities
- data model
- APIs/contracts
- deployment/runtime model
- product operational estate footprint
- web crawl/index/metadata architecture where applicable
- security/trust boundaries
- observability and operations model
- approved AI-agent operational interfaces unless explicitly throw-away or product-owner exempted
- failure/recovery behavior

## Minimum Expectations

At minimum, capture:

1. System overview
2. Component diagram or written equivalent
3. Data model
4. API/integration model
5. Deployment model
6. Product operational estate footprint
7. Trust boundaries and access model
8. Observability/operations model
9. AI-agent operation model unless explicitly throw-away or product-owner exempted
10. Key tradeoffs and risks

## Full Architecture Checklist

### 1. System Overview

Capture:

- purpose
- scope
- major components
- external dependencies
- users/systems interacting with it
- important constraints

### 2. Component and Service Boundaries

Capture:

- components/services
- responsibilities
- interfaces
- ownership
- scaling assumptions
- statefulness/statelessness

### 3. Data Architecture

Capture:

- data entities
- storage systems
- relationships
- migrations
- retention
- backup/restore
- data classification

### 4. API and Contract Design

Capture:

- API boundaries
- request/response contracts
- authentication/authorization
- versioning
- error handling
- rate limits
- idempotency where useful

### 5. Runtime and Deployment Model

Capture:

- target runtime
- container/runtime assumptions, Podman-friendly by default
- configuration model
- environment separation
- build/release/run separation where appropriate
- sitemap/robots/canonical generation for public web projects
- infrastructure dependencies

### 6. Product Operational Estate Architecture

Capture:

- domains, DNS zones, and certificate dependencies
- source repositories, package registries, artifact stores, and release accounts
- cloud accounts, SaaS tenants, identity providers, and administrative consoles
- environments, deployment targets, and infrastructure ownership
- external dependencies, service accounts, billing owners, and renewal obligations
- data stores, backup destinations, retention locations, and deletion/decommissioning paths
- ownership and handover model for each estate component

### 7. Security Architecture

Capture:

- trust boundaries
- network boundaries
- authn/authz flow
- service-to-service access
- secrets handling
- privileged actions
- audit points
- abuse mitigations

### 8. Operational Automation Architecture

Capture:

- health checks
- self-healing behaviors
- scheduled jobs
- backup automation
- dependency/security checks
- routine reports
- alert routing
- human approval boundaries

### 9. AI-Agent Operation Architecture, Where Applicable

Capture:

- approved agent roles and autonomy boundaries
- read-only diagnostic interfaces
- write-capable maintenance interfaces, if any
- human approval gates for risky, external, destructive, privacy-sensitive, or irreversible actions
- least-privilege credentials and scoped tool access for agents
- agent-visible runbooks, status pages, APIs, CLIs, logs, and dashboards
- audit trail for agent observations, recommendations, approvals, and actions
- rollback/undo paths for agent-performed changes
- explicit no-go zones for agent access or automation

### 10. Observability Architecture

Capture:

- logs
- metrics
- search/index/performance monitoring for public web projects
- traces where useful
- audit events
- dashboards/status checks
- alert conditions
- privacy-safe diagnostics

### 11. Resilience and Failure Modes

Capture:

- dependency failures
- partial failures
- retry/backoff behavior
- data consistency risks
- rollback/disable paths
- disaster recovery expectations

### 12. Tradeoffs and Alternatives

Capture:

- options considered
- selected approach
- why it was selected
- rejected alternatives
- known limitations
- future migration paths

## Lightweight Project Version

For small projects:

1. One-page architecture sketch
2. Data model notes
3. API/integration notes
4. Security boundary notes
5. Product operational estate notes
6. Deployment/config notes
7. Monitoring/backup notes
8. Agent-operation boundary notes if agents will help operate the project

## Recommended Project Files

- `docs/architecture/overview.md`
- `docs/architecture/components.md`
- `docs/architecture/data-model.md`
- `docs/architecture/api-contracts.md`
- `docs/architecture/deployment.md`
- `docs/architecture/digital-estate.md`
- `docs/architecture/security-architecture.md`
- `docs/architecture/agent-operation.md`
- `docs/architecture/observability.md`
- `docs/architecture/operational-automation.md`
- `docs/architecture/decision-records/`

## Definition of Architecture-Ready

Architecture is ready when:

- major components and boundaries are clear
- data and API models are plausible
- deployment/runtime assumptions are documented
- product operational estate ownership and dependencies are documented
- security and trust boundaries are visible
- agent-operation boundaries are documented where applicable
- operational automation and observability are planned
- major tradeoffs are understood

## Definition of Architecture-Done

Architecture is done when:

- implementation matches the approved architecture or deviations are documented
- decisions are recorded
- operational and security concerns are represented in the shipped system
- new architecture debt is tracked in the backlog
