"""Vercel serverless entrypoint for the AIBOS MCP server.

Vercel detects the exported ASGI ``app`` and serves it on Fluid Compute. The
server runs in stateless Streamable-HTTP mode so each request is independent
(safe across serverless instances).

Required environment variables (set in the Vercel project):
  AIBOS_MCP_TOKEN     bearer token clients must send
  PINECONE_API_KEY    enables the Pinecone semantic backend
  AIBOS_PINECONE_*    optional overrides (index/namespace/region/model)

The corpus Markdown is bundled via `includeFiles` in vercel.json so
get_aibos_document and the list_* tools work.
"""

import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(_REPO_ROOT, "mcp"))

# Default to the Pinecone backend on Vercel (serverless-friendly). A present
# PINECONE_API_KEY also auto-selects it, but we set it explicitly for clarity.
os.environ.setdefault("AIBOS_BACKEND", "pinecone")

from aibos_mcp.server import build_asgi_app  # noqa: E402

app = build_asgi_app(stateless=True)
