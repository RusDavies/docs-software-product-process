# Software Product Development Process

This document defines the baseline process for developing software products. It is intended for projects that may become real, used, operated, maintained, or exposed to other humans — an alarming number of ways for software to become inconvenient.

## Purpose

Every project should move deliberately from idea to operation:

1. Frame the product opportunity.
2. Define requirements.
3. Design the user experience.
4. Design security and privacy.
5. Define compliance readiness where enterprise, regulated, or customer-required.
6. Plan user, admin, operator, and developer documentation.
7. Design SEO/discovery for web products.
8. Design the technical architecture.
9. Plan implementation.
10. Build the product and documentation.
11. Verify quality, including documentation and SEO quality.
12. Pass release, documentation, SEO, and security gates.
13. Launch deliberately.
14. Operate and improve it.

The process is modular. Small projects can use lightweight versions. Larger, riskier, public, customer-facing, enterprise-targeted, regulated, security-sensitive, or multi-role projects should use the full process.

Before applying the full process, classify the project and select any target profile with `TAILORING_GUIDE.md`. Class 0 throw-away work is an explicit product-owner classification and excludes normal maintenance, product operational estate management, AI-agent operation design, and other long-term product machinery unless the classification breaks. Software library/package targets keep security, compatibility, release, documentation, provenance, vulnerability-intake, and patch-maintenance concerns, but exclude normal runtime operations concerns unless the library also ships an operated runtime component. Use `GOVERNANCE_AND_APPROVALS.md` when approvals, accepted risk, release authority, or agent autonomy boundaries matter.

## Process Principles

All phases should apply `ENGINEERING_PRINCIPLES.md`. Project teams may tailor or deviate from principles, but deviations should be explicit and justified.

Important baseline principles include:

- security by default
- privacy by design
- zero-trust networking where appropriate
- least privilege
- 12-factor app design where appropriate
- operational automation by default
- product operational estate stewardship
- Digital Estate Management assessment for non-corporate/end-user products
- AI-operable by design unless explicitly throw-away or product-owner exempted
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
- Digital Estate Management applicability decision for products with non-corporate users, personal assets, family/creator/identity data, or death/incapacity access implications

Security checkpoint:

- Identify sensitive data, obvious abuse cases, trust boundaries, external dependencies, and potential harms.
- For consumer, family, creator, life-admin, personal archive, AI-memory, finance, crypto, or personal-data products, decide whether Digital Estate Management applies.

Guidance: `PRODUCT_FRAMING_GUIDANCE.md`

### 2. Product Requirements

Turn the opportunity into requirements that can guide design and implementation.

Key outputs:

- user needs
- functional requirements
- non-functional requirements
- security and privacy requirements
- operational requirements
- product operational estate requirements
- Digital Estate Management requirements where applicable
- AI-agent operational requirements unless explicitly throw-away or product-owner exempted
- acceptance criteria
- constraints and dependencies

Security checkpoint:

- Security, privacy, compliance, auditability, abuse resistance, product operational estate stewardship, Digital Estate Management applicability, agent-operability boundaries, and operational safety are requirements, not garnish.

Guidance: `REQUIREMENTS_GUIDANCE.md`, `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`

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
- Digital Estate Management workflows where applicable: user asset inventory, disposition instructions, trusted people, export, review reminders, and death/incapacity paths

Security checkpoint:

- Design permission-aware states, trust UX, safe confirmations, audit visibility, recovery flows, and clear explanations for risky or automated actions.
- For Digital Estate Management features, clearly distinguish legal authority, consent, trusted-contact status, and technical access.

Guidance: `UX_GUIDANCE.md`, `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`

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
- CSAF/VEX provider-readiness decision where the product is a SaaS, security product, infrastructure product, developer tool, library/package, or enterprise-targeted product expected to publish machine-readable advisories about itself
- Digital Estate Management security/privacy review where applicable, including inventory/secret separation, trusted-contact access, export, survivor workflows, and third-party privacy

Security checkpoint:

- Security design should be reviewed before implementation begins for serious projects.
- Digital Estate Management features must not become password dumps, impersonation workflows, or terms-of-service bypass instructions.

Guidance: `SECURITY_GUIDANCE.md`, `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`

### 5. Compliance Readiness, Where Applicable

For enterprise-targeted, regulated, customer-facing B2B, or procurement-heavy products, define compliance readiness early enough that SOC 2, ISO/IEC 27001, and security-questionnaire evidence can be built into the operating model instead of reconstructed later with a shovel.

Key outputs:

- compliance target and scope
- control register
- evidence register
- policy/document index
- SOC 2 / ISO/IEC 27001 crosswalk where relevant
- enterprise security questionnaire answers
- audit-readiness checklist
- compliance gap backlog

Security checkpoint:

- Do not claim SOC 2 attestation, ISO/IEC 27001 certification, CSAF/VEX advisory-provider support, or equivalent readiness unless scope, controls, evidence, validation, and approval support that claim.

Guidance: `COMPLIANCE_READINESS_GUIDANCE.md`

