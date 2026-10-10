---
id: LEMURAN-UK-05
title: "PECR, cookies, tracking and marketing"
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

# PECR, cookies, tracking and marketing

Company-wide scope: apply this reference to Lemuran Ltd’s corporate/internal matters, all services and engagements, and every current or future product as relevant. FAQai.app examples do not limit applicability. See [the Legal Team Charter](20_LEGAL_TEAM_CHARTER.md).

## Executive summary

PECR applies to device storage/access and communications marketing; UK GDPR additionally applies where personal data is processed. A lawful basis under GDPR does not waive a PECR consent requirement. Marketing lead owns recipient classification; engineering owns tag behaviour; privacy lead reviews exemptions. Sources M01–M04.

## Website and application controls

**LAW:** assess cookies, local storage, pixels, SDKs, fingerprinting and similar technologies by purpose. Consent must precede use unless a valid exception applies. Avoid describing only cookies while deploying equivalent tracking elsewhere.

Current ICO guidance recognises five exception categories: communications transmission, strictly necessary service delivery, specified statistics, appearance/functionality preferences, and emergency assistance. These are purpose-limited. Statistics/appearance exceptions require information and a simple free objection route; their other conditions must also be satisfied. Advertising or cross-service profiling does not become exempt by calling it analytics. [ICO exception guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/what-are-the-exceptions/).

**POLICY:** if an exception is unresolved, block the affected technology pending consent or verified exception. Consent design should provide clear choices, reject optional uses without friction, granular purposes where needed and easy withdrawal. Consent evidence includes notice version, time, choices, withdrawal and enforcement result. Do not bundle necessary account terms with optional marketing agreement.

## Marketing decision table

| Channel/recipient | Binding rule to assess | Operational output |
|---|---|---|
| Unsolicited email/SMS to consumers, sole traders or relevant partnerships | Prior consent or valid soft opt-in; identify sender and provide opt-out | Consent evidence or documented soft-opt-in conditions |
| Email to corporate subscribers such as limited companies | PECR does not generally require prior consent; named contacts still invoke GDPR | Lawful basis, transparency and suppression screening |
| Live marketing calls | TPS/CTPS and objection checks, identification; sector-specific restrictions | Dated screening and call rationale |
| Automated recorded marketing calls | Specific consent rules | No automated campaign based merely on a public phone number |
| Social direct messages | Electronic-mail marketing rules may apply | Treat channel as marketing, not a loophole |
| Transactional messages | Classify actual content; promotions can make them marketing | Approved message purpose |

For the ordinary commercial soft opt-in, Lemuran must obtain details during a sale or negotiations for a sale of its product/service, market its own similar products/services, and provide an opt-out when collecting details and in every message. Purchased lists and third-party scraping do not establish these conditions. A free account is not automatically proof of negotiations. The charitable soft opt-in is not a general exemption for a commercial agency. [ICO electronic-mail rules](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/).

## Sales-data workflow

Classify corporate versus individual subscriber → establish source and purpose → select applicable PECR route and GDPR basis → provide required privacy information (including indirect collection rules) → screen suppression/TPS/CTPS as relevant → review exact audience and message → authorised send → process opt-outs. Legitimate interests needs a reasoned assessment where relied on, not a label copied into a CRM.

Keep minimal suppression records to honour objections rather than deleting every trace and accidentally reimporting the contact. Do not infer consent from business cards, public profiles, silence or pre-ticked boxes. Named work emails remain personal data. [ICO B2B guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing).

## Claims and reviews

**LAW:** avoid misleading claims, concealed paid endorsements and fake consumer reviews. Substantiate statements such as “GDPR compliant”, “100% accurate”, “fully autonomous”, “UK-only data” and “guaranteed savings”. AI-generated testimonials must never be represented as real customer experiences. File 06 covers consumer pricing/reviews. **PRACTICE:** approve a claims register with supporting tests, limitations, owner and expiry.

## Tests and acceptance

- Fresh visitor rejecting optional tracking must not trigger advertising calls.
- Withdrawal must affect subsequent device access; account deletion is not the only withdrawal path.
- Statistics exception with no objection route fails.
- Imported lead marked “B2B” but actually a sole trader fails the corporate-subscriber shortcut.
- An opted-out address remains suppressed after CRM reimport.

Verified 2026-10-09. Acceptance: evidence from network/tag tests and recipient records, not only banner screenshots or written policies. Proposed campaign approval is a company control; nothing here authorises sending marketing messages.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-09 | Initial UK/Lemuran knowledge pack and implementation specification; draft for review. |

Revision 1.1.0 (2026-10-10): company-wide scope alignment; legal-source verification remains 2026-10-09.
