# Tailoring Guide

Use this guide before applying the full guidance set. The goal is to choose the right amount of process for the project, not to make every tiny utility cosplay as a bank.

## Purpose

Tailoring answers:

- how much documentation is required
- which checks are mandatory
- who must approve the work
- what evidence should be kept
- where agents can proceed autonomously
- when lightweight guidance is enough

## Project Classes

### Class 1: Tiny / Personal / Throwaway

Use for scripts, experiments, one-off internal helpers, prototypes, and notes that do not affect users, production data, money, public output, or security-sensitive workflows.

Required:

- short problem statement
- basic usage notes
- obvious safety/privacy notes
- direct inspection or smoke test before calling done

Recommended:

- `README.md`
- lightweight sections from relevant guidance docs
- small backlog or TODO list if follow-up exists

Usually optional:

- formal UX artifacts
- formal architecture docs
- release security gate
- operations runbook

Escalate if the work starts touching real users, secrets, external systems, production data, or irreversible actions.

### Class 2: Small Internal Tool

Use for internal tools used by one person or a small trusted group, with limited blast radius and no public-facing release.

Required:

- product/problem framing
- requirements or acceptance criteria
- lightweight UX/workflow notes where a UI exists
- security/privacy notes
- lightweight architecture/deployment notes
- implementation checklist
- basic QA evidence
- rollback/disable note

Recommended documents:

- `PRODUCT_FRAMING_GUIDANCE.md`
- `REQUIREMENTS_GUIDANCE.md`
- `ARCHITECTURE_GUIDANCE.md`
- `IMPLEMENTATION_GUIDANCE.md`
- `QA_GUIDANCE.md`
- relevant templates from `templates/`

Approval:

- human approval for external actions, destructive actions, sensitive-data handling, or deployment into shared use

### Class 3: Serious Internal / Multi-User Product

Use for tools with multiple users, persistent data, meaningful workflow dependence, operational burden, or security/privacy implications.

Required:

- product brief
- requirements spec with acceptance criteria
- UX/workflow notes or design artifacts
- security/privacy review
- architecture overview
- implementation plan and backlog breakdown
- QA plan and test evidence
- release checklist
- operations runbook
- user/admin/operator documentation as applicable
- decision records for major tradeoffs

Recommended documents:

- all core guidance docs except items clearly irrelevant to the product
- `RELEASE_SECURITY_GATE.md` before launch
- `OPERATIONS_GUIDANCE.md` before ongoing use

Approval:

- human approval for product direction, release, accepted risk, external integration, data retention policy, and any high-risk automation

### Class 4: Public / Production / Commercial Product

Use for public-facing products, paid products, production services, customer data, or systems that affect trust, safety, finances, legal exposure, or reputation.

Required:

- full product process
- explicit security and privacy design
- threat model
- architecture review
- test evidence
- release security gate
- rollback/disable plan
- monitoring and incident path
- operations runbook
- accepted-risk record where needed
- post-launch review

Recommended:

- dependency/supply-chain evidence
- audit-event design
- backup/restore validation
- accessibility review
- abuse-case review
- support process

Approval:

- human approval required for release, accepted risks, public communications, external integrations, data handling changes, destructive operations, and incident/customer-impact decisions

### Class 4E: Enterprise-Targeted Product

Use when the product targets enterprise, regulated-business, security-conscious B2B, or procurement-heavy customers that are likely to ask for SOC 2 attestation, ISO/IEC 27001 certification/alignment, vendor-risk review, or detailed security questionnaires.

Class 4E inherits Class 4 and adds compliance-readiness expectations.

Required:

- compliance target: SOC 2, ISO/IEC 27001, both, or readiness only
- documented compliance scope
- control register
- evidence register
- policy/document index
- enterprise security questionnaire answers
- vendor/dependency register
- access-review process
- change-management evidence process
- incident-response evidence process
- customer-facing security posture summary

Recommended:

- SOC 2 / ISO/IEC 27001 crosswalk
- audit-readiness checklist
- Statement of Applicability planning if ISO/IEC 27001 certification is a real target
- SOC 2 Type I/Type II roadmap if attestation is a real target
- monthly evidence-readiness review until audit posture is mature

Approval:

- human approval required for compliance claims, audit scope, customer-facing security answers, accepted compliance gaps, formal auditor engagement, and any claim that the product is SOC 2 or ISO/IEC 27001 ready/certified.

Guidance: `COMPLIANCE_READINESS_GUIDANCE.md`

