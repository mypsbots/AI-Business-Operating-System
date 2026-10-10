---
id: LEMURAN-UK-18
title: "LLM handoff prompt for skill generation"
document_type: "Prompt"
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

# LLM handoff prompt for skill generation

## Copyable implementation brief

You are implementing Lemuran Ltd’s company-wide AI-assisted Legal and Compliance team within the existing AIBOS repository. Cover corporate governance and internal affairs, every service engagement, and all current and future products. FAQai.app is one product example only. Start with `20_LEGAL_TEAM_CHARTER.md`: implement central matter intake, portfolio applicability, official-document control and the domain capabilities. Do not hard-code FAQai.app as the only product or route all company work through a SaaS workflow.

First inspect repository instructions, actual tree, manifests/loaders, root specification, phase schema, existing legal/privacy/finance/security roles, working-tree status and CI. Use the inspection report in `17_REPOSITORY_INTEGRATION.md` as prior evidence, not proof of the current Git state. Preserve existing skills. Do not overwrite one without explicit approval of the exact change.

Read `00_START_HERE.md`, `01_BUSINESS_FACTS_AND_APPLICABILITY.md`, `14_SKILL_IMPLEMENTATION_SPEC.md` and `15_SKILL_CATALOGUE.md`. Load only the domain references required for each capability. Use `11_AUTHORITY_REGISTER.md` to distinguish opened/checked primary sources from legal anchors that remain unverified. Recheck decisive legal sources and commencement at execution time. Do not convert policy proposals or best practice into legal duties.

Create safe additive drafts in an unused namespace. Implement all enabled catalogue entries with triggers, typed inputs/outputs, sources, ownership, approval gates, guardrails, review triggers and scenario tests. Inherit the shared execution contract without duplicating large legal passages. If generating AIBOS role handbooks, follow the existing role schema. If runtime adapters are supported, use the runtime's required `SKILL.md` format and maintain clear links back to AIBOS references.

Do not invent company number, tax/ICO status, business establishment, suppliers, customers, data locations, product functions, insurance or signing authority. Record unknowns explicitly and continue independent drafting. Ask only for facts genuinely needed for a dependent decision and not obtainable from connected authorised sources.

Build mock tests from `16_TESTS_AND_ACCEPTANCE.md`; test legal classification, missing facts, source staleness, approval scope/version binding, idempotency and injection resistance. Keep customer/employee data and credentials out of Git/test fixtures. Do not send messages, sign documents, file returns, pay fees, publish live policies or change production processing merely to demonstrate the skill.

Deliver the exact additive diff, new IDs/files, validation evidence, remaining fact/legal reviews and rollback instructions. Clearly distinguish implemented behaviour from specifications and tests that have not been run. If writable repository access is unavailable, produce the draft pack and precise integration proposal without pretending to have installed it.

## Expected generation output

1. Repository inspection and compatibility findings.
2. Coverage matrix mapping all 25 capabilities to created artefacts and collaborating existing roles.
3. Additive knowledge/rules/checklists/playbooks/templates/runtime adapters as appropriate.
4. Test fixtures and actual results.
5. Human review package for remaining operational decisions.
6. No overwritten skills, unapproved external actions or unsupported compliance claims.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
