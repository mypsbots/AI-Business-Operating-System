---
id: ARCH-000002
title: Business Capabilities
document_type: Architecture
category: Enterprise Architecture
phase: Phase 01
owner: Office of the Chief Enterprise Architect
status: Draft
classification: Internal
version: 2.0.0
created: 2026-06-26
updated: 2026-06-26
tags:
  - business-capabilities
  - capability-model
related_documents:
  - 07_CAPABILITY_MAP.md
  - 03_OPERATING_MODEL.md
standards:
  - ISO 42001
---

# Business Capabilities

## Executive Summary

This document defines the core business capabilities an AI-native enterprise
requires. Capabilities describe *what* the enterprise must be able to do,
independent of *how* it is organised or implemented.

## Purpose

To provide a stable, technology-neutral capability taxonomy that anchors
organisation design, investment and architecture decisions.

## Scope

All enterprise capabilities across strategy, product, engineering, AI, data,
security, go-to-market and operations.

## Objectives

- Establish a shared capability vocabulary.
- Enable capability-based planning and investment.
- Reduce duplication and clarify ownership.

## Stakeholders

Executive leadership, enterprise architecture, division leaders, finance and
governance.

## Business Value

Improved investment focus, clearer accountability and reusable capability
building blocks.

## Architecture

Capabilities are organised into three tiers:

| Tier | Examples |
|------|----------|
| Strategic | Vision, Portfolio, Governance, Risk. |
| Core | Product, Engineering, AI Platform, Data, Security. |
| Enabling | Cloud, DevOps, Finance, Legal, People, Knowledge. |

Each capability links to owning divisions (Phase 03) and departments (Phase 04).

## Guiding Principles

AI First, Modular by Design, Reuse before Build, Security and Privacy by Design.

## Standards Mapping

ISO 42001 (AI capability governance), ISO 27001 (security capability).

## Risks

- Capability overlap creating duplicated investment.
- Capabilities defined too granularly to be useful.

## Assumptions

- The taxonomy is reviewed annually.

## Dependencies

- `01_ENTERPRISE_VISION.md`
- Phase 02 Enterprise Specifications.

## Acceptance Criteria

- Every capability has a single owning division.
- The map is complete across all tiers.

## Validation Checklist

- [ ] No duplicated capabilities.
- [ ] Each capability has an owner.
- [ ] Cross-references valid.

## References

- `07_CAPABILITY_MAP.md`
- `00_ROOT/AIBOS_ARCHITECTURE_PRINCIPLES.md`

## Version History

| Version | Date | Summary |
|---------|------|---------|
| 2.0.0 | 2026-06-26 | Initial business capability model. |
