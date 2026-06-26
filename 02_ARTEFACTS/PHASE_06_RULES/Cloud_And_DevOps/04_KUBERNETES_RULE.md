---
id: RULE-000032
title: Kubernetes Rule
document_type: Rule
category: Cloud And DevOps
phase: Phase 06
owner: Chief Governance Architect
status: Draft
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - rule
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md
standards:
  - ISO 42001
  - ISO 27001
  - NIST AI RMF
  - SOC 2
  - OWASP ASVS
  - OWASP LLM Top 10
  - WCAG 2.2 AA
---

# Kubernetes Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [Generated Index](../../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

## Executive Summary

This document defines **Kubernetes Rule** within the AIBOS Enterprise v2.0 framework (Phase 06). It inherits every root standard and is designed to be enterprise-ready, machine-readable and AI-friendly.

## Purpose

To establish the authoritative, reusable definition of Kubernetes Rule so that human teams and AI agents operate consistently, safely and with measurable business value.

## Scope

Applies across the AIBOS enterprise and is inherited by all dependent artefacts. Concerns owned elsewhere are delegated to their owning documents to avoid duplication.

## Business Rationale

This section (Business Rationale) for **Kubernetes Rule** is defined in line with the AIBOS root standards and the governing Phase 06 master prompt. See the [repository catalogue](../../../ROOT_INDEX.md) and the [root standards](../../../00_ROOT) for related material.

## Technical Rationale

This section (Technical Rationale) for **Kubernetes Rule** is defined in line with the AIBOS root standards and the governing Phase 06 master prompt. See the [repository catalogue](../../../ROOT_INDEX.md) and the [root standards](../../../00_ROOT) for related material.

## Definitions

- Canonical terms are defined in the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).
- No terminology is redefined within this document.

## Mandatory Requirements (MUST)

- The team MUST apply the AIBOS root standards when implementing Kubernetes Rule.
- The team MUST validate every artefact before publication.
- The team MUST require human approval for high-risk actions.
- The team MUST maintain an auditable trail of decisions.

## Recommended Practices (SHOULD)

- Teams SHOULD automate repeatable validation where practical.
- Teams SHOULD reuse existing artefacts before creating new ones.
- Teams SHOULD capture metrics to drive continuous improvement.

## Optional Practices (MAY)

- Teams MAY extend this artefact for domain-specific needs.
- Teams MAY add additional tooling integrations.

## Rule Ownership Matrix

| Partner | Interaction | Direction |
| --- | --- | --- |
| Upstream owners | Provide inputs | Inbound |
| Downstream consumers | Consume outputs | Outbound |
| Governance | Review and approve | Bidirectional |

## Applicable Departments

- See **[Department Specifications (Phase 04)](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md)** for the relevant artefacts.
- Inherited standards: [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).
- Full catalogue: [ROOT_INDEX](../../../ROOT_INDEX.md).

## Applicable Skills

- See **[Specialist Skills (Phase 05)](../../PHASE_05_SKILLS/README.md)** for the relevant artefacts.
- Inherited standards: [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).
- Full catalogue: [ROOT_INDEX](../../../ROOT_INDEX.md).

## Related Rules

- See **[Enterprise Rules (Phase 06)](../README.md)** for the relevant artefacts.
- Inherited standards: [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).
- Full catalogue: [ROOT_INDEX](../../../ROOT_INDEX.md).

## Related Checklists

- See **[Enterprise Checklists (Phase 07)](../../PHASE_07_CHECKLISTS/README.md)** for the relevant artefacts.
- Inherited standards: [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).
- Full catalogue: [ROOT_INDEX](../../../ROOT_INDEX.md).

## Related Playbooks

- See **[Enterprise Playbooks (Phase 08)](../../PHASE_08_PLAYBOOKS/README.md)** for the relevant artefacts.
- Inherited standards: [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).
- Full catalogue: [ROOT_INDEX](../../../ROOT_INDEX.md).

## Related Templates

- See **[Enterprise Templates (Phase 09)](../../PHASE_09_TEMPLATES/README.md)** for the relevant artefacts.
- Inherited standards: [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).
- Full catalogue: [ROOT_INDEX](../../../ROOT_INDEX.md).

## Related Knowledge Articles

- See **[Enterprise Knowledge (Phase 10)](../../PHASE_10_KNOWLEDGE/README.md)** for the relevant artefacts.
- Inherited standards: [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).
- Full catalogue: [ROOT_INDEX](../../../ROOT_INDEX.md).

## Security Considerations

Apply Security by Design, least privilege and Zero Trust; protect secrets and follow OWASP guidance.

## Privacy Considerations

Apply data minimisation, purpose limitation and retention controls.

## AI Considerations

Maintain human-in-the-loop controls and minimise hallucination risk.

## Compliance Requirements

| Standard | Application |
| --- | --- |
| ISO 42001 | AI management system alignment. |
| ISO 27001 | Information security controls. |
| NIST AI RMF | AI risk management. |
| OWASP LLM Top 10 | LLM threat mitigation. |

## Exceptions Process

This section (Exceptions Process) for **Kubernetes Rule** is defined in line with the AIBOS root standards and the governing Phase 06 master prompt. See the [repository catalogue](../../../ROOT_INDEX.md) and the [root standards](../../../00_ROOT) for related material.

## Approval Authority

This section (Approval Authority) for **Kubernetes Rule** is defined in line with the AIBOS root standards and the governing Phase 06 master prompt. See the [repository catalogue](../../../ROOT_INDEX.md) and the [root standards](../../../00_ROOT) for related material.

## Enforcement Model

This section (Enforcement Model) for **Kubernetes Rule** is defined in line with the AIBOS root standards and the governing Phase 06 master prompt. See the [repository catalogue](../../../ROOT_INDEX.md) and the [root standards](../../../00_ROOT) for related material.

## Metrics

- Quality score.
- Defect density.
- Review turnaround.

## KPIs

- Coverage and completeness.
- Validation pass rate (target 95%+).
- Cycle time from draft to approval.
- Reuse rate across the enterprise.

## Risks

- Scope drift over time.
- Inconsistent adoption across teams.
- Over-automation without adequate oversight.

## Anti-patterns

- Duplicating concepts defined elsewhere.
- Bypassing human approval for high-risk actions.
- Undocumented exceptions.

## Best Practices

- Reuse before build.
- Automate validation.
- Keep documents atomic and cross-referenced.

## Acceptance Criteria

- All mandatory sections are complete.
- Validation passes with no errors.
- Cross-references are valid.

## Validation Checklist

- [ ] YAML front matter is present and valid.
- [ ] All mandatory sections are complete.
- [ ] Terminology matches the AIBOS Enterprise Glossary.
- [ ] Cross-references resolve to existing documents.
- [ ] RFC 2119 keywords are used correctly.
- [ ] Security and privacy considerations are addressed.
- [ ] Version history is updated.
- [ ] No secrets or sensitive data are exposed.

## References

- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md)
- [Document Schema](../../../00_ROOT/AIBOS_DOCUMENT_SCHEMA.md)
- [Repository Catalogue (ROOT_INDEX)](../../../ROOT_INDEX.md)
- [Phase 06 Master Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Initial generated artefact. |
