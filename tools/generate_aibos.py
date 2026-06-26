#!/usr/bin/env python3
"""AIBOS Enterprise v2.0 artefact generator.

Generates schema-compliant Markdown artefacts for Phases 1-20 from the
master prompts under ``01_PHASES``. Output is written to ``02_ARTEFACTS``.

Design goals:
- Deterministic, idempotent (skips files that already exist unless --overwrite).
- Every document includes YAML front matter and all required sections per phase.
- Output is markdownlint-clean (blank lines around headings, lists, tables,
  fenced code blocks; single trailing newline; no trailing whitespace).

This embodies the "Documentation as Code" principle from
AIBOS_ROOT_SPECIFICATION.md.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
from pathlib import Path

DATE = "2026-06-26"
VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "02_ARTEFACTS"

STANDARDS = [
    "ISO 42001",
    "ISO 27001",
    "NIST AI RMF",
    "SOC 2",
    "OWASP ASVS",
    "OWASP LLM Top 10",
    "WCAG 2.2 AA",
]


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def slug(text: str) -> str:
    """Convert a title to an UPPER_SNAKE_CASE filename component."""
    text = text.replace("&", "and").replace("/", " ").replace("+", " plus ")
    text = re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_")
    return text.upper()


def front_matter(doc_id: str, title: str, doc_type: str, category: str,
                 phase: str, owner: str, tags: list[str],
                 related: list[str]) -> str:
    tag_lines = "\n".join(f"  - {t}" for t in tags) or "  - aibos"
    rel_lines = "\n".join(f"  - {r}" for r in related) or "  - AIBOS_ROOT_SPECIFICATION.md"
    std_lines = "\n".join(f"  - {s}" for s in STANDARDS)
    return (
        "---\n"
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
        "---"
    )


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def checkboxes(items: list[str]) -> str:
    return "\n".join(f"- [ ] {i}" for i in items)


def table(headers: list[str], rows: list[list[str]]) -> str:
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{head}\n{sep}\n{body}"


def fenced(lang: str, code: str) -> str:
    return f"```{lang}\n{code.strip()}\n```"


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

VERSION_TABLE = table(
    ["Version", "Date", "Summary"],
    [[VERSION, DATE, "Initial generated artefact."]],
)


# --------------------------------------------------------------------------- #
# Section content builder
# --------------------------------------------------------------------------- #
def build_section(name: str, ctx: dict) -> str:
    title = ctx["title"]
    phase = ctx["phase"]
    n = name.lower()

    # Structured renderings by pattern -------------------------------------- #
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
    if n == "yaml schema" or n == "required metadata" or n == "metadata schema":
        return fenced("yaml", """
id: DOC-000000
title: Example
version: 2.0.0
owner: Owning Team
classification: Internal
""")
    if n in ("example completed template", "sample usage", "examples", "package manifest"):
        return fenced("yaml", f"""
