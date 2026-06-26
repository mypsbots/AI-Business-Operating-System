
# AIBOS_STYLE_GUIDE.md

# AIBOS Enterprise v2.0

## Enterprise Documentation Style Guide

Version: 2.0

---

# Purpose

This document defines the mandatory writing, formatting and presentation standards for every artefact generated within AIBOS Enterprise.

All Markdown documents MUST comply with this guide.

---

# Objectives

- Ensure consistency across all documentation.
- Optimise content for humans and AI.
- Improve readability and maintainability.
- Reduce ambiguity.
- Support RAG, semantic search and AI agents.

---

# Language Standards

- Use British English.
- Use clear, professional language.
- Prefer active voice.
- Define specialised terms using the AIBOS Enterprise Glossary.
- Avoid unnecessary jargon.
- Avoid marketing language in technical documents.
- Use RFC 2119 terminology:
  - MUST
  - MUST NOT
  - SHOULD
  - SHOULD NOT
  - MAY

---

# Document Structure

Every document should follow this order:

1. YAML Front Matter
2. Title
3. Executive Summary
4. Purpose
5. Scope
6. Background
7. Main Content
8. Examples
9. Risks
10. Validation Checklist
11. References
12. Version History

---

# Markdown Standards

- Use ATX headings (#, ##, ###).
- Leave one blank line between sections.
- Prefer tables for comparisons.
- Prefer bullet lists for collections.
- Use fenced code blocks with language identifiers.
- Use Mermaid diagrams for workflows and architecture.
- Avoid HTML unless essential.

---

# Naming Conventions

- Filenames: UPPER_SNAKE_CASE.md
- Headings: Title Case
- IDs: PREFIX-000001 format
- Versions: Semantic Versioning (MAJOR.MINOR.PATCH)

---

# Writing Principles

- One concept per section.
- One responsibility per document.
- Reuse instead of duplicate.
- Cross-reference related artefacts.
- Keep examples realistic.
- Clearly distinguish normative requirements from guidance.

---

# Diagram Standards

Use Mermaid for:

- Flowcharts
- Sequence diagrams
- Architecture diagrams
- State diagrams
- Entity relationships

Every diagram should include a short explanation.

---

# Code Standards

Examples must:

- Compile or be syntactically correct.
- Be minimal but complete.
- Include comments where helpful.
- Avoid secrets or credentials.

---

# Accessibility

- Use descriptive headings.
- Avoid colour-only meaning.
- Write meaningful link text.
- Keep tables simple.
- Use inclusive language.

---

# AI Optimisation

Documents should:

- Use consistent terminology.
- Be chunk-friendly for RAG.
- Avoid duplicated definitions.
- Include metadata where appropriate.
- Be easy to parse programmatically.

---

# Review Checklist

Before publishing verify:

- Grammar and spelling
- British English
- Heading hierarchy
- Consistent terminology
- Correct cross-references
- Working examples
- Version updated
- Validation checklist included

---

# References

- AIBOS_ROOT_SPECIFICATION.md
- AIBOS_ENTERPRISE_GLOSSARY.md
- BUILD_AIBOS_MASTER_PROMPT_v2.md

---

# Version History

| Version | Date | Summary |
|---------|------|---------|
| 2.0.0 | Initial | Enterprise style guide established |
