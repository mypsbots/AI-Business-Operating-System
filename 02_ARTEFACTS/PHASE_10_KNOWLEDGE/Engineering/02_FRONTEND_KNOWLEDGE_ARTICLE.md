---
id: KN-000009
title: Frontend
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
  - frontend
  - React
  - SSR
  - Core Web Vitals
  - accessibility
  - design system
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - WCAG 2.2 AA
---

# Frontend

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000009  •  **Category:** Engineering

## Tags

`frontend`, `React`, `SSR`, `Core Web Vitals`, `accessibility`, `design system`

## Executive Summary

Frontend engineering builds the user-facing layer — fast, accessible, responsive interfaces — typically with component-based frameworks.

## Purpose

To give people and AI agents a clear, reusable explanation of **Frontend** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of frontend as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Component architecture and state management.
- Rendering strategies: CSR, SSR, SSG, streaming.
- Core Web Vitals measure real user performance.
- Accessibility (WCAG) is a first-class requirement.
- Design systems ensure consistency.

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

Understanding frontend helps teams make better decisions, reduce risk and move faster. It connects directly to the related rules, checklists and playbooks below.

## Technical Context

In AIBOS, frontend is applied through the related standards and automated wherever possible, with AI agents operating under human oversight.

## Best Practices

- Meet Core Web Vitals and WCAG 2.2 AA.
- Use a design system and semantic HTML.
- Render on the server where it helps performance/SEO.

## Anti-patterns

- Shipping inaccessible custom widgets.
- Unbounded client bundles.
- Prop-drilling instead of proper state management.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Apply the best practices above to a real frontend task and validate with the related checklist.

## FAQs

**Q: CSR vs SSR?**

A: Client-side rendering builds UI in the browser; server-side rendering sends HTML from the server for faster first paint and SEO.

**Q: What are Core Web Vitals?**

A: Google's user-centric performance metrics: LCP, INP and CLS.

## Decision Tree

- Is this about frontend? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Learn a modern framework (React/Next.js).
- Study accessibility and Core Web Vitals.
- Build a component in a design system.

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
- [Backend](./03_BACKEND_KNOWLEDGE_ARTICLE.md)
- [API](./04_API_KNOWLEDGE_ARTICLE.md)
- [Integration](./05_INTEGRATION_KNOWLEDGE_ARTICLE.md)
- [Database](./06_DATABASE_KNOWLEDGE_ARTICLE.md)
- [Cloud](./07_CLOUD_KNOWLEDGE_ARTICLE.md)
- [DevOps](./08_DEVOPS_KNOWLEDGE_ARTICLE.md)
- [DevSecOps](./09_DEVSECOPS_KNOWLEDGE_ARTICLE.md)
- [Observability](./10_OBSERVABILITY_KNOWLEDGE_ARTICLE.md)
- [Testing](./11_TESTING_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Engineering
- **Child topics:** see Related Knowledge below
- **Sibling topics:** Architecture, Frontend, Backend, API, Integration, Database
- **Dependencies / related technologies:** frontend, React, SSR, Core Web Vitals, accessibility
- **Related business domains:** Engineering

## Department Ownership

Owned by the relevant department(s); see [Department Specifications](../../PHASE_04_DEPARTMENT_SPECIFICATIONS/README.md).

## Division Ownership

Governed by the relevant division; see [Division Specifications](../../PHASE_03_DIVISION_SPECIFICATIONS/README.md).

## External Standards

- WCAG 2.2 AA

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
| Keywords | frontend, React, SSR, Core Web Vitals, accessibility, design system |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`frontend`, `React`, `SSR`, `Core Web Vitals`, `accessibility`, `design system`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
