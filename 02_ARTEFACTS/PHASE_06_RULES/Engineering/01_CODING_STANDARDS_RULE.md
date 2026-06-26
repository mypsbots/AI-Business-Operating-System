---
id: RULE-000005
title: Coding Standards Rule
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
  - coding_standards_rule
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

# Coding Standards Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000005  •  **Category:** Engineering

## Executive Summary

This rule is the single source of truth for **Coding Standards** in the AIBOS Enterprise. Consistent, readable, maintainable source code across all teams and languages, enforced automatically wherever possible. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for coding standards so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect coding standards across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Consistent, readable, maintainable source code across all teams and languages, enforced automatically wherever possible. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Linter** — A tool that flags style and correctness issues.
- **Formatter** — A tool that rewrites code to a canonical style.

## Mandatory Requirements (MUST)

- Code MUST pass automated linting and formatting in CI before merge.
- Code MUST follow the agreed style guide for its language.
- Public functions and modules MUST have clear names and documentation.
- Code MUST NOT contain hard-coded secrets or credentials.
- Every change MUST be covered by tests appropriate to its risk.

## Recommended Practices (SHOULD)

- Functions SHOULD be small and single-purpose.
- Complex logic SHOULD include explanatory comments on intent.
- Dead code and TODOs SHOULD be removed or tracked as issues.

## Optional Practices (MAY)

- Teams MAY adopt stricter language-specific conventions.
- Teams MAY use AI assistants to draft and refactor code.

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

All departments performing coding standards. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| Twelve-Factor App | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (Head of Engineering), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of Engineering.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Lint pass rate
- Code duplication %
- Average PR size
- Test coverage

## KPIs

- Lint pass rate
- Code duplication %
- Average PR size
- Test coverage

## Risks

- Inconsistent code slows onboarding and review.
- Unscanned code leaks secrets.

## Anti-patterns

- Inconsistent formatting committed manually.
- God functions/classes doing too much.
- Copy-paste duplication instead of reuse.

## Best Practices

- Automate formatting on save and in CI.
- Adopt a single shared style guide per language.
- Review for readability, not just correctness.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] Linter and formatter pass with no errors.
- [ ] No hard-coded secrets detected by scanning.
- [ ] Naming follows the style guide.
- [ ] Tests added/updated for the change.
- [ ] No commented-out or dead code introduced.
- [ ] Cyclomatic complexity within agreed limits.
- [ ] Public APIs documented.
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
