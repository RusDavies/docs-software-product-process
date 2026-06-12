# Project Knowledge

## Purpose

What durable context should this project knowledge base preserve for humans and approved agents?

## Scope

- Project:
- Human owner:
- Knowledge owner:
- Last reviewed:
- Next review:

## Knowledge Structure

| Location | Purpose | Owner | Review Cadence | Notes |
| --- | --- | --- | --- | --- |
| `docs/knowledge/sources.yml` | Source manifest and provenance |  |  |  |
| `docs/knowledge/glossary.md` | Project terminology |  |  |  |
| `docs/knowledge/wiki/index.md` | Curated project knowledge index |  |  |  |
| `docs/knowledge/wiki/decisions.md` | Decision map linking to approved decision records |  |  |  |
| `docs/knowledge/wiki/domain-map.md` | Domain concepts, actors, and workflows |  |  |  |
| `docs/knowledge/wiki/implementation-map.md` | Codebase and implementation orientation |  |  |  |
| `docs/knowledge/wiki/operations-map.md` | Operational context and runbook links |  |  |  |

## Environment / Spec / Verifier Boundary

- Spec source(s):
- Verifier source(s):
- Environment source(s):
- Agent-facing project instructions:

The knowledge base may summarize or link to specs, decisions, and evidence. It does not replace approved requirements, decision records, risk acceptances, release approvals, or test evidence.

## Version-Control Rules

Commit:

- reviewed wiki pages
- source manifests and provenance notes
- glossary and conventions
- reviewed summaries
- lint/review checklists

Do not commit:

- secrets or credentials
- private customer data unless explicitly approved for this repository
- raw production logs
- sensitive chat exports
- generated indexes, embeddings, vector databases, caches, or temporary model output

Case-by-case:

- raw source snapshots
- transcripts
- licensed or internal documents
- public web captures

## Source and Review Rules

- Add source metadata to `sources.yml` before relying on a source.
- Link important claims to sources or approved project artifacts.
- Treat generated summaries as drafts until reviewed.
- Record knowledge gaps or stale-context risks in the backlog.
- Run the project knowledge lint checklist before release or major handoff.

## Sensitive Data Boundaries

- Data classes allowed in the knowledge base:
- Data classes forbidden in the knowledge base:
- Redaction requirements:
- Repository access assumptions:
- Model/provider restrictions where relevant:

## Maintenance Notes

- Review trigger for product changes:
- Review trigger for external source changes:
- Stale-doc detection method:
- Backlog process for gaps:
