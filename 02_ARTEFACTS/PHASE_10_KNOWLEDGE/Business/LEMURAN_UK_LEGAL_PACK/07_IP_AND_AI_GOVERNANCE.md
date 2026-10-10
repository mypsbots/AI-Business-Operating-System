---
id: LEMURAN-UK-07
title: "Intellectual property, licensing and AI risk governance"
document_type: "Knowledge Article"
owner: "Lemuran director — assignment pending"
status: Draft for human review
classification: Internal
version: 1.1.0
updated: "2026-10-10"
created: "2026-10-09"
verified_on: "2026-10-09"
jurisdiction: United Kingdom
legal_advice_status: Decision support; not a legal opinion
---

# Intellectual property, licensing and AI risk governance

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## IP ownership and licensing

**LAW / CONTRACT:** respect copyright, database rights, trademarks, confidentiality and licence restrictions. Copyright normally arises without registration. Employee-created works in the course of employment and commissioned contractor works have different ownership defaults. Obtain appropriate signed written assignments for contractor/founder contributions where ownership is intended; an invoice or “work for hire” label is insufficient. Identify any pre-existing IP and grant licences needed to use deliverables. [IPO ownership guidance](https://www.gov.uk/guidance/ownership-of-copyright-works), [copyright assignments](https://www.gov.uk/using-somebody-elses-intellectual-property/copyright).

**PRACTICE:** maintain an asset register for code, datasets, prompts, designs, documents, domains, marks and model licences. Record author, creation date, employment/assignment evidence, background IP, allowed use, restrictions and customer commitments. Search for conflicts before adopting a brand; Companies House registration or domain ownership does not itself grant trademark protection. Consult a patent professional before public disclosure of a potentially patentable invention.

For open source, maintain a software bill of materials and licence obligations: notices, attribution, source availability, redistribution and network-use clauses where relevant. Copyleft obligations depend on the licence and use/distribution; do not assume all OSS is unrestricted or all copyleft is prohibited. Model-weight, dataset and API terms need separate reviews for commercial use, acceptable uses, redistribution and downstream rights.

For RAG/crawling, check authority to copy, index, store and disclose material, including website terms, copyright/database rights and personal data. Public availability is not a licence. Do not assume non-commercial text/data-mining exceptions permit commercial SaaS training or crawling. AI output rights and infringement risk depend on facts; never guarantee exclusive copyright or non-infringement because a provider assigns its rights. The government's March 2026 copyright/AI report is a policy source, not permission to train on any work. [Government report](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence).

## UK AI governance

No special general AI SaaS licence is established by the sources reviewed for this pack. That is not a conclusion that a specific FAQai.app/agency use is unregulated. Apply data protection, consumer, equality, IP, safety and sector rules to actual uses, including healthcare/financial/employment functions. UK regulatory principles are guidance, not an independent blanket statute. [UK principles](https://www.gov.uk/government/publications/implementing-the-uks-ai-regulatory-principles-initial-guidance-for-regulators/implementing-the-uks-ai-regulatory-principles-initial-guidance-for-regulators).

**CONDITIONAL LAW:** assess solely automated significant decisions using the amended UK GDPR Articles 22A–22D introduced by DUAA, rather than repeating the old Article 22 prohibition as current law. Analyse meaningful human involvement, legal/similarly significant effect, special-category restrictions and applicable safeguards. Provide information, routes for representations, human intervention and challenge as required; a reviewer without authority or time is not meaningful oversight. Escalate special-category and recognised-legitimate-interest cases for current provision-level review. [DUAA s80](https://www.legislation.gov.uk/ukpga/2025/18/section/80), access limitation in source register.

## Proposed POLICY: AI lifecycle gates

| Stage | Deliverable | Gate |
|---|---|---|
| Intake | Intended purpose, users, affected people, territories, tools/actions, harms | Product owner classifies use |
| Design | Data/role map, AI risk assessment, DPIA screening, vendor/IP review | Privacy/security/sector reviewer where relevant |
| Evaluation | Grounded-answer tests, error/abstention, bias, tenant isolation, prompt injection, harmful requests | Evidence meets approved criteria |
| Release | Model/config version, limitations, monitoring, rollback and escalation route | Named accountable owner accepts residual risk |
| Operation | Complaints, errors, drift, supplier changes and incidents | Reassess on material change |
| Retirement | Export, deletion, access revocation and records | Owner verifies contractual/legal completion |

Recommended FAQai.app controls: cite or identify approved knowledge sources, handle stale/contradictory documents, abstain/escalate uncertain answers, protect tenant boundaries, avoid exposing hidden instructions or secrets, and limit agent actions by explicit permissions. Agency controls: approval before live client changes, sandbox testing, backup/rollback, least-privilege client access, and handover of monitoring responsibilities.

Risk ratings are internal, not statutory labels: low (bounded informational use), medium (personal data or external actions), high (vulnerable users, significant decisions, regulated advice, large-scale sensitive data or material loss), unacceptable (unlawful use or risk that cannot be controlled). A low internal rating does not waive law; an EU high-risk classification is a separate legal analysis.

## EU and online safety triggers

For EU-facing operations, classify Lemuran as provider/deployer/importer/distributor where applicable; using a third-party model does not automatically make Lemuran a GPAI model provider or remove system-provider duties. EU territorial scope can capture certain non-EU actors where output is used in the EU. Check prohibited practices, literacy, transparency and high-risk categories separately.

The Commission's checked timeline states general application from 2 August 2026 with exceptions, and reports the AI Omnibus entered into force on 27 July 2026, extending Annex III high-risk requirements to 2 December 2027 and Annex I product-related requirements to 2 August 2028. These extensions do not defer all AI Act duties. Retrieve the current consolidated legal text for any actual EU release decision. [Commission timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [Omnibus update](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force).

A chatbot may fall under the Online Safety Act depending on search/user-to-user/pornographic functionality and UK links. Run Ofcom's scope checker; do not assume all chatbots are covered or exempt. [Ofcom chatbot guidance](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ai-chatbots-and-online-regulation-what-you-need-to-know).

## Acceptance and tests

- Contractor code without assignment cannot be represented as fully owned.
- Customer asks to upload scraped competitor documentation: assess rights and purpose, do not approve automatically.
- HR ranking with rubber-stamp human review triggers significant-decision and equality analysis.
- Model version change invalidates affected evaluation approval.
- Agent tools cannot sign contracts or issue refunds outside approved authority.

Owner: product/engineering with legal/privacy reviewers. Verified 2026-10-09. Sources IP01–IP03, A01–A04. Certification and competence claims need evidence; an AI agent cannot claim to be a qualified solicitor.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
