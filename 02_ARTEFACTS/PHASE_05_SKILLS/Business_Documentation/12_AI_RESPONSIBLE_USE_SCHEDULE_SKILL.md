---
id: BIZDOC-012
title: AI and Responsible Use Schedule — Generation Skill
document_type: Skill
category: Business Documentation
phase: Phase 05
owner: Commercial and Contracts Lead
status: Published
lifecycle: Active
classification: Internal
version: 1.0.0
created: 2026-07-30
updated: 2026-07-30
jurisdiction: England and Wales
tags:
  - skill
  - business-documentation
  - ai-responsible-use-schedule
related_documents:
  - ROOT_INDEX.md
  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md
  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md
  - 02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/00_UK_CONTRACTING_FRAMEWORK.md
standards:
  - ISO 42001
  - NIST AI RMF
  - UK GDPR
  - OWASP LLM Top 10
---

# AI and Responsible Use Schedule — Generation Skill

> **Navigate:** [Home](../../../README.md) · [Catalogue](../../../ROOT_INDEX.md) · [All Skills](../README.md) · [Business Docs](README.md) · [UK Framework](00_UK_CONTRACTING_FRAMEWORK.md) · [Source Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)

## At a Glance

Sets the responsible-AI terms, limitations and risk allocation for AI-related deliverables.

| Field | Detail |
| --- | --- |
| Document | AI and Responsible Use Schedule |
| Category | Business Documentation |
| Jurisdiction | England and Wales (UK) |
| Pack | Extended |
| Binding status | Binding schedule to the MSA/SOW where incorporated. |
| Typical signatories | Authorised signatory of the Supplier and of the Customer. |
| AI automation | AI-draftable from the firm's responsible-AI policy; human/solicitor review for regulated use. |

## Legal Notice

> **Legal notice.** This skill produces a **draft** business document to speed up preparation. It is **not legal advice** and is **not a substitute for review by a UK-qualified solicitor**. For high-value, regulated, international, security-sensitive or complex engagements, obtain solicitor sign-off before signing. Unless otherwise agreed, the governing law is **England and Wales**. Do not store passwords, API keys or production credentials in generated documents.

## Purpose

An AI (Responsible Use) Schedule governs AI-specific risks: intended and prohibited uses, human oversight, accuracy limitations, data rights, and allocation of residual risk the customer accepts.

It makes clear that AI outputs require human review and that no regulated decision should rest solely on AI output unless expressly agreed and governed.

## When to Use

- Any deliverable that builds or integrates AI/LLM capabilities.
- Where model/provider dependencies and output rights need to be defined.
- Where the customer must accept AI accuracy/hallucination limitations.

## Document Blueprint (Generation Template)

When this skill is invoked, generate the document by expanding each blueprint section below into clear, formal UK business English, filling every placeholder from the *Inputs Required*, resolving or flagging any missing input, marking the output as a draft, and appending a dated signature block for the authorised signatories. Keep numbering and the order of precedence consistent with the [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md).

1. **Intended and prohibited uses** — Permitted use cases and explicit prohibitions.
2. **Human review responsibility** — Customer is responsible for appropriate human oversight.
3. **Accuracy and hallucination limitations** — Outputs may be inaccurate, incomplete or non-unique.
4. **Model and provider dependencies** — Named models/providers and their terms; changes may occur.
5. **Training-data and input-data rights** — Rights to use data for the service.
6. **Treatment of prompts and outputs** — How prompts/outputs are stored, used and secured.
7. **Personal-data restrictions** — Limits on personal data in prompts/training.
8. **Confidential-data restrictions** — Limits on confidential data in prompts/training.
9. **Bias and fairness testing** — Testing approach where relevant.
10. **Explainability expectations** — What explainability is/ isn't provided.
11. **Model changes** — Effect of third-party model changes.
12. **Output ownership and licensing** — Who owns/licenses generated output.
13. **Regulatory responsibilities** — Each party's regulatory duties.
14. **Logging, monitoring and safety controls** — Guardrails and monitoring.
15. **Residual-risk acceptance** — Customer acceptance of stated residual risks.

## Inputs Required to Generate

- Intended/prohibited uses; models and providers.
- Data rights and restrictions; output ownership.
- Human-oversight and regulatory responsibilities; residual risks.

## UK Legal and Compliance Notes

- State that no legal, medical, financial or regulated decision should be made solely from AI output unless expressly agreed and appropriately governed.
- Define AI performance metrics in the SOW rather than assuming them.
- Align with ISO/IEC 42001 and NIST AI RMF governance expectations.

## Best Practices and Pitfalls

- Require human-in-the-loop for consequential decisions.
- Be explicit about provider dependencies and change risk.

## Related Documents

- [Master Services Agreement](04_MASTER_SERVICES_AGREEMENT_SKILL.md)
- [Statement of Work](05_STATEMENT_OF_WORK_SKILL.md)
- [Data Processing Agreement](06_DATA_PROCESSING_AGREEMENT_SKILL.md)
- [UK Contracting Framework](00_UK_CONTRACTING_FRAMEWORK.md)
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide](../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md)
- [Business Documentation Index](README.md)
- [All Phase 05 Skills](../README.md)
- [Enterprise Templates](../../PHASE_09_TEMPLATES/README.md)
- [AIBOS Root Specification](../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md)
- [Enterprise Glossary](../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md)

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Complete, generate-ready UK business-document skill. |
