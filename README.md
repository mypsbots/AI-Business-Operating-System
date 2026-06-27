# AI Business Operating System (AIBOS) — Enterprise v2.0

> The constitutional standards, governance framework and phased generation
> prompts required to build, govern and operate enterprise-grade, AI-native
> organisations.

[![Markdown Validation](https://github.com/mypsbots/AI-Business-Operating-System/actions/workflows/markdown-validation.yml/badge.svg)](https://github.com/mypsbots/AI-Business-Operating-System/actions/workflows/markdown-validation.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.5.0-green.svg)](CHANGELOG.md)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://www.conventionalcommits.org)

---

## Overview

The **AI Business Operating System (AIBOS)** is a documentation-as-code
framework that defines *how* an AI-native enterprise should be designed,
documented, generated and governed. It is delivered as a curated set of
Markdown artefacts organised into two layers:

1. **Root Standards** — the constitutional rules every artefact must inherit
   (specification, glossary, style, schema, metadata, naming, versioning,
   quality, validation, generation, security, AI behaviour, architecture,
   design and reference standards).
2. **Phase Prompts** — twenty sequential master prompts that drive the
   generation of the full enterprise repository, from enterprise architecture
   through to an autonomous meta-orchestrator.

The framework is intentionally **vendor-neutral** and **model-agnostic**. It is
compatible with GPT, Claude, Gemini, Grok and capable open-source LLMs.

## Repository Status

All **20 phases are complete and enriched to ready-to-use depth** — every
artefact carries detailed, section-appropriate content (no scaffolding or
placeholder text), YAML front matter, navigation breadcrumbs and resolving
cross-references.

| Metric | Value |
|--------|-------|
| Generated artefacts | **1067** across all 20 phases |
| Browsable folder indexes | 163 `README.md` files |
| Markdown lint (`markdownlint-cli2`) | **0 errors** across 1,231 files |
| Internal link check | **0 broken** across 22,845 links |
| Current version | **2.5.0** (see [`CHANGELOG.md`](CHANGELOG.md)) |

## Core Principles

| Principle | Description |
|-----------|-------------|
| AI First | Maximise safe, governed AI capability across the enterprise. |
| Security & Privacy by Design | Embed protection from the outset. |
| Zero Trust | Never assume trust by network location or identity alone. |
| Documentation as Code | Treat documents as version-controlled engineering artefacts. |
| Human-in-the-Loop | Mandatory human approval for high-risk actions. |
| Standards Aligned | ISO 42001, ISO 27001, NIST AI RMF, SOC 2, OWASP, WCAG 2.2 AA. |

## Repository Structure

```text
.
├── 00_ROOT/        # Root specification + 16 enterprise standards & master prompts
├── 01_PHASES/      # 20 sequential phase master prompts
├── 02_ARTEFACTS/   # 1067 detailed, ready-to-use artefacts across all 20 phases
├── tools/          # Deterministic generators (shared + per-phase content libraries)
├── mcp/            # AIBOS MCP server (expose the repo to AI clients & IDEs)
├── api/            # Vercel serverless entrypoint for the hosted MCP endpoint
├── MCP_USAGE_GUIDE.md # How to use the MCP from every tool, IDE and AI client
├── ROOT_INDEX.md   # Machine- and human-readable index of every artefact
├── FINAL_REPORT.md # Repository assembly & validation report
├── CHANGELOG.md    # Semantic-versioned change history
└── .github/        # CI workflow, issue & pull request templates
```

A complete, ordered catalogue of every document is maintained in
[`ROOT_INDEX.md`](ROOT_INDEX.md).

## Getting Started

1. **Read the constitution.** Start with
   [`00_ROOT/AIBOS_ROOT_SPECIFICATION.md`](00_ROOT/AIBOS_ROOT_SPECIFICATION.md);
   it takes precedence over every other document.
2. **Load the standards in order.** Follow the *Context Loading Order* defined
   in [`00_ROOT/AIBOS_EXECUTION_WORKFLOW.md`](00_ROOT/AIBOS_EXECUTION_WORKFLOW.md).
3. **Run the phases sequentially.** Use the master prompts in
   [`01_PHASES/`](01_PHASES) one at a time, honouring all dependencies. The
   canonical execution order is defined in
   [`00_ROOT/AIBOS_ENTERPRISE_EXECUTION_ORDER_AND_MASTER_EXECUTION_PROMPT.md`](00_ROOT/AIBOS_ENTERPRISE_EXECUTION_ORDER_AND_MASTER_EXECUTION_PROMPT.md).

### How to Execute a Phase

Provide your chosen LLM with the following context, in order:

```text
1. AIBOS_ROOT_SPECIFICATION.md
2. BUILD_AIBOS_MASTER_PROMPT_v2.md
3. The 15 remaining root standards
4. The selected PHASE_XX prompt
```

Then instruct the model to **generate one artefact at a time**, validate it
against the standards, and cross-reference previously completed work.

## Use as an MCP Server

The entire repository is exposed to AI clients and IDEs through the **AIBOS
Model Context Protocol (MCP) server**, so any tool can search and use the
framework as grounded context — for both client delivery and internal
operations.

- **Full usage guide:** [`MCP_USAGE_GUIDE.md`](MCP_USAGE_GUIDE.md) — how to
  connect from Cursor, Claude Desktop, VS Code, Windsurf, JetBrains/Zed/Cline,
  ChatGPT, Gemini, Grok, your own app/SaaS, and your whole team.
- **Server details:** [`mcp/README.md`](mcp/README.md).
- **Hosting options:** [`mcp/DEPLOY.md`](mcp/DEPLOY.md).

A hosted endpoint runs at `https://aibos-mcp.vercel.app/mcp` (bearer-token
protected); local IDEs can run it over `stdio` with zero external services.

## Standards Inheritance

Every generated artefact inherits, and must not contradict, the root standards.
If a phase prompt conflicts with the root specification, the **root
specification wins** unless an override is explicit.

## Contributing

Contributions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and
the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) before opening an issue or pull
request. All changes follow [Conventional Commits](https://www.conventionalcommits.org)
and [Semantic Versioning](https://semver.org).

## Security

To report a vulnerability, follow the process in [`SECURITY.md`](SECURITY.md).
Please do not open public issues for security concerns.

## Versioning

This repository uses [Semantic Versioning](https://semver.org). The current
version is **2.5.0** within the **v2** release line. See
[`CHANGELOG.md`](CHANGELOG.md) for history.

## License

Distributed under the terms of the [MIT License](LICENSE).
