# Software Product UX Guidance

This document sets the baseline UX design process for software product projects. It is meant to keep projects from drifting straight from “idea” to “screens and code” without doing the thinking that makes software usable. Humans, famously, are bad at reading our minds. Design work is how we compensate.

## Purpose

Every project should define:

- who the users are
- what they are trying to accomplish
- what the product needs them to understand or trust
- how the product is structured
- how the core workflows behave
- how the experience is validated before and after launch

This guidance is a baseline, not bureaucracy for its own sake. Small projects can use lightweight versions of these steps. Complex, risky, regulated, security-sensitive, or multi-role products should treat them as mandatory design gates.

## Minimum UX Expectations

At minimum, every serious project should include:

1. User personas or role models
2. User workflows
3. Information architecture
4. Wireframes or equivalent UI sketches
5. UX approvals / design sign-off

Those are the floor. Good UX work should go further.

## Full UX Process Checklist

### 1. UX Strategy and Problem Framing

Before designing screens, define the actual problem.

Capture:

- the user problem being solved
- target users and affected roles
- business or project goals
- user success criteria
- product success metrics
- known constraints, risks, and assumptions
- what is explicitly out of scope

Useful questions:

- What pain exists today?
- Who has the pain?
- What happens if we do nothing?
- What would make users say, “yes, this solved it”?
- What tradeoffs are we deliberately making?

Deliverable options:

- UX strategy brief
- problem statement
- assumptions and risks list
- opportunity brief

### 2. User Research

Personas should be grounded in evidence where possible, not invented from vibes and caffeine.

Research may include:

- user interviews
- stakeholder interviews
- field/context research
- survey data
- support-ticket or sales-call analysis
- competitor/product review
- analytics from existing systems
- forum/community research

Capture:

- user goals
- pain points
- current workarounds
- vocabulary users actually use
- trust concerns
- accessibility needs
- technical comfort level
- decision-making authority
- environmental constraints

Deliverable options:

- research notes
- synthesis summary
- key findings
- opportunity map
- research-backed assumptions

### 3. Personas / Role Models

Define the important user types. For internal tools and security-heavy products, role models may be more useful than marketing-style personas.

Each persona or role should include:

- name or role label
- responsibilities
- goals
- pains/frustrations
- level of expertise
- permissions or authority
- context of use
- success criteria
- common failure modes
- trust concerns

Examples:

- End user
- Admin
- Reviewer/approver
- Security analyst
- Developer/operator
- Executive/stakeholder
- Support user
- External auditor

### 4. Jobs-to-Be-Done and Task Analysis

Define what users are trying to get done, not just what pages they visit.

Capture:

- core jobs-to-be-done
- trigger for each job
- user motivation
- required inputs
- expected outputs
- time sensitivity
- dependencies
- risks if the task fails
- definition of task completion

Example format:

> When [situation], I want to [motivation/action], so I can [desired outcome].

### 5. User Workflows

Map the steps users take to complete important tasks.

For each workflow, define:

- entry point
- actors/roles involved
- happy path
- alternate paths
- edge cases
- error states
- approval or review steps
- notifications
- handoffs
- completion state
- audit/logging needs, where relevant

Important workflow types:

- onboarding
- first successful use
- recurring daily/weekly use
- exception handling
- approval/rejection
- escalation
- recovery from failure
- account/settings changes
- destructive or irreversible actions

### 6. Journey Maps / Service Blueprints

Use journey maps when the experience spans time, channels, roles, or systems.

Capture:

- stages of the user journey
- user goals at each stage
- user emotions/friction
- visible product interactions
- behind-the-scenes system or team actions
- handoffs between roles
- support touchpoints
- trust or confidence gaps

Use service blueprints especially when humans, automation, and backend processes all interact.

### 7. Information Architecture

Define how information is organized and how users navigate it.

For public web projects, align information architecture with `SEO_GUIDANCE.md` so important content can be discovered, crawled, understood, and maintained.

Capture:

- top-level navigation
- page/screen hierarchy
- object model and relationships
- naming conventions
- search/filter/sort behavior
- SEO/discovery implications for public pages
- grouping and categorization rules
- settings structure
- permission-aware visibility
- empty states

