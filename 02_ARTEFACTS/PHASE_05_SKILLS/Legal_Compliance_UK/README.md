---
id: LEMURAN-UK-INDEX
title: Legal & Compliance (UK) — Skill Index
document_type: Index
category: Legal and Compliance (UK)
phase: Phase 05
owner: Director / legal operations lead
status: Draft for review
version: 1.1.0
created: 2026-10-07
updated: 2026-10-10
jurisdiction: United Kingdom
---

# Legal & Compliance (UK) — Skill Index

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Knowledge Pack](../../PHASE_10_KNOWLEDGE/Business/LEMURAN_UK_LEGAL_PACK/00_START_HERE.md) · [Charter](../../PHASE_10_KNOWLEDGE/Business/LEMURAN_UK_LEGAL_PACK/20_LEGAL_TEAM_CHARTER.md)

## Legal Notice

> **Legal notice.** This is an AIBOS *skill specification* for decision-support and drafting. It is **not legal advice**, **not a legal opinion**, and the AI function is **not a qualified solicitor**. It does **not** certify blanket compliance and does **not** replace accountable human decisions. UK legal sources were last verified on **2026-10-09**; decisive authority and commencement must be re-checked at execution time. No agreement is signed, filing submitted, payment made, external message sent, live policy published or production processing changed without the human approval gate named below.

## What this is

25 AIBOS *skill specifications* implementing Lemuran Ltd's company-wide, AI-assisted Legal & Compliance function across corporate governance, internal operations, every service engagement and all current and future products. They are decision-support/drafting specs that inherit the [common execution contract](00_COMMON_EXECUTION_CONTRACT.md) and cite the integrated [knowledge pack](../../PHASE_10_KNOWLEDGE/Business/LEMURAN_UK_LEGAL_PACK/00_START_HERE.md).

## Start here (company-wide spine)

- [Legal Matter Intake & Triage](23_INTAKE_SKILL.md) — routes every matter to an owner, deadline and specialist.
- [Portfolio Applicability](24_PORTFOLIO_SKILL.md) — per-scope obligation records; no inherited approvals.
- [Official Document Control](25_DOCUMENTS_SKILL.md) — draft/approve/version/issue lifecycle with G2 binding.
- [Common Execution Contract](00_COMMON_EXECUTION_CONTRACT.md) — envelopes, statuses, guardrails, gates.

## All skills

| Skill | Runtime name | Owner | Gates |
| --- | --- | --- | --- |
| [Governance](01_GOVERNANCE_SKILL.md) | `uk-company-governance` | Director | G1 |
| [Filings](02_FILINGS_SKILL.md) | `uk-companies-house-calendar` | Director / authorised filer | G1 |
| [Tax](03_TAX_SKILL.md) | `uk-tax-and-payroll-review` | Accountant and director | G1 |
| [VAT](04_VAT_SKILL.md) | `uk-vat-sales-classification` | Accountant | G1 |
| [Privacy](05_PRIVACY_SKILL.md) | `uk-privacy-and-ico` | Privacy lead | G2, G3 |
| [DPIA](06_DPIA_SKILL.md) | `uk-dpia-and-decision-safeguards` | Privacy lead / counsel / director | G3 |
| [Rights](07_RIGHTS_SKILL.md) | `uk-data-rights-and-complaints` | Privacy lead | G4 |
| [Transfers](08_TRANSFERS_SKILL.md) | `uk-data-transfer-review` | Privacy lead / counsel | G3 |
| [PECR](09_PECR_SKILL.md) | `uk-pecr-cookie-review` | Privacy lead / engineering | G2, G6 |
| [Marketing](10_MARKETING_SKILL.md) | `uk-marketing-permission-review` | Marketing / privacy lead | G2 |
| [SaaS](11_SAAS_SKILL.md) | `uk-saas-contract-review` | Counsel / authorised signatory | G2 |
| [Agency](12_AGENCY_SKILL.md) | `uk-agency-msa-sow` | Project owner / signatory | G2 |
| [Consumer](13_CONSUMER_SKILL.md) | `uk-consumer-sales-review` | Counsel / product owner | G2, G6 |
| [IP](14_IP_SKILL.md) | `uk-ip-and-licensing` | Legal / engineering | G2 |
| [AI](15_AI_SKILL.md) | `uk-ai-risk-release` | Product owner / counsel / privacy | G3, G6 |
| [Security](16_SECURITY_SKILL.md) | `uk-security-and-incident` | Incident lead / privacy / director | G4, G6 |
| [People](17_PEOPLE_SKILL.md) | `uk-people-contractor-compliance` | HR / employment adviser / director | G5, G6 |
| [Insurance](18_INSURANCE_SKILL.md) | `uk-insurance-commitment-review` | Director / broker | G5 |
| [International](19_INTERNATIONAL_SKILL.md) | `uk-international-market-screen` | Director / counsel / accountant | G2, G3 |
| [Disputes](20_DISPUTES_SKILL.md) | `uk-dispute-and-legal-hold` | Counsel / authorised owner | G4, G5 |
| [Retention](21_RETENTION_SKILL.md) | `uk-records-retention` | Data owner / privacy / legal | G6 |
| [Monitoring](22_MONITORING_SKILL.md) | `uk-legal-source-monitor` | Compliance maintainer / counsel | G2 |
| [Intake](23_INTAKE_SKILL.md) | `lemuran-legal-matter-intake` | Director / legal operations lead | G4 |
| [Portfolio](24_PORTFOLIO_SKILL.md) | `lemuran-product-service-legal-onboarding` | Product/service owner and legal lead | G2, G3 |
| [Documents](25_DOCUMENTS_SKILL.md) | `lemuran-official-legal-document-control` | Legal operations / authorised signatory | G1, G2, G4 |

## Tests

See [Acceptance Tests](ACCEPTANCE_TESTS.md) and the synthetic `fixtures/` directory. Tests are specifications and static fixtures; they are not claimed as executed live-agent runs.

## Manifest

Machine-readable routing data: `LEGAL_SKILL_CATALOGUE.json`.

## Generated by

`tools/generate_legal_compliance_skills.py` — regenerate after editing the knowledge pack catalogue; do not hand-edit generated files.
