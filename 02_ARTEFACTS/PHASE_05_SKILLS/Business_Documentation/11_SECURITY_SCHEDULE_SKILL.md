---
id: BIZDOC-011
title: Security Schedule — Generation Skill
document_type: Skill
category: Business Documentation
phase: Phase 05
owner: Commercial and Contracts Lead
status: Published
lifecycle: Active
classification: Internal
version: 1.0.0
created: 2026-07-30
updated: 2026-07-30
jurisdiction: England and Wales
tags:
  - skill
  - business-documentation
  - security-schedule
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md
  - 02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/00_UK_CONTRACTING_FRAMEWORK.md
standards:
  - ISO 27001
  - NCSC Cyber Essentials
  - UK GDPR
  - SOC 2
---

# Security Schedule — Generation Skill

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Business Docs](README.md) · [UK Framework](00_UK_CONTRACTING_FRAMEWORK.md) · [Source Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)

## At a Glance

Sets the information-security controls the Supplier applies when handling sensitive data or privileged system access.

| Field | Detail |
| --- | --- |
| Document | Security Schedule |
| Category | Business Documentation |
| Jurisdiction | England and Wales (UK) |
| Pack | Extended |
| Binding status | Binding schedule to the MSA/SOW where incorporated. |
| Typical signatories | Authorised signatory of the Supplier and of the Customer. |
| AI automation | AI-draftable from the firm's security baseline; security lead review required. |

## Legal Notice

> **Legal notice.** This skill produces a **draft** business document to speed up preparation. It is **not legal advice** and is **not a substitute for review by a UK-qualified solicitor**. For high-value, regulated, international, security-sensitive or complex engagements, obtain solicitor sign-off before signing. Unless otherwise agreed, the governing law is **England and Wales**. Do not store passwords, API keys or production credentials in generated documents.

## Purpose

A Security Schedule documents the technical and organisational controls the Supplier maintains when handling sensitive information, privileged access or enterprise systems, giving the customer assurance and a basis for audit.

It complements the DPA's Article 32 measures with concrete controls.

## When to Use

- Handling sensitive information or special-category data.
- Privileged access to customer production systems.
- Enterprise or regulated environments.

## Document Blueprint (Generation Template)

When this skill is invoked, generate the document by expanding each blueprint section below into clear, formal UK business English, filling every placeholder from the *Inputs Required*, resolving or flagging any missing input, marking the output as a draft, and appending a dated signature block for the authorised signatories. Keep numbering and the order of precedence consistent with the [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md).

1. **Access control** — Least-privilege, role-based access, joiner/mover/leaver.
2. **Multi-factor authentication** — MFA for privileged and remote access.
3. **Encryption** — In transit and at rest.
4. **Vulnerability management** — Scanning, patching cadence.
5. **Logging and monitoring** — Audit logs and retention.
6. **Backups** — Backup frequency, testing, retention.
7. **Incident handling** — Detection, response, notification timelines.
8. **Personnel security** — Vetting, training, confidentiality.
9. **Secure development** — Secure SDLC, code review, dependency management.
10. **Segregation of customer environments** — Isolation between customers.
11. **Data deletion** — Secure deletion on exit/request.
12. **Business continuity** — Continuity and recovery commitments.
13. **Penetration testing** — Frequency and remediation.
14. **Customer audit rights** — Scope and frequency of audits/evidence.

## Inputs Required to Generate

- The firm's security baseline and certifications (e.g. ISO 27001, Cyber Essentials).
- Project-specific controls, environments and audit rights.

## UK Legal and Compliance Notes

- Align controls with ISO 27001 / NCSC guidance and the DPA's security obligations.
- Only commit to controls you actually operate and can evidence.

## Best Practices and Pitfalls

- Reference certifications you hold; do not overstate.
- Keep the schedule consistent with the DPA measures.

## Related Documents

- [Data Processing Agreement](06_DATA_PROCESSING_AGREEMENT_SKILL.md)
- [Data Mapping Questionnaire](16_DATA_MAPPING_QUESTIONNAIRE_SKILL.md)
- [Service Level Agreement](10_SERVICE_LEVEL_AGREEMENT_SKILL.md)
- [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md)
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)
- [Business Documentation Index](README.md)
- [All Phase 05 Skills](../README.md)
- [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md)
- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Complete, generate-ready UK business-document skill. |
