"""Environment-driven configuration for the AIBOS MCP server."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# Repository root is the parent of the `mcp/` directory.
REPO_ROOT = Path(__file__).resolve().parents[2]

# Top-level content directories that make up the searchable corpus.
CONTENT_DIRS = ["00_ROOT", "01_PHASES", "02_ARTEFACTS"]


def _bool(value: str | None) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def _parse_tokens(raw: str, single: str) -> dict[str, str]:
    """Parse the labelled multi-token env into a ``{label: token}`` map.

    ``AIBOS_MCP_TOKENS`` is a comma-separated list where each entry is either
    ``label:token`` (recommended, enables per-agent audit + revocation) or a
    bare ``token`` (auto-labelled). The single ``AIBOS_MCP_TOKEN`` is kept for
    backward compatibility and added under the ``primary`` label.
    """
    tokens: dict[str, str] = {}
    if raw:
        for i, entry in enumerate(raw.split(","), start=1):
            entry = entry.strip()
            if not entry:
                continue
            if ":" in entry:
                label, _, value = entry.partition(":")
                label, value = label.strip(), value.strip()
            else:
                label, value = f"client{i}", entry
            if value:
                tokens[label or f"client{i}"] = value
    if single and single not in tokens.values():
        tokens.setdefault("primary", single)
    return tokens


@dataclass(frozen=True)
class Config:
    backend: str
    transport: str
    host: str
    port: int
    token: str
    tokens: dict[str, str]
    # Pinecone
    pinecone_api_key: str
    pinecone_index: str
    pinecone_namespace: str
    pinecone_cloud: str
    pinecone_region: str
    pinecone_embed_model: str
    # Local
    local_index_path: Path

    @staticmethod
    def load() -> "Config":
        api_key = os.getenv("PINECONE_API_KEY", "").strip()
        backend = os.getenv("AIBOS_BACKEND", "").strip().lower()
        if backend not in {"local", "pinecone"}:
            backend = "pinecone" if api_key else "local"

        local_index = os.getenv("AIBOS_LOCAL_INDEX", "").strip()
        local_path = (Path(local_index) if local_index
                      else REPO_ROOT / "mcp" / ".index" / "aibos.db")

        single_token = os.getenv("AIBOS_MCP_TOKEN", "").strip()
        tokens = _parse_tokens(os.getenv("AIBOS_MCP_TOKENS", "").strip(),
                               single_token)

        return Config(
            backend=backend,
            transport=os.getenv("AIBOS_MCP_TRANSPORT", "stdio").strip().lower(),
            host=os.getenv("AIBOS_MCP_HOST", "0.0.0.0").strip(),
            port=int(os.getenv("AIBOS_MCP_PORT", "8000")),
            token=single_token,
            tokens=tokens,
            pinecone_api_key=api_key,
            pinecone_index=os.getenv("AIBOS_PINECONE_INDEX", "aibos-knowledge").strip(),
            pinecone_namespace=os.getenv("AIBOS_PINECONE_NAMESPACE", "aibos").strip(),
            pinecone_cloud=os.getenv("AIBOS_PINECONE_CLOUD", "aws").strip(),
            pinecone_region=os.getenv("AIBOS_PINECONE_REGION", "us-east-1").strip(),
            pinecone_embed_model=os.getenv(
                "AIBOS_PINECONE_EMBED_MODEL", "llama-text-embed-v2").strip(),
            local_index_path=local_path,
        )


CONFIG = Config.load()
