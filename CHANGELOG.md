# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.12.0] - 2026-10-07

### Added

- **Partnership Documentation skill set (Phase 05, 13 generate-ready UK documents).**
  New
  [`02_ARTEFACTS/PHASE_05_SKILLS/Partnership_Documentation/`](02_ARTEFACTS/PHASE_05_SKILLS/Partnership_Documentation/README.md)
  turns AIBOS into a UK (England & Wales) generator for company-to-company partnership
  documents. Each skill embeds a full blueprint, required inputs, UK legal/compliance
  notes (competition law, "no legal partnership"/agency, IP, data sharing, anti-bribery,
  commercial-agents) and a standing solicitor-review legal notice, so referencing the
  skill produces the actual document. Covers the Core (formation) pack — Letter of Intent
  (Heads of Terms), Memorandum of Understanding, Strategic Partnership/Alliance Agreement,
  Teaming Agreement, Partnership Statement of Work — and the Extended pack —
  Reseller/Channel Partner Agreement, Referral/Introducer Agreement, Revenue Share and
  Commission Schedule, Co-Marketing and Co-Branding Agreement, Joint Venture Agreement,
  Partnership Data Sharing Agreement, Partnership Governance/Joint Steering Committee
  Terms of Reference, Partnership Exit/Disengagement Deed — plus a
  [UK Partnership Framework](02_ARTEFACTS/PHASE_05_SKILLS/Partnership_Documentation/00_UK_PARTNERSHIP_FRAMEWORK.md)
  reference (lifecycle, binding vs non-binding, competition-law health check, IP,
  revenue/tax, data sharing, governance, exit, CMA/ICO/GOV.UK references). It
  cross-references, rather than duplicates, the Business Documentation Mutual NDA, DPA and
  Data Sharing Agreement skills.
- **`tools/generate_partnership_docs.py`** — deterministic generator for the set
  (overwrites only the `Partnership_Documentation/` folder). Linked from the Phase 05
  index and generation index; picked up automatically by the MCP corpus and Pinecone
  reindex workflow.

## [2.11.0] - 2026-09-27

### Added

- **Per-agent bearer tokens for the MCP server.** The HTTP transport now accepts
  multiple labelled tokens via the new `AIBOS_MCP_TOKENS` env
  (`label:token,label:token`), so each client/agent (e.g. `hermes`, `cursor`) gets
  its own credential. The matched label is logged on every request (audit) and a
  single agent can be revoked by removing its entry and redeploying — without
  affecting the others. The single `AIBOS_MCP_TOKEN` remains supported (label
  `primary`) for backward compatibility. Documented in `mcp/.env.example`.

### Security

- Auth comparison now uses constant-time matching (`hmac.compare_digest`) across all
  configured tokens, and unauthorised attempts are logged. Rotate any previously
  shared `AIBOS_MCP_TOKEN` and issue per-agent tokens instead.

## [2.10.0] - 2026-07-30

### Added

- **Business Documentation skill set (Phase 05, 27 generate-ready UK documents).**
  New
  [`02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/`](02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/README.md)
  turns AIBOS into a UK (England & Wales) business-document generator for AI,
  automation, software, SaaS, consulting and implementation engagements. Each skill
  embeds a full document blueprint, required inputs, UK legal/compliance notes and a
  standing solicitor-review legal notice, so referencing the skill produces the
  actual document. Covers the essential pack (Mutual NDA, Proposal, Quotation, MSA,
  SOW, DPA, Change Request, Acceptance Certificate, Invoice) and the extended pack
  (SLA, Security Schedule, AI & Responsible Use Schedule, Requirements Specification,
  Project Plan, Risk Register, Data Mapping Questionnaire, Sub-processor List,
  Customer Due-Diligence Checklist, Project Closure Report, Support & Maintenance,
  Subcontractor, Independent Contractor, Data Sharing, Website Privacy Notice,
  Website Cookie Notice, Business Customer T&Cs, Consumer Terms), plus a
  [UK Contracting Framework](02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/00_UK_CONTRACTING_FRAMEWORK.md)
  reference (architecture, order of precedence, signing order, minimum-clause
  checklist, IP/payment/liability principles, ICO/GOV.UK references). Grounded in the
  `00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md`; Lemuran Ltd is the
  default example supplier with reusable Supplier/Customer placeholders.
- **`tools/generate_business_docs.py`** — deterministic generator for the set
  (overwrites only the `Business_Documentation/` folder). Linked from the Phase 05
  index and generation index; picked up automatically by the MCP corpus and Pinecone
  reindex workflow.

## [2.9.0] - 2026-07-28

### Added

