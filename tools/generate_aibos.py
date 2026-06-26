#!/usr/bin/env python3
"""AIBOS Enterprise v2.0 artefact generator.

Generates schema-compliant, cross-linked Markdown artefacts for Phases 1-20 from
the master prompts under ``01_PHASES``. Output is written to ``02_ARTEFACTS``.

Design goals:
- Deterministic and idempotent (``--overwrite`` regenerates everything).
- Every document includes YAML front matter, a navigation breadcrumb, all the
  sections required by its phase, and **working relative links** to the
  inherited standards and related phase artefacts.
- A browsable ``README.md`` index is written into every folder so the repository
  is easy to navigate on GitHub.
- Output is markdownlint-clean.

This embodies the "Documentation as Code" principle from
AIBOS_ROOT_SPECIFICATION.md.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS"

STANDARDS = ["ISO 42001", "ISO 27001", "NIST AI RMF", "SOC 2", "OWASP ASVS",
             "OWASP LLM Top 10", "WCAG 2.2 AA"]

PHASE_DIR = {
    1: "PHASE_01_ENTERPRISE_ARCHITECTURE",
    2: "PHASE_02_ENTERPRISE_SPECIFICATIONS",
    3: "PHASE_03_DIVISION_SPECIFICATIONS",
    4: "PHASE_04_DEPARTMENT_SPECIFICATIONS",
    5: "PHASE_05_SKILLS",
    6: "PHASE_06_RULES",
    7: "PHASE_07_CHECKLISTS",
    8: "PHASE_08_PLAYBOOKS",
    9: "PHASE_09_TEMPLATES",
    10: "PHASE_10_KNOWLEDGE",
    11: "PHASE_11_AI_AGENT_COLLABORATION",
    12: "PHASE_12_AUTOMATION",
    13: "PHASE_13_INDUSTRY_BLUEPRINTS",
    14: "PHASE_14_ACCELERATOR_PACKS",
    15: "PHASE_15_REFERENCE_IMPLEMENTATIONS",
    16: "PHASE_16_SDK_CLI",
    17: "PHASE_17_CERTIFICATION",
    18: "PHASE_18_MARKETPLACE",
    19: "PHASE_19_REFERENCE_ORGANISATION",
    20: "PHASE_20_META_ORCHESTRATOR",
}

PHASE_TITLE = {
    1: "Enterprise Architecture", 2: "Enterprise Specifications",
    3: "Division Specifications", 4: "Department Specifications",
    5: "Specialist Skills", 6: "Enterprise Rules", 7: "Enterprise Checklists",
    8: "Enterprise Playbooks", 9: "Enterprise Templates", 10: "Enterprise Knowledge",
    11: "AI Agent Collaboration", 12: "Enterprise Automation",
    13: "Industry Blueprints", 14: "Accelerator Packs",
    15: "Reference Implementations", 16: "SDK and CLI",
    17: "Certification and Maturity", 18: "Marketplace",
    19: "Reference Organisation", 20: "Meta-Orchestrator",
}

PHASE_PROMPT = {
    1: "PHASE_01_ENTERPRISE_ARCHITECTURE_MASTER_PROMPT.md",
    2: "PHASE_02_ENTERPRISE_SPECIFICATIONS_MASTER_PROMPT.md",
    3: "PHASE_03_DIVISION_SPECIFICATIONS_MASTER_PROMPT.md",
    4: "PHASE_04_DEPARTMENT_SPECIFICATIONS_MASTER_PROMPT.md",
    5: "PHASE_05_SKILLS_MASTER_PROMPT.md",
    6: "PHASE_06_RULES_MASTER_PROMPT.md",
    7: "PHASE_07_CHECKLISTS_MASTER_PROMPT.md",
    8: "PHASE_08_PLAYBOOKS_MASTER_PROMPT.md",
    9: "PHASE_09_TEMPLATES_MASTER_PROMPT.md",
    10: "PHASE_10_KNOWLEDGE_MASTER_PROMPT.md",
    11: "PHASE_11_AI_AGENT_COLLABORATION_MASTER_PROMPT.md",
    12: "PHASE_12_ENTERPRISE_AUTOMATION_CONTINUOUS_IMPROVEMENT_MASTER_PROMPT.md",
    13: "PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md",
    14: "PHASE_14_ENTERPRISE_ACCELERATOR_PACKS_MASTER_PROMPT.md",
    15: "PHASE_15_ENTERPRISE_REFERENCE_IMPLEMENTATIONS_MASTER_PROMPT.md",
    16: "PHASE_16_AIBOS_SDK_CLI_MASTER_PROMPT.md",
    17: "PHASE_17_AIBOS_CERTIFICATION_MATURITY_MASTER_PROMPT.md",
    18: "PHASE_18_AIBOS_MARKETPLACE_EXTENSION_FRAMEWORK_MASTER_PROMPT.md",
    19: "PHASE_19_AIBOS_REFERENCE_AI_ORGANISATION_MASTER_PROMPT.md",
    20: "PHASE_20_AIBOS_META_ORCHESTRATOR_AUTONOMOUS_ENTERPRISE_MASTER_PROMPT.md",
}

# Section keyword -> phase number, used to link cross-reference sections to the
# correct phase artefacts folder.
XREF_KEYWORDS = [
    ("checklist", 7), ("playbook", 8), ("template", 9), ("knowledge", 10),
    ("industry", 13), ("blueprint", 13), ("department", 4), ("agent", 11),
    ("automation", 12), ("marketplace", 18), ("sdk", 16), ("skill", 5),
    ("rule", 6),
]

ACRONYMS = {"AI", "API", "SDK", "CLI", "RAG", "MCP", "BI", "QA", "SRE", "IAM",
            "KPI", "OKR", "UX", "SEO", "AEO", "GEO", "IP", "HR", "PMO", "ETL",
            "CDC", "SBOM", "SOP", "PRD", "ADR", "ROI", "SME", "GA", "LTS",
            "OWASP", "ISO", "NIST", "SOC", "WCAG", "GDPR", "CI", "CD", "LLM",
            "LLMS", "FAQ", "AIBOS", "ASFE", "AIAE", "AICE", "MVP", "SAAS"}


# --------------------------------------------------------------------------- #
# Link + formatting helpers
# --------------------------------------------------------------------------- #
def rellink(from_dir: Path, target: Path) -> str:
    return os.path.relpath(target, from_dir).replace(os.sep, "/")


def slug(text: str) -> str:
    text = text.replace("&", "and").replace("/", " ").replace("+", " plus ")
    text = re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_")
    return text.upper()


def display(name: str) -> str:
    name = re.sub(r"\.md$", "", name)
    name = re.sub(r"^\d+_", "", name)
    words = name.replace("_", " ").split()
    out = []
    for w in words:
        out.append(w.upper() if w.upper() in ACRONYMS else w.capitalize())
    return " ".join(out) or name


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def numbered(items: list[str]) -> str:
    return "\n".join(f"{i}. {t}" for i, t in enumerate(items, start=1))


def checkboxes(items: list[str]) -> str:
    return "\n".join(f"- [ ] {i}" for i in items)


def table(headers: list[str], rows: list[list[str]]) -> str:
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{head}\n{sep}\n{body}"


def fenced(lang: str, code: str) -> str:
    return f"```{lang}\n{code.strip()}\n```"


def front_matter(doc_id, title, doc_type, category, phase, owner, tags, related):
    tag_lines = "\n".join(f"  - {t}" for t in tags) or "  - aibos"
    rel_lines = "\n".join(f"  - {r}" for r in related)
    std_lines = "\n".join(f"  - {s}" for s in STANDARDS)
    return ("---\n"
            f"id: {doc_id}\n"
            f"title: {title}\n"
            f"document_type: {doc_type}\n"
            f"category: {category}\n"
            f"phase: {phase}\n"
            f"owner: {owner}\n"
            "status: Draft\n"
            "lifecycle: Active\n"
            "classification: Internal\n"
            f"version: {VERSION}\n"
            f"created: {DATE}\n"
            f"updated: {DATE}\n"
            "tags:\n"
            f"{tag_lines}\n"
            "related_documents:\n"
            f"{rel_lines}\n"
            "standards:\n"
            f"{std_lines}\n"
            "---")


MERMAID_FLOW = fenced("mermaid", """
flowchart TD
    A[Trigger] --> B[Process Inputs]
    B --> C{High-risk action?}
    C -->|Yes| D[Human Approval]
    C -->|No| E[AI Agent Executes]
    D --> E
    E --> F[Validate Output]
    F --> G[Record Audit Trail]
""")

VERSION_TABLE = table(["Version", "Date", "Summary"],
                      [[VERSION, DATE, "Initial generated artefact."]])


# --------------------------------------------------------------------------- #
# Section content builder
# --------------------------------------------------------------------------- #
def xref_phase(name: str):
    n = name.lower()
    for kw, p in XREF_KEYWORDS:
        if kw in n:
            return p
    return None


def build_section(name: str, ctx: dict) -> str:
    title = ctx["title"]
    phase = ctx["phase"]
    lr = ctx["link_root"]
    ld = ctx["link_dir"]
    n = name.lower()

    if name == "Version History":
        return VERSION_TABLE
    if name == "Validation Checklist" or n == "validation steps":
        return checkboxes([
            "YAML front matter is present and valid.",
            "All mandatory sections are complete.",
            "Terminology matches the AIBOS Enterprise Glossary.",
            "Cross-references resolve to existing documents.",
            "RFC 2119 keywords are used correctly.",
            "Security and privacy considerations are addressed.",
            "Version history is updated.",
            "No secrets or sensitive data are exposed.",
        ])
    if "mermaid" in n or n.endswith("diagram") or n.endswith("diagrams"):
        return MERMAID_FLOW
    if n == "decision tree":
        return fenced("mermaid", """
flowchart TD
    Q1{Meets acceptance criteria?} -->|No| R[Reject and remediate]
    Q1 -->|Yes| Q2{High-risk?}
    Q2 -->|Yes| H[Escalate for human approval]
    Q2 -->|No| A[Approve and proceed]
""")
    if n == "json schema":
        return fenced("json", """
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["id", "title", "version"],
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "version": { "type": "string" }
  }
}
""")
    if n in ("yaml schema", "required metadata", "metadata schema"):
        return fenced("yaml", """
id: DOC-000000
title: Example
version: 2.0.0
owner: Owning Team
classification: Internal
""")
    if n in ("example completed template", "sample usage", "examples",
             "package manifest"):
        return fenced("yaml", f"""
