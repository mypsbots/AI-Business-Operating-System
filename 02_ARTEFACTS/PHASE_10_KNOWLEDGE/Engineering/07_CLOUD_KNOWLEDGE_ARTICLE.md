---
id: KN-000014
title: Cloud
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
  - cloud
  - serverless
  - IaaS
  - PaaS
  - regions
  - FinOps
  - well-architected
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - ISO 42001
---

# Cloud

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000014  •  **Category:** Engineering

## Tags

`cloud`, `serverless`, `IaaS`, `PaaS`, `regions`, `FinOps`, `well-architected`

## Executive Summary

Cloud computing provides on-demand, elastic infrastructure and managed services, shifting capital cost to usage-based operating cost.

## Purpose

To give people and AI agents a clear, reusable explanation of **Cloud** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of cloud as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Service models: IaaS, PaaS, SaaS, serverless.
- Elasticity, regions and availability zones.
- The shared responsibility model for security.
- Well-Architected pillars guide good design.
- Cost management (FinOps).

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding cloud helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, cloud is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Design for failure across AZs/regions.
- Use managed services to reduce toil.
- Track and optimise cost continuously.

## Anti-patterns

- Lift-and-shift without re-architecting.
- Ignoring the shared responsibility model.
- Uncontrolled spend.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real cloud task and validate with the related checklist.

## FAQs

**Q: What is serverless?**

A: Running code without managing servers, scaling automatically and billing per use (e.g. functions).

**Q: What is the shared responsibility model?**

A: The cloud secures the infrastructure; you secure your data, config and access.

## Decision Tree

- Is this about cloud? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Learn one cloud's core services.
- Study the Well-Architected Framework.
- Deploy a serverless function.

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
- [DevOps](./08_DEVOPS_KNOWLEDGE_ARTICLE.md)
- [DevSecOps](./09_DEVSECOPS_KNOWLEDGE_ARTICLE.md)
- [Observability](./10_OBSERVABILITY_KNOWLEDGE_ARTICLE.md)
- [Testing](./11_TESTING_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Engineering
- **Child topics:** see Related Knowledge below
- **Sibling topics:** Architecture, Frontend, Backend, API, Integration, Database
- **Dependencies / related technologies:** cloud, serverless, IaaS, PaaS, regions
- **Related business domains:** Engineering

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- Not applicable.

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
| Keywords | cloud, serverless, IaaS, PaaS, regions, FinOps, well-architected |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`cloud`, `serverless`, `IaaS`, `PaaS`, `regions`, `FinOps`, `well-architected`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
