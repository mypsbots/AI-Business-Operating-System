---
id: RULE-000024
title: Secrets Management Rule
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
  - secrets_management_rule
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

# Secrets Management Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000024  •  **Category:** Security

## Executive Summary

This rule is the single source of truth for **Secrets Management** in the AIBOS Enterprise. Securely storing, distributing and rotating credentials, keys and tokens so they never leak. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for secrets management so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect secrets management across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Securely storing, distributing and rotating credentials, keys and tokens so they never leak. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Secret** — A credential, key or token that grants access.

## Mandatory Requirements (MUST)

- Secrets MUST be stored in a managed secrets manager, never in code or config.
- Secrets MUST be rotated on a schedule and on compromise.
- Access to secrets MUST be least-privilege and audited.

## Recommended Practices (SHOULD)

- Secrets SHOULD be injected at runtime, not baked into images.
- CI SHOULD scan for accidentally committed secrets.

## Optional Practices (MAY)

- Teams MAY use dynamic, short-lived secrets.

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

All departments performing secrets management. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| ISO 27001 | Applies to this rule. |
| OWASP ASVS | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (CISO), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by CISO.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Secret-leak incidents
- Rotation compliance
- Time-to-rotate

## KPIs

- Secret-leak incidents
- Rotation compliance
- Time-to-rotate

## Risks

- Leaked secrets cause immediate compromise.

## Anti-patterns

- Secrets in .env committed to Git.
- Shared static credentials.
- No rotation.

## Best Practices

- Use a vault.
- Rotate automatically.
- Scan history for leaks.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] No secrets in source, config or images.
- [ ] Secrets stored in a managed vault.
- [ ] Rotation schedule defined and followed.
- [ ] Access least-privilege and audited.
- [ ] CI secret-scanning enabled.
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
