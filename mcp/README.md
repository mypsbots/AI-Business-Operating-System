# AIBOS MCP Server

Expose this repository — the AI Business Operating System (root standards, 20
phase prompts and ~1067 generated artefacts) — to AI clients and agents over
the **Model Context Protocol (MCP)**.

It is built for two jobs:

1. **Client delivery** — scope AI automation, integration with a customer's
   existing systems/website, and full implementations, grounded in industry
   blueprints, accelerator packs and reference implementations.
2. **Internal operations** — develop, enhance and manage your own company
   functions (HR, Finance, Technology, Sales, Marketing, Business Strategy, …)
   following the framework's department specs, rules, checklists, playbooks,
   templates and knowledge.

> **Looking for how to connect a specific tool or IDE?** See the complete
> [AIBOS MCP Usage Guide](../MCP_USAGE_GUIDE.md) — step-by-step setup for Cursor,
> Claude Desktop, VS Code, Windsurf, JetBrains/Zed/Cline, ChatGPT, Gemini, Grok,
> your own app/SaaS and team-wide access.

## What it exposes

**Tools**

| Tool | Use |
|------|-----|
| `search_aibos` | Semantic/full-text search across the whole framework, with `phase` / `category` / `document_type` filters. |
| `get_aibos_document` | Open any artefact by its repo-relative path. |
| `list_phases` / `list_departments` / `list_industries` / `list_accelerator_packs` | Discover what's available. |
| `design_customer_solution` | Assemble blueprint + accelerator pack + reference implementation + playbooks/templates for a customer need. |
| `improve_department` | Gather the department spec + applicable skills/rules/checklists/playbooks/templates/knowledge for an internal function. |
| `get_best_practices` | Knowledge + rules for a topic. |

**Resources:** `aibos://index/root`, `aibos://index/generation`,
`aibos://standard/{name}`.
**Prompts:** `client_engagement`, `internal_excellence`.

## Architecture

- **One server, two transports.** `stdio` for local IDE clients (Cursor, Claude
  Desktop, VS Code); **Streamable-HTTP + bearer auth** for remote clients
  (ChatGPT, Gemini, Grok, your app, the team).
- **Two pluggable search backends.**
  - `local` — SQLite FTS5, no external services, works offline. Great default.
  - `pinecone` — managed semantic search over an integrated-embedding index
    (Pinecone embeds server-side, so no separate embedding key). Best recall;
    recommended for the hosted/team deployment.
- Documents are chunked by `##` section with rich metadata (phase, category,
  document type, owner, standards) so results are focused and citable.

## Setup

```bash
cd "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS"

# 1. Create an isolated environment and install dependencies
python3 -m venv mcp/.venv
mcp/.venv/bin/python -m pip install -r mcp/requirements.txt

# 2a. LOCAL backend (zero external services) — build the search index
mcp/.venv/bin/python mcp/build_local_index.py

# 2b. PINECONE backend (semantic, for hosting/team) — ingest the corpus
cp mcp/.env.example mcp/.env        # set PINECONE_API_KEY (and a token)
AIBOS_BACKEND=pinecone PINECONE_API_KEY=... \
  mcp/.venv/bin/python mcp/ingest_pinecone.py
```

## Run

**Local (stdio)** — used automatically by the IDE client configs:

```bash
AIBOS_BACKEND=local mcp/.venv/bin/python mcp/run_server.py
```

**Remote (HTTP + auth)** — for ChatGPT/Gemini/Grok/app/team:

```bash
AIBOS_MCP_TRANSPORT=http AIBOS_MCP_TOKEN="<secret>" \
AIBOS_BACKEND=pinecone PINECONE_API_KEY=... \
  mcp/.venv/bin/python mcp/run_server.py
# endpoint: http://<host>:8000/mcp  (send: Authorization: Bearer <secret>)
```

## Connect your clients

Ready-made configs live in [`clients/`](clients):

- **Cursor** — copy [`clients/cursor.mcp.json`](clients/cursor.mcp.json) into
  the repo's `.cursor/mcp.json` (or merge into `~/.cursor/mcp.json`).
- **Claude Desktop** — merge
  [`clients/claude_desktop_config.json`](clients/claude_desktop_config.json)
  into `claude_desktop_config.json`.
- **VS Code** — copy [`clients/vscode_mcp.json`](clients/vscode_mcp.json) to
  `.vscode/mcp.json`.
- **Another IDE, remotely** (Windsurf, JetBrains, Zed, Cline, …) — see
  [`clients/OTHER_IDES.md`](clients/OTHER_IDES.md) (direct HTTP and the
  `mcp-remote` stdio bridge).
- **ChatGPT, Gemini, Grok, your app, team** — see
  [`clients/REMOTE_CLIENTS.md`](clients/REMOTE_CLIENTS.md).

The paths in the JSON files assume this repo's location; adjust if you move it.

## Deploying for remote / team use

The server runs in HTTP mode with bearer-token auth and a `/healthz` endpoint;
the local index is baked into the Docker image so it needs no external services.
See [`DEPLOY.md`](DEPLOY.md) for full instructions covering:

1. **Quick tunnel** (local server + `cloudflared`/`ngrok`) — reachable in minutes.
2. **Docker / docker-compose** — run anywhere (VM, Cloud Run, ECS).
3. **Vercel** (serverless, recommended if you use Vercel) — `api/index.py` +
   `vercel.json` run the server statelessly with the Pinecone backend.
4. **Fly.io** — [`deploy/fly.toml`](deploy/fly.toml).
5. **Render.com** — [`deploy/render.yaml`](deploy/render.yaml).

In all cases set a strong `AIBOS_MCP_TOKEN`, serve over HTTPS, and prefer
per-user tokens (or SSO at a proxy) for revocability and audit.

## Security

- The repository is **private/proprietary** — never expose the HTTP endpoint
  without **TLS and the bearer token**.
- Keep secrets in `mcp/.env` (git-ignored) or your host's secret manager; never
  commit `PINECONE_API_KEY` or `AIBOS_MCP_TOKEN`.
- The server is **read-only** over the corpus; `get_aibos_document` is guarded
  against path traversal (only `.md` files inside the repo).
- Prefer per-user tokens so access can be revoked and audited.

## Refreshing after content changes

```bash
# local backend
mcp/.venv/bin/python mcp/build_local_index.py
# pinecone backend
AIBOS_BACKEND=pinecone PINECONE_API_KEY=... mcp/.venv/bin/python mcp/ingest_pinecone.py
```
