#!/usr/bin/env python3
"""Create (if needed) and populate the Pinecone integrated-embedding index
with the AIBOS corpus for semantic search.

    export PINECONE_API_KEY=...        # or put it in mcp/.env
    python mcp/ingest_pinecone.py

Uses an integrated index, so Pinecone embeds the text server-side — no separate
embedding provider/key is required. Re-running upserts over existing records.
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aibos_mcp.config import CONFIG  # noqa: E402
from aibos_mcp.corpus import iter_chunks  # noqa: E402

BATCH = 90  # integrated upsert_records limit is 96 records/request


def _records():
    for c in iter_chunks():
        m = c.metadata
        yield {
            "_id": c.id,
            "chunk_text": c.text,
            "title": m["title"],
            "path": m["path"],
            "phase": m["phase"],
            "category": m["category"],
            "section": m["section"],
            "document_type": m["document_type"],
        }


def main() -> None:
    if not CONFIG.pinecone_api_key:
        sys.exit("PINECONE_API_KEY is not set. Add it to mcp/.env or export it.")

    from pinecone import Pinecone

    pc = Pinecone(api_key=CONFIG.pinecone_api_key)
    name = CONFIG.pinecone_index

    if not pc.has_index(name):
        print(f"Creating integrated index '{name}' "
              f"(model={CONFIG.pinecone_embed_model})...")
        pc.create_index_for_model(
            name=name,
            cloud=CONFIG.pinecone_cloud,
            region=CONFIG.pinecone_region,
            embed={"model": CONFIG.pinecone_embed_model,
                   "field_map": {"text": "chunk_text"}},
        )
        while not pc.describe_index(name).status.get("ready", False):
            time.sleep(2)

    index = pc.Index(name)

    batch, total = [], 0
    for rec in _records():
        batch.append(rec)
        if len(batch) >= BATCH:
            index.upsert_records(CONFIG.pinecone_namespace, batch)
            total += len(batch)
            print(f"  upserted {total} sections...", flush=True)
            batch = []
    if batch:
        index.upsert_records(CONFIG.pinecone_namespace, batch)
        total += len(batch)

    print(f"Done. Upserted {total} sections into '{name}' "
          f"(namespace='{CONFIG.pinecone_namespace}').")


if __name__ == "__main__":
    main()
