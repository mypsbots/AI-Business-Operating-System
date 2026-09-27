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

import re
from functools import lru_cache
from typing import Any

from mcp.server.fastmcp import FastMCP

from .backends import get_backend
from .config import CONFIG, REPO_ROOT
from .corpus import get_document as _get_document
from .corpus import iter_documents, list_groups

mcp = FastMCP("AIBOS", host=CONFIG.host, port=CONFIG.port)
_backend = get_backend(CONFIG)


def _hits(query: str, top_k: int, **filters: str | None) -> list[dict]:
    clean = {k: v for k, v in filters.items() if v}
    return [h.as_dict() for h in _backend.search(query, top_k=top_k,
                                                  filters=clean or None)]


def _doc_hits(query: str, top_k: int, **filters: str | None) -> list[dict]:
    """Like _hits, but returns at most one (best) section per document so the
    workflow tools list distinct documents rather than repeating a file."""
    clean = {k: v for k, v in filters.items() if v}
    raw = _backend.search(query, top_k=top_k * 4, filters=clean or None)
    seen: set[str] = set()
    out: list[dict] = []
    for h in raw:
        if h.path in seen:
            continue
        seen.add(h.path)
        out.append(h.as_dict())
        if len(out) >= top_k:
            break
    return out


def _doc_hits_pref(query: str, top_k: int, phase: str,
                   category: str | None) -> list[dict]:
    """Prefer category-filtered results; fall back to phase-only search when the
    category does not exist in that phase (so we never return an empty list just
    because the taxonomy differs across phases)."""
    if category:
        res = _doc_hits(query, top_k, phase=phase, category=category)
        if res:
            return res
    return _doc_hits(query, top_k, phase=phase)


# --------------------------------------------------------------------------- #
# Category resolution
# --------------------------------------------------------------------------- #
# A user-supplied department/industry term must be mapped to whatever bucket the
# *target phase* actually uses (the group folders differ per phase, e.g. Phase 04
# has "Finance"/"Sales" while Phase 06 groups those under "Business"). Each alias
# maps a normalised term to an ordered list of candidate categories; we pick the
# first candidate that exists in the phase being queried.
def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


_CATEGORY_ALIASES: dict[str, list[str]] = {
    "hr": ["Operations", "Business"],
    "human resources": ["Operations", "Business"],
    "people": ["Operations", "Business"],
    "people ops": ["Operations", "Business"],
    "talent": ["Operations", "Business"],
    "recruiting": ["Operations", "Business"],
    "recruitment": ["Operations", "Business"],
    "finance": ["Finance", "Business"],
    "accounting": ["Finance", "Business"],
    "procurement": ["Finance", "Business"],
    "commercial": ["Finance", "Business"],
    "sales": ["Sales", "Business"],
    "revenue": ["Sales", "Business"],
    "business development": ["Sales", "Business"],
    "marketing": ["Marketing", "Business"],
    "growth": ["Marketing", "Business"],
    "seo": ["Marketing", "Business"],
    "brand": ["Marketing", "Business"],
    "content": ["Marketing", "Business"],
    "communications": ["Marketing", "Business"],
    "technology": ["Engineering"],
    "tech": ["Engineering"],
    "it": ["Engineering"],
    "information technology": ["Engineering"],
    "software": ["Engineering"],
    "software engineering": ["Engineering"],
    "development": ["Engineering"],
    "engineering": ["Engineering"],
    "devops": ["Cloud And DevOps", "Infrastructure", "Engineering"],
    "cloud": ["Cloud And DevOps", "Infrastructure", "Engineering"],
    "infrastructure": ["Cloud And DevOps", "Infrastructure", "Engineering"],
    "platform": ["Cloud And DevOps", "Engineering"],
    "sre": ["Cloud And DevOps", "Observability", "Engineering"],
    "strategy": ["Executive", "Strategy And Governance", "Business"],
    "business strategy": ["Executive", "Strategy And Governance", "Business"],
    "leadership": ["Executive", "Business"],
    "executive": ["Executive", "Business"],
    "pmo": ["Executive", "Business"],
    "operations": ["Operations", "Business"],
    "ops": ["Operations", "Business"],
    "customer success": ["Customer Success", "Business"],
    "customer support": ["Customer Success", "Business"],
    "customer service": ["Customer Success", "Business"],
    "support": ["Customer Success", "Business"],
    "security": ["Security"],
    "compliance": ["Security"],
    "privacy": ["Security"],
    "risk": ["Security"],
    "iam": ["Security"],
    "infosec": ["Security"],
    "cybersecurity": ["Security"],
    "data": ["Data"],
    "analytics": ["Data"],
    "bi": ["Data"],
    "business intelligence": ["Data"],
    "data science": ["Data"],
    "ml": ["Data", "AI"],
    "machine learning": ["Data", "AI"],
    "quality": ["Quality"],
    "qa": ["Quality"],
    "testing": ["Quality"],
    "product": ["Product"],
    "product management": ["Product"],
    "legal": ["Legal", "Business"],
    "ai": ["AI", "Artificial Intelligence"],
    "artificial intelligence": ["AI", "Artificial Intelligence"],
    "research": ["Research"],
    "innovation": ["Research"],
    "governance": ["Governance", "Strategy And Governance"],
    "ecommerce": ["E Commerce"],
    "e commerce": ["E Commerce"],
}


