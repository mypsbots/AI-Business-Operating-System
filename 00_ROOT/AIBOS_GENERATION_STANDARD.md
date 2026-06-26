
# AIBOS_GENERATION_STANDARD.md

# AIBOS Enterprise v2.0
## Enterprise Generation Standard

Version: 2.0.0

---

# Purpose

This standard defines the canonical generation process for every artefact produced by Large Language Models (LLMs) within the AIBOS ecosystem.

It ensures deterministic, repeatable, high-quality and enterprise-ready outputs regardless of the underlying AI model.

---

# Scope

Applies to generation of:

- Specifications
- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge Articles
- AI Agents
- Prompts
- SDK Documentation
- APIs
- Marketplace Packages
- Industry Blueprints
- Reference Implementations

Supported models include GPT, Claude, Gemini, Grok and compatible open-source LLMs.

---

# Generation Principles

Every generation process MUST be:

- Deterministic where possible
- Traceable
- Modular
- Reusable
- AI-friendly
- Human-readable
- Consistent with AIBOS standards
- Secure by default

---

# Context Loading Order

Always load context in this order:

1. AIBOS_ROOT_SPECIFICATION.md
2. BUILD_AIBOS_MASTER_PROMPT_v2.md
3. AIBOS_ENTERPRISE_GLOSSARY.md
4. AIBOS_STYLE_GUIDE.md
5. AIBOS_DOCUMENT_SCHEMA.md
6. AIBOS_METADATA_STANDARD.md
7. AIBOS_NAMING_STANDARD.md
8. AIBOS_VERSIONING_STANDARD.md
9. AIBOS_QUALITY_STANDARD.md
10. AIBOS_VALIDATION_STANDARD.md
11. Current Phase Prompt

---

# Generation Workflow

1. Load standards
2. Load phase prompt
3. Identify dependencies
4. Produce generation plan
5. Generate artefact
6. Self-review
7. Validate against standards
8. Cross-reference related artefacts
9. Produce final output

---

# Prompt Engineering Standards

Prompts should:

- Assign an explicit role
- State the objective
- Define inputs
- Specify outputs
- Define constraints
- Reference inherited standards
- Require validation
- Require version history

---

# Token Management

- Keep logical sections intact.
- Prefer one document per generation.
- Stop gracefully before context exhaustion.
- Record continuation points.
- Resume without regenerating completed content.

---

# Output Requirements

Every generated artefact should include:

- YAML front matter
- Executive Summary
- Purpose
- Scope
- Main content
- Validation checklist
- References
- Version history

---

# Cross-Reference Rules

Reference existing artefacts rather than duplicating content.

Link to:

- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge
- Industry Blueprints
- Accelerator Packs

---

# Multi-Model Compatibility

Generation should remain compatible with:

- GPT family
- Claude family
- Gemini family
- Grok family
- Local LLMs

Avoid model-specific assumptions unless explicitly required.

---

# Failure Recovery

If generation stops:

- Preserve completed sections
- Report stopping point
- Record remaining work
- Continue from the last completed heading

---

# Generation Quality Gates

Before completion verify:

- Schema compliance
- Metadata completeness
- Terminology consistency
- Style guide compliance
- Naming compliance
- Version compliance
- Validation readiness

---

# References

- AIBOS_ROOT_SPECIFICATION.md
- BUILD_AIBOS_MASTER_PROMPT_v2.md
- AIBOS_STYLE_GUIDE.md
- AIBOS_DOCUMENT_SCHEMA.md
- AIBOS_QUALITY_STANDARD.md
- AIBOS_VALIDATION_STANDARD.md

---

# Version History

| Version | Summary |
|---------|---------|
| 2.0.0 | Initial enterprise generation standard |
