---
id: RULE-000012
title: Code Reviews Rule
document_type: Rule
category: Engineering
phase: Phase 06
owner: Head of Engineering
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - rule
  - engineering
  - code_reviews_rule
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

# Code Reviews Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000012  •  **Category:** Engineering

## Executive Summary

This rule is the single source of truth for **Code Reviews** in the AIBOS Enterprise. Peer review of proposed code changes to catch defects, share knowledge and uphold standards before code is merged. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for code reviews so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect code reviews across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Peer review of proposed code changes to catch defects, share knowledge and uphold standards before code is merged. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **PR** — Pull request: a proposed set of changes for review.

## Mandatory Requirements (MUST)

- Every change MUST be reviewed and approved by at least one other engineer.
- Reviewers MUST verify tests, security and adherence to standards.
- CI MUST pass before a pull request can be merged.
- Security-sensitive changes MUST receive a security-aware review.

## Recommended Practices (SHOULD)

- Pull requests SHOULD be small and focused.
- Reviewers SHOULD respond within one business day.
- Authors SHOULD provide context and a testing summary.

## Optional Practices (MAY)

- Teams MAY use AI-assisted review to augment (not replace) humans.

## Rule Ownership Matrix

| Role | Assignment |
| --- | --- |
| Rule Owner | Head of Engineering |
| Rule Approver | Chief Governance Architect |
| Mandatory Reviewers | Security Engineer, Compliance Specialist |
| Roles Required to Follow | All contributors within scope (human and AI) |
| Roles Allowed to Override | Head of Engineering (with documented exception) |
| Escalation Authority | Governance Division |

## Applicable Departments

All departments performing code reviews. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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

Exceptions MUST be requested from the rule owner (Head of Engineering), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of Engineering.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Review turnaround time
- PR size
- Defect escape rate
- Review coverage

## KPIs

- Review turnaround time
- PR size
- Defect escape rate
- Review coverage

## Risks

- Weak review lets defects and vulnerabilities through.

## Anti-patterns

- Rubber-stamp approvals.
- Giant PRs that cannot be reviewed.
- Self-merging without review.

## Best Practices

- Keep PRs under ~400 lines.
- Automate the mechanical checks.
- Be kind, specific and timely in feedback.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] At least one approving human review recorded.
- [ ] All CI checks green.
- [ ] PR description explains what and why.
- [ ] Tests cover the change and pass.
- [ ] No secrets or sensitive data in the diff.
- [ ] Linked to an issue or ticket.
- [ ] Breaking changes called out and documented.
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
