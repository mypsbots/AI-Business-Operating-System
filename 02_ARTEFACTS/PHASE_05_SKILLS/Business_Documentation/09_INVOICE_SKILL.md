---
id: BIZDOC-009
title: Invoice — Generation Skill
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
  - invoice
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md
  - 02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/00_UK_CONTRACTING_FRAMEWORK.md
standards:
  - HMRC VAT rules
  - ISO 27001
---

# Invoice — Generation Skill

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Business Docs](README.md) · [UK Framework](00_UK_CONTRACTING_FRAMEWORK.md) · [Source Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)

## At a Glance

A compliant demand for payment referencing the SOW/PO and agreed milestones.

| Field | Detail |
| --- | --- |
| Document | Invoice |
| Category | Business Documentation |
| Jurisdiction | England and Wales (UK) |
| Pack | Essential |
| Binding status | A payment demand supported by the signed contract; not itself a contract. |
| Typical signatories | Issued by the Supplier; no customer signature required. |
| AI automation | Fully AI-generatable from milestone + company data; human/finance check of VAT and totals. |

## Legal Notice

> **Legal notice.** This skill produces a **draft** business document to speed up preparation. It is **not legal advice** and is **not a substitute for review by a UK-qualified solicitor**. For high-value, regulated, international, security-sensitive or complex engagements, obtain solicitor sign-off before signing. Unless otherwise agreed, the governing law is **England and Wales**. Do not store passwords, API keys or production credentials in generated documents.

## Purpose

An Invoice requests payment for services delivered, referencing the governing SOW/PO and the agreed milestone so it is auditable and enforceable.

It must contain the correct legal and (where applicable) VAT details to be valid and payable.

## When to Use

- At deposit, each milestone, and on acceptance/final balance.
- For recurring services billed in advance.

## Document Blueprint (Generation Template)

When this skill is invoked, generate the document by expanding each blueprint section below into clear, formal UK business English, filling every placeholder from the *Inputs Required*, resolving or flagging any missing input, marking the output as a draft, and appending a dated signature block for the authorised signatories. Keep numbering and the order of precedence consistent with the [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md).

1. **Supplier legal name and address** — Legal name, registered/company address.
2. **Company number** — Where appropriate.
3. **Invoice number and date** — Unique sequential number; issue date.
4. **Customer details** — Billing name and address.
5. **Description of services** — What is being charged for.
6. **SOW or PO reference** — Link to the governing document and milestone.
7. **Net amount** — Amount before VAT.
8. **VAT details** — VAT number and amount, only where applicable / registered.
9. **Total due** — Gross total payable.
10. **Payment terms** — e.g. payable within 14 days of invoice date.
11. **Bank details** — Account for payment.
12. **Late-payment wording** — Statutory interest/compensation notice where appropriate.

## Inputs Required to Generate

- Supplier company details and bank details; VAT registration status.
- Customer billing details; SOW/PO reference and milestone.
- Net amount, VAT position, payment terms.

## UK Legal and Compliance Notes

- Only show VAT if VAT-registered; a valid VAT invoice has specific required content.
- For qualifying B2B debts, statutory late-payment interest is generally 8% above the Bank of England base rate plus fixed compensation; contractual interest wording can affect statutory rights.

## Best Practices and Pitfalls

- Reference the SOW/PO and milestone on every invoice.
- Keep invoice numbering sequential and auditable.

## Related Documents

- [Acceptance Certificate](08_ACCEPTANCE_CERTIFICATE_SKILL.md)
- [Statement of Work](05_STATEMENT_OF_WORK_SKILL.md)
- [Business Customer Terms and Conditions](26_BUSINESS_CUSTOMER_TERMS_SKILL.md)
- [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md)
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)
- [Business Documentation Index](README.md)
- [All Phase 05 Skills](../README.md)
- [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md)
- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md)

## Official References

- [Small Business Commissioner — Late-payment guidance](https://www.smallbusinesscommissioner.gov.uk/help-and-guidance/interest-calculator/)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Complete, generate-ready UK business-document skill. |
