---
id: IND-000175
title: Logistics Automation Catalogue
document_type: Industry Blueprint
category: Logistics
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
  - logistics
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

# Logistics Automation Catalogue

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [Logistics Pack](./README.md) · [Phase 13 Prompt](../../../01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md)

**Industry:** Logistics  •  **Document:** Automation Catalogue

## Executive Summary

Repeatable workflow automations for Logistics, executable by humans and AI agents.

## Automation Catalogue

| Automation | Trigger | Action | Integration |
| --- | --- | --- | --- |
| Re-route | Disruption | re-plan route. | GitHub / Slack / n8n |
| Delay alert | Risk | notify customer. | GitHub / Slack / n8n |
| Customs doc | Shipment | generate documents. | GitHub / Slack / n8n |
| Replenish | Low stock | trigger move. | GitHub / Slack / n8n |

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
