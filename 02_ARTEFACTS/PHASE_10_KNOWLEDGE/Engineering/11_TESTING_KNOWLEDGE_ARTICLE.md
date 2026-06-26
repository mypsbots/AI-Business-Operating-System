---
id: KN-000018
title: Testing
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
  - testing
  - test pyramid
  - TDD
  - coverage
  - e2e
  - flaky tests
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - ISO 42001
---

# Testing

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000018  •  **Category:** Engineering

## Tags

`testing`, `test pyramid`, `TDD`, `coverage`, `e2e`, `flaky tests`

## Executive Summary

Testing builds confidence that software behaves correctly, using a balanced mix of automated and manual checks across the test pyramid.

## Purpose

To give people and AI agents a clear, reusable explanation of **Testing** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of testing as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- The test pyramid: unit, integration, e2e.
- TDD/BDD shape design and behaviour.
- Coverage and mutation testing measure adequacy.
- Flaky tests erode trust and must be fixed.
- Shift-left and continuous testing in CI.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding testing helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, testing is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Favour many fast unit tests.
- Gate merges on the suite.
- Eliminate flakiness.

## Anti-patterns

- UI-only testing.
- Ignoring flaky tests.
- No tests accompanying bug fixes.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real testing task and validate with the related checklist.

## FAQs

**Q: What is the test pyramid?**

A: A guideline to have many unit tests, fewer integration tests and few slow end-to-end tests.

**Q: What is TDD?**

A: Test-Driven Development — write a failing test first, then code to pass it.

## Decision Tree

- Is this about testing? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Learn unit testing and TDD.
- Add e2e tests for a critical flow.
- Measure and improve coverage.

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
- [DevSecOps](./09_DEVSECOPS_KNOWLEDGE_ARTICLE.md)
- [Observability](./10_OBSERVABILITY_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Engineering
- **Child topics:** see Related Knowledge below
- **Sibling topics:** Architecture, Frontend, Backend, API, Integration, Database
- **Dependencies / related technologies:** testing, test pyramid, TDD, coverage, e2e
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
| Keywords | testing, test pyramid, TDD, coverage, e2e, flaky tests |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`testing`, `test pyramid`, `TDD`, `coverage`, `e2e`, `flaky tests`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
