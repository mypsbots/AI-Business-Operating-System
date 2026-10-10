---
id: LEMURAN-UK-09
title: "International sales, disputes and records retention"
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

# International sales, disputes and records retention

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## International market entry

UK incorporation does not displace overseas mandatory rules. **CONDITIONAL LAW:** assess privacy territorial scope, consumer protection, digital taxes/VAT/GST, sanctions/export controls, local employment and business establishment. Counsel/accountant should approve a country matrix before opening a new market; the gate is proposed company policy, while relevant underlying duties are legal.

| Market | Scope questions and required output |
|---|---|
| UK | Incorporation nation, customer type, sector, data role and tax registration |
| EEA | Targeting/monitoring under EU GDPR, Article 27 representative and exemptions, EU transfer rules, AI Act role, consumer/VAT rules and accessibility scope |
| US | State privacy/consumer/subscription requirements, sector laws, state sales-tax nexus and litigation/insurance coverage |
| India | Current DPDP Act/rules commencement and applicability, GST/OIDAR/withholding, contract enforcement and remote-worker status |
| Other | Local counsel/tax screening, languages, consumer rights, dispute forum and sanctions |

This is a UK pack: US/India requirements are **screening tasks, not verified legal conclusions**. Do not claim complete international compliance. UK restricted transfers and EU transfers require separate analysis; EEA-to-UK adequacy and UK-to-other-country adequacy are different decisions. Check current validity before relying on either.

**LAW:** applicable UK sanctions can prohibit transactions/services or dealings with designated parties, including relevant ownership/control. Screen countries, parties, beneficial ownership and service category proportionately; a name match needs review, not automatic accusation. Relevant licences/permissions must be verified. [UK sanctions regimes](https://www.gov.uk/government/collections/uk-sanctions-regimes-under-the-sanctions-act).

## Complaints and disputes

Create one intake with separate classifications: service complaint, consumer cancellation/refund, data-protection complaint, rights request, invoice dispute, IP notice, security incident, threatened claim or court/regulator document. Capture received time, service method, applicable contract/version, desired remedy, factual chronology and deadlines. Route urgent legal documents immediately; automated acknowledgement does not constitute a substantive defence.

**POLICY:** preserve evidence, suspend relevant routine deletion, involve counsel/insurer when appropriate, avoid admissions or threats without authority, and propose proportionate resolution. Do not promise legal privilege merely by labelling a record “privileged”; ordinary AI-generated legal notes are not automatically privileged. Keep lawyer communications separately controlled.

For agency payment disputes, inspect contractual payment/acceptance terms before suspension or collection. Statutory late-payment rights can apply to qualifying commercial debts; confirm rate, compensation and contract interaction before demanding them. They are not consumer-debt rules. [Late commercial payments](https://www.gov.uk/late-commercial-payments-interest-debt-recovery).

Consider applicable pre-action procedures and ADR; governing law/forum and limitation vary by jurisdiction and claim. In England and Wales many simple-contract claims have a six-year limitation period and deeds can have twelve, but accrual, concealment, special claims and other jurisdictions differ. These are not universal retention mandates or safe filing deadlines. Counsel calculates litigation dates from actual facts; never let an LLM close a case based on a generic period.

## Retention schedule

**LAW:** personal data must not be kept longer than necessary for its purpose; specific laws can require records. **PRACTICE/POLICY:** choose proportionate periods for other evidence, document justification, review holds, and delete across live systems, search indexes, embeddings, caches and backups according to a workable lifecycle.

| Record | Baseline / classification | Owner and trigger |
|---|---|---|
| Company financial/tax evidence | Normally 6 years from end of last financial year concerned, longer for statutory exceptions (LAW) | Finance; year end |
| Director meeting minutes | Companies Act s248 specifies at least 10 years (LAW; provision recheck before operational use) | Governance; meeting date |
| Member resolutions/meetings | Companies Act s355 specifies at least 10 years (LAW; provision recheck) | Governance; resolution/meeting |
| Executed contracts and acceptance evidence | Risk-based period considering limitation, claims and legal duties (POLICY) | Legal; expiry/termination/claim closure |
| PAYE records | At least 3 years from the end of the relevant tax year (LAW); other overlapping duties may require longer | Finance; tax year end |
| VAT records | Generally at least 6 years; relevant OSS/MOSS records 10 years (LAW, scheme-specific) | Finance; confirm applicable record/scheme trigger |
| Pension auto-enrolment records | Generally 6 years; opt-out records 4 years (LAW) | HR/finance; applicable record date |
| Minimum-wage evidence | At least 6 years under the current rule, starting at the end of the following pay reference period (LAW) | Payroll; preserve evidence of compliance |
| Right-to-work check evidence | Employment duration plus 2 years afterwards for the statutory-excuse route; maintain secure copies and check date | HR; end of employment |
| Other employment files | Purpose-specific schedule; do not retain all HR data for one generic period | HR/privacy; event-specific |
| Customer uploads/chats/embeddings | Agreed purpose/DPA; short documented operational period (LAW principle + CONTRACT/POLICY period) | Product/privacy; expiry or deletion request |
| Security logs | Justified detection/investigation duration, access controls and minimisation (POLICY) | Security; event date |
| Consent/suppression | Evidence needed to demonstrate permission and honour objections; minimal suppression identifiers | Marketing/privacy; last relevant use/objection |
| Incident/DPIA/rights records | Accountability evidence with category-specific risk/need review | Privacy; closure/review |
| Insurance policies/claims | Claims-made and long-tail needs; broker/legal review | Finance/legal; policy/claim dates |

Sources: [company records](https://www.gov.uk/running-a-limited-company/company-and-accounting-records), [Companies Act s248](https://www.legislation.gov.uk/ukpga/2006/46/section/248), [s355](https://www.legislation.gov.uk/ukpga/2006/46/section/355), [UK GDPR](https://www.legislation.gov.uk/eur/2016/679/contents). Statute access limitations are recorded in file 11.

Additional checked retention sources (2026-10-09): [PAYE](https://www.gov.uk/paye-for-employers/keeping-records), [VAT](https://www.gov.uk/charge-reclaim-record-vat/keeping-vat-records), [pensions](https://www.thepensionsregulator.gov.uk/en/document-library/automatic-enrolment-detailed-guidance/9-keeping-records), [minimum wage](https://www.gov.uk/hmrc-internal-manuals/national-minimum-wage-manual/nmwm12020), [right to work](https://www.gov.uk/government/publications/right-to-work-checklist/employers-right-to-work-checklist-accessible-version). Where one record serves several purposes, apply the relevant longest justified requirement, restrict access, and minimise unrelated personal information.

## Holds and deletion workflow

Receive legal hold → identify scoped records/custodians/systems → pause only relevant deletion → restrict access and record purpose → periodic counsel review → release hold with approval → resume schedule. For routine deletion, produce candidate inventory, check legal/contract holds, verify authorisation, delete through controlled jobs and record result without reproducing deleted content. Backup expiry must be documented; if restored, reapply deletion markers before normal use.

Tests: erasure request during a dispute does not result in indiscriminate deletion; existence of one dispute does not justify retaining all customer data forever. A UK-region host with overseas support triggers transfer assessment. Acceptance: country matrix, dispute clocks and retention/hold records are owned, evidenced and tested. Verified 2026-10-09.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
