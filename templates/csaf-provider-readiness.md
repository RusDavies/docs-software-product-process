# CSAF / VEX Provider Readiness Checklist

Use this when a SaaS, security product, developer tool, infrastructure product, or enterprise-targeted product may need to publish machine-readable security advisories about itself.

This checklist does **not** mean the product is CSAF-ready by default. It forces an explicit decision before making customer-facing claims. Standards cosplay is still cosplay, only with JSON schemas.

## Applicability Decision

- Product:
- Owner:
- Date:
- Decision: Not applicable / Defer / Prepare / Publish
- Rationale:

CSAF/VEX provider readiness is usually relevant when the product:

- is a SaaS, hosted service, infrastructure product, security product, developer platform, library/package, appliance, agent, or customer-integrated tool;
- may need to notify customers about vulnerabilities affecting the product;
- has enterprise customers that expect machine-readable security advisories;
- publishes SBOMs or vulnerability exploitability statements;
- operates a PSIRT/ProductCERT-style process; or
- makes trust-center, security-status, or vendor-risk claims that customers may ingest programmatically.

## Minimum Human-Readable Posture First

Before publishing CSAF/VEX, confirm the product has:

- [ ] Security contact or vulnerability reporting path
- [ ] Human-readable security/trust posture page or packet
- [ ] Incident/customer-notification posture
- [ ] Vulnerability intake and triage owner
- [ ] Patch/remediation decision owner
- [ ] Customer-facing claims review process
- [ ] Current limitations documented without overclaiming

## CSAF Provider Readiness

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

- [ ] Advisory publication does not leak tenant/customer/confidential information
- [ ] Draft advisories are access-controlled until approved
- [ ] Advisory publication is logged/audited
- [ ] Advisory corrections and revisions are tracked
- [ ] Emergency publishing path exists without bypassing approval entirely
- [ ] Support/security teams know where customers will find advisories
- [ ] Release/security gates check whether advisories need to be published or updated
- [ ] Backlog tracks missing provider-readiness work before claims are made

## Release Gate Questions

Before each release of an applicable product, ask:

1. Does this release fix, introduce, or materially change a security vulnerability?
2. Does any dependency/component vulnerability require a VEX statement?
3. Are existing advisories still accurate after this release?
4. Do security-questionnaire/trust-center answers mention CSAF/VEX? If yes, are they true today?
5. Are advisory URLs, provider metadata, signatures, and schema validation still working?

## Decision Record

- Decision:
- Approved by:
- Date:
- Evidence:
- Follow-up backlog items:
