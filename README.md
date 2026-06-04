# Guidance Docs

Workspace guidance for taking software products from idea to operation without skipping the thinking that prevents expensive stupidity later.

The guidance is modular. The top-level process explains the flow; each sub-document expands one discipline or checkpoint. Small projects can use the lightweight versions. Serious, public, security-sensitive, multi-user, enterprise-targeted, regulated, or production projects should treat the full guidance as required gates.

Start here instead of reading everything like a doomed compliance intern:

1. Classify the project with `TAILORING_GUIDE.md`.
2. Select any target profile, such as software library/package, that changes which process parts apply.
3. Follow the lifecycle spine in `SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md`.
4. Use the relevant discipline guide when that phase becomes active.
5. Copy starter artifacts from `templates/` when useful.
6. Use `GOVERNANCE_AND_APPROVALS.md` when decisions, approvals, risk acceptance, releases, or agent boundaries matter.
7. Use `OBSERVABILITY_DEBUGGABILITY_GUIDANCE.md` when operators, support staff, or incident teams need to understand failures and product health.
8. Use `PRODUCT_OPERATIONAL_ESTATE_GUIDANCE.md` and `AI_AGENT_OPERATION_GUIDANCE.md` when the product needs a clear operating footprint or may be operated with approved AI-agent assistance.
9. Use `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md` when a product has non-corporate end users whose digital assets, accounts, memories, identity, access paths, or death/incapacity instructions may matter.

## Quick Start by Project Size

### Throw-Away / Disposable

Use only when the product owner explicitly says the work is disposable and accepts that it will not receive normal maintenance, product operational estate management, or AI-agent operation readiness. If it is deployable, exposed, shared, depended upon, connected to external systems, stores data, uses credentials, costs money, or will survive beyond the experiment, it is not throw-away unless that risk is explicitly accepted.

Class 0 keeps only the small safety wrapper: disposable-work statement, owner approval, delete/rebuild expectation, basic safety/privacy check, no long-lived secrets/data/exposure/cost check, and smoke-test or inspection evidence. Long-term product machinery such as operations runbooks, estate registers, monitoring, backup/restore plans, compliance readiness, SEO, formal documentation QA, support processes, maintenance schedules, and AI-agent operation design is excluded by default.

### Tiny / Personal

Use:

- `TAILORING_GUIDE.md`
- lightweight sections from the relevant guidance docs
- direct smoke test or inspection evidence

Usually enough:

- short problem statement
- TODO/backlog note if follow-up exists
- usage notes
- safety/privacy note if relevant

### Small Internal Tool

Use:

- `TAILORING_GUIDE.md`
- `PRODUCT_FRAMING_GUIDANCE.md`
- `REQUIREMENTS_GUIDANCE.md`
- `ARCHITECTURE_GUIDANCE.md`
- `IMPLEMENTATION_GUIDANCE.md`
- `QA_GUIDANCE.md`
- selected templates

Add `GOVERNANCE_AND_APPROVALS.md` if the tool touches external systems, shared users, sensitive data, destructive actions, or release approval.

### Software Library / Package

Use the software-library target profile in `TAILORING_GUIDE.md` for reusable libraries, SDKs, framework modules, or packages that other software consumes but that do not themselves run as operated services.

Libraries keep the security, compatibility, test, documentation, release, provenance, maintainer, vulnerability-intake, and security-patching parts of the process. They exclude normal runtime operations machinery by default: no operations runbook, monitoring/alerting, backup/restore plan, runtime incident process, or AI-agent runtime-operation design unless the library also ships an operated service, daemon, scheduled job, data store, telemetry backend, update service, or other runtime component.

### Serious / Production / Public / Regulated Product

Use the full lifecycle:

- `SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md`
- `ENGINEERING_PRINCIPLES.md`
- all relevant discipline guides
- `RELEASE_SECURITY_GATE.md`
- `GOVERNANCE_AND_APPROVALS.md`
- templates for evidence and approvals

### Enterprise-Targeted Product

If the product targets enterprise customers, assume SOC 2, ISO/IEC 27001, vendor-risk review, and security questionnaires will become part of the sales and trust path.

Add:

- `COMPLIANCE_READINESS_GUIDANCE.md`
- compliance templates from `templates/`
- control/evidence/policy tracking before customer pressure turns into archaeology with deadlines

## Core Documents

### Start / Navigation

- `TAILORING_GUIDE.md` — classify project risk and choose the right amount of process
- `SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md` — high-level process and phase gates
- `ENGINEERING_PRINCIPLES.md` — baseline engineering, security, privacy, and operations principles
- `GOVERNANCE_AND_APPROVALS.md` — human approval boundaries, accepted-risk rules, and agent autonomy limits

### Product, Design, Documentation, and SEO

- `PRODUCT_FRAMING_GUIDANCE.md` — opportunity framing and problem definition
- `REQUIREMENTS_GUIDANCE.md` — product, functional, non-functional, security, and operational requirements
- `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md` — user-facing Digital Estate Management for personal/family assets, legacy access, and death/incapacity planning
- `UX_GUIDANCE.md` — UX design process, trust UX, accessibility, validation, and UX readiness
- `DOCUMENTATION_GUIDANCE.md` — user, admin, operator, developer, release, and documentation QA expectations
- `SEO_GUIDANCE.md` — search/discovery, metadata, crawlability, technical SEO, and launch SEO checks for web products

### Security, Compliance, Architecture, and Planning

