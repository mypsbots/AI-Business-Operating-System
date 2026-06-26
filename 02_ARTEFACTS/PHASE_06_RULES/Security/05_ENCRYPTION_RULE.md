---
id: RULE-000025
title: Encryption Rule
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
  - encryption_rule
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

# Encryption Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000025  •  **Category:** Security

## Executive Summary

This rule is the single source of truth for **Encryption** in the AIBOS Enterprise. Protecting data confidentiality and integrity in transit and at rest using strong, standard cryptography. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for encryption so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect encryption across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Protecting data confidentiality and integrity in transit and at rest using strong, standard cryptography. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **KMS** — Key Management Service.
- **Envelope encryption** — Encrypting data keys with a master key.

## Mandatory Requirements (MUST)

- Data in transit MUST use TLS 1.2+; data at rest MUST be encrypted.
- Only strong, standard algorithms MUST be used (no custom crypto).
- Encryption keys MUST be managed and rotated securely.

## Recommended Practices (SHOULD)

- Sensitive fields SHOULD be encrypted at the application layer.
- Key access SHOULD be least-privilege and audited.

## Optional Practices (MAY)

- Teams MAY use envelope encryption and HSMs.

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

All departments performing encryption. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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

- % data encrypted
- Key-rotation compliance
- TLS coverage

## KPIs

- % data encrypted
- Key-rotation compliance
- TLS coverage

## Risks

- Unencrypted data exposes the business in a breach.

## Anti-patterns

- Self-rolled crypto.
- Hard-coded keys.
- Unencrypted backups.

## Best Practices

- Use platform KMS.
- Rotate keys.
- Encrypt sensitive fields.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] TLS 1.2+ enforced everywhere.
- [ ] At-rest encryption enabled on stores.
- [ ] Standard algorithms only; no custom crypto.
- [ ] Keys managed in a KMS and rotated.
- [ ] Key access audited.
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