Validation methods:

- card sorting
- tree testing
- navigation walkthroughs
- prototype testing

### 8. Content Design

Words are part of the interface. Bad wording can ruin good UI with impressive efficiency.

Define:

- product terminology
- labels and navigation text
- page titles, descriptions, and share-preview copy for public web pages
- empty states
- error messages
- confirmation text
- onboarding copy
- help text
- tooltips
- notification copy
- success/failure messages
- tone and voice

Good content should be:

- clear
- specific
- actionable
- consistent
- accessible
- honest about uncertainty

For security, compliance, AI, or trust-sensitive products, avoid vague “magic” language. Explain what happened, why it matters, and what the user can safely do next.

### 9. Wireframes and Prototypes

Create wireframes before high-fidelity design when structure or flow is still uncertain.

Use wireframes to validate:

- layout
- hierarchy
- navigation
- form structure
- core actions
- decision points
- workflow completeness

Prototype when interaction risk is high.

Prototype types:

- low-fidelity sketches
- clickable wireframes
- high-fidelity UI prototypes
- coded prototypes
- role-specific workflow demos

Include key states, not just the happy path.

### 10. Interaction Design Specs

Document how the interface behaves.

Specify:

- loading states
- disabled states
- hover/focus/active states
- validation behavior
- error recovery
- undo/cancel behavior
- autosave/manual save behavior
- destructive action confirmation
- permission-denied states
- partial success states
- timeout/session-expiry behavior
- mobile/responsive behavior
- keyboard interactions

If a design only shows the perfect state, it is not finished. Real users specialize in finding the cursed states.

### 11. Accessibility Requirements

Accessibility is a baseline quality requirement, not garnish.

Define:

- WCAG target, normally WCAG 2.2 AA unless otherwise justified
- keyboard navigation behavior
- focus order
- screen reader expectations
- color contrast
- reduced motion behavior
- form labeling
- error announcement behavior
- touch target sizing
- zoom/reflow expectations
- caption/transcript needs for media

Accessibility should be considered during design, implementation, and QA.

### 12. Design System / Component Standards

Projects should reuse patterns where possible instead of inventing a new UI civilization every sprint.

Define or reference:

- components
- design tokens
- spacing rules
- typography
- color palette
- icon usage
- form behavior
- validation patterns
- navigation patterns
- table/list patterns
- modal/drawer rules
- notification/toast rules
- empty/error/success state patterns

For software product projects, prefer consistency across projects unless there is a strong product reason to diverge.

### 13. Usability Testing

Validate that real or representative users can complete important tasks.

Test:

- comprehension
- task completion
- time to completion
- error frequency
- confidence/trust
- navigation clarity
- terminology
- onboarding
- edge cases

Useful approaches:

- moderated usability tests
- unmoderated prototype tests
- hallway testing for early concepts
- task-based QA sessions
- accessibility testing
- expert review/heuristic evaluation

Capture findings as backlog items, not vague design sadness.

### 14. Analytics and Success Metrics

Define how UX success will be measured.

Possible metrics:

- activation rate
- task completion rate
- time to first value
- time on task
- drop-off points
- error rates
- search usage/failure
- support requests
- feature adoption
- retention
- user satisfaction
- trust/confidence rating

For early projects, simple qualitative feedback may be enough. For production products, instrument the critical paths.

### 15. UX Acceptance Criteria

Design expectations should become concrete acceptance criteria on implementation work.

Examples:

- A new user can complete onboarding without admin help.
- The primary workflow can be completed from the dashboard in under N steps.
- Error messages explain what happened and how to recover.
- Keyboard users can complete the full workflow.
- The page has defined empty, loading, error, and success states.
- Destructive actions require confirmation and show consequences.
- Role-restricted users see an explanatory denied state, not a broken page.

Avoid acceptance criteria like “make it intuitive”. That is not a requirement; that is a prayer.

### 16. UX Approvals / Design Sign-Off

Before implementation or release, the appropriate humans should approve the UX direction.

Approval should cover:

- problem framing
- personas/roles
- core workflows
- information architecture
- wireframes/prototypes
- accessibility posture
- key content decisions
- high-risk edge cases
- implementation acceptance criteria

