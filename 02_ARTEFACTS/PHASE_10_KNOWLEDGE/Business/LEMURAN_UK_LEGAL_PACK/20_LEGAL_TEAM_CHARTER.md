---
id: LEMURAN-UK-20
title: "Lemuran Ltd Legal Team Charter"
document_type: "Department Specification"
owner: "Lemuran director — assignment pending"
status: Draft for human review
classification: Internal
version: 1.1.0
created: "2026-10-10"
updated: "2026-10-10"
legal_sources_verified_on: "2026-10-09"
jurisdiction: United Kingdom
legal_advice_status: AI-assisted legal operations; not a legal opinion
---

# Lemuran Ltd Legal Team Charter

## Mission, scope and status

Provide Lemuran Ltd with a company-wide legal and compliance operating function inside AIBOS: receive matters, maintain legal knowledge, prepare documents, review commitments, track deadlines, preserve evidence and coordinate authorised decisions. Cover the company itself, its internal operations, all services and client engagements, and every current and future product. FAQai.app is one known product; no other products, legal entities or operating capabilities are assumed.

This is the **operating specification for Lemuran’s AI-assisted legal team**. It is not yet an installed team, an appointment of a lawyer, or a transfer of directors’ accountability. The agent supports accountable people and qualified external advisers when required. The following organisation and workflows are proposed **POLICY**, not additional claims about UK law. Existing legal knowledge retains its 9 October 2026 verification date.

## Service catalogue

| Workstream | Scope and deliverables |
|---|---|
| Corporate and governance | Company records, board/shareholder decision packs, filing calendars, authority and ownership matters |
| Finance and tax coordination | Accountant workpapers, VAT/sales treatment questions, filing/payment review packages |
| Products | Legal readiness for each product, customer terms, notices, data/AI/IP/security assessments, lifecycle changes |
| Services and projects | Proposals, MSA/SOW/DPA/SLA reviews, subcontractor terms, changes, acceptance and handover |
| Internal operations | Staff/contractors, procurement, confidentiality, business assets, insurance, internal policies |
| Data, security and AI | Purpose-based assessments, rights/complaints, supplier/transfer records, incidents, release review |
| Disputes and official correspondence | Matter triage, evidence/holds, draft notices/responses, escalation and adviser coordination |
| Legal operations | Document/version control, obligations and renewals, source monitoring, reporting and records |

Non-AI services or products remain in company scope: apply the relevant general controls and record why AI-specific controls do not apply. Unfamiliar activities—such as premises, financing, acquisitions or a regulated service—are still accepted into the matter register, then assigned a tailored source-backed assessment. The current pack must not pretend to contain a complete specialist playbook for every future transaction.

## Team structure and authority

| Function | AI assistance | Accountable human |
|---|---|---|
| Legal operations lead | Intake, routing, registers, document assembly and progress reporting | Director or named legal operations owner |
| Corporate/commercial desk | Review packs, contract comparisons, obligation extraction | Authorised signatory; counsel for legal judgement as needed |
| Privacy/AI/security desk | Data maps, risk assessment drafts, evidence and incident preparation | Privacy/product/security owners, with specialist advice |
| People/IP/insurance desk | Status questions, rights records, policy/coverage comparisons | HR/director, counsel/accountant/broker as relevant |
| External adviser coordination | Prepare focused questions and supporting evidence | Human instructing the adviser and approving scope/cost |

Role labels describe capabilities; they do not assert actual staff appointments or professional qualifications. People can hold multiple roles with appropriate authority and conflict management. Keep the approval gates in file 14; drafting and internal preparation should proceed without unnecessary repeated permissions. External correspondence requires authorisation for its recipient, purpose and final content.

## Matter lifecycle

1. **Intake:** record the request, entity, affected scope, received time, documents, requested outcome, confidentiality and owner. A corporate matter need not name a product.
2. **Triage:** identify urgency, actual legal/contract deadlines, conflicts, missing facts and relevant specialist capabilities. Court/regulator documents and incidents receive immediate escalation.
3. **Assessment:** retrieve the relevant current sources and company evidence; classify law, contract and proposed policy separately. Record unresolved scope instead of fabricating a conclusion.
4. **Preparation:** draft the document/decision package, alternatives, risks, supporting evidence and execution requirements.
5. **Review/approval:** bind approval to exact version and intended action; involve the appropriate adviser for matters requiring specialist judgement.
6. **Authorised action:** sign/file/send/publish only within valid authority. Reconcile uncertain outcomes before retrying.
7. **Obligations:** extract duties, deadlines, renewal/termination windows, responsible owners and evidence requirements from the effective document.
8. **Closure/review:** retain final evidence, update relevant portfolio controls and apply the appropriate retention/hold schedule. Closed matters may retain ongoing obligations.

