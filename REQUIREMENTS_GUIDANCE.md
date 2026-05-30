# Requirements Guidance

Requirements translate product intent into concrete expectations. Good requirements prevent “I thought you meant…” from becoming the architecture.

## Purpose

Every project should define:

- user requirements
- functional requirements
- non-functional requirements
- security and privacy requirements
- operational requirements
- product operational estate requirements
- Digital Estate Management requirements where applicable
- AI-agent operational requirements unless explicitly throw-away or product-owner exempted
- acceptance criteria
- constraints and dependencies

## Minimum Expectations

At minimum, capture:

1. User needs
2. Functional requirements
3. Non-functional requirements
4. Security/privacy requirements
5. Operational requirements
6. Acceptance criteria
7. Open questions

## Full Requirements Checklist

### 1. User and Role Requirements

Capture what users need to accomplish.

Include:

- user goals
- role-specific needs
- permission differences
- workflow expectations
- accessibility needs
- trust/confidence needs

### 2. Functional Requirements

Define what the product must do.

Include:

- features
- workflows
- inputs and outputs
- validation rules
- integrations
- notifications
- administration features
- reporting needs

### 3. Non-Functional Requirements

Define quality expectations.

Include:

- performance
- availability
- reliability
- SEO/discovery requirements for public web projects
- scalability
- maintainability
- accessibility
- compatibility
- localization, where relevant

### 4. Security Requirements

Security requirements are product requirements. Do not staple them on afterward and look surprised.

Include:

- authentication
- authorization
- roles and permissions
- data protection
- audit logging
- abuse prevention
- secrets handling
- vulnerability management
- secure defaults
- destructive action safeguards

### 5. Privacy and Data Requirements

Include:

- data classification
- data minimization
- retention
- deletion/export needs
- consent/legal basis, where relevant
- sensitive logging restrictions
- access visibility

### 6. Operational Requirements

Include:

- monitoring
- alerting
- backups
- restore expectations
- routine automation
- support procedures
- maintenance tasks
- incident response
- operator ratio expectations

### 7. Product Operational Estate Requirements

Define the product's operational footprint before it becomes a scavenger hunt with invoices.

Include:

- domains and DNS zones
- cloud accounts, SaaS tenants, repositories, registries, and package/distribution accounts
- environments and deployment targets
- certificates, keys, secrets, and renewal expectations
- external services, dependencies, and billing owners
- data stores, backup locations, and retention obligations
- ownership, access review, and handover expectations
- decommissioning expectations

### 8. Digital Estate Management Requirements, Where Applicable

For products with non-corporate end users, assess whether the product should help users plan, document, protect, or administer digital assets after death or incapacity.

Include:

- applicability decision: applies, not applicable, or deferred
- user digital asset categories: financial, sentimental, identity, legal, health/family, creator/business, device/access infrastructure, AI/data, or other
- user asset inventory requirements
- disposition instructions: preserve, transfer, export, memorialize, delete, close, sell, or seek professional review
- trusted-person roles: executor, digital helper, family member, advisor, technical custodian, or professional fiduciary
- distinction between consent, legal authority, and technical access
- inventory/secret separation requirements
- export, delegated access, emergency access, death/incapacity, and inactivity workflows where applicable
- audit, notification, delay, revocation, and support requirements for trusted-contact workflows
- privacy requirements for private communications, third-party data, sensitive media, and family-dispute contexts
- limits and disclaimers around platform rules, local law, transferability, provider cooperation, and professional advice

Guidance: `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`

### 9. AI-Agent Operational Requirements, Where Applicable

If approved AI agents may help inspect, diagnose, document, maintain, or operate the product, define the boundary as a product requirement instead of hoping future automation develops manners.

Include:

- read-only vs write-capable agent roles
- allowed diagnostic, reporting, maintenance, and remediation actions
- actions that require human approval
- actions agents must never perform
- least-privilege access requirements
- audit logging for agent-initiated actions
- safe rollback/undo requirements for agent-performed changes
- interfaces agents should use, such as APIs, CLIs, runbooks, or admin tools
- sensitive data exposure limits for agent workflows

### 10. Compliance and Policy Requirements

Where relevant, capture:

- regulatory needs
- internal policies
- contractual obligations
- enterprise customer expectations
- SOC 2 attestation target, if applicable
- ISO/IEC 27001 certification or alignment target, if applicable
- vendor-risk/security-questionnaire requirements
- audit evidence requirements
- control ownership requirements
- public metadata/SEO claim constraints where relevant
- approvals required

### 11. Acceptance Criteria

Make requirements verifiable.

Good acceptance criteria are:

- specific
- testable
- role-aware
- state-aware
- security-aware
- clear about failure/recovery behavior

Avoid: “make it intuitive”, “make it secure”, and other prayers in trench coats.

## Lightweight Project Version

For small projects:

1. Top user stories or jobs
2. Must-have features
3. Security/privacy notes
4. Operational notes
5. Acceptance criteria for each major item

## Recommended Project Files

- `docs/requirements/product-requirements.md`
- `docs/requirements/user-stories.md`
- `docs/requirements/non-functional-requirements.md`
- `docs/requirements/security-privacy-requirements.md`
- `docs/requirements/operational-requirements.md`
- `docs/requirements/digital-estate-management-requirements.md`, where applicable
- `docs/requirements/acceptance-criteria.md`

## Definition of Requirements-Ready

Requirements are ready when:

- user needs are understood
- required behavior is documented
- quality expectations are known
- security/privacy/operations requirements exist
- acceptance criteria are testable
- unresolved questions are tracked

## Definition of Requirements-Done

Requirements are done when:

- implementation and QA can proceed without guessing the product intent
- changes are controlled through backlog/review
- the relevant human has approved the requirements baseline
