---
id: LEMURAN-UK-08
title: "Cybersecurity, employment, contractors and insurance"
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

# Cybersecurity, employment, contractors and insurance

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## Cybersecurity

**LAW:** where processing personal data, implement security appropriate to risk under UK GDPR, including relevant confidentiality, integrity, availability, resilience, restoration and testing. **CONTRACT:** apply agreed controls and incident notice terms. **PRACTICE:** use NCSC guidance and risk-based assurance; ISO/SOC/Cyber Essentials are not compulsory for every SaaS. [NCSC small organisations guide](https://www.ncsc.gov.uk/collection/small-organisations-guide-to-cyber-security).

Proposed implementation baseline: MFA/passkeys for privileged access; least privilege; separate production/test; tenant authorisation enforced server-side; secure secrets; encryption with controlled keys; patch/dependency management; logging without unnecessary content; tested backups; incident response; supplier security review; secure development and change review. Security lead defines measurable thresholds based on actual risk and commitments rather than claiming the law prescribes one universal patch window.

AI-specific tests should cover prompt injection from retrieved documents, tool misuse, cross-tenant retrieval, training-data leakage, poisoned knowledge, unsafe output rendering, data exfiltration and excessive permissions. Client work requires explicit authorised scope for security testing and a restoration plan. Never run intrusive tests against third parties solely because they are connected to a client workflow.

Scope-check NIS obligations and any commenced cyber reforms when providing relevant cloud/managed/digital services; consumer connected-device security rules are not automatically applicable to pure SaaS. Record applicability rather than asserting a sector exemption without review. A data breach, cyber incident and contractual outage have overlapping but different reporting paths.

## Employees and contractors

**CONDITIONAL LAW:** assess employee/worker/self-employed status from actual arrangements and employment law, with a separate tax-status assessment. Contract labels do not settle either. Verify right-to-work duties for employees, required written employment particulars, pay/working-time/holiday rights, pension auto-enrolment, payroll, health/safety and equality obligations where applicable. [Employment status](https://www.gov.uk/employment-status).

For contractors/intermediaries, assess IR35/off-payroll rules, client size/sector and allocation of determination duties. The small-private-client position differs from medium/large/private or public-sector cases; do not infer the exemption from “startup” branding. Record working practices, substitution/control and relevant evidence. Overseas engagements can create local employment/tax duties despite a UK contract. [HMRC off-payroll rules](https://www.gov.uk/guidance/understanding-off-payroll-working-ir35).

**WATCH / effective-date check:** Employment Rights Act 2025 implementation is phased. The government's checked timeline was updated 25 September 2026 to confirm October measures. Before recruitment, dismissal, harassment policies, sick-pay calculations or tribunal deadlines, retrieve the current provisions and transitional rules. Do not reuse an old three-month tribunal deadline or assume every new employment right commenced together. [Implementation timeline](https://www.gov.uk/government/publications/implementing-the-plan-to-make-work-pay-and-employment-rights-act).

## Proposed people workflow

Before start: status/tax assessment → jurisdiction/right-to-work check where required → signed engagement with duties/pay, confidentiality, IP, acceptable AI use and security → payroll/pension/insurance assessment → least-privilege accounts and training. During work: review permissions, actual practices, performance and wellbeing; monitor only transparently and proportionately. At exit: assess notice/rights, revoke sessions/keys, return equipment, hand over work, preserve necessary evidence and delete unnecessary copies.

Do not upload CVs, disciplinary files, health data or identity documents to an unapproved LLM. Restrictive covenants and NDAs need tailored review and must not purport to prevent protected disclosures or other legally protected reporting. Employment decisions about an individual remain with an authorised human and must not be based on inferred protected characteristics.

## Insurance

| Type | Classification | Review questions |
|---|---|---|
| Employers' liability | CONDITIONAL LAW | Required employers ordinarily need at least £5m cover from an authorised insurer; assess exemptions and territory carefully |
| Professional indemnity / technology errors and omissions | PRACTICE or CONTRACT; may be sector-dependent | Does it cover AI output, automation mistakes, software failure and subcontractors? |
| Cyber | PRACTICE or CONTRACT | Breach response, restoration, interruption, ransomware conditions and notice obligations |
| Public liability | PRACTICE or CONTRACT | Client-site work and third-party injury/property risk |
| Directors and officers | PRACTICE | Management claims, exclusions and company size |
| Legal expenses | PRACTICE | Panel counsel, consent to costs, covered disputes and limits |

Check the Employers' Liability exemption rules specifically for a limited company; do not assume a family-only workforce always exempts it. Northern Ireland and overseas workers need jurisdiction-specific review. [GOV.UK EL guidance](https://www.gov.uk/employers-liability-insurance).

Record insurer, policy period, limits, excess, retroactive date, territorial/jurisdiction scope, claims-made/run-off terms, AI/IP exclusions, notification windows and warranties. Only represent cover shown in the policy. Report claims/circumstances promptly through authorised channels; do not admit liability or appoint expensive advisers contrary to policy conditions without review. Buying insurance does not discharge statutory duties.

## Tests and acceptance

Unknown worker status routes to assessment, not a contractor template. New hire cannot bypass EL/pension/payroll review. Expired insurance must fail a proposal claim. Backup evidence requires a restore result, not just a configured job. Accepted outcome: capability-backed security schedule, completed onboarding/offboarding controls, and broker-reviewed insurance matrix. Verified 2026-10-09; sources S01, H01–H04 and P01.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
