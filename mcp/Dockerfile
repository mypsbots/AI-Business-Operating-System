# AIBOS MCP server — remote (Streamable-HTTP) deployment image.
#
# Build context MUST be the repository root so the corpus is available:
#   docker build -f mcp/Dockerfile -t aibos-mcp .
#   docker run -p 8000:8000 -e AIBOS_MCP_TOKEN=... aibos-mcp
#
# The local SQLite search index is built at image-build time, so the container
# is fully self-contained and needs no external services. To use Pinecone
# instead, set AIBOS_BACKEND=pinecone and PINECONE_API_KEY at runtime.

FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    AIBOS_MCP_TRANSPORT=http \
    AIBOS_MCP_HOST=0.0.0.0 \
    AIBOS_MCP_PORT=8000 \
    AIBOS_BACKEND=local

WORKDIR /app

# Install dependencies first for better layer caching.
COPY mcp/requirements.txt /app/mcp/requirements.txt
RUN pip install -r /app/mcp/requirements.txt

# Copy the corpus the server serves plus the server code.
COPY 00_ROOT /app/00_ROOT
COPY 01_PHASES /app/01_PHASES
COPY 02_ARTEFACTS /app/02_ARTEFACTS
COPY mcp /app/mcp

# Build the local full-text index into the image.
RUN python /app/mcp/build_local_index.py

EXPOSE 8000

# AIBOS_MCP_TOKEN should be provided at runtime (do not bake secrets in).
CMD ["python", "/app/mcp/run_server.py"]
