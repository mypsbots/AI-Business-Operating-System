---
id: KN-000036
title: Incident Response
document_type: Knowledge Article
category: Security
phase: Phase 10
owner: Chief Knowledge Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - incident response
  - severity
  - post-mortem
  - MTTR
  - runbook
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - ISO 27001
  - SOC 2
---

# Incident Response

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000036  •  **Category:** Security

## Tags

`incident response`, `severity`, `post-mortem`, `MTTR`, `runbook`

## Executive Summary

Incident response is the structured process to detect, contain, resolve and learn from security and operational incidents.

## Purpose

To give people and AI agents a clear, reusable explanation of **Incident Response** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of incident response as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Lifecycle: prepare, detect, contain, eradicate, recover, learn.
- Severity levels and an incident commander.
- Communication and regulatory notification.
- Blameless post-mortems.
- Runbooks and game days.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding incident response helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, incident response is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Define severities and roles in advance.
- Communicate clearly during incidents.
- Run blameless post-mortems and track actions.

## Anti-patterns

- No clear commander.
- Blaming individuals.
- Skipping the post-mortem.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real incident response task and validate with the related checklist.

## FAQs

**Q: What is an incident commander?**

A: The single person coordinating the response and communications.

**Q: Why blameless post-mortems?**

A: They surface systemic causes honestly, leading to real fixes.

## Decision Tree

- Is this about incident response? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Learn the IR lifecycle (NIST/SANS).
- Write a runbook.
- Run a game day.

## Prerequisites

Familiarity with the AIBOS [Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md) and the basics of this domain.

## Related Skills

See the [Specialist Skills](../../PHASE_05_SKILLS/README.md).

## Related Rules

See the [Enterprise Rules](../../PHASE_06_RULES/README.md).

## Related Checklists

See the [Enterprise Checklists](../../PHASE_07_CHECKLISTS/README.md).

## Related Playbooks

See the [Enterprise Playbooks](../../PHASE_08_PLAYBOOKS/README.md).

## Related Templates

See the [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md).

## Related Knowledge

- [OWASP](./01_OWASP_KNOWLEDGE_ARTICLE.md)
- [OWASP LLM Top 10](./02_OWASP_LLM_TOP_10_KNOWLEDGE_ARTICLE.md)
- [Zero Trust](./03_ZERO_TRUST_KNOWLEDGE_ARTICLE.md)
- [IAM](./04_IAM_KNOWLEDGE_ARTICLE.md)
- [Encryption](./05_ENCRYPTION_KNOWLEDGE_ARTICLE.md)
- [Secrets](./06_SECRETS_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Security
- **Child topics:** see Related Knowledge below
- **Sibling topics:** OWASP, OWASP LLM Top 10, Zero Trust, IAM, Encryption, Secrets
- **Dependencies / related technologies:** incident response, severity, post-mortem, MTTR, runbook
- **Related business domains:** Security

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- ISO 27001
- SOC 2

## References

- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md)
- [Repository Catalogue (ROOT_INDEX)](../../../ROOT_INDEX.md)
- [Phase 10 Master Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

## AI Retrieval Metadata

| Field | Value |
| --- | --- |
| Document type | Knowledge Article |
| Domain | Security |
| Audience | Humans, AI agents, RAG, enterprise search |
| Keywords | incident response, severity, post-mortem, MTTR, runbook |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`incident response`, `severity`, `post-mortem`, `MTTR`, `runbook`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
