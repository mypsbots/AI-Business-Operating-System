---
id: LEMURAN-UK-01
title: "Business facts, scope and applicability"
document_type: "Knowledge Article"
owner: "Lemuran director — assignment pending"
status: Draft for human review
classification: Internal
version: 1.1.0
updated: "2026-10-10"
created: "2026-10-09"
verified_on: "2026-10-09"
jurisdiction: United Kingdom
legal_advice_status: Decision support; not a legal opinion
---

# Business facts, scope and applicability

## Executive summary

Lemuran Ltd is the company-wide scope. Maintain a portfolio of all products, services and internal activities; FAQai.app is one known product. Separate each product and engagement’s obligations while aggregating entity-level governance and relevant taxable turnover. Never assume a new brand is a separate legal entity or inherits another product’s legal approval. Confirm the contracting entity in every matter. The following is an intake, not a statement of established facts.

## Required intake

| Field | Evidence/input required | Consequence if unknown |
|---|---|---|
| Exact company name, number, status and incorporation nation | Companies House record plus director confirmation | Do not create a filing or final contracting party |
| Registered office/email, directors, PSCs, shareholders | Current register, private records, identity-verification status | Escalate discrepancy; keep personal codes outside Git |
| Accounting reference date, CT periods, trading start | Accountant/HMRC records | Deadline calculations remain provisional |
| VAT registration, taxable supplies, imported services | VAT certificate and 12-month ledger | No final tax treatment or tax invoice approval |
| Staff/contractors, working countries and status | Engagement records and actual working arrangements | Employment and overseas duties unresolved |
| FAQai.app functions | Architecture, demo, permissions, public claims | Do not infer “simple FAQ tool” is low risk |
| Agency services | Discovery, implementation, hosting, support, client accounts | Map each party's delivery and data responsibilities |
| B2B/B2C and sales countries | Checkout restrictions, customer declarations, usage | Consumer and international obligations remain possible |
| End users and vulnerable people | Age/access research; sector/customer uses | Children, accessibility and high-impact screening required |
| Data lifecycle | Inputs, uploads, URLs, prompts, embeddings, logs, outputs, backups | Privacy notice/DPA cannot be finalised |
| Model/hosting/support/payment vendors | Legal entity, terms, DPA, region and remote access | Transfer and onward processing unresolved |
| Training and product analytics | Actual settings and supplier rights | Never promise no training without evidence |
| Agent powers | Read/write tools, spending, external communications | Set human approval and permission boundaries |
| Ownership | Founder, employee and contractor assignments; OSS inventory | No promise of unrestricted ownership or exclusivity |
| Contracts/insurance | Executed versions and schedules | Do not treat proposed terms as existing commitments |

## Applicability decision sequence

1. Identify the legal entity, territory and activity date. Separate present law from forthcoming changes.
2. Determine customer capacity and actual purpose. A sole trader can buy for business, but is an individual subscriber under PECR. A B2B label does not settle either question.
3. For each processing purpose, decide controller, processor, joint controller or no personal data. Contracts must match reality.
4. Assess regulated sectors, significant automated decisions, special-category/criminal data, children, public-sector procurement, online-safety functionality and international markets.
5. Produce an obligation record with `applicable`, `not_applicable` or `unknown`, supporting facts and evidence. `not_applicable` requires a reason and recheck trigger.
6. Route tax to the accountant, legal interpretation and high-risk contracts to qualified counsel, security claims to engineering, and commercial acceptance to the authorised director.

## Example assumptions to test

FAQai.app might ingest customer help material and answer visitors' questions. If so, the customer may control visitor processing and Lemuran may process it; Lemuran can separately control billing, security and marketing. The agency might administer customer systems or implement automations: access to live data and decisions about processing determine roles, not who pays the cloud bill. These are hypotheses until the actual system is mapped.

## Legal expansion triggers

| Trigger | Required assessment before affected release or sale |
|---|---|
| Healthcare, lending, employment, education, legal advice or eligibility decisions | Sector law, discrimination, liability, DPIA and automated decision rules |
| Children likely to access | ICO Children's Code scope, age-appropriate design and safeguarding |
| Public sharing or multi-site live search | Ofcom Online Safety Act scope assessment |
| EU establishment, targeting or monitoring | EU GDPR, representation, EU AI Act roles and applicability; relevant national consumer/tax law |
| India, US or another new market | Local privacy/consumer/tax, sanctions and enforceability review |
| Equity investment or acquisition | Companies Act processes, cap table and possible National Security and Investment screening |
| Public procurement | Contractual security, accessibility and reporting requirements; do not assume all private-sector duties match |

## Responsibilities and acceptance

Director owns the fact record; functional owners supply evidence. No sensitive customer data or identity documents belong in a general LLM knowledge pack. Use evidence pointers with access controls. Acceptance: every critical field is evidenced or explicitly unknown, and unknowns affecting a decision are surfaced before action.

References: [Companies House](https://www.gov.uk/limited-company-formation), [ICO processor contracts](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/), [Ofcom scope](https://www.ofcom.org.uk/os-toolkit/regulation-checker/regulation-checker). Verified 2026-10-09.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
