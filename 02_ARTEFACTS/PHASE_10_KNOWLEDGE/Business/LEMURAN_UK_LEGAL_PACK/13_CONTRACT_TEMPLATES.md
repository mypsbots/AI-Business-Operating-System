---
id: LEMURAN-UK-13
title: "Contract drafting schedules and clause starters"
document_type: "Template Pack"
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

# Contract drafting schedules and clause starters

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## Status and usage

These are structured drafting templates for legal review, not execution-ready agreements. They intentionally leave negotiated variables unresolved. Do not simply remove the brackets and publish: check jurisdiction, customer status, authority, system capability and mandatory rights first. See [contracts knowledge](06_CONTRACTS_AND_CONSUMERS.md) and [source register](11_AUTHORITY_REGISTER.md).

## CT-01 — SaaS business terms / order form

**Parties:** Lemuran Ltd, company number [verified], registered office [verified], registered in [nation], and [customer legal entity/address]. Product: FAQai.app [plan/version]. Effective date [date]. Authorised signatories [names/roles].

| Schedule | Fill-in requirements |
|---|---|
| Subscription | Features, seats/tenants, usage limits, deployment, permitted users |
| Fees | Currency, tax treatment, usage overages, invoicing, payment, price changes |
| Term | Initial duration, renewal, notice, cancellation channel, trial conversion |
| Customer obligations | Content authority, lawful use, account security, dependencies |
| AI | Intended use, limits, prohibited sensitive uses, human escalation and tool powers |
| Data | DPA/roles, security schedule, subprocessor process, residency, export and deletion |
| IP | Lemuran platform/background rights, customer content licence, output qualifications |
| Support | Hours, severity definitions, response targets and any SLA |
| Risk | Warranties, exclusions, indemnities, caps, non-excludable liabilities, insurance |
| Exit | Suspension grounds/proportionality, cure, termination, refunds where due, transition |
| General | Confidentiality, notices, assignment, change mechanism, governing law/forum, precedence |

Clause starter — AI limitations: “The Service generates responses using [approved sources and model configuration]. Outputs may be incomplete or incorrect. The Customer should apply review appropriate to [intended use]. [Human escalation route]. Nothing in this provision limits liability or rights that cannot lawfully be limited.” Reviewer must align wording with actual capability and avoid implying this removes Lemuran's legal duties.

Clause starter — customer content: “The Customer grants Lemuran the rights necessary to process Customer Content to provide [defined services] during [defined period], subject to the Data Processing Schedule. Any additional use for model training or another independent purpose requires [separate defined lawful arrangement].” Do not insert a hidden training licence under a broad service clause.

## CT-02 — Master services agreement

1. Definitions, contract formation and order-of-precedence rule.
2. SOW commissioning, scope/dependencies and change control.
3. Delivery standard, personnel/subcontractors and customer cooperation.
4. Milestones, acceptance, defects and remedy procedure.
5. Fees, expenses, taxes, invoice disputes and payment/suspension.
6. Background IP, new deliverables, third-party materials and licence/assignment timing.
7. Confidentiality with lawful reporting carve-outs.
8. Data roles, security, authorised access, subprocessors and incident cooperation.
9. Warranties, indemnities, liability allocation and insurance.
10. Termination, transition, account ownership, data/source handover and survival.
11. Dispute escalation, ADR, notices, governing law/forum and execution formalities.

Suggested precedence for review: mandatory transfer clauses govern their subject matter; DPA controls data issues; SOW controls expressly negotiated project details; MSA governs remaining terms. Identify actual conflicts instead of relying on an all-purpose precedence sentence.

## CT-03 — Statement of work

- SOW ID / MSA version / customer / project owner:
- Business problem and defined intended use:
- Deliverables (versioned list) and explicit exclusions:
- Milestones/dates/customer prerequisites and delay handling:
- Environments, accounts and access permissions:
- Acceptance tests with objective expected outcomes and defect process:
- Price, tax, milestones, expenses and change rates:
- Data categories/roles/vendors/transfers and security requirements:
- IP deliverables/background licences/third-party dependencies:
- AI limitations, evaluations, agent powers and human approval points:
- Handover, documentation, training, warranty and ongoing support:
- Named approvers and signed change-control process:

