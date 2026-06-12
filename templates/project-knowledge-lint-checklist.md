# Project Knowledge Lint Checklist

## Scope

- Project:
- Knowledge base location:
- Reviewer:
- Date:

## Source Grounding

- [ ] Important claims link to sources or approved project artifacts
- [ ] Source manifest entries are complete enough to find the source again
- [ ] Generated summaries are marked draft or reviewed
- [ ] Reviewed summaries identify reviewer and review date where needed
- [ ] Unsupported claims are removed, sourced, or marked as assumptions

## Consistency

- [ ] Terminology matches the project glossary
- [ ] Duplicate concepts with different names are reconciled
- [ ] Knowledge pages do not contradict requirements, architecture, runbooks, decisions, or backlog items
- [ ] Stale information is removed, updated, or marked stale
- [ ] Broken links are fixed or recorded as follow-up

## Environment / Spec / Verifier Boundary

- [ ] Knowledge pages do not replace approved specs or decision records
- [ ] Acceptance criteria remain in the correct requirements or backlog artifact
- [ ] Test evidence remains in QA or release artifacts
- [ ] Risk acceptances and release approvals remain in approved governance artifacts
- [ ] Agent-facing environment notes point to the authoritative source for risky actions

## Security, Privacy, and Rights

- [ ] No secrets, credentials, tokens, or keys are committed
- [ ] No unnecessary customer, personal, or sensitive data is committed
- [ ] Raw source snapshots are tracked only when rights, privacy, and size support it
- [ ] Copyrighted external sources are linked or summarized instead of pasted in bulk
- [ ] Repository access assumptions match the sensitivity of stored knowledge
- [ ] Cache, embedding, generated-index, and temporary-output files are ignored or removed

## Completeness

- [ ] `docs/knowledge/README.md` explains maintenance and ownership
- [ ] `docs/knowledge/sources.yml` covers relied-upon sources
- [ ] Glossary exists where terminology matters
- [ ] Wiki index links to the main knowledge pages
- [ ] Important decisions link to approved decision records
- [ ] Important gaps are recorded in the backlog

## Decision

- Result: pass / pass with exceptions / fail
- Exceptions:
- Follow-up backlog items:
