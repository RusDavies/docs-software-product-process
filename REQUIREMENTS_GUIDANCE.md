# Requirements Guidance

Requirements translate product intent into concrete expectations. Good requirements prevent “I thought you meant…” from becoming the architecture.

## Purpose

Every project should define:

- user requirements
- functional requirements
- non-functional requirements
- security and privacy requirements
- operational requirements
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

### 7. Compliance and Policy Requirements

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
- approvals required

### 8. Acceptance Criteria

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