Clause starter — change control: “A proposed scope change will describe its effect on fees, dates, acceptance criteria and data/security obligations. It becomes part of this SOW only when approved by [authorised roles] through [agreed method].” Define emergency handling and avoid proceeding on an informal message from an unauthorised user.

## CT-04 — Data processing agreement / schedule

Use where Lemuran processes personal data on the customer's behalf, and adapt in the reverse direction when Lemuran appoints processors. Article 28 particulars: subject matter/duration; nature/purpose; data types/data subjects; controller rights and duties. Required terms cover documented instructions (including transfers), confidentiality, appropriate security, subprocessor authorisation and equivalent protection, rights assistance, assistance with security/breaches/DPIAs/consultation, end-of-service return/deletion subject to legal retention, compliance information/audits and warning of unlawful instructions. [ICO contract requirements](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/).

Schedules to complete:

| Annex | Content |
|---|---|
| A Processing | Every purpose, person/data category, operation, frequency and duration |
| B Security | Actual controls, access, isolation, encryption, backup, testing and evidence |
| C Subprocessors | Legal entity, function, location/access, notice/objection procedure |
| D Transfers | Exporter/importer, mechanism, completed IDTA/Addendum where needed, assessment |
| E Exit | Return format, deletion timeline, backups, holds and certification process |
| F Assistance | Contact channels, escalation, cooperation, reasonable commercial arrangements that do not defeat duties |

Do not substitute an NDA for a DPA. Do not rewrite mandatory IDTA/Addendum clauses beyond permitted changes. Do not give a processor 72 hours to notify its controller as though that were the statutory default.

## CT-05 — SLA / support schedule

Service [scope]; measurement point [external/end-to-end]; measurement period [month]; eligible minutes [definition]; unavailable minutes [definition]; availability formula `(eligible_minutes - unavailable_minutes) / eligible_minutes * 100`; approved exclusions [specific and proportionate]; planned maintenance [notice and cap]; support hours/timezone; severity examples; response versus restoration targets; customer dependencies; escalation; claim evidence/window; credits [amount/cap]; chronic failure remedy; relationship to other remedies.

**Example only, not a promise:** if 43,200 eligible minutes contain 60 unavailable minutes, availability is approximately 99.8611%. Verify monitoring can actually measure the agreed metric. Do not exclude all model-provider failures while advertising end-to-end availability without clearly explaining the scope.

## CT-06 — Consumer addendum worksheet

Confirm service/digital-content classification; mandatory pre-contract information; full price; trial/renewal disclosures; fair terms; durable confirmation; cancellation instructions/form; early-performance request if applicable; digital-content consent/acknowledgement if applicable; statutory remedies; accessible cancellation/refund flow; complaints and ADR disclosures where required. No blanket waiver or “all sales final” term.

## CT-07 — NDA, IP and contractor schedule

Define confidential information, permitted purpose, authorised recipients, security, legal-disclosure exceptions, return/deletion and duration. Include protected-disclosure carve-outs. List pre-existing assets and new deliverables; use appropriately drafted signed assignments or licences; address moral rights where relevant and legally possible; preserve third-party rights. Record open-source/model licence obligations and any customer approval needed. Employment/tax status must be analysed separately from IP wording.

## Contract review checklist

- [ ] Complete party/authority evidence and chosen jurisdiction.
- [ ] No unresolved bracket, invented promise or unknown fee.
- [ ] B2B/B2C and processor/controller distinctions resolved.
- [ ] Liability and indemnity terms approved against risk/insurance.
- [ ] SOW/SLA/DPA and supplier capability consistent.
- [ ] Acceptance/signature version captured; final changes reapproved.
- [ ] Obligations added to operations calendar with evidence owners.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
