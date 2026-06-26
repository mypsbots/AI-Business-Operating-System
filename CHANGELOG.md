# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.5.0] - 2026-06-26

### Changed

- **Framework phases (01–04, 11–12, 14–20) are now detailed, ready-to-use
  documents** instead of single-line placeholders. The shared generator's
  section builder was replaced with keyword-aware logic that emits
  section-appropriate content (bullets, tables, code blocks) for ~70 common
  section types — requirements, architecture, data flow, deployment, security,
  authn/authz, versioning, rollback, governance, agent authority/approval,
  collaboration, certification/assessment, maturity and more.
- Eliminated all 2,936 generic placeholder sections across 467 documents
  (now 0 remaining).

### Fixed

- The shared generator (`tools/generate_aibos.py`) no longer regenerates Phases
  05–10 and 13, so the hand-curated content produced by the dedicated generators
  is never overwritten.

### Verified

- `markdownlint-cli2` across all 1,231 artefact files: 0 errors.
- Internal link check across 22,845 links: 0 broken.

## [2.4.0] - 2026-06-26

### Changed

- **Phases 06–10 are now complete, ready-to-use documents** rather than scaffolds,
  generated from real topic-specific content libraries:
  - Phase 06 Rules (47): RFC-2119 MUST/SHOULD/MAY, ownership matrix, compliance
    mapping, metrics, anti-patterns and validation checklists.
  - Phase 07 Checklists (45): binary, auditable items plus cross-cutting security,
    privacy, AI, accessibility, performance and deployment validation.
  - Phase 08 Playbooks (36): triggers, roles, step-by-step procedures, Mermaid
    diagrams, decision branches, integrations, KPIs/SLAs and continuous improvement.
  - Phase 09 Templates (35): real, copy-paste fill-in skeletons with placeholder
    definitions, naming/folder conventions, schemas and AI-usage guidance.
  - Phase 10 Knowledge (59): atomic, RAG-optimised explainers with core concepts,
    definitions, examples, FAQs, a decision guide, a knowledge-graph block and
    retrieval metadata.

### Added

- `tools/content_kb.py`: shared topic content library powering Rules, Checklists
  and Playbooks.
- `tools/templates_kb.py` and `tools/knowledge_kb.py`: content libraries for
  Templates and Knowledge.
- `tools/generate_rules.py`, `generate_checklists.py`, `generate_playbooks.py`,
  `generate_templates.py`, `generate_knowledge.py`: per-phase generators.

All generated files are lint-clean and every internal link resolves.

## [2.3.0] - 2026-06-26

### Changed

- **Phase 05 Skills are now complete, ready-to-use reference documents** rather
  than scaffolds. Each of the 48 role documents now contains role-specific
  content: a plain-language "At a Glance" summary, a "How to Use This Document"
  guide, real technical/business/AI/soft skills, concrete tools, certifications,
  a staged learning path, KPIs, deliverables, career progression and tailored
  interview questions.

### Added

- `tools/skills_kb.py`: a curated knowledge base of real, role-specific content
  for all 48 skill roles.
- `tools/generate_skills.py`: generator that renders the knowledge base into
  complete, cross-linked, lint-clean skill documents.

## [2.2.0] - 2026-06-26

### Changed

- Generator now emits **working relative Markdown links** (e.g. `../../ROOT_INDEX.md`)
  computed from each document's location, replacing bare inline references that did
  not resolve from nested folders.
- Cross-reference sections (Required Rules, Checklists, Playbooks, etc.) now link to
  the correct phase artefacts folder instead of repeating identical boilerplate.
- Skill sub-competency sections (Technical, Business, AI, Soft) now carry distinct,
  role-appropriate content instead of duplicated text.

### Added

- A navigation breadcrumb (Home · Catalogue · Generated Index · Phase Prompt) at the
  top of every generated artefact.
- A browsable `README.md` index in every artefacts folder (163 indexes) so the
  repository is easy to surf directly on GitHub.

## [2.1.0] - 2026-06-26

### Added

- `tools/generate_aibos.py`: deterministic, idempotent generator that produces
  schema-compliant Markdown artefacts from the Phase master prompts.
- `02_ARTEFACTS/`: 1067 generated artefacts across all 20 phases, each with YAML
  front matter, the sections required by its phase, and cross-references to the
  inherited root standards.
- `02_ARTEFACTS/GENERATION_INDEX.md`: catalogue of generated artefacts with
  per-phase counts and regeneration instructions.

### Notes

- All generated artefacts pass Markdown validation and start at Draft status for
  subject-matter and AI-assisted enrichment.

## [2.0.0] - 2026-06-26

### Added

- Constitutional `AIBOS_ROOT_SPECIFICATION.md` and 16 enterprise standards and
  master prompts under `00_ROOT/`.
- Twenty sequential phase master prompts (`PHASE_01` … `PHASE_20`) under
  `01_PHASES/`.
- Repository completion artefacts: `ROOT_INDEX.md`, `README.md` and
  `FINAL_REPORT.md`.
- GitHub governance and automation: `LICENSE` (MIT), `CONTRIBUTING.md`,
  `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue and pull request templates, and a
  Markdown validation CI workflow.
- Repository hygiene configuration: `.gitignore`, `.gitattributes`,
  `.editorconfig` and `.markdownlint.json`.

### Notes

- Canonical `UPPER_SNAKE_CASE` filenames were preserved to maintain
  cross-reference integrity across all documents.

[2.1.0]: https://github.com/mypsbots/AI-Business-Operating-System/releases/tag/v2.1.0
[2.0.0]: https://github.com/mypsbots/AI-Business-Operating-System/releases/tag/v2.0.0
