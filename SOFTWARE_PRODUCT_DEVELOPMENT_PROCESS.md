# Software Product Development Process

This document defines the workspace baseline process for developing software products. It is intended for projects that may become real, used, operated, maintained, or exposed to other humans — an alarming number of ways for software to become inconvenient.

## Purpose

Every project should move deliberately from idea to operation:

1. Frame the product opportunity.
2. Define requirements.
3. Design the user experience.
4. Design security and privacy.
5. Design the technical architecture.
6. Plan implementation.
7. Build the product.
8. Verify quality.
9. Pass release and security gates.
10. Launch deliberately.
11. Operate and improve it.

The process is modular. Small projects can use lightweight versions. Larger, riskier, public, customer-facing, regulated, security-sensitive, or multi-role projects should use the full process.

Before applying the full process, classify the project with `TAILORING_GUIDE.md`. Use `GOVERNANCE_AND_APPROVALS.md` when approvals, accepted risk, release authority, or agent autonomy boundaries matter.

## Process Principles

All phases should apply `ENGINEERING_PRINCIPLES.md`. Project teams may tailor or deviate from principles, but deviations should be explicit and justified.

Important baseline principles include:

- security by default
- privacy by design
- zero-trust networking where appropriate
- least privilege
- 12-factor app design where appropriate
- operational automation by default
- observability from the start
- reproducibility and portability
- resilient failure modes
- human approval for high-risk actions

## Phase Checklist

### 1. Idea / Opportunity Framing

Define what problem exists, who has it, why it matters, and what success looks like.

Key outputs:

- problem statement
- target users and affected roles
- opportunity statement
- assumptions and risks
- initial success criteria
- explicit non-goals

Security checkpoint:

- Identify sensitive data, obvious abuse cases, trust boundaries, external dependencies, and potential harms.

Guidance: `PRODUCT_FRAMING_GUIDANCE.md`

### 2. Product Requirements

Turn the opportunity into requirements that can guide design and implementation.

Key outputs:

- user needs
- functional requirements
- non-functional requirements
- security and privacy requirements
- operational requirements
- acceptance criteria
- constraints and dependencies

Security checkpoint:

- Security, privacy, compliance, auditability, abuse resistance, and operational safety are requirements, not garnish.

Guidance: `REQUIREMENTS_GUIDANCE.md`

### 3. UX / Product Design

Define how users understand, navigate, trust, and complete the product’s workflows.

Key outputs:

- personas or role models
- jobs-to-be-done
- workflows
- information architecture
- wireframes or prototypes
- accessibility expectations
- UX acceptance criteria
- UX approval

Security checkpoint:

- Design permission-aware states, trust UX, safe confirmations, audit visibility, recovery flows, and clear explanations for risky or automated actions.

Guidance: `UX_GUIDANCE.md`

### 4. Security and Privacy Design

Make security and privacy explicit before implementation hardens bad assumptions into expensive concrete.

Key outputs:

- threat model
- data classification
- data-flow diagram
- identity and access model
- abuse cases
- secrets handling plan
- logging and audit model
- privacy review
- security acceptance criteria

Security checkpoint:

- Security design should be reviewed before implementation begins for serious projects.

Guidance: `SECURITY_GUIDANCE.md`

### 5. Technical Architecture

Define how the system is built, integrated, deployed, observed, and evolved.

Key outputs:

- architecture overview
- component/service boundaries
- data model
- API/contracts
- deployment model
- trust boundaries
- observability model
- operational automation model
- failure/recovery model

Security checkpoint:

- Architecture must show authentication, authorization, network boundaries, ingress/egress, secrets, data flows, audit points, and privileged operations.

Guidance: `ARCHITECTURE_GUIDANCE.md`

### 6. Implementation Planning

Turn the design into an actionable delivery plan.

Key outputs:

- milestones
- backlog breakdown
- sequencing and dependencies
- test strategy
- release strategy
- staffing/ownership assumptions
- risk register

Security checkpoint:

- Security and operational tasks must appear in the normal backlog, not a haunted appendix.

Guidance: `IMPLEMENTATION_PLANNING_GUIDANCE.md`

### 7. Build / Implementation

Implement the product with quality controls and security expectations embedded in everyday work.

Key outputs:

- code
- tests
- migrations
- documentation
- configuration
- deployment artifacts
- feature flags where useful
- review records

Security checkpoint:

- Apply secure coding, least privilege, input validation, authorization checks, dependency hygiene, secret scanning, logging hygiene, and review of risky changes.

Guidance: `IMPLEMENTATION_GUIDANCE.md`

### 8. Verification / QA

Prove the product behaves acceptably before release.

Key outputs:

- functional test results
- UX QA results
- accessibility checks
- integration/regression tests
- performance checks where relevant
- security test results
- known issues and accepted risks

Security checkpoint:

- Test authorization boundaries, abuse cases, input handling, dependency posture, audit logs, and risky workflows.

Guidance: `QA_GUIDANCE.md`

### 9. Release Security Gate

Before release, confirm security and operational readiness.

Key outputs:

- security review record
- accepted-risk record
- unresolved finding list
- release approval
- rollback/disable plan
- monitoring and incident path

Security checkpoint:

- High-risk findings must be fixed, explicitly accepted, or the release should not proceed. Revolutionary stuff, apparently.

Guidance: `RELEASE_SECURITY_GATE.md`

### 10. Launch / Release

Release deliberately, with rollback and support ready.

Key outputs:

- release notes
- deployment checklist
- rollback plan
- monitoring dashboard or checks
- support path
- known limitations
- post-launch review date

Security checkpoint:

- Confirm credentials, configuration, exposure, monitoring, audit, backups, and incident response are ready.

Guidance: `RELEASE_GUIDANCE.md`

### 11. Operations / Post-Launch Iteration

Operate the system, learn from real usage, and improve it.

Key outputs:

- operational runbook
- alerting rules
- automation jobs
- backup/restore process
- maintenance schedule
- vulnerability intake path
- incident process
- post-launch backlog

Security checkpoint:

- Maintain patching, access reviews, audit reviews, incident learning, dependency updates, and abuse monitoring.

Guidance: `OPERATIONS_GUIDANCE.md`

## Definition of Product-Ready for Build

A product or major feature is ready for implementation when:

- the problem and users are defined
- requirements and acceptance criteria exist
- UX direction is approved at the right level
- security and privacy risks are identified
- architecture is plausible and reviewed
- implementation work is broken down
- required human approvals are recorded
- major unknowns are either resolved or explicitly tracked

## Definition of Product-Ready for Release

A product or major feature is ready for release when:

- implementation matches requirements and UX intent
- quality gates have passed or exceptions are approved
- security review is complete
- operational monitoring exists
- rollback/disable paths are known
- support and incident paths are known
- known risks are documented
- release approval is recorded

## Lightweight Project Version

For small internal projects, confirm the project class in `TAILORING_GUIDE.md`, then use only the artifacts justified by risk and complexity.

Suggested minimum:

1. Problem statement
2. Target users/roles
3. Top requirements
4. Top workflows
5. Basic UX sketch
6. Security/privacy notes
7. Architecture sketch
8. Build checklist
9. Minimal QA/security checks
10. Launch/rollback note
11. Post-launch notes after first use

Lightweight does not mean thought-free. It means appropriately brief.
