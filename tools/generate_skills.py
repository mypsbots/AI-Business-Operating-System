#!/usr/bin/env python3
"""Generate complete, ready-to-use Phase 05 skill documents.

Unlike the deterministic scaffolder (``generate_aibos.py``), this generator uses
the role-specific knowledge base in ``skills_kb.py`` to produce self-contained
reference documents: each one explains what the role is, who uses the document
and how, plus real skills, tools, certifications, a learning path, KPIs, career
progression and interview questions.

Run:  python3 tools/generate_skills.py
"""

from __future__ import annotations

import os
import re
from pathlib import Path

from skills_kb import SKILLS, SOFT_DEFAULT

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS" / "PHASE_05_SKILLS"
PROMPT = "01_PHASES/PHASE_05_SKILLS_MASTER_PROMPT.md"

STANDARDS = ["ISO 42001", "ISO 27001", "NIST AI RMF", "SOC 2", "OWASP ASVS",
             "OWASP LLM Top 10", "WCAG 2.2 AA"]

# Order must match generate_aibos.py so filenames stay stable.
ROLES = [
    "Executive Leadership", "Product Manager", "Product Designer",
    "Enterprise Architect", "Solution Architect", "Frontend Engineer",
    "Backend Engineer", "API Engineer", "Integration Engineer", "Platform Engineer",
    "Cloud Engineer", "Infrastructure Engineer", "DevOps Engineer",
    "DevSecOps Engineer", "Site Reliability Engineer", "Security Engineer",
    "Privacy Engineer", "Compliance Specialist", "QA Engineer",
    "Performance Engineer", "Accessibility Specialist", "Prompt Engineer",
    "LLM Engineer", "RAG Engineer", "Agent Engineer", "MCP Engineer",
    "AI Evaluation Engineer", "AI Safety Engineer", "ML Engineer", "Data Engineer",
    "Analytics Engineer", "BI Analyst", "Data Scientist", "SEO Specialist",
    "AEO Specialist", "GEO Specialist", "Content Strategist", "Growth Marketer",
    "Sales Engineer", "Account Manager", "Customer Success Manager",
    "Support Engineer", "Finance Analyst", "Legal Counsel", "Operations Manager",
    "Knowledge Manager", "Research Scientist", "Innovation Lead",
]

# Cross-reference targets (repo-relative) for the Related Resources section.
RELATED_PHASES = [
    ("Enterprise Rules", "02_ARTEFACTS/PHASE_06_RULES/README.md"),
    ("Enterprise Checklists", "02_ARTEFACTS/PHASE_07_CHECKLISTS/README.md"),
    ("Enterprise Playbooks", "02_ARTEFACTS/PHASE_08_PLAYBOOKS/README.md"),
    ("Enterprise Templates", "02_ARTEFACTS/PHASE_09_TEMPLATES/README.md"),
    ("Enterprise Knowledge", "02_ARTEFACTS/PHASE_10_KNOWLEDGE/README.md"),
    ("Certification & Maturity", "02_ARTEFACTS/PHASE_17_CERTIFICATION/README.md"),
]


def slug(text: str) -> str:
    text = text.replace("&", "and").replace("/", " ").replace("+", " plus ")
    text = re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_")
    return text.upper()


def rl(target: str) -> str:
    return os.path.relpath(ROOT / target, OUT).replace(os.sep, "/")


def bullets(items):
    return "\n".join(f"- {i}" for i in items)


def numbered(items):
    return "\n".join(f"{n}. {t}" for n, t in enumerate(items, start=1))


def table(headers, rows):
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{head}\n{sep}\n{body}"


