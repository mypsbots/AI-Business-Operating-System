"""Load and chunk the AIBOS repository into searchable records.

Every artefact carries YAML front matter and a consistent set of ``##`` (H2)
sections. We split each document by H2 heading so retrieval returns focused,
citable sections rather than whole files, and attach metadata (phase, category,
document type, owner, standards) for filtered search.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

import yaml

from .config import CONTENT_DIRS, REPO_ROOT

_FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
_H2 = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
# Map a top-level artefact folder to a human-friendly phase label.
_PHASE_RE = re.compile(r"PHASE_(\d+)_([A-Z0-9_]+)")


@dataclass
class Document:
    rel_path: str
    meta: dict
    body: str
    phase: str = ""
    category: str = ""

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or Path(self.rel_path).stem)

    @property
    def document_type(self) -> str:
        return str(self.meta.get("document_type") or "Document")


@dataclass
class Chunk:
    id: str
    text: str
    metadata: dict = field(default_factory=dict)


def _split_front_matter(raw: str) -> tuple[dict, str]:
    m = _FRONT_MATTER.match(raw)
    if not m:
        return {}, raw
    try:
        meta = yaml.safe_load(m.group(1)) or {}
        if not isinstance(meta, dict):
            meta = {}
    except yaml.YAMLError:
        meta = {}
    return meta, raw[m.end():]


def _derive_phase_category(rel_path: str, meta: dict) -> tuple[str, str]:
    phase = str(meta.get("phase") or "")
    category = str(meta.get("category") or "")
    parts = Path(rel_path).parts
    if not phase or not category:
        for i, p in enumerate(parts):
            pm = _PHASE_RE.match(p)
            if pm:
                if not phase:
                    phase = f"Phase {int(pm.group(1)):02d}"
                # The folder immediately after the phase dir is the group/category.
                if not category and i + 1 < len(parts) - 1:
                    category = parts[i + 1].replace("_", " ")
                break
    return phase, category


def iter_documents() -> Iterator[Document]:
    """Yield every Markdown artefact in the corpus (excluding folder indexes)."""
    for top in CONTENT_DIRS:
        base = REPO_ROOT / top
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name == "README.md":
                continue
            raw = path.read_text(encoding="utf-8")
            meta, body = _split_front_matter(raw)
            rel = str(path.relative_to(REPO_ROOT))
            phase, category = _derive_phase_category(rel, meta)
            yield Document(rel_path=rel, meta=meta, body=body,
                           phase=phase, category=category)


def _section_chunks(doc: Document) -> Iterator[tuple[str, str]]:
    """Yield (section_title, section_text) pairs split on H2 headings."""
    body = doc.body.strip()
    matches = list(_H2.finditer(body))
    if not matches:
        yield ("Overview", body)
        return
    # Any preamble before the first H2.
    pre = body[: matches[0].start()].strip()
    if pre:
        yield ("Overview", pre)
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        section = body[start:end].strip()
        if section:
            yield (m.group(1).strip(), section)


def _base_metadata(doc: Document) -> dict:
    standards = doc.meta.get("standards") or []
    if isinstance(standards, list):
        standards = ", ".join(str(s) for s in standards)
    return {
        "doc_id": str(doc.meta.get("id") or ""),
        "title": doc.title,
        "path": doc.rel_path,
        "phase": doc.phase,
        "category": doc.category,
        "document_type": doc.document_type,
        "owner": str(doc.meta.get("owner") or ""),
        "status": str(doc.meta.get("status") or ""),
        "standards": str(standards),
    }


def iter_chunks(max_chars: int = 4000) -> Iterator[Chunk]:
    """Yield section-level chunks across the whole corpus."""
    for doc in iter_documents():
        base = _base_metadata(doc)
        for idx, (section, text) in enumerate(_section_chunks(doc)):
            # Guard against very large sections.
            for part_no, offset in enumerate(range(0, len(text), max_chars)):
                piece = text[offset:offset + max_chars]
                cid = f"{doc.rel_path}#s{idx}p{part_no}"
                header = f"{base['title']} \u2014 {section}\n({doc.phase})\n\n"
                meta = dict(base)
                meta["section"] = section
                meta["chunk_text"] = header + piece
                yield Chunk(id=cid, text=header + piece, metadata=meta)


def get_document(rel_path: str) -> str | None:
    """Return the full text of an artefact by repo-relative path."""
    rel = rel_path.strip().lstrip("/")
    candidate = (REPO_ROOT / rel).resolve()
    try:
        candidate.relative_to(REPO_ROOT)
    except ValueError:
        return None  # Path traversal guard.
    if candidate.is_file() and candidate.suffix == ".md":
        return candidate.read_text(encoding="utf-8")
    return None


def list_groups(phase_dir_prefix: str) -> list[str]:
    """List sub-group folder names under a Phase directory in 02_ARTEFACTS."""
    base = REPO_ROOT / "02_ARTEFACTS"
    for d in base.iterdir() if base.exists() else []:
        if d.is_dir() and d.name.startswith(phase_dir_prefix):
            return sorted(s.name for s in d.iterdir()
                          if s.is_dir())
    return []