### 6. Documentation Planning

Define what users, admins, operators, developers, support staff, and enterprise reviewers need to understand before build and release.

Key outputs:

- documentation audience map
- required user/admin/operator/developer docs
- quick-start and configuration expectations
- troubleshooting/recovery expectations
- documentation acceptance criteria
- documentation owner and maintenance plan
- documentation QA plan

Security checkpoint:

- Security, privacy, safety, and compliance claims in documentation must be accurate and approved before release.

Guidance: `DOCUMENTATION_GUIDANCE.md`

### 7. SEO / Discovery Design, Where Applicable

For public web products, documentation sites, marketing pages, content sites, landing pages, and enterprise trust pages, design search/discovery before build.

Key outputs:

- SEO/discovery goals
- target audiences and search intent
- page inventory and URL strategy
- metadata and share-preview plan
- crawl/index/sitemap/robots/canonical approach
- structured data plan where relevant
- performance/Core Web Vitals expectations
- analytics/search measurement plan
- launch SEO QA checklist

Security checkpoint:

- SEO metadata, structured data, public content, and snippets must not leak private data, overclaim security/compliance status, or contradict approved documentation.

Guidance: `SEO_GUIDANCE.md`

### 8. Technical Architecture

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
- product operational estate inventory
- ownership and account map
- dependency/service map
- environment and deployment inventory
- privileged access model for humans and approved agents
- failure/recovery model

Security checkpoint:

- Architecture must show authentication, authorization, network boundaries, ingress/egress, secrets, data flows, audit points, privileged operations, product operational estate ownership, and any AI-agent operational interfaces or autonomy boundaries.

Guidance: `ARCHITECTURE_GUIDANCE.md`

### 9. Implementation Planning

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

### 10. Build / Implementation

Implement the product with quality controls and security expectations embedded in everyday work.

Key outputs:

- code
- tests
- migrations
- user/admin/operator/developer documentation
- configuration
- deployment artifacts
- feature flags where useful
- review records

Security checkpoint:

- Apply secure coding, least privilege, input validation, authorization checks, dependency hygiene, secret scanning, logging hygiene, and review of risky changes.

Guidance: `IMPLEMENTATION_GUIDANCE.md`

### 11. Verification / QA

Prove the product behaves acceptably before release.

Key outputs:

- functional test results
- UX QA results
- accessibility checks
- integration/regression tests
- performance checks where relevant
- security test results
- documentation QA results
- SEO QA results for web projects
- known issues and accepted risks

Security checkpoint:

- Test authorization boundaries, abuse cases, input handling, dependency posture, audit logs, and risky workflows.

Guidance: `QA_GUIDANCE.md`

### 12. Release Security Gate

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

### 13. Launch / Release

Release deliberately, with rollback and support ready.

Key outputs:

- release notes
- user/admin/operator documentation
- SEO launch checklist for web projects
- deployment checklist
- rollback plan
- monitoring dashboard or checks
- support path
- known limitations
- Digital Estate Management release evidence where applicable, including tested export/delegated/survivor workflows and accurate user-facing limitations
- post-launch review date

Security checkpoint:

- Confirm credentials, configuration, exposure, monitoring, audit, backups, and incident response are ready.
- For Digital Estate Management features, confirm inventory/secret separation, authority/consent boundaries, export/delegated access auditability, and no overpromised legal/provider outcomes.

Guidance: `RELEASE_GUIDANCE.md`, `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`

### 14. Operations / Post-Launch Iteration

Operate the system, learn from real usage, and improve it.

Key outputs:

- operational runbook
- maintained product operational estate register
- service/account/domain ownership map
- account, domain, certificate, secret, and dependency renewal schedule
- alerting rules
- automation jobs
- agent-operable runbooks and safe automation boundaries, where applicable
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
- documentation needs and owners are identified
- SEO/discovery needs are identified for web projects
- required human approvals are recorded
- major unknowns are either resolved or explicitly tracked

## Definition of Product-Ready for Release

A product or major feature is ready for release when:

- implementation matches requirements and UX intent
- quality gates have passed or exceptions are approved
- security review is complete
- required documentation exists and has passed documentation QA or approved exceptions
- web SEO checks have passed or exceptions are approved where applicable
- operational monitoring exists
- product operational estate inventory is complete enough for operation
- ownership, renewal, access, and incident paths are known
- Digital Estate Management applicability is recorded, and applicable user-facing estate workflows meet approved requirements
- AI-agent operational boundaries are documented unless the product owner explicitly classified the work as throw-away or approved an exemption
- agent-accessible tools/APIs are least-privilege, observable, and approval-gated for risky actions
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
7. Compliance readiness notes if enterprise-targeted or customer-required
8. Documentation notes for users/operators
9. SEO/discovery notes for web projects
10. Architecture sketch
11. Build checklist
12. Minimal QA/security/documentation/SEO checks
13. Launch/rollback note
14. Post-launch notes after first use

Lightweight does not mean thought-free. It means appropriately brief.
