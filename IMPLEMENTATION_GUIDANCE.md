# Implementation Guidance

Implementation is where product intent becomes code, tests, docs, configuration, and occasionally a grim reminder that computers obey exactly what you typed.

## Purpose

Every project should build in a way that is:

- secure
- tested
- maintainable
- observable
- automatable
- documented
- reviewable

## Minimum Expectations

At minimum, implementation should include:

1. Version-controlled code
2. Clear setup/build instructions
3. Tests for critical behavior
4. Security-conscious coding
5. Configuration separated from code
6. Logging/observability basics
7. Review before release

## Full Implementation Checklist

### 1. Repository Hygiene

Expect:

- clear project structure
- meaningful commits
- branch-per-work-item where appropriate
- no unrelated changes swept into commits
- generated files ignored unless intentional
- secrets excluded

### 2. Code Quality

Expect:

- readable structure
- clear boundaries
- consistent naming
- small focused modules where practical
- error handling
- useful comments for non-obvious decisions
- no cleverness tax without payoff

### 3. Secure Coding

Expect:

- input validation
- output encoding where relevant
- server-side authorization checks
- safe file handling
- safe command/process use
- injection prevention
- secure session/cookie handling where relevant
- safe defaults
- no sensitive logs

### 4. Configuration and Secrets

Expect:

- configuration outside code
- environment/runtime config where appropriate
- documented required settings
- safe defaults
- secrets in approved secret stores or local ignored files
- no secrets committed

### 5. Tests

Expect:

- unit tests for core logic
- integration tests for boundaries
- regression tests for fixed bugs
- security-relevant tests for authorization and validation
- contract tests where useful
- acceptance tests for core workflows where practical

### 6. Observability

Expect:

- structured logs where useful
- health checks
- metrics for critical paths
- audit logs for meaningful actions
- clear error messages without leaking sensitive details

### 7. Operational Automation

Expect:

- automated setup/build/test commands
- migration scripts
- backup/restore hooks where relevant
- scheduled maintenance jobs where needed
- health/readiness endpoints or equivalent
- automation constrained by least privilege

### 8. Documentation

Expect:

- README
- setup instructions
- configuration reference
- user guide or quick start where user-facing
- admin guide where configurable/administered
- operational notes/runbook where operated
- troubleshooting guidance where shared
- security/privacy notes
- architecture notes updated when implementation diverges

Guidance: `DOCUMENTATION_GUIDANCE.md`

### 9. Review

Review should check:

- requirement fit
- UX fit
- security implications
- test coverage
- operational impact
- documentation updates against the documentation plan

## Lightweight Project Version

For small projects:

1. README/setup notes
2. Basic tests or manual verification notes
3. Security/config review
4. Minimal user/operator documentation notes
5. Minimal operational notes
6. Clean git status/commit

## Recommended Project Files

- `README.md`
- `.gitignore`
- `docs/implementation/setup.md`
- `docs/implementation/configuration.md`
- `docs/implementation/security-notes.md`
- `docs/implementation/developer-notes.md`
- `docs/user/quick-start.md`
- `docs/user/troubleshooting.md`
- `docs/documentation/documentation-plan.md`

## Definition of Implementation-Ready

Implementation is ready when:

- requirements and acceptance criteria are known
- architecture is sufficient
- security-sensitive areas are identified
- implementation tasks are broken down
- verification expectations are clear

## Definition of Implementation-Done

Implementation is done when:

- code meets requirements
- tests/checks pass
- security-sensitive behavior is reviewed
- docs are updated
- operational hooks exist where required
- changes are committed cleanly
