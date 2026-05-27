# Governance and Approvals

This document defines who controls product direction, risk acceptance, release decisions, and agent autonomy across workspace projects.

## Purpose

Guidance documents are useful only if decisions and approvals are clear. This document prevents process from turning into vibes with filenames.

It defines:

- human-owned decisions
- agent autonomy boundaries
- approval checkpoints
- accepted-risk rules
- evidence expectations
- decision records

## Governance Principles

1. Humans own product direction.
2. Humans own risk acceptance.
3. Humans approve external, public, destructive, and production-impacting actions.
4. Agents may prepare evidence, propose options, implement approved work, and perform low-risk internal tasks.
5. Automation must be constrained, auditable, reversible where possible, and boring in the best possible way.

## Decision Ownership

### Human-Owned Decisions

Humans must own decisions about:

- product goals and priorities
- target users and market positioning
- release approval
- accepted security/privacy/operational/compliance risk
- legal, medical, financial, employment, child-related, disability, or safety-sensitive direction
- public statements and external communications
- enterprise compliance claims, including SOC 2 and ISO/IEC 27001 readiness, attestation, certification, or alignment
- data retention, deletion, sharing, or consent policy
- production access grants
- destructive or irreversible actions
- high-risk automation policies

### Agent-Owned or Agent-Executable Work

Agents may generally do the following without additional approval when scoped to the workspace and low risk:

- read and summarize project files
- create or improve internal documentation
- propose backlog items
- implement approved backlog items
- run tests, linters, builds, and local inspections
- create branches and commits following project workflow
- draft templates, checklists, runbooks, and release notes
- identify risks and recommend mitigations

Agents should still report meaningful changes and blockers.

## Approval Checkpoints

### Product Approval

Required before major implementation when product direction is ambiguous.

Evidence:

- product brief or framing note
- target users/roles
- goals and non-goals
- important assumptions

### UX Approval

Required for user-facing workflows when design direction affects usability, trust, or accessibility.

Evidence:

- workflows
- wireframes/prototypes or written equivalent
- important states and edge cases
- accessibility expectations

### Architecture Approval

Required for serious internal, production, public, or high-risk systems.

Evidence:

- architecture overview
- data model
- trust boundaries
- deployment/runtime model
- key tradeoffs

### Security and Privacy Approval

Required for systems touching sensitive data, auth, secrets, public exposure, customer data, production systems, or high-risk decisions.

Evidence:

- asset/data inventory
- data flows
- threat model or abuse-case review
- security requirements
- privacy notes
- unresolved findings

### Compliance Claim Approval

Required before making customer-facing or public claims about SOC 2, ISO/IEC 27001, audit readiness, certification, attestation, or enterprise compliance posture.

Evidence:

- compliance target and scope
- control register
- evidence register
- policy index
- gaps and accepted risks
- reviewer/approver
- exact claim text or customer-facing answer

### Release Approval

Required before launching Class 3+ shared systems and all Class 4/4E/5 systems.

Evidence:

- passed QA or approved exceptions
- release security gate
- rollback/disable plan
- monitoring/support path
- known limitations
- accepted risks, if any

### Risk Acceptance

Risk acceptance must be explicit. Silence is not approval; it is just a bug wearing a cardigan.

Evidence:

- risk description
- impact and likelihood
- mitigation options considered
- selected decision
- owner/approver
- expiry/review date where appropriate

## Approval Format

Approvals may be lightweight, but they must be visible and durable.

Acceptable forms:

- project `docs/decisions/ADR-*.md`
- `docs/release/release-checklist.md`
- `docs/security/accepted-risks.md`
- issue/backlog item with approval note
- chat message copied into the project evidence trail when needed

Minimum approval fields:

- decision
- approver
- date
- scope
- conditions or limitations
- follow-up date if relevant

## Agent Stop Conditions

Agents must stop and ask before:

- sending external communications or public posts
- changing production systems
- deleting or destructively modifying data
- exposing a service publicly
- handling secrets in a new way
- accepting unresolved high or critical security risk
- making legal/medical/financial/safety-sensitive recommendations as final authority
- changing product priorities when humans have not delegated that authority
- bypassing tests, gates, or safety controls to “just ship it”

## Evidence Trail

For serious work, keep enough evidence that another competent human or agent can understand what happened.

Recommended locations:

- `docs/decisions/`
- `docs/security/`
- `docs/architecture/`
- `docs/qa/`
- `docs/release/`
- `docs/operations/`

At minimum, record:

- what changed
- why it changed
- how it was verified
- what risks remain
- who approved high-risk decisions
- what follow-up exists

## Backlog Governance

Backlogs should include security, privacy, operations, accessibility, documentation, and technical debt work as normal first-class items.

Do not hide them in a separate “someday maybe” list unless the goal is to build future archaeology.

Each backlog item should include:

- goal
- acceptance criteria
- risk/priority notes
- verification method
- approval requirement if any

## Incident and Exception Governance

During incidents or urgent exceptions:

- preserve evidence
- prefer reversible mitigations
- keep humans informed
- record what was done
- record follow-up hardening work
- do not normalize emergency bypasses into standard practice

## Definition of Governance-Ready

A project is governance-ready when:

- project class is selected
- human-owned decisions are identified
- approval checkpoints are known
- evidence locations are chosen
- agent autonomy boundaries are clear

## Definition of Governance-Done

Governance is done when:

- required approvals are recorded
- accepted risks are explicit
- release/operation decisions have evidence
- follow-up items are in the backlog
- agents and humans can tell who owns what without consulting a séance