def front_matter(doc_id, title, category, owner, role):
    tags = ["skill", slug(category).lower().replace("_", "-"),
            slug(role).lower().replace("_", "-")]
    tag_lines = "\n".join(f"  - {t}" for t in tags)
    std_lines = "\n".join(f"  - {s}" for s in STANDARDS)
    rel_lines = "\n".join(f"  - {r}" for r in
                          ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md",
                           PROMPT])
    return ("---\n"
            f"id: {doc_id}\n"
            f"title: {title}\n"
            "document_type: Skill\n"
            f"category: {category}\n"
            "phase: Phase 05\n"
            f"owner: {owner}\n"
            "status: Published\n"
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


def build(idx: int, role: str) -> str:
    kb = SKILLS[role]
    title = f"{role} Skill"
    doc_id = f"SKILL-{idx:06d}"
    soft = kb.get("soft", SOFT_DEFAULT)

    nav = ("> **Navigate:** "
           f"[Home]({rl('README.md')}) · "
           f"[Catalogue]({rl('ROOT_INDEX.md')}) · "
           f"[All Skills](README.md) · "
           f"[Phase 05 Prompt]({rl(PROMPT)})")

    quick = table(["Field", "Detail"], [
        ["Role", role],
        ["Category", kb["category"]],
        ["Typically reports to", kb["reports_to"]],
        ["Filled by", "A human, an AI agent, or both (human-in-the-loop)"],
        ["AI automation", kb["automatable"]],
        ["Key collaborators", ", ".join(kb["collaborates"])],
    ])

    how_to = bullets([
        "**Hiring managers** — use it as a job description, scorecard and "
        "interview guide (see *Required Skills* and *Sample Interview Questions*).",
        "**People in or entering the role** — use *Learning Path* and "
        "*Career Progression* to plan development.",
        "**AI / automation teams** — use *Role Summary*, *Responsibilities* and "
        "*Required Skills* as the basis for an AI agent's instructions/system prompt.",
        "**Team & quality leads** — use *KPIs* and *Deliverables* to set "
        "expectations and measure performance.",
    ])

    learning = numbered(kb["learning"])
    career = numbered([f"**{c}**" if ":" not in c else c for c in kb["career"]])
    interview = numbered(kb["interview"])

    related = bullets(
        [f"[{label}]({rl(path)})" for label, path in RELATED_PHASES]
        + [f"[AIBOS Root Specification]({rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')})",
           f"[Enterprise Glossary]({rl('00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md')})"])

    version_tbl = table(["Version", "Date", "Summary"],
                        [[VERSION, DATE, "Complete, ready-to-use skill reference."]])

    sections = [
        front_matter(doc_id, title, f"{kb['category']} Skill",
                     "Chief Skills Architect", role),
        "",
        f"# {role} Skill",
        "",
        nav,
        "",
        "## At a Glance",
        "",
        kb["summary"],
        "",
        quick,
        "",
        "## How to Use This Document",
        "",
        how_to,
        "",
        "## Role Summary",
        "",
        f"**Mission:** {kb['mission']}",
        "",
        kb["summary"],
        "",
        "## Key Responsibilities",
        "",
        bullets(kb["responsibilities"]),
        "",
        "## Required Skills",
        "",
        "### Technical Skills",
        "",
        bullets(kb["technical"]),
        "",
        "### Business Skills",
        "",
        bullets(kb["business"]),
        "",
        "### AI Skills",
        "",
        bullets(kb["ai"]),
        "",
        "### Soft Skills",
        "",
        bullets(soft),
        "",
        "## Tools and Technologies",
        "",
        bullets(kb["tools"]),
        "",
        "## Certifications and Qualifications",
        "",
        bullets(kb["certs"]),
        "",
        "## Learning Path",
        "",
        learning,
        "",
        "## Key Performance Indicators (KPIs)",
        "",
        bullets(kb["kpis"]),
        "",
        "## Typical Deliverables",
        "",
        bullets(kb["deliverables"]),
        "",
        "## Collaboration and Interfaces",
        "",
        f"This role works most closely with: {', '.join(kb['collaborates'])}.",
        "",
        "## Career Progression",
        "",
        career,
        "",
        "## Sample Interview Questions",
        "",
        interview,
        "",
        "## Related Resources",
        "",
        related,
        "",
        "## Version History",
        "",
        version_tbl,
        "",
    ]
    text = "\n".join(sections)
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
    return text


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    written = 0
    missing = [r for r in ROLES if r not in SKILLS]
    if missing:
        raise SystemExit(f"Missing KB entries: {missing}")
    for idx, role in enumerate(ROLES, start=1):
        path = OUT / f"{idx:02d}_{slug(role + ' Skill')}.md"
        path.write_text(build(idx, role), encoding="utf-8")
        written += 1
    print(f"Wrote {written} complete skill documents to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
