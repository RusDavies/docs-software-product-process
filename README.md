# Guidance Docs

Workspace guidance for taking software products from idea to operation without skipping the thinking that prevents expensive stupidity later.

The guidance is modular. The top-level process explains the flow; each sub-document expands one discipline or checkpoint. Small projects can use the lightweight versions. Serious, public, security-sensitive, multi-user, enterprise-targeted, regulated, or production projects should treat the full guidance as required gates.

Start here instead of reading everything like a doomed compliance intern:

1. Classify the project with `TAILORING_GUIDE.md`.
2. Follow the lifecycle spine in `SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md`.
3. Use the relevant discipline guide when that phase becomes active.
4. Copy starter artifacts from `templates/` when useful.
5. Use `GOVERNANCE_AND_APPROVALS.md` when decisions, approvals, risk acceptance, releases, or agent boundaries matter.
6. Use `DIGITAL_ESTATE_GUIDANCE.md` and `AI_AGENT_OPERATION_GUIDANCE.md` when the product needs a clear operating footprint or may be operated with approved AI-agent assistance.

## Quick Start by Project Size

### Throw-Away / Disposable

Use only when the product owner explicitly says the work is disposable and accepts that it will not receive normal maintenance or AI-agent operation readiness. If it is deployable, exposed, shared, depended upon, connected to external systems, stores data, uses credentials, costs money, or will survive beyond the experiment, it is not throw-away unless that risk is explicitly accepted.

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
- `UX_GUIDANCE.md` — UX design process, trust UX, accessibility, validation, and UX readiness
- `DOCUMENTATION_GUIDANCE.md` — user, admin, operator, developer, release, and documentation QA expectations
- `SEO_GUIDANCE.md` — search/discovery, metadata, crawlability, technical SEO, and launch SEO checks for web products

### Security, Compliance, Architecture, and Planning

- `SECURITY_GUIDANCE.md` — canonical security and privacy design process
- `COMPLIANCE_READINESS_GUIDANCE.md` — SOC 2, ISO/IEC 27001, enterprise questionnaire, control, and evidence readiness
- `ARCHITECTURE_GUIDANCE.md` — technical architecture and system design
- `IMPLEMENTATION_PLANNING_GUIDANCE.md` — milestones, backlog breakdown, and delivery planning
- `DIGITAL_ESTATE_GUIDANCE.md` — domains, accounts, environments, credentials, dependencies, renewals, ownership, and decommissioning
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
- `templates/digital-estate-register.md`
- `templates/agent-operation-boundaries.md`
- `templates/decision-record.md`
- `templates/control-register.md`
- `templates/evidence-register.md`
- `templates/policy-index.md`
- `templates/soc2-iso27001-crosswalk.md`
- `templates/audit-readiness-checklist.md`
- `templates/security-questionnaire.md`
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
- Digital estate ownership and renewal source of truth: `DIGITAL_ESTATE_GUIDANCE.md`
- AI-agent operational boundary source of truth: `AI_AGENT_OPERATION_GUIDANCE.md`
- Overall lifecycle source of truth: `SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md`
- Project-class/tailoring source of truth: `TAILORING_GUIDE.md`
- Approval and agent-boundary source of truth: `GOVERNANCE_AND_APPROVALS.md`

Other documents may include phase-specific checkpoints, but should not redefine those policies in incompatible ways.

## Operating Model

Security, privacy, accessibility, observability, maintainability, digital estate stewardship, AI-agent operability by default unless explicitly throw-away or product-owner exempted, and automated operations are first-class concerns. They appear both as dedicated documents and as checkpoints throughout the process.

The desired end state is boring software: understandable, secure by default, observable, recoverable, and automated enough that one competent operator could oversee many projects without living inside a pager-shaped coffin.
