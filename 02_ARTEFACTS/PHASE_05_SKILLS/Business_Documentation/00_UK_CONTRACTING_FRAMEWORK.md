---
id: BIZDOC-000
title: UK Contracting Framework (Reference)
document_type: Reference
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
  - business-documentation
  - contracts
  - reference
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md
---

# UK Contracting Framework (Reference)

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Business Docs](README.md) · [Source Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)

## Legal Notice

> **Legal notice.** This skill produces a **draft** business document to speed up preparation. It is **not legal advice** and is **not a substitute for review by a UK-qualified solicitor**. For high-value, regulated, international, security-sensitive or complex engagements, obtain solicitor sign-off before signing. Unless otherwise agreed, the governing law is **England and Wales**. Do not store passwords, API keys or production credentials in generated documents.

## Overview

This is the shared reference for the AIBOS Business Documentation skills. It captures
the recommended contract architecture, document set, order of precedence, signing
order and drafting principles for United Kingdom (England and Wales) B2B technology
engagements. It is derived from the
[Lemuran Ltd — UK Client Engagement Legal Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md) and standard UK best
practice. Each skill in this folder generates one document consistent with this
framework.

## Recommended Contract Architecture

```text
Customer enquiry -> Discovery call -> NDA (where required)
   -> Proposal / Quotation -> Due diligence & risk review
   -> MSA + SOW + DPA/SLA (where applicable) -> Both parties sign
   -> Deposit / first milestone -> Delivery
   -> Change Requests (for scope changes) -> Testing & acceptance
   -> Acceptance Certificate -> Final invoice, support, renewal or closure
```

For most B2B AI and software projects use **MSA + SOW + DPA (where personal data is
processed) + SLA (where ongoing service commitments apply)**, supported by an **NDA**
before detailed disclosure, **Change Requests** during delivery, and an **Acceptance
Certificate** at completion. For a small, low-risk project, combine terms into one
well-drafted [Business Customer Terms and Conditions](26_BUSINESS_CUSTOMER_TERMS_SKILL.md)
(Services Agreement) with schedules.

## Essential Document Pack

| # | Document | Purpose |
| --- | --- | --- |
| 01 | [Mutual Non-Disclosure Agreement](01_MUTUAL_NDA_SKILL.md) | Protects confidential information both parties share before the commercial contract is signed. |
| 02 | [Proposal](02_PROPOSAL_SKILL.md) | Explains the recommended solution and the commercial offer to the customer. |
| 03 | [Quotation](03_QUOTATION_SKILL.md) | A concise priced offer for a defined, lower-complexity piece of work. |
| 04 | [Master Services Agreement](04_MASTER_SERVICES_AGREEMENT_SKILL.md) | The umbrella legal and commercial terms governing the whole customer relationship; individual projects run under separate SOWs. |
| 05 | [Statement of Work](05_STATEMENT_OF_WORK_SKILL.md) | Defines exactly what will be delivered for one project, with acceptance criteria and payment milestones, under the MSA. |
| 06 | [Data Processing Agreement](06_DATA_PROCESSING_AGREEMENT_SKILL.md) | The UK GDPR-mandated controller–processor contract used where the Supplier processes personal data on the customer's behalf. |
| 07 | [Change Request](07_CHANGE_REQUEST_SKILL.md) | Formalises any agreed change to scope, price, timeline or deliverables during delivery. |
| 08 | [Acceptance Certificate](08_ACCEPTANCE_CERTIFICATE_SKILL.md) | Records the customer's written acceptance of deliverables and triggers warranty and final invoicing. |
| 09 | [Invoice](09_INVOICE_SKILL.md) | A compliant demand for payment referencing the SOW/PO and agreed milestones. |

## Extended Document Pack

