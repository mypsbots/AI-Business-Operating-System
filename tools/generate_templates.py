#!/usr/bin/env python3
"""Generate complete, ready-to-use Phase 09 TEMPLATE documents from templates_kb.

Each document contains the actual reusable, fill-in skeleton (with placeholders),
placeholder definitions, naming/folder conventions, validation/quality criteria,
schemas, AI prompt usage guidance and automation compatibility.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from templates_kb import TEMPLATES

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS" / "PHASE_09_TEMPLATES"
OWNER = "Chief Documentation and Knowledge Architect"
PROMPT = "01_PHASES/PHASE_09_TEMPLATES_MASTER_PROMPT.md"
STANDARDS = ["ISO 42001", "ISO 27001", "NIST AI RMF", "SOC 2", "OWASP ASVS",
             "OWASP LLM Top 10", "WCAG 2.2 AA"]

GROUPS = {
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


def slug(text):
    text = text.replace("&", "and").replace("/", " ").replace("+", " plus ")
    return re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_").upper()


def bullets(items):
    return "\n".join(f"- {i}" for i in items)


def checks(items):
    return "\n".join(f"- [ ] {i}" for i in items)


def table(headers, rows):
    h = "| " + " | ".join(headers) + " |"
    s = "| " + " | ".join("---" for _ in headers) + " |"
    b = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{h}\n{s}\n{b}"


def fm(doc_id, title, group):
    tags = "\n".join(f"  - {t}" for t in
                     ["template", group.lower().replace("_", "-"), slug(title).lower()])
    std = "\n".join(f"  - {s}" for s in STANDARDS)
    rel = "\n".join(f"  - {r}" for r in
                    ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md", PROMPT])
    return ("---\n"
            f"id: {doc_id}\ntitle: {title}\ndocument_type: Template\n"
            f"category: {group.replace('_', ' ')}\nphase: Phase 09\nowner: {OWNER}\n"
            "status: Published\nlifecycle: Active\nclassification: Internal\n"
            f"version: {VERSION}\ncreated: {DATE}\nupdated: {DATE}\n"
            f"tags:\n{tags}\nrelated_documents:\n{rel}\nstandards:\n{std}\n---")


def build(doc_id, title, group, from_dir):
    tpl = TEMPLATES[title]
    body = tpl["body"].rstrip()
    lang = "yaml" if tpl.get("kind") == "yaml" else "markdown"
    disp = title if title.endswith("Template") else f"{title} Template"

    def rl(target):
        return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")

    def ph(n):
        rels = {5: "PHASE_05_SKILLS", 6: "PHASE_06_RULES", 7: "PHASE_07_CHECKLISTS",
                8: "PHASE_08_PLAYBOOKS", 10: "PHASE_10_KNOWLEDGE"}
        return os.path.relpath(OUT.parent / rels[n] / "README.md",
                               from_dir).replace(os.sep, "/")

    placeholders = tpl.get("placeholders", [])
    ph_rows = [[f"`{{{{{name}}}}}`", desc] for name, desc in placeholders] + \
              [["`{{date}}`", "ISO date the document is created (YYYY-MM-DD)."]]

    nav = (f"> **Navigate:** [Home]({rl('README.md')}) · "
           f"[Catalogue]({rl('ROOT_INDEX.md')}) · "
           f"[All Templates]({os.path.relpath(OUT / 'README.md', from_dir).replace(os.sep, '/')}) · "
           f"[Phase 09 Prompt]({rl(PROMPT)})")

    # 4-backtick fence so any inner ``` (e.g. mermaid) does not break out.
    template_block = f"````{lang}\n{body}\n````"

    P = [
        fm(doc_id, disp, group), "",
        f"# {disp}", "", nav, "",
        f"**Template ID:** {doc_id}  •  **Category:** {group.replace('_', ' ')}", "",
        "## Purpose", "", tpl["purpose"], "",
        "## When to Use", "", tpl["when"], "",
        "## Audience", "", tpl["audience"], "",
        "## Inputs Required", "",
        bullets([d for _, d in placeholders] or ["The information the template asks for."]),
        "",
        "## Outputs Produced", "",
        f"A completed **{disp}** ready for review and use.", "",
        "## Required Metadata", "",
        "Every instance MUST carry: `id`, `title`, `owner`, `version`, `status`, "
        "`created`, `updated`.", "",
        "## Placeholder Definitions", "", table(["Placeholder", "Meaning"], ph_rows), "",
        "## Template", "",
        "Copy the block below and replace every `{{placeholder}}` with real content.", "",
        template_block, "",
        "## Naming Convention", "",
        f"`NN_{slug(title)}.md` (zero-padded order prefix, UPPER_SNAKE_CASE).", "",
        "## Folder Convention", "",
        f"Master template lives under `02_ARTEFACTS/PHASE_09_TEMPLATES/{group}/`. "
        "Copy instances into the relevant project/repository location.", "",
        "## Required Skills", "",
        f"See the [Specialist Skills]({ph(5)}) relevant to this artefact.", "",
        "## Required Rules", "",
        f"Comply with the [Enterprise Rules]({ph(6)}).", "",
        "## Required Checklists", "",
        f"Validate with the [Enterprise Checklists]({ph(7)}).", "",
        "## Required Playbooks", "",
        f"Produced within the [Enterprise Playbooks]({ph(8)}).", "",
        "## Required Knowledge Articles", "",
        f"Background in the [Enterprise Knowledge base]({ph(10)}).", "",
        "## Validation Rules", "",
        checks(["All `{{placeholders}}` are replaced (none remain).",
                "Required metadata is present and valid.",
                "No secrets or sensitive data are included.",
                "Cross-references resolve.",
                "Content follows the AIBOS style guide."]), "",
        "## Quality Criteria", "",
        bullets(["Consistent and reusable across teams.",
                 "Modular and easy to customise.",
                 "Machine-readable and automation-ready.",
                 "Version-controlled and reviewed."]), "",
        "## Example Completed Template", "",
        "Fill each placeholder with concrete values. For example, replace "
        f"`{{{{{(placeholders[0][0] if placeholders else 'title')}}}}}` with a real "
        "value and complete each section with project-specific detail.", "",
        "## JSON Schema", "",
        "```json\n{\n  \"$schema\": \"https://json-schema.org/draft/2020-12/schema\",\n"
        "  \"type\": \"object\",\n  \"required\": [\"id\", \"title\", \"version\"],\n"
        "  \"properties\": {\n    \"id\": { \"type\": \"string\" },\n"
        "    \"title\": { \"type\": \"string\" },\n"
        "    \"version\": { \"type\": \"string\" }\n  }\n}\n```", "",
        "## YAML Schema", "",
        "```yaml\nid: DOC-000000\ntitle: Example\nowner: Owning Team\n"
        "version: 1.0.0\nstatus: Draft\n```", "",
        "## AI Prompt Usage Guidance", "",
        bullets([
            f"Prompt an AI agent: \"Using the {disp} below, produce a completed "
            "version for <context>; replace every placeholder and keep the structure.\"",
            "Provide the source inputs (notes, tickets, data) as context.",
            "Ask the agent to flag any placeholder it cannot fill confidently.",
            "Always have a human review AI-completed instances before use."]), "",
        "## Automation Compatibility", "",
        bullets(["GitHub / GitHub Actions (scaffold and validate).",
                 "Cursor, Claude, GPT, Gemini (AI-assisted completion).",
                 "n8n / Make (workflow generation).",
                 "MCP tools and CI/CD pipelines."]), "",
        "## Version History", "",
        table(["Version", "Date", "Summary"],
              [[VERSION, DATE, "Complete, ready-to-use template."]]), "",
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(P)).rstrip() + "\n"


def main():
    counter = 1
    written = 0
    for group, items in GROUPS.items():
        for i, title in enumerate(items, start=1):
            path = OUT / group / f"{i:02d}_{slug(title + ' Template')}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build(f"TEMP-{counter:06d}", title, group, path.parent),
                            encoding="utf-8")
            counter += 1
            written += 1
    print(f"Wrote {written} complete template documents to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
