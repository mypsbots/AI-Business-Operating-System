# Deploying the AIBOS MCP server for remote use

The server runs in **HTTP mode** (`AIBOS_MCP_TRANSPORT=http`) and is protected
by a bearer token (`AIBOS_MCP_TOKEN`). The local SQLite index is baked into the
Docker image, so the container needs **no external services**. Pinecone is an
optional upgrade (set `AIBOS_BACKEND=pinecone` + `PINECONE_API_KEY`).

Pick the option that matches how far you want to go.

## 0. Prepare a token

```bash
openssl rand -hex 32        # use this as AIBOS_MCP_TOKEN
```

Keep it in `mcp/.env` (git-ignored) for local runs, or as a host secret in
production. **Never commit it.**

## 1. Quick remote without hosting — local server + tunnel

Fastest way to reach the server from another machine/IDE today:

```bash
# Terminal 1: run the server (reads mcp/.env)
set -a; . mcp/.env; set +a
mcp/.venv/bin/python mcp/run_server.py

# Terminal 2: expose it over HTTPS
cloudflared tunnel --url http://localhost:8000      # or: ngrok http 8000
```

Use the printed `https://…` URL + `/mcp` in your IDE (see
[`clients/OTHER_IDES.md`](clients/OTHER_IDES.md)).

## 2. Docker (anywhere: your VM, a server, Cloud Run, ECS, …)

```bash
# Build from the REPOSITORY ROOT (the corpus must be in the build context)
docker build -f mcp/Dockerfile -t aibos-mcp .

docker run -d -p 8000:8000 \
  -e AIBOS_MCP_TOKEN="<your-secret>" \
  --name aibos-mcp aibos-mcp

curl -s http://localhost:8000/healthz   # -> ok
```

Or with compose (reads `mcp/.env`):

```bash
docker compose -f mcp/docker-compose.yml up --build -d
```

## 3. Fly.io (managed, global)

```bash
fly launch --no-deploy --copy-config --config mcp/deploy/fly.toml --dockerfile mcp/Dockerfile
fly secrets set AIBOS_MCP_TOKEN="<your-secret>"
fly deploy --config mcp/deploy/fly.toml --dockerfile mcp/Dockerfile
# endpoint: https://<app-name>.fly.dev/mcp
```

## 4. Render.com (Blueprint)

Push the repo, then in Render: **New + → Blueprint** and select it. Render reads
[`mcp/deploy/render.yaml`](deploy/render.yaml), builds the Docker image, and
prompts for `AIBOS_MCP_TOKEN`.
Endpoint: `https://<service>.onrender.com/mcp`.

## Security checklist

- Always serve over **HTTPS** in production (hosts above do this automatically;
  for option 2 put it behind a TLS reverse proxy or load balancer).
- Set a strong `AIBOS_MCP_TOKEN`; prefer **per-user tokens** so access is
  revocable and auditable, or front the endpoint with SSO.
- The repository is private/proprietary — never expose `/mcp` without the token.
- `/healthz` is intentionally unauthenticated and returns only `ok`.

## Refreshing content

The index is built at image-build time. After changing artefacts, rebuild and
redeploy the image (or, for the tunnel option, re-run
`mcp/build_local_index.py`). For Pinecone, re-run `mcp/ingest_pinecone.py`.