| # | Document | Purpose |
| --- | --- | --- |
| 10 | [Service Level Agreement](10_SERVICE_LEVEL_AGREEMENT_SKILL.md) | Defines service levels, response/resolution targets and remedies for ongoing managed services, hosting or support. |
| 11 | [Security Schedule](11_SECURITY_SCHEDULE_SKILL.md) | Sets the information-security controls the Supplier applies when handling sensitive data or privileged system access. |
| 12 | [AI and Responsible Use Schedule](12_AI_RESPONSIBLE_USE_SCHEDULE_SKILL.md) | Sets the responsible-AI terms, limitations and risk allocation for AI-related deliverables. |
| 13 | [Requirements Specification](13_REQUIREMENTS_SPECIFICATION_SKILL.md) | Documents functional and non-functional requirements for development or automation work. |
| 14 | [Project Plan](14_PROJECT_PLAN_SKILL.md) | Sets out the work breakdown, milestones, owners, dependencies and cadence for larger projects. |
| 15 | [Risk Register](15_RISK_REGISTER_SKILL.md) | Tracks project risks with likelihood, impact, owners and mitigations. |
| 16 | [Data Mapping Questionnaire](16_DATA_MAPPING_QUESTIONNAIRE_SKILL.md) | Captures what personal data is involved, so the correct data-protection terms can be applied. |
| 17 | [Sub-processor List](17_SUB_PROCESSOR_LIST_SKILL.md) | The maintained register of approved sub-processors disclosed to the customer under the DPA. |
| 18 | [Customer Due-Diligence Checklist](18_CUSTOMER_DUE_DILIGENCE_CHECKLIST_SKILL.md) | The pre-engagement checks confirming who the customer is and whether the work is safe to accept. |
| 19 | [Project Closure Report](19_PROJECT_CLOSURE_REPORT_SKILL.md) | Formally closes a project: outcomes, acceptance, outstanding items, lessons and handover. |
| 20 | [Support and Maintenance Agreement](20_SUPPORT_AND_MAINTENANCE_AGREEMENT_SKILL.md) | Governs ongoing support, maintenance and updates after go-live, usually with an SLA. |
| 21 | [Subcontractor Agreement](21_SUBCONTRACTOR_AGREEMENT_SKILL.md) | Governs work the Supplier subcontracts to a specialist, flowing down customer obligations. |
| 22 | [Independent Contractor Agreement](22_INDEPENDENT_CONTRACTOR_AGREEMENT_SKILL.md) | Engages an individual contractor, clarifying self-employed status, IP assignment and confidentiality. |
| 23 | [Data Sharing Agreement](23_DATA_SHARING_AGREEMENT_SKILL.md) | Governs controller-to-controller personal-data sharing (where a processor DPA is not the right instrument). |
| 24 | [Website Privacy Notice](24_WEBSITE_PRIVACY_NOTICE_SKILL.md) | The public UK GDPR transparency notice explaining how the business handles personal data on its website. |
| 25 | [Website Cookie Notice](25_WEBSITE_COOKIE_NOTICE_SKILL.md) | Explains cookies/similar technologies and obtains PECR-compliant consent for non-essential cookies. |
| 26 | [Business Customer Terms and Conditions](26_BUSINESS_CUSTOMER_TERMS_SKILL.md) | Standard B2B terms for lower-complexity engagements, or a combined Services Agreement for small projects. |
| 27 | [Consumer Terms](27_CONSUMER_TERMS_SKILL.md) | Separate terms for individuals buying outside their trade, with mandatory consumer protections. |

## Order of Precedence (Contract Hierarchy)

State the hierarchy expressly in the MSA. Recommended order:

1. Signed Change Request
2. Statement of Work
3. Data Processing Agreement (for data-protection matters)
4. Service Level Agreement (for service-level matters)
5. Master Services Agreement
6. Proposal
7. Purchase Order

## Recommended Signing Order

**Standard project:** NDA (if required) → Proposal marked "subject to contract" →
customer due-diligence checks → MSA → SOW → DPA and Security Schedule (where
required) → SLA (where required) → both parties sign → deposit or first invoice
paid → kick-off.

