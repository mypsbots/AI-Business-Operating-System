---
id: KN-000032
title: Zero Trust
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
  - zero trust
  - least privilege
  - identity
  - micro-segmentation
  - assume breach
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - NIST AI RMF
  - ISO 27001
---

# Zero Trust

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000032  •  **Category:** Security

## Tags

`zero trust`, `least privilege`, `identity`, `micro-segmentation`, `assume breach`

## Executive Summary

Zero Trust is a security model that assumes no implicit trust: every request is authenticated, authorised and verified regardless of network location.

## Purpose

To give people and AI agents a clear, reusable explanation of **Zero Trust** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of zero trust as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- 'Never trust, always verify.'
- Identity as the primary perimeter.
- Least privilege and micro-segmentation.
- Continuous verification and device posture.
- Assume breach; limit blast radius.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding zero trust helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, zero trust is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Verify every request explicitly.
- Apply least privilege everywhere.
- Segment networks and assume breach.

## Anti-patterns

- Trusting the internal network implicitly.
- Flat networks with no segmentation.
- Standing, over-broad access.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real zero trust task and validate with the related checklist.

## FAQs

**Q: What does Zero Trust replace?**

A: The old castle-and-moat model that trusted anything inside the network perimeter.

**Q: Is Zero Trust a product?**

A: No — it's an architecture/strategy implemented with identity, policy and segmentation.

## Decision Tree

- Is this about zero trust? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Learn the NIST Zero Trust model.
- Map identities and least privilege.
- Pilot micro-segmentation.

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
- [IAM](./04_IAM_KNOWLEDGE_ARTICLE.md)
- [Encryption](./05_ENCRYPTION_KNOWLEDGE_ARTICLE.md)
- [Secrets](./06_SECRETS_KNOWLEDGE_ARTICLE.md)
- [Incident Response](./07_INCIDENT_RESPONSE_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Security
- **Child topics:** see Related Knowledge below
- **Sibling topics:** OWASP, OWASP LLM Top 10, Zero Trust, IAM, Encryption, Secrets
- **Dependencies / related technologies:** zero trust, least privilege, identity, micro-segmentation, assume breach
- **Related business domains:** Security

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- NIST AI RMF
- ISO 27001

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
| Keywords | zero trust, least privilege, identity, micro-segmentation, assume breach |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`zero trust`, `least privilege`, `identity`, `micro-segmentation`, `assume breach`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
