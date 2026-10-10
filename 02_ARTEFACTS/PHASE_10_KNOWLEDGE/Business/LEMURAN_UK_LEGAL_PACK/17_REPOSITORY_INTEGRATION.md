---
id: LEMURAN-UK-17
title: "AIBOS inspection and safe additive integration proposal"
document_type: "Integration Proposal"
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

# AIBOS inspection and safe additive integration proposal

## Inspection evidence — 2026-10-09

The connected AIBOS service returned the 20 phases, including skills (05), rules (06), checklists (07), playbooks (08), templates (09), knowledge (10) and automation/improvement (12). The following full documents were read:

| Observed path | Finding |
|---|---|
| `00_ROOT/AIBOS_ROOT_SPECIFICATION.md` | Enterprise v2.0; YAML metadata, semantic versions, uppercase snake-case Markdown names; common document sections |
| `01_PHASES/PHASE_05_SKILLS_MASTER_PROMPT.md` | Role-handbook generation; extensive role schema; one role document at a time |
| `02_ARTEFACTS/PHASE_05_SKILLS/44_LEGAL_COUNSEL_SKILL.md` | Existing `SKILL-000044`, version 2.0.0, 2026-06-26; AI-assisted drafting/review with human judgement |
| `02_ARTEFACTS/PHASE_06_RULES/Business/06_LEGAL_RULE.md` | Existing `RULE-000046`; review/approval before signing; IP and regulatory compliance |
| `02_ARTEFACTS/PHASE_10_KNOWLEDGE/Business/06_LEGAL_KNOWLEDGE_ARTICLE.md` | Existing `KN-000006`; general legal background, not UK-specific procedures |

Search also returned Legal department specifications, a Legal Checklist, and business playbooks/templates. They were discovered, not all read in full. The root recommends a generic layout differing from the observed `02_ARTEFACTS` paths; preserve actual conventions and resolve this with repository maintainers rather than reorganising the repo.

The generated local workspace contained no AIBOS checkout. Listed projects did not identify one. GitHub's accessible-repository listing returned an empty list. Public name search returned unrelated Aibo repositories and was not used as proof of repository identity. The AIBOS connector offered search/read capabilities, not file mutation. Its index did not expose a commit SHA or prove freshness against the default branch. Therefore this deliverable is an **additive proposal only**; no commit, branch, pull request, installation or existing-skill modification occurred.

## Company-wide revision — 2026-10-10

The delivered pack is now version 1.1.0 and defines Lemuran Ltd’s company-wide legal function. Add the Legal Team Charter and three capabilities for matter intake, portfolio onboarding and official-document control. Retain FAQai.app as an example within an open-ended portfolio. No new repository access or live installation is claimed by this revision; the inspection above remains the 9 October snapshot.

## Proposed first addition

After confirming the target repository, reserve an unused namespace, for example:

```text
02_ARTEFACTS/PHASE_10_KNOWLEDGE/Business/LEMURAN_UK_LEGAL_PACK/
  00_START_HERE.md
  ...all Markdown files in this delivered pack...
```

This preserves relative links and keeps the pack self-contained. The path is proposed, not confirmed to be absent. On collision, use a reviewed versioned namespace or stop; never overwrite an existing skill or silently merge unrelated content. Namespace IDs start `LEMURAN-UK-`; check repo-wide uniqueness before import.

## Subsequent phase mapping

| Pack content | Proposed AIBOS phase use | Existing assets to retain |
|---|---|---|
| Files 01–11 | Phase 10 UK-specific references | Existing legal knowledge |
| File 15 capabilities + file 14 execution contract | Phase 05 extension to existing roles or runtime adapters | `44_LEGAL_COUNSEL_SKILL.md` and collaborating roles |
| Common guardrails / approval registry | Phase 06 supplemental UK rules | Existing Legal Rule; no weakening |
| File 12 checklists | Phase 07 dedicated launch/onboarding checks | Existing Legal Checklist |
| Files 09–10 workflows | Phase 08 playbooks | Existing customer/project workflows |
| Files 12–13 forms | Phase 09 templates | Existing business templates |
| Source monitoring | Phase 12 automation specification | Existing scheduler/tools; no live scheduling from this pack |
| File 16 fixtures | Existing test system, path to discover | Preserve all existing tests/CI |

Do not duplicate the full legal knowledge into every role document. Link to controlled references. If formal Phase 05 role handbooks are generated, satisfy the repository's existing master-prompt schema (mission, services, RACI, decision authority, dependencies, KPIs, acceptance and other required fields). A compact runtime `SKILL.md` adapter should not be falsely presented as a complete AIBOS role handbook.

## Integration procedure

1. Confirm owner/repo/local path, default branch and current commit. Read `AGENTS.md`, root/index, contribution rules, manifests, schemas and existing loaders/CI. Inspect working-tree status and existing legal/privacy/finance/security roles. Do not guess a branch or remote from a public search.
2. Inventory candidate destinations and document IDs. Capture checksums of existing skill files before work. If a related skill exists, propose references/extensions; obtain approval before changing its contents as requested by the user.
3. Create a suitable isolated branch/worktree only under repository conventions. Add the pack to an unused directory using exclusive-create semantics. No replacements, deletions, dependency changes or CI modifications in the initial addition.
4. Validate frontmatter, relative links, IDs, JSON catalogue and source registry. Run actual repository checks; do not claim they passed if unavailable. Secret-scan draft content before upload.
5. Add a new standalone manifest/index inside the new directory. Changes to an existing catalogue are separate reviewed diffs; never assume its parser accepts arbitrary fields or automatically discovers nested documents.
6. Present exact add-only diff, files, tests, unresolved legal reviews and rollback. If a PR is created, keep it reviewable and attach its URL to the chat. Do not merge solely because the pack was generated.
7. Roll back by removing only the introduced files via a reviewed revert; preserve any operational evidence or signed agreements created later. Do not reset the entire repo.

## Candidate runtime adapter (example, not installed)

```yaml
---
name: uk-vat-sales-classification
description: Assess VAT registration and sales/imported-service treatment when turnover, contracts or countries change.
metadata:
  aibos_id: LEMURAN-UK-VAT
  version: 1.0.0
  status: draft
  knowledge_ref: path-resolved-at-integration/03_TAX_AND_VAT.md
---
```

Body should load the resolved tax reference and shared execution contract, validate required inputs from catalogue entry, prepare a sourced assessment and accountant review package, and follow G1 before a filing/payment. Preserve automatic skill discovery unless the actual runtime/user requests otherwise; discovery does not authorise external action. Use lowercase folder names only for runtime adapters, while keeping AIBOS reference filenames uppercase snake case.

## Suggested review description

“Adds a UK/Lemuran legal knowledge and implementation pack covering FAQai.app and agency operations. Includes dated primary-authority references, applicability decisions, templates, 25 skill capability specifications and test fixtures. Existing legal skills are preserved. Company-specific facts and legal review remain necessary before operational use. Packaging validation is separate from runtime/CI/legal approval.”

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
