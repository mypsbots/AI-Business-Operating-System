# ROOT_INDEX.md

# AIBOS Enterprise v2.0 — Repository Index

Version: 2.5.0

This document is the authoritative, ordered index of every artefact in the
AIBOS Enterprise repository. It is maintained as both a human-readable map and
a machine-friendly catalogue to support navigation, governance and AI
retrieval.

---

## Reading & Execution Order

Artefacts MUST be loaded and executed in the order below. The root
specification takes precedence over all other documents.

---

## Stage 0 & 1 — Root Foundation and Standards

Location: [`00_ROOT/`](00_ROOT)

| # | Document | Purpose |
|--:|----------|---------|
| 1 | [AIBOS_ROOT_SPECIFICATION.md](00_ROOT/AIBOS_ROOT_SPECIFICATION.md) | Constitutional specification inherited by every artefact. |
| 2 | [BUILD_AIBOS_MASTER_PROMPT_v2.md](00_ROOT/BUILD_AIBOS_MASTER_PROMPT_v2.md) | Master orchestrator prompt and execution workflow. |
| 3 | [AIBOS_ENTERPRISE_GLOSSARY.md](00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md) | Canonical semantic dictionary and terminology. |
| 4 | [AIBOS_STYLE_GUIDE.md](00_ROOT/AIBOS_STYLE_GUIDE.md) | Mandatory writing, formatting and presentation standards. |
| 5 | [AIBOS_DOCUMENT_SCHEMA.md](00_ROOT/AIBOS_DOCUMENT_SCHEMA.md) | Canonical Markdown document schema and section order. |
| 6 | [AIBOS_METADATA_STANDARD.md](00_ROOT/AIBOS_METADATA_STANDARD.md) | Canonical metadata model and controlled vocabularies. |
| 7 | [AIBOS_NAMING_STANDARD.md](00_ROOT/AIBOS_NAMING_STANDARD.md) | Mandatory naming conventions for all artefacts. |
| 8 | [AIBOS_VERSIONING_STANDARD.md](00_ROOT/AIBOS_VERSIONING_STANDARD.md) | Semantic versioning and release-channel strategy. |
| 9 | [AIBOS_QUALITY_STANDARD.md](00_ROOT/AIBOS_QUALITY_STANDARD.md) | Quality gates, dimensions and definitions of ready/done. |
| 10 | [AIBOS_VALIDATION_STANDARD.md](00_ROOT/AIBOS_VALIDATION_STANDARD.md) | Validation framework, severity levels and scorecard. |
| 11 | [AIBOS_GENERATION_STANDARD.md](00_ROOT/AIBOS_GENERATION_STANDARD.md) | Deterministic, multi-model artefact generation process. |
| 12 | [AIBOS_SECURITY_STANDARD.md](00_ROOT/AIBOS_SECURITY_STANDARD.md) | Security, privacy and Zero Trust baseline. |
| 13 | [AIBOS_AI_BEHAVIOUR_STANDARD.md](00_ROOT/AIBOS_AI_BEHAVIOUR_STANDARD.md) | Behavioural contract for AI models and agents. |
| 14 | [AIBOS_ARCHITECTURE_PRINCIPLES.md](00_ROOT/AIBOS_ARCHITECTURE_PRINCIPLES.md) | Enterprise and solution architecture principles. |
| 15 | [AIBOS_DESIGN_PRINCIPLES.md](00_ROOT/AIBOS_DESIGN_PRINCIPLES.md) | Product, UX, API and AI design principles. |
| 16 | [AIBOS_REFERENCE_STANDARDS.md](00_ROOT/AIBOS_REFERENCE_STANDARDS.md) | Catalogue of adopted external standards and frameworks. |
| 17 | [AIBOS_EXECUTION_WORKFLOW.md](00_ROOT/AIBOS_EXECUTION_WORKFLOW.md) | End-to-end execution and lifecycle workflow. |

**Orchestration reference:**
[AIBOS_ENTERPRISE_EXECUTION_ORDER_AND_MASTER_EXECUTION_PROMPT.md](00_ROOT/AIBOS_ENTERPRISE_EXECUTION_ORDER_AND_MASTER_EXECUTION_PROMPT.md)
— defines the recommended structure, execution order and master execution
prompt for the entire repository.

---

## Stage 2 — Phase Prompts

Location: [`01_PHASES/`](01_PHASES)

Phases MUST be generated sequentially. Before each phase: load all root
documents, load previously completed phases, resolve dependencies, validate
terminology and reuse existing artefacts.

