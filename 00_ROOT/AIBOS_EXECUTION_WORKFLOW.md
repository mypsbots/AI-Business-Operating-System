
# AIBOS_EXECUTION_WORKFLOW.md

# AIBOS Enterprise v2.0
## Enterprise Execution Workflow

Version: 2.0.0

---

# Purpose

This document defines the end-to-end execution workflow for creating,
reviewing, validating, publishing and maintaining every AIBOS artefact.

It is the operational playbook for humans and AI systems that generate
or manage AIBOS content.

---

# Scope

Applies to:

- Root standards
- Phase prompts
- Specifications
- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge
- SDKs
- AI Agents
- Marketplace Packages
- Reference Implementations

---

# Guiding Principles

- Standards before content
- Reuse before create
- Validate before publish
- Version every change
- Automate where practical
- Human approval for high-risk changes

---

# Context Loading Order

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
11. AIBOS_GENERATION_STANDARD.md
12. AIBOS_SECURITY_STANDARD.md
13. AIBOS_AI_BEHAVIOUR_STANDARD.md
14. AIBOS_ARCHITECTURE_PRINCIPLES.md
15. AIBOS_DESIGN_PRINCIPLES.md
16. AIBOS_REFERENCE_STANDARDS.md
17. Current Phase Prompt

---

# Execution Lifecycle

1. Load standards
2. Analyse requested phase
3. Resolve dependencies
4. Create execution plan
5. Generate one artefact at a time
6. Self-review
7. Validate
8. Cross-reference
9. Human review (if required)
10. Publish
11. Version
12. Archive superseded versions

---

# Phase Workflow

- Execute phases sequentially unless dependencies allow parallel work.
- Complete validation before starting dependent phases.
- Record assumptions and unresolved issues.

---

# Continuation Strategy

If generation reaches model limits:

- Stop at a completed heading.
- Record the last completed artefact.
- List remaining artefacts.
- Resume from the next unfinished section only.

---

# Repository Workflow

Draft → Review → Approved → Published → Maintained → Deprecated → Archived

---

# CI/CD Integration

Automate:

- Markdown linting
- Schema validation
- Metadata validation
- Link checking
- Security scanning
- Version checks
- Package publication

---

# Governance Gates

Required approvals may include:

- Technical Review
- Security Review
- Architecture Review
- Business Review
- Executive Approval (where applicable)

---

# Deliverables

Every execution should produce:

- Generated artefacts
- Validation report
- Change log
- Version updates
- Outstanding actions

---

# Success Criteria

Execution is complete when:

- All requested artefacts are generated.
- Validation passes.
- Cross-references are correct.
- Version history is updated.
- Required approvals are recorded.

---

# References

- AIBOS_ROOT_SPECIFICATION.md
- BUILD_AIBOS_MASTER_PROMPT_v2.md
- AIBOS_GENERATION_STANDARD.md
- AIBOS_VALIDATION_STANDARD.md
- AIBOS_QUALITY_STANDARD.md

---

# Version History

| Version | Summary |
|---------|---------|
| 2.0.0 | Initial enterprise execution workflow |
