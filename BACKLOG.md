# Backlog

## Completed

- [x] Add explicit user/admin/operator documentation guidance, templates, and release/QA gates.
- [x] Run consistency pass across guidance docs for terminology, navigation, phase numbering, and ambiguous references.
- [x] Add SEO/discovery guidance for web projects, including templates and process/release/QA gates.
- [x] Split Product Operational Estate Management from user-facing Digital Estate Management, add Digital Estate Management process guidance, and add starter templates.
- [x] Add CSAF/VEX advisory-readiness guidance for SaaS/security/infrastructure/developer products that may need to publish machine-readable advisories about themselves.
- [x] Broaden CSAF/VEX advisory readiness to cover inbound vendor/dependency advisory ingestion, triage, affected-product mapping, VEX/not-affected decisions, and release/customer-notice triggers.
- [x] Add observability/debuggability guidance so operators and incident teams can understand system health, reconstruct failures, preserve evidence, and debug safely.
- [x] Add release workflow action SHA-pinning as a supply-chain good practice for package-publication and trusted-publishing workflows.
- [x] Add canonical Project Knowledge Architecture / LLM wiki guidance as part of the agent-operable project environment, including tracked wiki/source manifests, ignored cache/raw-bulk rules, provenance and review expectations, and spec/verifier/environment mapping for agent-heavy work.
- [x] Add starter templates for project knowledge architecture, including `docs/knowledge/README.md`, `sources.yml`, and a project knowledge lint checklist.
- [x] Wire Project Knowledge Guidance into lifecycle, tailoring, AI-agent operation, implementation planning, QA, documentation, and governance guidance.
- [x] Apply the new Digital Estate Management applicability assessment to existing non-corporate/end-user projects and update their project-specific requirements/backlogs where it applies.
  - Updated `projects/digital-asset-management-inventory` with an applies-if-reopened assessment and requirements/security backlog.
  - Updated `projects/www-dam-certificate-xxx` with certification-content versus website-feature scope boundaries.
  - Updated `projects/digital-estate-question-bank` with content/provenance applicability and assessment-delivery limits.

## Open

- [ ] Define public reuse and licensing posture for the guidance repo:
  - Decide whether the public docs are intended for reuse, reference only, or later open-source collaboration.
  - Add the corresponding `LICENSE` or copyright/reuse note.
  - Update `README.md` so visitors understand whether they may copy, adapt, or contribute to the guidance.
- [ ] Decide which management artifacts remain public versus move private:
  - Review `BACKLOG.md`, future `LIFECYCLE_STATE.md`, review notes, decision records, and channel/project metadata.
  - Keep product-facing process guidance public.
  - Move or omit internal planning/history only when it exposes private context, clutters the showcase, or belongs to channel operations rather than the public guidance corpus.
- [ ] Create private management boundary for future work:
  - Create or designate a private `docs-software-product-process-mgnt` project/repo if ongoing planning, lifecycle state, review notes, or channel-specific decisions continue.
  - Record that the public repo is the guidance artifact and the private management repo is the operational/project-control layer.
  - Link the private management repo from local channel mapping or project notes without adding private URLs or operational details to the public repo.
- [ ] Move current management backlog if presentation review says it should not stay public:
  - If `BACKLOG.md` is retained publicly, trim it to public-roadmap language.
  - If it moves private, replace it in the public repo with a short public roadmap or remove it entirely.
  - Preserve useful completed-work history in the private management repo before removing it from the public repo.
- [ ] Add public/private repository hygiene checks:
  - Add a lightweight check for private-management-only paths, channel metadata, secrets, runtime files, and local workspace references.
  - Document the check in `README.md` or a contributor note.
  - Run it before future pushes to the public docs repo.
- [ ] Re-review public-readiness after the split:
  - Confirm public repo contains only guidance docs, templates, public roadmap/licensing material, and safe contributor-facing notes.
  - Confirm private management repo contains any internal planning, lifecycle state, operational notes, and channel-specific history.
  - Confirm both repos are clean and remotes/visibility match their intended roles.

## Burndown

- Done: 12
- Open: 6
- Total: 18