**Very small project:** one combined Services Agreement and SOW covering scope,
deliverables, timeline, price, payment, IP, confidentiality, data protection,
liability, termination, acceptance, governing law and signatures.

## Minimum Clause Checklist

- Correct legal parties; scope and exclusions; deliverables; timeline and milestones
- Customer dependencies; fees and payment dates; expenses and taxes; change control
- Acceptance testing; intellectual property (incl. Background IP); third-party and open-source components
- Confidentiality; data protection; information security; AI-specific risks
- Warranties; liability cap; excluded losses; indemnities; insurance
- Subcontractors; suspension; termination; exit and data deletion; dispute escalation
- Governing law; signature authority

## Intellectual Property Principles

- The Supplier normally retains **Background IP** (frameworks, templates, libraries, prompts, reusable code, tools, know-how, models, connectors).
- The customer receives ownership or a broad licence to the **bespoke paid-for deliverables**; assignment or final licence takes effect **only after full payment**.
- **Third-party and open-source** components remain subject to their own licences — the Supplier cannot grant greater rights than it holds.
- UK copyright in commissioned work is not transferred automatically; assignment must be **in writing and signed**.

## Payment and Financial Protections

- New customers: 30%–50% deposit; milestone payments; final balance on acceptance; recurring services billed in advance.
- Clear payment terms (e.g. "payable within 14 days of the invoice date").
- Late payment: for qualifying B2B debts, statutory interest is generally **8% above the Bank of England base rate** plus fixed compensation; review contractual interest wording against statutory rights.
- Allow **suspension** after overdue payment, written notice and a reasonable cure period.

## Liability and Risk Allocation

- Cap ordinary contractual liability (e.g. fees under the relevant SOW, or fees paid in the previous 12 months) aligned to insurance.
- Exclude indirect/consequential loss, lost profits/revenue/business, loss of goodwill (where legally permitted).
- Do **not** exclude non-excludable liabilities (death/personal injury from negligence, fraud). A solicitor should draft this section.
- Use indemnities carefully — they can create uncapped exposure.

## Customer Due Diligence

Verify legal name, Companies House record, addresses, VAT number, authorised
signatory, creditworthiness, sanctions exposure, adverse media (higher-risk work),
data source/use, regulated-sector requirements, project legality, ability to pay and
conflicts of interest before accepting work.

## Insurance to Consider

Professional Indemnity; Cyber; Public Liability; Employers' Liability (if required);
Directors' and Officers'; Legal Expenses. Align liability caps with available cover.

## Internal Approval (Director Sign-off) Triggers

Value over threshold; unlimited liability; cap exceeding insurance; customer wants
Supplier Background IP; exclusivity; broad indemnities; special-category data;
complex international transfers; regulated decision-making; certifications not held;
extended payment terms; foreign law/courts; subcontracting prohibited; source-code
escrow; unusually high penalties or service credits.

## Practical Operating Rules

1. Do not start work without a signed agreement.
2. Do not start changed work without an approved Change Request.
3. Collect a deposit for new or higher-risk customers.
4. Define acceptance objectively.
5. Keep reusable IP outside customer ownership.
6. Do not process customer personal data without the correct data terms.
7. Do not accept unlimited liability without specialist legal review.
8. Keep all signed versions and audit trails.
9. Review the contract against insurance.
10. Use a solicitor for high-risk or high-value engagements.

## Official References

- [ICO — Contracts between controllers and processors](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/)
- [UK IPO — Ownership of copyright works](https://www.gov.uk/guidance/ownership-of-copyright-works)
- [GOV.UK — Electronic execution of documents](https://www.gov.uk/government/publications/electronic-execution-of-documents)
- [Small Business Commissioner — Late-payment guidance](https://www.smallbusinesscommissioner.gov.uk/help-and-guidance/interest-calculator/)

## Related Resources

- [Business Documentation Index](README.md)
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)
- [All Phase 05 Skills](../README.md)
- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | UK contracting framework reference for the Business Documentation skills. |