# Example for: {title}
name: example
version: {VERSION}
status: draft
""")

    # Cross-reference sections -> real relative links ----------------------- #
    # The four skill sub-competency sections are differentiated below; they must
    # not be treated as generic cross-references even though they contain "skill".
    SKILL_SUBSKILLS = {"required technical skills", "required business skills",
                       "required ai skills", "required soft skills"}
    p = xref_phase(name)
    if p is not None and n not in SKILL_SUBSKILLS and (
        n.startswith(("required", "related", "applicable", "supporting",
                      "governing")) or n.endswith("mapping")
        or n in ("ai agents involved", "knowledge dependencies",
                 "applicable departments", "marketplace assets", "sdk usage")):
        return bullets([
            f"See **[{PHASE_TITLE[p]} (Phase {p:02d})]({ld(p)})** for the "
            "relevant artefacts.",
            f"Inherited standards: [AIBOS Root Specification]"
            f"({lr('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')}).",
            f"Full catalogue: [ROOT_INDEX]({lr('ROOT_INDEX.md')}).",
        ])

    if name == "References":
        return bullets([
            f"[AIBOS Root Specification]({lr('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')})",
            f"[Enterprise Glossary]({lr('00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md')})",
            f"[Document Schema]({lr('00_ROOT/AIBOS_DOCUMENT_SCHEMA.md')})",
            f"[Repository Catalogue (ROOT_INDEX)]({lr('ROOT_INDEX.md')})",
            f"[Phase {ctx['num']:02d} Master Prompt]({ctx['link_prompt']()})",
        ])

    if "raci" in n:
        return table(["Activity", "Responsible", "Accountable", "Consulted", "Informed"],
                     [["Primary task", "Specialist", "Department Lead", "Architecture",
                       "Stakeholders"]])
    if "matrix" in n:
        return table(["Partner", "Interaction", "Direction"],
                     [["Upstream owners", "Provide inputs", "Inbound"],
                      ["Downstream consumers", "Consume outputs", "Outbound"],
                      ["Governance", "Review and approve", "Bidirectional"]])
    if "30/60/90" in n or "roadmap" in n:
        return table(["Horizon", "Focus", "Outcome"],
                     [["0-30 days", "Discover and assess", "Baseline established"],
                      ["31-60 days", "Design and build", "Pilot delivered"],
                      ["61-90 days", "Validate and scale", "Production rollout"]])
    if n == "mandatory requirements (must)":
        return bullets([
            f"The team MUST apply the AIBOS root standards when implementing {title}.",
            "The team MUST validate every artefact before publication.",
            "The team MUST require human approval for high-risk actions.",
            "The team MUST maintain an auditable trail of decisions."])
    if n == "recommended practices (should)":
        return bullets([
            "Teams SHOULD automate repeatable validation where practical.",
            "Teams SHOULD reuse existing artefacts before creating new ones.",
            "Teams SHOULD capture metrics to drive continuous improvement."])
    if n == "optional practices (may)":
        return bullets([
            "Teams MAY extend this artefact for domain-specific needs.",
            "Teams MAY add additional tooling integrations."])
    if n in ("standards mapping", "compliance mapping", "compliance requirements",
             "compliance controls", "external standards", "compliance validation"):
        return table(["Standard", "Application"],
                     [["ISO 42001", "AI management system alignment."],
                      ["ISO 27001", "Information security controls."],
                      ["NIST AI RMF", "AI risk management."],
                      ["OWASP LLM Top 10", "LLM threat mitigation."]])
    if n == "faqs":
        return ("**Q: How does this artefact relate to the AIBOS standards?**\n\n"
                "A: It inherits and must not contradict the root standards.\n\n"
                f"**Q: Who owns {title}?**\n\n"
                f"A: {ctx['owner']}.")
    if n == "definitions":
        return bullets([
            f"Canonical terms are defined in the "
            f"[Enterprise Glossary]({lr('00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md')}).",
            "No terminology is redefined within this document."])

    # Skill-specific differentiated content --------------------------------- #
    skill_sections = {
        "required technical skills": [
            "Proficiency with the relevant languages, frameworks and tooling.",
            "Sound understanding of APIs, data structures and system design.",
            "Cloud-native, CI/CD and Infrastructure-as-Code practices.",
            "Disciplined version control with Git and peer code review."],
        "required business skills": [
            "Translating business goals into measurable outcomes.",
            "Stakeholder communication and expectation management.",
            "Prioritisation, planning and value-based decision making.",
            "Commercial awareness of cost, ROI and risk."],
        "required ai skills": [
            "Prompt engineering and context design for LLMs.",
            "Retrieval-Augmented Generation (RAG) and evaluation techniques.",
            "Responsible AI, guardrails and hallucination mitigation.",
            "Awareness of the OWASP LLM Top 10."],
        "required soft skills": [
            "Clear written and verbal communication.",
            "Collaboration across human and AI teams.",
            "Critical thinking and structured problem solving.",
            "Adaptability and a continuous-learning mindset."],
        "required certifications": [
            "A relevant cloud certification (AWS, Azure or GCP).",
            "A security certification where applicable.",
            "The matching AIBOS role certification (see Phase 17)."],
        "required tools": [
            "Git and GitHub for version control and collaboration.",
            "CI/CD pipelines and Infrastructure as Code.",
            "AI tooling: IDE assistants, model providers and MCP servers.",
            "Observability and security-scanning tooling."],
        "technology stack": [
            "Cloud-native runtime and managed services.",
            "API-first interfaces (OpenAPI) and event-driven messaging.",
            "Vector database and RAG components where applicable.",
            "OpenTelemetry-based observability."],
        "services provided": [
            "Specialist outputs that meet the AIBOS Definition of Done.",
            "Reviews and guidance within the role's authority.",
            "Reusable artefacts contributed back to the enterprise."],
        "services consumed": [
            "Inputs and decisions from upstream roles and divisions.",
            "Shared platforms, tooling and knowledge.",
            "Governance approvals for high-risk actions."],
        "out of scope": [
            "Responsibilities owned by other roles or departments.",
            "Decisions outside the role's delegated authority.",
            "High-risk actions without human approval."],
        "deliverables": [
            "Validated, versioned artefacts.",
            "Updated cross-references and documentation.",
            "Evidence required by the relevant checklists."],
        "interview questions": [
            f"How would you apply the AIBOS standards in the {title} role?",
            "Describe how you ensure security and privacy by design.",
            "How do you collaborate safely with AI agents?",
            "Give an example of measuring and improving quality."],
    }
    if n in skill_sections:
        return bullets(skill_sections[n])
    if n == "recommended learning path":
        return numbered([
            f"Study the [root standards]({lr('00_ROOT')}).",
            "Complete the relevant department specification (Phase 04).",
            "Practise with the related playbooks and templates.",
            "Pursue the matching AIBOS certification (Phase 17)."])
    if n == "self assessment matrix":
        return table(["Level", "Indicator"],
                     [["Foundational", "Understands the standards and applies guidance."],
                      ["Proficient", "Delivers independently to the Definition of Done."],
                      ["Advanced", "Mentors others and improves the standards."]])

    # Narrative defaults ---------------------------------------------------- #
    narrative = {
        "executive summary":
            f"This document defines **{title}** within the AIBOS Enterprise v2.0 "
            f"framework ({phase}). It inherits every root standard and is designed "
            "to be enterprise-ready, machine-readable and AI-friendly.",
        "purpose":
            f"To establish the authoritative, reusable definition of {title} so "
            "that human teams and AI agents operate consistently, safely and with "
            "measurable business value.",
        "scope":
            "Applies across the AIBOS enterprise and is inherited by all dependent "
            "artefacts. Concerns owned elsewhere are delegated to their owning "
            "documents to avoid duplication.",
        "vision":
            f"{title} contributes to an AI-native enterprise that is secure, "
            "governed, automated and continuously improving.",
        "mission":
            f"To operate {title} to a consistent, enterprise-grade standard that "
            "balances autonomy with human oversight.",
        "business purpose":
            f"{title} exists to deliver measurable value while upholding the AIBOS "
            "principles of security, privacy and accountability.",
        "business value":
            "Reduced duplication, faster safe delivery, improved compliance posture "
            "and scalable AI augmentation.",
        "objectives":
            bullets(["Establish a clear, governed definition.",
                     "Enable consistent execution by humans and AI agents.",
                     "Provide measurable acceptance criteria."]),
        "responsibilities":
            bullets(["Own and maintain this artefact.",
                     "Ensure alignment with the root standards.",
                     "Validate outputs before publication."]),
        "guiding principles":
            bullets(["AI First", "Security by Design", "Privacy by Design",
                     "Zero Trust", "Documentation as Code", "Human-in-the-Loop"]),
        "risks":
            bullets(["Scope drift over time.",
                     "Inconsistent adoption across teams.",
                     "Over-automation without adequate oversight."]),
        "mitigations":
            bullets(["Periodic governance review.",
                     "Automated validation in CI.",
                     "Mandatory human approval for high-risk actions."]),
        "assumptions":
            bullets(["Root standards are adopted enterprise-wide.",
                     "Executive sponsorship is sustained."]),
        "dependencies":
            bullets(["Inherits the root standards in `00_ROOT/`.",
                     "Depends on earlier phases as defined by the master prompt."]),
        "upstream dependencies":
            bullets(["Receives inputs from earlier phases and divisions.",
                     "Relies on the inherited root standards."]),
        "downstream consumers":
            bullets(["Dependent divisions, departments and artefacts.",
                     "AI agents that consume this document for grounding."]),
        "acceptance criteria":
            bullets(["All mandatory sections are complete.",
                     "Validation passes with no errors.",
                     "Cross-references are valid."]),
        "security responsibilities":
            "Apply Security by Design, least privilege and Zero Trust; protect "
            "secrets; follow OWASP ASVS and the OWASP LLM Top 10.",
        "security considerations":
            "Apply Security by Design, least privilege and Zero Trust; protect "
            "secrets and follow OWASP guidance.",
        "security controls":
            bullets(["Authentication and authorisation enforced.",
                     "Encryption in transit and at rest.",
                     "Audit logging and continuous monitoring."]),
        "ai responsibilities":
            "Maintain human-in-the-loop controls, minimise hallucinations, prefer "
            "verified knowledge and preserve audit trails.",
        "ai considerations":
            "Maintain human-in-the-loop controls and minimise hallucination risk.",
        "privacy considerations":
            "Apply data minimisation, purpose limitation and retention controls.",
        "privacy controls":
            bullets(["Data minimisation.", "Purpose limitation.",
                     "Retention and secure-deletion policies."]),
        "compliance responsibilities":
            "Map controls to ISO 27001, ISO 42001 and SOC 2; retain audit evidence.",
        "best practices":
            bullets(["Reuse before build.",
                     "Automate validation.",
                     "Keep documents atomic and cross-referenced."]),
        "anti-patterns":
            bullets(["Duplicating concepts defined elsewhere.",
                     "Bypassing human approval for high-risk actions.",
                     "Undocumented exceptions."]),
        "definition of done":
            bullets(["Artefact validated and approved.",
                     "Cross-references confirmed.",
                     "Version history updated."]),
        "kpis":
            bullets(["Coverage and completeness.",
                     "Validation pass rate (target 95%+).",
                     "Cycle time from draft to approval.",
                     "Reuse rate across the enterprise."]),
        "metrics":
            bullets(["Quality score.", "Defect density.", "Review turnaround."]),
        "okrs":
            bullets(["Objective: raise enterprise consistency.",
                     "Key result: 95%+ validation pass rate.",
                     "Key result: measurable reuse across teams."]),
        "slas":
            bullets(["Acknowledgement within 1 business day.",
                     "Resolution targets aligned to severity.",
                     "Reporting on breaches and trends."]),
        "slos":
            bullets(["Availability and latency targets defined per service.",
                     "Error budgets tracked and reviewed."]),
        "slas/slos":
            bullets(["Service-level objectives defined and monitored.",
                     "Error budgets and breach handling defined."]),
    }
    if n in narrative:
        return narrative[n]

    # Keyword-aware, section-appropriate content so every section is useful and
    # varied (rather than a single generic placeholder). Keyed on the section name.
    def has(*words):
        return any(w in n for w in words)

    if has("challenge", "pain point", "problem"):
        return bullets([
            f"Complexity and fragmentation that make {title.lower()} hard to scale.",
            "Manual, repetitive work that is slow and error-prone.",
            "Governance, security and compliance obligations to uphold.",
            "Change management and adoption across teams."])
    if has("goal", "objective", "outcome") and not has("learning"):
        return bullets([
            f"Deliver {title.lower()} consistently and at scale.",
            "Increase speed and quality while reducing cost.",
            "Maintain security, privacy and compliance.",
            "Enable safe AI augmentation with human oversight."])
    if has("opportunit", "use case", "use-case"):
        return bullets([
            "Conversational assistants grounded in approved sources (RAG).",
            "Workflow automation for repetitive, rules-based tasks.",
            "Predictive analytics to anticipate issues and demand.",
            "AI-assisted drafting, synthesis and decision support.",
            "Always with human-in-the-loop for high-risk actions."])
    if has("capability map", "capability model", "capabilities"):
        return table(["Capability", "Description"],
                     [["Discover", "Understand needs and data."],
                      ["Build", "Implement with reusable components."],
                      ["Operate", "Run safely with observability."],
                      ["Govern", "Oversee risk, security and compliance."],
                      ["Improve", "Measure and iterate continuously."]])
    if has("operating model", "target operating"):
        return bullets([
            "AI agents augment teams under human oversight.",
            "A shared platform provides data, RAG, agents and automation.",
            "A centre of excellence sets standards; teams deliver value.",
            "Continuous measurement against defined success metrics."])
    if has("architecture", "solution design", "blueprint") and "decision" not in n:
        return bullets([
            "Experience layer: apps, assistants and channels.",
            "Orchestration layer: agents, tools (MCP) and workflows.",
            "AI layer: LLMs, RAG, evaluation and guardrails.",
            "Data layer: sources, pipelines, vector store and governance.",
            "Platform layer: cloud, security and observability."])
    if has("data source", "data input"):
        return bullets([
            "Core line-of-business systems and databases.",
            "Event streams and operational telemetry.",
            "Documents and knowledge bases (for RAG).",
            "Third-party and reference data, governed for access."])
    if has("data model", "entities", "schema") and "json" not in n and "yaml" not in n:
        return bullets([
            "Core entities are modelled with clear keys and ownership.",
            "Events capture state changes for analytics and agents.",
            "Sensitive data carries classification and retention rules."])
    if has("integration", "interface", "interop"):
        return bullets([
            "Event-driven integration with idempotent consumers.",
            "Governed APIs (OpenAPI) and MCP tools for system access.",
            "Retry, back-off and dead-letter handling for resilience.",
            "Monitoring and alerting on every integration."])
    if has("governance", "oversight", "control model"):
        return bullets([
            "Risk-tiered oversight aligned to ISO 42001 and NIST AI RMF.",
            "Human-in-the-loop for high-impact decisions.",
            "Audit trails, evaluation gates and model documentation.",
            "Clear ownership, approval and escalation paths."])
    if has("agent", "portfolio") and phase not in ("Phase 05",):
        return table(["Agent", "Role", "Authority", "Human Approval"],
                     [["Orchestrator", "Plans and delegates", "Coordinate",
                       "For high-risk plans"],
                      ["Specialist agents", "Execute scoped tasks",
                       "Least-privilege", "For risky actions"],
                      ["Reviewer agent", "Validates outputs", "Read/assess", "N/A"]])
    if has("automation", "workflow"):
        return bullets([
            "Identify repeatable, rules-based steps to automate.",
            "Combine deterministic steps with AI-agent steps for reliability.",
            "Add human approval checkpoints for high-risk actions.",
            "Instrument cost, success rate and audit trails."])
    if has("cost", "pricing", "licensing", "budget"):
        return bullets([
            "Model/compute (token) costs — align to actual usage.",
            "Platform, data and integration costs.",
            "Run and oversight costs (human-in-the-loop, monitoring).",
            "Track against budget and optimise continuously (FinOps)."])
    if has("roi", "return on investment", "value realisation", "business value"):
        return bullets([
            "Cost savings from automation and efficiency.",
            "Revenue uplift from better experience and decisions.",
            "Payback period and net benefit per initiative.",
            "Baseline before deployment and measure the delta."])
    if has("change management", "adoption", "enablement", "training"):
        return bullets([
            "Engage stakeholders and communicate early and often.",
            "Train teams and redesign processes around AI plus humans.",
            "Pilot, measure and scale what works.",
            "Manage expectations with transparent metrics."])
    if has("monitoring", "observability", "telemetry"):
        return bullets([
            "Emit metrics, logs and traces (OpenTelemetry).",
            "Alert on SLOs and symptoms, not noise.",
            "Dashboards for key services, with runbooks linked."])
    if has("testing", "quality", "evaluation") and "model" not in n:
        return bullets([
            "Automated tests proportional to risk, gating merges.",
            "Evaluation of AI quality and safety before release.",
            "Continuous measurement and regression detection."])
    if has("support", "maintenance", "operations runbook", "run book"):
        return bullets([
            "Defined SLAs, on-call and escalation.",
            "Runbooks for common operational tasks.",
            "Knowledge base and AI-assisted support with oversight."])
    if has("ecosystem", "marketplace", "partner"):
        return bullets([
            "Reusable, versioned, well-documented assets.",
            "Clear contribution, review and certification process.",
            "Security and licence due diligence for third-party assets."])
    if has("certification", "exam", "curriculum", "competency"):
        return bullets([
            "Defined competencies mapped to the relevant skills.",
            "Assessment via knowledge checks and practical tasks.",
            "Recertification on a defined cadence."])
    if has("stakeholder", "audience", "persona"):
        return bullets([
            "Executives and sponsors (value and risk).",
            "Delivery teams (build and operate).",
            "Governance, security and compliance functions.",
            "End users and AI agents that consume this artefact."])
    if has("principle", "tenet", "philosophy"):
        return bullets(["AI First", "Security by Design", "Privacy by Design",
                        "Zero Trust", "Documentation as Code", "Human-in-the-Loop"])
    if has("forbidden", "prohibited", "not allowed", "out-of-bounds"):
        return bullets([
            "Taking irreversible or high-risk actions without human approval.",
            "Accessing data or systems outside granted least-privilege scope.",
            "Spending beyond defined cost/loop limits.",
            "Bypassing guardrails, logging or audit."])
    if has("allowed decision", "permitted", "in-scope decision", "can decide"):
        return bullets([
            "Low-risk, reversible actions within the granted scope.",
            "Drafting, analysis and recommendations for human review.",
            "Routine tasks explicitly delegated to the agent."])
    if has("authority", "boundaries", "permission", "delegation"):
        return bullets([
            "Authority is explicit, least-privilege and scoped to the task.",
            "Allowed: low-risk, reversible actions within scope.",
            "Requires approval: high-risk, irreversible or external actions.",
            "All actions are logged and auditable."])
    if has("approval", "sign-off", "sign off"):
        return bullets([
            "Required before any irreversible or high-risk action.",
            "Required before external or customer-facing communications.",
            "Required before financial or regulated decisions.",
            "Captured with identity, timestamp and rationale."])
    if has("escalation"):
        return bullets([
            "Owner -> domain lead -> Governance Division.",
            "Severity-based timelines for response.",
            "Clear hand-off with full context and audit trail."])
    if has("collaboration", "handoff", "hand-off", "communication", "coordination",
           "protocol", "interaction model"):
        return bullets([
            "An orchestrator delegates tasks to specialist agents/teams.",
            "Context and decisions are shared through governed memory.",
            "Hand-offs carry full context and an audit trail.",
            "Conflicts follow a defined resolution path."])
    if has("memory", "context management", "state management", "knowledge sharing"):
        return bullets([
            "Short-term working context for the active task.",
            "Governed long-term memory for reuse, with access control.",
            "Provenance and freshness tracked for grounding."])
    if has("orchestration", "routing", "workflow overview"):
        return bullets([
            "A planner decomposes goals into steps.",
            "Deterministic and agent steps are combined for reliability.",
            "Human checkpoints gate high-risk steps.",
            "Results are aggregated, validated and recorded."])
    if has("failure", "recovery", "fallback", "exception", "error handling",
           "resilience"):
        return bullets([
            "Detect, capture and classify the error with context.",
            "Apply a safe fallback or stop safely.",
            "Retry idempotently where safe; otherwise escalate.",
            "Open an incident if customer impact is possible."])
    if has("guardrail", "safety control", "safeguard"):
        return bullets([
            "Input and output filtering (PII, toxicity, injection).",
            "Schema/format validation of outputs.",
            "Action gating with human-in-the-loop for high risk.",
            "Monitoring, evaluation and incident response."])
    if has("trigger", "event"):
        return bullets([
            "A request or task is submitted.",
            "A scheduled cycle or threshold is reached.",
            "An upstream event or signal is received."])
    if has("input"):
        return bullets([
            "The request/context that initiated the work.",
            "Relevant data, artefacts and configuration.",
            "Applicable rules, standards and prior decisions."])
    if has("output", "deliverable"):
        return bullets([
            "The validated result of the work.",
            "Evidence and an audit trail.",
            "Follow-up actions and updated cross-references."])
    if has("role", "persona", "responsib"):
        return bullets([
            "Owner — accountable for this artefact/workflow.",
            "Contributors — execute within their authority (human or AI).",
            "Reviewers/Approvers — validate and sign off.",
            "Governance — oversee risk, security and compliance."])
    if has("prerequisite", "precondition", "entry criteria"):
        return bullets([
            "Required inputs, access and approvals are available.",
            "Relevant rules, standards and checklists are known.",
            "The work item is well-formed enough to proceed."])
    if has("tool", "technology", "platform", "tooling"):
        return bullets([
            "Cloud-native services and managed platforms.",
            "Git, CI/CD and Infrastructure as Code.",
            "AI tooling: model providers, RAG and MCP servers.",
            "Observability and security-scanning tooling."])
    if has("metric", "kpi", "measure", "success"):
        return bullets([
            "Adoption and coverage.",
            "Quality and validation pass rate.",
            "Cycle time and efficiency.",
            "Business outcome versus target."])
    if has("non-functional", "nonfunctional"):
        return bullets([
            "Performance: defined latency/throughput targets (p95/p99).",
            "Reliability: availability SLOs and error budgets.",
            "Security and privacy by design.",
            "Scalability, maintainability and accessibility (WCAG 2.2 AA)."])
    if has("functional requirement"):
        return bullets([
            "The capability MUST deliver its defined user/business outcomes.",
            "Inputs are validated; outputs are correct and consistent.",
            "Errors and edge cases are handled gracefully.",
            "Behaviour is covered by tests."])
    if has("organis", "organiz", "team structure", "org chart", "required teams"):
        return bullets([
            "Cross-functional teams aligned to value streams.",
            "Clear ownership, RACI and decision rights.",
            "A centre of excellence sets standards; teams deliver.",
            "Human roles augmented by AI agents under oversight."])
    if has("mission"):
        return (f"To operate {title} to a consistent, enterprise-grade standard that "
                "delivers measurable value while balancing autonomy with human "
                "oversight.")
    if has("okr"):
        return bullets(["Objective: raise enterprise consistency and value.",
                        "Key result: 95%+ validation pass rate.",
                        "Key result: measurable reuse and cycle-time reduction."])
    if has("context strategy", "context"):
        return bullets([
            "Ground responses in approved, current sources (RAG).",
            "Manage short-term working context and long-term memory.",
            "Track provenance and freshness; enforce access control."])
    if has("scenario", "business case", "example use"):
        return bullets([
            f"A representative {title.lower()} situation and its goals.",
            "The actors, triggers and expected outcome.",
            "How AIBOS standards and agents apply, with human oversight."])
    if has("repository structure", "folder layout", "repo structure", "project layout"):
        return fenced("text", "project/\n  src/        # application code\n"
                              "  infra/      # infrastructure as code\n"
                              "  docs/       # documentation\n"
                              "  tests/      # automated tests\n"
                              "  .github/    # CI/CD workflows")
    if has("deployment", "release model"):
        return bullets([
            "Automated, versioned, traceable deployments via CI/CD.",
            "Progressive delivery (canary/blue-green) for risky changes.",
            "Post-deploy health checks with automatic rollback."])
    if has("infrastructure"):
        return bullets([
            "Cloud-native, defined as code (Terraform/Pulumi).",
            "Containerised workloads with orchestration.",
            "Managed data, networking and security services.",
            "Observability and cost controls built in."])
    if has("ai component", "ml component", "model component"):
        return bullets([
            "LLM/model providers via a gateway.",
            "RAG pipeline: ingestion, retrieval and grounding.",
            "Evaluation and guardrails.",
            "Agent framework with tracing and tool (MCP) access."])
    if has("data flow", "dataflow"):
        return bullets([
            "Sources -> ingestion/validation -> storage.",
            "Retrieval/embedding for AI grounding.",
            "Processing and serving to apps and agents.",
            "Telemetry and audit captured throughout."])
    if has("api contract", "api spec", "endpoints", "commands/api", "commands", "cli"):
        return bullets([
            "Contracts described by OpenAPI (or typed CLI help).",
            "Versioned with a clear deprecation policy.",
            "AuthN/AuthZ, validation and consistent errors.",
            "Documented with examples for humans and agents."])
    if has("config"):
        return bullets([
            "Configuration via environment, separate from code (Twelve-Factor).",
            "Validated at startup; safe, documented defaults.",
            "No secrets in config — use a secrets manager."])
    if has("secret"):
        return bullets([
            "Stored in a managed secrets manager, never in code/config.",
            "Injected at runtime; rotated on schedule and on compromise.",
            "Least-privilege access, audited; CI secret-scanning enabled."])
    if has("logging", "log strategy"):
        return bullets([
            "Structured, centralised logs with correlation IDs.",
            "No secrets or unmasked PII in logs.",
            "Retention aligned to policy; security events captured."])
    if has("alert"):
        return bullets([
            "Alert on SLOs and symptoms, not noise.",
            "Every alert is actionable with a linked runbook.",
            "Severity-based routing to on-call."])
    if has("rollback"):
        return bullets([
            "A tested rollback path restores a known-good version.",
            "Database changes are backward compatible.",
            "Rollback is fast and may be automated on failed health checks."])
    if has("scalab", "capacity"):
        return bullets([
            "Stateless, horizontally scalable services.",
            "Caching, queues and autoscaling for load.",
            "Performance budgets and load testing."])
    if has("implementation phase", "phases", "milestone", "sprint plan"):
        return table(["Phase", "Focus", "Outcome"],
                     [["Phase 1", "Foundations and a pilot", "Validated value"],
                      ["Phase 2", "Harden and integrate", "Production rollout"],
                      ["Phase 3", "Scale across the portfolio", "Broad adoption"]])
    if has("migration"):
        return bullets([
            "Assess current state and define target state.",
            "Migrate incrementally with backward compatibility.",
            "Validate at each step; keep a rollback path."])
    if has("risk"):
        return bullets(["Scope drift and unclear ownership.",
                        "Weak data foundations or access.",
                        "Insufficient oversight on high-risk actions.",
                        "Change resistance and adoption gaps."])
    if has("business model", "commercial model", "revenue", "monetis", "monetiz"):
        return bullets([
            "Clear value proposition and target customers.",
            "Pricing aligned to a value metric.",
            "Cost structure and margin understood.",
            "Growth and retention levers identified."])
    if has("dashboard", "reporting"):
        return bullets([
            "Executive view of outcomes and KPIs.",
            "Operational view of health and throughput.",
            "Governance view of risk, security and compliance."])
    if has("version"):
        return bullets([
            "Semantic Versioning (MAJOR.MINOR.PATCH).",
            "Backward compatibility within a major version.",
            "Documented deprecation policy and changelog."])
    if has("dependency", "dependencies"):
        return bullets([
            "Pin and scan dependencies (SCA) for vulnerabilities.",
            "Keep dependencies patched and minimal.",
            "Track licences and provenance (SBOM)."])
    if has("signature", "signing"):
        return bullets([
            "Sign artefacts and verify provenance.",
            "Use strong, standard cryptography and managed keys.",
            "Reject unsigned or tampered artefacts."])
    if has("trust model"):
        return bullets([
            "Zero Trust: never trust, always verify.",
            "Identity as the perimeter; least privilege.",
            "Assume breach; segment and limit blast radius."])
    if has("authentication", "authn"):
        return bullets([
            "Standard protocols (OIDC/OAuth 2.1).",
            "MFA for privileged access; strong password hashing.",
            "Short-lived, scoped tokens; session revocation."])
    if has("authoris", "authoriz", "access control"):
        return bullets([
            "Least privilege, deny by default, server-side checks.",
            "RBAC/ABAC modelled explicitly.",
            "Privileged actions audited; periodic access reviews."])
    if has("extension", "extensib", "plugin", "customis", "customiz"):
        return bullets([
            "Well-defined extension points and stable interfaces.",
            "Versioned contracts and backward compatibility.",
            "Sandboxing and least privilege for extensions."])
    if has("compatib"):
        return bullets([
            "Backward compatibility within a major version.",
            "Deprecations announced with a migration path.",
            "Contract tests guard against breakage."])
    if has("performance", "latency", "throughput"):
        return bullets([
            "Defined performance budgets/SLAs (p95/p99).",
            "Load and stress testing before major releases.",
            "Profiling and caching to remove bottlenecks."])
    if has("decision logic", "decision criteria", "rules engine"):
        return bullets([
            "Decisions are explicit, explainable and auditable.",
            "High-risk or ambiguous cases route to humans.",
            "Logic is versioned and tested."])
    if has("eligibilit", "entry requirement"):
        return bullets([
            "Open to the relevant roles meeting the prerequisites.",
            "Foundational knowledge of the domain is assumed.",
            "No prior certification required for the entry level."])
    if has("learning objective", "outcomes of learning"):
        return bullets([
            "Understand the core concepts and standards.",
            "Apply them to realistic tasks safely.",
            "Demonstrate competence through assessment."])
    if has("continuous improvement", "feedback loop", "improvement loop", "kaizen"):
        return bullets([
            "Capture metrics, incidents and feedback.",
            "Review on a regular cadence and prioritise improvements.",
            "Update artefacts and re-measure the impact."])
    if has("developer value", "user value", "value proposition", "benefit"):
        return bullets([
            "Faster delivery through reuse and automation.",
            "Higher quality and consistency by default.",
            "Lower risk via built-in security and governance."])
    if has("security"):
        return bullets([
            "Secure by design; Zero Trust and least privilege.",
            "Protect data in transit and at rest (strong crypto).",
            "Validate inputs; scan code, dependencies and secrets.",
            "Log security events; monitor and respond to incidents."])
    if has("knowledge area", "syllabus", "curriculum", "topics covered"):
        return bullets([
            "Core concepts and the AIBOS standards.",
            "Practical application to realistic tasks.",
            "Security, privacy, governance and oversight.",
            "AI-specific quality, evaluation and safety."])
    if has("practical assessment", "assessment", "exam"):
        return bullets([
            "A mix of knowledge checks and hands-on tasks.",
            "Scenario-based problems reflecting real work.",
            "Assessed against an objective rubric."])
    if has("passing criteria", "pass mark", "grading"):
        return bullets([
            "A defined minimum score (e.g. 70%+).",
            "Critical-competency items must be passed.",
            "Results recorded with evidence."])
    if has("evidence requirement", "evidence"):
        return bullets([
            "Verifiable artefacts demonstrating competence.",
            "Provenance and authorship are attributable.",
            "Retained per the records-retention policy."])
    if has("scoring rubric", "rubric", "marking"):
        return table(["Level", "Descriptor"],
                     [["Exceeds", "Mastery beyond requirements."],
                      ["Meets", "Competent and reliable."],
                      ["Developing", "Partial; needs improvement."],
                      ["Not met", "Does not meet the standard."]])
    if has("renewal", "recert", "cpd", "continuing"):
        return bullets([
            "Recertify on a defined cadence (e.g. every 2 years).",
            "Evidence of continuing professional development.",
            "Re-assessment against the current standard."])
    if has("audit"):
        return bullets([
            "Maintain complete, tamper-evident audit trails.",
            "Independent review on a defined schedule.",
            "Findings tracked to closure with owners."])
    if has("maturity"):
        return table(["Level", "Indicator"],
                     [["1 Initial", "Ad hoc, inconsistent."],
                      ["2 Managed", "Repeatable, documented."],
                      ["3 Defined", "Standardised across teams."],
                      ["4 Measured", "Quantitatively managed."],
                      ["5 Optimising", "Continuously improving."]])
    if has("improvement guidance", "guidance", "recommendation"):
        return bullets([
            "Prioritise gaps by risk and value.",
            "Adopt the relevant skills, rules and playbooks.",
            "Re-measure after each change to confirm impact."])
    if has("handover", "hand over", "handover rules", "transition"):
        return bullets([
            "Hand-offs carry complete context and current state.",
            "Ownership and next actions are explicit.",
            "An audit trail records the transition."])
    if has("team"):
        return bullets([
            "Cross-functional teams aligned to value streams.",
            "Clear ownership and decision rights (RACI).",
            "Human roles augmented by AI agents under oversight."])

    # Final, still-useful default (no generic placeholder).
    return (f"This section establishes the **{name}** for **{title}** within "
            f"{phase}, aligned to the AIBOS root standards. It is implemented through "
            "the related skills, rules, checklists, playbooks and templates, with "
            "automation where practical and human oversight for high-risk actions. "
            f"See the [repository catalogue]({lr('ROOT_INDEX.md')}) and the "
            f"[root standards]({lr('00_ROOT')}).")


def render(out_path: Path, doc_id, title, doc_type, category, phase, owner,
           sections, tags) -> str:
    num = int(phase.split()[1])
    from_dir = out_path.parent

    def lr(t):
        return rellink(from_dir, ROOT / t)

    def ld(p):
        return rellink(from_dir, OUT / PHASE_DIR[p] / "README.md")

    def link_prompt():
        return rellink(from_dir, ROOT / "01_PHASES" / PHASE_PROMPT[num])

    ctx = {"title": title, "phase": phase, "owner": owner, "num": num,
           "link_root": lr, "link_dir": ld, "link_prompt": link_prompt}

    related = ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md",
               f"01_PHASES/{PHASE_PROMPT[num]}"]
    nav = ("> **Navigate:** "
           f"[Home]({lr('README.md')}) · "
           f"[Catalogue]({lr('ROOT_INDEX.md')}) · "
           f"[Generated Index]({rellink(from_dir, OUT / 'README.md')}) · "
           f"[Phase {num:02d} Prompt]({link_prompt()})")

    parts = [front_matter(doc_id, title, doc_type, category, phase, owner, tags,
                          related), "", f"# {title}", "", nav, ""]
    for s in sections:
        parts.append(f"## {s}")
        parts.append("")
        parts.append(build_section(s, ctx).strip())
        parts.append("")
    text = "\n".join(parts)
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
    return text


def write(path: Path, content: str, overwrite: bool, stats: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        stats["skipped"] += 1
        return
    path.write_text(content, encoding="utf-8")
    stats["written"] += 1


# --------------------------------------------------------------------------- #
# Folder index (README.md) generation
# --------------------------------------------------------------------------- #
def build_indexes(stats: dict) -> None:
    for dirpath, dirnames, filenames in os.walk(OUT):
        d = Path(dirpath)
        dirnames.sort()
        subdirs = sorted(n for n in dirnames)
        md_files = sorted(f for f in filenames
                          if f.endswith(".md") and f != "README.md")
        if not subdirs and not md_files:
            continue

        title = "Generated Artefacts" if d == OUT else display(d.name)
        parts = [f"# {title} — Index", ""]

        # Navigation
        up = rellink(d, (ROOT / "README.md") if d == OUT
                     else (d.parent / "README.md"))
        nav = (f"> **Navigate:** [Up]({up}) · "
               f"[Catalogue]({rellink(d, ROOT / 'ROOT_INDEX.md')}) · "
               f"[Generated Index]({rellink(d, OUT / 'README.md')})")
        parts += [nav, ""]

        if d == OUT:
            parts += ["This folder contains the artefacts generated from the "
                      "Phase master prompts. Browse by phase below.", ""]

        if subdirs:
            parts.append("## Sections")
            parts.append("")
            parts.append(bullets(
                [f"[{display(s)}]({s}/README.md)" for s in subdirs]))
            parts.append("")

        if md_files:
            parts.append("## Documents")
            parts.append("")
            parts.append(bullets([f"[{display(f)}]({f})" for f in md_files]))
            parts.append("")

        text = re.sub(r"\n{3,}", "\n\n", "\n".join(parts)).rstrip() + "\n"
        (d / "README.md").write_text(text, encoding="utf-8")
        stats["indexes"] += 1


# --------------------------------------------------------------------------- #
# Section sets per phase
# --------------------------------------------------------------------------- #
S = {
    1: ["Executive Summary", "Purpose", "Scope", "Objectives", "Stakeholders",
        "Business Value", "Architecture", "Guiding Principles", "Standards Mapping",
        "Risks", "Assumptions", "Dependencies", "Acceptance Criteria",
        "Validation Checklist", "References", "Version History"],
    2: ["Executive Summary", "Purpose", "Vision", "Scope", "Business Objectives",
        "Stakeholders", "Architecture Principles", "Governance Model",
        "Roles and Responsibilities", "Standards Mapping", "Dependencies",
        "Quality Gates", "KPIs", "Risks", "Mitigations", "Acceptance Criteria",
        "Validation Checklist", "References", "Version History"],
    3: ["Executive Summary", "Vision", "Mission", "Business Purpose", "Scope",
        "Responsibilities", "Organisational Structure", "Leadership Roles", "Teams",
        "Collaboration Matrix", "Upstream Dependencies", "Downstream Consumers",
        "KPIs", "OKRs", "Quality Gates", "Required Skills", "Applicable Rules",
        "Applicable Checklists", "Applicable Playbooks", "Security Responsibilities",
        "Compliance Responsibilities", "AI Responsibilities", "Reporting Structure",
        "Decision Authority", "Escalation Path", "Risks", "Mitigations",
        "Acceptance Criteria", "Validation Checklist", "References", "Version History"],
    4: ["Executive Summary", "Department Mission", "Vision", "Business Purpose",
        "Scope", "Services Provided", "Services Consumed", "Responsibilities",
        "Organisational Structure", "Required Specialist Roles", "Required Skills",
        "Department KPIs", "Department OKRs", "Decision Authority", "Escalation Path",
        "Collaboration Matrix", "Required Rules", "Required Checklists",
        "Required Playbooks", "Required Templates", "Security Responsibilities",
        "AI Responsibilities", "Compliance Responsibilities", "Risks", "Mitigations",
        "Acceptance Criteria", "Validation Checklist", "References", "Version History"],
    5: ["Executive Summary", "Mission", "Vision", "Role Purpose", "Scope",
        "Responsibilities", "Out of Scope", "Services Provided", "Services Consumed",
        "Required Technical Skills", "Required Business Skills", "Required AI Skills",
        "Required Soft Skills", "Required Certifications", "Recommended Learning Path",
        "Required Tools", "Technology Stack", "Decision Authority",
        "Collaboration Matrix", "RACI", "Required Rules", "Required Checklists",
        "Required Playbooks", "Required Templates", "Required Knowledge Articles",
        "KPIs", "OKRs", "Security Responsibilities", "AI Responsibilities",
        "Compliance Responsibilities", "Risks", "Anti-patterns", "Best Practices",
        "Definition of Done", "Deliverables", "Acceptance Criteria",
        "Validation Checklist", "Interview Questions", "Self Assessment Matrix",
        "References", "Version History"],
    6: ["Executive Summary", "Purpose", "Scope", "Business Rationale",
        "Technical Rationale", "Definitions", "Mandatory Requirements (MUST)",
        "Recommended Practices (SHOULD)", "Optional Practices (MAY)",
        "Rule Ownership Matrix", "Applicable Departments", "Applicable Skills",
        "Related Rules", "Related Checklists", "Related Playbooks",
        "Related Templates", "Related Knowledge Articles", "Security Considerations",
        "Privacy Considerations", "AI Considerations", "Compliance Requirements",
        "Exceptions Process", "Approval Authority", "Enforcement Model", "Metrics",
        "KPIs", "Risks", "Anti-patterns", "Best Practices", "Acceptance Criteria",
        "Validation Checklist", "References", "Version History"],
    7: ["Purpose", "Scope", "Prerequisites", "Inputs", "Outputs",
        "Roles Responsible", "Quality Gate", "Acceptance Criteria",
        "Validation Steps", "Pass / Fail Criteria", "Evidence Required",
        "Required Skills", "Required Rules", "Related Playbooks", "Related Templates",
        "Related Knowledge Articles", "Security Validation", "Privacy Validation",
        "AI Validation", "Compliance Validation", "Accessibility Validation",
        "Performance Validation", "Deployment Readiness", "Rollback Readiness",
        "Reviewer Sign-off", "Escalation Process", "Risks", "References",
        "Version History"],
    8: ["Executive Summary", "Business Objective", "Scope", "Trigger Conditions",
        "Preconditions", "Inputs", "Outputs", "Roles Responsible",
        "AI Agents Involved", "Human Approval Points", "Workflow Overview",
        "Mermaid Workflow Diagram", "Step-by-Step Procedure", "Decision Branches",
        "Exception Handling", "Escalation Path", "Required Skills", "Required Rules",
        "Required Checklists", "Required Templates", "Required Knowledge Articles",
        "Automation Opportunities", "Integration Points", "KPIs", "SLAs", "Risks",
        "Best Practices", "Anti-patterns", "Definition of Done", "Acceptance Criteria",
        "Post-Implementation Review", "Continuous Improvement", "Validation Checklist",
        "References", "Version History"],
    9: ["Purpose", "When to Use", "Audience", "Inputs Required", "Outputs Produced",
        "Required Metadata", "Placeholder Definitions", "Naming Convention",
        "Folder Convention", "Required Skills", "Required Rules", "Required Checklists",
        "Required Playbooks", "Required Knowledge Articles", "Validation Rules",
        "Quality Criteria", "Example Completed Template", "JSON Schema", "YAML Schema",
        "AI Prompt Usage Guidance", "Automation Compatibility", "Version History"],
    10: ["Executive Summary", "Purpose", "Scope", "Core Concepts", "Definitions",
         "Business Context", "Technical Context", "Best Practices", "Anti-patterns",
         "Design Patterns", "Examples", "FAQs", "Decision Tree", "Learning Path",
         "Prerequisites", "Related Skills", "Related Rules", "Related Checklists",
         "Related Playbooks", "Related Templates", "Related Knowledge",
         "Department Ownership", "Division Ownership", "External Standards",
         "References", "AI Retrieval Metadata", "Suggested Chunk Boundaries",
         "Suggested Embedding Keywords", "Version History"],
    11: ["Purpose", "Scope", "Agent Persona", "Responsibilities",
         "Authority Boundaries", "Allowed Decisions", "Forbidden Decisions",
         "Human Approval Points", "Inputs", "Outputs", "Memory Strategy",
         "Context Strategy", "Tool Permissions", "External Integrations",
         "Communication Protocol", "Handover Rules", "Collaboration Matrix",
         "Escalation Path", "Failure Recovery", "Error Handling", "Observability",
         "Cost Optimisation", "Security Controls", "Privacy Controls",
         "Compliance Requirements", "KPIs", "Quality Metrics", "Validation Checklist",
         "References", "Version History"],
    12: ["Executive Summary", "Purpose", "Scope", "Business Value", "Trigger Events",
         "Inputs", "Outputs", "Workflow Description", "Mermaid Diagram",
         "AI Agents Involved", "Human Approval Points", "Automation Opportunities",
         "Tool Integrations", "Required Skills", "Governing Rules",
         "Required Checklists", "Supporting Playbooks", "Required Templates",
         "Knowledge Dependencies", "Monitoring Strategy", "Alerting Strategy",
         "Metrics", "KPIs", "SLAs/SLOs", "Error Handling", "Rollback Strategy",
         "Security Controls", "Privacy Controls", "Compliance Mapping",
         "Cost Optimisation", "Continuous Improvement Loop", "Validation Checklist",
         "References", "Version History"],
    13: ["Executive Summary", "Business Challenges", "Business Goals",
         "AI Opportunities", "Recommended AI Use Cases", "AI Agent Portfolio",
         "Business Capability Map", "Target Operating Model", "Reference Architecture",
         "Technology Stack", "Data Sources", "Integration Patterns",
         "Security Controls", "Privacy Controls", "Compliance Mapping",
         "Governance Model", "Required Skills", "Required Rules", "Required Checklists",
         "Required Playbooks", "Required Templates", "Knowledge Dependencies", "KPIs",
         "ROI Metrics", "Cost Considerations", "Risks", "Adoption Roadmap",
         "Change Management", "Mermaid Architecture Diagrams", "Validation Checklist",
         "References", "Version History"],
    14: ["Executive Summary", "Business Problem", "Business Outcome",
         "Target Audience", "Prerequisites", "Implementation Phases",
         "30/60/90 Day Roadmap", "Architecture Overview", "Required Teams",
         "Required AI Agents", "Required Skills", "Required Rules",
         "Required Checklists", "Required Playbooks", "Required Templates",
         "Required Knowledge Articles", "Required Industry Blueprints",
         "Technology Stack", "Infrastructure", "Security Controls",
         "Compliance Requirements", "Automation Opportunities", "Integration Map",
         "Migration Strategy", "Change Management Plan", "Success Metrics",
         "KPI Dashboard", "ROI Model", "Cost Estimate", "Risk Register",
         "Validation Checklist", "Deliverables", "Definition of Done",
         "Version History"],
    15: ["Purpose", "Scope", "Business Scenario", "Functional Requirements",
         "Non-functional Requirements", "Architecture Overview",
         "Mermaid Architecture Diagrams", "Repository Structure", "Folder Layout",
         "Technology Stack", "Deployment Model", "Infrastructure Components",
         "Security Controls", "AI Components", "Data Flow", "Integration Flow",
         "API Contracts", "Configuration Strategy", "Secrets Strategy",
         "Monitoring Strategy", "Logging Strategy", "Testing Strategy",
         "Scalability Strategy", "Disaster Recovery", "Cost Optimisation",
         "Required Skills", "Required Rules", "Required Checklists",
         "Required Playbooks", "Required Templates", "Required Knowledge",
         "Related Industry Blueprints", "Validation Checklist", "References",
         "Version History"],
    16: ["Executive Summary", "Purpose", "Scope", "Business Value", "Developer Value",
         "Functional Requirements", "Non-functional Requirements",
         "Public Interfaces", "Commands/APIs", "Configuration Model",
         "Authentication", "Authorisation", "Extension Points", "Plugin Architecture",
         "Versioning Strategy", "Backward Compatibility", "Error Handling",
         "Observability", "Security Controls", "Privacy Controls",
         "Performance Targets", "Testing Strategy", "CI/CD Integration",
         "Required Skills", "Required Rules", "Required Checklists",
         "Required Playbooks", "Required Templates", "Required Knowledge",
         "Sample Usage", "Mermaid Diagrams", "Validation Checklist", "References",
         "Version History"],
    17: ["Purpose", "Scope", "Target Audience", "Eligibility", "Learning Objectives",
         "Competency Framework", "Knowledge Areas", "Required Skills", "Required Rules",
         "Required Checklists", "Required Playbooks", "Required Templates",
         "Required Knowledge", "Assessment Blueprint", "Practical Assessments",
         "Passing Criteria", "Evidence Requirements", "Scoring Rubric",
         "Renewal Requirements", "CPD Requirements", "Audit Requirements",
         "Compliance Mapping", "Maturity Indicators", "Improvement Guidance",
         "Metrics", "Validation Checklist", "References", "Version History"],
    18: ["Purpose", "Scope", "Supported Package Types", "Metadata Schema",
         "Package Manifest", "Semantic Versioning Strategy", "Compatibility Matrix",
         "Dependency Management", "Publishing Workflow", "Validation Workflow",
         "Review Workflow", "Approval Process", "Digital Signature Requirements",
         "Security Requirements", "Trust Model", "Licensing Options",
         "Commercial Model", "Required Skills", "Required Rules", "Required Checklists",
         "Required Playbooks", "Required Templates", "Required Knowledge",
         "API Interfaces", "CLI Integration", "SDK Integration",
         "Marketplace Search Metadata", "KPIs", "Success Metrics",
         "Validation Checklist", "References", "Version History"],
    19: ["Executive Summary", "Purpose", "Scope", "Organisational Context",
         "Business Model", "Organisation Chart", "Mermaid Diagrams", "Team Structure",
         "AI Agent Structure", "Roles and Responsibilities", "RACI", "Governance",
         "Decision Matrix", "Escalation Model", "Skills Mapping", "Rules Mapping",
         "Checklists Mapping", "Playbooks Mapping", "Templates Mapping",
         "Knowledge Mapping", "Automation Mapping", "Marketplace Assets", "SDK Usage",
         "CI/CD Integration", "Security Controls", "Compliance Controls", "KPIs",
         "OKRs", "Dashboards", "Risks", "Continuous Improvement",
         "Validation Checklist", "References", "Version History"],
    20: ["Executive Summary", "Purpose", "Scope", "Business Value", "Responsibilities",
         "Inputs", "Outputs", "Decision Logic", "Human Approval Gates",
         "AI Agents Involved", "Memory Strategy", "Context Strategy",
         "Governance Model", "Security Controls", "Privacy Controls",
         "Compliance Mapping", "Tool Integrations", "Event Triggers", "KPIs", "SLOs",
         "Error Recovery", "Escalation Strategy", "Continuous Improvement Loop",
         "Related Skills", "Related Rules", "Related Checklists", "Related Playbooks",
         "Related Templates", "Related Knowledge", "Mermaid Diagrams",
         "Validation Checklist", "References", "Version History"],
}


# --------------------------------------------------------------------------- #
# Phase data
# --------------------------------------------------------------------------- #
PHASE1 = ["Enterprise Vision", "Business Capabilities", "Operating Model",
          "Organisation Structure", "Enterprise Architecture", "Domain Model",
          "Capability Map", "Repository Architecture", "Document Hierarchy",
          "Governance Model", "Decision Framework", "RACI Framework",
          "Quality Gate Architecture", "AI Collaboration Architecture",
          "Security Architecture", "Information Architecture", "Metadata Standard",
          "Versioning Standard", "Document Lifecycle", "Enterprise Roadmap"]

PHASE2 = ["AIBOS Specification", "ASFE Specification", "AIAE Specification",
          "AICE Specification", "Enterprise Governance Specification",
          "Security Specification", "AI Governance Specification",
          "Document Standard Specification", "Quality Framework Specification",
          "Knowledge Base Specification"]

PHASE3 = ["Executive Division", "Product Division", "Engineering Division",
          "AI Division", "Data Division", "Security Division", "Cloud Division",
          "DevOps Division", "QA Division", "UX Division", "Marketing Division",
          "Sales Division", "Customer Success Division", "Finance Division",
          "Legal Division", "Operations Division", "HR Division", "Research Division",
          "Innovation Division", "Governance Division"]

PHASE4 = {
    "Executive": ["Strategy", "Portfolio Management", "PMO", "Business Excellence"],
    "Product": ["Product Management", "Product Design", "Product Analytics", "Roadmap"],
    "Engineering": ["Frontend", "Backend", "API", "Architecture", "Integration",
                    "Platform Engineering"],
    "AI": ["Prompt Engineering", "LLM Engineering", "RAG Engineering",
           "Agent Engineering", "MCP Engineering", "AI Evaluation", "AI Safety"],
    "Data": ["Data Engineering", "Analytics", "BI", "Data Science", "ML Engineering"],
    "Security": ["Application Security", "Cloud Security", "IAM", "Privacy",
                 "Compliance", "Risk"],
    "Cloud_And_DevOps": ["Cloud Platform", "Infrastructure", "DevOps", "DevSecOps",
                         "SRE", "Observability"],
    "Quality": ["QA", "Test Automation", "Performance", "Accessibility"],
    "Marketing": ["SEO", "AEO", "GEO", "Content", "Growth", "Community"],
    "Sales": ["Pre-Sales", "Sales Engineering", "Account Management", "Partnerships"],
    "Customer_Success": ["Implementation", "Support", "Training", "Customer Success"],
    "Finance": ["Accounting", "Commercial", "Procurement"],
    "Legal": ["Contracts", "Licensing", "IP", "Regulatory"],
    "Operations": ["Service Delivery", "Release Management", "Incident Management",
                   "Knowledge Management"],
    "Research": ["Innovation", "Emerging Technology", "Standards"],
}

PHASE5_ROLES = [
    "Executive Leadership", "Product Manager", "Product Designer", "Enterprise Architect",
    "Solution Architect", "Frontend Engineer", "Backend Engineer", "API Engineer",
    "Integration Engineer", "Platform Engineer", "Cloud Engineer",
    "Infrastructure Engineer", "DevOps Engineer", "DevSecOps Engineer",
    "Site Reliability Engineer", "Security Engineer", "Privacy Engineer",
    "Compliance Specialist", "QA Engineer", "Performance Engineer",
    "Accessibility Specialist", "Prompt Engineer", "LLM Engineer", "RAG Engineer",
    "Agent Engineer", "MCP Engineer", "AI Evaluation Engineer", "AI Safety Engineer",
    "ML Engineer", "Data Engineer", "Analytics Engineer", "BI Analyst",
    "Data Scientist", "SEO Specialist", "AEO Specialist", "GEO Specialist",
    "Content Strategist", "Growth Marketer", "Sales Engineer", "Account Manager",
    "Customer Success Manager", "Support Engineer", "Finance Analyst",
    "Legal Counsel", "Operations Manager", "Knowledge Manager", "Research Scientist",
    "Innovation Lead",
]

PHASE6 = {
    "Governance": ["Decision Making", "Change Management", "Risk Management",
                   "Document Governance"],
    "Engineering": ["Coding Standards", "Architecture Standards", "API Standards",
                    "Database Standards", "Integration Standards", "Version Control",
                    "Branching Strategy", "Code Reviews"],
    "AI": ["Prompt Engineering", "RAG Standards", "MCP Standards", "AI Safety",
           "Model Evaluation", "Agent Collaboration", "Hallucination Mitigation",
           "Responsible AI"],
    "Security": ["Secure Coding", "Authentication", "Authorization",
                 "Secrets Management", "Encryption", "Logging", "Incident Response",
                 "Vulnerability Management"],
    "Cloud_And_DevOps": ["Infrastructure as Code", "CI/CD", "Containers",
                         "Kubernetes", "Monitoring", "Backups", "Disaster Recovery"],
    "Quality": ["Testing", "Performance", "Accessibility", "Documentation",
                "Release Management"],
    "Business": ["Product Management", "Marketing", "Sales", "Customer Success",
                 "Finance", "Legal", "Procurement"],
}

PHASE7 = {
    "Enterprise": ["Executive Review", "Governance Review", "Risk Assessment",
                   "Business Readiness"],
    "Product": ["Product Discovery", "Requirements Review", "Roadmap Approval",
                "Feature Readiness"],
    "Architecture": ["Architecture Review", "Solution Design Review",
                     "Integration Review"],
    "Engineering": ["Code Review", "Pull Request Review", "API Review",
                    "Database Review", "Infrastructure Review"],
    "AI": ["Prompt Review", "RAG Review", "MCP Review", "AI Safety Review",
           "Agent Review", "Model Evaluation"],
    "Security": ["Secure Coding", "Threat Modelling", "IAM", "Secrets",
                 "Penetration Testing", "Vulnerability Review"],
    "Cloud_And_DevOps": ["CI/CD", "Deployment", "Rollback", "Monitoring",
                         "Disaster Recovery"],
    "Quality": ["Functional Testing", "Regression", "Performance", "Accessibility",
                "Documentation", "Release Readiness"],
    "Business": ["Marketing", "Sales", "Customer Success", "Finance", "Legal",
                 "Procurement"],
}

PHASE8 = {
    "Executive": ["Annual Planning", "Quarterly Planning", "Strategy Review",
                  "Budget Planning"],
    "Product": ["Product Discovery", "Product Validation", "Feature Prioritisation",
                "Product Launch"],
    "Engineering": ["Feature Delivery", "Code Review", "Release Management",
                    "Incident Response", "Technical Debt Management"],
    "AI": ["Prompt Lifecycle", "RAG Development", "Agent Development",
           "MCP Integration", "AI Evaluation", "Hallucination Investigation"],
    "Security": ["Security Review", "Vulnerability Response", "Threat Modelling",
                 "Secrets Rotation"],
    "Cloud_And_DevOps": ["CI/CD Deployment", "Rollback", "Disaster Recovery",
                         "Infrastructure Provisioning"],
    "Quality": ["Test Strategy", "Performance Optimisation", "Accessibility Review",
                "Production Readiness"],
    "Business": ["Sales Discovery", "Proposal Creation", "Customer Onboarding",
                 "Customer Success Review", "Marketing Campaign Launch"],
}

PHASE9 = {
    "Strategy_And_Governance": ["Business Case", "Project Charter",
                                "Decision Record (ADR)", "Risk Register",
                                "Governance Report"],
    "Product": ["PRD", "Feature Specification", "User Story", "Acceptance Criteria",
                "Release Notes"],
    "Engineering": ["API Specification", "Database Design", "Architecture Decision",
                    "Technical Design", "Code Review Report"],
    "AI": ["Prompt Template", "Agent Specification", "RAG Configuration",
           "Evaluation Report", "Model Card", "MCP Server Specification"],
    "Security": ["Threat Model", "Security Review", "Incident Report",
                 "Vulnerability Report"],
    "Operations": ["Runbook", "SOP", "Incident Timeline", "Postmortem",
                   "Change Request"],
    "Business": ["Sales Proposal", "Discovery Questionnaire", "Customer Success Plan",
                 "Marketing Campaign Brief", "ROI Assessment"],
}

PHASE10 = {
    "Business": ["Strategy", "Finance", "Marketing", "Sales", "Customer Success",
                 "Legal", "Operations"],
    "Engineering": ["Architecture", "Frontend", "Backend", "API", "Integration",
                    "Database", "Cloud", "DevOps", "DevSecOps", "Observability",
                    "Testing"],
    "Artificial_Intelligence": ["LLMs", "Prompt Engineering", "Agents",
                                "Agentic Workflows", "RAG", "MCP", "Embeddings",
                                "Vector Databases", "Evaluation", "Guardrails",
                                "Responsible AI"],
    "Security": ["OWASP", "OWASP LLM Top 10", "Zero Trust", "IAM", "Encryption",
                 "Secrets", "Incident Response"],
    "Data": ["Analytics", "BI", "ML", "Data Engineering", "Data Governance"],
    "SaaS": ["Product Management", "Pricing", "Product-Led Growth", "Onboarding",
             "Retention", "Support"],
    "Industry_Playbooks": ["Retail", "Healthcare", "Education", "Real Estate",
                           "Manufacturing", "Finance", "Insurance", "Government",
                           "Construction", "Hospitality", "Logistics", "Legal"],
}

PHASE11 = {
    "Agent_Governance": ["Agent Registry", "Agent Lifecycle", "Agent Versioning",
                         "Agent Capability Model"],
    "Agent_Roles": ["Executive Agents", "Product Agents", "Engineering Agents",
                    "AI Engineering Agents", "Security Agents", "QA Agents",
                    "Marketing Agents", "Sales Agents", "Customer Success Agents",
                    "Finance Agents", "Legal Agents", "Operations Agents"],
    "Collaboration": ["Agent-to-Agent Protocol", "Agent-to-Human Protocol",
                      "Human Approval Workflow", "Escalation Workflow",
                      "Conflict Resolution", "Shared Context Management"],
    "Memory": ["Working Memory", "Long-term Memory", "Knowledge Retrieval",
               "Context Compression", "Session Continuity"],
    "Tooling": ["MCP Integration", "Tool Permissions", "API Access",
                "Secrets Handling", "Audit Logging"],
}

PHASE12 = {
    "Enterprise_Automation": ["Automation Strategy", "Automation Governance",
                              "Workflow Registry", "Automation Catalogue",
                              "Event-Driven Architecture"],
    "AI_Automation": ["AI Workflow Automation", "Agent Orchestration",
                      "Prompt Lifecycle Automation", "Knowledge Refresh Automation",
                      "RAG Pipeline Automation"],
    "Engineering_Automation": ["CI/CD", "IaC Automation", "Release Automation",
                               "Dependency Updates", "Environment Provisioning"],
    "Security_Automation": ["Security Scanning", "Secret Rotation",
                            "Compliance Monitoring", "Threat Detection",
                            "Vulnerability Remediation"],
    "Quality_Automation": ["Test Automation", "Performance Monitoring",
                           "Accessibility Monitoring", "Documentation Validation",
                           "Architecture Validation"],
    "Platform_Operations": ["Observability", "Incident Automation", "Capacity Planning",
                            "Backup Verification", "Disaster Recovery Automation"],
    "Business_Automation": ["CRM Automation", "Customer Onboarding", "Billing Automation",
                            "Marketing Automation", "Customer Success Automation"],
    "Executive_Intelligence": ["KPI Dashboards", "OKR Tracking", "Executive Reporting",
                               "Cost Optimisation", "Portfolio Health"],
}

PHASE13_INDUSTRIES = [
    "Retail", "E-commerce", "Healthcare", "Pharmaceuticals", "Education",
    "Higher Education", "Banking", "Financial Services", "Insurance", "Manufacturing",
    "Automotive", "Logistics", "Supply Chain", "Government", "Defence", "Energy",
    "Telecommunications", "Hospitality", "Travel", "Real Estate", "Construction",
    "Legal", "Accounting", "Human Resources", "Recruitment", "Media",
    "Marketing Agencies", "SaaS Companies", "AI Consulting Firms",
    "Non-profit Organisations",
]
PHASE13_DOCS = ["Business Overview", "AI Opportunities", "Reference Architecture",
                "Agent Catalogue", "Automation Catalogue", "Data Model",
                "Security Model", "Compliance Model", "Implementation Roadmap",
                "Success Metrics"]

PHASE14 = {
    "AI_Product": ["Build AI SaaS", "Launch MVP", "Enterprise SaaS", "AI Marketplace",
                   "Multi-tenant Platform"],
    "AI_Consulting": ["AI Readiness Assessment", "AI Strategy", "AI Centre of Excellence",
                      "Enterprise AI Adoption", "AI Governance Rollout"],
    "AI_Engineering": ["Enterprise RAG", "AI Agent Platform", "MCP Platform",
                       "Prompt Platform", "Evaluation Platform"],
    "Business": ["AI Marketing", "AI Sales", "AI Customer Support", "AI HR",
                 "AI Finance", "AI Legal", "AI Operations"],
}

PHASE15 = {
    "Repository_Standards": ["Monorepo", "Polyrepo", "Git Strategy",
                             "Branch Protection", "Repository Layout"],
    "Application_Architectures": ["AI SaaS", "Multi-Tenant SaaS", "AI Agent Platform",
                                  "Enterprise RAG Platform", "Internal AI Assistant",
                                  "AI Gateway", "API Platform"],
    "Infrastructure": ["Terraform", "Pulumi", "Kubernetes", "Docker", "Serverless",
                       "Hybrid Cloud"],
    "CICD": ["GitHub Actions", "GitLab CI", "Azure DevOps", "Release Pipelines",
             "Progressive Delivery"],
    "AI_Platforms": ["Prompt Platform", "Agent Runtime", "MCP Servers",
                     "Model Registry", "Evaluation Platform", "Vector Database Patterns"],
    "Security": ["Zero Trust", "IAM", "Secrets", "Network Security",
                 "Secure Supply Chain", "SBOM"],
    "Observability": ["Logging", "Metrics", "Tracing", "Dashboards", "Alerting"],
    "Data_Platforms": ["Lakehouse", "Warehouse", "Streaming", "ETL", "CDC",
                       "Data Governance"],
    "Sample_Applications": ["FAQ Platform", "AI Support Agent", "AI Sales Assistant",
                            "AI Knowledge Portal", "AI Workflow Engine",
                            "AI Consulting Portal"],
}

PHASE16 = {
    "Core_CLI": ["CLI Architecture", "Command Reference", "Configuration", "Profiles",
                 "Authentication", "Plugins", "Telemetry", "Upgrade Strategy"],
    "SDKs": ["Python SDK", "TypeScript SDK", "Go SDK", "Java SDK", ".NET SDK"],
    "Project_Scaffolding": ["AI SaaS Starter", "AI Agent Starter", "RAG Starter",
                            "MCP Starter", "AI Consulting Starter"],
    "Validation_Engine": ["Repository Validation", "Rules Validation",
                          "Skills Validation", "Architecture Validation",
                          "Compliance Validation"],
    "Developer_Experience": ["VS Code Extension", "Cursor Extension", "JetBrains Plugin",
                             "GitHub App", "GitHub Actions", "Pre-commit Hooks"],
    "APIs": ["REST API", "GraphQL API", "MCP Interface", "Event API", "Webhooks"],
    "Automation": ["Project Bootstrap", "Document Generator",
                   "Repository Synchronisation", "Dependency Scanner",
                   "Prompt Compiler"],
}

PHASE17 = {
    "Maturity_Model": ["Level 0 Initial", "Level 1 Managed", "Level 2 Defined",
                       "Level 3 Integrated", "Level 4 Optimised",
                       "Level 5 Autonomous AI Enterprise"],
    "Individual_Certifications": ["AI Developer", "AI Engineer", "AI Architect",
                                  "AI Security Engineer", "AI Consultant",
                                  "AI Product Manager", "DevSecOps Engineer",
                                  "Prompt Engineer", "RAG Engineer", "MCP Engineer",
                                  "AI Auditor"],
    "Organisation_Certifications": ["Startup", "SME", "Enterprise", "Government",
                                    "Partner", "Training Provider"],
    "Audit_Framework": ["Internal Audit", "External Audit", "Evidence Collection",
                        "Control Mapping", "Risk Scoring", "Gap Analysis"],
    "Continuous_Compliance": ["Compliance Monitoring", "KPI Dashboards",
                              "Executive Scorecards", "Capability Heat Maps",
                              "Improvement Roadmaps"],
}

PHASE18 = {
    "Marketplace_Platform": ["Marketplace Architecture", "Marketplace Governance",
                             "Discovery Engine", "Search and Ranking",
                             "Recommendation Engine", "Review and Rating System"],
    "Package_Types": ["Skills Packs", "Rules Packs", "Checklist Packs",
                      "Playbook Packs", "Template Packs", "Knowledge Packs",
                      "Industry Packs", "Accelerator Packs", "AI Agent Packs",
                      "Prompt Packs", "MCP Server Packs", "SDK Extensions",
                      "CLI Plugins", "Automation Packs", "Compliance Packs"],
    "Package_Lifecycle": ["Create", "Validate", "Publish", "Version", "Deprecate",
                          "Archive", "Restore"],
    "Trust_And_Security": ["Digital Signing", "Package Verification",
                           "Supply Chain Security", "Trust Levels",
                           "Vulnerability Reporting"],
    "Commercial": ["Licensing", "Pricing Models", "Subscription Models",
                   "Revenue Sharing", "Billing Integration"],
    "Community": ["Contributor Programme", "Maintainer Guide", "Governance Council",
                  "Code of Conduct"],
}

PHASE19 = {
    "Corporate_Structure": ["Board", "Executive Leadership", "PMO", "Finance", "Legal",
                            "HR", "Operations"],
    "Product_Organisation": ["Product Portfolio", "Roadmaps", "Product Teams"],
    "Engineering_Organisation": ["Platform", "Backend", "Frontend", "Data", "AI",
                                 "Security", "DevSecOps", "QA", "SRE"],
    "AI_Workforce": ["Executive Agents", "Product Agents", "Engineering Agents",
                     "Security Agents", "Marketing Agents", "Sales Agents",
                     "Customer Success Agents", "Finance Agents", "Legal Agents"],
    "Technology_Estate": ["Repositories", "Cloud Accounts", "Networks", "CI/CD",
                          "Observability", "Data Platforms", "AI Platforms"],
    "Business_Operations": ["Marketing", "Sales", "Customer Success", "Support",
                            "Procurement", "Vendor Management"],
    "Simulation_Scenarios": ["Product Launch", "Security Incident", "AI Model Upgrade",
                             "Customer Onboarding", "Enterprise Sales Cycle",
                             "Disaster Recovery", "Compliance Audit",
                             "Quarterly Planning"],
}

PHASE20 = {
    "Enterprise_Brain": ["Enterprise Orchestrator", "Executive Decision Engine",
                         "Goal Management", "Portfolio Optimisation",
                         "Strategy Execution"],
    "Multi_Agent_Coordination": ["Task Planning", "Agent Scheduling", "Agent Discovery",
                                 "Agent Registry", "Dynamic Delegation",
                                 "Agent Negotiation", "Conflict Resolution"],
    "Enterprise_Memory": ["Working Memory", "Long-term Memory", "Knowledge Graph",
                          "Context Management", "Memory Governance"],
    "Autonomous_Governance": ["Policy Enforcement", "Rule Validation",
                              "Architecture Compliance", "Risk Monitoring",
                              "Audit Automation"],
    "Autonomous_Engineering": ["Repository Health", "Technical Debt Detection",
                               "Architecture Drift Detection",
                               "Prompt Lifecycle Governance", "AI Model Lifecycle"],
    "Business_Intelligence": ["KPI Analytics", "Executive Dashboards", "Forecasting",
                              "Cost Optimisation", "Capacity Planning"],
    "Continuous_Improvement": ["Feedback Collection", "Experimentation", "Benchmarking",
                               "Lessons Learned", "Self-Healing Workflows"],
}


# --------------------------------------------------------------------------- #
# Generation routines
# --------------------------------------------------------------------------- #
def gen_flat(folder, prefix, doctype, category, owner, phase, items, sections,
             tags, ow, stats):
    base = OUT / folder
    for i, title in enumerate(items, start=1):
        path = base / f"{i:02d}_{slug(title)}.md"
        content = render(path, f"{prefix}-{i:06d}", title, doctype, category, phase,
                         owner, sections, tags)
        write(path, content, ow, stats)


def gen_grouped(folder, prefix, doctype, owner, phase, groups, sections, tags,
                ow, stats, suffix=""):
    counter = 1
    for group, items in groups.items():
        for i, title in enumerate(items, start=1):
            full = f"{title}{suffix}"
            path = OUT / folder / group / f"{i:02d}_{slug(full)}.md"
            content = render(path, f"{prefix}-{counter:06d}", full, doctype,
                             group.replace("_", " "), phase, owner, sections, tags)
            write(path, content, ow, stats)
            counter += 1


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()
    ow = args.overwrite
    stats = {"written": 0, "skipped": 0, "indexes": 0}

    gen_flat(PHASE_DIR[1], "ARCH", "Architecture", "Enterprise Architecture",
             "Office of the Chief Enterprise Architect", "Phase 01", PHASE1, S[1],
             ["enterprise-architecture"], ow, stats)
    gen_flat(PHASE_DIR[2], "SPEC", "Specification", "Enterprise Specification",
             "Office of the Chief Enterprise Architect", "Phase 02", PHASE2, S[2],
             ["specification"], ow, stats)
    gen_flat(PHASE_DIR[3], "DIV", "Specification", "Division Specification",
             "Division Leadership", "Phase 03", PHASE3, S[3], ["division"], ow, stats)
    gen_grouped(PHASE_DIR[4], "DEPT", "Specification", "Department Leadership",
                "Phase 04", PHASE4, S[4], ["department"], ow, stats,
                suffix=" Department")
    # Phases 05-10 and 13 are owned by dedicated content-rich generators
    # (generate_skills.py, generate_rules.py, generate_checklists.py,
    # generate_playbooks.py, generate_templates.py, generate_knowledge.py and
    # generate_industry.py). They are intentionally NOT regenerated here so this
    # generator never overwrites their hand-curated content.
    gen_grouped(PHASE_DIR[11], "AGENT", "Framework", "Chief AI Systems Architect",
                "Phase 11", PHASE11, S[11], ["ai-agent"], ow, stats)
    gen_grouped(PHASE_DIR[12], "AUTO", "Framework", "Chief Automation Architect",
                "Phase 12", PHASE12, S[12], ["automation"], ow, stats)

    gen_grouped(PHASE_DIR[14], "ACCEL", "Accelerator", "Chief Transformation Architect",
                "Phase 14", PHASE14, S[14], ["accelerator"], ow, stats,
                suffix=" Accelerator Pack")
    for i, ind in enumerate(PHASE13_INDUSTRIES, start=1):
        title = f"{ind} Accelerator Pack"
        path = OUT / PHASE_DIR[14] / "Industry" / f"{i:02d}_{slug(title)}.md"
        content = render(path, f"ACCEL-9{i:05d}", title, "Accelerator", "Industry",
                         "Phase 14", "Chief Transformation Architect", S[14],
                         ["accelerator"])
        write(path, content, ow, stats)

    gen_grouped(PHASE_DIR[15], "IMPL", "Implementation", "Chief Solution Architect",
                "Phase 15", PHASE15, S[15], ["reference-implementation"], ow, stats)
    gen_grouped(PHASE_DIR[16], "SDK", "Component", "Chief Platform Engineer",
                "Phase 16", PHASE16, S[16], ["sdk-cli"], ow, stats)
    gen_grouped(PHASE_DIR[17], "CERT", "Certification",
                "Chief Governance Audit and Certification Architect", "Phase 17",
                PHASE17, S[17], ["certification"], ow, stats)
    gen_grouped(PHASE_DIR[18], "MKT", "Marketplace",
                "Chief Platform Ecosystem Architect", "Phase 18", PHASE18, S[18],
                ["marketplace"], ow, stats)
    gen_grouped(PHASE_DIR[19], "ORG", "Organisation",
                "Chief Enterprise Transformation Architect", "Phase 19", PHASE19,
                S[19], ["reference-organisation"], ow, stats)
    gen_grouped(PHASE_DIR[20], "META", "Framework",
                "Chief Autonomous Systems Architect", "Phase 20", PHASE20, S[20],
                ["meta-orchestrator"], ow, stats)

    build_indexes(stats)
    print(f"Written: {stats['written']}  Skipped: {stats['skipped']}  "
          f"Indexes: {stats['indexes']}")


if __name__ == "__main__":
    main()
