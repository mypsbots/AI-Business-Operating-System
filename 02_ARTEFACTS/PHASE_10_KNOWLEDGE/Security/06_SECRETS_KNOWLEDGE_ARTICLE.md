---
id: KN-000035
title: Secrets
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
  - secrets
  - vault
  - rotation
  - secret scanning
  - dynamic secrets
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - ISO 27001
  - OWASP ASVS
---

# Secrets

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000035  •  **Category:** Security

## Tags

`secrets`, `vault`, `rotation`, `secret scanning`, `dynamic secrets`

## Executive Summary

Secrets management securely stores, distributes and rotates credentials, keys and tokens so they never leak into code, logs or images.

## Purpose

To give people and AI agents a clear, reusable explanation of **Secrets** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of secrets as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Centralised secret stores (Vault, cloud managers).
- Runtime injection, not baked-in secrets.
- Rotation and dynamic, short-lived secrets.
- Secret scanning in CI and history.
- Least-privilege, audited access.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding secrets helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, secrets is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Never commit secrets; use a vault.
- Rotate automatically and on compromise.
- Scan code and history for leaks.

## Anti-patterns

- Secrets in .env committed to Git.
- Shared static credentials.
- No rotation.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real secrets task and validate with the related checklist.

## FAQs

**Q: Where should secrets live?**

A: In a managed secrets manager/vault, injected at runtime — never in code, config or images.

**Q: What are dynamic secrets?**

A: Short-lived credentials generated on demand and automatically expired.

## Decision Tree

- Is this about secrets? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Use a secrets manager.
- Add secret scanning (gitleaks).
- Implement rotation.

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
- [Incident Response](./07_INCIDENT_RESPONSE_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Security
- **Child topics:** see Related Knowledge below
- **Sibling topics:** OWASP, OWASP LLM Top 10, Zero Trust, IAM, Encryption, Secrets
- **Dependencies / related technologies:** secrets, vault, rotation, secret scanning, dynamic secrets
- **Related business domains:** Security

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- ISO 27001
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
| Keywords | secrets, vault, rotation, secret scanning, dynamic secrets |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`secrets`, `vault`, `rotation`, `secret scanning`, `dynamic secrets`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
