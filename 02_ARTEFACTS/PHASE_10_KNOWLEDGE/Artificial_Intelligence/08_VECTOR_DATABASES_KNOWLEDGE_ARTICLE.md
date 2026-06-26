---
id: KN-000026
title: Vector Databases
document_type: Knowledge Article
category: Artificial Intelligence
phase: Phase 10
owner: Chief Knowledge Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - vector database
  - ANN
  - HNSW
  - pgvector
  - Pinecone
  - hybrid search
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - ISO 42001
---

# Vector Databases

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000026  •  **Category:** Artificial Intelligence

## Tags

`vector database`, `ANN`, `HNSW`, `pgvector`, `Pinecone`, `hybrid search`

## Executive Summary

Vector databases store and index embeddings for fast similarity search at scale, powering RAG and semantic search.

## Purpose

To give people and AI agents a clear, reusable explanation of **Vector Databases** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of vector databases as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- ANN indexes (HNSW, IVF) trade accuracy for speed.
- Hybrid search combines vectors with keywords/filters.
- Metadata filtering narrows results.
- Scaling, sharding and freshness.
- Options: pgvector, Pinecone, Weaviate, Qdrant.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding vector databases helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, vector databases is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Use metadata filters with vector search.
- Tune the ANN index for recall vs latency.
- Keep embeddings and content in sync.

## Anti-patterns

- Treating it as a normal SQL store.
- Ignoring recall/latency tuning.
- Stale vectors after content changes.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real vector databases task and validate with the related checklist.

## FAQs

**Q: Do I need a dedicated vector DB?**

A: pgvector in Postgres is enough for many cases; dedicated stores help at large scale or with advanced features.

**Q: What is HNSW?**

A: A graph-based approximate-nearest-neighbour index offering fast, high-recall search.

## Decision Tree

- Is this about vector databases? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Learn ANN indexing.
- Use pgvector or Pinecone for a RAG store.
- Tune recall vs latency.

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

- [LLMs](./01_LLMS_KNOWLEDGE_ARTICLE.md)
- [Prompt Engineering](./02_PROMPT_ENGINEERING_KNOWLEDGE_ARTICLE.md)
- [Agents](./03_AGENTS_KNOWLEDGE_ARTICLE.md)
- [Agentic Workflows](./04_AGENTIC_WORKFLOWS_KNOWLEDGE_ARTICLE.md)
- [RAG](./05_RAG_KNOWLEDGE_ARTICLE.md)
- [MCP](./06_MCP_KNOWLEDGE_ARTICLE.md)
- [Embeddings](./07_EMBEDDINGS_KNOWLEDGE_ARTICLE.md)
- [Evaluation](./09_EVALUATION_KNOWLEDGE_ARTICLE.md)
- [Guardrails](./10_GUARDRAILS_KNOWLEDGE_ARTICLE.md)
- [Responsible AI](./11_RESPONSIBLE_AI_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Artificial Intelligence
- **Child topics:** see Related Knowledge below
- **Sibling topics:** LLMs, Prompt Engineering, Agents, Agentic Workflows, RAG, MCP
- **Dependencies / related technologies:** vector database, ANN, HNSW, pgvector, Pinecone
- **Related business domains:** Artificial Intelligence

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
| Domain | Artificial Intelligence |
| Audience | Humans, AI agents, RAG, enterprise search |
| Keywords | vector database, ANN, HNSW, pgvector, Pinecone, hybrid search |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`vector database`, `ANN`, `HNSW`, `pgvector`, `Pinecone`, `hybrid search`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
