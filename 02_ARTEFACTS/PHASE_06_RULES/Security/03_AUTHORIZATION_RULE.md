---
id: RULE-000023
title: Authorization Rule
document_type: Rule
category: Security
phase: Phase 06
owner: CISO
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - rule
  - security
  - authorization_rule
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

# Authorization Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000023  •  **Category:** Security

## Executive Summary

This rule is the single source of truth for **Authorization** in the AIBOS Enterprise. Controlling what an authenticated identity is allowed to do, using least privilege. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for authorization so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect authorization across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Controlling what an authenticated identity is allowed to do, using least privilege. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **RBAC** — Role-based access control.
- **IDOR** — Insecure direct object reference.

## Mandatory Requirements (MUST)

- Access MUST follow least privilege and deny by default.
- Authorisation MUST be enforced server-side on every request.
- Privileged actions MUST be logged and auditable.

## Recommended Practices (SHOULD)

- Roles/permissions SHOULD be modelled explicitly (RBAC/ABAC).
- Access SHOULD be reviewed periodically.

## Optional Practices (MAY)

- Systems MAY use policy-as-code for fine-grained control.

## Rule Ownership Matrix

| Role | Assignment |
| --- | --- |
| Rule Owner | CISO |
| Rule Approver | Chief Governance Architect |
| Mandatory Reviewers | Security Engineer, Compliance Specialist |
| Roles Required to Follow | All contributors within scope (human and AI) |
| Roles Allowed to Override | CISO (with documented exception) |
| Escalation Authority | Governance Division |

## Applicable Departments

All departments performing authorization. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| OWASP ASVS | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (CISO), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by CISO.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Excess-privilege findings
- IDOR incidents
- Review coverage

## KPIs

- Excess-privilege findings
- IDOR incidents
- Review coverage

## Risks

- Broken access control is a top breach cause.

## Anti-patterns

- Client-side-only checks.
- Over-broad admin roles.
- Missing object-level checks (IDOR).

## Best Practices

- Deny by default.
- Model RBAC/ABAC explicitly.
- Use policy-as-code (OPA).

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] Server-side authorisation on every sensitive action.
- [ ] Least-privilege roles defined.
- [ ] No insecure direct object references (IDOR).
- [ ] Privileged actions audited.
- [ ] Periodic access review evidence.
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
