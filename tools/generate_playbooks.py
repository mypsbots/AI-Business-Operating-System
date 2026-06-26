#!/usr/bin/env python3
"""Generate complete, ready-to-use Phase 08 PLAYBOOK documents from content_kb.

Each playbook is a repeatable, automatable workflow executable by humans and AI
agents: triggers, roles, a step-by-step procedure, a Mermaid diagram, decision
branches, exception handling, integrations, KPIs/SLAs and continuous improvement.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from content_kb import TOPICS, topic_key

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS" / "PHASE_08_PLAYBOOKS"
OWNER = "Chief Operations Architect"
PROMPT = "01_PHASES/PHASE_08_PLAYBOOKS_MASTER_PROMPT.md"
STANDARDS = ["ISO 42001", "ISO 27001", "NIST AI RMF", "SOC 2", "OWASP ASVS",
             "OWASP LLM Top 10", "WCAG 2.2 AA"]

GROUPS = {
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


def slug(text):
    text = text.replace("&", "and").replace("/", " ").replace("+", " plus ")
    return re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_").upper()


def bullets(items):
    return "\n".join(f"- {i}" for i in items) if items else "- Not applicable."


def numbered(items):
    return "\n".join(f"{n}. {x}" for n, x in enumerate(items, start=1))


def checks(items):
    return "\n".join(f"- [ ] {i}" for i in items)


def table(headers, rows):
    h = "| " + " | ".join(headers) + " |"
    s = "| " + " | ".join("---" for _ in headers) + " |"
    b = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{h}\n{s}\n{b}"


def fm(doc_id, title, group):
    tags = "\n".join(f"  - {t}" for t in
                     ["playbook", group.lower().replace("_", "-"), slug(title).lower()])
    std = "\n".join(f"  - {s}" for s in STANDARDS)
    rel = "\n".join(f"  - {r}" for r in
                    ["ROOT_INDEX.md", "00_ROOT/AIBOS_ROOT_SPECIFICATION.md", PROMPT])
    return ("---\n"
            f"id: {doc_id}\ntitle: {title}\ndocument_type: Playbook\n"
            f"category: {group.replace('_', ' ')}\nphase: Phase 08\nowner: {OWNER}\n"
            "status: Published\nlifecycle: Active\nclassification: Internal\n"
            f"version: {VERSION}\ncreated: {DATE}\nupdated: {DATE}\n"
            f"tags:\n{tags}\nrelated_documents:\n{rel}\nstandards:\n{std}\n---")


def mermaid(steps):
    lines = ["```mermaid", "flowchart TD", "    S([Trigger]) --> A0"]
    prev = "A0"
    for idx, (actor, action) in enumerate(steps):
        node = f"A{idx}"
        label = action.replace('"', "'")[:48]
        lines.append(f'    {node}["{actor}: {label}"]')
        if idx > 0:
            lines.append(f"    A{idx - 1} --> {node}")
    lines.append(f"    {prev if len(steps) <= 1 else 'A' + str(len(steps) - 1)} "
                 "--> D{High-risk?}")
    lines.append("    D -->|Yes| H[Human approval]")
    lines.append("    D -->|No| E[Execute]")
    lines.append("    H --> E --> R([Record audit trail])")
    lines.append("```")
    return "\n".join(lines)


def default_steps(title):
    return [("Owner", f"Initiate {title.lower()} and confirm preconditions."),
            ("Team / AI agent", f"Perform the core {title.lower()} work."),
            ("Reviewer", "Validate against the relevant checklist and rules."),
            ("Approver", "Approve; record outcome and audit trail.")]


def build(doc_id, title, group, from_dir):
    t = TOPICS[topic_key(title + " Playbook")]
    steps = t.get("steps") or default_steps(title)
    triggers = t.get("triggers") or [f"A request to perform {title.lower()}",
                                      "A scheduled cycle"]

    def rl(target):
        return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")

    def ph(n):
        rels = {5: "PHASE_05_SKILLS", 6: "PHASE_06_RULES", 7: "PHASE_07_CHECKLISTS",
                9: "PHASE_09_TEMPLATES", 10: "PHASE_10_KNOWLEDGE"}
        return os.path.relpath(OUT.parent / rels[n] / "README.md",
                               from_dir).replace(os.sep, "/")

    nav = (f"> **Navigate:** [Home]({rl('README.md')}) · "
           f"[Catalogue]({rl('ROOT_INDEX.md')}) · "
           f"[All Playbooks]({os.path.relpath(OUT / 'README.md', from_dir).replace(os.sep, '/')}) · "
           f"[Phase 08 Prompt]({rl(PROMPT)})")

    step_rows = [[str(i), a, act] for i, (a, act) in enumerate(steps, start=1)]

    P = [
        fm(doc_id, f"{title} Playbook", group), "",
        f"# {title} Playbook", "", nav, "",
        f"**Playbook ID:** {doc_id}  •  **Category:** {group.replace('_', ' ')}", "",
        "## Executive Summary", "",
        f"A repeatable, automatable workflow for **{title}**. {t['what']} It is "
        "executable by human teams and AI agents with clear human-approval points.", "",
        "## Business Objective", "",
        f"Make {title.lower()} consistent, fast, safe and auditable across the "
        "enterprise.", "",
        "## Scope", "",
        f"Covers the end-to-end {title.lower()} workflow. Out-of-scope concerns are "
        "delegated to their own playbooks.", "",
        "## Trigger Conditions", "", bullets(triggers), "",
        "## Preconditions", "",
        bullets(["Required inputs, access and approvals are available.",
                 "Relevant rules and checklists are known."]), "",
        "## Inputs", "",
        bullets(["The request/context that triggered the workflow.",
                 "Relevant data, artefacts and configuration."]), "",
        "## Outputs", "",
        bullets(["The completed outcome of the workflow.",
                 "Evidence, audit trail and any follow-up actions."]), "",
        "## Roles Responsible", "",
        bullets(sorted({a for a, _ in steps})), "",
        "## AI Agents Involved", "",
        bullets(["Task agent(s) that execute eligible steps.",
                 "Reviewer/evaluator agent that checks outputs.",
                 "Orchestrator that coordinates and escalates."]), "",
        "## Human Approval Points", "",
        bullets(["Before any high-risk or irreversible action.",
                 "At the final approval/sign-off step."]), "",
        "## Workflow Overview", "",
        f"The workflow proceeds through {len(steps)} main steps with a decision point "
        "that routes high-risk actions to human approval.", "",
        "## Mermaid Workflow Diagram", "", mermaid(steps), "",
        "## Step-by-Step Procedure", "",
        table(["Step", "Actor", "Action"], step_rows), "",
        "## Decision Branches", "",
        bullets(["If the action is high-risk or irreversible -> require human approval.",
                 "If validation fails -> remediate and repeat the step.",
                 "If blocked -> follow the escalation path."]), "",
        "## Exception Handling", "",
        bullets(["Capture the error and context.",
                 "Apply the documented fallback or safe-stop.",
                 "Open an incident if customer impact is possible."]), "",
        "## Escalation Path", "",
        "Owner -> domain lead -> Governance Division, with severity-based timelines.", "",
        "## Required Skills", "",
        f"Executed by holders of the relevant [Specialist Skills]({ph(5)}).", "",
        "## Required Rules", "",
        f"Must comply with the [Enterprise Rules]({ph(6)}).", "",
        "## Required Checklists", "",
        f"Validated using the [Enterprise Checklists]({ph(7)}).", "",
        "## Required Templates", "",
        f"Uses the [Enterprise Templates]({ph(9)}).", "",
        "## Required Knowledge Articles", "",
        f"Background in the [Enterprise Knowledge base]({ph(10)}).", "",
        "## Automation Opportunities", "",
        bullets(["Automate repeatable steps and validations in CI/CD or workflows.",
                 "Use AI agents for drafting, triage and checks.",
                 "Auto-collect evidence and update tracking systems."]), "",
        "## Integration Points", "",
        bullets(["GitHub / GitLab (code, PRs, actions).",
                 "Jira / Linear (tracking).", "Slack / Teams (notifications).",
                 "Vercel / cloud (deploy).", "n8n / Make (orchestration)."]), "",
        "## KPIs", "", bullets(t.get("metrics", ["Cycle time", "Success rate"])), "",
        "## SLAs", "",
        bullets(["Acknowledge triggers within 1 business day.",
                 "Complete standard runs within the agreed target time.",
                 "Resolve exceptions per severity SLA."]), "",
        "## Risks", "", bullets(t.get("risks", ["Inconsistent or unsafe execution."])),
        "",
        "## Best Practices", "", bullets(t.get("best", ["Automate.", "Measure.",
                                                        "Keep humans in the loop."])), "",
        "## Anti-patterns", "", bullets(t.get("anti", ["Skipping validation.",
                                                       "No audit trail."])), "",
        "## Definition of Done", "",
        bullets(["Outcome achieved and validated.",
                 "Audit trail recorded.",
                 "Follow-up actions tracked."]), "",
        "## Acceptance Criteria", "",
        bullets(["All steps completed or consciously skipped with reason.",
                 "Required checklist passed.",
                 "Approvals obtained."]), "",
        "## Post-Implementation Review", "",
        "Review outcomes against objectives; capture lessons and improvement actions.", "",
        "## Continuous Improvement", "",
        "Feed metrics and lessons back into this playbook; update on a regular cadence.", "",
        "## Validation Checklist", "",
        checks(["Trigger and preconditions verified.",
                "Steps executed in order with evidence.",
                "Human approval obtained for high-risk actions.",
                "Required checklist passed.",
                "Audit trail recorded.",
                "Cross-references resolve."]), "",
        "## References", "",
        bullets([
            f"[AIBOS Root Specification]({rl('00_ROOT/AIBOS_ROOT_SPECIFICATION.md')})",
            f"[Repository Catalogue (ROOT_INDEX)]({rl('ROOT_INDEX.md')})",
            f"[Phase 08 Master Prompt]({rl(PROMPT)})"]), "",
        "## Version History", "",
        table(["Version", "Date", "Summary"],
              [[VERSION, DATE, "Complete, ready-to-use playbook."]]), "",
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(P)).rstrip() + "\n"


def main():
    counter = 1
    written = 0
    for group, items in GROUPS.items():
        for i, title in enumerate(items, start=1):
            path = OUT / group / f"{i:02d}_{slug(title + ' Playbook')}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build(f"PLAY-{counter:06d}", title, group, path.parent),
                            encoding="utf-8")
            counter += 1
            written += 1
    print(f"Wrote {written} complete playbook documents to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
