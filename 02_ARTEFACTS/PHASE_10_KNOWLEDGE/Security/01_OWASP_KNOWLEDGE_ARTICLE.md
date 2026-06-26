---
id: KN-000030
title: OWASP
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
  - OWASP
  - Top 10
  - ASVS
  - access control
  - injection
  - ZAP
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - OWASP ASVS
---

# OWASP

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000030  •  **Category:** Security

## Tags

`OWASP`, `Top 10`, `ASVS`, `access control`, `injection`, `ZAP`

## Executive Summary

OWASP (Open Worldwide Application Security Project) provides free, community-driven standards and tools for application security, most famously the OWASP Top 10.

## Purpose

To give people and AI agents a clear, reusable explanation of **OWASP** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of owasp as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- The OWASP Top 10 web risks (e.g. broken access control, injection).
- ASVS — a verification standard for security requirements.
- Cheat Sheets for practical guidance.
- Tools like ZAP and Dependency-Check.
- Security as a continuous practice.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding owasp helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, owasp is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Design against the OWASP Top 10.
- Use ASVS to set verification requirements.
- Adopt OWASP cheat sheets and tools.

## Anti-patterns

- Treating the Top 10 as a checklist-only exercise.
- Ignoring access control (the #1 risk).
- No verification standard.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real owasp task and validate with the related checklist.

## FAQs

**Q: What is the OWASP Top 10?**

A: A regularly updated list of the most critical web application security risks.

**Q: What is ASVS?**

A: The Application Security Verification Standard — a framework of security requirements and levels.

## Decision Tree

- Is this about owasp? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Study the OWASP Top 10.
- Map ASVS requirements to a project.
- Run OWASP ZAP against a test app.

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

- [OWASP LLM Top 10](./02_OWASP_LLM_TOP_10_KNOWLEDGE_ARTICLE.md)
- [Zero Trust](./03_ZERO_TRUST_KNOWLEDGE_ARTICLE.md)
- [IAM](./04_IAM_KNOWLEDGE_ARTICLE.md)
- [Encryption](./05_ENCRYPTION_KNOWLEDGE_ARTICLE.md)
- [Secrets](./06_SECRETS_KNOWLEDGE_ARTICLE.md)
- [Incident Response](./07_INCIDENT_RESPONSE_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Security
- **Child topics:** see Related Knowledge below
- **Sibling topics:** OWASP, OWASP LLM Top 10, Zero Trust, IAM, Encryption, Secrets
- **Dependencies / related technologies:** OWASP, Top 10, ASVS, access control, injection
- **Related business domains:** Security

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- OWASP ASVS

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
| Keywords | OWASP, Top 10, ASVS, access control, injection, ZAP |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`OWASP`, `Top 10`, `ASVS`, `access control`, `injection`, `ZAP`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
