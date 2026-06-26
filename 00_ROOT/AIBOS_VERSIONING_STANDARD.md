
# AIBOS_VERSIONING_STANDARD.md

# AIBOS Enterprise v2.0

## Enterprise Versioning Standard

Version: 2.0.0

---

# Purpose

This document defines the enterprise-wide versioning strategy for every artefact produced within AIBOS. It ensures predictable evolution, compatibility, traceability and governance across documentation, software, AI assets and automation.

---

# Scope

This standard applies to:

- Specifications
- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge Articles
- AI Agents
- Prompts
- SDKs
- CLI
- APIs
- MCP Servers
- Marketplace Packages
- Industry Blueprints
- Reference Implementations
- Infrastructure
- Automation Workflows

---

# Core Principles

- Use Semantic Versioning (MAJOR.MINOR.PATCH).
- Version every published artefact.
- Never modify a released version in place.
- Breaking changes require a MAJOR increment.
- New backwards-compatible functionality requires a MINOR increment.
- Fixes require a PATCH increment.

---

# Semantic Versioning

MAJOR.MINOR.PATCH

Examples:

- 1.0.0
- 2.1.0
- 2.1.4

---

# Release Channels

- Alpha
- Beta
- Release Candidate (RC)
- General Availability (GA)
- Long-Term Support (LTS)
- Deprecated
- End of Life (EOL)

Example:

2.0.0-beta.1
2.0.0-rc.2
2.0.0
2.0.0-lts

---

# Compatibility Rules

Every artefact must define:

- Compatible AIBOS version
- Minimum supported version
- Maximum tested version
- Breaking changes
- Migration guidance
- Dependencies

---

# Artefact Version Matrix

| Artefact | Version Required |
|----------|------------------|
| Specification | Yes |
| Skill | Yes |
| Rule | Yes |
| Checklist | Yes |
| Playbook | Yes |
| Template | Yes |
| Knowledge | Yes |
| AI Agent | Yes |
| Prompt | Yes |
| SDK | Yes |
| CLI | Yes |
| API | Yes |
| Marketplace Package | Yes |

---

# API Versioning

- Prefer URI or header versioning.
- Deprecate before removal.
- Publish migration guidance.

Examples:

/v1/agents
/v2/agents

---

# AI Asset Versioning

Every AI Agent, Prompt and MCP Server must include:

- Version
- Model compatibility
- Prompt compatibility
- Tool compatibility
- Memory schema version
- Evaluation version

---

# Documentation Versioning

Every document must contain:

- Document Version
- Last Updated
- Change Summary
- Review Date

---

# Deprecation Policy

Deprecation lifecycle:

1. Announce
2. Deprecate
3. Support Window
4. End of Life
5. Archive

---

# Change Log Requirements

Every release must record:

- Version
- Date
- Author
- Summary
- Breaking Changes
- Migration Steps

---

# Validation Rules

Verify:

- Semantic version format
- Dependency compatibility
- Cross-reference compatibility
- Release channel correctness
- Changelog completeness

---

# References

- AIBOS_ROOT_SPECIFICATION.md
- AIBOS_DOCUMENT_SCHEMA.md
- AIBOS_METADATA_STANDARD.md
- AIBOS_NAMING_STANDARD.md

---

# Version History

| Version | Summary |
|---------|---------|
| 2.0.0 | Initial enterprise versioning standard |