- `SECURITY_GUIDANCE.md` — canonical security and privacy design process
- `COMPLIANCE_READINESS_GUIDANCE.md` — SOC 2, ISO/IEC 27001, enterprise questionnaire, control, and evidence readiness
- `ARCHITECTURE_GUIDANCE.md` — technical architecture and system design
- `OBSERVABILITY_DEBUGGABILITY_GUIDANCE.md` — operator visibility, diagnostics, failure reconstruction, and incident evidence design
- `IMPLEMENTATION_PLANNING_GUIDANCE.md` — milestones, backlog breakdown, and delivery planning
- `PRODUCT_OPERATIONAL_ESTATE_GUIDANCE.md` — product/operator estate: domains, accounts, environments, credentials, dependencies, renewals, ownership, and decommissioning
- `AI_AGENT_OPERATION_GUIDANCE.md` — safe, auditable, least-privilege operation by approved AI agents

### Build, Verify, Release, Operate

- `IMPLEMENTATION_GUIDANCE.md` — build guidance and coding expectations
- `QA_GUIDANCE.md` — verification, testing, and quality gates
- `RELEASE_SECURITY_GATE.md` — explicit security review before release
- `RELEASE_GUIDANCE.md` — launch/release checklist and rollback readiness
- `OPERATIONS_GUIDANCE.md` — post-launch operations, automation, maintenance, and incident handling

## Templates

Starter artifacts live in `templates/`:

- `templates/product-brief.md`
- `templates/requirements-spec.md`
- `templates/architecture-overview.md`
- `templates/risk-register.md`
- `templates/threat-model.md`
- `templates/qa-plan.md`
- `templates/release-checklist.md`
- `templates/operations-runbook.md`
- `templates/observability-debuggability-plan.md`
- `templates/product-operational-estate-register.md`
- `templates/digital-estate-management-requirements.md`
- `templates/digital-estate-user-inventory.md`
- `templates/agent-operation-boundaries.md`
- `templates/decision-record.md`
- `templates/control-register.md`
- `templates/evidence-register.md`
- `templates/policy-index.md`
- `templates/soc2-iso27001-crosswalk.md`
- `templates/audit-readiness-checklist.md`
- `templates/security-questionnaire.md`
- `templates/csaf-vex-advisory-readiness.md`
- `templates/user-guide.md`
- `templates/admin-guide.md`
- `templates/quick-start.md`
- `templates/configuration-guide.md`
- `templates/troubleshooting-guide.md`
- `templates/documentation-plan.md`
- `templates/documentation-qa-checklist.md`
- `templates/seo-plan.md`
- `templates/page-inventory.md`
- `templates/metadata-plan.md`
- `templates/technical-seo-checklist.md`
- `templates/launch-seo-checklist.md`
- `templates/post-launch-seo-review.md`

Templates are deliberately plain Markdown. Copy them into a project and delete what does not apply. The punishment for using every section blindly is owning the resulting bureaucracy.

## Canonical Source Rules

Some topics appear in multiple documents because they matter in multiple phases. To avoid drift:

- Security/privacy design source of truth: `SECURITY_GUIDANCE.md`
- Release security decision source of truth: `RELEASE_SECURITY_GATE.md`
- Enterprise compliance readiness source of truth: `COMPLIANCE_READINESS_GUIDANCE.md`
- User/admin/operator documentation source of truth: `DOCUMENTATION_GUIDANCE.md`
- Web SEO/discovery source of truth: `SEO_GUIDANCE.md`
- Operational ownership and runbooks source of truth: `OPERATIONS_GUIDANCE.md`
- Observability/debuggability source of truth: `OBSERVABILITY_DEBUGGABILITY_GUIDANCE.md`
- Product operational estate ownership and renewal source of truth: `PRODUCT_OPERATIONAL_ESTATE_GUIDANCE.md`
- User-facing Digital Estate Management source of truth: `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`
- AI-agent operational boundary source of truth: `AI_AGENT_OPERATION_GUIDANCE.md`
- Overall lifecycle source of truth: `SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md`
- Project-class/tailoring source of truth: `TAILORING_GUIDE.md`
- Approval and agent-boundary source of truth: `GOVERNANCE_AND_APPROVALS.md`

Other documents may include phase-specific checkpoints, but should not redefine those policies in incompatible ways.

## Terminology Guardrails

- **Digital Estate Management** means user-facing planning for personal/family digital assets, legacy access, trusted people, and death/incapacity instructions.
- **Product Operational Estate Management** means operator-facing continuity for the product itself: domains, DNS, certificates, repositories, cloud/SaaS accounts, secrets, billing, backups, handover, and decommissioning.
- **CSAF/VEX Advisory Readiness** means the product has explicitly decided whether it must ingest machine-readable or vendor-published security advisories from its own vendors, suppliers, dependencies, cloud providers, managed services, model providers, or open-source components, and whether it will publish machine-readable security advisories about itself. Where applicable, it has owners, sources, mapping, triage, validation, signing/integrity, publication, correction, and customer-claim evidence to support that.
- **Digital Asset Management / DAM** means corporate/media/content asset-library management: reusable files, brand assets, approvals, licensing, distribution, and content governance.

## Operating Model

Security, privacy, accessibility, observability, maintainability, product operational estate stewardship, AI-agent operability by default unless explicitly throw-away or product-owner exempted, and automated operations are first-class concerns. They appear both as dedicated documents and as checkpoints throughout the process.

The desired end state is boring software: understandable, secure by default, observable, recoverable, and automated enough that one competent operator could oversee many projects without living inside a pager-shaped coffin.