Suggested states: `new`, `triaged`, `awaiting_facts`, `in_assessment`, `drafting`, `in_review`, `approved_for_scoped_action`, `action_pending_verification`, `effective_or_completed`, `closed`. These are matter/document states; runtime run statuses remain those defined in file 14.

## Portfolio record

```json
{
  "scope_id": "product-faqai",
  "scope_type": "product",
  "display_name": "FAQai.app",
  "legal_entity_ref": "lemuran-ltd-record",
  "owner": null,
  "lifecycle": "unknown",
  "business_model": null,
  "customer_types": [],
  "countries": [],
  "data_map_ref": null,
  "supplier_refs": [],
  "applicable_control_refs": [],
  "document_refs": [],
  "approval_refs": [],
  "open_issues": ["Business-specific facts and readiness not verified"]
}
```

Create an independent record for each product/service and link individual engagements where needed. Company master data is referenced once; product differences belong in schedules. For a new product, assess customer type, territory, sector, data roles, technology, IP, billing, support and risk before deciding which templates apply. Company-wide source changes identify every affected scope and owner.

## Official legal document register and lifecycle

“Official” means controlled and issued through the appropriate company authority, not merely generated on company letterhead. Track drafts separately from approved, executed, filed, published, superseded and withdrawn records. Legal effectiveness depends on the relevant facts and formalities, not an internal status flag.

```json
{
  "document_id": "unique-document-id",
  "matter_id": "unique-matter-id",
  "document_type": "contract_or_resolution_or_notice_or_policy_or_filing_or_other",
  "entity_ref": "lemuran-ltd-record",
  "scope_refs": [],
  "counterparty_refs": [],
  "version": "0.1.0",
  "status": "draft",
  "template_ref": null,
  "content_hash": null,
  "prepared_by": null,
  "reviewer_refs": [],
  "approval_ref": null,
  "signatory_authority_ref": null,
  "issued_at": null,
  "effective_at": null,
  "execution_or_acceptance_evidence_ref": null,
  "supersedes": null,
  "obligation_refs": [],
  "retention_rule_ref": null,
  "legal_hold_refs": []
}
```

Before issue: verify entity/recipient facts, unresolved variables, authority, applicable formalities, final content and attachments. Afterwards: save accepted/executed evidence, identify obligations and preserve the approved version. A material edit requires renewed approval. Do not overwrite executed documents when revising a template; changes to existing obligations follow their lawful variation mechanism. Store confidential signed documents outside the general knowledge repository with controlled evidence links.

## Additional templates

### Company legal request

Requester; request date; company/entity; corporate/internal/product/service/engagement scope; affected IDs; issue and desired result; actual deadline and source; documents/counterparties; known facts; uncertainties; confidentiality; proposed owner; requested action versus draft only.

### Board or management decision pack

Decision requested; competent decision-maker under verified governing documents; background/facts; alternatives; financial/legal/data/security impacts; conflicts; adviser input; recommended conditions; draft resolution if appropriate; approval/execution requirements; follow-up filings/actions. Do not invent quorum, voting thresholds or directors’ names.

### Official correspondence review sheet

Matter/reference; verified recipient and channel; purpose; facts supported by evidence; draft body/attachments; admissions or commitments; applicable deadline; confidentiality/privilege review; approver and authority; exact final version; dispatch and receipt record.

## Acceptance and metrics

- A corporate filing, employment matter or supplier dispute routes without a product ID.
- A newly introduced product receives its own assessment and documents; FAQai.app is not the default legal scope.
- A non-AI service can use the general company function without irrelevant AI controls.
- Shared policy changes identify all affected products and engagements.
- Drafts cannot be silently classified as signed, filed or legally effective.
- Official documents have authority, version, scope, evidence and obligation records.
- All specialist gaps are accepted as matters and routed for further assessment, rather than falsely certified complete.

Measure open urgent matters, missed deadlines, unsupported commitments, expired approvals, unresolved fact gaps and obligations without owners. Track implementation, not the number of documents generated.

## References and dependencies

This charter is an internal operating design. It depends on [company facts](01_BUSINESS_FACTS_AND_APPLICABILITY.md), [operations/RACI](10_OPERATIONS_AND_REVIEW.md), [skill contract](14_SKILL_IMPLEMENTATION_SPEC.md), [catalogue](15_SKILL_CATALOGUE.md), [test specification](16_TESTS_AND_ACCEPTANCE.md) and [repository integration](17_REPOSITORY_INTEGRATION.md). Legal propositions are sourced in [the authority register](11_AUTHORITY_REGISTER.md).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.1.0 | 2026-10-10 | Company-wide Legal Team Charter, portfolio routing and official-document lifecycle. |