# Example for: {title}
name: example
version: {VERSION}
status: draft
""")
    if "raci" in n:
        return table(
            ["Activity", "Responsible", "Accountable", "Consulted", "Informed"],
            [["Primary task", "Specialist", "Department Lead", "Architecture", "Stakeholders"]],
        )
    if "matrix" in n:
        return table(
            ["Partner", "Interaction", "Direction"],
            [["Upstream owners", "Provide inputs", "Inbound"],
             ["Downstream consumers", "Consume outputs", "Outbound"],
             ["Governance", "Review and approve", "Bidirectional"]],
        )
    if "30/60/90" in n or "roadmap" in n:
        return table(
            ["Horizon", "Focus", "Outcome"],
            [["0-30 days", "Discover and assess", "Baseline established"],
             ["31-60 days", "Design and build", "Pilot delivered"],
             ["61-90 days", "Validate and scale", "Production rollout"]],
        )
    if n == "mandatory requirements (must)":
        return bullets([
            f"The team MUST apply the AIBOS root standards when implementing {title}.",
            "The team MUST validate every artefact before publication.",
            "The team MUST require human approval for high-risk actions.",
            "The team MUST maintain an auditable trail of decisions.",
        ])
    if n == "recommended practices (should)":
        return bullets([
            "Teams SHOULD automate repeatable validation where practical.",
            "Teams SHOULD reuse existing artefacts before creating new ones.",
            "Teams SHOULD capture metrics to drive continuous improvement.",
        ])
    if n == "optional practices (may)":
        return bullets([
            "Teams MAY extend this artefact for domain-specific needs.",
            "Teams MAY add additional tooling integrations.",
        ])
    if n in ("standards mapping", "compliance mapping", "compliance requirements",
             "compliance controls", "external standards"):
        return table(
            ["Standard", "Application"],
            [["ISO 42001", "AI management system alignment."],
             ["ISO 27001", "Information security controls."],
             ["NIST AI RMF", "AI risk management."],
             ["OWASP LLM Top 10", "LLM threat mitigation."]],
        )
    if n == "faqs":
        return ("**Q: How does this artefact relate to the AIBOS standards?**\n\n"
                "A: It inherits and must not contradict the root standards.\n\n"
                f"**Q: Who owns {title}?**\n\n"
                f"A: {ctx['owner']}.")
    if n == "definitions":
        return bullets([
            "Refer to `00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md` for canonical terms.",
            "No terminology is redefined within this document.",
        ])
    if (n.startswith("required ") or n.startswith("related ")
            or n.startswith("applicable ") or n.startswith("supporting ")
            or n.startswith("governing ") or n.endswith("mapping")
            or n in ("upstream dependencies", "downstream consumers",
                     "dependencies", "knowledge dependencies",
                     "required industry blueprints", "related industry blueprints")):
        return bullets([
            "Inherits all root standards under `00_ROOT/`.",
            "Cross-references the relevant Phase artefacts under `02_ARTEFACTS/`.",
            "See `ROOT_INDEX.md` for the full catalogue.",
        ])
    if n in ("kpis", "metrics", "quality metrics", "success metrics",
             "okrs", "slas", "slos", "slas/slos", "roi metrics", "roi model",
             "maturity indicators", "performance targets"):
        return bullets([
            "Coverage and completeness of the artefact.",
            "Validation pass rate (target 95%+).",
            "Cycle time from draft to approval.",
            "Reuse rate across the enterprise.",
        ])
    if n == "validation rules":
        return bullets([
            "All placeholders are resolved before use.",
            "Required metadata fields are populated.",
            "Output conforms to the AIBOS Document Schema.",
        ])

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
            f"{title} exists to deliver measurable value while upholding the "
            "AIBOS principles of security, privacy and accountability.",
        "business value":
            "Reduced duplication, faster safe delivery, improved compliance "
            "posture and scalable AI augmentation.",
        "objectives":
            bullets(["Establish a clear, governed definition.",
                     "Enable consistent execution by humans and AI agents.",
                     "Provide measurable acceptance criteria."]),
        "responsibilities":
            bullets(["Own and maintain this artefact.",
                     "Ensure alignment with root standards.",
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
        "acceptance criteria":
            bullets(["All mandatory sections are complete.",
                     "Validation passes with no errors.",
                     "Cross-references are valid."]),
        "security responsibilities":
            "Apply Security by Design, least privilege and Zero Trust; protect "
            "secrets; follow OWASP ASVS and the OWASP LLM Top 10.",
        "ai responsibilities":
            "Maintain human-in-the-loop controls, minimise hallucinations, prefer "
            "verified knowledge and preserve audit trails.",
        "compliance responsibilities":
            "Map controls to ISO 27001, ISO 42001 and SOC 2; retain evidence for "
            "audit.",
        "security controls":
            bullets(["Authentication and authorisation enforced.",
                     "Encryption in transit and at rest.",
                     "Audit logging and monitoring."]),
        "privacy controls":
            bullets(["Data minimisation.", "Purpose limitation.",
                     "Retention and secure deletion policies."]),
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
    }
    if n in narrative:
        return narrative[n]

    # Generic fallback ------------------------------------------------------ #
    return (f"This section ({name}) for **{title}** is defined in line with the "
            f"AIBOS root standards and the governing {phase} master prompt. "
            "See `ROOT_INDEX.md` for related artefacts and `00_ROOT/` for the "
            "inherited standards.")


def render(doc_id: str, title: str, doc_type: str, category: str, phase: str,
           owner: str, sections: list[str], tags: list[str],
           related: list[str]) -> str:
    ctx = {"title": title, "phase": phase, "owner": owner}
    parts = [front_matter(doc_id, title, doc_type, category, phase, owner, tags, related),
             "", f"# {title}", ""]
    for s in sections:
        parts.append(f"## {s}")
        parts.append("")
        parts.append(build_section(s, ctx).strip())
        parts.append("")
    text = "\n".join(parts)
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
    return text


# Hand-authored documents that must never be overwritten by the generator.
PROTECTED = {
    "PHASE_01_ENTERPRISE_ARCHITECTURE/01_ENTERPRISE_VISION.md",
    "PHASE_01_ENTERPRISE_ARCHITECTURE/02_BUSINESS_CAPABILITIES.md",
    "PHASE_01_ENTERPRISE_ARCHITECTURE/03_OPERATING_MODEL.md",
}


def write(path: Path, content: str, overwrite: bool, stats: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rel = path.relative_to(OUT).as_posix()
    if rel in PROTECTED:
        stats["skipped"] += 1
        return
    if path.exists() and not overwrite:
        stats["skipped"] += 1
        return
    path.write_text(content, encoding="utf-8")
    stats["written"] += 1


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
             tags, overwrite, stats):
    base = OUT / folder
    for i, title in enumerate(items, start=1):
        doc_id = f"{prefix}-{i:06d}"
        fname = f"{i:02d}_{slug(title)}.md"
        content = render(doc_id, title, doctype, category, phase, owner,
                         sections, tags, ["AIBOS_ROOT_SPECIFICATION.md"])
        write(base / fname, content, overwrite, stats)


def gen_grouped(folder, prefix, doctype, owner, phase, groups, sections,
                tags, overwrite, stats, suffix=""):
    counter = 1
    for group, items in groups.items():
        gdir = OUT / folder / group
        for i, title in enumerate(items, start=1):
            full_title = f"{title}{suffix}"
            doc_id = f"{prefix}-{counter:06d}"
            fname = f"{i:02d}_{slug(full_title)}.md"
            content = render(doc_id, full_title, doctype, group.replace('_', ' '),
                             phase, owner, sections, tags,
                             ["AIBOS_ROOT_SPECIFICATION.md"])
            write(gdir / fname, content, overwrite, stats)
            counter += 1


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()
    ow = args.overwrite
    stats = {"written": 0, "skipped": 0}

    gen_flat("PHASE_01_ENTERPRISE_ARCHITECTURE", "ARCH", "Architecture",
             "Enterprise Architecture", "Office of the Chief Enterprise Architect",
             "Phase 01", PHASE1, S[1], ["enterprise-architecture"], ow, stats)

    gen_flat("PHASE_02_ENTERPRISE_SPECIFICATIONS", "SPEC", "Specification",
             "Enterprise Specification", "Office of the Chief Enterprise Architect",
             "Phase 02", PHASE2, S[2], ["specification"], ow, stats)

    gen_flat("PHASE_03_DIVISION_SPECIFICATIONS", "DIV", "Specification",
             "Division Specification", "Division Leadership", "Phase 03",
             PHASE3, S[3], ["division"], ow, stats)

    gen_grouped("PHASE_04_DEPARTMENT_SPECIFICATIONS", "DEPT", "Specification",
                "Department Leadership", "Phase 04", PHASE4, S[4],
                ["department"], ow, stats, suffix=" Department")

    gen_flat("PHASE_05_SKILLS", "SKILL", "Skill", "Specialist Skill",
             "Chief Skills Architect", "Phase 05",
             [f"{r} Skill" for r in PHASE5_ROLES], S[5], ["skill"], ow, stats)

    gen_grouped("PHASE_06_RULES", "RULE", "Rule", "Chief Governance Architect",
                "Phase 06", PHASE6, S[6], ["rule"], ow, stats, suffix=" Rule")

    gen_grouped("PHASE_07_CHECKLISTS", "CHECK", "Checklist",
                "Chief Quality and Compliance Architect", "Phase 07", PHASE7, S[7],
                ["checklist"], ow, stats, suffix=" Checklist")

    gen_grouped("PHASE_08_PLAYBOOKS", "PLAY", "Playbook",
                "Chief Operations Architect", "Phase 08", PHASE8, S[8],
                ["playbook"], ow, stats, suffix=" Playbook")

    gen_grouped("PHASE_09_TEMPLATES", "TEMP", "Template",
                "Chief Documentation and Knowledge Architect", "Phase 09", PHASE9,
                S[9], ["template"], ow, stats, suffix=" Template")

    gen_grouped("PHASE_10_KNOWLEDGE", "KNOW", "Knowledge", "Chief Knowledge Architect",
                "Phase 10", PHASE10, S[10], ["knowledge"], ow, stats,
                suffix=" Knowledge Article")

    gen_grouped("PHASE_11_AI_AGENT_COLLABORATION", "AGENT", "Framework",
                "Chief AI Systems Architect", "Phase 11", PHASE11, S[11],
                ["ai-agent"], ow, stats)

    gen_grouped("PHASE_12_AUTOMATION", "AUTO", "Framework",
                "Chief Automation Architect", "Phase 12", PHASE12, S[12],
                ["automation"], ow, stats)

    # Phase 13: industry x 10 docs
    counter = 1
    for ind in PHASE13_INDUSTRIES:
        idir = OUT / "PHASE_13_INDUSTRY_BLUEPRINTS" / slug(ind)
        for i, d in enumerate(PHASE13_DOCS, start=1):
            title = f"{ind} {d}"
            doc_id = f"IND-{counter:06d}"
            fname = f"{i:02d}_{slug(d)}.md"
            content = render(doc_id, title, "Blueprint", ind, "Phase 13",
                             "Chief Industry Solutions Architect", S[13],
                             ["industry-blueprint"], ["AIBOS_ROOT_SPECIFICATION.md"])
            write(idir / fname, content, ow, stats)
            counter += 1

    gen_grouped("PHASE_14_ACCELERATOR_PACKS", "ACCEL", "Accelerator",
                "Chief Transformation Architect", "Phase 14", PHASE14, S[14],
                ["accelerator"], ow, stats, suffix=" Accelerator Pack")
    # Industry accelerator packs
    idir = OUT / "PHASE_14_ACCELERATOR_PACKS" / "Industry"
    for i, ind in enumerate(PHASE13_INDUSTRIES, start=1):
        title = f"{ind} Accelerator Pack"
        content = render(f"ACCEL-9{i:05d}", title, "Accelerator", "Industry",
                         "Phase 14", "Chief Transformation Architect", S[14],
                         ["accelerator"], ["AIBOS_ROOT_SPECIFICATION.md"])
        write(idir / f"{i:02d}_{slug(title)}.md", content, ow, stats)

    gen_grouped("PHASE_15_REFERENCE_IMPLEMENTATIONS", "IMPL", "Implementation",
                "Chief Solution Architect", "Phase 15", PHASE15, S[15],
                ["reference-implementation"], ow, stats)

    gen_grouped("PHASE_16_SDK_CLI", "SDK", "Component", "Chief Platform Engineer",
                "Phase 16", PHASE16, S[16], ["sdk-cli"], ow, stats)

    gen_grouped("PHASE_17_CERTIFICATION", "CERT", "Certification",
                "Chief Governance Audit and Certification Architect", "Phase 17",
                PHASE17, S[17], ["certification"], ow, stats)

    gen_grouped("PHASE_18_MARKETPLACE", "MKT", "Marketplace",
                "Chief Platform Ecosystem Architect", "Phase 18", PHASE18, S[18],
                ["marketplace"], ow, stats)

    gen_grouped("PHASE_19_REFERENCE_ORGANISATION", "ORG", "Organisation",
                "Chief Enterprise Transformation Architect", "Phase 19", PHASE19,
                S[19], ["reference-organisation"], ow, stats)

    gen_grouped("PHASE_20_META_ORCHESTRATOR", "META", "Framework",
                "Chief Autonomous Systems Architect", "Phase 20", PHASE20, S[20],
                ["meta-orchestrator"], ow, stats)

    print(f"Written: {stats['written']}  Skipped: {stats['skipped']}")


if __name__ == "__main__":
    main()
