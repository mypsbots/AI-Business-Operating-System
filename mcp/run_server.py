#!/usr/bin/env python3
"""Launcher for the AIBOS MCP server.

Run this file directly (it puts the `mcp/` directory on sys.path so the
`aibos_mcp` package imports cleanly and never clashes with the MCP SDK's own
top-level `mcp` package):

    python /abs/path/to/repo/mcp/run_server.py

Transport and backend are controlled by environment variables (see .env.example).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aibos_mcp.server import main  # noqa: E402

if __name__ == "__main__":
    main()