### Class 5: Regulated / Safety-Critical / High-Risk

Use when legal, medical, financial, safety, employment, child-related, disability, identity, surveillance, or high-impact automated decision-making concerns are present.

Required:

- all Class 4 requirements
- stricter privacy/data-flow review
- human decision ownership
- auditability and evidence preservation
- documented limitations and disclaimers
- explicit escalation paths
- compliance/legal review where appropriate

Approval:

- humans own product direction, policy decisions, accepted risk, and release decisions. Agents may prepare evidence but must not quietly become a lawyer, doctor, regulator, or chaos goblin with commit access.

## Tailoring Matrix

| Artifact / Check | Class 1 | Class 2 | Class 3 | Class 4 | Class 4E | Class 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Problem statement | Required | Required | Required | Required | Required | Required |
| Requirements / acceptance criteria | Light | Required | Required | Required | Required | Required |
| UX/workflow notes | If UI | If UI | Required if user-facing | Required | Required | Required |
| Accessibility expectations | Basic if UI | Basic if UI | Required if UI | Required if UI | Required if UI | Required if UI |
| Security/privacy notes | Basic | Required | Required | Required | Required | Required |
| Threat model | Optional | Optional unless risky | Recommended | Required | Required | Required |
| Architecture notes | Light | Required | Required | Required | Required | Required |
| Implementation plan | Optional | Light | Required | Required | Required | Required |
| QA evidence | Smoke test | Required | Required | Required | Required | Required |
| Release security gate | Optional | If shared/risky | Required before release | Required | Required | Required |
| Rollback/disable plan | Optional | Required | Required | Required | Required | Required |
| Operations runbook | Optional | If operated | Required | Required | Required | Required |
| Risk acceptance record | Optional | If risk accepted | Required when applicable | Required when applicable | Required when applicable | Required when applicable |
| Documentation plan | Optional | Light | Required | Required | Required | Required |
| User/admin docs | Usage notes | If shared/user-facing | Required if user-facing | Required | Required | Required |
| Operator docs/runbook | Optional | If operated | Required | Required | Required | Required |
| Documentation QA | Smoke check | Required if shared | Required | Required | Required | Required |
| Compliance readiness | Optional | Optional | If enterprise-targeted | If enterprise-targeted | Required | Required if regulated/customer-required |
| Post-launch review | Optional | Recommended | Required | Required | Required | Required |

## Escalation Triggers

Escalate to a higher project class when any of these appear:

- real users beyond the creator
- public internet exposure
- enterprise customers or security-conscious B2B procurement
- customer requests for SOC 2, ISO/IEC 27001, vendor-risk review, or security questionnaire evidence
- customer or personal data
- secrets, credentials, auth, or authorization
- payment, legal, medical, employment, disability, child-related, or safety implications
- persistent production data
- irreversible/destructive actions
- automated external messaging or posting
- agent-operated production actions
- security monitoring, incident response, or access-control decisions
- reliance by other projects or people
- someone other than the creator needs to use, administer, support, or operate the product

## Minimum Evidence by Class

Class 1 evidence can be a short note and smoke-test result.

Class 2 evidence should include:

- requirements or TODO completion notes
- test/smoke-test output
- user/admin/operator notes where shared or operated
- known limitations
- rollback/disable note

Class 3 evidence should include:

- requirements and acceptance criteria
- architecture/security/privacy notes
- documentation plan and documentation QA results
- QA results
- release checklist
- operations notes

Class 4 evidence should include:

- all Class 3 evidence
- release security gate result
- accepted-risk record if anything material remains
- monitoring/incident readiness
- rollback validation or clear rollback procedure
- post-launch review schedule

Class 4E evidence should also include:

- compliance target and scope
- control register
- evidence register
- policy index
- SOC 2 / ISO/IEC 27001 crosswalk where both are target outcomes
- audit-readiness checklist
- enterprise security questionnaire answers

Class 5 evidence should include all Class 4 evidence plus any required compliance/legal/safety-review evidence.

## Agent Use

Agents should use the smallest project class that fits the risk, then escalate when new facts increase risk.

Agents may generally proceed autonomously with internal, reversible Class 1 and low-risk Class 2 work.

Agents must pause for human approval when work involves:

- external/public actions
- destructive or irreversible operations
- production releases
- sensitive data policy decisions
- accepted-risk decisions
- major product direction or prioritization
- high-risk automation

When unsure, choose the safer class and ask one specific question. Heroic ambiguity is how incident reports get their origin story.
