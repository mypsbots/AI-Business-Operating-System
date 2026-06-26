---
id: RULE-000009
title: Integration Standards Rule
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
  - integration_standards_rule
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

# Integration Standards Rule

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Rules](../README.md) · [Phase 06 Prompt](../../../01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md)

**Rule ID:** RULE-000009  •  **Category:** Engineering

## Executive Summary

This rule is the single source of truth for **Integration Standards** in the AIBOS Enterprise. Reliable, secure, observable connections between systems using consistent patterns for data, events and errors. It is mandatory within its scope and inherits the [root standards](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md).

## Purpose

To set clear, enforceable, measurable expectations for integration standards so that human teams and AI agents act consistently and safely.

## Scope

Applies to all teams, services and AI agents that perform or affect integration standards across the enterprise. Concerns owned by other rules are referenced rather than duplicated.

## Business Rationale

Reliable, secure, observable connections between systems using consistent patterns for data, events and errors. Getting this right reduces risk, rework and cost while increasing trust, speed and compliance.

## Technical Rationale

Consistent, automated enforcement makes outcomes predictable, auditable and safe to scale across humans and AI agents.

## Definitions

- **Dead-letter queue** — Holds messages that repeatedly fail.

## Mandatory Requirements (MUST)

- Integrations MUST use authenticated, encrypted channels.
- Integrations MUST be idempotent and handle retries safely.
- Failures MUST be logged, alerted and recoverable.

## Recommended Practices (SHOULD)

- Integrations SHOULD use events/webhooks over tight coupling.
- Contracts SHOULD be versioned and documented.

## Optional Practices (MAY)

- Teams MAY use an iPaaS for low-code connectors.

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

All departments performing integration standards. See the [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

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
| OpenTelemetry | Applies to this rule. |

## Exceptions Process

Exceptions MUST be requested from the rule owner (Head of Engineering), be time-boxed, risk-assessed and recorded. Unapproved deviations are non-compliant.

## Approval Authority

This rule is approved by the Chief Governance Architect; exceptions are approved by Head of Engineering.

## Enforcement Model

Enforced through automated checks in CI, peer review and the related checklists. Violations are flagged, tracked and remediated.

## Metrics

- Integration uptime
- Duplicate/failure rate
- MTTR

## KPIs

- Integration uptime
- Duplicate/failure rate
- MTTR

## Risks

- Brittle integrations cause cascading failures.

## Anti-patterns

- Tight point-to-point coupling.
- No retry/idempotency handling.
- Silent failures.

## Best Practices

- Prefer events.
- Make everything idempotent.
- Observe every integration.

## Acceptance Criteria

- All MUST requirements are satisfied.
- Validation checklist passes.
- Ownership and exceptions are documented.
- Cross-references resolve.

## Validation Checklist

- [ ] Authenticated, encrypted transport.
- [ ] Idempotent processing (no duplicate side effects).
- [ ] Retry/back-off and dead-letter handling.
- [ ] Monitoring and alerting on failures.
- [ ] Contract documented and versioned.
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
