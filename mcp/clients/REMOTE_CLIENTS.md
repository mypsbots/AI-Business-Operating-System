# Connecting remote clients (ChatGPT, Gemini, Grok, your app, the team)

Cursor, Claude Desktop and VS Code run the server **locally** over `stdio`
(see the JSON files in this folder). ChatGPT, Gemini, Grok, your own
app/SaaS backend and any shared team access instead connect to the server
running in **remote HTTP mode**.

## 1. Start the server in HTTP mode

```bash
cd "/Users/prakash/Documents/Personals/Learning/Automation/Skills/AI Business Operating System-AIBOS"

AIBOS_MCP_TRANSPORT=http \
AIBOS_MCP_HOST=0.0.0.0 \
AIBOS_MCP_PORT=8000 \
AIBOS_MCP_TOKEN="<a-long-random-secret>" \
AIBOS_BACKEND=pinecone \
PINECONE_API_KEY="<your-pinecone-key>" \
mcp/.venv/bin/python mcp/run_server.py
```

- MCP endpoint: `http://<host>:8000/mcp`
- Every request must send: `Authorization: Bearer <a-long-random-secret>`
- For internet exposure, put it behind HTTPS (a reverse proxy or a host such
  as Vercel/Fly/Render) — never expose the proprietary content without TLS
  **and** the bearer token.

> Tip: you can run HTTP mode with `AIBOS_BACKEND=local` too (no Pinecone), but
> semantic recall is best with Pinecone for shared/team use.

## 2. Client-by-client

### ChatGPT

Use a **custom connector / MCP server** (Settings → Connectors, or Developer
mode). Add the URL `https://<your-host>/mcp` and set the Authorization header
to `Bearer <token>`. The AIBOS tools then appear in chat and deep research.

### Google Gemini

Gemini connects to MCP servers through the **Gemini API / Vertex AI** using an
MCP client in your integration code (pass the URL and bearer header), or via
environments that support remote MCP connectors. Point it at
`https://<your-host>/mcp` with the bearer token.

### Grok (xAI)

Connect through xAI's API tool-use / MCP client support: register the remote
MCP endpoint `https://<your-host>/mcp` with the `Authorization: Bearer <token>`
header.

### Your own app / SaaS backend

Use any MCP client SDK (TypeScript `@modelcontextprotocol/sdk` or Python `mcp`)
with the **Streamable HTTP** transport:

```ts
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const transport = new StreamableHTTPClientTransport(
  new URL("https://your-host/mcp"),
  { requestInit: { headers: { Authorization: `Bearer ${process.env.AIBOS_MCP_TOKEN}` } } }
);
const client = new Client({ name: "my-app", version: "1.0.0" });
await client.connect(transport);
const tools = await client.listTools();
```

### Whole team

Deploy one shared HTTPS endpoint and either issue a **per-user token** (so
access is revocable/auditable) or front it with your SSO/proxy. Each teammate
adds the same URL in their client with their token.
