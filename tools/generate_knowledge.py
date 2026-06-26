#!/usr/bin/env python3
"""Generate complete, ready-to-use Phase 10 KNOWLEDGE articles from knowledge_kb.

Each article is an atomic, RAG-optimised explainer: core concepts, definitions,
business/technical context, best practices, anti-patterns, examples, FAQs, a
decision guide, learning path, a knowledge-graph block and retrieval metadata.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from knowledge_kb import get

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS" / "PHASE_10_KNOWLEDGE"
OWNER = "Chief Knowledge Architect"
PROMPT = "01_PHASES/PHASE_10_KNOWLEDGE_MASTER_PROMPT.md"

GROUPS = {
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

DOMAIN_LABEL = {
    "Business": "Business", "Engineering": "Engineering",
    "Artificial_Intelligence": "Artificial Intelligence", "Security": "Security",
    "Data": "Data", "SaaS": "SaaS", "Industry_Playbooks": "Industry Playbooks",
}


def slug(text):
    text = text.replace("&", "and").replace("/", " ").replace("+", " plus ")
    return re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_").upper()


def bullets(items):
    return "\n".join(f"- {i}" for i in items) if items else "- Not applicable."


def table(headers, rows):
    h = "| " + " | ".join(headers) + " |"
    s = "| " + " | ".join("---" for _ in headers) + " |"
    b = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{h}\n{s}\n{b}"


def fm(doc_id, title, domain, keywords, standards):
    tags = "\n".join(f"  - {t}" for t in keywords)
    std = "\n".join(f"  - {s}" for s in (standards or ["ISO 42001"]))
    rel = "\n".join(f"  - {r}" for r in
                    ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md", PROMPT])
    return ("---\n"
            f"id: {doc_id}\ntitle: {title}\ndocument_type: Knowledge Article\n"
            f"category: {DOMAIN_LABEL[domain]}\nphase: Phase 10\nowner: {OWNER}\n"
            "status: Published\nlifecycle: Active\nclassification: Internal\n"
            f"version: {VERSION}\ncreated: {DATE}\nupdated: {DATE}\n"
            f"tags:\n{tags}\nrelated_documents:\n{rel}\nstandards:\n{std}\n---")


def build(doc_id, title, domain, siblings, from_dir):
    e = get(domain, title)
    kws = e["keywords"]

    def rl(target):
        return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")

    def ph(n):
        rels = {5: "PHASE_05_SKILLS", 6: "PHASE_06_RULES", 7: "PHASE_07_CHECKLISTS",
                8: "PHASE_08_PLAYBOOKS", 9: "PHASE_09_TEMPLATES",
                4: "PHASE_04_DEPARTMENT_SPECIFICATIONS",
                3: "PHASE_03_DIVISION_SPECIFICATIONS"}
        return os.path.relpath(OUT.parent / rels[n] / "README.md",
                               from_dir).replace(os.sep, "/")

    sib_links = [f"[{s}](./{idx:02d}_{slug(s + ' Knowledge Article')}.md)"
                 for idx, s in enumerate(siblings, start=1) if s != title]
    defs = e.get("defs", [])
    faqs = e.get("faqs", [])

    nav = (f"> **Navigate:** [Home]({rl('README.md')}) · "
           f"[Catalogue]({rl('ROOT_INDEX.md')}) · "
           f"[All Knowledge]({os.path.relpath(OUT / 'README.md', from_dir).replace(os.sep, '/')}) · "
           f"[Phase 10 Prompt]({rl(PROMPT)})")

    # Context sections differ slightly for industry articles.
    if e.get("industry"):
        biz_ctx = (f"AI is reshaping the {title} sector. The highest-value, "
                   "lowest-risk entry points are listed under Core Concepts; the "
                   "business case rests on efficiency, experience and risk reduction.")
        tech_ctx = ("Typical solutions combine grounded RAG over approved sources, "
                    "workflow automation and predictive models, with human oversight "
                    "for regulated decisions.")
        examples = e.get("usecases", [])
    else:
        biz_ctx = (f"Understanding {title.lower()} helps teams make better decisions, "
                   "reduce risk and move faster. It connects directly to the related "
                   "rules, checklists and playbooks below.")
        tech_ctx = (f"In AIBOS, {title.lower()} is applied through the related "
                    "standards and automated wherever possible, with AI agents "
                    "operating under human oversight.")
        examples = e.get("examples", []) or [
            f"Apply the best practices above to a real {title.lower()} task and "
            "validate with the related checklist."]

    decision = bullets([
        f"Is this about {title.lower()}? -> Use this article and its related rule.",
        "Is it high-risk or regulated? -> Keep a human in the loop and check "
        "compliance.",
        "Need to act? -> Follow the related playbook and validate with the checklist.",
        "Need to produce an artefact? -> Use the related template."])

    P = [
        fm(doc_id, title, domain, kws, e.get("standards")), "",
        f"# {title}", "", nav, "",
        f"**Knowledge ID:** {doc_id}  •  **Category:** {DOMAIN_LABEL[domain]}", "",
        "## Tags", "", ", ".join(f"`{k}`" for k in kws), "",
        "## Executive Summary", "", e["summary"], "",
        "## Purpose", "",
        f"To give people and AI agents a clear, reusable explanation of "
        f"**{title}** that supports learning, retrieval (RAG) and decision support.",
        "",
        "## Scope", "",
        f"Covers the core ideas, practices and pitfalls of {title.lower()} as applied "
        "in AIBOS. Deep procedural detail lives in the related playbooks.", "",
        "## Core Concepts", "", bullets(e["concepts"]), "",
        "## Definitions", "",
        bullets([f"**{t}** — {d}" for t, d in defs]) if defs
        else f"See the [Enterprise Glossary]({rl('00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md')}).",
        "",
        "## Business Context", "", biz_ctx, "",
        "## Technical Context", "", tech_ctx, "",
        "## Best Practices", "", bullets(e["best"]), "",
        "## Anti-patterns", "", bullets(e["anti"]), "",
        "## Design Patterns", "",
        bullets(e.get("patterns", [])) if e.get("patterns")
        else "Apply the best practices above as repeatable patterns for this topic.", "",
        "## Examples", "", bullets(examples), "",
    ]

    if e.get("industry"):
        P += ["## Compliance Considerations", "", bullets(e.get("compliance", [])), "",
              "## Key Challenges", "", bullets(e.get("challenges", [])), ""]

    P += [
        "## FAQs", "",
        "\n\n".join(f"**Q: {q}**\n\nA: {a}" for q, a in faqs) if faqs
        else "_See Core Concepts and Best Practices._", "",
        "## Decision Tree", "", decision, "",
        "## Learning Path", "", bullets(e["learning"]), "",
        "## Prerequisites", "",
        "Familiarity with the AIBOS [Root Specification]("
        + rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md') + ") and the basics of this "
        "domain.", "",
        "## Related Skills", "", f"See the [Specialist Skills]({ph(5)}).", "",
        "## Related Rules", "", f"See the [Enterprise Rules]({ph(6)}).", "",
        "## Related Checklists", "", f"See the [Enterprise Checklists]({ph(7)}).", "",
        "## Related Playbooks", "", f"See the [Enterprise Playbooks]({ph(8)}).", "",
        "## Related Templates", "", f"See the [Enterprise Templates]({ph(9)}).", "",
        "## Related Knowledge", "",
        bullets(sib_links) if sib_links else "- See the knowledge catalogue.", "",
        "## Knowledge Graph", "",
        bullets([f"**Parent topic:** {DOMAIN_LABEL[domain]}",
                 "**Child topics:** see Related Knowledge below",
                 f"**Sibling topics:** {', '.join(siblings[:6])}",
                 f"**Dependencies / related technologies:** {', '.join(kws[:5])}",
                 f"**Related business domains:** {DOMAIN_LABEL[domain]}"]), "",
        "## Department Ownership", "",
        f"Owned by the relevant department(s); see [Department Specifications]({ph(4)}).",
        "",
        "## Division Ownership", "",
        f"Governed by the relevant division; see [Division Specifications]({ph(3)}).", "",
        "## External Standards", "", bullets(e.get("standards", ["ISO 42001"])), "",
        "## References", "",
        bullets([
            f"[AIBOS Root Specification]({rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')})",
            f"[Enterprise Glossary]({rl('00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md')})",
            f"[Repository Catalogue (ROOT_INDEX)]({rl('ROOT_INDEX.md')})",
            f"[Phase 10 Master Prompt]({rl(PROMPT)})"]), "",
        "## AI Retrieval Metadata", "",
        table(["Field", "Value"],
              [["Document type", "Knowledge Article"],
               ["Domain", DOMAIN_LABEL[domain]],
               ["Audience", "Humans, AI agents, RAG, enterprise search"],
               ["Keywords", ", ".join(kws)]]), "",
        "## Suggested Chunk Boundaries", "",
        bullets(["Executive Summary (overview chunk).",
                 "Core Concepts (concept chunk).",
                 "Best Practices + Anti-patterns (guidance chunk).",
                 "FAQs (Q&A chunks, one per question)."]), "",
        "## Suggested Embedding Keywords", "", ", ".join(f"`{k}`" for k in kws), "",
        "## Version History", "",
        table(["Version", "Date", "Summary"],
              [[VERSION, DATE, "Complete, ready-to-use knowledge article."]]), "",
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(P)).rstrip() + "\n"


def main():
    counter = 1
    written = 0
    missing = []
    for domain, items in GROUPS.items():
        for i, title in enumerate(items, start=1):
            if get(domain, title) is None:
                missing.append((domain, title))
                continue
            path = OUT / domain / f"{i:02d}_{slug(title + ' Knowledge Article')}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build(f"KN-{counter:06d}", title, domain, items, path.parent),
                            encoding="utf-8")
            counter += 1
            written += 1
    if missing:
        print("MISSING content for:", missing)
    print(f"Wrote {written} complete knowledge articles to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
