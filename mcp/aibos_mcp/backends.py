"""Pluggable search backends for the AIBOS MCP server.

* ``LocalFtsBackend`` — SQLite FTS5 full-text search. No external services,
  works offline, ideal for local IDE use and CI.
* ``PineconeBackend`` — managed semantic search over an integrated-embedding
  index. Best recall; used for the hosted/team deployment.
"""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from .config import Config
from .corpus import iter_chunks

_FTS_SAFE = re.compile(r"[^0-9A-Za-z\u00C0-\u024F\s]")


@dataclass
class SearchHit:
    score: float
    title: str
    path: str
    phase: str
    category: str
    section: str
    document_type: str
    snippet: str

    def as_dict(self) -> dict:
        return {
            "score": round(self.score, 4),
            "title": self.title,
            "path": self.path,
            "phase": self.phase,
            "category": self.category,
            "section": self.section,
            "document_type": self.document_type,
            "snippet": self.snippet,
        }


class SearchBackend:
    def search(self, query: str, top_k: int = 8,
               filters: dict | None = None) -> list[SearchHit]:
        raise NotImplementedError

    def is_ready(self) -> bool:
        raise NotImplementedError


# --------------------------------------------------------------------------- #
# Local SQLite FTS5 backend
# --------------------------------------------------------------------------- #
class LocalFtsBackend(SearchBackend):
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def is_ready(self) -> bool:
        return self.db_path.exists()

    def build(self) -> int:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        if self.db_path.exists():
            self.db_path.unlink()
        con = sqlite3.connect(self.db_path)
        try:
            con.execute(
                "CREATE VIRTUAL TABLE chunks USING fts5("
                "cid UNINDEXED, title, phase, category, document_type, "
                "path UNINDEXED, section, body, tokenize='porter unicode61')")
            rows = ((c.id, c.metadata["title"], c.metadata["phase"],
                     c.metadata["category"], c.metadata["document_type"],
                     c.metadata["path"], c.metadata["section"], c.text)
                    for c in iter_chunks())
            con.executemany(
                "INSERT INTO chunks(cid,title,phase,category,document_type,"
                "path,section,body) VALUES (?,?,?,?,?,?,?,?)", rows)
            con.commit()
            count = con.execute("SELECT count(*) FROM chunks").fetchone()[0]
        finally:
            con.close()
        return count

    @staticmethod
    def _match_query(query: str) -> str:
        terms = _FTS_SAFE.sub(" ", query).split()
        # Quote each token so punctuation/operators can't break FTS5 syntax.
        return " OR ".join(f'"{t}"' for t in terms) if terms else '""'

    def search(self, query: str, top_k: int = 8,
               filters: dict | None = None) -> list[SearchHit]:
        if not self.is_ready():
            raise RuntimeError(
                "Local index not built. Run: python -m mcp.build_local_index")
        match = self._match_query(query)
        if match == '""':
            return []
        where = ["chunks MATCH ?"]
        params: list = [
            "title:" + match + " OR section:" + match + " OR body:" + match]
        for col in ("phase", "category", "document_type"):
            val = (filters or {}).get(col)
            if val:
                where.append(f"{col} = ?")
                params.append(val)
        sql = (
            "SELECT cid,title,phase,category,document_type,path,section,"
            "snippet(chunks,7,'','','\u2026',16) AS snip, bm25(chunks) AS rank "
            f"FROM chunks WHERE {' AND '.join(where)} ORDER BY rank LIMIT ?")
        params.append(top_k)
        con = sqlite3.connect(self.db_path)
        try:
            cur = con.execute(sql, params)
            hits = []
            for r in cur.fetchall():
                # bm25() returns negative values where lower is more relevant;
                # negate so a higher score means a better match.
                hits.append(SearchHit(
                    score=-float(r[8]),
                    title=r[1], phase=r[2], category=r[3],
                    document_type=r[4], path=r[5], section=r[6],
                    snippet=r[7]))
            return hits
        finally:
            con.close()


# --------------------------------------------------------------------------- #
# Pinecone integrated-embedding backend
# --------------------------------------------------------------------------- #
class PineconeBackend(SearchBackend):
    def __init__(self, config: Config):
        self.config = config
        self._index = None

    def _get_index(self):
        if self._index is None:
            from pinecone import Pinecone
            pc = Pinecone(api_key=self.config.pinecone_api_key)
            self._index = pc.Index(self.config.pinecone_index)
        return self._index

    def is_ready(self) -> bool:
        if not self.config.pinecone_api_key:
            return False
        try:
            from pinecone import Pinecone
            pc = Pinecone(api_key=self.config.pinecone_api_key)
            return pc.has_index(self.config.pinecone_index)
        except Exception:
            return False

    def search(self, query: str, top_k: int = 8,
               filters: dict | None = None) -> list[SearchHit]:
        index = self._get_index()
        flt = {k: {"$eq": v} for k, v in (filters or {}).items() if v}
        resp = index.search(
            namespace=self.config.pinecone_namespace,
            top_k=top_k,
            inputs={"text": query},
            filter=flt or None,
            fields=["chunk_text", "title", "path", "phase", "category",
                    "section", "document_type"])
        # Normalise the response to a plain dict across SDK versions.
        try:
            data = resp.to_dict()
        except AttributeError:
            data = resp if isinstance(resp, dict) else {}
        hits = []
        for h in data.get("result", {}).get("hits", []):
            f = h.get("fields", {})
            text = f.get("chunk_text", "")
            score = h.get("score_", h.get("_score", h.get("score", 0.0)))
            hits.append(SearchHit(
                score=float(score or 0.0),
                title=f.get("title", ""), path=f.get("path", ""),
                phase=f.get("phase", ""), category=f.get("category", ""),
                section=f.get("section", ""),
                document_type=f.get("document_type", ""),
                snippet=(text[:280] + "\u2026") if len(text) > 280 else text))
        return hits


def get_backend(config: Config) -> SearchBackend:
    if config.backend == "pinecone":
        return PineconeBackend(config)
    return LocalFtsBackend(config.local_index_path)
