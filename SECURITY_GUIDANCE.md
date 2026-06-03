# Security and Privacy Guidance

Security is a product discipline, not a final boss battle after implementation. This guidance makes security and privacy explicit throughout design, build, release, and operations.

## Purpose

Every serious project should define:

- what must be protected
- who or what it must be protected from
- how access is controlled
- how misuse is detected
- how incidents are handled
- what security risks are accepted

## Minimum Security Expectations

At minimum, capture:

1. Data classification
2. Threat model or abuse-case list
3. Authentication/authorization model
4. Secrets handling
5. Logging/audit expectations
6. Dependency/supply-chain posture
7. Security acceptance criteria
8. Release security review

## Full Security Process Checklist

### 1. Asset and Data Inventory

Identify what matters.

Capture:

- sensitive data
- credentials/secrets
- privileged actions
- business-critical workflows
- administrative interfaces
- external integrations
- generated artifacts

### 2. Data Classification and Flows

Map where data goes.

Capture:

- data sources
- storage locations
- processing steps
- transmission paths
- third-party processors
- retention/deletion expectations
- trust boundaries

### 3. Threat Modeling

Identify plausible threats.

Consider:

- spoofing
- tampering
- repudiation
- information disclosure
- denial of service
- privilege escalation
- abuse cases specific to the product
- insider misuse
- automation misuse

### 4. Identity and Access Management

Define access deliberately.

Capture:

- authentication methods
- roles and permissions
- admin privileges
- service accounts
- API keys/tokens
- approval flows
- access review expectations

### 5. Network and Boundary Security

Apply zero-trust thinking where appropriate.

Capture:

- ingress points
- egress needs
- service-to-service access
- network segmentation
- TLS expectations
- exposed ports/services
- internal trust assumptions

### 6. Secure Data Handling

Define protections for data.

Capture:

- encryption in transit
- encryption at rest where relevant
- sensitive field handling
- masking/redaction
- safe logging
- backup protection
- deletion/export handling

### 7. Secrets Management

Secrets should not become folklore.

Capture:

- where secrets live
- rotation process
- local development handling
- CI/CD handling
- production access
- emergency revocation

### 8. Supply-Chain Security

Capture:

- dependency sources
- update process
- vulnerability scanning
- lockfiles/pinning
- container/image provenance
- SBOM needs
- review process for risky packages

### 9. Secure Coding and Review

Define implementation expectations.

Include:

- input validation
- output encoding
- authorization checks
- CSRF/session protections where relevant
- safe file handling
- safe command execution
- injection prevention
- error handling
- security-focused code review

### 10. Audit and Detection

Define what must be visible later.

Capture:

- audit events
- security logs
- admin actions
- automated actions
- approval records
- anomaly indicators
- alert thresholds

### 11. Privacy Review

Capture:

- data minimization
- retention
- consent/legal basis where relevant
- user visibility/control
- third-party sharing
- privacy-safe analytics
- privacy risks and mitigations

### 12. Security Advisory and CSAF/VEX Readiness

For SaaS, security products, developer tools, infrastructure products, libraries/packages, agents, appliances, and enterprise-targeted products, decide whether the product must ingest machine-readable or vendor-published security advisories from its own vendors and dependencies, publish machine-readable security advisories about itself, or both.

Capture:

- whether CSAF/VEX advisory readiness applies, is deferred, ingest-only, provider-only, or both ingesting and publishing
- human-readable trust/security posture that should exist before machine-readable advisory claims
- vendor/dependency advisory sources, owners, polling/monitoring approach, and failure handling
- advisory-to-product mapping across vendors, dependencies, SBOM components, services, environments, versions, and customer-impact categories
- vulnerability intake, triage, remediation, approval, and publication owners
- advisory ingestion and issuance policy: what inbound advisories trigger triage, VEX/not-affected decisions, mitigations, release holds, CSAF advisories, VEX statements, corrections, withdrawals, or customer notices
- `provider-metadata.json`, `security.txt`, signing/integrity, hosting, retention, and revision-history expectations where applicable
- schema validation and sample advisory evidence before claiming CSAF/VEX ingestion or publication support
- separation between product-wide advisories and tenant/customer confidential information

Use `templates/csaf-vex-advisory-readiness.md` when this applies. Do not claim CSAF, VEX, OpenVEX, PSIRT, ProductCERT, or machine-readable advisory ingestion/publication support until the process, sources, metadata, validation, owners, intake path, and publication path exist where applicable.

### 13. Security Acceptance Criteria

Examples:

- Role-restricted endpoints reject unauthorized access server-side.
- Destructive actions require confirmation and are audited.
- Secrets are not stored in source control or logs.
- Sensitive fields are redacted from diagnostic output.
- Dependency scanning has no unresolved critical findings unless explicitly accepted.

## Lightweight Project Version

For small projects:

1. Sensitive data list
2. Abuse-case list
3. Auth/access note
4. Secrets/logging note
5. Dependency scan/check
6. CSAF/VEX applicability note for SaaS, security, infrastructure, developer-tool, library/package, or enterprise-targeted products
7. Security acceptance criteria
8. Human approval for accepted risks

## Recommended Project Files

- `docs/security/data-classification.md`
- `docs/security/data-flows.md`
- `docs/security/threat-model.md`
- `docs/security/access-control.md`
- `docs/security/secrets-management.md`
- `docs/security/audit-logging.md`
- `docs/security/privacy-review.md`
- `docs/security/security-acceptance-criteria.md`
- `docs/security/csaf-vex-advisory-readiness.md` where applicable
- `docs/security/risk-acceptance.md`

## Definition of Security-Ready

A project is security-ready for build when:

- assets and data are identified
- threat model or abuse cases exist
- access model is defined
- secrets/logging/dependency expectations are known
- security acceptance criteria exist
- significant risks are reviewed

## Definition of Security-Done

Security is done for release when:

- security acceptance criteria pass
- high-risk findings are fixed or accepted
- audit/logging is in place
- secrets and config are reviewed
- release gate approval is recorded
- post-launch security monitoring and maintenance are planned

## Digital Estate Management Security and Privacy, Where Applicable

Digital Estate Management features need explicit security and privacy review because they often touch access paths, trusted contacts, family members, private communications, financial assets, crypto, identity, and death/incapacity workflows.

Required review topics include:

- separation of asset inventory metadata, disposition instructions, and raw secrets
- whether the product is explicitly designed to store credentials, keys, seed phrases, recovery codes, or private instructions
- strong authentication and MFA for ordinary and delegated access
- consent, legal authority, and trusted-contact boundaries
- notification, delay, revocation, and audit controls for emergency or survivor workflows
- export controls and audit evidence
- private communications, sensitive media, and third-party data handling
- safeguards against impersonation-by-design
- language that avoids terms-of-service bypass advice or overpromised provider cooperation
- high-risk warnings for crypto, private keys, recovery codes, hardware wallets, irreversible transfers, and platform-locked property

The default stance is: an inventory is not a password dump. If a product stores secrets, it needs a vault-grade design and explicit approval for that scope.

Guidance: `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`
