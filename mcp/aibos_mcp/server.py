"""AIBOS Model Context Protocol server.

Exposes the AI Business Operating System repository to AI clients and agents,
with tools designed around two workflows:

1. Client delivery  - scoping AI automation / integration / implementation for
   customers (industry blueprints, accelerator packs, reference implementations).
2. Internal operations - developing and managing company functions (HR, Finance,
   Technology, Sales, Marketing, Strategy, ...) using the framework's
   department specs, rules, checklists, playbooks, templates and knowledge.

Run locally (stdio) for Cursor / Claude Desktop / VS Code, or remotely
(Streamable-HTTP + bearer auth) for ChatGPT, Gemini, Grok, your own app and
your whole team.
"""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from .backends import get_backend
from .config import CONFIG, REPO_ROOT
from .corpus import get_document as _get_document
from .corpus import list_groups

mcp = FastMCP("AIBOS", host=CONFIG.host, port=CONFIG.port)
_backend = get_backend(CONFIG)


def _hits(query: str, top_k: int, **filters: str | None) -> list[dict]:
    clean = {k: v for k, v in filters.items() if v}
    return [h.as_dict() for h in _backend.search(query, top_k=top_k,
                                                  filters=clean or None)]


# --------------------------------------------------------------------------- #
# Core retrieval tools
# --------------------------------------------------------------------------- #
@mcp.tool()
def search_aibos(query: str, top_k: int = 8, phase: str | None = None,
                 category: str | None = None,
                 document_type: str | None = None) -> dict[str, Any]:
    """Semantically search the AIBOS framework and return the most relevant
    artefact sections with their citation path.

    Args:
        query: A natural-language question or topic.
        top_k: Number of sections to return (1-25).
        phase: Optional filter, e.g. "Phase 13" or "Phase 06".
        category: Optional filter, e.g. "Finance", "Sales", "Security".
        document_type: Optional filter, e.g. "Rule", "Checklist", "Playbook",
            "Template", "Knowledge", "Specification", "Blueprint".

    Returns a list of hits, each with title, path (use get_aibos_document to
    open it), phase, category, section, a snippet and a relevance score.
    """
    top_k = max(1, min(int(top_k), 25))
    return {"backend": CONFIG.backend,
            "results": _hits(query, top_k, phase=phase, category=category,
                             document_type=document_type)}


@mcp.tool()
def get_aibos_document(path: str) -> dict[str, Any]:
    """Return the full Markdown of an AIBOS artefact by its repo-relative path
    (the `path` field returned by search_aibos), e.g.
    "02_ARTEFACTS/PHASE_06_RULES/Engineering/01_CODE_REVIEW_RULE.md".
    """
    text = _get_document(path)
    if text is None:
        return {"error": f"Not found or invalid path: {path}"}
    return {"path": path, "content": text}


# --------------------------------------------------------------------------- #
# Navigation / discovery tools
# --------------------------------------------------------------------------- #
_PHASES = [
    ("01", "Enterprise Architecture"), ("02", "Enterprise Specifications"),
    ("03", "Division Specifications"), ("04", "Department Specifications"),
    ("05", "Specialist Skills"), ("06", "Enterprise Rules"),
    ("07", "Enterprise Checklists"), ("08", "Enterprise Playbooks"),
    ("09", "Enterprise Templates"), ("10", "Enterprise Knowledge"),
    ("11", "AI Agent Collaboration"), ("12", "Automation & Improvement"),
    ("13", "Industry Blueprints"), ("14", "Accelerator Packs"),
    ("15", "Reference Implementations"), ("16", "SDK & CLI"),
    ("17", "Certification & Maturity"), ("18", "Marketplace & Extensions"),
    ("19", "Reference AI Organisation"), ("20", "Meta-Orchestrator"),
]


@mcp.tool()
def list_phases() -> list[dict[str, str]]:
    """List the 20 AIBOS phases and what each one covers."""
    return [{"phase": f"Phase {n}", "area": area} for n, area in _PHASES]


