---
id: KN-000024
title: MCP
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
  - MCP
  - tools
  - resources
  - least privilege
  - agents
  - protocol
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - OWASP LLM Top 10
---

# MCP

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000024  •  **Category:** Artificial Intelligence

## Tags

`MCP`, `tools`, `resources`, `least privilege`, `agents`, `protocol`

## Executive Summary

The Model Context Protocol is an open standard for connecting AI models to tools, resources and data in a consistent, secure way.

## Purpose

To give people and AI agents a clear, reusable explanation of **MCP** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of mcp as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Servers expose tools, resources and prompts.
- Clients (AI apps) consume them over a standard protocol.
- Explicit schemas and least-privilege permissions.
- Authentication, authorisation and audit.
- Human approval for high-risk tools.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding mcp helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, mcp is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Define explicit tool schemas and least privilege.
- Authenticate and audit every call.
- Gate risky actions behind human approval.

## Anti-patterns

- Over-broad tool permissions.
- Unauthenticated tools.
- No audit trail.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real mcp task and validate with the related checklist.

## FAQs

**Q: What problem does MCP solve?**

A: It standardises how agents access tools/data, replacing bespoke integrations with one protocol.

**Q: How is MCP secured?**

A: Through authentication, least-privilege scopes, auditing and human approval for risky actions.

## Decision Tree

- Is this about mcp? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Read the MCP spec.
- Build a simple MCP server.
- Add auth and least-privilege scopes.

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
- [Embeddings](./07_EMBEDDINGS_KNOWLEDGE_ARTICLE.md)
- [Vector Databases](./08_VECTOR_DATABASES_KNOWLEDGE_ARTICLE.md)
- [Evaluation](./09_EVALUATION_KNOWLEDGE_ARTICLE.md)
- [Guardrails](./10_GUARDRAILS_KNOWLEDGE_ARTICLE.md)
- [Responsible AI](./11_RESPONSIBLE_AI_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Artificial Intelligence
- **Child topics:** see Related Knowledge below
- **Sibling topics:** LLMs, Prompt Engineering, Agents, Agentic Workflows, RAG, MCP
- **Dependencies / related technologies:** MCP, tools, resources, least privilege, agents
- **Related business domains:** Artificial Intelligence

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
| Domain | Artificial Intelligence |
| Audience | Humans, AI agents, RAG, enterprise search |
| Keywords | MCP, tools, resources, least privilege, agents, protocol |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`MCP`, `tools`, `resources`, `least privilege`, `agents`, `protocol`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
