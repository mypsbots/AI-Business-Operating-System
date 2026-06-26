#!/usr/bin/env python3
"""Generate complete, ready-to-use Phase 06 RULES documents from content_kb.

Each rule is a single source of truth for an enterprise standard, written in
RFC-2119 style (MUST/SHOULD/MAY) with real, topic-specific content, an ownership
matrix, compliance mapping, metrics, anti-patterns and a validation checklist.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from content_kb import TOPICS, topic_key

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS" / "PHASE_06_RULES"
OWNER = "Chief Governance Architect"
PROMPT = "01_PHASES/PHASE_06_RULES_MASTER_PROMPT.md"
STANDARDS = ["ISO 42001", "ISO 27001", "NIST AI RMF", "SOC 2", "OWASP ASVS",
             "OWASP LLM Top 10", "WCAG 2.2 AA"]

GROUPS = {
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

GROUP_OWNER = {
    "Governance": "Head of Governance", "Engineering": "Head of Engineering",
    "AI": "Head of AI Engineering", "Security": "CISO",
    "Cloud_And_DevOps": "Head of Platform", "Quality": "Head of Quality",
    "Business": "Head of Business Operations",
}


def slug(text: str) -> str:
    text = text.replace("&", "and").replace("/", " ").replace("+", " plus ")
    return re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_").upper()


def bullets(items):
    return "\n".join(f"- {i}" for i in items) if items else "- Not applicable."


def checks(items):
    return "\n".join(f"- [ ] {i}" for i in items)


def table(headers, rows):
    h = "| " + " | ".join(headers) + " |"
    s = "| " + " | ".join("---" for _ in headers) + " |"
    b = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{h}\n{s}\n{b}"


def fm(doc_id, title, group, owner):
    tags = "\n".join(f"  - {t}" for t in
                     ["rule", group.lower().replace("_", "-"), slug(title).lower()])
    std = "\n".join(f"  - {s}" for s in STANDARDS)
    rel = "\n".join(f"  - {r}" for r in
                    ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md", PROMPT])
    return ("---\n"
            f"id: {doc_id}\ntitle: {title}\ndocument_type: Rule\n"
            f"category: {group.replace('_', ' ')}\nphase: Phase 06\nowner: {owner}\n"
            "status: Published\nlifecycle: Active\nclassification: Internal\n"
            f"version: {VERSION}\ncreated: {DATE}\nupdated: {DATE}\n"
            f"tags:\n{tags}\nrelated_documents:\n{rel}\nstandards:\n{std}\n---")


def build(doc_id, title, group, from_dir) -> str:
    t = TOPICS[topic_key(title + " Rule")]
    what = t["what"]
    gowner = GROUP_OWNER[group]

    def rl(target):
        return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")

    def ph(n, name):
        rels = {6: "PHASE_06_RULES", 7: "PHASE_07_CHECKLISTS", 8: "PHASE_08_PLAYBOOKS",
                9: "PHASE_09_TEMPLATES", 10: "PHASE_10_KNOWLEDGE",
                5: "PHASE_05_SKILLS", 4: "PHASE_04_DEPARTMENT_SPECIFICATIONS"}
        return os.path.relpath(OUT.parent / rels[n] / "README.md",
                               from_dir).replace(os.sep, "/")

    defs = t.get("defs", [])
    std_rows = [[s, "Applies to this rule."] for s in t.get("standards", [])] or \
               [["ISO 27001", "Information security baseline."]]

    nav = (f"> **Navigate:** [Home]({rl('README.md')}) · "
           f"[Catalogue]({rl('ROOT_INDEX.md')}) · "
           f"[All Rules]({os.path.relpath(OUT / 'README.md', from_dir).replace(os.sep, '/')}) · "
           f"[Phase 06 Prompt]({rl(PROMPT)})")

    ownership = table(["Role", "Assignment"], [
        ["Rule Owner", gowner],
        ["Rule Approver", OWNER],
        ["Mandatory Reviewers", "Security Engineer, Compliance Specialist"],
        ["Roles Required to Follow", "All contributors within scope (human and AI)"],
        ["Roles Allowed to Override", f"{gowner} (with documented exception)"],
        ["Escalation Authority", "Governance Division"],
    ])

    P = [
        fm(doc_id, f"{title} Rule", group, gowner), "",
        f"# {title} Rule", "", nav, "",
        f"**Rule ID:** {doc_id}  •  **Category:** {group.replace('_', ' ')}", "",
        "## Executive Summary", "",
        f"This rule is the single source of truth for **{title}** in the AIBOS "
        f"Enterprise. {what} It is mandatory within its scope and inherits the "
        "[root standards](" + rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md') + ").", "",
        "## Purpose", "",
        f"To set clear, enforceable, measurable expectations for {title.lower()} so "
        "that human teams and AI agents act consistently and safely.", "",
        "## Scope", "",
        "Applies to all teams, services and AI agents that perform or affect "
        f"{title.lower()} across the enterprise. Concerns owned by other rules are "
        "referenced rather than duplicated.", "",
        "## Business Rationale", "",
        f"{what} Getting this right reduces risk, rework and cost while increasing "
        "trust, speed and compliance.", "",
        "## Technical Rationale", "",
        "Consistent, automated enforcement makes outcomes predictable, auditable and "
        "safe to scale across humans and AI agents.", "",
        "## Definitions", "",
        bullets([f"**{term}** — {d}" for term, d in defs]) if defs
        else "See the [Enterprise Glossary]("
             + rl('00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md') + ").", "",
        "## Mandatory Requirements (MUST)", "", bullets(t.get("must", [])), "",
        "## Recommended Practices (SHOULD)", "", bullets(t.get("should", [])), "",
        "## Optional Practices (MAY)", "", bullets(t.get("may", [])), "",
        "## Rule Ownership Matrix", "", ownership, "",
        "## Applicable Departments", "",
        f"All departments performing {title.lower()}. See the "
        f"[Department Specifications]({ph(4, '')}).", "",
        "## Applicable Skills", "",
        f"Roles that must follow this rule are defined in the "
        f"[Specialist Skills]({ph(5, '')}).", "",
        "## Related Rules", "",
        f"See other rules in the [Enterprise Rules catalogue]({ph(6, '')}).", "",
        "## Related Checklists", "",
        f"Validated via the [Enterprise Checklists]({ph(7, '')}).", "",
        "## Related Playbooks", "",
        f"Operationalised through the [Enterprise Playbooks]({ph(8, '')}).", "",
        "## Related Templates", "",
        f"Supported by the [Enterprise Templates]({ph(9, '')}).", "",
        "## Related Knowledge Articles", "",
        f"Explained in the [Enterprise Knowledge base]({ph(10, '')}).", "",
        "## Security Considerations", "",
        "Apply Security by Design, least privilege and Zero Trust. Protect secrets "
        "and follow OWASP ASVS and the OWASP LLM Top 10 where AI is involved.", "",
        "## Privacy Considerations", "",
        "Apply data minimisation, purpose limitation and retention controls to any "
        "personal data touched by this rule.", "",
        "## AI Considerations", "",
        "Where AI agents apply this rule, keep a human in the loop for high-risk "
        "actions, maintain audit trails and mitigate hallucination.", "",
        "## Compliance Requirements", "", table(["Standard", "Application"], std_rows), "",
        "## Exceptions Process", "",
        f"Exceptions MUST be requested from the rule owner ({gowner}), be "
        "time-boxed, risk-assessed and recorded. Unapproved deviations are "
        "non-compliant.", "",
        "## Approval Authority", "",
        f"This rule is approved by the {OWNER}; exceptions are approved by {gowner}.", "",
        "## Enforcement Model", "",
        "Enforced through automated checks in CI, peer review and the related "
        "checklists. Violations are flagged, tracked and remediated.", "",
        "## Metrics", "", bullets(t.get("metrics", [])), "",
        "## KPIs", "", bullets(t.get("metrics", [])), "",
        "## Risks", "", bullets(t.get("risks", [])), "",
        "## Anti-patterns", "", bullets(t.get("anti", [])), "",
        "## Best Practices", "", bullets(t.get("best", [])), "",
        "## Acceptance Criteria", "",
        bullets(["All MUST requirements are satisfied.",
                 "Validation checklist passes.",
                 "Ownership and exceptions are documented.",
                 "Cross-references resolve."]), "",
        "## Validation Checklist", "",
        checks(t.get("checks", []) + [
            "RFC-2119 keywords used correctly.",
            "Cross-references resolve to existing documents.",
            "No secrets or sensitive data exposed.",
            "Version history updated."]), "",
        "## References", "",
        bullets([
            f"[AIBOS Root Specification]({rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')})",
            f"[Enterprise Glossary]({rl('00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md')})",
            f"[Repository Catalogue (ROOT_INDEX)]({rl('ROOT_INDEX.md')})",
            f"[Phase 06 Master Prompt]({rl(PROMPT)})"]), "",
        "## Version History", "",
        table(["Version", "Date", "Summary"],
              [[VERSION, DATE, "Complete, ready-to-use rule."]]), "",
    ]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(P)).rstrip() + "\n"
    return text


def main() -> None:
    counter = 1
    written = 0
    for group, items in GROUPS.items():
        for i, title in enumerate(items, start=1):
            path = OUT / group / f"{i:02d}_{slug(title + ' Rule')}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build(f"RULE-{counter:06d}", title, group, path.parent),
                            encoding="utf-8")
            counter += 1
            written += 1
    print(f"Wrote {written} complete rule documents to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
