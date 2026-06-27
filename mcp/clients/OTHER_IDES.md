# Using the AIBOS MCP server from another IDE (remote)

Once the server runs in HTTP mode (locally, via a tunnel, or hosted — see
[`../DEPLOY.md`](../DEPLOY.md)), point any MCP-capable IDE at:

- **Endpoint:** `https://<your-host>/mcp` (or `http://<host>:8000/mcp` for local)
  - On Vercel this is `https://<project>.vercel.app/mcp`.
- **Auth header:** `Authorization: Bearer <AIBOS_MCP_TOKEN>`

There are two connection styles depending on what your IDE supports.

## A. IDEs that support remote (HTTP) MCP directly

Cursor, Windsurf, VS Code (1.102+), and similar.

**Cursor / Windsurf** (`mcp.json`):

```json
{
  "mcpServers": {
    "aibos": {
      "url": "https://<your-host>/mcp",
      "headers": { "Authorization": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

**VS Code** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "aibos": {
      "type": "http",
      "url": "https://<your-host>/mcp",
      "headers": { "Authorization": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

## B. IDEs that only support local (stdio) MCP

Use the `mcp-remote` bridge — it runs locally and forwards to your remote
endpoint, so any stdio-only client (JetBrains plugins, Cline, Zed, etc.) works:

```json
{
  "mcpServers": {
    "aibos": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote@latest",
        "https://<your-host>/mcp",
        "--header", "Authorization:${AIBOS_AUTH}"
      ],
      "env": { "AIBOS_AUTH": "Bearer <AIBOS_MCP_TOKEN>" }
    }
  }
}
```

(Requires Node.js for `npx`.)

> Put the token in `env` and reference it as `Authorization:${AIBOS_AUTH}` with no
> space around the colon. Some clients (Cursor, Claude Desktop) mangle spaces in
> `args`, so the inline `--header "Authorization: Bearer <token>"` form can arrive
> malformed and return `401`; the env-var form avoids that.

## C. Same machine, different IDE (no remote needed)

If the other IDE is on this machine, you can skip HTTP entirely and reuse the
local stdio config — copy the relevant file from this folder
(`cursor.mcp.json`, `claude_desktop_config.json`, `vscode_mcp.json`) and adjust
the paths.

## Verify the connection

```bash
curl -s https://<your-host>/healthz          # -> ok  (no auth required)
# A missing/invalid token on /mcp returns 401 Unauthorized.
```
