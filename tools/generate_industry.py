#!/usr/bin/env python3
"""Generate complete, focused Phase 13 Industry Blueprint documents.

For each industry, renders ten distinct, ready-to-use documents (overview,
opportunities, architecture, agents, automations, data, security, compliance,
roadmap, metrics) from real industry content in industries_kb.py.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from industries_kb import INDUSTRIES

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS" / "PHASE_13_INDUSTRY_BLUEPRINTS"
OWNER = "Chief Industry Solutions Architect"
PROMPT = "01_PHASES/PHASE_13_INDUSTRY_BLUEPRINTS_MASTER_PROMPT.md"
STANDARDS = ["ISO 42001", "ISO 27001", "NIST AI RMF", "SOC 2", "OWASP ASVS",
             "OWASP LLM Top 10", "WCAG 2.2 AA"]

DOCS = [
    ("01_BUSINESS_OVERVIEW.md", "Business Overview"),
    ("02_AI_OPPORTUNITIES.md", "AI Opportunities"),
    ("03_REFERENCE_ARCHITECTURE.md", "Reference Architecture"),
    ("04_AGENT_CATALOGUE.md", "Agent Catalogue"),
    ("05_AUTOMATION_CATALOGUE.md", "Automation Catalogue"),
    ("06_DATA_MODEL.md", "Data Model"),
    ("07_SECURITY_MODEL.md", "Security Model"),
    ("08_COMPLIANCE_MODEL.md", "Compliance Model"),
    ("09_IMPLEMENTATION_ROADMAP.md", "Implementation Roadmap"),
    ("10_SUCCESS_METRICS.md", "Success Metrics"),
]


def bullets(items):
    return "\n".join(f"- {i}" for i in items) if items else "- Not applicable."


def checks(items):
    return "\n".join(f"- [ ] {i}" for i in items)


def table(headers, rows):
    h = "| " + " | ".join(headers) + " |"
    s = "| " + " | ".join("---" for _ in headers) + " |"
    b = "\n".join("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |"
                  for r in rows)
    return f"{h}\n{s}\n{b}"


def fm(doc_id, title, category):
    std = "\n".join(f"  - {s}" for s in STANDARDS)
    rel = "\n".join(f"  - {r}" for r in
                    ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md", PROMPT])
    return ("---\n"
            f"id: {doc_id}\ntitle: {title}\ndocument_type: Industry Blueprint\n"
            f"category: {category}\nphase: Phase 13\nowner: {OWNER}\n"
            "status: Published\nlifecycle: Active\nclassification: Internal\n"
            f"version: {VERSION}\ncreated: {DATE}\nupdated: {DATE}\n"
            f"tags:\n  - industry-blueprint\n  - {category.lower().replace(' ', '-')}\n"
            f"related_documents:\n{rel}\nstandards:\n{std}\n---")


def body_for(label, rec):
    name = rec["name"]
    if label == "Business Overview":
        caps = [u[0] for u in rec["usecases"]]
        return [
            "## Executive Summary", "",
            f"{rec['summary']} This blueprint pack gives a reusable, vendor-neutral "
            f"path to deploy AI across {name} with proven architecture, governance "
            "and delivery guidance.", "",
            "## Business Challenges", "", bullets(rec["challenges"]), "",
            "## Business Goals", "", bullets(rec["goals"]), "",
            "## Business Capability Map", "",
            bullets([f"**{c}** capability enabled by AI." for c in caps]), "",
            "## Target Operating Model", "",
            bullets(["AI agents augment teams under human oversight.",
                     "Shared platform: data, RAG, agents, automation, governance.",
                     "Centre of excellence sets standards; teams deliver use cases.",
                     "Continuous measurement against the success metrics."]), "",
            "## How to Use This Blueprint", "",
            bullets([
                "[AI Opportunities](./02_AI_OPPORTUNITIES.md) — what to build.",
                "[Reference Architecture](./03_REFERENCE_ARCHITECTURE.md) — how.",
                "[Agent Catalogue](./04_AGENT_CATALOGUE.md) — the agents.",
                "[Automation Catalogue](./05_AUTOMATION_CATALOGUE.md) — workflows.",
                "[Data Model](./06_DATA_MODEL.md) — the data.",
                "[Security](./07_SECURITY_MODEL.md) and "
                "[Compliance](./08_COMPLIANCE_MODEL.md) — guardrails.",
                "[Roadmap](./09_IMPLEMENTATION_ROADMAP.md) and "
                "[Success Metrics](./10_SUCCESS_METRICS.md) — deliver and measure."]),
            "",
        ]
    if label == "AI Opportunities":
        rows = [[u[0], u[1], "High"] for u in rec["usecases"]]
        return [
            "## Executive Summary", "",
            f"The highest-value AI opportunities for {name}, prioritised for impact "
            "and feasibility.", "",
            "## High-Value AI Use Cases", "",
            table(["Use Case", "Description", "Value"], rows), "",
            "## RAG Opportunities", "",
            bullets([f"Ground answers in {name} knowledge sources with citations.",
                     "Enable semantic search across documents and records.",
                     "Keep responses current via scheduled re-indexing."]), "",
            "## MCP Opportunities", "",
            bullets(["Expose core systems as governed MCP tools for agents.",
                     "Enforce least-privilege scopes and human approval.",
                     "Audit every tool invocation."]), "",
            "## Customer Experience Improvements", "",
            bullets(["Faster, 24/7, personalised service.",
                     "Consistent, accurate, grounded answers.",
                     "Proactive outreach based on predictions."]), "",
            "## Internal Productivity Gains", "",
            bullets(["Automate repetitive, rules-based work.",
                     "Assist experts with drafting and synthesis.",
                     "Reduce cycle times across core processes."]), "",
            "## Prioritisation (Value vs Effort)", "",
            table(["Use Case", "Value", "Effort", "Sequence"],
                  [[u[0], "High", "Medium", str(i)]
                   for i, u in enumerate(rec["usecases"], start=1)]), "",
        ]
    if label == "Reference Architecture":
        return [
            "## Executive Summary", "",
            f"A vendor-neutral reference architecture for AI in {name}, built on the "
            "AIBOS platform standards.", "",
            "## Reference Architecture", "",
            bullets(["Experience layer: apps, assistants and channels.",
                     "Agent/orchestration layer: agents, tools (MCP), workflows.",
                     "AI layer: LLMs, RAG, evaluation and guardrails.",
                     "Data layer: sources, pipelines, vector store, governance.",
                     "Platform layer: cloud, security, observability."]), "",
            "## Technology Stack", "",
            bullets(["Cloud-native runtime and managed services.",
                     "API-first interfaces (OpenAPI) and event-driven messaging.",
                     "Vector database and RAG components.",
                     "Agent framework with tracing and guardrails.",
                     "OpenTelemetry-based observability."]), "",
            "## Data Sources", "", bullets(rec["datasources"]), "",
            "## Integration Patterns", "",
            bullets(["Event-driven integration with idempotent consumers.",
                     "Governed APIs and MCP tools for system access.",
                     "Retry, back-off and dead-letter handling."]), "",
            "## Mermaid Architecture Diagram", "",
            "```mermaid\nflowchart TD\n"
            "    U[Users / Channels] --> X[Experience Layer]\n"
            "    X --> O[Agents & Orchestration]\n"
            "    O --> AI[LLMs + RAG + Guardrails]\n"
            "    O --> T[MCP Tools]\n"
            "    AI --> D[(Data + Vector Store)]\n"
            "    T --> S[Core Systems]\n"
            "    O --> H{High-risk?}\n"
            "    H -->|Yes| A[Human Approval]\n"
            "    H -->|No| E[Execute]\n"
            "    A --> E --> R([Audit Trail])\n```", "",
            "## Governance Model", "",
            bullets(["Risk-tiered oversight aligned to ISO 42001 / NIST AI RMF.",
                     "Human-in-the-loop for high-impact decisions.",
                     "Full audit trails and evaluation gates."]), "",
        ]
    if label == "Agent Catalogue":
        rows = [[a[0], a[1], "Scoped, least-privilege",
                 "Required for high-risk actions"] for a in rec["agents"]]
        return [
            "## Executive Summary", "",
            f"The portfolio of AI agents for {name}, each with a clear role and "
            "authority boundaries.", "",
            "## AI Agent Portfolio", "",
            table(["Agent", "Role", "Authority", "Human Approval"], rows), "",
            "## Collaboration Model", "",
            bullets(["An orchestrator delegates tasks to specialist agents.",
                     "Agents share governed context/memory.",
                     "Conflicts and failures follow defined escalation."]), "",
            "## Guardrails", "",
            bullets(["Least-privilege tools and scoped permissions.",
                     "Input/output filtering and injection defence.",
                     "Cost and loop limits; full observability."]), "",
        ]
    if label == "Automation Catalogue":
        rows = []
        for a in rec["automations"]:
            trig, act = (a[1].split("->", 1) + [""])[:2] if "->" in a[1] else (a[1], "")
            rows.append([a[0], trig.strip(), act.strip() or "Automated action",
                         "GitHub / Slack / n8n"])
        return [
            "## Executive Summary", "",
            f"Repeatable workflow automations for {name}, executable by humans and AI "
            "agents.", "",
            "## Automation Catalogue", "",
            table(["Automation", "Trigger", "Action", "Integration"], rows), "",
            "## Integration Points", "",
            bullets(["GitHub / GitHub Actions", "Slack / Teams notifications",
                     "Jira / Linear tracking", "n8n / Make orchestration",
                     "Core line-of-business systems via MCP"]), "",
            "## Human Approval Points", "",
            bullets(["Before any irreversible or high-risk action.",
                     "Before external customer-facing communications.",
                     "Before financial or regulated decisions."]), "",
        ]
    if label == "Data Model":
        ent_rows = [[e, f"Core {name} entity."] for e in rec["entities"]]
        return [
            "## Executive Summary", "",
            f"The core data entities and sources that power AI in {name}.", "",
            "## Core Entities", "", table(["Entity", "Description"], ent_rows), "",
            "## Relationships", "",
            bullets(["Entities relate through clear keys and ownership.",
                     "Events capture state changes for analytics and agents.",
                     "Sensitive entities carry classification and retention."]), "",
            "## Mermaid Entity Diagram", "",
            "```mermaid\nflowchart LR\n"
            + "\n".join(f"    E{i}[{e}]" for i, e in enumerate(rec["entities"][:5]))
            + "\n" + "\n".join(f"    E0 --> E{i}"
                               for i in range(1, min(5, len(rec["entities"]))))
            + "\n```", "",
            "## Data Sources", "", bullets(rec["datasources"]), "",
            "## Privacy Controls", "",
            bullets(["Data minimisation and purpose limitation.",
                     "Encryption and masking of sensitive fields.",
                     "Retention and secure-deletion policies."]), "",
        ]
    if label == "Security Model":
        return [
            "## Executive Summary", "",
            f"The security model for AI in {name}, applying defence-in-depth and Zero "
            "Trust.", "",
            "## Threat Landscape", "", bullets(rec["threats"]), "",
            "## Security Controls", "",
            bullets(["Authentication and authorisation on every action.",
                     "Encryption in transit (TLS 1.2+) and at rest.",
                     "Input validation, output handling and dependency scanning.",
                     "Audit logging and continuous monitoring."]), "",
            "## Zero Trust and IAM", "",
            bullets(["Never trust, always verify; least privilege everywhere.",
                     "MFA on privileged access; periodic access reviews.",
                     "Micro-segmentation and assume-breach design."]), "",
            "## Secrets Management", "",
            bullets(["Store secrets in a managed vault; never in code/config.",
                     "Rotate on a schedule and on compromise.",
                     "Scan code and history for leaks."]), "",
            "## Monitoring and Incident Response", "",
            bullets(["Centralised, structured logging and alerting.",
                     "Defined severities, on-call and runbooks.",
                     "Blameless post-mortems with tracked actions."]), "",
        ]
    if label == "Compliance Model":
        rows = [[c, "Mapped to relevant controls and evidence."]
                for c in rec["compliance"]]
        return [
            "## Executive Summary", "",
            f"The compliance and governance model for AI in {name}.", "",
            "## Compliance Mapping", "",
            table(["Standard / Regulation", "Application"], rows), "",
            "## Privacy Controls", "",
            bullets(["Lawful basis, minimisation and purpose limitation.",
                     "Data subject rights and retention controls.",
                     "Vendor/data-processor due diligence."]), "",
            "## Governance Model", "",
            bullets(["AI risk classification per ISO 42001 / NIST AI RMF.",
                     "Human oversight for high-impact decisions.",
                     "Model cards, evaluation gates and audit trails."]), "",
            "## Responsible AI", "",
            bullets(["Bias and fairness assessment.",
                     "Transparency and explainability where required.",
                     "Accountability and appeal for affected users."]), "",
        ]
    if label == "Implementation Roadmap":
        return [
            "## Executive Summary", "",
            f"A phased, low-risk path to deploy AI across {name} and scale what works.",
            "",
            "## Adoption Roadmap", "",
            table(["Horizon", "Focus", "Outcome"],
                  [["0–30 days", "Discover and assess; pick 1–2 use cases",
                    "Baseline, data access and a prioritised backlog"],
                   ["31–90 days", "Build and pilot with guardrails",
                    "Validated pilot with measured impact"],
                   ["3–6 months", "Harden and integrate",
                    "Production rollout of initial use cases"],
                   ["6–12 months", "Scale across the portfolio",
                    "Multiple use cases live; CoE established"]]), "",
            "## Change Management", "",
            bullets(["Engage stakeholders and communicate early.",
                     "Train teams; redesign processes around AI + humans.",
                     "Manage expectations with transparent metrics."]), "",
            "## Risks", "",
            bullets(["Starting too broad instead of proving value.",
                     "Weak data foundations or access.",
                     "Insufficient oversight on regulated decisions.",
                     "Change resistance and unclear ownership."]), "",
            "## Dependencies", "",
            bullets(["Data access and quality.",
                     "Platform, security and governance readiness.",
                     "Skilled people and executive sponsorship."]), "",
        ]
    if label == "Success Metrics":
        rows = [[m[0], m[1]] for m in rec["metrics"]]
        return [
            "## Executive Summary", "",
            f"How to measure the impact of AI in {name} against business outcomes.", "",
            "## KPIs", "", table(["Metric", "Target Direction"], rows), "",
            "## ROI Metrics", "",
            bullets(["Cost savings from automation and efficiency.",
                     "Revenue uplift from better experience and decisions.",
                     "Payback period and net benefit per use case."]), "",
            "## Cost Considerations", "",
            bullets(["Model/compute (token) costs — align to usage.",
                     "Platform, data and integration costs.",
                     "Run/oversight costs (human-in-the-loop, monitoring)."]), "",
            "## Measurement Approach", "",
            bullets(["Baseline before deployment; measure deltas.",
                     "Instrument outcomes, not just outputs.",
                     "Review on a cadence and iterate."]), "",
        ]
    return ["## Executive Summary", "", rec["summary"], ""]


def footer(rec, from_dir):
    def rl(target):
        return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")

    def ph(n):
        rels = {5: "PHASE_05_SKILLS", 6: "PHASE_06_RULES", 7: "PHASE_07_CHECKLISTS",
                8: "PHASE_08_PLAYBOOKS", 9: "PHASE_09_TEMPLATES",
                10: "PHASE_10_KNOWLEDGE"}
        return os.path.relpath(OUT.parent / rels[n] / "README.md",
                               from_dir).replace(os.sep, "/")
    return [
        "## Required Skills", "", f"See the [Specialist Skills]({ph(5)}).", "",
        "## Required Rules", "", f"See the [Enterprise Rules]({ph(6)}).", "",
        "## Required Checklists", "", f"See the [Enterprise Checklists]({ph(7)}).", "",
        "## Required Playbooks", "", f"See the [Enterprise Playbooks]({ph(8)}).", "",
        "## Required Templates", "", f"See the [Enterprise Templates]({ph(9)}).", "",
        "## Knowledge Dependencies", "",
        f"See the [Enterprise Knowledge base]({ph(10)}).", "",
        "## Validation Checklist", "",
        checks(["YAML front matter present and valid.",
                "Industry-specific content is accurate and actionable.",
                "Cross-references resolve.",
                "Security, privacy and compliance addressed.",
                "No secrets or sensitive data exposed."]), "",
        "## References", "",
        bullets([
            f"[AIBOS Root Specification]({rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')})",
            f"[Repository Catalogue (ROOT_INDEX)]({rl('ROOT_INDEX.md')})",
            f"[Phase 13 Master Prompt]({rl(PROMPT)})"]), "",
        "## Version History", "",
        table(["Version", "Date", "Summary"],
              [[VERSION, DATE, "Complete, focused industry blueprint."]]), "",
    ]


def build(doc_id, folder, label, rec, from_dir):
    name = rec["name"]
    title = f"{name} {label}"

    def rl(target):
        return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")

    nav = (f"> **Navigate:** [Home]({rl('README.md')}) · "
           f"[Catalogue]({rl('ROOT_INDEX.md')}) · "
           f"[{name} Pack](./README.md) · "
           f"[Phase 13 Prompt]({rl(PROMPT)})")

    P = [fm(doc_id, title, name), "", f"# {title}", "", nav, "",
         f"**Industry:** {name}  •  **Document:** {label}", ""]
    P += body_for(label, rec)
    P += footer(rec, from_dir)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(P)).rstrip() + "\n"


def main():
    counter = 1
    written = 0
    for folder in sorted(INDUSTRIES):
        rec = INDUSTRIES[folder]
        for fname, label in DOCS:
            path = OUT / folder / fname
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build(f"IND-{counter:06d}", folder, label, rec, path.parent),
                            encoding="utf-8")
            counter += 1
            written += 1
    print(f"Wrote {written} industry blueprint documents across "
          f"{len(INDUSTRIES)} industries to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
