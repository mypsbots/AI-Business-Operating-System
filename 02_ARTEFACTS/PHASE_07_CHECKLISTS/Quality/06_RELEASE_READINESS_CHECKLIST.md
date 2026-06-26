---
id: CHECK-000039
title: Release Readiness Checklist
document_type: Checklist
category: Quality
phase: Phase 07
owner: Chief Quality and Compliance Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - checklist
  - quality
  - release_readiness_checklist
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_07_CHECKLISTS_MASTER_PROMPT.md
standards:
  - ISO 42001
  - ISO 27001
  - NIST AI RMF
  - SOC 2
  - OWASP ASVS
  - OWASP LLM Top 10
  - WCAG 2.2 AA
---

# Release Readiness Checklist

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Checklists](../README.md) · [Phase 07 Prompt](../../../01_PHASES/PHASE_07_CHECKLISTS_MASTER_PROMPT.md)

**Checklist ID:** CHECK-000039  •  **Category:** Quality

## Purpose

To validate release readiness objectively and repeatably before it passes its quality gate. Every item is binary (Pass/Fail) and auditable.

## Scope

Applies whenever release readiness is performed or reviewed, by human reviewers or AI agents.

## Prerequisites

- The relevant rule(s) and standards have been read.
- Required inputs and access are available.
- The artefact under review is complete enough to assess.

## Inputs

- The artefact or change under review.
- Relevant requirements, designs and acceptance criteria.

## Outputs

- A completed checklist with Pass/Fail per item.
- Recorded evidence and a sign-off decision.

## Roles Responsible

- Reviewer (human or AI agent) — performs the checklist.
- Approver — signs off the quality gate.
- Owner of the artefact — remediates failures.

## Quality Gate

This checklist is the gate for release readiness; the artefact MUST NOT progress until all mandatory items pass.

## Acceptance Criteria

- All mandatory items pass.
- Evidence is captured for each item.
- Failures are remediated or formally accepted.

## Validation Steps

- [ ] Release-readiness checklist passed.
- [ ] Version and changelog produced.
- [ ] Rollback plan in place.
- [ ] Stakeholders notified.
- [ ] Post-release monitoring planned.

## Pass / Fail Criteria

- **Pass** — all mandatory items are satisfied with evidence.
- **Fail** — any mandatory item is unmet; remediate and re-run.
- **Conditional** — minor items deferred with an approved exception.

## Evidence Required

- Links to passing CI runs, scans or test reports.
- Screenshots or logs demonstrating each check.
- Reviewer and approver identities and timestamps.

## Required Skills

Reviewers should hold the relevant [Specialist Skills](../../PHASE_05_SKILLS/README.md).

## Required Rules

This checklist enforces the [Enterprise Rules](../../PHASE_06_RULES/README.md).

## Related Playbooks

Used within the [Enterprise Playbooks](../../PHASE_08_PLAYBOOKS/README.md).

## Related Templates

Supported by the [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md).

## Related Knowledge Articles

Background in the [Enterprise Knowledge base](../../PHASE_10_KNOWLEDGE/README.md).

## Security Validation

- [ ] Authentication and authorisation enforced on all sensitive actions.
- [ ] No secrets or credentials exposed in code, config, logs or output.
- [ ] Inputs validated and outputs safely encoded.
- [ ] Dependencies scanned; no unresolved critical vulnerabilities.

## Privacy Validation

- [ ] Personal data is minimised and lawfully processed.
- [ ] Sensitive data is masked in logs and encrypted at rest/in transit.
- [ ] Retention and deletion rules are respected.

## AI Validation

- [ ] AI outputs are grounded/cited where factual.
- [ ] Human-in-the-loop approval exists for high-risk AI actions.
- [ ] Prompt-injection and unsafe-output guardrails are in place.

## Compliance Validation

- [ ] Relevant controls (ISO 27001/42001, SOC 2) are satisfied.
- [ ] Evidence is captured and retained for audit.
- [ ] Exceptions are documented and approved.

## Accessibility Validation

- [ ] UI meets WCAG 2.2 AA (contrast, labels, keyboard).
- [ ] Automated accessibility scan passes.

## Performance Validation

- [ ] Performance budgets/SLAs are met (p95/p99).
- [ ] No unresolved performance regressions.

## Deployment Readiness

- [ ] Deployment is automated, versioned and traceable.
- [ ] Post-deploy health checks pass.

## Rollback Readiness

- [ ] A tested rollback path exists.
- [ ] Database changes are backward compatible.

## Reviewer Sign-off

| Field | Value |
| --- | --- |
| Reviewer | _(name / agent)_ |
| Decision | Pass / Fail |
| Date | _(date)_ |
| Notes | _(notes)_ |

## Escalation Process

If items cannot be resolved, escalate to the artefact owner, then to the governing rule owner, then to the Governance Division.

## Risks

- Poorly managed releases cause outages and confusion.

## References

- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Repository Catalogue (ROOT_INDEX)](../../../ROOT_INDEX.md)
- [Phase 07 Master Prompt](../../../01_PHASES/PHASE_07_CHECKLISTS_MASTER_PROMPT.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use checklist. |