@mcp.tool()
def list_departments() -> list[str]:
    """List the company functions/departments available as specifications
    (Phase 04), e.g. Finance, Sales, Marketing, Engineering, Security."""
    return list_groups("PHASE_04_")


@mcp.tool()
def list_industries() -> list[str]:
    """List the industries with end-to-end AI blueprints (Phase 13) you can use
    to scope customer solutions."""
    return list_groups("PHASE_13_")


@mcp.tool()
def list_accelerator_packs() -> list[str]:
    """List the accelerator pack categories (Phase 14) — reusable assets for
    AI consulting, engineering, product and business delivery."""
    return list_groups("PHASE_14_")


# --------------------------------------------------------------------------- #
# Workflow tool 1: client delivery
# --------------------------------------------------------------------------- #
@mcp.tool()
def design_customer_solution(business_need: str, industry: str | None = None,
                             current_systems: str | None = None,
                             top_k: int = 5) -> dict[str, Any]:
    """Assemble grounded references to scope an AI solution for a customer
    (automation, integration with existing systems/websites, or full
    implementation).

    It gathers the most relevant: industry blueprint (Phase 13), accelerator
    packs (Phase 14), reference implementations (Phase 15), playbooks (Phase 08)
    and templates (Phase 09) for the stated need. Use the returned paths with
    get_aibos_document to read the detail, then synthesise a proposal.

    Args:
        business_need: What the customer wants, in plain language.
        industry: Optional industry to bias the blueprint (see list_industries).
        current_systems: Optional note on the customer's existing stack/website
            to ground the integration approach.
        top_k: References to return per category (1-10).
    """
    top_k = max(1, min(int(top_k), 10))
    q = business_need + (f" for the {industry} industry" if industry else "")
    integ_q = (f"integrate AI with {current_systems}" if current_systems
               else f"AI integration and implementation for {business_need}")
    return {
        "business_need": business_need,
        "industry": industry,
        "industry_blueprint": _hits(q, top_k, phase="Phase 13"),
        "accelerator_packs": _hits(q, top_k, phase="Phase 14"),
        "reference_implementations": _hits(integ_q, top_k, phase="Phase 15"),
        "delivery_playbooks": _hits(business_need, top_k, phase="Phase 08"),
        "reusable_templates": _hits(business_need, top_k, phase="Phase 09"),
        "how_to_use": (
            "Open the highest-scoring paths with get_aibos_document, combine the "
            "industry blueprint (problem framing) with an accelerator pack "
            "(reusable assets), a reference implementation (architecture) and the "
            "relevant playbooks/templates (delivery), then produce a tailored "
            "proposal. Keep human-in-the-loop approval for high-risk actions."),
    }


# --------------------------------------------------------------------------- #
# Workflow tool 2: internal operations
# --------------------------------------------------------------------------- #
@mcp.tool()
def improve_department(department: str, objective: str | None = None,
                       top_k: int = 5) -> dict[str, Any]:
    """Gather everything needed to develop, enhance or manage an internal
    company function (e.g. HR, Finance, Technology, Sales, Marketing, Business
    Strategy) following AIBOS best practices.

    Returns the department specification (Phase 04) plus the applicable skills,
    rules, checklists, playbooks, templates and knowledge articles for the
    stated objective.

    Args:
        department: The function to improve, e.g. "Finance" or "Marketing".
        objective: Optional goal, e.g. "reduce month-end close time with AI".
        top_k: References to return per category (1-10).
    """
    top_k = max(1, min(int(top_k), 10))
    q = f"{department} {objective}".strip()
    return {
        "department": department,
        "objective": objective,
        "department_specification": _hits(q, top_k, category=department,
                                          phase="Phase 04") or _hits(q, top_k,
                                          phase="Phase 04"),
        "applicable_skills": _hits(q, top_k, phase="Phase 05"),
        "applicable_rules": _hits(q, top_k, phase="Phase 06"),
        "applicable_checklists": _hits(q, top_k, phase="Phase 07"),
        "applicable_playbooks": _hits(q, top_k, phase="Phase 08"),
        "reusable_templates": _hits(q, top_k, phase="Phase 09"),
        "knowledge": _hits(q, top_k, phase="Phase 10"),
        "how_to_use": (
            "Start from the department specification, then apply the rules and "
            "checklists as guardrails, the playbooks as step-by-step procedures, "
            "and the templates to produce artefacts. Use the knowledge articles "
            "for background. Automate repeatable steps with human oversight."),
    }


