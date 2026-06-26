---
id: PLAY-000006
title: Product Validation Playbook
document_type: Playbook
category: Product
phase: Phase 08
owner: Chief Operations Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - playbook
  - product
  - product_validation_playbook
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_08_PLAYBOOKS_MASTER_PROMPT.md
standards:
  - ISO 42001
  - ISO 27001
  - NIST AI RMF
  - SOC 2
  - OWASP ASVS
  - OWASP LLM Top 10
  - WCAG 2.2 AA
---

# Product Validation Playbook

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Playbooks](../README.md) · [Phase 08 Prompt](../../../01_PHASES/PHASE_08_PLAYBOOKS_MASTER_PROMPT.md)

**Playbook ID:** PLAY-000006  •  **Category:** Product

## Executive Summary

A repeatable, automatable workflow for **Product Validation**. Discovering customer problems and prioritising what to build to deliver measurable business and user value. It is executable by human teams and AI agents with clear human-approval points.

## Business Objective

Make product validation consistent, fast, safe and auditable across the enterprise.

## Scope

Covers the end-to-end product validation workflow. Out-of-scope concerns are delegated to their own playbooks.

## Trigger Conditions

- New opportunity
- Customer feedback
- Quarter planning

## Preconditions

- Required inputs, access and approvals are available.
- Relevant rules and checklists are known.

## Inputs

- The request/context that triggered the workflow.
- Relevant data, artefacts and configuration.

## Outputs

- The completed outcome of the workflow.
- Evidence, audit trail and any follow-up actions.

## Roles Responsible

- Product Manager
- Team

## AI Agents Involved

- Task agent(s) that execute eligible steps.
- Reviewer/evaluator agent that checks outputs.
- Orchestrator that coordinates and escalates.

## Human Approval Points

- Before any high-risk or irreversible action.
- At the final approval/sign-off step.

## Workflow Overview

The workflow proceeds through 4 main steps with a decision point that routes high-risk actions to human approval.

## Mermaid Workflow Diagram

```mermaid
flowchart TD
    S([Trigger]) --> A0
    A0["Product Manager: Discover and validate the problem."]
    A1["Product Manager: Define success metrics and scope."]
    A0 --> A1
    A2["Team: Build and launch."]
    A1 --> A2
    A3["Product Manager: Review outcomes and iterate."]
    A2 --> A3
    A3 --> D{High-risk?}
    D -->|Yes| H[Human approval]
    D -->|No| E[Execute]
    H --> E --> R([Record audit trail])
```

## Step-by-Step Procedure

| Step | Actor | Action |
| --- | --- | --- |
| 1 | Product Manager | Discover and validate the problem. |
| 2 | Product Manager | Define success metrics and scope. |
| 3 | Team | Build and launch. |
| 4 | Product Manager | Review outcomes and iterate. |

## Decision Branches

- If the action is high-risk or irreversible -> require human approval.
- If validation fails -> remediate and repeat the step.
- If blocked -> follow the escalation path.

## Exception Handling

- Capture the error and context.
- Apply the documented fallback or safe-stop.
- Open an incident if customer impact is possible.

## Escalation Path

Owner -> domain lead -> Governance Division, with severity-based timelines.

## Required Skills

Executed by holders of the relevant [Specialist Skills](../../PHASE_05_SKILLS/README.md).

## Required Rules

Must comply with the [Enterprise Rules](../../PHASE_06_RULES/README.md).

## Required Checklists

Validated using the [Enterprise Checklists](../../PHASE_07_CHECKLISTS/README.md).

## Required Templates

Uses the [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md).

## Required Knowledge Articles

Background in the [Enterprise Knowledge base](../../PHASE_10_KNOWLEDGE/README.md).

## Automation Opportunities

- Automate repeatable steps and validations in CI/CD or workflows.
- Use AI agents for drafting, triage and checks.
- Auto-collect evidence and update tracking systems.

## Integration Points

- GitHub / GitLab (code, PRs, actions).
- Jira / Linear (tracking).
- Slack / Teams (notifications).
- Vercel / cloud (deploy).
- n8n / Make (orchestration).

## KPIs

- Adoption/activation
- Outcome vs target
- Cycle time

## SLAs

- Acknowledge triggers within 1 business day.
- Complete standard runs within the agreed target time.
- Resolve exceptions per severity SLA.

## Risks

- Building the wrong thing wastes effort.

## Best Practices

- Validate first.
- Prioritise ruthlessly.
- Measure outcomes.

## Anti-patterns

- Building without validating.
- No success metric.
- Feature factory.

## Definition of Done

- Outcome achieved and validated.
- Audit trail recorded.
- Follow-up actions tracked.

## Acceptance Criteria

- All steps completed or consciously skipped with reason.
- Required checklist passed.
- Approvals obtained.

## Post-Implementation Review

Review outcomes against objectives; capture lessons and improvement actions.

## Continuous Improvement

Feed metrics and lessons back into this playbook; update on a regular cadence.

## Validation Checklist

- [ ] Trigger and preconditions verified.
- [ ] Steps executed in order with evidence.
- [ ] Human approval obtained for high-risk actions.
- [ ] Required checklist passed.
- [ ] Audit trail recorded.
- [ ] Cross-references resolve.

## References

- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Repository Catalogue (ROOT_INDEX)](../../../ROOT_INDEX.md)
- [Phase 08 Master Prompt](../../../01_PHASES/PHASE_08_PLAYBOOKS_MASTER_PROMPT.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use playbook. |
