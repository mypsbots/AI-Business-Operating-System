---
id: BIZDOC-006
title: Data Processing Agreement — Generation Skill
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
  - data-processing-agreement
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

# Data Processing Agreement — Generation Skill

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Business Docs](README.md) · [UK Framework](00_UK_CONTRACTING_FRAMEWORK.md) · [Source Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)

## At a Glance

The UK GDPR-mandated controller–processor contract used where the Supplier processes personal data on the customer's behalf.

| Field | Detail |
| --- | --- |
| Document | Data Processing Agreement |
| Category | Business Documentation |
| Jurisdiction | England and Wales (UK) |
| Pack | Essential |
| Binding status | Binding; legally required where the Supplier acts as processor. Takes precedence on data-protection matters. |
| Typical signatories | Authorised signatory of the Supplier (processor) and Customer (controller). |
| AI automation | AI-draftable from a compliant base + Inputs; DPO/solicitor review for special-category data or international transfers. |

## Legal Notice

> **Legal notice.** This skill produces a **draft** business document to speed up preparation. It is **not legal advice** and is **not a substitute for review by a UK-qualified solicitor**. For high-value, regulated, international, security-sensitive or complex engagements, obtain solicitor sign-off before signing. Unless otherwise agreed, the governing law is **England and Wales**. Do not store passwords, API keys or production credentials in generated documents.

## Purpose

A Data Processing Agreement (DPA) is required by UK GDPR Article 28 wherever the Supplier processes personal data on behalf of the customer as a processor. It sets the mandatory controller–processor terms and records the processing details.

Where both parties independently decide why and how personal data is used, a processor DPA is the wrong instrument and a Data Sharing Agreement should be used instead.

## When to Use

- The customer shares employee or customer records for the Supplier to process.
- The Supplier builds/operates an AI system using personal data, or hosts customer data.
- The Supplier accesses a CRM, email, help desk, HR or analytics system containing personal data.
- Support work provides access to identifiable user information.

## Document Blueprint (Generation Template)

When this skill is invoked, generate the document by expanding each blueprint section below into clear, formal UK business English, filling every placeholder from the *Inputs Required*, resolving or flagging any missing input, marking the output as a draft, and appending a dated signature block for the authorised signatories. Keep numbering and the order of precedence consistent with the [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md).

1. **Parties and roles** — Identify controller and processor and the governing agreement.
2. **Processing only on documented instructions** — Processor acts only on the controller's documented instructions.
3. **Confidentiality of personnel** — Persons authorised to process are bound by confidentiality.
4. **Security measures (Art. 32)** — Appropriate technical and organisational measures.
5. **Sub-processors** — Prior authorisation and flow-down of equivalent terms; keep a Sub-processor List.
6. **Assistance with data-subject rights** — Help the controller respond to access/erasure/other requests.
7. **Breach notification and assistance** — Notify without undue delay; assist with obligations.
8. **DPIA and prior-consultation assistance** — Assist with impact assessments where required.
9. **Deletion or return at end** — Return or delete personal data at the controller's choice.
10. **Audit information and inspections** — Make available information to demonstrate compliance; allow audits.
11. **International transfers** — Only with a valid transfer mechanism (e.g. IDTA / UK Addendum to SCCs).
12. **Processing details schedule** — Subject matter; duration; nature and purpose; categories of personal data; categories of data subjects; controller rights/obligations; approved sub-processors; data locations; transfer mechanism; retention period; technical and organisational measures.
13. **Signature block** — Authorised signatories and dates.

## Inputs Required to Generate

- Controller and processor details; governing MSA/SOW reference.
- Processing details: subject matter, duration, nature/purpose, data categories, data-subject categories.
- Approved sub-processors, data locations, transfer mechanism, retention period.
- Technical and organisational security measures.

## UK Legal and Compliance Notes

- UK GDPR Article 28 requires specific mandatory provisions — all must be present.
- For restricted international transfers, use the ICO IDTA or the UK Addendum to the EU SCCs.
- Special-category data or large-scale/high-risk processing warrants DPO/solicitor review and possibly a DPIA.

## Best Practices and Pitfalls

- Complete the processing-details schedule fully; blanks undermine compliance.
- Keep the Sub-processor List current and notify the controller of changes.
- Use a Data Sharing Agreement for controller-to-controller sharing.

## Related Documents

- [Data Mapping Questionnaire](16_DATA_MAPPING_QUESTIONNAIRE_SKILL.md)
- [Sub-processor List](17_SUB_PROCESSOR_LIST_SKILL.md)
- [Security Schedule](11_SECURITY_SCHEDULE_SKILL.md)
- [Data Sharing Agreement](23_DATA_SHARING_AGREEMENT_SKILL.md)
- [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md)
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)
- [Business Documentation Index](README.md)
- [All Phase 05 Skills](../README.md)
- [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md)
- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md)

## Official References

- [ICO — Contracts between controllers and processors](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/)
- [ICO — What needs to be in the contract](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Complete, generate-ready UK business-document skill. |
