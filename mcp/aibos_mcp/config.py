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


@dataclass(frozen=True)
class Config:
    backend: str
    transport: str
    host: str
    port: int
    token: str
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

        return Config(
            backend=backend,
            transport=os.getenv("AIBOS_MCP_TRANSPORT", "stdio").strip().lower(),
            host=os.getenv("AIBOS_MCP_HOST", "0.0.0.0").strip(),
            port=int(os.getenv("AIBOS_MCP_PORT", "8000")),
            token=os.getenv("AIBOS_MCP_TOKEN", "").strip(),
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
