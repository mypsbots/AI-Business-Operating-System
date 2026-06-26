---
id: IND-000075
title: Energy Automation Catalogue
document_type: Industry Blueprint
category: Energy
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
  - energy
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

# Energy Automation Catalogue

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [Energy Pack](./README.md) · [Phase 13 Prompt](../../../01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md)

**Industry:** Energy  •  **Document:** Automation Catalogue

## Executive Summary

Repeatable workflow automations for Energy, executable by humans and AI agents.

## Automation Catalogue

| Automation | Trigger | Action | Integration |
| --- | --- | --- | --- |
| Maintenance alert | Sensor | schedule. | GitHub / Slack / n8n |
| Outage detect | Signal | dispatch crew. | GitHub / Slack / n8n |
| Demand response | Peak | trigger DR. | GitHub / Slack / n8n |
| Safety check | Job | verify procedure. | GitHub / Slack / n8n |

## Integration Points

- GitHub / GitHub Actions
- Slack / Teams notifications
- Jira / Linear tracking
- n8n / Make orchestration
- Core line-of-business systems via MCP

## Human Approval Points

- Before any irreversible or high-risk action.
- Before external customer-facing communications.
- Before financial or regulated decisions.

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
