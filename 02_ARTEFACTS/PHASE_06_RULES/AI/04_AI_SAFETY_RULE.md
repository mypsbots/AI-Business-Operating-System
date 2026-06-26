---
id: RULE-000016
title: AI Safety Rule
document_type: Rule
category: AI
phase: Phase 06
owner: Head of AI Engineering
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - rule
  - ai
  - ai_safety_rule
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

# AI Safety Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000016  •  **Category:** AI

## Executive Summary

This rule is the single source of truth for **AI Safety** in the AIBOS Enterprise. Keeping AI behaviour within safe, lawful, policy-compliant boundaries through guardrails, red-teaming and oversight. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for ai safety so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect ai safety across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Keeping AI behaviour within safe, lawful, policy-compliant boundaries through guardrails, red-teaming and oversight. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Red-teaming** — Adversarial testing for unsafe behaviour.

## Mandatory Requirements (MUST)

- AI features MUST have guardrails against harmful/unsafe output.
- High-risk AI actions MUST keep a human in the loop.
- AI systems MUST be red-teamed before release and monitored after.

## Recommended Practices (SHOULD)

- Safety incidents SHOULD have a response process.
- Outputs SHOULD be filtered for policy compliance.

## Optional Practices (MAY)

- Teams MAY use external safety models (e.g. Llama Guard).

## Rule Ownership Matrix

| Role | Assignment |
| --- | --- |
| Rule Owner | Head of AI Engineering |
| Rule Approver | Chief Governance Architect |
| Mandatory Reviewers | Security Engineer, Compliance Specialist |
| Roles Required to Follow | All contributors within scope (human and AI) |
| Roles Allowed to Override | Head of AI Engineering (with documented exception) |
| Escalation Authority | Governance Division |

## Applicable Departments

All departments performing ai safety. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| NIST AI RMF | Applies to this rule. |
| ISO 42001 | Applies to this rule. |
| OWASP LLM Top 10 | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (Head of AI Engineering), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of AI Engineering.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Unsafe-output rate
- Jailbreak success rate
- Time-to-mitigate

## KPIs

- Unsafe-output rate
- Jailbreak success rate
- Time-to-mitigate

## Risks

- Unsafe AI output harms users and the business.

## Anti-patterns

- No guardrails.
- Full autonomy for risky actions.
- No red-teaming.

## Best Practices

- Layer guardrails.
- Keep humans in the loop.
- Red-team.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] Guardrails/content filters in place.
- [ ] Human-in-the-loop on high-risk actions.
- [ ] Red-team testing completed.
- [ ] OWASP LLM Top 10 considered.
- [ ] Monitoring and incident process defined.
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