@lru_cache(maxsize=1)
def _category_catalogue() -> dict[str, dict[str, str]]:
    """Map each phase label to ``{normalised_category: stored_category}`` using
    the *actual* category values the corpus is indexed/filtered on (these come
    from front matter when present, so they can differ from folder names, e.g.
    folder ``RETAIL`` but stored category ``Retail``). Computed once and cached."""
    cat: dict[str, dict[str, str]] = {}
    for doc in iter_documents():
        if doc.phase and doc.category:
            cat.setdefault(doc.phase, {})[_norm(doc.category)] = doc.category
    return cat


def _resolve_category(phase_label: str, term: str | None) -> str | None:
    """Map a free-text department/industry term to an existing category in the
    given phase (e.g. ``"Phase 04"``). Returns the stored category label exactly
    as indexed (so it matches the search filter), or ``None`` if nothing fits."""
    if not term:
        return None
    cats = _category_catalogue().get(phase_label, {})
    if not cats:
        return None
    n = _norm(term)
    if n in cats:                         # direct match (e.g. "finance")
        return cats[n]
    for cand in _CATEGORY_ALIASES.get(n, []):
        if _norm(cand) in cats:           # alias landed on an existing bucket
            return cats[_norm(cand)]
    for tok in n.split():                 # token match (e.g. "cloud security")
        if tok in cats:
            return cats[tok]
    return None


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
    industry_cat = _resolve_category("Phase 13", industry)
    return {
        "business_need": business_need,
        "industry": industry,
        "matched_industry": industry_cat,
        "industry_blueprint": _doc_hits_pref(q, top_k, "Phase 13", industry_cat),
        "accelerator_packs": _doc_hits(q, top_k, phase="Phase 14"),
        "reference_implementations": _doc_hits(integ_q, top_k, phase="Phase 15"),
        "delivery_playbooks": _doc_hits(business_need, top_k, phase="Phase 08"),
        "reusable_templates": _doc_hits(business_need, top_k, phase="Phase 09"),
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
    stated objective. The ``department`` term is resolved to the framework's
    actual categories (see ``list_departments``), so common synonyms such as
    "HR", "IT"/"Technology" (-> Engineering) or "Business Strategy"
    (-> Executive) are mapped automatically; ``matched_category`` reports the
    bucket that was used.

    Args:
        department: The function to improve, e.g. "Finance" or "Marketing".
        objective: Optional goal, e.g. "reduce month-end close time with AI".
        top_k: References to return per category (1-10).
    """
    top_k = max(1, min(int(top_k), 10))
    objective = objective or ""
    q = f"{department} {objective}".strip()
    return {
        "department": department,
        "objective": objective or None,
        "matched_category": _resolve_category("Phase 04", department),
        "department_specification": _doc_hits_pref(
            q, top_k, "Phase 04", _resolve_category("Phase 04", department)),
        "applicable_skills": _doc_hits(q, top_k, phase="Phase 05"),
        "applicable_rules": _doc_hits_pref(
            q, top_k, "Phase 06", _resolve_category("Phase 06", department)),
        "applicable_checklists": _doc_hits_pref(
            q, top_k, "Phase 07", _resolve_category("Phase 07", department)),
        "applicable_playbooks": _doc_hits_pref(
            q, top_k, "Phase 08", _resolve_category("Phase 08", department)),
        "reusable_templates": _doc_hits_pref(
            q, top_k, "Phase 09", _resolve_category("Phase 09", department)),
        "knowledge": _doc_hits_pref(
            q, top_k, "Phase 10", _resolve_category("Phase 10", department)),
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
def build_asgi_app(stateless: bool = False):
    """Build the Streamable-HTTP ASGI app with a bearer-auth gate and an
    unauthenticated /healthz endpoint.

    Set ``stateless=True`` for serverless hosts (e.g. Vercel) where requests may
    land on different instances — each request is then fully self-contained.
    """
    import hmac
    import logging

    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.responses import JSONResponse, PlainTextResponse
    from starlette.routing import Route

    if stateless:
        mcp.settings.stateless_http = True
        mcp.settings.json_response = True

    # {label: token}. Empty means "no auth" (trusted localhost only).
    tokens = CONFIG.tokens
    public_paths = {"/healthz"}
    logger = logging.getLogger("aibos.mcp.auth")

    class AuthMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            if tokens and request.url.path not in public_paths:
                header = request.headers.get("authorization", "")
                presented = header[7:] if header.startswith("Bearer ") else ""
                label = None
                if presented:
                    # Constant-time compare against every configured token so a
                    # match reveals which agent/client authenticated (audit) and
                    # timing cannot be used to guess a valid token.
                    for lbl, tok in tokens.items():
                        if hmac.compare_digest(presented, tok):
                            label = lbl
                            break
                if label is None:
                    logger.warning("auth denied path=%s", request.url.path)
                    return JSONResponse({"error": "unauthorized"},
                                        status_code=401)
                request.state.client_label = label
                logger.info("auth ok client=%s path=%s", label,
                            request.url.path)
            return await call_next(request)

    async def healthz(_request):
        return PlainTextResponse("ok")

    app = mcp.streamable_http_app()
    app.router.routes.append(Route("/healthz", healthz, methods=["GET"]))
    app.add_middleware(AuthMiddleware)
    return app


def _run_http() -> None:
    import uvicorn
    uvicorn.run(build_asgi_app(stateless=False), host=CONFIG.host,
                port=CONFIG.port)


def main() -> None:
    if CONFIG.transport == "http":
        _run_http()
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
