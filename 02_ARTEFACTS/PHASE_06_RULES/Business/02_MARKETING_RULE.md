---
id: RULE-000042
title: Marketing Rule
document_type: Rule
category: Business
phase: Phase 06
owner: Head of Business Operations
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - rule
  - business
  - marketing_rule
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

# Marketing Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000042  •  **Category:** Business

## Executive Summary

This rule is the single source of truth for **Marketing** in the AIBOS Enterprise. Generating awareness, demand and reputation for the product through content, channels and campaigns — including AI search visibility. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for marketing so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect marketing across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Generating awareness, demand and reputation for the product through content, channels and campaigns — including AI search visibility. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Attribution** — Crediting outcomes to channels/touchpoints.

## Mandatory Requirements (MUST)

- Campaigns MUST define audience, goal and success metrics.
- Claims MUST be accurate and compliant.
- Personal data MUST be handled lawfully (consent, privacy).

## Recommended Practices (SHOULD)

- Content SHOULD be optimised for SEO/AEO/GEO.
- Campaigns SHOULD be measured and iterated.

## Optional Practices (MAY)

- Teams MAY use AI to scale content with human review.

## Rule Ownership Matrix

| Role | Assignment |
| --- | --- |
| Rule Owner | Head of Business Operations |
| Rule Approver | Chief Governance Architect |
| Mandatory Reviewers | Security Engineer, Compliance Specialist |
| Roles Required to Follow | All contributors within scope (human and AI) |
| Roles Allowed to Override | Head of Business Operations (with documented exception) |
| Escalation Authority | Governance Division |

## Applicable Departments

All departments performing marketing. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| WCAG 2.2 AA | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (Head of Business Operations), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of Business Operations.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Qualified leads
- CAC
- Conversion
- Share of voice

## KPIs

- Qualified leads
- CAC
- Conversion
- Share of voice

## Risks

- Inaccurate or non-compliant marketing harms trust and law.

## Anti-patterns

- Vanity metrics only.
- Unsubstantiated claims.
- Ignoring privacy.

## Best Practices

- Define KPIs first.
- Measure attribution.
- Stay compliant.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] Audience, goal and KPI defined.
- [ ] Claims accurate and compliant.
- [ ] Tracking/attribution in place.
- [ ] Privacy/consent respected.
- [ ] Brand and accessibility guidelines met.
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
