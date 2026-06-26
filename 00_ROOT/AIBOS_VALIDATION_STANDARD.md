
# AIBOS_VALIDATION_STANDARD.md

# AIBOS Enterprise v2.0
## Enterprise Validation Standard

Version: 2.0.0

---

# Purpose

This standard defines the enterprise validation framework for every AIBOS artefact.
It specifies how quality, consistency, security, governance and AI-readiness are
verified before publication and throughout the artefact lifecycle.

---

# Objectives

- Establish repeatable validation processes
- Support automated and manual validation
- Prevent inconsistent or invalid artefacts
- Improve trust in AI-generated content
- Enable CI/CD quality gates

---

# Scope

Applies to all AIBOS artefacts:

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
- APIs
- Marketplace Packages
- Industry Blueprints
- Reference Implementations

---

# Validation Principles

Validation MUST be:

- Objective
- Repeatable
- Traceable
- Automated where practical
- Risk-based
- Evidence-driven
- Independent where appropriate

---

# Validation Lifecycle

1. Author Self-Validation
2. Automated Validation
3. Peer Validation
4. Technical Validation
5. Security Validation
6. Governance Validation
7. Final Approval
8. Continuous Validation

---

# Validation Types

## Structural
- Markdown syntax
- YAML schema
- Heading hierarchy
- Required sections

## Metadata
- Required fields
- ID uniqueness
- Version format
- Owner and classification

## Content
- Terminology consistency
- Grammar and spelling
- Duplicate detection
- Broken references

## AI
- Hallucination detection
- Unsupported claims
- Prompt leakage
- Sensitive information exposure
- RAG optimisation
- Embedding quality

## Technical
- Code syntax
- API examples
- Mermaid diagrams
- Configuration samples

## Security
- Secret detection
- Security guidance
- Compliance mapping
- OWASP alignment

## Governance
- Required approvals
- Ownership
- Lifecycle status
- Review schedule

---

# Severity Levels

| Level | Description | Action |
|-------|-------------|--------|
| Info | Improvement suggestion | Optional |
| Warning | Minor issue | Should fix |
| Error | Validation failure | Must fix |
| Critical | High-risk issue | Publication blocked |

---

# Acceptance Criteria

Publication requires:

- No Critical issues
- No Errors
- Required approvals recorded
- Metadata complete
- Cross-references valid
- Version updated

---

# Validation Scorecard

Recommended weighting:

| Area | Weight |
|------|-------:|
| Structure | 10% |
| Metadata | 15% |
| Content | 20% |
| Technical | 20% |
| Security | 15% |
| Governance | 10% |
| AI Optimisation | 10% |

Target overall score: **95%+**

---

# CI/CD Integration

Validation should execute automatically on:

- Pull Requests
- Merge Requests
- Main branch merges
- Release creation
- Marketplace publication

---

# Validation Report

Every validation should produce:

- Artefact ID
- Validation timestamp
- Validator
- Rules executed
- Passed checks
- Failed checks
- Severity summary
- Overall score
- Approval decision

---

# Exception Handling

Exceptions require:

- Business justification
- Risk assessment
- Named approver
- Expiry date
- Review schedule

---

# Continuous Validation

Continuously monitor:

- Link integrity
- Dependency changes
- Standard revisions
- Security advisories
- Deprecated references

---

# References

- AIBOS_ROOT_SPECIFICATION.md
- AIBOS_DOCUMENT_SCHEMA.md
- AIBOS_METADATA_STANDARD.md
- AIBOS_QUALITY_STANDARD.md
- AIBOS_VERSIONING_STANDARD.md

---

# Version History

| Version | Summary |
|---------|---------|
| 2.0.0 | Initial enterprise validation standard |