For small projects, this can be a short written approval. For larger projects, use a design review checkpoint.

### 17. Implementation QA / Design Review

After implementation, verify the shipped experience matches the approved design and intent.

Check:

- visual/layout fidelity
- workflow completeness
- responsive behavior
- accessibility basics
- error/loading/empty states
- role/permission behavior
- content accuracy
- browser/device support
- analytics events
- performance impact on UX

Design QA should happen before calling the feature done.

### 18. Post-Launch Feedback and Iteration

UX work continues after release. Users become much more honest once the thing is inconveniencing them in production.

After launch, review:

- analytics
- support requests
- user feedback
- bug reports
- session recordings, where appropriate and privacy-safe
- onboarding/drop-off data
- feature adoption
- trust/confidence issues

Turn findings into backlog items and prioritize them deliberately.

## Special Track: Trust UX

For AI, security, compliance, privacy, healthcare, finance, or operational-risk products, include trust UX explicitly.

Design for:

- what the system knows
- what it does not know
- confidence and uncertainty
- evidence/provenance
- user control
- auditability
- policy decisions
- permissions
- safe next actions
- escalation paths
- reversibility
- explainability without jargon floods

Users should understand:

- why something happened
- what evidence supports it
- what risk remains
- what they can do next
- when they need human review

Trust UX is not decorative reassurance. It is operational clarity.

## Lightweight Project Version

For small internal projects, use this reduced checklist:

1. Problem statement
2. Target users/roles
3. Top 3 user workflows
4. Basic information architecture
5. Wireframes or sketches for core screens
6. Empty/error/loading states
7. Accessibility basics
8. UX acceptance criteria
9. Human approval before build or release
10. Post-launch notes after first use

## Recommended Project Files

For future projects, consider adding a `docs/ux/` folder with:

- `docs/ux/ux-strategy.md`
- `docs/ux/research-notes.md`
- `docs/ux/personas.md`
- `docs/ux/jobs-to-be-done.md`
- `docs/ux/workflows.md`
- `docs/ux/journey-maps.md`
- `docs/ux/information-architecture.md`
- `docs/ux/content-design.md`
- `docs/ux/wireframes.md`
- `docs/ux/accessibility.md`
- `docs/ux/usability-testing.md`
- `docs/ux/ux-acceptance-criteria.md`
- `docs/ux/ux-approval.md`
- `docs/ux/post-launch-ux-review.md`

Use only what the project actually needs, but do not skip the thinking just because the interface looks obvious. “Obvious” is often where the bugs breed.

## Definition of UX-Ready

A project or feature is UX-ready when:

- users and roles are defined
- core workflows are documented
- information architecture is clear
- key screens or interactions are sketched or prototyped
- important states and edge cases are specified
- accessibility expectations are known
- success metrics or feedback methods are defined
- UX acceptance criteria exist
- the relevant human has approved the direction

## Definition of UX-Done

A project or feature is UX-done when:

- implementation matches the approved UX direction
- core workflows have been tested
- accessibility basics have been checked
- content is clear and consistent
- edge states behave acceptably
- analytics or feedback paths are in place, where appropriate
- launch feedback has been reviewed or scheduled
- new UX follow-up items have been added to the backlog

## Digital Estate Management UX, Where Applicable

For products that help non-corporate users prepare or administer personal digital assets, design Digital Estate Management as a deliberate workflow rather than a settings-page junk drawer.

Consider:

- a user-facing digital estate inventory
- asset categories and asset-specific disposition instructions
- trusted-person and role-management flows
- review reminders after life events, inactivity, or major account changes
- export packages for users, executors, advisors, fiduciaries, or family members
- emergency or survivor workflows with delay, notification, revocation, and audit where appropriate
- clear explanations of the limits imposed by platform rules, local law, provider processes, and professional advice
- privacy-first handling of private communications, sensitive media, third-party data, and family-dispute contexts

The UX must distinguish legal authority, consent, trusted-contact status, and technical access. Blurring those together is how a helpful feature becomes an unauthorized-access machine wearing a cardigan.

Guidance: `DIGITAL_ESTATE_MANAGEMENT_GUIDANCE.md`
