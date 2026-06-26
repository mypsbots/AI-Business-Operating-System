---
id: KN-000031
title: OWASP LLM Top 10
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
  - OWASP LLM Top 10
  - prompt injection
  - excessive agency
  - output handling
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - OWASP LLM Top 10
---

# OWASP LLM Top 10

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000031  •  **Category:** Security

## Tags

`OWASP LLM Top 10`, `prompt injection`, `excessive agency`, `output handling`

## Executive Summary

The OWASP Top 10 for LLM Applications catalogues the most critical security risks specific to LLM-powered systems.

## Purpose

To give people and AI agents a clear, reusable explanation of **OWASP LLM Top 10** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of owasp llm top 10 as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Prompt injection (direct and indirect).
- Insecure output handling.
- Training-data poisoning and model theft.
- Sensitive information disclosure.
- Excessive agency and insecure plugin/tool design.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding owasp llm top 10 helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, owasp llm top 10 is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Treat all model output as untrusted.
- Constrain agent/tool permissions (least privilege).
- Defend against direct and indirect prompt injection.

## Anti-patterns

- Trusting LLM output blindly.
- Giving agents excessive agency.
- Exposing secrets via prompts/outputs.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real owasp llm top 10 task and validate with the related checklist.

## FAQs

**Q: What is indirect prompt injection?**

A: Malicious instructions hidden in content the model retrieves (e.g. a web page or document).

**Q: What is 'excessive agency'?**

A: Granting an LLM/agent more capability or autonomy than the task safely requires.

## Decision Tree

- Is this about owasp llm top 10? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Study the OWASP LLM Top 10.
- Test prompt-injection defences.
- Apply least privilege to tools.

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
- [Zero Trust](./03_ZERO_TRUST_KNOWLEDGE_ARTICLE.md)
- [IAM](./04_IAM_KNOWLEDGE_ARTICLE.md)
- [Encryption](./05_ENCRYPTION_KNOWLEDGE_ARTICLE.md)
- [Secrets](./06_SECRETS_KNOWLEDGE_ARTICLE.md)
- [Incident Response](./07_INCIDENT_RESPONSE_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Security
- **Child topics:** see Related Knowledge below
- **Sibling topics:** OWASP, OWASP LLM Top 10, Zero Trust, IAM, Encryption, Secrets
- **Dependencies / related technologies:** OWASP LLM Top 10, prompt injection, excessive agency, output handling
- **Related business domains:** Security

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- OWASP LLM Top 10

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
| Keywords | OWASP LLM Top 10, prompt injection, excessive agency, output handling |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`OWASP LLM Top 10`, `prompt injection`, `excessive agency`, `output handling`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
