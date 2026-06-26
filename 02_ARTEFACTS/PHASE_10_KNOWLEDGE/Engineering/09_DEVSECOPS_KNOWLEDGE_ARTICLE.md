---
id: KN-000016
title: DevSecOps
document_type: Knowledge Article
category: Engineering
phase: Phase 10
owner: Chief Knowledge Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - DevSecOps
  - shift-left
  - SAST
  - SCA
  - SBOM
  - supply chain
  - OPA
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - OWASP ASVS
---

# DevSecOps

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000016  •  **Category:** Engineering

## Tags

`DevSecOps`, `shift-left`, `SAST`, `SCA`, `SBOM`, `supply chain`, `OPA`

## Executive Summary

DevSecOps builds security into the delivery pipeline so it is automated, continuous and everyone's responsibility — 'shift left'.

## Purpose

To give people and AI agents a clear, reusable explanation of **DevSecOps** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of devsecops as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Security gates in CI: SAST, SCA, secret scanning, IaC scanning.
- Shift-left: find issues early and cheaply.
- Supply-chain security (SBOM, signing, provenance).
- Policy as code enforces guardrails.
- Runtime security and continuous monitoring.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding devsecops helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, devsecops is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Automate security scanning in CI.
- Generate and track an SBOM; sign artifacts.
- Enforce policy as code.

## Anti-patterns

- Security only at the end (gate of pain).
- Ignoring dependency vulnerabilities.
- No software supply-chain controls.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real devsecops task and validate with the related checklist.

## FAQs

**Q: What is shift-left security?**

A: Moving security checks earlier in the lifecycle, into development and CI.

**Q: What is an SBOM?**

A: A Software Bill of Materials — an inventory of components and dependencies.

## Decision Tree

- Is this about devsecops? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Add SAST/SCA to a pipeline.
- Learn supply-chain security (SLSA).
- Try policy-as-code with OPA.

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

- [Architecture](./01_ARCHITECTURE_KNOWLEDGE_ARTICLE.md)
- [Frontend](./02_FRONTEND_KNOWLEDGE_ARTICLE.md)
- [Backend](./03_BACKEND_KNOWLEDGE_ARTICLE.md)
- [API](./04_API_KNOWLEDGE_ARTICLE.md)
- [Integration](./05_INTEGRATION_KNOWLEDGE_ARTICLE.md)
- [Database](./06_DATABASE_KNOWLEDGE_ARTICLE.md)
- [Cloud](./07_CLOUD_KNOWLEDGE_ARTICLE.md)
- [DevOps](./08_DEVOPS_KNOWLEDGE_ARTICLE.md)
- [Observability](./10_OBSERVABILITY_KNOWLEDGE_ARTICLE.md)
- [Testing](./11_TESTING_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Engineering
- **Child topics:** see Related Knowledge below
- **Sibling topics:** Architecture, Frontend, Backend, API, Integration, Database
- **Dependencies / related technologies:** DevSecOps, shift-left, SAST, SCA, SBOM
- **Related business domains:** Engineering

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
| Domain | Engineering |
| Audience | Humans, AI agents, RAG, enterprise search |
| Keywords | DevSecOps, shift-left, SAST, SCA, SBOM, supply chain, OPA |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`DevSecOps`, `shift-left`, `SAST`, `SCA`, `SBOM`, `supply chain`, `OPA`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
