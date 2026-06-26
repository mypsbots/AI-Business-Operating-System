# GENERATION_INDEX.md

# AIBOS Enterprise v2.0 — Generated Artefacts Index

Version: 2.0.0

This index catalogues the artefacts generated from the Phase master prompts in
[`01_PHASES/`](../01_PHASES). Artefacts are produced by the deterministic,
idempotent generator at [`tools/generate_aibos.py`](../tools/generate_aibos.py),
embodying the **Documentation as Code** principle. Every artefact includes YAML
front matter, all sections required by its phase, and cross-references to the
inherited root standards.

## How Artefacts Are Generated

```bash
python3 tools/generate_aibos.py            # generate missing artefacts
python3 tools/generate_aibos.py --overwrite  # regenerate all (protects hand-authored docs)
```

The generator is data-driven: each phase's deliverable list and required section
schema are encoded from the corresponding master prompt. Hand-authored documents
(for example, the enriched Phase 01 foundation documents) are protected and never
overwritten.

## Artefact Counts by Phase

| Phase | Area | Documents |
|------:|------|----------:|
| 01 | Enterprise Architecture | 20 |
| 02 | Enterprise Specifications | 10 |
| 03 | Division Specifications | 20 |
| 04 | Department Specifications | 70 |
| 05 | Specialist Skills | 48 |
| 06 | Enterprise Rules | 47 |
| 07 | Enterprise Checklists | 45 |
| 08 | Enterprise Playbooks | 36 |
| 09 | Enterprise Templates | 35 |
| 10 | Enterprise Knowledge | 59 |
| 11 | AI Agent Collaboration | 32 |
| 12 | Enterprise Automation | 40 |
| 13 | Industry Blueprints (30 industries x 10 docs) | 300 |
| 14 | Accelerator Packs | 52 |
| 15 | Reference Implementations | 52 |
| 16 | SDK & CLI | 39 |
| 17 | Certification & Maturity | 34 |
| 18 | Marketplace & Extensions | 42 |
| 19 | Reference AI Organisation | 49 |
| 20 | Meta-Orchestrator | 37 |
| **Total** | | **1067** |

## Directory Layout

```text
02_ARTEFACTS/
├── PHASE_01_ENTERPRISE_ARCHITECTURE/
├── PHASE_02_ENTERPRISE_SPECIFICATIONS/
├── PHASE_03_DIVISION_SPECIFICATIONS/
├── PHASE_04_DEPARTMENT_SPECIFICATIONS/<Division>/
├── PHASE_05_SKILLS/
├── PHASE_06_RULES/<Category>/
├── PHASE_07_CHECKLISTS/<Category>/
├── PHASE_08_PLAYBOOKS/<Category>/
├── PHASE_09_TEMPLATES/<Category>/
├── PHASE_10_KNOWLEDGE/<Domain>/
├── PHASE_11_AI_AGENT_COLLABORATION/<Group>/
├── PHASE_12_AUTOMATION/<Group>/
├── PHASE_13_INDUSTRY_BLUEPRINTS/<Industry>/
├── PHASE_14_ACCELERATOR_PACKS/<Category>/
├── PHASE_15_REFERENCE_IMPLEMENTATIONS/<Group>/
├── PHASE_16_SDK_CLI/<Group>/
├── PHASE_17_CERTIFICATION/<Group>/
├── PHASE_18_MARKETPLACE/<Group>/
├── PHASE_19_REFERENCE_ORGANISATION/<Group>/
└── PHASE_20_META_ORCHESTRATOR/<Group>/
```

## Status & Maturity

All artefacts are generated at **Draft** status with complete structure,
metadata and cross-references. They provide a consistent, validated foundation
that subject-matter experts and AI agents enrich into fully detailed content,
following the AIBOS quality and validation standards. The enriched Phase 01
foundation documents demonstrate the target depth.

## Version History

| Version | Date | Summary |
|---------|------|---------|
| 2.0.0 | 2026-06-26 | Initial generation of 1067 artefacts across 20 phases. |
