# AIBOS_ROOT_SPECIFICATION.md

# AIBOS Enterprise v2.0 Root Specification

## Purpose

This document is the constitutional specification for every artefact generated inside AIBOS Enterprise.

All Phase prompts inherit this specification. If a Phase prompt conflicts with this document, this document takes precedence unless explicitly overridden.

## Identity

- Name: AI Business Operating System (AIBOS)
- Edition: Enterprise
- Version: 2.0
- Primary Goal: Build, govern and operate enterprise-grade AI-native organisations.

## Core Principles

- AI First
- Security by Design
- Privacy by Design
- Zero Trust
- Cloud Native
- API First
- Documentation as Code
- Infrastructure as Code
- Automation First
- Observability First
- Human-in-the-Loop for high-risk actions
- Vendor-neutral where practical

## Global Standards

Align with, where applicable:

- ISO 42001
- ISO 27001
- NIST AI RMF
- SOC 2
- OWASP ASVS
- OWASP LLM Top 10
- WCAG 2.2 AA
- OpenAPI
- OAuth 2.1
- OpenTelemetry
- Twelve-Factor App

## Repository Standards

Recommended structure:

00_ROOT/
01_PHASES/
02_SHARED/
03_TEMPLATES/
04_KNOWLEDGE/
05_REFERENCE/
06_MARKETPLACE/

Use semantic versioning.
Use Markdown.
Prefer Mermaid diagrams.
Use YAML front matter.

## Universal Document Schema

Every document should include:

- YAML metadata
- Executive Summary
- Purpose
- Scope
- Responsibilities
- Dependencies
- Risks
- Acceptance Criteria
- Validation Checklist
- References
- Version History

## Writing Standards

- Enterprise tone
- Concise but comprehensive
- No duplicated concepts
- Reusable content
- Cross-reference related documents
- Prefer tables over long prose where appropriate

## AI Behaviour

The LLM must:

- Never invent facts.
- Maintain consistency.
- Prefer reusable architecture.
- Generate production-ready artefacts.
- Preserve terminology.
- Clearly distinguish MUST / SHOULD / MAY.
- Stop safely if context limits are reached and provide a continuation point.

## Naming

Use uppercase snake case filenames ending in .md.

## Success Criteria

Every generated artefact must be internally consistent, traceable, versioned and reusable.
