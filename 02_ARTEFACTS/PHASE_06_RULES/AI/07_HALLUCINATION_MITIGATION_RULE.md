---
id: RULE-000019
title: Hallucination Mitigation Rule
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
  - hallucination_mitigation_rule
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

# Hallucination Mitigation Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000019  •  **Category:** AI

## Executive Summary

This rule is the single source of truth for **Hallucination Mitigation** in the AIBOS Enterprise. Reducing and detecting confident-but-wrong AI output through grounding, verification and guardrails. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for hallucination mitigation so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect hallucination mitigation across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Reducing and detecting confident-but-wrong AI output through grounding, verification and guardrails. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Hallucination** — Confident but incorrect AI output.

## Mandatory Requirements (MUST)

- User-facing factual claims MUST be grounded or clearly caveated.
- High-stakes outputs MUST be verifiable or human-reviewed.
- Hallucination rate MUST be measured for key features.

## Recommended Practices (SHOULD)

- Answers SHOULD cite sources where possible.
- Systems SHOULD detect low-confidence/unsupported answers.

## Optional Practices (MAY)

- Teams MAY use self-checking or verifier models.

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

All departments performing hallucination mitigation. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| ISO 42001 | Applies to this rule. |
| OWASP LLM Top 10 | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (Head of AI Engineering), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of AI Engineering.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Hallucination rate
- Citation accuracy
- User-reported errors

## KPIs

- Hallucination rate
- Citation accuracy
- User-reported errors

## Risks

- Hallucinations mislead users and create liability.

## Anti-patterns

- Presenting unsupported claims confidently.
- No way to say 'I don't know'.

## Best Practices

- Ground in sources.
- Cite.
- Measure and reduce.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] Grounding/citations for factual claims.
- [ ] Hallucination rate measured.
- [ ] Low-confidence handling defined.
- [ ] High-stakes output reviewed.
- [ ] Fallbacks for 'I don't know'.
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
