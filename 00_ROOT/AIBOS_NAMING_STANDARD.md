
# AIBOS_NAMING_STANDARD.md

# AIBOS Enterprise v2.0
## Enterprise Naming Standard

Version: 2.0.0

---

# Purpose

This document defines the mandatory naming conventions for every artefact within the AIBOS ecosystem. Consistent naming improves discoverability, automation, governance, traceability and AI-assisted retrieval.

---

# Scope

Applies to:

- Repositories
- Directories
- Markdown documents
- AI Agents
- Skills
- Rules
- Checklists
- Playbooks
- Templates
- Knowledge articles
- APIs
- Services
- Databases
- Tables
- Environment variables
- Configuration files
- Docker images
- Kubernetes resources
- Git branches
- Releases
- Marketplace packages

---

# General Principles

- Names MUST be descriptive.
- Avoid abbreviations unless industry standard.
- Use consistent casing.
- Avoid spaces.
- Avoid special characters unless required.
- Names MUST remain stable after publication.

---

# File Naming

Markdown:

UPPER_SNAKE_CASE.md

Examples:

AIBOS_STYLE_GUIDE.md
RULE_API_SECURITY.md
SKILL_PROMPT_ENGINEERING.md

---

# Directory Naming

Use lowercase kebab-case.

Examples:

platform-engineering/
knowledge-base/
industry-blueprints/

---

# Repository Naming

Use lowercase kebab-case.

Pattern:

organisation-project-purpose

Examples:

aibos-enterprise
faqai-platform
ai-agent-framework

---

# Branch Naming

feature/<name>
bugfix/<name>
hotfix/<name>
release/<version>
docs/<topic>

Example:

feature/agent-memory
release/v2.1.0

---

# Document IDs

Examples:

SPEC-000001
RULE-000001
CHECK-000001
PLAY-000001
TEMP-000001
KNOW-000001
AGENT-000001

IDs MUST be immutable.

---

# API Naming

REST resources:

/agents
/playbooks
/templates

Use nouns.
Use plural resources.

---

# Environment Variables

Use UPPER_SNAKE_CASE.

Examples:

OPENAI_API_KEY
DATABASE_URL
AIBOS_ENVIRONMENT

---

# Database Naming

Tables:

snake_case

Columns:

snake_case

Primary Keys:

id

Foreign Keys:

<entity>_id

---

# Docker

Images:

organisation/project

Tags:

semantic versioning

Example:

aibos/platform:2.0.0

---

# Kubernetes

Namespaces:

lowercase-kebab-case

Resources:

lowercase-kebab-case

---

# AI Agent Naming

Pattern:

<Role> Agent

Examples:

Platform Engineer Agent
Architecture Reviewer Agent
Security Auditor Agent

Internal IDs:

AGENT-000001

---

# Prompt Naming

PROMPT_<DOMAIN>_<PURPOSE>.md

Example:

PROMPT_RAG_EVALUATION.md

---

# Marketplace Package Naming

package-name

Semantic version required.

Example:

enterprise-rag-pack

---

# Validation Rules

Names must satisfy:

- Unique where required
- Stable
- Readable
- Searchable
- Automation-friendly
- Machine-readable

---

# References

- AIBOS_ROOT_SPECIFICATION.md
- AIBOS_DOCUMENT_SCHEMA.md
- AIBOS_METADATA_STANDARD.md
- AIBOS_STYLE_GUIDE.md

---

# Version History

| Version | Summary |
|---------|---------|
| 2.0.0 | Initial enterprise naming standard |
