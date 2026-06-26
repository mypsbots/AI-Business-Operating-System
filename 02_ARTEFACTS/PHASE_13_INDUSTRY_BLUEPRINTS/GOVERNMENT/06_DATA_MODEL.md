---
id: IND-000106
title: Government Data Model
document_type: Industry Blueprint
category: Government
phase: Phase 13
owner: Chief Industry Solutions Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - industry-blueprint
  - government
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md
standards:
  - ISO 42001
  - ISO 27001
  - NIST AI RMF
  - SOC 2
  - OWASP ASVS
  - OWASP LLM Top 10
  - WCAG 2.2 AA
---

# Government Data Model

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [Government Pack](./README.md) · [Phase 13 Prompt](../../../01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md)

**Industry:** Government  •  **Document:** Data Model

## Executive Summary

The core data entities and sources that power AI in Government.

## Core Entities

| Entity | Description |
| --- | --- |
| Citizen | Core Government entity. |
| Case | Core Government entity. |
| Application | Core Government entity. |
| Service | Core Government entity. |
| Document | Core Government entity. |
| Payment | Core Government entity. |
| Agency | Core Government entity. |

## Relationships

- Entities relate through clear keys and ownership.
- Events capture state changes for analytics and agents.
- Sensitive entities carry classification and retention.

## Mermaid Entity Diagram

```mermaid
flowchart LR
    E0[Citizen]
    E1[Case]
    E2[Application]
    E3[Service]
    E4[Document]
    E0 --> E1
    E0 --> E2
    E0 --> E3
    E0 --> E4
```

## Data Sources

- Case systems
- Identity systems
- Document stores
- Open data

## Privacy Controls

- Data minimisation and purpose limitation.
- Encryption and masking of sensitive fields.
- Retention and secure-deletion policies.

## Required Skills

See the [Specialist Skills](../../PHASE_05_SKILLS/README.md).

## Required Rules

See the [Enterprise Rules](../../PHASE_06_RULES/README.md).

## Required Checklists

See the [Enterprise Checklists](../../PHASE_07_CHECKLISTS/README.md).

## Required Playbooks

See the [Enterprise Playbooks](../../PHASE_08_PLAYBOOKS/README.md).

## Required Templates

See the [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md).

## Knowledge Dependencies

See the [Enterprise Knowledge base](../../PHASE_10_KNOWLEDGE/README.md).

## Validation Checklist

- [ ] YAML front matter present and valid.
- [ ] Industry-specific content is accurate and actionable.
- [ ] Cross-references resolve.
- [ ] Security, privacy and compliance addressed.
- [ ] No secrets or sensitive data exposed.

## References

- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Repository Catalogue (ROOT_INDEX)](../../../ROOT_INDEX.md)
- [Phase 13 Master Prompt](../../../01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, focused industry blueprint. |
