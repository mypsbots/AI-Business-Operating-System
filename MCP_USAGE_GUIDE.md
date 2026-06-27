---
title: AIBOS MCP Usage Guide
description: How to connect and use the AIBOS Model Context Protocol server from every supported tool, IDE and AI client.
status: stable
---

# AIBOS MCP Usage Guide

This is the single, authoritative guide for using the **AIBOS Model Context
Protocol (MCP) server** — the interface that exposes this repository (the AI
Business Operating System: root standards, 20 phase prompts and ~1,067 generated
artefacts) to AI clients, IDEs and your own applications.

It is built for two jobs:

1. **Client delivery** — scope AI automation, integration with a customer's
   existing systems/website, and full implementations, grounded in industry
   blueprints, accelerator packs and reference implementations.
2. **Internal operations** — develop, enhance and manage your own company
   functions (HR, Finance, Technology, Sales, Marketing, Business Strategy, …)
   using the framework's department specs, rules, checklists, playbooks,
   templates and knowledge.

> The repository is **private/proprietary**. Never expose the HTTP endpoint
> without **HTTPS and the bearer token**. See [Security](#security).

## Contents

- [Overview](#overview)
- [Quick reference](#quick-reference)
- [How connections work](#how-connections-work)
- [One-time setup](#one-time-setup)
- [Local IDEs over stdio](#local-ides-over-stdio)
- [Remote clients over HTTP](#remote-clients-over-http)
- [Tools reference](#tools-reference)
- [Resources and prompts](#resources-and-prompts)
- [Example workflows](#example-workflows)
- [Verify the connection](#verify-the-connection)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Refresh after content changes](#refresh-after-content-changes)
- [Further reading](#further-reading)

## Overview

The AIBOS MCP server is **one server with two transports** and **two pluggable
search backends**, so the same content works everywhere from a local IDE to a
shared team endpoint.

- **Transports**
  - `stdio` — the server runs locally, launched by your IDE. Best for Cursor,
    Claude Desktop and VS Code on your own machine. No network, no token.
  - **Streamable-HTTP + bearer auth** — the server runs as a hosted/remote
    service. Required for ChatGPT, Gemini, Grok, your own app/SaaS, and
    team-wide access.
- **Search backends**
  - `local` — SQLite full-text search (FTS5). Zero external services, works
    offline. Great default for local IDE use.
  - `pinecone` — managed semantic search over an integrated-embedding index.
    Best recall; recommended for the hosted/team deployment.

A hosted endpoint is already live on Vercel:

- **Endpoint:** `https://aibos-mcp.vercel.app/mcp`
- **Health check:** `https://aibos-mcp.vercel.app/healthz` (no auth, returns `ok`)
- **Auth:** every `/mcp` request must send `Authorization: Bearer <AIBOS_MCP_TOKEN>`

The token lives in `mcp/.env` (git-ignored) and in the Vercel project's
environment variables. It is never committed to the repository.

## Quick reference

| Client | Transport | What you configure |
|--------|-----------|--------------------|
| Cursor (local) | stdio | `command` + `args` to the venv Python and `run_server.py` |
| Cursor (remote) | HTTP | `url` + `Authorization` header |
| Claude Code | HTTP (remote) or stdio (local) | `claude mcp add` (CLI) or `.mcp.json` |
| Claude Desktop | stdio (local) or `mcp-remote` bridge | `command` / `args` |
| VS Code | stdio (local) or HTTP (1.102+) | `.vscode/mcp.json` |
| Windsurf | HTTP | `url` + `Authorization` header |
| JetBrains / Zed / Cline | `mcp-remote` bridge | `npx mcp-remote <url> --header …` |
| ChatGPT | HTTP (custom connector) | URL + bearer header |
| Google Gemini | HTTP (API / Vertex MCP client) | URL + bearer header |
| Grok (xAI) | HTTP (API MCP client) | URL + bearer header |
| Your own app / SaaS | HTTP (MCP SDK) | URL + bearer header |
| Whole team | HTTP (shared endpoint) | one URL, per-user tokens |

- **Local endpoint (HTTP mode):** `http://<host>:8000/mcp`
- **Hosted endpoint:** `https://aibos-mcp.vercel.app/mcp`
- **Repository path** (used by the local stdio configs):
  `/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS`

## How connections work

There are exactly two ways any client connects:

1. **Local (stdio).** The client launches the Python process on your machine and
   talks to it over standard input/output. Nothing is exposed to the network and
   no token is needed. Use this for IDEs running on the same machine as the repo.
2. **Remote (HTTP).** The server runs as a long-lived HTTP service (hosted on
   Vercel, a VM, Docker, Fly, Render, or a local tunnel). Clients connect to a
   URL and must send a bearer token. Use this for cloud AI products (ChatGPT,
   Gemini, Grok), your own application, and shared team access.

Stdio-only clients can still reach a remote server through the **`mcp-remote`**
bridge (a small local proxy run via `npx`). See
[JetBrains, Zed, Cline and other stdio-only IDEs](#jetbrains-zed-cline-and-other-stdio-only-ides).

## One-time setup

You only need this if you are running the server yourself (local stdio, or
hosting your own HTTP endpoint). If you are connecting to the already-hosted
Vercel endpoint, skip to [Remote clients over HTTP](#remote-clients-over-http).

```bash
cd "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS"

# 1. Create an isolated environment and install dependencies
python3 -m venv mcp/.venv
mcp/.venv/bin/python -m pip install -r mcp/requirements.txt

# 2a. LOCAL backend (zero external services) — build the search index
mcp/.venv/bin/python mcp/build_local_index.py

# 2b. PINECONE backend (semantic, for hosting/team) — set keys, then ingest
cp mcp/.env.example mcp/.env        # set PINECONE_API_KEY and AIBOS_MCP_TOKEN
AIBOS_BACKEND=pinecone PINECONE_API_KEY=... \
  mcp/.venv/bin/python mcp/ingest_pinecone.py
```

For full setup and hosting details see [`mcp/README.md`](mcp/README.md) and
[`mcp/DEPLOY.md`](mcp/DEPLOY.md).

## Local IDEs over stdio

These run the server on your machine with the `local` (SQLite) backend. Ready-made
config files live in [`mcp/clients/`](mcp/clients). The paths inside them assume
this repository's location — adjust if you moved the repo.

### Cursor

Copy [`mcp/clients/cursor.mcp.json`](mcp/clients/cursor.mcp.json) into the repo's
`.cursor/mcp.json`, or merge it into your global `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "aibos": {
      "command": "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS/mcp/.venv/bin/python",
      "args": [
        "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS/mcp/run_server.py"
      ],
      "env": { "AIBOS_BACKEND": "local" }
    }
  }
}
```

Then open Cursor Settings → MCP and confirm `aibos` is connected. The tools
appear to the agent automatically.

### Claude Desktop

Merge [`mcp/clients/claude_desktop_config.json`](mcp/clients/claude_desktop_config.json)
into your Claude Desktop `claude_desktop_config.json`
(macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "aibos": {
      "command": "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS/mcp/.venv/bin/python",
      "args": [
        "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS/mcp/run_server.py"
      ],
      "env": { "AIBOS_BACKEND": "local" }
    }
  }
}
```

Restart Claude Desktop; the AIBOS tools show under the tools (plug) menu.

**Using the remote (hosted) server from Claude Desktop.** Claude Desktop's config
only accepts local (`stdio`) servers — a `type`/`url`/`headers` entry is rejected
("not valid MCP server configurations and were skipped"). Use the `mcp-remote`
bridge instead, with the env-var header form (no space around the colon):

```json
{
  "mcpServers": {
    "aibos": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote@latest",
        "https://aibos-mcp.vercel.app/mcp",
        "--header", "Authorization:${AIBOS_AUTH}"
      ],
      "env": { "AIBOS_AUTH": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

Then fully quit and reopen Claude Desktop. (For the command-line **Claude Code**,
which supports remote HTTP natively, see [Claude Code](#claude-code).)

### VS Code

Copy [`mcp/clients/vscode_mcp.json`](mcp/clients/vscode_mcp.json) to
`.vscode/mcp.json` in your workspace:

```json
{
  "servers": {
    "aibos": {
      "type": "stdio",
      "command": "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS/mcp/.venv/bin/python",
      "args": [
        "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS/mcp/run_server.py"
      ],
      "env": { "AIBOS_BACKEND": "local" }
    }
  }
}
```

Use the **MCP: List Servers** command (VS Code 1.102+) to start/inspect it.

## Remote clients over HTTP

All remote clients use the same endpoint and bearer token. Use the hosted Vercel
endpoint, or run your own HTTP server (see
[Run your own HTTP server](#run-your-own-http-server)).

- **Endpoint:** `https://aibos-mcp.vercel.app/mcp`
- **Header:** `Authorization: Bearer <AIBOS_MCP_TOKEN>`

### Cursor remote

Use a URL-based entry in `.cursor/mcp.json` (no local Python needed):

```json
{
  "mcpServers": {
    "aibos": {
      "url": "https://aibos-mcp.vercel.app/mcp",
      "headers": { "Authorization": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

### Claude Code

Claude Code (the CLI) connects to the remote server over HTTP. Run this in your
**terminal** (not inside a Claude session); flags must come **before** the name.
Set `AIBOS_MCP_TOKEN` in your shell first so the secret is not hardcoded:

```bash
export AIBOS_MCP_TOKEN="<your-token>"

claude mcp add --transport http aibos https://aibos-mcp.vercel.app/mcp \
  --header "Authorization: Bearer $AIBOS_MCP_TOKEN"
```

- Add `--scope user` (before the name) to enable it in every project, or
  `--scope project` to write a shared `.mcp.json` for your team. The default
  `local` scope is private to the current project.
- Verify with `claude mcp list` or `claude mcp get aibos`; inside a session run
  `/mcp` to see status and the AIBOS tools.
- On Claude Code 2.1.1+ the JSON form is equivalent:
  `claude mcp add-json aibos '{"type":"http","url":"https://aibos-mcp.vercel.app/mcp","headers":{"Authorization":"Bearer <AIBOS_MCP_TOKEN>"}}'`.

Alternatively, commit a project-scoped `.mcp.json` at the repository root (Claude
Code reads it automatically):

```json
{
  "mcpServers": {
    "aibos": {
      "type": "http",
      "url": "https://aibos-mcp.vercel.app/mcp",
      "headers": { "Authorization": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

### VS Code remote

`.vscode/mcp.json` with the HTTP type (VS Code 1.102+):

```json
{
  "servers": {
    "aibos": {
      "type": "http",
      "url": "https://aibos-mcp.vercel.app/mcp",
      "headers": { "Authorization": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

### Windsurf

`mcp.json` (Windsurf supports remote MCP directly):

```json
{
  "mcpServers": {
    "aibos": {
      "url": "https://aibos-mcp.vercel.app/mcp",
      "headers": { "Authorization": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

### JetBrains, Zed, Cline and other stdio-only IDEs

If your IDE only supports local (stdio) MCP, use the **`mcp-remote`** bridge — it
runs locally and forwards to the remote endpoint. Requires Node.js (`npx`):

```json
{
  "mcpServers": {
    "aibos": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote@latest",
        "https://aibos-mcp.vercel.app/mcp",
        "--header", "Authorization:${AIBOS_AUTH}"
      ],
      "env": { "AIBOS_AUTH": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

> **Important — header format.** Put the token in an `env` value and reference it
> as `Authorization:${AIBOS_AUTH}` with **no space around the colon**. Several
> clients (Cursor, Claude Desktop) mangle spaces inside `args`, so the common
> `--header "Authorization: Bearer <token>"` form can arrive malformed and cause
> a `401`. The env-var form avoids this.

See [`mcp/clients/OTHER_IDES.md`](mcp/clients/OTHER_IDES.md) for more detail.

### ChatGPT

Add a **custom connector / MCP server** (Settings → Connectors, or Developer
mode). Set the URL to `https://aibos-mcp.vercel.app/mcp` and add an
`Authorization` header of `Bearer <AIBOS_MCP_TOKEN>`. The AIBOS tools then appear
in chat and deep research.

### Google Gemini

Gemini connects to MCP servers through the **Gemini API / Vertex AI** using an
MCP client in your integration code, or environments that support remote MCP
connectors. Point it at `https://aibos-mcp.vercel.app/mcp` and pass the
`Authorization: Bearer <AIBOS_MCP_TOKEN>` header.

### Grok (xAI)

Connect through xAI's API tool-use / MCP client support: register the remote MCP
endpoint `https://aibos-mcp.vercel.app/mcp` with the
`Authorization: Bearer <AIBOS_MCP_TOKEN>` header.

### Your own app or SaaS backend

Use any MCP client SDK with the **Streamable HTTP** transport.

TypeScript (`@modelcontextprotocol/sdk`):

```ts
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const transport = new StreamableHTTPClientTransport(
  new URL("https://aibos-mcp.vercel.app/mcp"),
  { requestInit: { headers: { Authorization: `Bearer ${process.env.AIBOS_MCP_TOKEN}` } } }
);
const client = new Client({ name: "my-app", version: "1.0.0" });
await client.connect(transport);

const tools = await client.listTools();
const res = await client.callTool({
  name: "design_customer_solution",
  arguments: { business_need: "AI chatbot for support", industry: "Retail", top_k: 5 },
});
```

Python (`mcp`):

```python
import os, asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def main():
    headers = {"Authorization": f"Bearer {os.environ['AIBOS_MCP_TOKEN']}"}
    async with streamablehttp_client("https://aibos-mcp.vercel.app/mcp", headers=headers) as (r, w, _):
        async with ClientSession(r, w) as session:
            await session.initialize()
            result = await session.call_tool(
                "improve_department",
                {"department": "Finance", "objective": "reduce month-end close time"},
            )
            print(result)

asyncio.run(main())
```

### Whole team

Deploy one shared HTTPS endpoint (the Vercel deployment already does this) and
either issue a **per-user token** (revocable and auditable) or front it with your
SSO/proxy. Each teammate adds the same URL in their client with their token.

### Run your own HTTP server

To self-host instead of (or in addition to) Vercel:

```bash
cd "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS"

AIBOS_MCP_TRANSPORT=http \
AIBOS_MCP_HOST=0.0.0.0 \
AIBOS_MCP_PORT=8000 \
AIBOS_MCP_TOKEN="<a-long-random-secret>" \
AIBOS_BACKEND=pinecone \
PINECONE_API_KEY="<your-pinecone-key>" \
mcp/.venv/bin/python mcp/run_server.py
# endpoint: http://<host>:8000/mcp
```

For tunnels, Docker, Fly.io and Render see [`mcp/DEPLOY.md`](mcp/DEPLOY.md).

## Tools reference

All tools are read-only over the corpus and return citable artefact paths. Use
`get_aibos_document` with any returned `path` to read the full content.

| Tool | Purpose | Key arguments |
|------|---------|---------------|
| `search_aibos` | Search the whole framework and return the most relevant artefact sections. | `query`, `top_k` (1-25), `phase`, `category`, `document_type` |
| `get_aibos_document` | Return the full Markdown of an artefact by repo-relative path. | `path` |
| `list_phases` | List the 20 AIBOS phases and what each covers. | — |
| `list_departments` | List the company functions available as Phase 04 specs. | — |
| `list_industries` | List industries with end-to-end blueprints (Phase 13). | — |
| `list_accelerator_packs` | List accelerator pack categories (Phase 14). | — |
| `design_customer_solution` | Assemble blueprint + accelerator pack + reference implementation + playbooks/templates for a customer need. | `business_need`, `industry`, `current_systems`, `top_k` (1-10) |
| `improve_department` | Gather the department spec + applicable skills/rules/checklists/playbooks/templates/knowledge for an internal function. | `department`, `objective`, `top_k` (1-10) |
| `get_best_practices` | Knowledge (Phase 10) + rules (Phase 06) for a topic. | `topic`, `top_k` (1-15) |

Notes:

- `search_aibos` filters are optional. Useful values: `phase` like `"Phase 13"`;
  `category` like `"Finance"` or `"Security"`; `document_type` like `"Rule"`,
  `"Checklist"`, `"Playbook"`, `"Template"`, `"Knowledge"`, `"Specification"`,
  `"Blueprint"`.
- `improve_department` and `design_customer_solution` automatically resolve common
  synonyms to the framework's real categories (for example `HR`, `IT`/`Technology`
  → Engineering, `Business Strategy` → Executive, `e-commerce` → the E-commerce
  blueprint). The response includes `matched_category` / `matched_industry` so you
  can see which bucket was used.

Example raw JSON-RPC call (HTTP):

```bash
curl -sS https://aibos-mcp.vercel.app/mcp \
  -H "Authorization: Bearer <AIBOS_MCP_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_aibos","arguments":{"query":"zero trust architecture","top_k":3}}}'
```

## Resources and prompts

**Resources** (read-only documents the client can pull in as context):

- `aibos://index/root` — the authoritative, ordered catalogue of every artefact.
- `aibos://index/generation` — the generated-artefacts index (counts and layout).
- `aibos://standard/{name}` — a root standard from `00_ROOT`, for example
  `aibos://standard/AIBOS_SECURITY_STANDARD`.

**Prompts** (guided, reusable workflows your client can invoke):

- `client_engagement` — guides an AI client-delivery engagement. Inputs:
  `business_need`, optional `industry`.
- `internal_excellence` — guides improving an internal function. Inputs:
  `department`, optional `objective`.

## Example workflows

### Scope an AI solution for a customer

1. Invoke the `client_engagement` prompt (or just ask the agent to use
   `design_customer_solution`) with the customer's need and industry.
2. The tool returns the best industry blueprint, accelerator packs, reference
   implementations, delivery playbooks and reusable templates.
3. Open the top `path`s with `get_aibos_document`, then ask the agent to produce
   a proposal: problem framing, AI architecture and integration approach, delivery
   plan, risks/governance, and success metrics — citing the artefact paths.

### Improve an internal department

1. Invoke the `internal_excellence` prompt (or ask the agent to use
   `improve_department`) with the function and your goal — for example
   `department = "Finance"`, `objective = "reduce month-end close time with AI"`.
2. The tool returns the department specification plus the applicable rules,
   checklists, playbooks, templates and knowledge.
3. Open the references and ask the agent for a prioritised improvement plan that
   follows the best practices, automates repeatable work with human oversight, and
   lists guardrails and success metrics.

## Verify the connection

```bash
# Health (no auth) — should print: ok
curl -s https://aibos-mcp.vercel.app/healthz

# Initialize (with token) — should return serverInfo for "AIBOS"
curl -sS https://aibos-mcp.vercel.app/mcp \
  -H "Authorization: Bearer <AIBOS_MCP_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"curl","version":"1.0"}}}'
```

A missing or invalid token on `/mcp` returns `401 Unauthorized`. For local stdio,
confirm the server in your IDE's MCP panel shows as connected with tools listed.

## Security

- The repository is **private/proprietary** — never expose the HTTP endpoint
  without **TLS and the bearer token**.
- Keep secrets in `mcp/.env` (git-ignored) or your host's secret manager. Never
  commit `PINECONE_API_KEY` or `AIBOS_MCP_TOKEN`.
- The server is **read-only** over the corpus; `get_aibos_document` is guarded
  against path traversal (only `.md` files inside the repository).
- Prefer **per-user tokens** so access can be revoked and audited; or place the
  endpoint behind your SSO/proxy.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `401 Unauthorized` on `/mcp` | Missing/incorrect `Authorization` header | Send `Authorization: Bearer <AIBOS_MCP_TOKEN>`; confirm the token matches the host's `AIBOS_MCP_TOKEN`. |
| Tools don't appear in the IDE | Server not started or wrong config path | Check the MCP panel/logs; verify the Python and `run_server.py` paths in the JSON config. |
| `Local index not built` error | Missing SQLite index | Run `mcp/.venv/bin/python mcp/build_local_index.py`. |
| Empty or weak results on hosted endpoint | Pinecone not ingested or wrong key | Run `mcp/ingest_pinecone.py`; verify `PINECONE_API_KEY` on the host. |
| First hosted request is slow | Serverless cold start | Expected; subsequent requests are fast. Hit `/healthz` to warm it. |
| Stale results after editing content | Index/Pinecone not refreshed | See [Refresh after content changes](#refresh-after-content-changes). |

## Refresh after content changes

Whenever the repository content changes, rebuild the search index for whichever
backend you use:

```bash
# local backend
mcp/.venv/bin/python mcp/build_local_index.py

# pinecone backend
AIBOS_BACKEND=pinecone PINECONE_API_KEY=... \
  mcp/.venv/bin/python mcp/ingest_pinecone.py
```

## Further reading

- [`mcp/README.md`](mcp/README.md) — server overview, setup and architecture.
- [`mcp/DEPLOY.md`](mcp/DEPLOY.md) — hosting options (tunnel, Docker, Vercel, Fly, Render).
- [`mcp/clients/REMOTE_CLIENTS.md`](mcp/clients/REMOTE_CLIENTS.md) — remote client notes.
- [`mcp/clients/OTHER_IDES.md`](mcp/clients/OTHER_IDES.md) — other IDEs and the `mcp-remote` bridge.
- [`ROOT_INDEX.md`](ROOT_INDEX.md) — the full catalogue of repository artefacts.
