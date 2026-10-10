---
id: LEMURAN-UK-12
title: "Operational templates and launch checklists"
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

# Operational templates and launch checklists

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## How to use

Copy only the needed template into the approved evidence system. Replace bracketed fields with verified facts; leave unknown values explicitly null. These templates are proposed internal controls, not completed records. Classify and restrict personal/confidential data. Relevant legal authorities are in files 02–11.

## TPL-01 — Business and obligation record

```yaml
record_id: "[unique-id]"
entity: Lemuran Ltd
company_number: null
service_line: "[FAQai.app|agency|corporate]"
activity: "[precise event]"
territory: "[country and UK nation]"
customer_capacity: unknown
obligation_class: "[LAW|CONDITIONAL_LAW|CONTRACT|POLICY|PRACTICE|WATCH]"
source_ids: []
source_provision: null
applicability: unknown
applicability_reason: null
facts_evidence: []
trigger_at: null
due_at: null
deadline_rule: null
timezone: Europe/London
owner: null
deputy: null
status: needs_facts
approval_ref: null
evidence_refs: []
verified_on: null
next_review_trigger: null
```

## TPL-02 — Processing inventory / ROPA worksheet

| Activity ID | Purpose | Data subjects/categories | Role and parties | Article 6 basis / Article 9 or 10 condition | Recipients/locations | Transfer mechanism | Retention trigger/period | Security | Notice/DPA | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| [ID] | [purpose] | [minimum necessary data] | [actual role] | [basis and evidence] | [including support] | [ref] | [justification] | [controls] | [version] | [name] |

Keep controller and processor record requirements separately mapped. For indirect collection, record source and transparency timing. For training, analytics and profiling, identify each additional purpose instead of hiding it under “service delivery”.

## TPL-03 — DPIA and AI risk assessment

- Project, owner, date, version and proposed launch:
- Intended purpose, necessity, alternatives and affected people:
- Data flow, roles, sources, locations and retention:
- DPIA trigger assessment and legal basis/conditions:
- Significant automated decision, meaningful human involvement and challenge route:
- Risks to people (not only business): severity, likelihood and evidence:
- Fairness, accessibility, children/vulnerability and discrimination considerations:
- Mitigations, test results, residual risk and responsible owner:
- Consultation with affected stakeholders/DPO and unresolved disagreements:
- Whether ICO prior consultation is required; evidence and status:
- Release decision, approver, conditions and reassessment triggers:

## TPL-04 — Supplier and transfer assessment

Supplier legal entity; service; controller/processor role; data categories; regions and remote support; subprocessors; retention/training configuration; security evidence; incident notice; deletion/return capability; DPA version; contract conflicts; transfer test; adequacy or safeguard; TRA/data protection test where needed; DPF entity/UK Extension evidence if used; exit plan; reviewer and review date.

Outcome: approve / approve with conditions / unresolved / reject for this use. Record restrictions by data/use case; approval for public documentation is not approval for employee health records.

## TPL-05 — Incident assessment and notification draft

Incident ID, reporter, occurrence/detection/awareness times (with timezone), affected systems/tenants, data/confidentiality/integrity/availability impact, known versus unconfirmed facts, containment already authorised, preserved evidence, controller/processor role, customer contract clocks, risk to individuals, ICO decision and reasons, individual-notice decision and reasons, notification deadline, approver/deputy, insurer/regulator/customer recipients, phased-update plan and recovery tests.

Draft notice structure: what happened and when; affected data/people to current knowledge; likely consequences; containment and mitigation; steps recipients can take; contact; uncertainties and next update. Do not invent counts or claim containment before evidence. Do not send from this template without appropriate authority.

## TPL-06 — Rights request and complaint record

Received at; request channel; requester/agent; safe identity verification; actual rights invoked; separate complaint flag; controller/processor owner; original deadline; lawful adjustment and reason; systems searched; reasonable/proportionate search record; third-party redactions/exemptions; response draft; approval; delivery evidence; escalation and closure. Complaint acknowledgement due date must remain distinct from SAR response due date.

## TPL-07 — Marketing and cookie decision log

Campaign/page; audience/subscriber class; channel; data source; lawful basis; PECR consent/soft-opt-in/exception evidence; notice version; suppression/TPS/CTPS check as appropriate; tags/purpose/recipient; exception conditions; free objection/withdrawal path; network test result; reviewer; authorised audience/message; expiry/recheck trigger.

## TPL-08 — AI system/model card

System ID; service line; intended/prohibited uses; model/provider/version; data sources; IP/licences; personal-data roles; known limitations; tool permissions; human approval boundaries; groundedness/error/abstention and fairness metrics; adversarial/tenant-isolation tests; operational thresholds; user disclosure; complaints/escalation; rollback; risk owner; release decision and expiry.

## TPL-09 — Retention and legal hold

| Record class | Purpose | Legal/contract basis | Start event | Duration and justification | Systems/backups | Hold status | Delete method | Owner/reviewer | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| [class] | [purpose] | [source] | [event] | [no invented period] | [list] | [hold ID or clear] | [method] | [names] | [result] |

Hold record: matter ID, scope, custodians, systems, issued by, issued at, review date, release authorisation. Never place full dispute evidence in a public repository.

## TPL-10 — Approval / deviation record

Decision ID; exact artefact version/hash; proposed external action; facts/source snapshot; risks and alternatives; approver identity and role; authority evidence; approved scope; conditions; expiry; counterparty approval if required; execution receipt. A changed artefact or scope invalidates its approval. Legal duties cannot be waived through this form.

## TPL-11 — Launch checklist

- [ ] Entity/customer/territory facts completed; exceptions triaged.
- [ ] Terms and order accepted; consumer flows validated if applicable.
- [ ] Privacy notice, DPA, vendor/transfer evidence reflect actual processing.
- [ ] Cookies/marketing permissions tested, not merely documented.
- [ ] Security/AI evaluation, human intervention and incident routing tested.
- [ ] IP chain, licence notices and customer-content rights resolved.
- [ ] Tax treatment, invoices, cancellation and refunds configured correctly.
- [ ] Support/SLA/insurance promises verified.
- [ ] Retention/export/deletion and offboarding demonstrated.
- [ ] Accountable owner signs the exact release scope and residual risks.

## TPL-12 — Agency project acceptance / change order

Project/SOW version; deliverable; test and expected result; observed evidence; defects by severity; acceptance/rejection and reasons; authorised customer decision; warranty/support start; unresolved dependencies. Change order: requested change, reason, added/removed scope, price/VAT, dates, acceptance changes, IP/data/security impacts and both parties' required approvals.

## TPL-13 — Monthly compliance review

Reporting period; open legal deadlines; overdue/unknown issues; source changes; VAT forecast; complaints/rights/incidents; vendor/model changes; expiring contracts/insurance; control failures; actions with owner/date; director decisions. Report facts and evidence, not a generic “all compliant” badge.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
