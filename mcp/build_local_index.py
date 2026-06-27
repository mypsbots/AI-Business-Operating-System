#!/usr/bin/env python3
"""Build the local SQLite FTS5 search index from the AIBOS corpus.

    python mcp/build_local_index.py

Produces mcp/.index/aibos.db (override with AIBOS_LOCAL_INDEX). Safe to re-run;
it rebuilds the index from scratch each time.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aibos_mcp.backends import LocalFtsBackend  # noqa: E402
from aibos_mcp.config import CONFIG  # noqa: E402


def main() -> None:
    backend = LocalFtsBackend(CONFIG.local_index_path)
    count = backend.build()
    print(f"Indexed {count} sections into {CONFIG.local_index_path}")


if __name__ == "__main__":
    main()
