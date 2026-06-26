---
id: TEMP-000026
title: Runbook Template
document_type: Template
category: Operations
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
  - operations
  - runbook_template
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

# Runbook Template

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Templates](../README.md) · [Phase 09 Prompt](../../../01_PHASES/PHASE_09_TEMPLATES_MASTER_PROMPT.md)

**Template ID:** TEMP-000026  •  **Category:** Operations

## Purpose

Step-by-step operational procedure for a task/service.

## When to Use

For recurring or on-call operational tasks.

## Audience

On-call engineers and operators.

## Inputs Required

- Task/service

## Outputs Produced

A completed **Runbook Template** ready for review and use.

## Required Metadata

Every instance MUST carry: `id`, `title`, `owner`, `version`, `status`, `created`, `updated`.

## Placeholder Definitions

| Placeholder | Meaning |
| --- | --- |
| `{{task}}` | Task/service |
| `{{date}}` | ISO date the document is created (YYYY-MM-DD). |

## Template

Copy the block below and replace every `{{placeholder}}` with real content.

````markdown
# Runbook: {{task}}

## When to Use
- ...

## Prechecks
- [ ] ...

## Procedure
1. ...
2. ...

## Verification
- [ ] ...

## Rollback
- ...

## Escalation
- ...
````

## Naming Convention

`NN_RUNBOOK.md` (zero-padded order prefix, UPPER_SNAKE_CASE).

## Folder Convention

Master template lives under `02_ARTEFACTS/PHASE_09_TEMPLATES/Operations/`. Copy instances into the relevant project/repository location.

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

Fill each placeholder with concrete values. For example, replace `{{task}}` with a real value and complete each section with project-specific detail.

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

- Prompt an AI agent: "Using the Runbook Template below, produce a completed version for <context>; replace every placeholder and keep the structure."
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
