---
id: LEMURAN-UK-04
title: "UK GDPR, ICO and international data transfers"
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

# UK GDPR, ICO and international data transfers

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## Scope and responsibilities

Privacy lead maintains the processing inventory; engineering verifies the data map; director approves material risk; counsel resolves contested roles, lawful bases and high-risk processing. A privacy lead is not automatically a statutory DPO. Assess DPO criteria (including relevant large-scale monitoring or special-category processing) and independence requirements. Sources P01–P11; authoritative law is UK GDPR and DPA 2018 as amended by the Data (Use and Access) Act 2025 (DUAA).

## Core controls

| ID / classification | Decision/control | Evidence |
|---|---|---|
| PRIV-01 LAW | Establish purpose, Article 6 lawful basis, fairness, transparency, minimisation, accuracy, retention and security for each activity | Processing inventory and notice mapping |
| PRIV-02 CONDITIONAL LAW | Special-category data needs an Article 9 condition as well as Article 6; criminal-offence data needs its separate legal route | Condition, necessity assessment, any required policy document |
| PRIV-03 LAW | Classify each controller/processor relationship by actual decisions; use Article 28 terms for processor arrangements | Role memo, signed DPA and supplier chain |
| PRIV-04 CONDITIONAL LAW | Pay ICO data-protection fee unless exempt; check fee band and renew | Assessment, registration/renewal evidence |
| PRIV-05 CONDITIONAL LAW | DPIA before likely high-risk processing; consult ICO if residual high risk cannot be mitigated | DPIA, risks, mitigations, approvals |
| PRIV-06 LAW | Enable access, correction, deletion, restriction, objection and portability where applicable | Request log, deadline, identity/risk checks, response |
| PRIV-07 LAW | Record and assess breaches; notify according to role and risk | Incident record, decision and notification receipts |
| PRIV-08 CONDITIONAL LAW | Comply with restricted-transfer rules for overseas recipients/access | Transfer inventory, mechanism and assessment |
| PRIV-09 LAW | Provide a data-protection complaint route and required handling process | Contact channel, acknowledgement and investigation log |

[UK GDPR authority](https://www.legislation.gov.uk/eur/2016/679/contents), [ICO accountability contracts](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/contracts), [DPIA guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/).

## FAQai.app and agency data mapping — proposed implementation

Document data from collection to deletion, including customer-uploaded files, crawled web pages, chat transcripts, vector embeddings, support tickets, telemetry, billing, model-provider logs and backups. Record tenants, regions, remote support countries, access roles, retention and model-training settings. Embeddings or pseudonymous IDs are not automatically anonymous.

For FAQai.app, separate customer-instructed answers from Lemuran's billing, fraud/security and marketing purposes. For the agency, map access in client-owned tools, hosting under Lemuran accounts, exports and subcontractors. Customer approval does not remove Lemuran's own duties. A supplier using inputs for its own model training may not be acting solely as processor; reassess purpose, disclosure, lawful basis and contract before enabling that use.

**POLICY defaults pending adoption:** no customer-content model training; segregated tenants; minimise prompt/log content; synthetic data for tests; special-category and children's data excluded from ordinary onboarding until reviewed. Do not publish these as factual promises until verified in all relevant systems and vendor terms.

## Individual rights and complaints

Access requests normally require response without undue delay and within one month. A qualifying extension can add up to two months, with timely explanation. Reasonable identity/clarification handling and proportionate searches have legal limits; do not reset clocks simply because a request is inconvenient. Track original receipt and any justified adjustment separately. Review third-party information and exemptions before disclosure. A processor routes requests to its controller and assists rather than making the controller's substantive decision. [Current ICO access guide](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/subject-access-requests/a-guide-to-subject-access/).

The data-protection complaints duty is in force: supply a clear route, acknowledge within 30 days, investigate appropriately and communicate the result. Thirty days is an acknowledgement limit, not a universal final-resolution deadline. Keep rights requests and complaints as separate clocks even when one message contains both. [ICO, June 2026](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/new-data-protection-complaints-law-now-in-force/).

## Breaches

A controller reports a personal-data breach to the ICO unless it is unlikely to risk people's rights and freedoms; where reportable, act without undue delay and within 72 hours of awareness where feasible, explaining delay. High risk to individuals triggers notice to them without undue delay, subject to lawful exceptions. A processor informs the controller without undue delay; 72 hours is not a universal processor grace period. Log all breaches and non-notification reasons. Do not wait for complete forensics if an initial report is due. [ICO breach reporting](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/).

## Restricted transfers

Apply the ICO transfer test to the exporter, separate overseas receiver and processing relationship; mere foreign nationality is not the test. Overseas remote support can matter even with UK hosting. Record onward transfers and subprocessors.

- Where relevant UK adequacy regulations cover the receiver and activity, document scope and continuing validity.
- Otherwise assess appropriate safeguards, usually UK IDTA or EU SCCs plus the UK Addendum, and the required transfer risk assessment/data protection test. EU SCCs alone do not cover a UK restricted transfer.
- For a US recipient relying on the UK Extension to the Data Privacy Framework, check that exact entity's active participation, UK Extension and covered data; preserve dated evidence.
- Article 49 exceptions are narrowly interpreted and usually unsuitable as the default for routine SaaS outsourcing. Contract necessity is not established merely by writing a transfer into terms.

[ICO transfer guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/), [approved clauses](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/appropriate-safeguards/what-are-standard-data-protection-clauses-the-uk-idta-and-the-addendum/).

## Checklist and acceptance

- [ ] Purpose-by-purpose roles and notices match actual settings.
- [ ] Article 30 documentation requirement assessed; under-250-staff exception is not a blanket exemption. Regular SaaS processing warrants a maintained inventory.
- [ ] Fee, DPO, DPIA and children's-code applicability decisions evidenced.
- [ ] Rights, complaint and incident channels tested end to end.
- [ ] Supplier chain, transfer mechanisms and deletion capability verified.

Acceptance: reviewed data map, appropriate legal basis/condition, notice/DPA evidence and unresolved-risk register. Verification 2026-10-09; DUAA-affected guidance marked under review must be checked against current legislation before a sensitive decision.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
