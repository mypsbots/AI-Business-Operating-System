---
id: RULE-000030
title: CI/CD Rule
document_type: Rule
category: Cloud And DevOps
phase: Phase 06
owner: Head of Platform
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - rule
  - cloud-and-devops
  - ci_cd_rule
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

# CI/CD Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000030  •  **Category:** Cloud And DevOps

## Executive Summary

This rule is the single source of truth for **CI/CD** in the AIBOS Enterprise. Automated pipelines that build, test and deploy software safely and frequently from version control. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for ci/cd so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect ci/cd across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Automated pipelines that build, test and deploy software safely and frequently from version control. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Progressive delivery** — Gradual rollout (canary/blue-green).

## Mandatory Requirements (MUST)

- Builds and tests MUST run automatically on every change.
- Deployments MUST be automated, repeatable and auditable.
- Pipelines MUST run security and quality gates before release.

## Recommended Practices (SHOULD)

- Pipelines SHOULD support fast rollback.
- Releases SHOULD use progressive delivery where risky.

## Optional Practices (MAY)

- Teams MAY deploy continuously to production behind flags.

## Rule Ownership Matrix

| Role | Assignment |
| --- | --- |
| Rule Owner | Head of Platform |
| Rule Approver | Chief Governance Architect |
| Mandatory Reviewers | Security Engineer, Compliance Specialist |
| Roles Required to Follow | All contributors within scope (human and AI) |
| Roles Allowed to Override | Head of Platform (with documented exception) |
| Escalation Authority | Governance Division |

## Applicable Departments

All departments performing ci/cd. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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

Exceptions MUST be requested from the rule owner (Head of Platform), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of Platform.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Deployment frequency
- Lead time
- Change-failure rate
- MTTR

## KPIs

- Deployment frequency
- Lead time
- Change-failure rate
- MTTR

## Risks

- Manual or gate-less delivery causes outages.

## Anti-patterns

- Manual deploys.
- Skipping gates under pressure.
- No rollback plan.

## Best Practices

- Automate everything.
- Keep pipelines fast.
- Make rollback trivial.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] CI runs build + tests on every PR.
- [ ] Security/quality gates enforced.
- [ ] Deployment is automated and auditable.
- [ ] Rollback path tested.
- [ ] Artifacts versioned and traceable.
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