@mcp.tool()
def get_best_practices(topic: str, top_k: int = 8) -> dict[str, Any]:
    """Return AIBOS best practices for a topic by combining knowledge articles
    (Phase 10) and rules (Phase 06)."""
    top_k = max(1, min(int(top_k), 15))
    return {
        "topic": topic,
        "knowledge": _hits(topic, top_k, phase="Phase 10"),
        "rules": _hits(topic, top_k, phase="Phase 06"),
    }


# --------------------------------------------------------------------------- #
# Resources
# --------------------------------------------------------------------------- #
@mcp.resource("aibos://index/root")
def root_index() -> str:
    """The authoritative, ordered catalogue of every artefact."""
    return _get_document("ROOT_INDEX.md") or ""


@mcp.resource("aibos://index/generation")
def generation_index() -> str:
    """The generated-artefacts index (counts and layout by phase)."""
    return _get_document("02_ARTEFACTS/GENERATION_INDEX.md") or ""


@mcp.resource("aibos://standard/{name}")
def standard(name: str) -> str:
    """A root standard from 00_ROOT, e.g. name=AIBOS_SECURITY_STANDARD."""
    return _get_document(f"00_ROOT/{name}.md") or f"Unknown standard: {name}"


# --------------------------------------------------------------------------- #
# Guided prompts
# --------------------------------------------------------------------------- #
@mcp.prompt()
def client_engagement(business_need: str, industry: str = "") -> str:
    """Guide an AI client-delivery engagement grounded in AIBOS."""
    return (
        f"You are an AI solutions consultant. A customer needs: {business_need}."
        + (f" Industry: {industry}." if industry else "")
        + " Call design_customer_solution with these inputs, open the top "
        "references with get_aibos_document, then produce: (1) problem framing, "
        "(2) proposed AI architecture and integration approach, (3) delivery "
        "plan with playbooks/templates, (4) risks, governance and human "
        "oversight points, (5) success metrics. Cite artefact paths.")


@mcp.prompt()
def internal_excellence(department: str, objective: str = "") -> str:
    """Guide improving an internal company function using AIBOS."""
    return (
        f"Improve our {department} function" + (f" to: {objective}." if objective
        else ".") + " Call improve_department, read the department "
        "specification and applicable rules/checklists/playbooks/templates with "
        "get_aibos_document, then propose a prioritised improvement plan that "
        "follows the best practices, automates repeatable work with human "
        "oversight, and lists guardrails and success metrics. Cite paths.")


# --------------------------------------------------------------------------- #
# Entry point: stdio (local) or Streamable-HTTP + auth (remote/team)
# --------------------------------------------------------------------------- #
def _run_http() -> None:
    import uvicorn
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.responses import JSONResponse

    token = CONFIG.token

    class AuthMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            if token:
                header = request.headers.get("authorization", "")
                if header != f"Bearer {token}":
                    return JSONResponse({"error": "unauthorized"},
                                        status_code=401)
            return await call_next(request)

    app = mcp.streamable_http_app()
    app.add_middleware(AuthMiddleware)
    uvicorn.run(app, host=CONFIG.host, port=CONFIG.port)


def main() -> None:
    if CONFIG.transport == "http":
        _run_http()
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
