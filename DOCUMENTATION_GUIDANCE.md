# Documentation Guidance

Documentation is part of the product. If users cannot understand, configure, recover from, or safely operate the thing, the product is not done; it is merely code with an alibi.

## Purpose

This guidance covers documentation for:

- end users
- administrators
- operators
- support teams
- developers/integrators
- enterprise buyers and security reviewers, where relevant

It makes user and operator documentation explicit release artifacts, not optional debris generated after everyone is tired.

## Minimum Expectations

At minimum, define:

1. Documentation audience(s)
2. Required user-facing docs
3. Required admin/operator docs
4. Setup/configuration instructions
5. Troubleshooting and recovery guidance
6. Security/privacy/safety notes users need to know
7. Release notes or change summary
8. Documentation owner and maintenance path
9. Documentation QA/sign-off before release

## Full Documentation Checklist

### 1. Audience and Scope

Capture:

- end users
- admins
- operators
- support users
- developers/integrators
- security/compliance reviewers
- accessibility needs
- technical comfort level
- documentation locations
- versioning expectations

### 2. User Documentation

For user-facing products, provide enough documentation for users to succeed without private archaeology.

Capture:

- product overview
- getting started / quick start
- core workflows
- feature explanations
- account/profile/settings guidance
- permissions and roles visible to users
- common errors and recovery
- limitations and known constraints
- data/security/privacy implications users should understand
- FAQ or help topics where useful

### 3. Admin Documentation

For products with administrative roles, document:

- admin responsibilities
- setup and configuration
- user/role management
- permission model
- integration setup
- data import/export
- policy controls
- audit/log access
- backup/restore expectations where admin-visible
- safe destructive actions
- escalation paths

### 4. Operator Documentation

For operated systems, document:

- system overview
- deployment/run model
- configuration
- health checks
- monitoring and alerts
- routine maintenance
- backup and restore
- incident response
- rollback/disable procedure
- common failures, diagnostics, and remediation
- automation boundaries
- support handoffs

Operator docs should align with `OPERATIONS_GUIDANCE.md`.

### 5. Developer / Integrator Documentation

For APIs, SDKs, plugins, extensions, integrations, or installable components, document:

- local setup
- authentication
- API contracts
- examples
- errors and rate limits
- versioning and compatibility
- security requirements
- test/sandbox environment
- migration notes

### 6. Security, Privacy, and Trust Documentation

Document what users, admins, and customers need to know about:

- data collected and processed
- retention and deletion behavior
- encryption/security posture at the right level
- access control
- audit logging
- risky/destructive actions
- AI/automation limitations where applicable
- compliance status without overclaiming
- responsible disclosure/security contact where relevant

For enterprise-targeted products, align customer-facing claims with `COMPLIANCE_READINESS_GUIDANCE.md`.

### 7. In-Product Help and Content

Where useful, define:

- empty states
- error messages
- onboarding text
- tooltips/help text
- confirmation dialogs
- safe next actions
- links to docs
- accessibility of help content

This overlaps with `UX_GUIDANCE.md`; the documentation source should not contradict the product interface.

### 8. Release Notes and Change Communication

For releases, document:

- what changed
- who is affected
- migration or configuration steps
- new risks or limitations
- deprecations/removals
- known issues
- rollback/disable notes where relevant
- support path

### 9. Documentation QA

Before release, verify:

- instructions match the product
- setup/configuration steps work
- screenshots/examples are current where used
- links work
- terminology is consistent
- security/privacy claims are accurate
- accessibility basics are met
- operator runbooks match real procedures and diagnostic paths
- release notes match the release

Docs that confidently explain the wrong product are worse than no docs. At least no docs are honest about being useless.

### 10. Maintenance

Define:

- documentation owner
- update trigger for product changes
- review cadence
- docs backlog process
- stale-doc detection method
- versioning/archive approach where needed

## Lightweight Project Version

For small projects:

1. README / overview
2. quick start
3. configuration notes
4. common troubleshooting
5. security/privacy caveats where relevant
6. operator/run notes if anyone other than the author will run it
7. release/change note if shared

## Recommended Project Files

- `docs/user/user-guide.md`
- `docs/user/quick-start.md`
- `docs/user/troubleshooting.md`
- `docs/admin/admin-guide.md`
- `docs/admin/configuration.md`
- `docs/operations/runbook.md`
- `docs/developer/api-or-integration-guide.md`
- `docs/release/release-notes.md`
- `docs/documentation/documentation-plan.md`
- `docs/documentation/documentation-qa-checklist.md`

## Definition of Documentation-Ready

Documentation is ready for implementation/release planning when:

- audiences are identified
- required docs are listed
- documentation owners are assigned
- documentation acceptance criteria exist
- security/privacy/compliance claims needing approval are identified

## Definition of Documentation-Done

Documentation is done when:

- required user/admin/operator docs exist
- setup/configuration/troubleshooting instructions have been checked
- release notes are prepared where needed
- documentation QA has passed or exceptions are approved
- known documentation gaps are in the backlog
- docs match the product closely enough that support does not need to perform interpretive dance
