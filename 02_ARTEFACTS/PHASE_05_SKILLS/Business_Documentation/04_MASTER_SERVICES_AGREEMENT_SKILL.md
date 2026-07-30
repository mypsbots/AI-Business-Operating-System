---
id: BIZDOC-004
title: Master Services Agreement — Generation Skill
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
  - master-services-agreement
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

# Master Services Agreement — Generation Skill

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Business Docs](README.md) · [UK Framework](00_UK_CONTRACTING_FRAMEWORK.md) · [Source Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)

## At a Glance

The umbrella legal and commercial terms governing the whole customer relationship; individual projects run under separate SOWs.

| Field | Detail |
| --- | --- |
| Document | Master Services Agreement |
| Category | Business Documentation |
| Jurisdiction | England and Wales (UK) |
| Pack | Essential |
| Binding status | Binding once signed; governs all SOWs executed under it. |
| Typical signatories | Authorised signatory of the Supplier and of the Customer. |
| AI automation | AI-draftable from a firm-approved base; SOLICITOR review required before first use and for non-standard terms. |

## Legal Notice

> **Legal notice.** This skill produces a **draft** business document to speed up preparation. It is **not legal advice** and is **not a substitute for review by a UK-qualified solicitor**. For high-value, regulated, international, security-sensitive or complex engagements, obtain solicitor sign-off before signing. Unless otherwise agreed, the governing law is **England and Wales**. Do not store passwords, API keys or production credentials in generated documents.

## Purpose

The Master Services Agreement (MSA) contains the legal and commercial rules that apply across the entire customer relationship. It is signed once; each project is then documented via its own Statement of Work that incorporates the MSA.

This separation lets the Supplier reuse stable legal terms while tailoring scope, price and risk per project in the SOW.

## When to Use

- Any ongoing or multi-project B2B relationship.
- Where the Supplier wants stable terms with per-project SOWs.
- As the backbone of the recommended MSA + SOW + DPA + SLA stack.

## Document Blueprint (Generation Template)

When this skill is invoked, generate the document by expanding each blueprint section below into clear, formal UK business English, filling every placeholder from the *Inputs Required*, resolving or flagging any missing input, marking the output as a draft, and appending a dated signature block for the authorised signatories. Keep numbering and the order of precedence consistent with the [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md).

1. **1. Parties and company details** — Full legal names, company numbers, registered offices.
2. **2. Definitions and interpretation** — Defined terms used throughout.
3. **3. Contract structure and document priority** — How MSA, SOW, DPA, SLA and Change Requests fit together and the order of precedence.
4. **4. Services and standard of performance** — Reasonable skill and care; conformance to the SOW.
5. **5. Customer responsibilities and dependencies** — Access, data, decisions, approvals the customer must provide.
6. **6. Project governance and authorised contacts** — Named contacts, escalation, meetings.
7. **7. Fees, expenses, invoicing, taxes and payment** — Charging basis, invoicing cadence, VAT, payment days.
8. **8. Late payment** — Interest and remedies for overdue amounts (see UK notes).
9. **9. Changes and Change Requests** — No changed work without an approved Change Request.
10. **10. Intellectual property** — Ownership of deliverables vs Background IP; assignment on payment.
11. **11. Licensing of pre-existing materials** — Licence for Supplier Background IP embedded in deliverables.
12. **12. Open-source software** — Disclosure and licence compliance for OSS components.
13. **13. AI and third-party technology** — Model/provider dependencies and limitations (see AI Schedule).
14. **14. Confidentiality** — Mutual confidentiality obligations.
15. **15. Data protection** — UK GDPR roles; DPA applies where personal data is processed.
16. **16. Information security** — Security obligations; Security Schedule where applicable.
17. **17. Warranties** — Skill and care; qualified personnel; authority; AI-specific limitations.
18. **18. Indemnities** — Carefully scoped indemnities (e.g. third-party IP, customer content).
19. **19. Limitation of liability** — Caps and excluded losses; non-excludable liabilities preserved.
20. **20. Insurance** — Levels of cover the Supplier maintains, aligned to liability caps.
21. **21. Subcontractors** — Right to subcontract; Supplier remains responsible.
22. **22. Non-solicitation** — Reasonable, time-limited, where justified.
23. **23. Compliance with laws** — Both parties comply with applicable law.
24. **24. Anti-bribery and sanctions** — ABC and sanctions compliance.
25. **25. Publicity and use of customer name** — Consent required to name the customer.
26. **26. Suspension rights** — Suspend on non-payment or risk, after notice and cure.
27. **27. Term and termination** — Duration; termination for cause / convenience / insolvency.
28. **28. Consequences of termination** — Payment for work done; licence effects; survival.
29. **29. Exit assistance and data return** — Handover, data return/deletion at exit.
30. **30. Force majeure** — Relief for events beyond reasonable control.
31. **31. Dispute escalation** — Escalation and, optionally, mediation before litigation.
32. **32. Notices** — How formal notices are given.
33. **33. Assignment** — Restrictions on assignment/novation.
34. **34. Third-party rights** — Whether the Contracts (Rights of Third Parties) Act is excluded.
35. **35. Entire agreement** — Supersedes prior discussions (with fraud carve-out).
36. **36. Variation** — Changes only in writing and signed.
37. **37. Waiver and severability** — Standard boilerplate.
38. **38. Electronic signatures and counterparts** — E-signature and counterpart execution permitted.
39. **39. Governing law and jurisdiction** — England and Wales; exclusive jurisdiction of its courts.
40. **Signature block** — Authorised signatories, titles, dates.

## Inputs Required to Generate

- Supplier and Customer legal details and authorised signatories.
- Firm-standard positions: liability cap basis, IP model, payment days, insurance levels.
- Any negotiated deviations (flag for solicitor review).

## UK Legal and Compliance Notes

- Recommended governing law: the laws of England and Wales, with exclusive jurisdiction of the courts of England and Wales.
- Do not exclude non-excludable liabilities (death/personal injury from negligence, fraud, or others that cannot be limited by law).
- International customers may request arbitration/foreign law — obtain legal advice before agreeing.
- The MSA must expressly state the order of precedence with SOW/DPA/SLA/Change Requests.

## Best Practices and Pitfalls

- Keep the MSA stable; put project specifics in the SOW.
- Align the liability cap to available insurance.
- Have a UK commercial solicitor produce/review the first reusable MSA.

## Related Documents

- [Statement of Work](05_STATEMENT_OF_WORK_SKILL.md)
- [Data Processing Agreement](06_DATA_PROCESSING_AGREEMENT_SKILL.md)
- [Service Level Agreement](10_SERVICE_LEVEL_AGREEMENT_SKILL.md)
- [Security Schedule](11_SECURITY_SCHEDULE_SKILL.md)
- [AI and Responsible Use Schedule](12_AI_RESPONSIBLE_USE_SCHEDULE_SKILL.md)
- [Business Customer Terms and Conditions](26_BUSINESS_CUSTOMER_TERMS_SKILL.md)
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
