# Engineering Principles

These principles are baseline defaults for workspace software projects. They are not magic commandments carved into a cloud architecture diagram. Projects may tailor or deviate from them, but meaningful deviations should be explicit and justified.

## Purpose

The principles give every project a shared engineering posture:

- secure by default
- private by design
- observable
- automatable
- maintainable
- resilient
- reproducible
- humane to operate

## Principle 1: Security by Default

Systems should start from safe defaults.

Expectations:

- deny by default
- least privilege
- private by default
- explicit opt-in for risky behavior
- secure configuration defaults
- safe handling of errors and partial failures
- no secrets in code, logs, screenshots, or tickets
- authorization checks on meaningful actions, not just pages

Useful questions:

- What happens if a user, service, or dependency is malicious?
- What is the safest default state?
- Can a low-privilege actor escalate access?
- Are risky features explicit and auditable?

## Principle 2: Privacy by Design

Collect, retain, expose, and log the minimum data needed.

Expectations:

- data classification for meaningful data stores
- minimum necessary collection
- retention expectations
- privacy-safe logging
- clear user/admin visibility where appropriate
- export/deletion needs identified early
- consent/legal basis considered where relevant

Useful questions:

- What sensitive data exists?
- Why do we need it?
- How long do we keep it?
- Who can see it?
- Where could it leak accidentally?

## Principle 3: Zero-Trust Networking Where Appropriate

Do not treat “inside the network” as a security model.

Expectations:

- authenticate meaningful boundaries
- authorize service-to-service access
- limit lateral movement
- use explicit ingress and egress rules
- segment sensitive components
- avoid broad internal trust
- log security-relevant access

Useful questions:

- What are the trust boundaries?
- What happens if one service is compromised?
- Can this component talk to more things than it needs?
- Is internal traffic authenticated and authorized where risk justifies it?

## Principle 4: 12-Factor Design Where Appropriate

Use 12-factor app practices when they fit the product and deployment model.

Expectations:

- codebase is versioned and reproducible
- dependencies are explicit
- configuration is separated from code
- backing services are attached resources
- build, release, and run stages are separated where useful
- processes are stateless where practical
- logs are treated as event streams
- runtime instances are disposable/recreatable
- dev/prod parity is maintained where sensible

Useful questions:

- Can a new environment be created without archaeology?
- Are config and secrets externalized?
- Can instances be replaced safely?
- Are logs useful outside the process that produced them?

## Principle 5: Operational Automation by Default

Systems should be designed to operate with minimal routine human intervention. The ideal operating model is that normal monitoring, recovery, maintenance, reporting, and routine administration are automated, with humans involved mainly for exceptions, approvals, ambiguous judgment calls, incidents, and product direction.

The design test: could one competent operator oversee 50 similar projects without becoming a tragic cautionary tale?

Expectations:

- health checks and readiness checks
- actionable alerts, not noise confetti
- self-healing where safe
- automated backups and restore validation where relevant
- automated dependency/security checks
- automated housekeeping and retention jobs
- automated reporting for routine status
- runbooks encoded into automation where safe
- exception-based human attention
- approval gates for high-risk automation
- audit trails for automated actions

Useful questions:

- What routine operations can the system handle itself?
- What requires human judgment?
- What can safely self-heal?
- What alerts are actionable?
- How does automation fail safely?
- How is automated behavior audited and constrained?

## Principle 6: Observability from the Start

A system that cannot explain what it is doing is not production-ready; it is a séance with TCP ports.

Expectations:

- structured logs
- useful metrics
- health/readiness checks
- traceability for critical paths where useful
- audit trails for meaningful user/admin/security actions
- dashboards or status checks for operated systems
- clear distinction between diagnostic logs and sensitive content

Useful questions:

- How will we know it is healthy?
- How will we debug failure?
- What should alert a human?
- What must be auditable?
- What must never be logged?

## Principle 7: Resilience and Graceful Degradation

Systems should fail predictably and recoverably.

Expectations:

- clear failure modes
- bounded retries with backoff
- no silent data loss
- idempotency where useful
- safe partial success behavior
- rollback/disable paths for risky features
- backup and restore expectations where relevant
- user-visible recovery guidance

Useful questions:

- What breaks when a dependency is down?
- Can work be retried safely?
- Can the system degrade instead of collapse?
- How do users and operators recover?

## Principle 8: Supply-Chain Hygiene

Dependencies and build artifacts are part of the product.

Expectations:

- explicit dependencies
- dependency update process
- vulnerability scanning for serious projects
- pinned versions where appropriate
- provenance for containers/artifacts where relevant
- SBOM or equivalent for serious production systems
- review of risky transitive dependencies

Useful questions:

- What third-party code are we trusting?
- How do we know when it becomes vulnerable?
- Can builds be reproduced?
- Are images/artifacts traceable?

## Principle 9: Portability and Reproducibility

Projects should be understandable and recreatable.

Expectations:

- documented local setup
- deterministic build steps where practical
- environment assumptions documented
- migrations scripted
- infrastructure assumptions recorded
- Podman-friendly container/runtime guidance by default unless a project needs Docker specifically

Useful questions:

- Can a new developer/operator run this from the docs?
- Can a dead environment be recreated?
- Are assumptions written down or stored in someone’s doomed mammal brain?

## Principle 10: Human Control for High-Risk Actions

Automation should reduce toil, not quietly become the product owner, legal department, and chaos monkey.

Expectations:

- destructive actions require confirmation or policy approval
- irreversible actions have explicit safeguards
- external/public actions require clear authorization
- high-risk security actions are audited
- production-affecting automation has constrained permissions
- humans retain product direction and prioritization

Useful questions:

- What actions need approval?
- What actions need rollback?
- What decisions must remain human?
- What evidence is recorded when automation acts?

## Definition of Principle-Ready

A project is principle-ready when:

- applicable principles are identified
- deviations are documented
- security/privacy/operations implications are understood
- principle-driven requirements are captured
- high-risk tradeoffs are approved by the right human

## Definition of Principle-Done

A project is principle-done when:

- implemented behavior reflects the selected principles
- deviations remain documented and accepted
- verification covers principle-driven requirements
- operational automation and observability are working where required
- follow-up improvements are tracked in the backlog
