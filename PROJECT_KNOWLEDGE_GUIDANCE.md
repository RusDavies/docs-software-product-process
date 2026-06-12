# Project Knowledge Guidance

Project knowledge guidance defines how a product keeps durable, source-grounded context that humans and approved agents can use without rediscovering the same facts every week like procedural amnesia with commit access.

## Purpose

Project knowledge architecture provides the agent-operable environment around the product:

- source inventory
- project glossary and terminology
- decision and rationale map
- domain notes
- implementation context
- operational context
- research summaries
- reusable agent instructions
- links to requirements, architecture, risks, runbooks, and backlog items

The project knowledge base is part of the environment. It helps humans and agents understand the project, form plans, and find evidence. It is not itself the product specification, approval record, risk acceptance, or release authority unless a human explicitly reviews and approves that content as such.

Practical rule: environment informs work; specs authorize work.

## Applicability Rule

Use project knowledge architecture when a project has enough durable context that repeated rediscovery would create cost, drift, or risk.

Recommended for:

- Class 2 and higher projects with ongoing maintenance
- long-running agent-assisted projects
- projects with domain research, customer discovery, or competitive analysis
- products with security, compliance, operational, or legal context
- projects with multiple contributors or handoffs
- products with a meaningful decision history
- repositories where agents need stable orientation before making changes

Usually unnecessary for:

- Class 0 throw-away work
- tiny one-off scripts with no durable context
- pure experiments where the product owner explicitly accepts deletion/rebuild instead of maintenance

For software libraries/packages, use a lightweight knowledge base when there is significant API rationale, compatibility history, security posture, vulnerability intake, release process, or maintainer handoff context.

## Environment, Not Spec

For agent-heavy work, distinguish three concerns:

- **Spec:** the goal, acceptance criteria, constraints, approved decisions, risks, and non-goals.
- **Verifier:** tests, review gates, linters, security checks, QA evidence, and human approval paths.
- **Environment:** repository structure, tools, runbooks, project docs, agent instructions, source corpus, and project knowledge base.

An LLM wiki, project memory, or generated knowledge map belongs primarily in the environment. It may summarize or link to specifications, decisions, and evidence, but it should not silently replace them.

## Recommended Structure

Use a simple structure unless the project genuinely needs more:

```text
docs/knowledge/
  README.md
  sources.yml
  glossary.md
  wiki/
    index.md
    decisions.md
    domain-map.md
    implementation-map.md
    operations-map.md
  raw/
  cache/
```

Suggested roles:

- `README.md` explains how the knowledge base is maintained.
- `sources.yml` lists source material, provenance, ownership, access rules, and review state.
- `glossary.md` defines important terms and avoids local dialect drift.
- `wiki/` contains curated, reviewed, human-readable project knowledge.
- `raw/` holds source snapshots only when rights, privacy, and size make that appropriate.
- `cache/` holds generated indexes, temporary model output, embeddings, or rebuildable files and is normally ignored.

Project-specific agent instructions may live in the repository root `AGENTS.md`, in `docs/knowledge/README.md`, or in a dedicated project agent-environment document. Avoid hiding operationally important rules in private model prompts that cannot be reviewed in git.

## Version Control Rules

Default to committing reviewed knowledge and ignoring rebuildable machinery or sensitive bulk.

Commit:

- curated wiki pages under `docs/knowledge/wiki/`
- source manifests and provenance maps
- schemas, conventions, glossary, and agent-facing project notes
- human-reviewed summaries
- decision maps that link to approved decision records
- ingestion, validation, and lint scripts where used

Usually do not commit:

- private customer data
- secrets, credentials, tokens, or keys
- raw production logs
- sensitive chat exports
- huge generated indexes
- embeddings or vector databases
- cache directories
- temporary model outputs
- generated summaries that have not been reviewed

Case-by-case:

- project-owned raw source snapshots
- licensed internal documents
- public web captures
- transcripts
- research exports

Only commit case-by-case material when the project has the right to store it, the content is not sensitive beyond the repository's intended access boundary, the size is reasonable, and the source is needed for auditability or review.

Recommended ignore patterns:

```gitignore
docs/knowledge/cache/
docs/knowledge/**/*.embeddings
docs/knowledge/**/*.index
docs/knowledge/**/*.tmp
.wiki-cache/
```

If `docs/knowledge/raw/` may contain sensitive or bulky material, ignore it by default and explicitly opt in individual safe files.

## Source and Provenance Rules

Every curated knowledge page should make it clear where important claims came from.

Capture source metadata such as:

