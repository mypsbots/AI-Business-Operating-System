---
id: RULE-000039
title: Documentation Rule
document_type: Rule
category: Quality
phase: Phase 06
owner: Head of Quality
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - rule
  - quality
  - documentation_rule
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

# Documentation Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000039  •  **Category:** Quality

## Executive Summary

This rule is the single source of truth for **Documentation** in the AIBOS Enterprise. Clear, current, version-controlled documentation for products, systems and processes — for humans and AI agents. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for documentation so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect documentation across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Clear, current, version-controlled documentation for products, systems and processes — for humans and AI agents. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Docs-as-code** — Treating docs like code: versioned and reviewed.

## Mandatory Requirements (MUST)

- Every system/feature MUST have current documentation.
- Docs MUST be version-controlled and reviewed like code.
- Docs MUST NOT contain secrets or sensitive data.

## Recommended Practices (SHOULD)

- Docs SHOULD follow the style guide and be cross-linked.
- Docs SHOULD be updated in the same change as the code.

## Optional Practices (MAY)

- Teams MAY auto-generate docs from specs/code.

## Rule Ownership Matrix

| Role | Assignment |
| --- | --- |
| Rule Owner | Head of Quality |
| Rule Approver | Chief Governance Architect |
| Mandatory Reviewers | Security Engineer, Compliance Specialist |
| Roles Required to Follow | All contributors within scope (human and AI) |
| Roles Allowed to Override | Head of Quality (with documented exception) |
| Escalation Authority | Governance Division |

## Applicable Departments

All departments performing documentation. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Applicable Skills

Roles that must follow this rule are defined in the [Specialist Skills](../../PHASE_05_SKILLS/README.md).

## Related Rules

See other rules in the [Enterprise Rules catalogue](../README.md).

## Related Checklists

Validated via the [Enterprise Checklists](../../PHASE_07_CHECKLISTS/README.md).

## Related Playbooks

Operationalised through the [Enterprise Playbooks](../../PHASE_08_PLAYBOOKS/README.md).

## Related Templates

Supported by the [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md).

## Related Knowledge Articles

Explained in the [Enterprise Knowledge base](../../PHASE_10_KNOWLEDGE/README.md).

## Security Considerations

Apply Security by Design, least privilege and Zero Trust. Protect secrets and follow OWASP ASVS and the OWASP LLM Top 10 where AI is involved.

## Privacy Considerations

Apply data minimisation, purpose limitation and retention controls to any personal data touched by this rule.

## AI Considerations

Where AI agents apply this rule, keep a human in the loop for high-risk actions, maintain audit trails and mitigate hallucination.

## Compliance Requirements

| Standard | Application |
| --- | --- |
| ISO 27001 | Information security baseline. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (Head of Quality), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of Quality.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Doc freshness
- Broken-link count
- Findability

## KPIs

- Doc freshness
- Broken-link count
- Findability

## Risks

- Stale docs mislead people and AI agents.

## Anti-patterns

- Docs that drift from reality.
- Tribal knowledge only.
- Docs outside version control.

## Best Practices

- Docs-as-code.
- Update docs with code.
- Cross-link.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] Documentation exists and is current.
- [ ] Version-controlled and reviewed.
- [ ] Cross-links resolve.
- [ ] No secrets/PII included.
- [ ] Follows the style guide.
- [ ] RFC-2119 keywords used correctly.
- [ ] Cross-references resolve to existing documents.
- [ ] No secrets or sensitive data exposed.
- [ ] Version history updated.

## References

- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md)
- [Repository Catalogue (ROOT_INDEX)](../../../ROOT_INDEX.md)
- [Phase 06 Master Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use rule. |
