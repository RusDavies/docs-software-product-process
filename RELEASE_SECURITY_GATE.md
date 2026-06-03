# Release Security Gate

The release security gate is the explicit checkpoint before a product, feature, or major change ships. It exists because “we’ll secure it later” is how later becomes incident response.

For software libraries/packages, this gate focuses on dependency posture, supply-chain integrity, package contents, signing/provenance, secure defaults, misuse resistance, vulnerability disclosure, and security-patch readiness. Runtime operations checks apply only when the library also ships an operated service or runtime component.

## Purpose

Before release, confirm:

- security requirements are met
- serious findings are resolved or accepted
- secrets/config/exposure are reviewed
- audit and monitoring are ready
- operational response paths exist
- humans approve the remaining risk

## Minimum Expectations

At minimum, capture:

1. Scope of release
2. Security checklist result
3. Open findings
4. Accepted risks
5. Secrets/config review
6. Dependency posture
7. Monitoring/audit readiness
8. Compliance-readiness status for enterprise-targeted products
9. CSAF/VEX advisory-provider readiness decision for SaaS, security, infrastructure, developer-tool, library/package, or enterprise-targeted products
10. Approval decision

## Full Release Security Checklist

### 1. Scope Confirmation

Capture:

- what is being released
- changed components
- changed data flows
- changed permissions
- changed external exposure
- changed dependencies

### 2. Threat Model Review

Confirm:

- threat model exists or lightweight abuse cases exist
- new risks are reflected
- mitigations are implemented or tracked
- accepted risks are documented

### 3. Access Control Review

Confirm:

- authentication works as intended
- authorization is enforced server-side
- admin paths are protected
- service accounts are least-privilege
- destructive actions are guarded

### 4. Data Protection Review

Confirm:

- sensitive data handling is appropriate
- logs are redacted
- backups are protected
- retention expectations are implemented or tracked
- export/delete needs are addressed where relevant

### 5. Secrets and Configuration Review

Confirm:

- no secrets in source control
- production secrets are stored appropriately
- config is environment-specific
- debug/dev settings are disabled in production
- exposed ports/services are intentional

### 6. Dependency and Supply-Chain Review

Confirm:

- dependency scan is acceptable
- critical/high findings are fixed or accepted
- container/images are from expected sources
- build artifacts are traceable where relevant

### 7. Security Testing Review

Confirm:

- security acceptance criteria passed
- authorization tests passed
- injection/input tests performed where relevant
- audit logging tested
- abuse cases checked

### 8. Monitoring and Incident Readiness

Confirm:

- security-relevant logs exist
- alerts exist for important failures/abuse where relevant
- incident contact/path is known
- rollback/disable process exists
- audit trail captures important actions

### 9. Security Advisory / CSAF-VEX Readiness

For SaaS, security products, developer tools, infrastructure products, libraries/packages, agents, appliances, and enterprise-targeted products, confirm:

- the release has been checked for whether it needs a customer security advisory, vulnerability notice, VEX statement, or trust-center/security-status update
- existing customer-facing security advisories remain accurate after the release
- CSAF/VEX provider readiness is explicitly marked not applicable, deferred, preparing, or publishing
- no CSAF/VEX/OpenVEX/PSIRT/ProductCERT claim is made unless owners, metadata, validation, publication path, and revision/correction process are in place
- `provider-metadata.json`, `security.txt` CSAF links, signing/integrity, schema validation, and advisory storage are checked where the product publishes CSAF/VEX
- tenant/customer confidential information is not exposed in product-wide advisories

Template: `templates/csaf-provider-readiness.md`

### 10. Enterprise Compliance Readiness

For enterprise-targeted products, confirm:

- SOC 2 / ISO/IEC 27001 target status is documented
- control register is current
- evidence register is current
- policy index is current
- security-questionnaire answers are accurate
- customer-facing compliance claims do not overstate reality
- compliance gaps are tracked or explicitly accepted

Guidance: `COMPLIANCE_READINESS_GUIDANCE.md`

### 11. Risk Acceptance

For unresolved risks, capture:

- risk description
- severity/likelihood
- affected users/data
- reason for acceptance
- compensating controls
- owner
- review date
- approving human

## Lightweight Project Version

For small projects:

1. Security checklist
2. Dependency check
3. Secrets/config check
4. Auth/access check
5. CSAF/VEX applicability check where relevant
6. Open risk list
7. Human approval

## Recommended Project Files

- `docs/release/security-gate.md`
- `docs/release/security-checklist.md`
- `docs/release/risk-acceptance.md`
- `docs/release/dependency-review.md`
- `docs/release/csaf-provider-readiness.md` where applicable
- `docs/release/config-review.md`

## Definition of Security-Gate-Ready

A release is ready for security gate review when:

- implementation is complete enough to assess
- QA/security test evidence exists
- open findings are listed
- release scope is clear
- rollback/disable plan exists

## Definition of Security-Gate-Done

The security gate is done when:

- release is approved, blocked, or explicitly deferred
- open risks are accepted or assigned
- approval is recorded
- follow-up security work is in the backlog
