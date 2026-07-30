---
id: BIZDOC-010
title: Service Level Agreement — Generation Skill
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
  - service-level-agreement
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md
  - 02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/00_UK_CONTRACTING_FRAMEWORK.md
standards:
  - UK GDPR
  - Data Protection Act 2018
  - ISO 27001
  - ISO 42001
  - SOC 2
---

# Service Level Agreement — Generation Skill

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Business Docs](README.md) · [UK Framework](00_UK_CONTRACTING_FRAMEWORK.md) · [Source Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)

## At a Glance

Defines service levels, response/resolution targets and remedies for ongoing managed services, hosting or support.

| Field | Detail |
| --- | --- |
| Document | Service Level Agreement |
| Category | Business Documentation |
| Jurisdiction | England and Wales (UK) |
| Pack | Extended |
| Binding status | Binding schedule; takes precedence on service-level matters. |
| Typical signatories | Authorised signatory of the Supplier and of the Customer. |
| AI automation | AI-draftable from a service catalogue; human review of targets and service credits. |

## Legal Notice

> **Legal notice.** This skill produces a **draft** business document to speed up preparation. It is **not legal advice** and is **not a substitute for review by a UK-qualified solicitor**. For high-value, regulated, international, security-sensitive or complex engagements, obtain solicitor sign-off before signing. Unless otherwise agreed, the governing law is **England and Wales**. Do not store passwords, API keys or production credentials in generated documents.

## Purpose

A Service Level Agreement (SLA) sets measurable commitments for an ongoing service — support, hosting, maintenance or availability — and the consequences (e.g. service credits) if targets are missed.

It protects the Supplier by defining exclusions and realistic targets, and protects the customer with clear, measurable service levels.

## When to Use

- Ongoing managed service, hosting or maintenance.
- Availability or support-response commitments.
- Any recurring service with performance obligations.

## Document Blueprint (Generation Template)

When this skill is invoked, generate the document by expanding each blueprint section below into clear, formal UK business English, filling every placeholder from the *Inputs Required*, resolving or flagging any missing input, marking the output as a draft, and appending a dated signature block for the authorised signatories. Keep numbering and the order of precedence consistent with the [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md).

1. **Service description and hours** — Services covered and service hours.
2. **Support channels** — How the customer raises issues.
3. **Priority definitions** — Severity levels (P1–P4) with examples.
4. **Response times** — Time to first response per priority.
5. **Resolution / workaround targets** — Target resolution or workaround per priority.
6. **Uptime target** — Availability % and how measured.
7. **Maintenance windows** — Planned maintenance timing and notice.
8. **Exclusions** — Planned maintenance, customer systems, internet failures, third-party cloud/AI outages, force majeure, customer misuse.
9. **Customer responsibilities** — What the customer must do for SLAs to apply.
10. **Monitoring method** — How performance is measured.
11. **Service credits** — Remedy for missed targets and how claimed.
12. **Reporting** — Cadence and content of service reports.
13. **Escalation path** — Who to escalate to and when.
14. **Security incident contact** — Contact and process for security incidents.
15. **Disaster recovery and business continuity** — RTO/RPO and continuity commitments.

## Inputs Required to Generate

- Service scope and hours; support channels.
- Priority definitions, response/resolution targets, uptime target.
- Exclusions, service credits, reporting and escalation.
- DR/BC commitments (RTO/RPO).

## UK Legal and Compliance Notes

- Do not promise 100% uptime; define exclusions explicitly.
- Service credits are usually the sole financial remedy for SLA breaches — state this clearly.

## Best Practices and Pitfalls

- Set realistic, measurable targets you can evidence.
- Exclude third-party cloud/AI provider failures outside your control.

## Related Documents

- [Master Services Agreement](04_MASTER_SERVICES_AGREEMENT_SKILL.md)
- [Security Schedule](11_SECURITY_SCHEDULE_SKILL.md)
- [Support and Maintenance Agreement](20_SUPPORT_AND_MAINTENANCE_AGREEMENT_SKILL.md)
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
