#!/usr/bin/env python3
"""Generate complete, ready-to-use Phase 07 CHECKLIST documents from content_kb.

Each checklist is objective, auditable and binary (Pass/Fail), with topic-specific
validation items plus cross-cutting security, privacy, AI, accessibility,
performance and deployment checks.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from content_kb import TOPICS, topic_key

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS" / "PHASE_07_CHECKLISTS"
OWNER = "Chief Quality and Compliance Architect"
PROMPT = "01_PHASES/PHASE_07_CHECKLISTS_MASTER_PROMPT.md"
STANDARDS = ["ISO 42001", "ISO 27001", "NIST AI RMF", "SOC 2", "OWASP ASVS",
             "OWASP LLM Top 10", "WCAG 2.2 AA"]

GROUPS = {
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

SEC = ["Authentication and authorisation enforced on all sensitive actions.",
       "No secrets or credentials exposed in code, config, logs or output.",
       "Inputs validated and outputs safely encoded.",
       "Dependencies scanned; no unresolved critical vulnerabilities."]
PRIV = ["Personal data is minimised and lawfully processed.",
        "Sensitive data is masked in logs and encrypted at rest/in transit.",
        "Retention and deletion rules are respected."]
AIV = ["AI outputs are grounded/cited where factual.",
       "Human-in-the-loop approval exists for high-risk AI actions.",
       "Prompt-injection and unsafe-output guardrails are in place."]
COMP = ["Relevant controls (ISO 27001/42001, SOC 2) are satisfied.",
        "Evidence is captured and retained for audit.",
        "Exceptions are documented and approved."]
ACC = ["UI meets WCAG 2.2 AA (contrast, labels, keyboard).",
       "Automated accessibility scan passes."]
PERF = ["Performance budgets/SLAs are met (p95/p99).",
        "No unresolved performance regressions."]
DEP = ["Deployment is automated, versioned and traceable.",
       "Post-deploy health checks pass."]
ROLL = ["A tested rollback path exists.",
        "Database changes are backward compatible."]


def slug(text):
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


def fm(doc_id, title, group):
    tags = "\n".join(f"  - {t}" for t in
                     ["checklist", group.lower().replace("_", "-"), slug(title).lower()])
    std = "\n".join(f"  - {s}" for s in STANDARDS)
    rel = "\n".join(f"  - {r}" for r in
                    ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md", PROMPT])
    return ("---\n"
            f"id: {doc_id}\ntitle: {title}\ndocument_type: Checklist\n"
            f"category: {group.replace('_', ' ')}\nphase: Phase 07\nowner: {OWNER}\n"
            "status: Published\nlifecycle: Active\nclassification: Internal\n"
            f"version: {VERSION}\ncreated: {DATE}\nupdated: {DATE}\n"
            f"tags:\n{tags}\nrelated_documents:\n{rel}\nstandards:\n{std}\n---")


def build(doc_id, title, group, from_dir):
    t = TOPICS[topic_key(title + " Checklist")]

    def rl(target):
        return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")

    def ph(n):
        rels = {5: "PHASE_05_SKILLS", 6: "PHASE_06_RULES", 8: "PHASE_08_PLAYBOOKS",
                9: "PHASE_09_TEMPLATES", 10: "PHASE_10_KNOWLEDGE"}
        return os.path.relpath(OUT.parent / rels[n] / "README.md",
                               from_dir).replace(os.sep, "/")

    topic_checks = t.get("checks", t.get("must", []))
    nav = (f"> **Navigate:** [Home]({rl('README.md')}) · "
           f"[Catalogue]({rl('ROOT_INDEX.md')}) · "
           f"[All Checklists]({os.path.relpath(OUT / 'README.md', from_dir).replace(os.sep, '/')}) · "
           f"[Phase 07 Prompt]({rl(PROMPT)})")

    P = [
        fm(doc_id, f"{title} Checklist", group), "",
        f"# {title} Checklist", "", nav, "",
        f"**Checklist ID:** {doc_id}  •  **Category:** {group.replace('_', ' ')}", "",
        "## Purpose", "",
        f"To validate {title.lower()} objectively and repeatably before it passes its "
        "quality gate. Every item is binary (Pass/Fail) and auditable.", "",
        "## Scope", "",
        f"Applies whenever {title.lower()} is performed or reviewed, by human reviewers "
        "or AI agents.", "",
        "## Prerequisites", "",
        bullets(["The relevant rule(s) and standards have been read.",
                 "Required inputs and access are available.",
                 "The artefact under review is complete enough to assess."]), "",
        "## Inputs", "",
        bullets(["The artefact or change under review.",
                 "Relevant requirements, designs and acceptance criteria."]), "",
        "## Outputs", "",
        bullets(["A completed checklist with Pass/Fail per item.",
                 "Recorded evidence and a sign-off decision."]), "",
        "## Roles Responsible", "",
        bullets(["Reviewer (human or AI agent) — performs the checklist.",
                 "Approver — signs off the quality gate.",
                 "Owner of the artefact — remediates failures."]), "",
        "## Quality Gate", "",
        f"This checklist is the gate for {title.lower()}; the artefact MUST NOT "
        "progress until all mandatory items pass.", "",
        "## Acceptance Criteria", "",
        bullets(["All mandatory items pass.",
                 "Evidence is captured for each item.",
                 "Failures are remediated or formally accepted."]), "",
        "## Validation Steps", "", checks(topic_checks), "",
        "## Pass / Fail Criteria", "",
        bullets(["**Pass** — all mandatory items are satisfied with evidence.",
                 "**Fail** — any mandatory item is unmet; remediate and re-run.",
                 "**Conditional** — minor items deferred with an approved exception."]), "",
        "## Evidence Required", "",
        bullets(["Links to passing CI runs, scans or test reports.",
                 "Screenshots or logs demonstrating each check.",
                 "Reviewer and approver identities and timestamps."]), "",
        "## Required Skills", "",
        f"Reviewers should hold the relevant [Specialist Skills]({ph(5)}).", "",
        "## Required Rules", "",
        f"This checklist enforces the [Enterprise Rules]({ph(6)}).", "",
        "## Related Playbooks", "",
        f"Used within the [Enterprise Playbooks]({ph(8)}).", "",
        "## Related Templates", "",
        f"Supported by the [Enterprise Templates]({ph(9)}).", "",
        "## Related Knowledge Articles", "",
        f"Background in the [Enterprise Knowledge base]({ph(10)}).", "",
        "## Security Validation", "", checks(SEC), "",
        "## Privacy Validation", "", checks(PRIV), "",
        "## AI Validation", "", checks(AIV), "",
        "## Compliance Validation", "", checks(COMP), "",
        "## Accessibility Validation", "", checks(ACC), "",
        "## Performance Validation", "", checks(PERF), "",
        "## Deployment Readiness", "", checks(DEP), "",
        "## Rollback Readiness", "", checks(ROLL), "",
        "## Reviewer Sign-off", "",
        table(["Field", "Value"],
              [["Reviewer", "_(name / agent)_"], ["Decision", "Pass / Fail"],
               ["Date", "_(date)_"], ["Notes", "_(notes)_"]]), "",
        "## Escalation Process", "",
        "If items cannot be resolved, escalate to the artefact owner, then to the "
        "governing rule owner, then to the Governance Division.", "",
        "## Risks", "", bullets(t.get("risks", ["Unvalidated work reaches production."])),
        "",
        "## References", "",
        bullets([
            f"[AIBOS Root Specification]({rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')})",
            f"[Repository Catalogue (ROOT_INDEX)]({rl('ROOT_INDEX.md')})",
            f"[Phase 07 Master Prompt]({rl(PROMPT)})"]), "",
        "## Version History", "",
        table(["Version", "Date", "Summary"],
              [[VERSION, DATE, "Complete, ready-to-use checklist."]]), "",
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(P)).rstrip() + "\n"


def main():
    counter = 1
    written = 0
    for group, items in GROUPS.items():
        for i, title in enumerate(items, start=1):
            path = OUT / group / f"{i:02d}_{slug(title + ' Checklist')}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build(f"CHECK-{counter:06d}", title, group, path.parent),
                            encoding="utf-8")
            counter += 1
            written += 1
    print(f"Wrote {written} complete checklist documents to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
