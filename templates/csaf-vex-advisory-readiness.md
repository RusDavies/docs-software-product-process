# CSAF / VEX Advisory Readiness Checklist

Use this when a SaaS, security product, developer tool, infrastructure product, library/package, appliance, agent, customer-integrated tool, or enterprise-targeted product may need to publish machine-readable security advisories about itself **or ingest machine-readable advisories from its own vendors, suppliers, dependencies, cloud providers, or service providers**.

This checklist does **not** mean the product is CSAF-ready by default. It forces an explicit decision before making customer-facing claims or relying on upstream advisory feeds. Standards cosplay is still cosplay, only with JSON schemas.

## Applicability Decision

- Product:
- Owner:
- Date:
- Decision: Not applicable / Defer / Ingest only / Prepare provider / Publish provider advisories / Both ingest and publish
- Rationale:

CSAF/VEX advisory readiness is usually relevant when the product:

- is a SaaS, hosted service, infrastructure product, security product, developer platform, library/package, appliance, agent, or customer-integrated tool;
- may need to notify customers about vulnerabilities affecting the product;
- consumes vendor, dependency, infrastructure, cloud-provider, appliance, model-provider, or managed-service security advisories;
- has enterprise customers that expect machine-readable security advisories;
- publishes or consumes SBOMs, VEX statements, vulnerability exploitability statements, or vendor-risk evidence;
- operates a PSIRT/ProductCERT-style process; or
- makes trust-center, security-status, compliance, or vendor-risk claims that customers or the product team may ingest programmatically.

## Minimum Human-Readable Posture First

Before publishing or relying on CSAF/VEX, confirm the product has:

- [ ] Security contact or vulnerability reporting path
- [ ] Human-readable security/trust posture page or packet
- [ ] Incident/customer-notification posture
- [ ] Vulnerability intake and triage owner
- [ ] Vendor/dependency advisory intake owner
- [ ] Patch/remediation decision owner
- [ ] Customer-facing claims review process
- [ ] Current limitations documented without overclaiming

## Vendor Advisory Ingestion Readiness

- [ ] Identify advisory sources for critical vendors, suppliers, dependencies, cloud providers, managed services, appliances, models, APIs, and open-source components
- [ ] Record source type for each feed: CSAF, VEX/OpenVEX, OSV, GitHub Security Advisory, vendor RSS/email, trust portal, security bulletin, API, manual portal, or other
- [ ] Define how advisory feeds are discovered, authenticated, fetched, parsed, normalized, validated, and monitored for failure
- [ ] Define how advisories are mapped to product assets, SBOM components, services, environments, versions, tenants, and customer-impact categories
- [ ] Define deduplication, correlation, severity normalization, affected-version matching, and exploitability interpretation rules
- [ ] Define triage SLAs and escalation paths for vendor advisories by severity, exploitability, exposure, and customer impact
- [ ] Define how false positives, not-affected decisions, compensating controls, accepted risks, and VEX conclusions are recorded
- [ ] Define when an inbound vendor advisory triggers a patch, mitigation, customer notice, release hold, emergency release, trust-center update, or outbound advisory
- [ ] Track vendor advisory intake evidence in the risk register, vulnerability register, dependency register, or evidence register
- [ ] Review critical vendor advisory sources periodically so silent feed breakage does not become the incident response strategy. It is a poor strategy.

## CSAF/VEX Provider Readiness

- [ ] Decide whether the product should be a CSAF provider now, later, or not at all
- [ ] Define advisory issuance policy: what events trigger a CSAF advisory?
- [ ] Define VEX issuance policy: when will exploitability status be stated?
- [ ] Assign advisory author, reviewer, approver, and publisher roles
- [ ] Define advisory severity, status, remediation, and revision conventions
- [ ] Prepare `provider-metadata.json` ownership and hosting location
- [ ] Decide whether `/.well-known/csaf/provider-metadata.json` will be supported
- [ ] Decide whether `security.txt` will link to CSAF provider metadata
- [ ] Define signing/integrity approach and key custody, if advisories are signed
- [ ] Define advisory storage, retention, correction, and withdrawal process
- [ ] Validate sample CSAF documents against the CSAF 2.0 schema before claiming support
- [ ] Validate sample VEX/OpenVEX statements before claiming support
- [ ] Document customer-facing discovery URL(s)
- [ ] Document unsupported advisory classes explicitly

## Operational Requirements

- [ ] Inbound advisory ingestion failures are detectable and assigned to an owner
- [ ] Inbound advisory triage, not-affected decisions, accepted risks, and remediation actions are logged/audited
- [ ] Advisory publication does not leak tenant/customer/confidential information
- [ ] Draft outbound advisories are access-controlled until approved
- [ ] Outbound advisory publication is logged/audited
- [ ] Advisory corrections and revisions are tracked
- [ ] Emergency intake, triage, mitigation, and publishing paths exist without bypassing approval entirely
- [ ] Support/security teams know where customers will find outbound advisories and where internal teams find inbound vendor-advisory status
- [ ] Release/security gates check whether inbound vendor advisories require a patch, mitigation, VEX decision, customer notice, or outbound advisory update
- [ ] Backlog tracks missing advisory-readiness work before claims are made or vendor feeds are relied upon

## Release Gate Questions

Before each release of an applicable product, ask:

1. Does this release fix, introduce, or materially change a security vulnerability?
2. Have relevant vendor, supplier, dependency, cloud-provider, managed-service, model-provider, and open-source advisories been checked for affected components or services?
3. Does any dependency/component vulnerability require a VEX statement, not-affected rationale, mitigation, patch, customer notice, or release hold?
4. Are existing customer-facing advisories still accurate after this release?
5. Do security-questionnaire/trust-center answers mention CSAF/VEX or machine-readable advisory ingestion/publication? If yes, are they true today?
6. Are inbound advisory sources, parsing/validation paths, advisory URLs, provider metadata, signatures, and schema validation still working where applicable?

## Decision Record

- Decision:
- Approved by:
- Date:
- Evidence:
- Follow-up backlog items:
