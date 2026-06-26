---
id: IND-000266
title: SaaS Companies Data Model
document_type: Industry Blueprint
category: SaaS Companies
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
  - saas-companies
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

# SaaS Companies Data Model

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [SaaS Companies Pack](./README.md) · [Phase 13 Prompt](../../../01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md)

**Industry:** SaaS Companies  •  **Document:** Data Model

## Executive Summary

The core data entities and sources that power AI in SaaS Companies.

## Core Entities

| Entity | Description |
| --- | --- |
| Account | Core SaaS Companies entity. |
| User | Core SaaS Companies entity. |
| Subscription | Core SaaS Companies entity. |
| Usage Event | Core SaaS Companies entity. |
| Ticket | Core SaaS Companies entity. |
| Invoice | Core SaaS Companies entity. |
| Feature Flag | Core SaaS Companies entity. |

## Relationships

- Entities relate through clear keys and ownership.
- Events capture state changes for analytics and agents.
- Sensitive entities carry classification and retention.

## Mermaid Entity Diagram

```mermaid
flowchart LR
    E0[Account]
    E1[User]
    E2[Subscription]
    E3[Usage Event]
    E4[Ticket]
    E0 --> E1
    E0 --> E2
    E0 --> E3
    E0 --> E4
```

## Data Sources

- Product analytics
- Billing
- Support/CRM
- App database

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
