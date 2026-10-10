---
id: LEMURAN-UK-00
title: "Lemuran UK legal and compliance knowledge pack"
document_type: "Guide"
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

# Lemuran UK legal and compliance knowledge pack

## Purpose and scope

This pack defines the **company-wide AI-assisted Legal and Compliance function of Lemuran Ltd, United Kingdom**. It covers corporate affairs, internal operations, all service engagements, and all current and future products. **FAQai.app is one product in that portfolio**, not the boundary of the legal function. These names and relationships are user-supplied; incorporation, ownership, product behaviour and compliance status have not been independently established. The pack is suitable for LLM retrieval and implementation planning. It does not certify compliance or supply signature-ready legal advice.

**Research verification date: 9 October 2026 (Europe/London).** Source access is documented in [the authority register](11_AUTHORITY_REGISTER.md). Some legislation pages could not be fetched; these are marked separately. Verification means the cited guidance was consulted, not that a solicitor reviewed the pack or every commencement instrument was checked.

## Reading and ingestion order

1. Read the [Legal Team Charter and company-wide operating model](20_LEGAL_TEAM_CHARTER.md), then [Business facts and applicability](01_BUSINESS_FACTS_AND_APPLICABILITY.md): complete the facts before generating company-specific conclusions.
2. Knowledge: [company](02_COMPANY_GOVERNANCE.md), [tax](03_TAX_AND_VAT.md), [privacy](04_PRIVACY_AND_TRANSFERS.md), [marketing](05_PECR_AND_MARKETING.md), [contracts/consumer law](06_CONTRACTS_AND_CONSUMERS.md), [IP/AI](07_IP_AND_AI_GOVERNANCE.md), [security/people/insurance](08_SECURITY_PEOPLE_AND_INSURANCE.md), [international/disputes/retention](09_INTERNATIONAL_DISPUTES_AND_RECORDS.md).
3. [Operations and review](10_OPERATIONS_AND_REVIEW.md) and [primary authorities](11_AUTHORITY_REGISTER.md).
4. [Templates](12_OPERATIONAL_TEMPLATES.md) and [contract drafting schedules](13_CONTRACT_TEMPLATES.md).
5. [Skill implementation contract](14_SKILL_IMPLEMENTATION_SPEC.md), [machine-readable skill catalogue](15_SKILL_CATALOGUE.md), [acceptance tests](16_TESTS_AND_ACCEPTANCE.md), [AIBOS integration proposal](17_REPOSITORY_INTEGRATION.md), and [LLM handoff prompt](18_LLM_HANDOFF_PROMPT.md).

## Obligation labels used throughout

| Label | Meaning | Can management waive it? |
|---|---|---|
| LAW | Binding legal duty where the stated scope applies | No; a lawful exemption requires evidence |
| CONDITIONAL LAW | Binding only after a factual/legal trigger is established | No once applicable; unknown is not exempt |
| CONTRACT | Obligation arising from an executed agreement | Only through lawful agreed variation or an existing contractual mechanism |
| GUIDANCE | Regulator/government interpretation; underlying legislation remains controlling | Departures need reasoned analysis, not casual dismissal |
| POLICY | Proposed Lemuran operating rule; not yet adopted | An authorised, recorded exception may be possible |
| PRACTICE | Recommended risk-management measure | Yes, with proportionality and evidence |
| WATCH | Announced, proposed or future change; commencement must be checked | Do not describe as currently binding |

“MUST” in a generated skill must always carry one of these labels. ISO 27001, ISO 42001, SOC 2, Cyber Essentials and NIST AI RMF are not universal UK statutory obligations. A contract or tender can require them. No certification is claimed here.

## Boundaries and status

- Drafting, research, local checks and recommendations can run automatically within authorised scope. Signing, filing, payments, external notices, production legal-policy publication and material risk acceptance require the appropriate human decision at the execution boundary.
- Human gates must not stall urgent statutory action: designate a director and deputy, deadline alerts and emergency escalation. A queued approval never extends a legal deadline.
- Company numbers, addresses, tax references, registered IP, employee details, renewal dates, insurance coverage and vendor promises must not be invented.
- Use England and Wales only as a provisional contract-law drafting assumption. Confirm incorporation jurisdiction, customer location and dispute forum; Scotland and Northern Ireland differ in material respects.
- Templates are review worksheets and clause starters. Commercial terms such as liability caps and uptime targets remain unfilled until approved.

## Repository outcome

The connected AIBOS read service exposed its 20-phase structure, root specification, Phase 05 generator, Legal Counsel skill, Legal Rule and Legal Knowledge article. The GitHub accessible-repository list was empty; no writable AIBOS checkout was identified. **No repository files were changed.** The additive integration proposal is grounded in the documents actually read; it is not a claim to have inspected a complete current Git tree or repository CI.

## Validation report

[File 19](19_VALIDATION_REPORT.md) records the checks performed and their limits. The ZIP contains all 21 Markdown files together, preserving relative links.

## Completion criteria

The pack is complete when files, links and embedded JSON pass the packaging checks. Business implementation is complete only after facts are resolved, owners approve the relevant controls, runtime tests pass, and evidence supports each applicable obligation. Start with the first 30-day plan in file 10.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
