
# AIBOS_METADATA_STANDARD.md

# AIBOS Enterprise v2.0
## Enterprise Metadata Standard

Version: 2.0.0

---

# Purpose

This document defines the canonical metadata model for every AIBOS artefact.
Metadata enables governance, traceability, search, automation, AI retrieval,
versioning and lifecycle management.

---

# Scope

Applies to all AIBOS artefacts including:

- Specifications
- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge
- SDKs
- CLI
- Marketplace Assets
- Industry Blueprints
- Reference Implementations

---

# Metadata Principles

Metadata MUST be:

- Complete
- Accurate
- Consistent
- Machine-readable
- Human-readable
- Versioned
- Searchable
- Governed

---

# Canonical Metadata Schema

```yaml
id: SPEC-000001
title: Example Title
document_type: Specification
category: Engineering
domain: AI Engineering
phase: Phase 05
owner: Platform Engineering
maintainer: Architecture Team
status: Draft
lifecycle: Active
priority: High
criticality: Business Critical
classification: Internal
version: 2.0.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
review_due: YYYY-MM-DD
authors: []
reviewers: []
approvers: []
tags: []
keywords: []
related_documents: []
related_skills: []
related_rules: []
related_checklists: []
related_playbooks: []
related_templates: []
related_knowledge: []
standards: []
dependencies: []
```

---

# Controlled Vocabularies

## Status
- Draft
- Review
- Approved
- Published
- Deprecated
- Archived

## Lifecycle
- Planned
- Active
- Maintenance
- Deprecated
- Retired

## Classification
- Public
- Internal
- Confidential
- Restricted

## Priority
- Low
- Medium
- High
- Critical

---

# Identifier Standards

Examples:

- SPEC-000001
- SKILL-000001
- RULE-000001
- CHECK-000001
- PLAY-000001
- TEMP-000001
- KNOW-000001
- AGENT-000001

Identifiers MUST be immutable.

---

# Tagging Rules

- Use lowercase.
- Use hyphens for multi-word tags.
- Prefer controlled vocabulary.
- Maximum 20 tags.

Example:

- ai
- rag
- prompt-engineering
- security

---

# Ownership

Every artefact MUST define:

- Business Owner
- Technical Owner
- Maintainer
- Review Frequency

---

# Versioning

Semantic Versioning:

MAJOR.MINOR.PATCH

Increment:
- MAJOR for breaking changes
- MINOR for enhancements
- PATCH for corrections

---

# AI Metadata

Include where applicable:

- Retrieval keywords
- Embedding keywords
- Chunk identifiers
- Parent document
- Child documents
- Related concepts

---

# Validation

Metadata must pass:

- Required field validation
- Enum validation
- ID uniqueness
- Date validation
- Version validation
- Cross-reference validation

---

# Inheritance

This standard is inherited by every AIBOS document alongside:

- AIBOS_ROOT_SPECIFICATION.md
- AIBOS_ENTERPRISE_GLOSSARY.md
- AIBOS_STYLE_GUIDE.md
- AIBOS_DOCUMENT_SCHEMA.md

---

# Version History

| Version | Summary |
|---------|---------|
| 2.0.0 | Initial enterprise metadata standard |
