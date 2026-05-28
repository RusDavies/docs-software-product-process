# Digital Estate Guidance

Digital estate guidance defines the owned and depended-on assets that must be known, renewed, secured, transferred, or retired for a product to keep operating.

## Purpose

Every operated product should maintain an estate view covering:

- domains and DNS
- certificates and renewal paths
- repositories, package registries, artifact stores, and release accounts
- cloud accounts, SaaS tenants, identity providers, and admin consoles
- environments, deployment targets, and infrastructure ownership
- secrets, keys, service accounts, and privileged credentials
- databases, object stores, backup locations, and retention/deletion duties
- third-party services, billing owners, contracts, and support contacts
- access review, handover, and decommissioning expectations

Class 0 throw-away/disposable work is exempt from digital estate management by default. If the work has domains, DNS, certificates, repositories that must persist, release accounts, cloud/SaaS tenants, long-lived credentials, persistent data stores, billing dependencies, or external integrations, the throw-away classification is probably wrong and should be escalated or explicitly risk-accepted by the product owner.

If nobody can answer “what do we own, where does it run, who pays for it, who can access it, and what expires next?”, the product is not operationally mature. It is just vibing in production, which is adorable until it becomes expensive.

## Minimum Expectations

At minimum, capture:

1. Owner for the estate register
2. Domains/DNS/certificates
3. Repositories and release/distribution accounts
4. Runtime environments and deployment targets
5. Cloud/SaaS/admin accounts
6. Data stores and backup locations
7. Secrets/service accounts and credential owners
8. External dependencies and billing/support owners
9. Renewal and access review cadence
10. Decommissioning notes

## Full Digital Estate Checklist

### 1. Ownership and Register Maintenance

Capture:

- estate register owner
- review cadence
- approval path for adding/removing estate items
- handover process
- stale item cleanup process

### 2. Domains, DNS, and Certificates

Capture:

- domains and registrars
- DNS zones and providers
- certificate providers and renewal automation
- expiration dates and alerting
- ownership and emergency access path

### 3. Source, Build, and Release Estate

Capture:

- source repositories
- CI/CD systems
- package registries and publishing accounts
- container/image registries
- artifact stores
- signing keys and release credentials
- release authority and approval boundaries

### 4. Runtime and Infrastructure Estate

Capture:

- cloud accounts, subscriptions, and projects
- infrastructure providers
- environments: dev, test, staging, production, demo, support
- deployment targets
- network boundaries and ingress/egress dependencies
- infrastructure-as-code locations
- privileged administrative consoles

### 5. Identity, Access, and Secrets

Capture:

- identity providers and SSO groups
- administrative users and roles
- service accounts
- API keys, tokens, certificates, and secrets
- secret storage locations
- rotation cadence
- access review cadence
- emergency access process

### 6. Data, Backup, and Retention Estate

Capture:

- databases
- object/file stores
- analytics stores
- logs and audit stores
- backup locations
- restore owners
- retention/deletion requirements
- sensitive data classifications

### 7. Third-Party Services and Commercial Dependencies

Capture:

- SaaS dependencies
- external APIs
- payment/billing owners
- contracts and renewal dates
- support contacts
- criticality and substitution options
- customer/security questionnaire implications

### 8. Decommissioning

Capture:

- shutdown criteria
- data export/deletion steps
- credential revocation
- DNS/certificate cleanup
- repository/archive decisions
- account closure
- customer/user communication where applicable
- final evidence record

## Lightweight Project Version

For small projects:

1. One-page estate register
2. List domains/accounts/repos/environments
3. Note owners and renewal dates
4. Note backup and secret locations
5. Note how to shut it down safely

## Recommended Project Files

- `docs/operations/digital-estate-register.md`
- `docs/architecture/digital-estate.md`
- `docs/operations/maintenance.md`
- `docs/security/access-review.md`
- `docs/operations/decommissioning.md`

## Definition of Estate-Ready

A product is estate-ready when:

- owned accounts, domains, repos, environments, data stores, and dependencies are listed
- owners and renewal obligations are known
- access and secrets are reviewable
- backup/restore and decommissioning responsibilities are known
- critical unknowns are tracked in the backlog

## Definition of Estate-Done

Estate management is never truly done. For a release, it is done when:

- the register is current enough for another competent operator to take over
- expiration/renewal risks are visible
- access review and credential rotation expectations are documented
- new estate items introduced by the release are captured
