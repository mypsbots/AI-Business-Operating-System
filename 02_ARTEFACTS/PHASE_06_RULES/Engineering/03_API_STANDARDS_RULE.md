---
id: RULE-000007
title: API Standards Rule
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
  - api_standards_rule
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

# API Standards Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000007  •  **Category:** Engineering

## Executive Summary

This rule is the single source of truth for **API Standards** in the AIBOS Enterprise. Consistent, versioned, well-documented API contracts so internal teams, partners and AI agents can integrate reliably. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for api standards so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect api standards across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Consistent, versioned, well-documented API contracts so internal teams, partners and AI agents can integrate reliably. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Idempotency** — Repeating a request has no additional effect.
- **OpenAPI** — A standard machine-readable API description.

## Mandatory Requirements (MUST)

- APIs MUST be described by an OpenAPI (or GraphQL/Proto) specification.
- APIs MUST use semantic versioning and avoid breaking changes without a new version.
- APIs MUST enforce authentication and authorisation.
- APIs MUST validate inputs and return consistent error formats.

## Recommended Practices (SHOULD)

- APIs SHOULD be paginated, idempotent where appropriate and rate-limited.
- APIs SHOULD publish a changelog and deprecation policy.

## Optional Practices (MAY)

- APIs MAY expose tool/function schemas for AI-agent consumption.

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

All departments performing api standards. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| OpenAPI | Applies to this rule. |
| OAuth 2.1 | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (Head of Engineering), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of Engineering.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Breaking-change incidents
- Spec coverage
- p95 latency
- Time-to-integrate

## KPIs

- Breaking-change incidents
- Spec coverage
- p95 latency
- Time-to-integrate

## Risks

- Breaking changes disrupt integrations and agents.

## Anti-patterns

- Breaking changes shipped silently.
- Inconsistent error formats.
- Undocumented endpoints.

## Best Practices

- Design API-first from the spec.
- Contract-test against the spec.
- Treat the API as a product with clear DX.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] OpenAPI/GraphQL spec present and valid.
- [ ] Versioning strategy applied; no unversioned breaking change.
- [ ] AuthN/AuthZ enforced on every endpoint.
- [ ] Input validation and consistent error schema.
- [ ] Rate limiting and pagination where relevant.
- [ ] Idempotency for unsafe operations.
- [ ] Documentation published.
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
