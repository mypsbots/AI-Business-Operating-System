---
id: SDK-000002
title: Command Reference
document_type: Component
category: Core CLI
phase: Phase 16
owner: Chief Platform Engineer
status: Draft
lifecycle: Active
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - sdk-cli
related_documents:
  - AIBOS_ROOT_SPECIFICATION.md
standards:
  - ISO 42001
  - ISO 27001
  - NIST AI RMF
  - SOC 2
  - OWASP ASVS
  - OWASP LLM Top 10
  - WCAG 2.2 AA
---

# Command Reference

## Executive Summary

This document defines **Command Reference** within the AIBOS Enterprise v2.0 framework (Phase 16). It inherits every root standard and is designed to be enterprise-ready, machine-readable and AI-friendly.

## Purpose

To establish the authoritative, reusable definition of Command Reference so that human teams and AI agents operate consistently, safely and with measurable business value.

## Scope

Applies across the AIBOS enterprise and is inherited by all dependent artefacts. Concerns owned elsewhere are delegated to their owning documents to avoid duplication.

## Business Value

Reduced duplication, faster safe delivery, improved compliance posture and scalable AI augmentation.

## Developer Value

This section (Developer Value) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Functional Requirements

This section (Functional Requirements) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Non-functional Requirements

This section (Non-functional Requirements) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Public Interfaces

This section (Public Interfaces) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Commands/APIs

This section (Commands/APIs) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Configuration Model

This section (Configuration Model) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Authentication

This section (Authentication) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Authorisation

This section (Authorisation) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Extension Points

This section (Extension Points) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Plugin Architecture

This section (Plugin Architecture) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Versioning Strategy

This section (Versioning Strategy) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Backward Compatibility

This section (Backward Compatibility) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Error Handling

This section (Error Handling) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Observability

This section (Observability) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Security Controls

- Authentication and authorisation enforced.
- Encryption in transit and at rest.
- Audit logging and monitoring.

## Privacy Controls

- Data minimisation.
- Purpose limitation.
- Retention and secure deletion policies.

## Performance Targets

- Coverage and completeness of the artefact.
- Validation pass rate (target 95%+).
- Cycle time from draft to approval.
- Reuse rate across the enterprise.

## Testing Strategy

This section (Testing Strategy) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## CI/CD Integration

This section (CI/CD Integration) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Required Skills

- Inherits all root standards under `00_ROOT/`.
- Cross-references the relevant Phase artefacts under `02_ARTEFACTS/`.
- See `ROOT_INDEX.md` for the full catalogue.

## Required Rules

- Inherits all root standards under `00_ROOT/`.
- Cross-references the relevant Phase artefacts under `02_ARTEFACTS/`.
- See `ROOT_INDEX.md` for the full catalogue.

## Required Checklists

- Inherits all root standards under `00_ROOT/`.
- Cross-references the relevant Phase artefacts under `02_ARTEFACTS/`.
- See `ROOT_INDEX.md` for the full catalogue.

## Required Playbooks

- Inherits all root standards under `00_ROOT/`.
- Cross-references the relevant Phase artefacts under `02_ARTEFACTS/`.
- See `ROOT_INDEX.md` for the full catalogue.

## Required Templates

- Inherits all root standards under `00_ROOT/`.
- Cross-references the relevant Phase artefacts under `02_ARTEFACTS/`.
- See `ROOT_INDEX.md` for the full catalogue.

## Required Knowledge

- Inherits all root standards under `00_ROOT/`.
- Cross-references the relevant Phase artefacts under `02_ARTEFACTS/`.
- See `ROOT_INDEX.md` for the full catalogue.

## Sample Usage

```yaml
# Example for: Command Reference
name: example
version: 2.0.0
status: draft
```

## Mermaid Diagrams

```mermaid
flowchart TD
    A[Trigger] --> B[Process Inputs]
    B --> C{High-risk action?}
    C -->|Yes| D[Human Approval]
    C -->|No| E[AI Agent Executes]
    D --> E
    E --> F[Validate Output]
    F --> G[Record Audit Trail]
```

## Validation Checklist

- [ ] YAML front matter is present and valid.
- [ ] All mandatory sections are complete.
- [ ] Terminology matches the AIBOS Enterprise Glossary.
- [ ] Cross-references resolve to existing documents.
- [ ] RFC 2119 keywords are used correctly.
- [ ] Security and privacy considerations are addressed.
- [ ] Version history is updated.
- [ ] No secrets or sensitive data are exposed.

## References

This section (References) for **Command Reference** is defined in line with the AIBOS root standards and the governing Phase 16 master prompt. See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the inherited standards.

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 2.0.0 | 2026-06-26 | Initial generated artefact. |
