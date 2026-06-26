---
id: TEMP-000017
title: Agent Specification Template
document_type: Template
category: AI
phase: Phase 09
owner: Chief Documentation and Knowledge Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - template
  - ai
  - agent_specification_template
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_09_TEMPLATES_MASTER_PROMPT.md
standards:
  - ISO 42001
  - ISO 27001
  - NIST AI RMF
  - SOC 2
  - OWASP ASVS
  - OWASP LLM Top 10
  - WCAG 2.2 AA
---

# Agent Specification Template

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Templates](../README.md) · [Phase 09 Prompt](../../../01_PHASES/PHASE_09_TEMPLATES_MASTER_PROMPT.md)

**Template ID:** TEMP-000017  •  **Category:** AI

## Purpose

Define an AI agent's persona, authority and tools.

## When to Use

Before building or deploying an agent.

## Audience

Agent engineers and reviewers.

## Inputs Required

- Agent name
- Purpose

## Outputs Produced

A completed **Agent Specification Template** ready for review and use.

## Required Metadata

Every instance MUST carry: `id`, `title`, `owner`, `version`, `status`, `created`, `updated`.

## Placeholder Definitions

| Placeholder | Meaning |
| --- | --- |
| `{{name}}` | Agent name |
| `{{purpose}}` | Purpose |
| `{{date}}` | ISO date the document is created (YYYY-MM-DD). |

## Template

Copy the block below and replace every `{{placeholder}}` with real content.

````markdown
# Agent Specification: {{name}}

## Purpose
{{purpose}}

## Authority Boundaries
- Allowed: ...
- Forbidden: ...
- Human approval required for: ...

## Tools / Permissions
| Tool | Scope | Approval |
| --- | --- | --- |

## Memory & Context
- ...

## Failure Handling & Escalation
- ...

## Observability & KPIs
- ...
````

## Naming Convention

`NN_AGENT_SPECIFICATION.md` (zero-padded order prefix, UPPER_SNAKE_CASE).

## Folder Convention

Master template lives under `02_ARTEFACTS/PHASE_09_TEMPLATES/AI/`. Copy instances into the relevant project/repository location.

## Required Skills

See the [Specialist Skills](../../PHASE_05_SKILLS/README.md) relevant to this artefact.

## Required Rules

Comply with the [Enterprise Rules](../../PHASE_06_RULES/README.md).

## Required Checklists

Validate with the [Enterprise Checklists](../../PHASE_07_CHECKLISTS/README.md).

## Required Playbooks

Produced within the [Enterprise Playbooks](../../PHASE_08_PLAYBOOKS/README.md).

## Required Knowledge Articles

Background in the [Enterprise Knowledge base](../../PHASE_10_KNOWLEDGE/README.md).

## Validation Rules

- [ ] All `{{placeholders}}` are replaced (none remain).
- [ ] Required metadata is present and valid.
- [ ] No secrets or sensitive data are included.
- [ ] Cross-references resolve.
- [ ] Content follows the AIBOS style guide.

## Quality Criteria

- Consistent and reusable across teams.
- Modular and easy to customise.
- Machine-readable and automation-ready.
- Version-controlled and reviewed.

## Example Completed Template

Fill each placeholder with concrete values. For example, replace `{{name}}` with a real value and complete each section with project-specific detail.

## JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["id", "title", "version"],
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "version": { "type": "string" }
  }
}
```

## YAML Schema

```yaml
id: DOC-000000
title: Example
owner: Owning Team
version: 1.0.0
status: Draft
```

## AI Prompt Usage Guidance

- Prompt an AI agent: "Using the Agent Specification Template below, produce a completed version for <context>; replace every placeholder and keep the structure."
- Provide the source inputs (notes, tickets, data) as context.
- Ask the agent to flag any placeholder it cannot fill confidently.
- Always have a human review AI-completed instances before use.

## Automation Compatibility

- GitHub / GitHub Actions (scaffold and validate).
- Cursor, Claude, GPT, Gemini (AI-assisted completion).
- n8n / Make (workflow generation).
- MCP tools and CI/CD pipelines.

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use template. |