- title
- owner or publisher
- URL or repository path
- access date
- license or usage constraint where known
- sensitivity/classification
- review status
- related requirements, decisions, risks, or backlog items

Do not paste large copyrighted sources into the repository unless the project has the right to store them. Prefer a source manifest, short summary, and link. For private or sensitive material, store only the minimum safe context needed for maintainers and agents to find the approved source.

Generated summaries should be treated as drafts until reviewed. Once reviewed, record the reviewer, date, and source material used.

## Ingest and Update Workflow

Use a repeatable workflow:

1. Identify the source and whether it may be stored.
2. Add or update the source manifest.
3. Capture raw material only when allowed and useful.
4. Update curated wiki pages with links back to the source.
5. Add or update glossary terms if the source introduces important language.
6. Link relevant requirements, decisions, risks, backlog items, or runbooks.
7. Review the diff.
8. Run the project knowledge lint checklist where available.
9. Commit the reviewed knowledge changes.

Do not let an agent ingest a large body of private, licensed, or customer-sensitive material without explicit approval and a clear repository-access boundary.

## Lint and Review Expectations

Project knowledge should be checked for:

- unsupported claims
- stale or broken links
- duplicate concepts with different names
- contradictory guidance
- summaries that drift from sources
- missing source references
- copied private or sensitive data
- accidental secrets
- generated output presented as approved fact
- documentation that conflicts with requirements, architecture, runbooks, or decision records

For serious projects, review knowledge-base changes through normal code review or documentation review. A beautiful wiki that lies is just a spreadsheet with better typography.

## Scale Limits and Hybrid Search

An LLM wiki works best when the curated context is small enough to load, review, and reason over directly.

When the source corpus grows too large or changes frequently, use a hybrid model:

- curated wiki for stable project understanding
- source manifest for provenance
- repository search for exact text
- specialized indexes or search tools for large corpora
- generated summaries only as reviewable drafts

Do not treat a huge generated wiki as a substitute for search, tests, specs, or human review. Past a certain size, the issue is not whether the model can read it; the issue is whether anyone can verify that it is still true.

## Security and Privacy Boundaries

Project knowledge bases often attract sensitive context because they are useful. That makes them a security boundary.

Define:

- what data classes may appear in the knowledge base
- what raw sources may be stored
- what must remain external or private
- who may read the repository
- redaction rules
- secret-scanning expectations
- model/provider constraints where generated summaries are used
- retention and deletion expectations for raw sources and caches

Never store secrets in project knowledge. Do not store customer or personal data unless the repository access model, retention rules, and product owner approval support it.

## Relationship to Other Artifacts

Project knowledge should link to, not replace:

- requirements specifications
- architecture overviews
- decision records
- risk registers
- threat models
- QA plans and results
- release checklists
- operations runbooks
- product operational estate registers
- compliance evidence
- backlog items

If a knowledge page discovers a missing requirement, decision, risk, or backlog item, add that item to the correct artifact instead of leaving it only in the wiki.

## Lightweight Project Version

For small maintained projects:

1. Add `docs/knowledge/README.md`.
2. Add `docs/knowledge/sources.yml` if external or research sources matter.
3. Add one `docs/knowledge/wiki/index.md` with important context and links.
4. Track reviewed knowledge in git.
5. Ignore caches, generated indexes, and sensitive raw material.
6. Add knowledge gaps or stale-context risks to the backlog.

## Recommended Project Files

- `docs/knowledge/README.md`
- `docs/knowledge/sources.yml`
- `docs/knowledge/glossary.md`
- `docs/knowledge/wiki/index.md`
- `docs/knowledge/wiki/decisions.md`
- `docs/knowledge/wiki/domain-map.md`
- `docs/knowledge/wiki/implementation-map.md`
- `docs/knowledge/wiki/operations-map.md`
- `docs/knowledge/project-knowledge-lint-checklist.md`

## Definition of Knowledge-Ready

Project knowledge is ready when:

- the project has a documented knowledge structure
- source and provenance expectations are clear
- version-control and ignore rules are defined
- sensitive-data boundaries are stated
- agent-facing context points to approved specs, runbooks, decisions, and backlog items
- generated summaries are treated as drafts until reviewed

## Definition of Knowledge-Done

For a release or major project milestone, project knowledge work is done when:

- the curated wiki reflects current approved project context
- important claims link to sources or approved artifacts
- stale or unsupported material has been removed or marked
- caches and generated indexes are ignored or reproducible
- sensitive material has not been committed accidentally
- follow-up knowledge gaps are in the backlog
