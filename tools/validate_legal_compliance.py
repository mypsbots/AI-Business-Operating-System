#!/usr/bin/env python3
"""Static validation for the Lemuran Legal & Compliance skill set.

Runs structural / coverage checks that CAN be verified without a live runtime:

* all 25 catalogue capabilities have a rendered specification;
* each specification declares the mandated sections (triggers, inputs, outputs,
  dependencies, sources, guardrails, decision authority + approval gates,
  review triggers, tests, company-facts, implementation status);
* each catalogue ``knowledge_ref`` resolves inside the integrated pack;
* each referenced acceptance-test fixture exists and is valid JSON;
* the machine-readable manifest matches the rendered docs.

This is explicitly NOT a live-agent test. Exit code 0 = all checks pass.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PACK = REPO / "02_ARTEFACTS/PHASE_10_KNOWLEDGE/Business/LEMURAN_UK_LEGAL_PACK"
OUT = REPO / "02_ARTEFACTS/PHASE_05_SKILLS/Legal_Compliance_UK"

REQUIRED_SECTIONS = [
    "## Legal Notice", "## Overview", "## Scope and Applicability",
    "## Triggers", "## Required Inputs", "## Outputs", "## Knowledge Sources",
    "## Dependencies", "## Guardrails",
    "## Decision Authority and Human Approval Gates", "## Review Triggers",
    "## Acceptance Tests", "## Company Facts Required", "## Implementation Status",
]


def load_catalogue() -> dict:
    raw = (PACK / "15_SKILL_CATALOGUE.md").read_text(encoding="utf-8")
    return json.loads(re.search(r"```json\s*(.*?)```", raw, re.DOTALL).group(1))


def domain_of(sid: str) -> str:
    return sid.replace("LEMURAN-UK-", "")


def main() -> int:
    cat = load_catalogue()
    skills = cat["skills"]
    checks: list[tuple[bool, str]] = []

    def check(cond: bool, label: str) -> None:
        checks.append((bool(cond), label))

    # 1. Coverage: one rendered doc per catalogue skill.
    manifest = json.loads((OUT / "LEGAL_SKILL_CATALOGUE.json").read_text())
    rendered = {m["id"]: m["doc"] for m in manifest["skills"]}
    check(len(skills) == 25, f"catalogue has 25 capabilities (found {len(skills)})")
    check(len(rendered) == 25, f"manifest lists 25 skills (found {len(rendered)})")

    for i, s in enumerate(skills, 1):
        sid = s["id"]
        doc = OUT / f"{i:02d}_{domain_of(sid)}_SKILL.md"
        check(doc.exists(), f"{sid}: specification file exists ({doc.name})")
        if not doc.exists():
            continue
        text = doc.read_text(encoding="utf-8")
        missing = [sec for sec in REQUIRED_SECTIONS if sec not in text]
        check(not missing, f"{sid}: all mandated sections present"
              + (f" (missing {missing})" if missing else ""))
        # knowledge_refs resolve in pack
        for ref in s.get("knowledge_refs", []):
            check((PACK / ref).exists(),
                  f"{sid}: knowledge_ref resolves -> {ref}")
        # declared gates appear in the doc
        for g in s.get("approval_gates", []):
            check(g in text, f"{sid}: approval gate {g} documented")
        # fixtures exist + valid for each acceptance test
        for t in s.get("acceptance_tests", []):
            fx = OUT / "fixtures" / f"{t}.json"
            ok = fx.exists()
            if ok:
                try:
                    json.loads(fx.read_text())
                except Exception:
                    ok = False
            check(ok, f"{sid}: fixture valid -> {t}.json")
        # manifest id matches rendered doc name
        check(rendered.get(sid) == doc.name,
              f"{sid}: manifest points at {doc.name}")

    # 2. Shared assets present.
    check((OUT / "00_COMMON_EXECUTION_CONTRACT.md").exists(),
          "common execution contract present")
    check((OUT / "README.md").exists(), "folder index present")
    check((OUT / "ACCEPTANCE_TESTS.md").exists(), "acceptance test spec present")

    # Report
    passed = sum(1 for ok, _ in checks if ok)
    failed = [lbl for ok, lbl in checks if not ok]
    print(f"Static validation: {passed}/{len(checks)} checks passed.")
    if failed:
        print("\nFAILED:")
        for lbl in failed:
            print(f"  - {lbl}")
        return 1
    print("All structural / coverage checks passed.")
    print("NOTE: semantic legal reasoning and live-agent execution are NOT "
          "tested here and require a bound runtime + human legal review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
