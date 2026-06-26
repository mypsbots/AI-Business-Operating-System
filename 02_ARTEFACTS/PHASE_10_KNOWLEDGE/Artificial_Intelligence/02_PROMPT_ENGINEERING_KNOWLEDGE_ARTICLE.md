---
id: KN-000020
title: Prompt Engineering
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
  - prompt engineering
  - few-shot
  - chain-of-thought
  - structured output
  - prompt injection
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - OWASP LLM Top 10
  - ISO 42001
---

# Prompt Engineering

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000020  •  **Category:** Artificial Intelligence

## Tags

`prompt engineering`, `few-shot`, `chain-of-thought`, `structured output`, `prompt injection`

## Executive Summary

Prompt engineering is the craft of designing inputs and instructions that reliably steer an LLM to produce useful, safe, well-structured output.

## Purpose

To give people and AI agents a clear, reusable explanation of **Prompt Engineering** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of prompt engineering as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Clear instructions, roles and constraints.
- Few-shot examples and chain-of-thought.
- Structured output (JSON) for downstream parsing.
- Prompt-injection defence.
- Versioning and evaluation of prompts.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding prompt engineering helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, prompt engineering is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Be explicit; show examples.
- Request structured output where parsed.
- Version and evaluate prompts; defend against injection.

## Anti-patterns

- Vague prompts.
- Unversioned prompts edited in prod.
- Trusting instructions embedded in user data.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real prompt engineering task and validate with the related checklist.

## FAQs

**Q: What is few-shot prompting?**

A: Including a few examples in the prompt to demonstrate the desired output.

**Q: What is prompt injection?**

A: Malicious input that tries to override the system's instructions.

## Decision Tree

- Is this about prompt engineering? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Practise instruction and few-shot prompting.
- Enforce JSON output.
- Set up prompt evaluation (promptfoo).

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
- [Agents](./03_AGENTS_KNOWLEDGE_ARTICLE.md)
- [Agentic Workflows](./04_AGENTIC_WORKFLOWS_KNOWLEDGE_ARTICLE.md)
- [RAG](./05_RAG_KNOWLEDGE_ARTICLE.md)
- [MCP](./06_MCP_KNOWLEDGE_ARTICLE.md)
- [Embeddings](./07_EMBEDDINGS_KNOWLEDGE_ARTICLE.md)
- [Vector Databases](./08_VECTOR_DATABASES_KNOWLEDGE_ARTICLE.md)
- [Evaluation](./09_EVALUATION_KNOWLEDGE_ARTICLE.md)
- [Guardrails](./10_GUARDRAILS_KNOWLEDGE_ARTICLE.md)
- [Responsible AI](./11_RESPONSIBLE_AI_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Artificial Intelligence
- **Child topics:** see Related Knowledge below
- **Sibling topics:** LLMs, Prompt Engineering, Agents, Agentic Workflows, RAG, MCP
- **Dependencies / related technologies:** prompt engineering, few-shot, chain-of-thought, structured output, prompt injection
- **Related business domains:** Artificial Intelligence

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- OWASP LLM Top 10
- ISO 42001

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
| Keywords | prompt engineering, few-shot, chain-of-thought, structured output, prompt injection |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`prompt engineering`, `few-shot`, `chain-of-thought`, `structured output`, `prompt injection`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