| Phase | Document | Generates |
|------:|----------|-----------|
| 01 | [PHASE_01_ENTERPRISE_ARCHITECTURE_MASTER_PROMPT.md](01_PHASES/PHASE_01_ENTERPRISE_ARCHITECTURE_MASTER_PROMPT.md) | Enterprise Architecture |
| 02 | [PHASE_02_ENTERPRISE_SPECIFICATIONS_MASTER_PROMPT.md](01_PHASES/PHASE_02_ENTERPRISE_SPECIFICATIONS_MASTER_PROMPT.md) | Enterprise Specifications |
| 03 | [PHASE_03_DIVISION_SPECIFICATIONS_MASTER_PROMPT.md](01_PHASES/PHASE_03_DIVISION_SPECIFICATIONS_MASTER_PROMPT.md) | Division Specifications |
| 04 | [PHASE_04_DEPARTMENT_SPECIFICATIONS_MASTER_PROMPT.md](01_PHASES/PHASE_04_DEPARTMENT_SPECIFICATIONS_MASTER_PROMPT.md) | Department Specifications |
| 05 | [PHASE_05_SKILLS_MASTER_PROMPT.md](01_PHASES/PHASE_05_SKILLS_MASTER_PROMPT.md) | Specialist Skills |
| 06 | [PHASE_06_RULES_MASTER_PROMPT.md](01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md) | Enterprise Rules |
| 07 | [PHASE_07_CHECKLISTS_MASTER_PROMPT.md](01_PHASES/PHASE_07_CHECKLISTS_MASTER_PROMPT.md) | Enterprise Checklists |
| 08 | [PHASE_08_PLAYBOOKS_MASTER_PROMPT.md](01_PHASES/PHASE_08_PLAYBOOKS_MASTER_PROMPT.md) | Enterprise Playbooks |
| 09 | [PHASE_09_TEMPLATES_MASTER_PROMPT.md](01_PHASES/PHASE_09_TEMPLATES_MASTER_PROMPT.md) | Enterprise Templates |
| 10 | [PHASE_10_KNOWLEDGE_MASTER_PROMPT.md](01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md) | Enterprise Knowledge |
| 11 | [PHASE_11_AI_AGENT_COLLABORATION_MASTER_PROMPT.md](01_PHASES/PHASE_11_AI_AGENT_COLLABORATION_MASTER_PROMPT.md) | AI Agent Collaboration Framework |
| 12 | [PHASE_12_ENTERPRISE_AUTOMATION_CONTINUOUS_IMPROVEMENT_MASTER_PROMPT.md](01_PHASES/PHASE_12_ENTERPRISE_AUTOMATION_CONTINUOUS_IMPROVEMENT_MASTER_PROMPT.md) | Automation & Continuous Improvement |
| 13 | [PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md](01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md) | Industry Blueprints & Reference Architectures |
| 14 | [PHASE_14_ENTERPRISE_ACCELERATOR_PACKS_MASTER_PROMPT.md](01_PHASES/PHASE_14_ENTERPRISE_ACCELERATOR_PACKS_MASTER_PROMPT.md) | Enterprise Accelerator Packs |
| 15 | [PHASE_15_ENTERPRISE_REFERENCE_IMPLEMENTATIONS_MASTER_PROMPT.md](01_PHASES/PHASE_15_ENTERPRISE_REFERENCE_IMPLEMENTATIONS_MASTER_PROMPT.md) | Reference Implementations |
| 16 | [PHASE_16_AIBOS_SDK_CLI_MASTER_PROMPT.md](01_PHASES/PHASE_16_AIBOS_SDK_CLI_MASTER_PROMPT.md) | AIBOS SDK & CLI |
| 17 | [PHASE_17_AIBOS_CERTIFICATION_MATURITY_MASTER_PROMPT.md](01_PHASES/PHASE_17_AIBOS_CERTIFICATION_MATURITY_MASTER_PROMPT.md) | Certification & Maturity Framework |
| 18 | [PHASE_18_AIBOS_MARKETPLACE_EXTENSION_FRAMEWORK_MASTER_PROMPT.md](01_PHASES/PHASE_18_AIBOS_MARKETPLACE_EXTENSION_FRAMEWORK_MASTER_PROMPT.md) | Marketplace & Extension Framework |
| 19 | [PHASE_19_AIBOS_REFERENCE_AI_ORGANISATION_MASTER_PROMPT.md](01_PHASES/PHASE_19_AIBOS_REFERENCE_AI_ORGANISATION_MASTER_PROMPT.md) | Reference AI Organisation |
| 20 | [PHASE_20_AIBOS_META_ORCHESTRATOR_AUTONOMOUS_ENTERPRISE_MASTER_PROMPT.md](01_PHASES/PHASE_20_AIBOS_META_ORCHESTRATOR_AUTONOMOUS_ENTERPRISE_MASTER_PROMPT.md) | Meta-Orchestrator & Autonomous Enterprise |

---

## Generated Artefacts

Location: [`02_ARTEFACTS/`](02_ARTEFACTS)

The Phase master prompts drive generation of the detailed enterprise artefacts.
These are produced by the deterministic generators under
[`tools/`](tools) and catalogued in
[`02_ARTEFACTS/GENERATION_INDEX.md`](02_ARTEFACTS/GENERATION_INDEX.md)
(1067 detailed, ready-to-use documents across all 20 phases). Each phase folder
also has a browsable `README.md` index.

---

## Repository Meta Documents

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Project overview and getting started guide. |
| [FINAL_REPORT.md](FINAL_REPORT.md) | Assembly, validation and completion report. |
| [CHANGELOG.md](CHANGELOG.md) | Semantic-versioned change history. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution workflow and standards. |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community behaviour expectations. |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting process. |

---

## Version History

| Version | Summary |
|---------|---------|
| 2.5.0 | All 20 phases enriched to detailed, ready-to-use depth; validated (lint + links clean). |
| 2.0.0 | Initial repository index covering 17 root documents and 20 phases. |
