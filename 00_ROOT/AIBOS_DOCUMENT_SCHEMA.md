
# AIBOS_DOCUMENT_SCHEMA.md

# AIBOS Enterprise v2.0

## Canonical Document Schema Standard

Version: 2.0.0

---

# Purpose

This document defines the mandatory schema for every Markdown artefact generated within the AIBOS ecosystem.

It ensures every document is:

- Consistent
- Traceable
- AI-friendly
- Machine-readable
- Enterprise-ready
- Suitable for RAG and semantic search

---

# Scope

Applies to:

- Specifications
- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge
- Architecture
- Reference Implementations
- Industry Packs
- Accelerator Packs
- SDK Documents
- CLI Documents
- Marketplace Assets

---

# Mandatory YAML Front Matter

```yaml
id: DOC-000001
title: Example Document
document_type: Specification
category: Engineering
owner: Platform Engineering
status: Draft
version: 2.0.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
authors:
  - Name
reviewers:
  - Name
approvers:
  - Name
classification: Internal
tags:
  - ai
  - architecture
related_documents: []
related_skills: []
related_rules: []
related_checklists: []
related_playbooks: []
related_templates: []
related_knowledge: []
standards:
  - ISO 42001
  - ISO 27001
```

---

# Canonical Section Order

1. Executive Summary
2. Purpose
3. Scope
4. Audience
5. Background
6. Definitions
7. Main Content
8. Requirements
9. Examples
10. Risks
11. Dependencies
12. Related Artefacts
13. Validation Checklist
14. References
15. Version History

---

# Requirement Levels

Use RFC 2119 keywords only:

- MUST
- MUST NOT
- SHOULD
- SHOULD NOT
- MAY

---

# Metadata Standards

Every document must declare:

- Unique ID
- Version
- Status
- Owner
- Classification
- Tags
- Related artefacts
- Standards mapping

---

# Cross-Reference Model

Every document should reference:

- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge
- Industry Blueprints
- Accelerator Packs

Do not duplicate content already defined elsewhere.

---

# AI Optimisation

Optimise every document for:

- Semantic chunking
- RAG retrieval
- Embedding quality
- AI agent consumption
- Enterprise search

Recommended chunk size:

- 500–800 tokens
- Preserve section boundaries

---

# Validation Rules

Every document must pass:

- Schema validation
- Markdown validation
- Link validation
- Metadata validation
- Cross-reference validation
- Version validation
- Terminology validation

---

# Inheritance Rules

All documents inherit:

- AIBOS_ROOT_SPECIFICATION.md
- AIBOS_ENTERPRISE_GLOSSARY.md
- AIBOS_STYLE_GUIDE.md
- This schema

Phase-specific documents may extend but must not contradict these standards.

---

# Version History

| Version | Summary |
|---------|---------|
| 2.0.0 | Initial enterprise document schema |
