---
id: KN-000049
title: Healthcare
document_type: Knowledge Article
category: Industry Playbooks
phase: Phase 10
owner: Chief Knowledge Architect
status: Published
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - healthcare
  - HIPAA
  - clinical
  - EHR
  - triage
  - PHI
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md
standards:
  - ISO 42001
  - NIST AI RMF
---

# Healthcare

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Knowledge](../README.md) · [Phase 10 Prompt](../../../01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md)

**Knowledge ID:** KN-000049  •  **Category:** Industry Playbooks

## Tags

`healthcare`, `HIPAA`, `clinical`, `EHR`, `triage`, `PHI`

## Executive Summary

Healthcare delivers clinical and administrative services under strict safety and privacy regulation, where accuracy and trust are paramount.

## Purpose

To give people and AI agents a clear, reusable explanation of **Healthcare** that supports learning, retrieval (RAG) and decision support.

## Scope

Covers the core ideas, practices and pitfalls of healthcare as applied in AIBOS. Deep procedural detail lives in the related playbooks.

## Core Concepts

- Clinical documentation and ambient scribing.
- Patient triage and intake assistants.
- Administrative automation (coding, claims).
- Knowledge retrieval for clinicians (RAG over guidelines).
- Operational forecasting (capacity, no-shows).

## Definitions

See the [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md).

## Business Context

AI is reshaping the Healthcare sector. The highest-value, lowest-risk entry points are listed under Core Concepts; the business case rests on efficiency, experience and risk reduction.

## Technical Context

Typical solutions combine grounded RAG over approved sources, workflow automation and predictive models, with human oversight for regulated decisions.

## Best Practices

- Start with a high-value, low-risk use case and a clear metric.
- Ground AI in approved, current sources (RAG) and cite them.
- Keep a human in the loop for regulated or high-impact decisions.
- Map and meet the industry's compliance obligations early.

## Anti-patterns

- Deploying AI into regulated decisions without oversight.
- Ignoring sector-specific compliance.
- Boiling the ocean instead of proving one use case.

## Design Patterns

Apply the best practices above as repeatable patterns for this topic.

## Examples

- Ambient AI scribe drafting notes for clinician review.
- Patient-facing FAQ assistant grounded in approved content.
- Automating prior-authorisation paperwork.

## Compliance Considerations

- HIPAA / HITECH (US)
- GDPR for health data (EU)
- Medical device / clinical safety regulation
- EU AI Act (high-risk)

## Key Challenges

- Patient safety and liability
- Strict privacy of PHI
- Integration with legacy EHRs

## FAQs

**Q: Where should this industry start with AI?**

A: With a narrow, high-value use case (often document or service automation) that has measurable ROI and low regulatory risk.

**Q: What is the biggest risk?**

A: Compliance and trust — regulated decisions need human oversight, auditability and grounded, citable answers.

## Decision Tree

- Is this about healthcare? -> Use this article and its related rule.
- Is it high-risk or regulated? -> Keep a human in the loop and check compliance.
- Need to act? -> Follow the related playbook and validate with the checklist.
- Need to produce an artefact? -> Use the related template.

## Learning Path

- Map the industry value chain and pain points.
- Identify a high-ROI, low-risk AI use case.
- Design controls for the relevant regulations.

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

- [Retail](./01_RETAIL_KNOWLEDGE_ARTICLE.md)
- [Education](./03_EDUCATION_KNOWLEDGE_ARTICLE.md)
- [Real Estate](./04_REAL_ESTATE_KNOWLEDGE_ARTICLE.md)
- [Manufacturing](./05_MANUFACTURING_KNOWLEDGE_ARTICLE.md)
- [Finance](./06_FINANCE_KNOWLEDGE_ARTICLE.md)
- [Insurance](./07_INSURANCE_KNOWLEDGE_ARTICLE.md)
- [Government](./08_GOVERNMENT_KNOWLEDGE_ARTICLE.md)
- [Construction](./09_CONSTRUCTION_KNOWLEDGE_ARTICLE.md)
- [Hospitality](./10_HOSPITALITY_KNOWLEDGE_ARTICLE.md)
- [Logistics](./11_LOGISTICS_KNOWLEDGE_ARTICLE.md)
- [Legal](./12_LEGAL_KNOWLEDGE_ARTICLE.md)

## Knowledge Graph

- **Parent topic:** Industry Playbooks
- **Child topics:** see Related Knowledge below
- **Sibling topics:** Retail, Healthcare, Education, Real Estate, Manufacturing, Finance
- **Dependencies / related technologies:** healthcare, HIPAA, clinical, EHR, triage
- **Related business domains:** Industry Playbooks

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
| Domain | Industry Playbooks |
| Audience | Humans, AI agents, RAG, enterprise search |
| Keywords | healthcare, HIPAA, clinical, EHR, triage, PHI |

## Suggested Chunk Boundaries

- Executive Summary (overview chunk).
- Core Concepts (concept chunk).
- Best Practices + Anti-patterns (guidance chunk).
- FAQs (Q&A chunks, one per question).

## Suggested Embedding Keywords

`healthcare`, `HIPAA`, `clinical`, `EHR`, `triage`, `PHI`

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Complete, ready-to-use knowledge article. |
