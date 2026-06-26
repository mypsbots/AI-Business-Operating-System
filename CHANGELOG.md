# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
