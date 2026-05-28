# AI-Agent Operation Boundaries

## Product / Project

- Name:
- Human owner:
- Agent-operation owner:
- Last reviewed:
- Next review:

## Agent Operation Decision

- Classification: throw-away / AI-agent-operable / product-owner exempted
- If throw-away or exempted, who approved that decision and why?
- Are AI agents allowed to operate or assist operation of this product? yes/no/limited
- Approved agent identities or classes:
- Human escalation path:
- Summary of allowed role:

## Read-Only Access

| Interface / Source | Purpose | Data Exposed | Agent Access | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Write-Capable Actions

| Action | Interface | Required Permission | Human Approval Required? | Rollback / Undo | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Human Approval Gates

List actions that require explicit human approval before execution.

- External-facing changes:
- Destructive or irreversible actions:
- Privacy-sensitive actions:
- Financially material actions:
- Privilege/access changes:
- Production-impacting changes:
- Public/customer communications:
- Risk acceptance or release approval:

## Forbidden Actions / No-Go Zones

Agents must not:

- 

## Credentials and Tool Scopes

Do not paste secrets here. Record scopes and storage locations only.

| Credential / Tool | Scope | Storage Location | Owner | Rotation / Review Cadence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Audit and Evidence

- Where are agent observations recorded?
- Where are recommendations recorded?
- Where are approvals recorded?
- Where are actions logged?
- How are agent actions distinguished from human actions?
- Required before/after evidence:

## Rollback, Recovery, and Containment

- General rollback path:
- Failed-action handling:
- Agent access kill switch / revocation path:
- Incident escalation path:

## Sensitive Data Boundaries

- Data classes agents may view:
- Data classes agents may not view:
- Redaction requirements:
- Prompt/logging restrictions:
- Tenant/customer boundary notes:
- Model/provider restrictions where relevant:

## Agent-Readable Runbook Notes

List runbooks, commands, dashboards, APIs, or procedures designed for agent use.

| Surface | Purpose | Read/Write | Approval Boundary | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
