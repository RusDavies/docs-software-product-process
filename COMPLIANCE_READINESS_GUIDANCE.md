# Compliance Readiness Guidance

Enterprise-targeted products should assume customers will ask about SOC 2, ISO/IEC 27001, security questionnaires, vendor risk reviews, and evidence. If the product is meant for serious business use, compliance readiness is part of product readiness, not a decorative badge slapped on later by a panicked founder with a spreadsheet.

## Purpose

This guidance helps projects prepare for:

- SOC 2 readiness and attestation planning
- ISO/IEC 27001 alignment or certification planning
- enterprise vendor-security reviews
- customer security questionnaires
- audit evidence collection
- security policy and control documentation

This is not legal, audit, or certification advice. A qualified auditor, compliance lead, or legal advisor should confirm the final scope and control interpretation.

## When This Applies

Use this guidance when a project targets or may target:

- enterprise customers
- regulated customers
- security-conscious B2B customers
- customers requiring SOC 2 reports
- customers requiring ISO/IEC 27001 certification or alignment
- customers requiring vendor-risk assessments
- products handling customer data, identity data, operational data, financial data, health data, employee data, or sensitive business data
- products integrated into customer infrastructure, identity providers, CI/CD, source code, ticketing, monitoring, or production workflows

## Minimum Expectations for Enterprise-Targeted Products

At minimum, define:

1. Compliance target: SOC 2, ISO/IEC 27001, both, or readiness only
2. System and organizational scope
3. Control owner(s)
4. Policy/document inventory
5. Control register
6. Evidence register
7. Risk register and accepted-risk process
8. Vendor/dependency register
9. Access-control review process
10. Change-management evidence
11. Incident-response evidence
12. Security-monitoring and audit-log evidence
13. Backup/business-continuity expectations
14. Customer-facing security posture summary

## SOC 2 Readiness Track

SOC 2 readiness should identify which Trust Services Criteria apply.

Common baseline:

- Security: normally required
- Availability: likely required for production SaaS or business-critical services
- Confidentiality: likely required when handling sensitive customer data
- Processing Integrity: relevant when correctness/completeness of processing matters
- Privacy: relevant when personal information is collected, used, retained, disclosed, or deleted under privacy commitments

Capture:

- SOC 2 report target: Type I, Type II, or readiness only
- audit period target for Type II
- system description scope
- control objectives
- controls mapped to criteria
- evidence source and owner for each control
- control test frequency
- exceptions and remediation plan

Common SOC 2 evidence themes:

- access reviews
- onboarding/offboarding records
- MFA/SSO enforcement
- privileged-access approvals
- change approvals and deployment evidence
- security reviews for risky changes
- vulnerability management records
- incident-response tests or incident records
- backup/restore evidence
- monitoring and alert review
- vendor/security review records
- risk assessment updates
- policy acknowledgements where appropriate

## ISO/IEC 27001 Readiness Track

ISO/IEC 27001 readiness should define the Information Security Management System (ISMS) scope and evidence model.

Capture:

- ISMS scope statement
- interested parties and requirements
- risk assessment method
- risk treatment plan
- Statement of Applicability (SoA)
- Annex A control applicability rationale
- security objectives and metrics
- internal audit approach
- management review approach
- corrective-action tracking

Common ISO 27001 evidence themes:

- asset inventory
- risk assessment and treatment decisions
- access-control policy and reviews
- supplier/vendor management
- secure development process
- change management
- logging and monitoring
- incident management
- business continuity / backup restore
- human-resources security where applicable
- cryptography/secrets handling
- vulnerability management
- internal audit and management review records

## Enterprise Security Questionnaire Readiness

Enterprise sales and procurement often require security questionnaires before SOC 2 or ISO evidence is fully mature.

Prepare answers for:

- company and product security overview
- data types processed
- data residency and retention
- encryption in transit and at rest
- access control and MFA
- SSO/SAML/OIDC support where relevant
- RBAC and least privilege
- audit logging
- vulnerability management
- secure SDLC
- dependency and supply-chain management
- incident response
- backup and disaster recovery
- subprocessors/vendors
- penetration testing or security testing
- compliance roadmap and current status

