---
id: KN-000027
title: Evaluation
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
  - evaluation
  - golden set
  - LLM-as-judge
  - faithfulness
  - regression
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - ISO 42001
  - NIST AI RMF
---

# Evaluation

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000027  •  **Category:** Artificial Intelligence

## Tags

`evaluation`, `golden set`, `LLM-as-judge`, `faithfulness`, `regression`

## Executive Summary

AI evaluation measures the quality, safety and cost of models and pipelines objectively so you can compare options and catch regressions.

## Purpose

To give people and AI agents a clear, reusable explanation of **Evaluation** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of evaluation as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Golden datasets and task-specific metrics.
- LLM-as-judge (used carefully) and human evaluation.
- RAG metrics: faithfulness, recall, precision.
- Safety metrics: jailbreak/unsafe-output rates.
- Continuous evaluation in CI.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding evaluation helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, evaluation is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Evaluate every model/prompt change.
- Include safety, not just accuracy.
- Automate evals and track regressions.

## Anti-patterns

- Shipping AI changes without evals.
- Accuracy-only evaluation.
- Over-trusting LLM-as-judge.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real evaluation task and validate with the related checklist.

## FAQs

**Q: What is LLM-as-judge?**

A: Using an LLM to score outputs against criteria — convenient but needing calibration against humans.

**Q: What is faithfulness?**

A: Whether a generated answer is grounded in the retrieved/source context.

## Decision Tree

- Is this about evaluation? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Build a golden eval set.
- Measure RAG and safety metrics.
- Wire evals into CI.

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
- [Vector Databases](./08_VECTOR_DATABASES_KNOWLEDGE_ARTICLE.md)
- [Guardrails](./10_GUARDRAILS_KNOWLEDGE_ARTICLE.md)
- [Responsible AI](./11_RESPONSIBLE_AI_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Artificial Intelligence
- **Child topics:** see Related Knowledge below
- **Sibling topics:** LLMs, Prompt Engineering, Agents, Agentic Workflows, RAG, MCP
- **Dependencies / related technologies:** evaluation, golden set, LLM-as-judge, faithfulness, regression
- **Related business domains:** Artificial Intelligence

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- ISO 42001
- NIST AI RMF

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
| Keywords | evaluation, golden set, LLM-as-judge, faithfulness, regression |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`evaluation`, `golden set`, `LLM-as-judge`, `faithfulness`, `regression`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
