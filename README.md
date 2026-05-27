# Guidance Docs

Workspace guidance for taking software products from idea to operation without skipping the thinking that prevents expensive stupidity later.

The guidance is deliberately modular. The top-level process explains the flow; each sub-document expands one discipline or checkpoint. Small projects can use the lightweight versions. Serious, public, security-sensitive, multi-user, regulated, or production projects should treat the full guidance as required gates.

## Core Documents

- `SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md` — high-level process and phase gates
- `ENGINEERING_PRINCIPLES.md` — baseline engineering, security, privacy, and operations principles
- `PRODUCT_FRAMING_GUIDANCE.md` — opportunity framing and problem definition
- `REQUIREMENTS_GUIDANCE.md` — product, functional, non-functional, security, and operational requirements
- `UX_GUIDANCE.md` — UX design process, trust UX, accessibility, validation, and UX readiness
- `SECURITY_GUIDANCE.md` — security and privacy design process
- `ARCHITECTURE_GUIDANCE.md` — technical architecture and system design
- `IMPLEMENTATION_PLANNING_GUIDANCE.md` — milestones, backlog breakdown, and delivery planning
- `IMPLEMENTATION_GUIDANCE.md` — build guidance and coding expectations
- `QA_GUIDANCE.md` — verification, testing, and quality gates
- `RELEASE_SECURITY_GATE.md` — explicit security review before release
- `RELEASE_GUIDANCE.md` — launch/release checklist and rollback readiness
- `OPERATIONS_GUIDANCE.md` — post-launch operations, automation, maintenance, and incident handling

## Operating Model

Security, privacy, accessibility, observability, maintainability, and automated operations are first-class concerns. They appear both as dedicated documents and as checkpoints throughout the process.

The desired end state is boring software: understandable, secure by default, observable, recoverable, and automated enough that one competent operator could oversee many projects without living inside a pager-shaped coffin.