Do not overclaim. “Planned,” “implemented,” “partially implemented,” and “not applicable” are better than inventing compliance fan fiction.

## Full Compliance Readiness Checklist

### 1. Scope

Capture:

- product/system scope
- environments in scope
- data types in scope
- teams/people in scope
- infrastructure and vendors in scope
- exclusions and rationale
- target customers and contractual expectations

### 2. Control Register

Capture each control with:

- control ID
- framework mapping
- control description
- owner
- implementation status
- evidence source
- test frequency
- gaps/remediation

### 3. Evidence Register

Track:

- evidence item
- control(s) supported
- evidence location
- owner
- collection frequency
- retention period
- last collected date
- gaps or exceptions

### 4. Policy Index

Maintain policies or equivalent documented procedures for:

- information security
- access control
- acceptable use
- asset management
- data classification and handling
- cryptography/secrets
- secure SDLC
- change management
- vulnerability management
- incident response
- business continuity / disaster recovery
- vendor management
- risk management
- logging and monitoring
- backup and restore
- privacy/data retention where applicable

### 5. Risk Management

Capture:

- risk assessment cadence
- risk scoring model
- risk owners
- treatment options
- accepted-risk approval
- review/expiry dates
- remediation tracking

### 6. Access Control

Capture:

- identity provider model
- MFA requirements
- privileged roles
- approval process
- onboarding/offboarding
- periodic access reviews
- service accounts and tokens
- break-glass access

### 7. Change Management and Secure SDLC

Capture:

- code review expectations
- security review triggers
- test evidence
- deployment approval
- rollback path
- emergency change process
- dependency update process
- secret scanning and vulnerability scanning

### 8. Monitoring, Logging, and Incident Response

Capture:

- audit logs
- security events
- alert routing
- review cadence
- incident severity model
- containment process
- communication process
- post-incident review

### 9. Vendor and Supply-Chain Management

Capture:

- vendor inventory
- data shared with each vendor
- vendor criticality
- security review status
- contractual/compliance notes
- dependency scanning
- artifact provenance where relevant

### 10. Business Continuity and Recovery

Capture:

- backup scope and cadence
- restore tests
- recovery objectives
- critical dependencies
- disaster recovery plan
- operational ownership

### 11. Customer-Facing Security Package

Prepare:

- security overview
- compliance status and roadmap
- data-processing summary
- subprocessors list where applicable
- responsible disclosure/security contact
- incident notification posture
- standard questionnaire answers

## Lightweight Enterprise Version

For early enterprise-targeted products before formal audit:

1. Define whether SOC 2, ISO 27001, or both are target outcomes.
2. Create a control register.
3. Create an evidence register.
4. Create a policy index with current/planned status.
5. Document key gaps and remediation backlog.
6. Prepare honest customer-facing security answers.
7. Revisit monthly until audit readiness is real.

## Recommended Project Files

- `docs/compliance/compliance-readiness.md`
- `docs/compliance/control-register.md`
- `docs/compliance/evidence-register.md`
- `docs/compliance/policy-index.md`
- `docs/compliance/soc2-iso27001-crosswalk.md`
- `docs/compliance/audit-readiness-checklist.md`
- `docs/compliance/security-questionnaire.md`
- `docs/security/risk-register.md`
- `docs/security/accepted-risks.md`

## Definition of Compliance-Ready

A project is compliance-ready when:

- target frameworks are defined
- scope is documented
- controls are mapped
- owners are assigned
- evidence sources are known
- policy gaps are tracked
- risk treatment is documented
- customer-facing claims are accurate
- audit/certification next steps are clear

## Definition of Compliance-Done

Compliance readiness is done when:

- controls are implemented or gaps are tracked with owners
- evidence is collected on the required cadence
- required policies/procedures exist
- access, change, incident, vendor, and risk processes are operating
- unresolved risks are explicitly accepted or remediated
- customer-facing security claims match reality
- formal auditor/certification work, if targeted, has a defined owner and plan