- **Two more Branding skills (Phase 05 › Branding, now 19 total).** Added
  [Consumer and Perception Research](02_ARTEFACTS/PHASE_05_SKILLS/Branding/18_CONSUMER_AND_PERCEPTION_RESEARCH_SKILL.md)
  (research-driven, perception-first positioning: segmentation, perceptual
  mapping, "the position you already own vs the one to create", creativity within
  reality, big-picture thinking) and
  [Repositioning](02_ARTEFACTS/PHASE_05_SKILLS/Branding/19_REPOSITIONING_SKILL.md)
  (changing an established perception by attribute, segment or category frame —
  including positioning against a leader and reframing the category, e.g. "the
  uncola"). These close the gaps from the *Positioning: The Battle for Your Mind*
  strategy/skill checklist; all other listed strategies were already covered
  across the existing skills.

## [2.8.0] - 2026-07-25

### Added

- **Branding skill set (Phase 05).** New
  [`02_ARTEFACTS/PHASE_05_SKILLS/Branding/`](02_ARTEFACTS/PHASE_05_SKILLS/Branding/README.md)
  with 17 detailed, ready-to-use branding competency skills — Focus &
  Simplification, Brand Positioning, Naming Expertise, Messaging Consistency,
  Strategic Brand Extension, Category Leadership, Publicity & Media Relations,
  Advertising & Promotion, Perception Management, Collaborative Networking
  (Fellowship), Global Brand Building, Brand Monitoring & Adaptation, Crisis &
  Change Management, Differentiation & Attribute Ownership, Competitor Analysis &
  Positioning, Category Creation, and Persistence & Long-term Vision — plus a
  [22 Immutable Laws of Branding](02_ARTEFACTS/PHASE_05_SKILLS/Branding/00_22_IMMUTABLE_LAWS_OF_BRANDING.md)
  reference. Each skill maps to the relevant laws and is grounded in current
  practice (Aaker & Keller brand-equity models, the positioning framework of
  points of difference vs points of parity, a structured naming methodology, and
  mental-availability / Category Entry Point measurement), with explicit
  anti-patterns, KPIs and human-in-the-loop AI guidance.
- **`tools/generate_branding_skills.py`** — deterministic generator for the
  Branding set (overwrites only the `Branding/` folder). Linked from the Phase 05
  index and the generation index; picked up automatically by the MCP corpus and
  the Pinecone reindex workflow.

## [2.7.0] - 2026-06-27

### Added

- **Automatic Pinecone reindex on push.** New
  `.github/workflows/reindex-pinecone.yml` rebuilds the hosted MCP search index
  whenever corpus content (`00_ROOT`, `01_PHASES`, `02_ARTEFACTS`) or the
  chunking/ingest code changes on `main` (also runnable manually). `ingest_pinecone.py`
  gains a `--fresh` mode (env `AIBOS_REINDEX_FRESH=1`) that clears the namespace
  first so deleted/renamed sections leave no stale chunks. Requires the
  `PINECONE_API_KEY` Actions secret.
- **`MCP_USAGE_GUIDE.md` — single authoritative guide** for using the AIBOS MCP
  server from every tool, IDE and AI client: Cursor, Claude Desktop, VS Code,
  Windsurf, JetBrains/Zed/Cline, ChatGPT, Gemini, Grok, your own app/SaaS and
  team-wide access, plus a tools/resources/prompts reference, example workflows,
  verification, security and troubleshooting. Linked from `README.md` and
  `mcp/README.md`.

### Fixed

- **MCP workflow relevance.** `improve_department` and `design_customer_solution`
  previously filtered on the raw user term (e.g. `category="HR"`), matching no
  category and silently falling back to a generic search. Added a normalized,
  alias-aware category resolver (built from the corpus's actual stored
  categories) with a filter-then-fallback strategy, so synonyms like HR/IT/
  Technology/Business Strategy and industries (Retail, e-commerce) resolve
  correctly; responses now include `matched_category` / `matched_industry`.
- **Vercel deployment.** Set `framework` to `null` in `vercel.json` so
  `api/index.py` is detected as a Python serverless function.

## [2.6.0] - 2026-06-27

### Added

- **`mcp/` — AIBOS Model Context Protocol server.** Exposes the repository to AI
  clients/agents with tools designed around two workflows: **client delivery**
  (`design_customer_solution`) and **internal operations** (`improve_department`),
  plus `search_aibos`, `get_aibos_document`, `get_best_practices`, `list_*`
  navigation tools, MCP resources (`aibos://index/root`, `aibos://standard/{name}`)
  and guided prompts (`client_engagement`, `internal_excellence`).
- **Dual transport:** `stdio` for Cursor / Claude Desktop / VS Code, and
  **Streamable-HTTP + bearer auth** for ChatGPT, Gemini, Grok, your own app and
  team use.
- **Two pluggable backends:** local SQLite FTS5 (no external services) and
  Pinecone integrated-embedding semantic search; corpus is chunked by `##`
  section with phase/category/document-type metadata for filtered retrieval.
- Ingest CLIs (`build_local_index.py`, `ingest_pinecone.py`), ready-made client
  configs under `mcp/clients/`, and a setup/deploy/security guide in
  `mcp/README.md`.
- **Remote deployment assets:** `mcp/Dockerfile` (builds the search index into
  the image), `mcp/docker-compose.yml`, Fly.io and Render configs under
  `mcp/deploy/`, an unauthenticated `/healthz` endpoint for load balancers, and
  guides `mcp/DEPLOY.md` and `mcp/clients/OTHER_IDES.md` (direct HTTP and the
  `mcp-remote` stdio bridge for other IDEs).
- **Vercel serverless deployment:** `api/index.py`, `vercel.json` and root
  `requirements.txt` run the MCP server as a Python Fluid-Compute function in
  stateless Streamable-HTTP mode with the Pinecone backend; `build_asgi_app()`
  in `mcp/aibos_mcp/server.py` is shared by the local HTTP server and Vercel.

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
