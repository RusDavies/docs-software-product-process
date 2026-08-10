# Implementation Planning Guidance

Implementation planning turns design into executable work. This is where “we should probably secure it” becomes actual backlog items instead of decorative anxiety.

## Purpose

Every project should define:

- milestones
- backlog structure
- sequencing
- dependencies
- ownership
- verification gates
- release approach
- risks and decision points

## Minimum Expectations

At minimum, capture:

1. Milestones
2. Backlog items
3. Dependencies
4. Test/verification plan
5. Security and operational tasks
6. Release plan
7. Spec / verifier / environment assumptions for agent-heavy work
8. Project knowledge tasks where durable context is needed
9. Optional high-intensity verifier modes where an artifact needs repeated critique
10. Known risks/blockers

## Full Planning Checklist

### 1. Delivery Milestones

Define meaningful milestones:

- prototype
- design approval
- architecture approval
- MVP
- internal alpha
- beta/pilot
- production release
- post-launch review

### 2. Backlog Breakdown

Each backlog item should include:

- goal
- scope
- acceptance criteria
- dependencies
- security/privacy impact
- UX impact
- test expectations
- documentation impact
- project knowledge impact where durable context, provenance, or agent environment changes

### 3. Sequencing

Plan order deliberately.

Consider:

- dependencies
- highest-risk unknowns
- security foundations
- data model foundations
- UX validation
- integration timing
- migration needs

### 4. Security and Privacy Work Items

Include normal backlog items for:

- access model
- threat model mitigations
- secrets management
- audit logging
- dependency scanning
- privacy controls
- release security review

### 5. Operational Automation Work Items

Include normal backlog items for:

- health checks
- metrics/logging/tracing/audit events
- failure-mode diagnostics
- backups
- restore checks
- housekeeping jobs
- alerting
- routine reports
- runbooks

### 6. Verification Strategy

Capture:

- unit tests
- integration tests
- end-to-end tests
- UX QA
- accessibility checks
- security checks
- performance checks
- manual review gates

### 7. Spec / Verifier / Environment Planning

For agent-heavy work, make the working model explicit:

- **Spec:** goal, acceptance criteria, constraints, approved decisions, risks, and non-goals
- **Verifier:** tests, QA checks, review gates, security checks, knowledge linting, and approval evidence
- **Environment:** repository structure, tools, runbooks, agent instructions, project knowledge base, and allowed operations

Do not let generated project knowledge become the spec. Link it to approved requirements, decision records, risks, and backlog items.

Guidance: [`PROJECT_KNOWLEDGE_GUIDANCE.md`](https://github.com/RusDavies/docs-software-product-process/blob/main/PROJECT_KNOWLEDGE_GUIDANCE.md)

### 8. Optional Gauntlet Loop Verifier Mode

Use a Gauntlet Loop only as an intensified verifier or execution tactic inside
the Spec / Verifier / Environment model. It is useful when the work produces a
concrete artifact and repeated independent critique can move it closer to a
clear quality bar.

Good candidates include:

- UI screens or flows with a reference design or acceptance criteria
- product copy, documentation, or launch content with a known audience and tone
- prototypes with a concrete behavior target
- creative assets with an accepted reference or explicit constraints
- complex implementation slices with defined tests, review checks, and stop rules

Before planning a Gauntlet Loop, capture:

- the artifact under review
- the spec and non-goals
- the independent critique method
- deterministic checks that must still pass
- human approval boundaries
- stop conditions, budget limits, and escalation triggers
- where review notes or evidence will be recorded

Do not use the loop to change scope, approval requirements, security posture,
release readiness, public claims, or accepted risks. Those stay governed by the
normal spec, decision, risk, and approval process. Otherwise the verifier starts
writing the spec, which is how you get process soup with extra confidence.

Template: [`templates/gauntlet-loop-review-log.md`](https://github.com/RusDavies/docs-software-product-process/blob/main/templates/gauntlet-loop-review-log.md)

### 9. Release Strategy

Capture:

- environments
- feature flags
- migration sequence
- rollback plan
- approval gates
- launch communication
- support expectations

### 10. Risk Register

Track:

- technical risks
- product risks
- security risks
- privacy risks
- operational risks
- schedule risks
- unresolved decisions

## Lightweight Project Version

For small projects:

1. Milestone list
2. Prioritized backlog
3. Verification checklist
4. Security/operations tasks
5. Spec/verifier/environment note for agent-heavy work
6. Optional Gauntlet Loop note if a concrete artifact needs intensified critique
7. Project knowledge note if durable context matters
8. Release note

## Recommended Project Files

- [`BACKLOG.md`](https://github.com/RusDavies/docs-software-product-process/blob/main/BACKLOG.md) or an equivalent project-specific TODO file
- `docs/knowledge/README.md`
- `docs/knowledge/sources.yml`
- `docs/planning/milestones.md`
- `docs/planning/risk-register.md`
- `docs/planning/test-strategy.md`
- `docs/planning/release-plan.md`
- `docs/qa/gauntlet-loop-review-log.md`

## Definition of Planning-Ready

Planning is ready when:

- work is broken into actionable items
- sequencing is sensible
- security, observability/debuggability, and operations are represented
- verification is planned
- any Gauntlet Loop verifier mode has a concrete artifact, quality bar, and stop rules
- spec/verifier/environment assumptions are explicit where agent-heavy work is expected
- project knowledge work is represented where durable context or source provenance matters
- risks and blockers are visible

## Definition of Planning-Done

Planning is done when:

- the team can start implementation without inventing the plan mid-flight
- major dependencies are tracked
- the relevant human approves the delivery approach
