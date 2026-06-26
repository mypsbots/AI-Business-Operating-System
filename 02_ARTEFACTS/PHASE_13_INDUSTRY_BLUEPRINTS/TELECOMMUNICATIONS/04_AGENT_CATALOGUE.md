---
id: IND-000284
title: Telecommunications Agent Catalogue
document_type: Industry Blueprint
category: Telecommunications
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
  - telecommunications
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

# Telecommunications Agent Catalogue

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [Telecommunications Pack](./README.md) · [Phase 13 Prompt](../../../01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md)

**Industry:** Telecommunications  •  **Document:** Agent Catalogue

## Executive Summary

The portfolio of AI agents for Telecommunications, each with a clear role and authority boundaries.

## AI Agent Portfolio

| Agent | Role | Authority | Human Approval |
| --- | --- | --- | --- |
| Network Agent | Detects and predicts faults. | Scoped, least-privilege | Required for high-risk actions |
| Service Agent | Resolves customer issues. | Scoped, least-privilege | Required for high-risk actions |
| Retention Agent | Targets churn risk. | Scoped, least-privilege | Required for high-risk actions |
| Field Agent | Optimises dispatch. | Scoped, least-privilege | Required for high-risk actions |
| Planning Agent | Forecasts capacity. | Scoped, least-privilege | Required for high-risk actions |

## Collaboration Model

- An orchestrator delegates tasks to specialist agents.
- Agents share governed context/memory.
- Conflicts and failures follow defined escalation.

## Guardrails

- Least-privilege tools and scoped permissions.
- Input/output filtering and injection defence.
- Cost and loop limits; full observability.

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
