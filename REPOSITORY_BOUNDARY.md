# Repository Boundary

This repository is the public guidance artifact for the software product
process. It should stay useful to readers who want to understand, reuse, or
adapt the guidance without needing access to private project operations.

## Public Repository Contents

Keep these in this public repository:

- product-process guidance documents
- reusable templates
- public README/navigation material
- license and public reuse/contribution notes
- public-facing roadmap or backlog items that explain planned guidance work
- repository-boundary guidance that helps contributors keep the public artifact clean

The public repository should be understandable on its own. It should not depend
on private Discord history, private workspace notes, or local OpenClaw runtime
state to make sense.

## Private Management Contents

Move or keep these in a private management repository when that repository
exists:

- private planning notes and review sessions
- Discord channel metadata and channel lifecycle operations
- detailed project-management history that is not useful to public readers
- internal decision notes that mention private workspace context
- incident notes, recovery notes, or operational queue details
- draft work that includes private names, local paths, or workspace-specific
  operational assumptions

Use the private management layer for the work record. Use this public repository
for the guidance corpus.

## Current Artifact Decisions

| Artifact | Current placement | Decision |
| --- | --- | --- |
| Guidance docs | Public repo | Keep public. |
| Templates | Public repo | Keep public. |
| `README.md` | Public repo | Keep public. |
| `LICENSE` | Public repo | Keep public. |
| `BACKLOG.md` | Public repo for now | Keep temporarily as public roadmap/backlog; later trim or replace after the private management repo exists. |
| `LIFECYCLE_STATE.md` | Private management repo | Keep out of the public repo; it is operational channel state, not public guidance content. |
| Review sessions | Private management | Do not add to public repo unless intentionally rewritten as public design notes. |
| Discord/channel metadata | Private management or workspace map | Do not add to public repo. |
| Internal operational notes | Private management | Do not add to public repo. |

## Split Rule

If a file helps a public reader use or improve the software-product-process
guidance, it can stay public. If a file mainly helps Skippy/Russ operate the
channel, track private decisions, recover work, or manage local workflow, it
belongs in the private management layer.

When unsure, keep the reusable guidance public and move the operational record
private. Annoying, but less annoying than explaining why a public docs repo has
channel plumbing in it.
