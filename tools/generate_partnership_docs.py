#!/usr/bin/env python3
"""Generate the Partnership Documentation skill set for AIBOS Phase 05.

Creates 02_ARTEFACTS/PHASE_05_SKILLS/Partnership_Documentation/ with:
  * 00_UK_PARTNERSHIP_FRAMEWORK.md      — shared reference: when to use which
                                          partnership instrument, binding vs
                                          non-binding, competition-law and
                                          "no legal partnership" caveats, IP,
                                          revenue/tax, data sharing, governance
                                          and exit principles, official refs.
  * NN_<DOC>_SKILL.md                   — one generate-ready skill per partnership
                                          document (LOI, MOU, Alliance Agreement,
                                          Teaming, Partnership SOW, Reseller,
                                          Referral, Revenue Share, Co-Marketing,
                                          Joint Venture, Data Sharing, Governance,
                                          Exit Deed).
  * README.md                           — the Partnership Documentation index.

Each skill embeds a full, UK (England & Wales) blueprint so that when the skill is
referenced, an AI agent (or a person) can produce the actual document. Content is
grounded in the Lemuran Ltd — UK Client Engagement Legal & Contracting Guide
(00_ROOT/) IP/liability/data principles and standard UK best practice for
commercial collaborations (Partnership Act 1890 caveats, UK competition law /
Competition Act 1998, UK GDPR / ICO Data Sharing Code, Bribery Act 2010,
Commercial Agents Regulations 1993, electronic-execution guidance).

These are practical drafting aids, NOT legal advice. High-value, exclusive,
equity, cross-border, competition-sensitive or complex partnerships must be
reviewed by a UK-qualified solicitor before signing.

Re-run any time; it overwrites only files inside the Partnership_Documentation/ folder.
"""

from __future__ import annotations

import pathlib

REPO = pathlib.Path(__file__).resolve().parents[1]
OUT = REPO / "02_ARTEFACTS" / "PHASE_05_SKILLS" / "Partnership_Documentation"
CREATED = "2026-10-07"
FRAMEWORK_FILE = "00_UK_PARTNERSHIP_FRAMEWORK.md"
CORE_MAX = 5  # docs 1..5 are the Core (formation) pack; 6+ are Extended.

# Relative paths from a skill file inside Partnership_Documentation/.
R_HOME = "../../../README.md"
R_INDEX = "../../../ROOT_INDEX.md"
R_SPEC = "../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md"
R_GLOSSARY = "../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md"
R_SKILLS = "../README.md"
R_GUIDE = "../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md"
R_RULES = "../../PHASE_06_RULES/README.md"
R_TEMPLATES = "../../PHASE_09_TEMPLATES/README.md"

# Cross-links into the sibling Business Documentation set (reused, not duplicated).
R_BIZ_INDEX = "../Business_Documentation/README.md"
R_BIZ_FRAMEWORK = "../Business_Documentation/00_UK_CONTRACTING_FRAMEWORK.md"
R_BIZ_NDA = "../Business_Documentation/01_MUTUAL_NDA_SKILL.md"
R_BIZ_DPA = "../Business_Documentation/06_DATA_PROCESSING_AGREEMENT_SKILL.md"
R_BIZ_DSA = "../Business_Documentation/23_DATA_SHARING_AGREEMENT_SKILL.md"
R_BIZ_SOW = "../Business_Documentation/05_STATEMENT_OF_WORK_SKILL.md"

STANDARDS_DEFAULT = [
    "UK GDPR",
    "Data Protection Act 2018",
    "Competition Act 1998",
    "Bribery Act 2010",
    "ISO 27001",
]

LEGAL_NOTICE = (
    "> **Legal notice.** This skill produces a **draft** partnership document to speed "
    "up preparation. It is **not legal advice** and is **not a substitute for review by "
    "a UK-qualified solicitor**. Partnership, alliance, reseller, revenue-share and "
    "joint-venture arrangements can raise competition-law, tax, employment, agency and "
    "unintended-liability issues — obtain solicitor sign-off for exclusive, equity, "
    "cross-border, competition-sensitive, high-value or otherwise complex deals before "
    "signing. Unless otherwise agreed, the governing law is **England and Wales**. Do "
    "not store passwords, API keys or production credentials in generated documents."
)

GENERATE_INSTRUCTION = (
    "When this skill is invoked, generate the document by expanding each blueprint "
    "section below into clear, formal UK business English, filling every placeholder "
    "from the *Inputs Required*, resolving or flagging any missing input, marking the "
    "output as a draft, and appending a dated signature block for the authorised "
    "signatories. State the binding status explicitly, keep the parties' obligations "
    "balanced, and stay consistent with the "
    "[UK Partnership Framework](" + FRAMEWORK_FILE + ")."
)

DOCS = [
{
  "num": 1, "slug": "LETTER_OF_INTENT", "title": "Letter of Intent (Heads of Terms)",
  "short": "Records the parties' intent to explore a partnership and the key terms, before a binding agreement is negotiated.",
  "binding": "Generally non-binding as to the deal, except confidentiality, exclusivity, costs and governing law, which are expressed to bind.",
  "signatories": "Authorised signatory of each prospective partner.",
  "ai_level": "Fully AI-draftable from the outline deal; human review of what is intended to bind.",
  "purpose": [
    "A Letter of Intent (LOI) or Heads of Terms sets out, early and quickly, that two companies intend to work towards a partnership and the principal terms they have provisionally agreed — scope, structure, economics and timeline — so negotiation of the full agreement starts from a shared position.",
    "It is normally non-binding as to the commercial deal, with a small number of clauses (confidentiality, exclusivity, costs, governing law) deliberately made binding. Its status must be stated expressly to avoid accidentally creating a contract.",
  ],
  "when_use": [
    "At the start of a potential partnership, alliance, reseller, JV or acquisition-style discussion.",
    "To secure a period of exclusivity while the full agreement is negotiated.",
    "To align both sides' decision-makers on headline terms before investing in legal drafting.",
  ],
  "blueprint": [
    ("Parties and purpose", "Legal names, company numbers and the purpose of the proposed collaboration."),
    ("Summary of the proposed deal", "High-level description of the partnership model and what each party brings."),
    ("Key proposed terms", "Provisional scope, structure, economics (margin/commission/share), term and territory."),
    ("Conditions to a binding deal", "What must happen first (due diligence, approvals, definitive agreement)."),
    ("Exclusivity", "Whether and for how long the parties will not negotiate with others (binding, if agreed)."),
    ("Confidentiality", "Binding confidentiality (or reference to the existing Mutual NDA)."),
    ("Costs", "Each party bears its own costs unless agreed otherwise."),
    ("Binding vs non-binding statement", "Explicitly state which clauses bind and that the rest is subject to contract."),
    ("Timetable", "Indicative milestones towards signing the definitive agreement."),
    ("Governing law and jurisdiction", "England and Wales (binding)."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Names, company numbers and registered addresses of both parties.",
    "Headline deal terms (model, scope, economics, term, territory).",
    "Whether exclusivity applies and for how long; which clauses are intended to bind.",
    "Target timetable to a definitive agreement.",
  ],
  "uk_notes": [
    "Mark the document 'subject to contract' and state clearly which clauses are binding — otherwise sufficiently certain terms acted upon can form a contract.",
    "Keep deal language provisional ('the parties intend to'), not definite ('the parties shall'), for non-binding sections.",
    "Exclusivity, confidentiality, costs and governing law are the clauses usually made binding.",
  ],
  "best": [
    "Reference the signed Mutual NDA rather than restating full confidentiality.",
    "Do not include firm prices or fixed delivery promises you are not ready to be held to.",
    "Set a realistic deadline so the LOI does not drift.",
  ],
  "related": [2, 3, 10],
},
{
  "num": 2, "slug": "MEMORANDUM_OF_UNDERSTANDING", "title": "Memorandum of Understanding (MOU)",
  "short": "A non-binding framework describing how two organisations intend to collaborate, their roles and shared objectives.",
  "binding": "Non-binding as to the collaboration, except any clauses expressly stated to bind (confidentiality, IP ground rules, governing law).",
  "signatories": "Authorised signatory of each organisation.",
  "ai_level": "Fully AI-draftable from the collaboration outline; human review of scope and binding carve-outs.",
  "purpose": [
    "A Memorandum of Understanding (MOU) records a shared understanding between two organisations about why and how they intend to collaborate — objectives, respective roles, contributions, and the areas they will work on — without (usually) creating binding commercial obligations.",
    "It is widely used to signal commitment publicly or internally, to frame a longer-term relationship, and to set the ground rules before (or alongside) binding agreements such as an Alliance Agreement or specific SOWs.",
  ],
  "when_use": [
    "To frame a strategic relationship or collaboration programme at a high level.",
    "Where the parties want a documented understanding but are not ready for binding commitments.",
    "For public-sector, academic, not-for-profit or ecosystem collaborations where an MOU is the expected instrument.",
  ],
  "blueprint": [
    ("Parties and background", "Legal names and the context/motivation for collaborating."),
    ("Shared objectives", "The outcomes both organisations want from the collaboration."),
    ("Scope of collaboration", "Areas, activities and initiatives the parties will pursue together."),
    ("Roles and contributions", "What each party will contribute (people, technology, access, funding, brand)."),
    ("Governance and contacts", "Named relationship owners, meeting cadence, how decisions are coordinated."),
    ("Resourcing and costs", "Each party bears its own costs unless a separate agreement says otherwise."),
    ("Intellectual property ground rules", "Each keeps its Background IP; separate agreements govern any jointly created IP."),
    ("Confidentiality", "Binding confidentiality or reference to the Mutual NDA."),
    ("Data protection", "Personal data shared only under a separate DPA/Data Sharing Agreement."),
    ("Status — non-binding", "Express statement that the MOU does not create legally binding obligations except the stated clauses."),
    ("Term and review", "Duration, review points and how either party may withdraw."),
    ("Relationship clause", "No partnership (legal sense), agency or authority to bind the other."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Both organisations' legal details and relationship owners.",
    "Shared objectives, scope of collaboration and each party's contributions.",
    "Governance/meeting cadence; review and withdrawal terms.",
    "Which clauses (if any) are intended to bind.",
  ],
  "uk_notes": [
    "State unambiguously that the MOU is not legally binding (except named clauses); courts look at substance, so avoid definite obligation language elsewhere.",
    "Include the 'no legal partnership/agency' clause so the MOU cannot imply a Partnership Act 1890 relationship.",
    "If personal data will be shared, do not rely on the MOU — put a Data Sharing Agreement or DPA in place.",
  ],
  "best": [
    "Keep it strategic and short; move binding detail into the Alliance Agreement or an SOW.",
    "Name a relationship owner on each side so the MOU is acted on, not shelved.",
    "Set a review date and a clean, no-fault withdrawal mechanism.",
  ],
  "related": [1, 3, 9, 11],
},
{
  "num": 3, "slug": "STRATEGIC_PARTNERSHIP_AGREEMENT", "title": "Strategic Partnership / Alliance Agreement",
  "short": "The binding master agreement governing an ongoing, non-equity partnership between two companies.",
  "binding": "Binding once signed; the master framework under which joint activities and SOWs run.",
  "signatories": "Authorised signatory of each partner.",
  "ai_level": "AI-draftable from a firm-approved base; SOLICITOR review required before first use and for exclusivity, IP or competition-sensitive terms.",
  "purpose": [
    "A Strategic Partnership (or Alliance) Agreement sets the binding legal and commercial rules for an ongoing collaboration between two independent companies that are not forming a separate legal entity — covering scope, each party's commitments, IP and brand use, economics, governance, liability, confidentiality, term and exit.",
    "It is the backbone under which specific joint activities, co-marketing, reseller/referral arrangements or joint-delivery SOWs are then executed as schedules or linked agreements.",
  ],
  "when_use": [
    "An ongoing, multi-initiative relationship (not a single bid or one-off deal).",
    "Where the parties want stable alliance terms with specific activities run under schedules/SOWs.",
    "As the master agreement that Revenue Share, Co-Marketing, Data Sharing and Governance schedules attach to.",
  ],
  "blueprint": [
    ("1. Parties and definitions", "Legal names, company numbers, registered offices and defined terms."),
    ("2. Purpose and scope of the alliance", "Objectives, fields of collaboration and what is in/out of scope."),
    ("3. Nature of relationship", "Independent contractors; no partnership (legal sense), agency, employment or authority to bind."),
    ("4. Each party's commitments", "What each party will do, provide and maintain."),
    ("5. Exclusivity (if any)", "Scope, territory and duration of any exclusivity (flag for competition-law review)."),
    ("6. Joint activities and SOWs", "How specific initiatives are agreed and documented (link to Partnership SOW)."),
    ("7. Economics and revenue sharing", "Charging/revenue/commission model (detail in the Revenue Share Schedule)."),
    ("8. Intellectual property", "Each keeps Background IP; licences granted; ownership of jointly created IP."),
    ("9. Brand and trade-mark use", "Controlled licence for names/logos; approval and quality control (link to Co-Marketing)."),
    ("10. Confidentiality", "Mutual obligations (or incorporate the Mutual NDA)."),
    ("11. Data protection", "UK GDPR roles; DPA or Data Sharing Agreement where personal data is involved."),
    ("12. Information security", "Security expectations where systems/data are accessed."),
    ("13. Warranties", "Authority, skill and care, compliance with law."),
    ("14. Anti-bribery and sanctions", "Bribery Act 2010 and sanctions compliance."),
    ("15. Compliance with competition law", "Each party complies; no unlawful coordination or information exchange."),
    ("16. Liability and indemnities", "Caps, excluded losses, carefully scoped indemnities; non-excludable liabilities preserved."),
    ("17. Insurance", "Cover each party maintains."),
    ("18. Governance", "Joint Steering Committee, cadence, decisions, escalation (link to Governance ToR)."),
    ("19. Non-solicitation", "Reasonable, time-limited, where justified."),
    ("20. Term and termination", "Duration, renewal, termination for cause/convenience/insolvency/change of control."),
    ("21. Consequences of termination and run-off", "Wind-down of live initiatives, trailing economics, licence survival, customer/data handover (link to Exit Deed)."),
    ("22. Dispute resolution", "Escalation and, optionally, mediation before litigation."),
    ("23. Boilerplate", "Notices, assignment, third-party rights, entire agreement, variation, waiver, severability, counterparts, e-signature."),
    ("24. Governing law and jurisdiction", "England and Wales; exclusive jurisdiction."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Both parties' legal details and authorised signatories.",
    "Alliance scope, each party's commitments and any exclusivity.",
    "Economic model, IP/brand licences, governance structure.",
    "Liability caps, insurance levels, term and exit terms.",
  ],
  "uk_notes": [
    "Include an explicit 'no legal partnership/agency' clause to avoid Partnership Act 1890 joint liability.",
    "Exclusivity, pricing coordination and information sharing can engage the Competition Act 1998 — obtain competition-law advice.",
    "Align the liability cap with available insurance; do not exclude non-excludable liabilities (death/personal injury from negligence, fraud).",
    "Put the detailed economics in a schedule so the master terms stay stable.",
  ],
  "best": [
    "Keep the master agreement stable; run specific initiatives through schedules/SOWs.",
    "Control brand/trade-mark use with approval and quality rights.",
    "Have a UK commercial solicitor produce or review the first reusable alliance agreement.",
  ],
  "related": [2, 5, 8, 12, 13],
},
{
  "num": 4, "slug": "TEAMING_AGREEMENT", "title": "Teaming Agreement",
  "short": "Binds two companies to bid jointly for one specific opportunity and sets what happens if they win.",
  "binding": "Binding for the bid phase; commits the parties to pursue the opportunity together and to contract if awarded.",
  "signatories": "Authorised signatory of each team member (typically a lead/prime and a partner).",
  "ai_level": "AI-draftable from the opportunity details; human review of exclusivity, work-share and award terms.",
  "purpose": [
    "A Teaming Agreement commits two (or more) companies to collaborate on a specific bid, tender or opportunity — defining who leads, each party's role and work-share, bid responsibilities and costs, exclusivity for that opportunity, and the agreement to enter a subcontract or joint contract if the bid succeeds.",
    "It de-risks joint pursuits by fixing the ground rules before the win, so the parties are not negotiating basic terms under award-deadline pressure.",
  ],
  "when_use": [
    "Pursuing a single client tender, framework or RFP jointly.",
    "Where one party is prime/lead and the other is a specialist partner.",
    "Where exclusivity and a defined work-share for that opportunity are needed up front.",
  ],
  "blueprint": [
    ("Parties and roles", "Identify the lead/prime and the partner, and the opportunity being pursued."),
    ("The opportunity", "The specific client, tender or RFP, and its scope."),
    ("Exclusivity for the opportunity", "Neither party teams with a competitor for this opportunity during the bid."),
    ("Bid responsibilities", "Who prepares what; timelines; approvals; single point of contact with the client."),
    ("Work-share on award", "Each party's intended scope/share of the work if the bid wins."),
    ("Bid costs", "Each party bears its own bid costs unless agreed otherwise."),
    ("Confidentiality", "Protection of each party's and the client's information (or reference the NDA)."),
    ("Commitment to contract on award", "Obligation to negotiate in good faith and sign a subcontract or joint contract if awarded (link to Partnership SOW/subcontract)."),
    ("Intellectual property", "Ownership of bid materials and each party's Background IP."),
    ("Publicity", "No announcements without consent and (where required) the client's consent."),
    ("Term", "Runs until award, non-award, or withdrawal of the opportunity."),
    ("Relationship clause", "Independent parties; no partnership (legal sense) or authority to bind beyond the bid."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "The specific opportunity (client, tender reference, scope).",
    "Lead/prime and partner roles; intended work-share on award.",
    "Bid responsibilities, timeline and cost treatment.",
    "Exclusivity scope and duration for the opportunity.",
  ],
  "uk_notes": [
    "Keep exclusivity limited to the specific opportunity to reduce competition-law risk; broad exclusivity needs review under the Competition Act 1998.",
    "Make the 'commit to contract if awarded' obligation clear but realistic — an unconditional pre-agreed subcontract is cleaner than an 'agreement to agree'.",
    "Respect the client's own procurement rules on teaming, subcontracting and disclosure.",
  ],
  "best": [
    "Attach or pre-agree the key subcontract terms so award does not trigger a fresh negotiation.",
    "Define a single client-facing point of contact to avoid mixed messages.",
    "State clearly who owns the bid materials.",
  ],
  "related": [3, 5, 1],
},
{
  "num": 5, "slug": "PARTNERSHIP_STATEMENT_OF_WORK", "title": "Partnership Statement of Work (Joint Delivery)",
  "short": "Defines a specific joint engagement delivered by both partners, with each party's scope, responsibilities, economics and acceptance.",
  "binding": "Binding once signed; executed under the Alliance or Teaming Agreement and takes precedence on engagement-specific matters.",
  "signatories": "Authorised signatory of each partner (and, where relevant, acknowledged by the end client).",
  "ai_level": "Fully AI-draftable from scope inputs; human review of split of responsibilities, economics and acceptance.",
  "purpose": [
    "A Partnership Statement of Work (SOW) describes a single joint engagement delivered by both partners: the combined scope and deliverables, the split of responsibilities between the parties, the timeline, the economics (revenue split and who invoices the client), and objective acceptance criteria.",
    "It differs from a client-delivery SOW by making the inter-party division of work and revenue explicit, so both partners know exactly who does what, who carries which risk, and how money flows.",
  ],
  "when_use": [
    "Delivering a specific project jointly under an Alliance or Teaming Agreement.",
    "Where responsibilities and revenue must be split clearly between the partners.",
    "Where the end client needs one combined scope and acceptance.",
  ],
  "blueprint": [
    ("SOW reference and governing agreement", "Unique number; effective date; the Alliance/Teaming Agreement it runs under."),
    ("Engagement background and objectives", "The client/opportunity and the outcomes sought."),
    ("Combined scope and deliverables", "The full scope and each tangible output."),
    ("Split of responsibilities", "Exactly which party delivers which workstream/deliverable."),
    ("Dependencies between partners", "What each partner must provide to the other and by when."),
    ("Timeline and milestones", "Phased plan with owners across both parties."),
    ("Client-facing and lead party", "Who contracts with and invoices the client; who leads delivery."),
    ("Economics and revenue split", "Fees, the split between partners, and payment flow (link to Revenue Share Schedule)."),
    ("Acceptance criteria", "Objective, measurable criteria per deliverable and the acceptance process."),
    ("Intellectual property", "Ownership/licence of deliverables and each party's Background IP."),
    ("Data protection and security", "Flag where personal data is processed (trigger DPA/Data Sharing Agreement)."),
    ("Liability between partners", "How risk and liability are shared for this engagement."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Governing Alliance/Teaming Agreement reference; SOW number and dates.",
    "Combined scope, deliverables and the split of responsibilities between partners.",
    "Economics and revenue split; who invoices the client.",
    "Acceptance criteria; IP, data-protection and security flags.",
  ],
  "uk_notes": [
    "Make acceptance criteria objective and testable, as with a client SOW (see the Business Docs Statement of Work).",
    "Be explicit about which partner carries delivery and payment risk, and how shortfalls are handled.",
    "Where personal data is processed jointly, put the correct UK GDPR instrument in place before starting.",
  ],
  "best": [
    "Map every deliverable to exactly one responsible partner.",
    "Tie the revenue split to the responsibility split to avoid disputes.",
    "Keep the client-facing scope consistent with each partner's internal scope.",
  ],
  "related": [3, 4, 8],
  "refs": [
    ("Business Docs — Statement of Work skill", R_BIZ_SOW),
  ],
},
{
  "num": 6, "slug": "RESELLER_AGREEMENT", "title": "Reseller / Channel Partner Agreement",
  "short": "Authorises a partner to resell the company's product or SaaS, setting discount/margin, territory, obligations and brand use.",
  "binding": "Binding once signed; governs the reseller relationship and individual resales.",
  "signatories": "Authorised signatory of the Supplier (vendor) and the Reseller.",
  "ai_level": "AI-draftable from a channel base; solicitor review for exclusivity, resale-pricing and liability.",
  "purpose": [
    "A Reseller (or Channel Partner) Agreement lets a partner sell the company's product or SaaS to end customers, defining whether the partner resells in its own name or refers, the discount/margin or price, the territory and any exclusivity, the partner's sales and support obligations, brand use, and end-customer terms.",
    "It grows distribution while protecting the vendor's brand, pricing integrity (within competition-law limits), customers and IP.",
  ],
  "when_use": [
    "A partner will sell your product/SaaS to its own customers.",
    "Building a channel/distribution network or regional coverage.",
    "Where margin, territory and support responsibilities must be defined.",
  ],
  "blueprint": [
    ("Parties and appointment", "Appoint the reseller; state exclusive or non-exclusive and the territory."),
    ("Products and resale model", "What may be resold and whether the reseller resells in its own name or as an agent."),
    ("Pricing, discount and margin", "Vendor price and reseller discount/margin; the reseller sets its own resale price (RPM caution)."),
    ("Orders and provisioning", "How the reseller orders, how customers are provisioned and activated."),
    ("Reseller obligations", "Sales effort, minimum commitments (if any), accreditation/training, first-line support."),
    ("Vendor obligations", "Product supply, updates, second-line support, enablement materials."),
    ("End-customer terms and EULA", "The customer must accept the vendor's end-user terms; flow-down obligations."),
    ("Brand and trade-mark licence", "Controlled use of the vendor's marks; brand guidelines and approval."),
    ("Intellectual property", "No IP transfer; licence only to market and resell."),
    ("Data protection", "UK GDPR roles for customer data; DPA/Data Sharing Agreement as applicable."),
    ("Anti-bribery and lawful sales", "Bribery Act 2010 compliance; no misrepresentation; honest marketing."),
    ("Warranties and liability", "Product warranty scope; caps and excluded losses; non-excludable liabilities preserved."),
    ("Term, renewal and termination", "Duration; termination for cause/convenience/insolvency/change of control."),
    ("Post-termination", "Run-off of existing customers, trailing margin, customer transition, licence survival."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Products/SaaS to be resold; exclusive or non-exclusive; territory.",
    "Pricing, discount/margin and any minimum commitments.",
    "Support split; brand-use rules; end-customer terms.",
    "Term, renewal and post-termination treatment of customers.",
  ],
  "uk_notes": [
    "Resale price maintenance (fixing the reseller's resale price or minimum price) is generally unlawful under UK competition law — the reseller must be free to set its resale price; you may set a recommended price only.",
    "Exclusivity and territorial restrictions can engage the Competition Act 1998 — review before granting.",
    "Reseller commissions/discounts carry Bribery Act 2010 risk — include ABC warranties and audit rights.",
  ],
  "best": [
    "Set a recommended (not mandatory) resale price; let the reseller price freely.",
    "Define support tiers clearly (first-line reseller, second-line vendor).",
    "Protect existing customers with run-off and transition terms on exit.",
  ],
  "related": [3, 7, 8],
},
{
  "num": 7, "slug": "REFERRAL_AGREEMENT", "title": "Referral / Introducer Agreement",
  "short": "Pays a partner a commission for introducing qualified leads that convert, without the partner reselling or advising.",
  "binding": "Binding once signed; governs introductions and commission.",
  "signatories": "Authorised signatory of the Supplier and the Referrer/Introducer.",
  "ai_level": "Fully AI-draftable from a commission model; human review of agency status and commission terms.",
  "purpose": [
    "A Referral (or Introducer) Agreement rewards a partner for introducing prospective customers that go on to buy, defining what counts as a qualifying introduction, the commission, how long referrals are tracked, and the limits on the referrer's role (introduce only — not resell, advise, or bind the company).",
    "It is the lightest-touch channel model: the company contracts directly with the customer, and the referrer is paid for the introduction.",
  ],
  "when_use": [
    "A partner will pass leads but not sell, advise or contract with the customer.",
    "Low-friction channel or affiliate arrangements.",
    "Where commission on converted introductions is the agreed reward.",
  ],
  "blueprint": [
    ("Parties and role", "Appoint the referrer to introduce leads only; no authority to bind, advise or resell."),
    ("Qualifying introduction", "What counts as a valid, trackable introduction (named contact, consent, registration)."),
    ("Referral process and tracking", "How referrals are submitted, acknowledged and tracked; duplicate/conflict handling."),
    ("Attribution window", "How long after introduction a conversion earns commission."),
    ("Commission", "Rate, base amount, qualifying event (signed/paid), exclusions (refunds, taxes, churn) — link to Revenue Share Schedule."),
    ("Payment and reporting", "Invoicing, VAT treatment, payment timing, statements and audit rights."),
    ("Data protection", "Lawful basis for sharing contact data; consent/legitimate interests; transparency to the lead."),
    ("Anti-bribery", "Bribery Act 2010 compliance; no inducements to improper conduct; honest representation."),
    ("No agency / no authority", "Referrer cannot make representations, give advice or bind the company."),
    ("Confidentiality", "Protect company and customer information."),
    ("Term and termination", "Duration; treatment of in-flight referrals and trailing commission on exit."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Commission rate, base and qualifying event; attribution window.",
    "Referral submission/tracking process and exclusions.",
    "Data-sharing basis for lead contact details.",
    "Term and trailing-commission treatment.",
  ],
  "uk_notes": [
    "Check whether the arrangement makes the partner a 'commercial agent' under the Commercial Agents (Council Directive) Regulations 1993 — a true agent may be entitled to compensation/indemnity on termination; a mere introducer usually is not.",
    "Sharing a lead's personal data needs a lawful basis and transparency under UK GDPR — do not pass contact details without this.",
    "Referral commissions are a common Bribery Act 2010 risk, especially in regulated sectors — include ABC terms.",
  ],
  "best": [
    "Define 'qualifying introduction' and the attribution window precisely to avoid commission disputes.",
    "Keep the referrer as introducer-only, with no authority to advise or bind.",
    "Confirm the lead has been told their details may be shared.",
  ],
  "related": [6, 8, 3],
},
{
  "num": 8, "slug": "REVENUE_SHARE_SCHEDULE", "title": "Revenue Share and Commission Schedule",
  "short": "The economics schedule attaching to an alliance, reseller or referral agreement: base, rate, qualifying events, reporting and audit.",
  "binding": "Binding schedule to its parent agreement; governs the money.",
  "signatories": "Authorised signatory of each party (as a schedule to the parent agreement).",
  "ai_level": "Fully AI-draftable from the commercial model; human/finance review of rates, VAT and exclusions.",
  "purpose": [
    "A Revenue Share and Commission Schedule sets out exactly how money flows in a partnership: the base amount the share/commission is calculated on, the rate(s), the qualifying events that trigger payment, the exclusions (refunds, taxes, chargebacks, churn), and the reporting, reconciliation and audit mechanics.",
    "Putting the economics in a schedule keeps the parent agreement stable and makes disputes rare by removing ambiguity about who gets paid what, when.",
  ],
  "when_use": [
    "Attached to an Alliance, Reseller or Referral Agreement.",
    "Wherever a margin, commission, or revenue/profit share must be defined precisely.",
    "Where tiered rates, caps or minimum commitments apply.",
  ],
  "blueprint": [
    ("Parent agreement reference", "The agreement this schedule attaches to and takes its defined terms from."),
    ("Economic model", "Margin/discount, commission, or revenue/profit share — state which."),
    ("Base amount", "Exactly what the share/commission is calculated on (e.g. net revenue excluding VAT, refunds)."),
    ("Rate(s) and tiers", "The percentage(s), any volume tiers, accelerators or caps."),
    ("Qualifying event", "What triggers entitlement (order signed, payment received, go-live)."),
    ("Exclusions and adjustments", "Refunds, cancellations, chargebacks, taxes, bad debt, churn clawbacks."),
    ("VAT and invoicing", "VAT treatment; who invoices whom and when."),
    ("Reporting and statements", "Cadence and content of statements; self-billing (if used)."),
    ("Reconciliation and disputes", "How discrepancies are raised and resolved."),
    ("Audit rights", "Right to inspect records supporting the calculation."),
    ("Minimum commitments", "Any minimums, and consequences of missing them (if applicable)."),
    ("Payment terms", "Payment days and method."),
  ],
  "inputs": [
    "The parent agreement and its defined terms.",
    "Economic model, base amount, rate(s)/tiers and qualifying event.",
    "Exclusions, VAT treatment, reporting cadence and audit rights.",
    "Any minimum commitments and payment terms.",
  ],
  "uk_notes": [
    "Define the base amount with no ambiguity (net of VAT, refunds and taxes) — most revenue-share disputes are about the base.",
    "Get the VAT treatment of commissions/revenue shares right; confirm who issues the VAT invoice (or whether self-billing is used).",
    "Avoid any term that fixes a reseller's resale price — set the share, not the customer price.",
  ],
  "best": [
    "Worked examples in the schedule prevent 90% of disputes.",
    "Tie clawbacks to refunds/churn so you never pay commission on money you repay.",
    "Keep reporting and audit rights concrete and time-bound.",
  ],
  "related": [6, 7, 3],
},
{
  "num": 9, "slug": "CO_MARKETING_AGREEMENT", "title": "Co-Marketing and Co-Branding Agreement",
  "short": "Governs joint marketing, PR, events and use of each other's brand, with approval rights and brand controls.",
  "binding": "Binding once signed; governs joint marketing activities and brand use.",
  "signatories": "Authorised signatory of each party.",
  "ai_level": "Fully AI-draftable from the campaign plan; human review of brand licence, approvals and cost split.",
  "purpose": [
    "A Co-Marketing (and Co-Branding) Agreement lets two companies market together — joint campaigns, content, webinars, events, press and case studies — and use each other's names and logos under a controlled licence, with approval rights, brand guidelines and a fair split of costs and leads.",
    "It protects both brands (quality control, approvals), clarifies who owns jointly created marketing materials and leads, and keeps claims accurate and compliant.",
  ],
  "when_use": [
    "Joint campaigns, events, webinars, content or PR with a partner.",
    "Where each party's brand/logo will appear on the other's materials.",
    "Where leads and marketing costs must be shared fairly.",
  ],
  "blueprint": [
    ("Parties and campaign scope", "The joint marketing activities and the period covered."),
    ("Brand and trade-mark licence", "Limited, revocable licence to use names/logos for the agreed activities only."),
    ("Brand guidelines and approvals", "Each party approves uses of its brand before publication; quality control."),
    ("Content ownership and licences", "Who owns jointly created materials; licences to reuse."),
    ("Messaging and claims", "Accurate, substantiated claims; compliance with advertising rules."),
    ("Leads and data", "How jointly generated leads are shared; UK GDPR basis and transparency (link to Data Sharing)."),
    ("Costs and contributions", "Cost split and each party's contributions."),
    ("Responsibilities and timeline", "Who delivers what, by when."),
    ("Confidentiality", "Pre-announcement confidentiality; embargoes."),
    ("Term and termination", "Duration; takedown of brand use on termination."),
    ("Relationship clause", "No partnership (legal sense) or authority to bind."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "The campaign/activities, period and each party's contributions.",
    "Brand-use rules and approval process.",
    "Lead-sharing and data-protection basis; cost split.",
    "Ownership of co-created content.",
  ],
  "uk_notes": [
    "Trade-mark use should be controlled (approval + quality control); uncontrolled licensing can harm the mark.",
    "Marketing claims must be accurate and substantiated (ASA/CAP Code); correct each other's misstatements.",
    "Lead lists are personal data — share only with a lawful basis and transparency under UK GDPR.",
  ],
  "best": [
    "Agree brand approval SLAs so campaigns are not blocked.",
    "Decide content ownership and reuse rights before producing assets.",
    "Require prompt takedown of brand use after the campaign ends.",
  ],
  "related": [3, 2, 11],
},
{
  "num": 10, "slug": "JOINT_VENTURE_AGREEMENT", "title": "Joint Venture Agreement",
  "short": "Establishes a joint venture — a shared entity or a contractual JV — with ownership, governance, funding and exit.",
  "binding": "Binding once signed; the constitutional agreement for the JV. Solicitor and tax advice required.",
  "signatories": "Authorised signatory of each venturer (and the JV entity, where incorporated).",
  "ai_level": "AI-draftable first draft only; SOLICITOR and TAX advice mandatory before signing.",
  "purpose": [
    "A Joint Venture (JV) Agreement sets up a deeper collaboration where the parties pool resources to pursue an opportunity together — either by forming a new jointly owned company (corporate JV) or by a purely contractual JV — governing ownership/shareholding, capital and funding, governance and board, IP contributions, profit share, deadlock and exit.",
    "Because a JV can create shared ownership, shared liabilities and significant tax and competition consequences, it is the heaviest partnership instrument and must be structured with professional advice.",
  ],
  "when_use": [
    "The parties will share ownership, risk and reward in a venture (not just collaborate).",
    "Forming a new jointly owned company, or a long-term contractual JV.",
    "Where capital contribution, profit share and governance of a shared venture are needed.",
  ],
  "blueprint": [
    ("Parties and JV structure", "Corporate (new company) or contractual JV; the venture's purpose and scope."),
    ("Ownership / shareholding", "Each party's stake; classes of shares; the new entity's details (if incorporated)."),
    ("Capital and funding", "Initial contributions; further funding; what happens if a party cannot fund."),
    ("Contributions in kind", "IP, technology, people, customers, brand each party contributes, and on what terms."),
    ("Governance and board", "Board composition, appointment rights, quorum, chair, meeting cadence."),
    ("Reserved matters", "Decisions needing special/unanimous approval (budgets, borrowing, new business, IP)."),
    ("Profit share and distributions", "How profits are shared and distributed."),
    ("Intellectual property", "Ownership/licensing of contributed and JV-created IP."),
    ("Competition-law compliance", "No unlawful coordination; information controls between the venturers."),
    ("Deadlock resolution", "Mechanism for resolving board/shareholder deadlock."),
    ("Transfer of interests", "Restrictions on share transfer; pre-emption; change of control."),
    ("Term and exit", "Duration; exit routes; buy-out (put/call); wind-up and asset distribution (link to Exit Deed)."),
    ("Warranties, liability and indemnities", "Between the venturers and to/from the JV."),
    ("Confidentiality and non-compete", "Protecting the venture; reasonable restrictive covenants."),
    ("Governing law and jurisdiction", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "JV purpose and structure (corporate vs contractual).",
    "Ownership split, capital contributions and funding plan.",
    "Governance, reserved matters and profit-share terms.",
    "IP contributions; exit, deadlock and transfer terms.",
  ],
  "uk_notes": [
    "A corporate JV also needs constitutional documents (articles, shareholders' agreement) and Companies House filings — this agreement should align with them.",
    "JVs can raise merger-control and competition-law issues; obtain competition advice, especially between competitors.",
    "Tax structuring (corporation tax, VAT, profit extraction) is material — obtain tax advice before signing.",
    "This is the highest-risk instrument here — do not sign without a solicitor.",
  ],
  "best": [
    "Decide deadlock and exit mechanics before signing, not after a dispute.",
    "Keep reserved matters tight so neither party is trapped by the other.",
    "Separate contributed Background IP from JV-created IP clearly.",
  ],
  "related": [3, 12, 13],
},
{
  "num": 11, "slug": "PARTNERSHIP_DATA_SHARING_AGREEMENT", "title": "Partnership Data Sharing Agreement",
  "short": "Governs controller-to-controller personal-data sharing between partners (leads, contacts, joint customers).",
  "binding": "Binding; the UK GDPR instrument for independent/joint controller sharing between partners.",
  "signatories": "Authorised signatory of each party (as controller).",
  "ai_level": "AI-draftable from a base; DPO/solicitor review recommended, especially for joint controllership.",
  "purpose": [
    "A Partnership Data Sharing Agreement governs the sharing of personal data between partners who each decide their own purposes for the data (controller-to-controller) — for example exchanging leads, contacts or joint-customer information in an alliance, reseller or referral relationship.",
    "It records the purpose and lawful basis for sharing, the data involved, security, data-subject rights, retention and liability, in line with the ICO Data Sharing Code. Where instead one partner processes data on the other's behalf, a Data Processing Agreement is the correct instrument.",
  ],
  "when_use": [
    "Partners exchange leads, contacts or customer data for their own purposes.",
    "Independent or joint controller relationships in a partnership.",
    "Any partnership personal-data sharing not covered by a processor DPA.",
  ],
  "blueprint": [
    ("Parties and roles", "Each party as controller; independent vs joint controllers."),
    ("Purpose of sharing", "Why data is shared and the lawful basis for each party (e.g. legitimate interests, consent)."),
    ("Data shared", "Categories of personal data and data subjects (e.g. lead contact details)."),
    ("Method and frequency", "How and how often data is shared; format and security in transit."),
    ("Transparency to data subjects", "How individuals are told their data is shared (privacy information)."),
    ("Security measures", "Protection in transit and at rest; access controls."),
    ("Data-subject rights", "How access/erasure/objection requests are handled across both parties."),
    ("Joint-controller arrangement", "Where joint controllers, the allocation of responsibilities and a contact point."),
    ("Retention and deletion", "How long each party keeps the data; deletion on exit."),
    ("International transfers", "Mechanism where data leaves the UK (IDTA / UK Addendum)."),
    ("Breach handling", "Notification timelines and cooperation."),
    ("Liability and indemnity", "Allocation between the controllers."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Purpose, lawful basis and data categories/subjects.",
    "Sharing method, frequency and security.",
    "Retention, transfers and breach-handling terms.",
    "Whether the parties are independent or joint controllers.",
  ],
  "uk_notes": [
    "Use this (not a processor DPA) when both parties determine their own purposes; follow the ICO Data Sharing Code.",
    "Confirm a lawful basis and transparency before any lead/contact data is shared — consent or legitimate interests, documented.",
    "For joint controllers, UK GDPR requires a clear allocation of responsibilities and a data-subject contact point.",
  ],
  "best": [
    "Be explicit about who is controller for what, and the lawful basis each relies on.",
    "Minimise shared data to what the partnership actually needs.",
    "Keep a record of the sharing decision and privacy information provided to individuals.",
  ],
  "related": [3, 7, 9],
  "refs": [
    ("Business Docs — Data Sharing Agreement skill", R_BIZ_DSA),
    ("Business Docs — Data Processing Agreement skill", R_BIZ_DPA),
  ],
},
{
  "num": 12, "slug": "PARTNERSHIP_GOVERNANCE_TOR", "title": "Partnership Governance and Joint Steering Committee Terms of Reference",
  "short": "Defines how an ongoing partnership is governed: the steering committee, representatives, decisions, KPIs, escalation and review.",
  "binding": "Governance schedule to the Alliance/JV Agreement; operational rather than heavily commercial.",
  "signatories": "Agreed by authorised representatives of each party (schedule to the parent agreement).",
  "ai_level": "Fully AI-draftable from the governance model; human review of decision thresholds and representatives.",
  "purpose": [
    "A Partnership Governance / Joint Steering Committee Terms of Reference sets out how an ongoing alliance or JV is run: who sits on the steering committee, how often it meets, what it decides, the KPIs it tracks, how issues escalate, and how the partnership is reviewed and changed.",
    "Good governance keeps a partnership active and accountable, prevents drift, and provides a structured way to resolve issues before they become disputes.",
  ],
  "when_use": [
    "Any ongoing alliance or JV that needs active management.",
    "As a schedule to the Strategic Partnership or Joint Venture Agreement.",
    "Where KPIs, decision rights and escalation must be defined.",
  ],
  "blueprint": [
    ("Purpose and scope", "What the governance body oversees."),
    ("Steering committee membership", "Named roles/representatives from each party and a chair."),
    ("Meeting cadence and quorum", "How often it meets, quorum and how meetings are called."),
    ("Decision-making and thresholds", "How decisions are made; matters needing joint or escalated approval."),
    ("KPIs and success metrics", "The measures tracked and the targets."),
    ("Reporting", "What is reported, by whom and when."),
    ("Issue management and escalation", "How operational issues are raised and escalated to leadership."),
    ("Change mechanism", "How the partnership scope/plan is changed without re-papering the whole agreement."),
    ("Review points", "Periodic health-check and renewal reviews."),
    ("Dispute escalation", "Escalation ladder before formal dispute resolution."),
    ("Records", "Minutes, decisions and action tracking."),
  ],
  "inputs": [
    "Parent agreement reference; committee representatives and chair.",
    "Meeting cadence, quorum and decision thresholds.",
    "KPIs/success metrics and reporting cadence.",
    "Escalation ladder and review points.",
  ],
  "uk_notes": [
    "Keep governance decisions within the authority each agreement grants — the committee should not be able to bind beyond its remit.",
    "For JVs, align decision thresholds with the reserved-matters list in the JV Agreement.",
    "Record decisions in minutes; they can matter if a dispute arises.",
  ],
  "best": [
    "Pick a few meaningful KPIs rather than many vanity metrics.",
    "Give the committee a clear change mechanism so the partnership can evolve.",
    "Define escalation so issues reach decision-makers quickly.",
  ],
  "related": [3, 10, 13],
},
{
  "num": 13, "slug": "PARTNERSHIP_EXIT_DEED", "title": "Partnership Exit / Disengagement Deed",
  "short": "Winds down a partnership in an orderly way: run-off, trailing economics, customer and data handover, and survival terms.",
  "binding": "Binding deed recording the agreed terms of exit and the parties' releases.",
  "signatories": "Authorised signatory of each party (executed as a deed where releases are given).",
  "ai_level": "AI-draftable from the exit plan; solicitor review for releases, run-off and liability.",
  "purpose": [
    "A Partnership Exit (or Disengagement) Deed records how a partnership ends cleanly — the effective exit date, run-off of existing deals and trailing commissions, transition of joint customers, return or deletion of data, treatment of jointly created IP and brand use, surviving obligations, and any mutual releases.",
    "It prevents a messy or disputed break-up by agreeing, in advance or at exit, exactly what each party keeps, owes and must do, protecting customers and both reputations.",
  ],
  "when_use": [
    "Ending an alliance, reseller, referral or JV relationship.",
    "On expiry, termination, or a change of strategy/control.",
    "Whenever customers, data, IP or trailing money must be disentangled.",
  ],
  "blueprint": [
    ("Parties and the ending agreement", "Identify the partnership agreement being wound down and the exit date."),
    ("Reason and effective date", "Basis for exit (expiry, termination, mutual) and when it takes effect."),
    ("Run-off of existing deals", "How in-flight deals/customers are completed or transferred."),
    ("Trailing economics", "Commissions/revenue share still payable, and for how long."),
    ("Customer transition", "How joint/channel customers are transitioned and communicated to."),
    ("Data return and deletion", "Return or secure deletion of personal and confidential data (subject to legal retention)."),
    ("Intellectual property and brand", "Ceasing brand/trade-mark use; treatment of jointly created IP; licence survival/termination."),
    ("Outstanding liabilities", "Settlement of amounts owed each way."),
    ("Surviving obligations", "Confidentiality, data protection, non-solicit and other terms that survive."),
    ("Mutual releases", "Where agreed, releases of claims (take legal advice)."),
    ("Announcements", "Agreed messaging about the end of the partnership."),
    ("Governing law", "England and Wales."),
    ("Execution as a deed", "Signatures/witnessing as required for a deed."),
  ],
  "inputs": [
    "The agreement being wound down and the exit date.",
    "Run-off, trailing-commission and customer-transition plan.",
    "Data return/deletion and IP/brand treatment.",
    "Any mutual releases and agreed announcements.",
  ],
  "uk_notes": [
    "Where the parties give mutual releases or other promises without consideration, execute as a deed (with correct witnessing).",
    "Honour transitional protection for live customers so they are not stranded on exit.",
    "Confirm data-return/deletion obligations are met and documented for UK GDPR accountability.",
  ],
  "best": [
    "Agree exit mechanics early (in the main agreement) so this deed is quick to produce.",
    "Protect customers first — a clean handover protects both reputations.",
    "Document that data and brand use have actually ceased.",
  ],
  "related": [3, 10, 12],
},
]

# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
DOC_BY_NUM = {d["num"]: d for d in DOCS}


def file_name(d: dict) -> str:
    return f"{d['num']:02d}_{d['slug']}_SKILL.md"


def pack_of(d: dict) -> str:
    return "Core" if d["num"] <= CORE_MAX else "Extended"


def bullets(items) -> str:
    return "\n".join(f"- {i}" for i in items)


def numbered_blueprint(items) -> str:
    return "\n".join(f"{n}. **{t}** — {g}" for n, (t, g) in enumerate(items, 1))


def related_links(d: dict) -> list[str]:
    out = []
    for n in d.get("related", []):
        r = DOC_BY_NUM.get(n)
        if r:
            out.append(f"- [{r['title']}]({file_name(r)})")
    return out


def render_skill(d: dict) -> str:
    tag_slug = d["slug"].lower().replace("_", "-")
    standards = d.get("standards", STANDARDS_DEFAULT)
    fm = [
        "---",
        f"id: PARTDOC-{d['num']:03d}",
        f"title: {d['title']} — Generation Skill",
        "document_type: Skill",
        "category: Partnership Documentation",
        "phase: Phase 05",
        "owner: Commercial and Partnerships Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "jurisdiction: England and Wales",
        "tags:",
        "  - skill",
        "  - partnership-documentation",
        f"  - {tag_slug}",
        "related_documents:",
        "  - ROOT_INDEX.md",
        "  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md",
        "  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md",
        f"  - 02_ARTEFACTS/PHASE_05_SKILLS/Partnership_Documentation/{FRAMEWORK_FILE}",
        "standards:",
    ]
    fm += [f"  - {s}" for s in standards]
    fm.append("---")

    purpose = "\n\n".join(d["purpose"])
    refs = d.get("refs")
    refs_block = ""
    if refs:
        refs_block = "\n## Official References\n\n" + "\n".join(
            f"- [{label}]({url})" for label, url in refs
        ) + "\n"

    related = related_links(d)
    related.append(f"- [UK Partnership Framework]({FRAMEWORK_FILE})")
    related.append(f"- [Mutual NDA (Business Docs)]({R_BIZ_NDA})")
    related.append(f"- [Data Processing Agreement (Business Docs)]({R_BIZ_DPA})")
    related.append(f"- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide]({R_GUIDE})")
    related.append(f"- [Partnership Documentation Index](README.md)")
    related.append(f"- [All Phase 05 Skills]({R_SKILLS})")
    related.append(f"- [AIBOS Root Specification]({R_SPEC})")
    related.append(f"- [Enterprise Glossary]({R_GLOSSARY})")

    body = f"""# {d['title']} — Generation Skill

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Skills]({R_SKILLS}) · [Partnership Docs](README.md) · [UK Framework]({FRAMEWORK_FILE}) · [Business Docs]({R_BIZ_INDEX})

## At a Glance

{d['short']}

| Field | Detail |
| --- | --- |
| Document | {d['title']} |
| Category | Partnership Documentation |
| Jurisdiction | England and Wales (UK) |
| Pack | {pack_of(d)} |
| Binding status | {d['binding']} |
| Typical signatories | {d['signatories']} |
| AI automation | {d['ai_level']} |

## Legal Notice

{LEGAL_NOTICE}

## Purpose

{purpose}

## When to Use

{bullets(d['when_use'])}

## Document Blueprint (Generation Template)

{GENERATE_INSTRUCTION}

{numbered_blueprint(d['blueprint'])}

## Inputs Required to Generate

{bullets(d['inputs'])}

## UK Legal and Compliance Notes

{bullets(d['uk_notes'])}

## Best Practices and Pitfalls

{bullets(d['best'])}

## Related Documents

{chr(10).join(related)}
{refs_block}
## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | Complete, generate-ready UK partnership-document skill. |
"""
    return "\n".join(fm) + "\n\n" + body


ARCH_DIAGRAM = """```text
Explore fit  ->  Mutual NDA (before disclosure)
   ->  Letter of Intent / Heads of Terms (non-binding intent, exclusivity)
   ->  Memorandum of Understanding (non-binding collaboration framework)
   ->  Due diligence & competition-law check
   ->  Binding agreement for the chosen model:
         - Strategic Partnership / Alliance Agreement (ongoing collaboration)
         - Teaming Agreement (one joint bid / opportunity)
         - Reseller / Channel Partner Agreement (partner resells your product)
         - Referral / Introducer Agreement (partner introduces leads)
         - Joint Venture Agreement (shared entity or contractual JV)
   ->  Supporting schedules: Revenue Share, Co-Marketing, Data Sharing,
       Partnership SOW (joint delivery), Governance / Steering Committee ToR
   ->  Operate & review  ->  Exit / Disengagement Deed (orderly wind-down)
```"""


def render_framework() -> str:
    core = [d for d in DOCS if d["num"] <= CORE_MAX]
    extended = [d for d in DOCS if d["num"] > CORE_MAX]

    def rows(docs):
        return "\n".join(
            f"| {d['num']:02d} | [{d['title']}]({file_name(d)}) | {d['short']} |"
            for d in docs
        )

    fm = [
        "---",
        "id: PARTDOC-000",
        "title: UK Partnership Framework (Reference)",
        "document_type: Reference",
        "category: Partnership Documentation",
        "phase: Phase 05",
        "owner: Commercial and Partnerships Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "jurisdiction: England and Wales",
        "tags:",
        "  - partnership-documentation",
        "  - partnerships",
        "  - reference",
        "related_documents:",
        "  - ROOT_INDEX.md",
        "  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md",
        "---",
    ]

    body = f"""# UK Partnership Framework (Reference)

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Skills]({R_SKILLS}) · [Partnership Docs](README.md) · [Business Docs]({R_BIZ_INDEX}) · [Source Guide]({R_GUIDE})

## Legal Notice

{LEGAL_NOTICE}

## Overview

This is the shared reference for the AIBOS Partnership Documentation skills. It
captures the recommended document architecture, the choice between binding and
non-binding instruments, and the drafting principles for United Kingdom (England
and Wales) business-to-business **partnerships, alliances, reseller/referral
channels and joint ventures**. It complements the sibling
[UK Contracting Framework]({R_BIZ_FRAMEWORK}) (client delivery) and reuses its
[Mutual NDA]({R_BIZ_NDA}), [Data Processing Agreement]({R_BIZ_DPA}) and
[Data Sharing Agreement]({R_BIZ_DSA}) rather than duplicating them. Each skill in
this folder generates one document consistent with this framework.

## Partnership Lifecycle Architecture

{ARCH_DIAGRAM}

## Core Pack (Formation)

| # | Document | Purpose |
| --- | --- | --- |
{rows(core)}

## Extended Pack (Models, Operation and Exit)

| # | Document | Purpose |
| --- | --- | --- |
{rows(extended)}

## Binding vs Non-Binding — Get This Right First

- A **Letter of Intent / Heads of Terms** and a **Memorandum of Understanding** are
  normally **non-binding** as to the commercial deal, **except** for specific clauses
  that are intended to bind — typically **confidentiality, exclusivity, costs and
  governing law**. State expressly which clauses bind and which do not.
- A document can bind even if called "MOU" if its terms are sufficiently certain and
  the parties act on it. If you do not intend to be bound yet, mark it clearly and
  avoid definite language ("shall deliver", fixed prices, firm dates).
- The **Strategic Partnership / Alliance, Teaming, Reseller, Referral and Joint
  Venture** agreements are **binding** once signed.

## "No Legal Partnership" — Avoid Unintended Liability

- Under the **Partnership Act 1890**, two businesses "carrying on a business in common
  with a view of profit" can be treated as a **legal partnership**, creating **joint
  and several liability** for each other's debts — usually the opposite of what a
  commercial "partnership" intends.
- Every alliance, co-marketing, teaming and reseller agreement should include a
  **relationship clause** stating that nothing creates a partnership (in the legal
  sense), agency, employment or fiduciary relationship, and that **neither party may
  bind the other**.
- Use the word "partner" with care in public-facing materials; it can imply authority
  to bind. Prefer "alliance partner", "channel partner" or "referral partner" with the
  no-agency clause in support.

## Competition-Law Health Check

Collaborations between independent businesses can breach the **Chapter I prohibition
(Competition Act 1998)** and must be reviewed where they involve:

- **Price fixing**, coordinating discounts, or agreeing resale prices (resale price
  maintenance is generally unlawful — a reseller sets its own resale prices).
- **Market, customer or territory sharing**, or output limitation.
- **Exclusivity** that forecloses competitors, or **wide "most-favoured" clauses**.
- **Commercially sensitive information sharing** (pricing, costs, pipeline, strategy) —
  limit to what the collaboration needs, and use "clean team"/need-to-know controls.

When in doubt, obtain competition-law advice before signing; penalties are severe.

## Intellectual Property Principles

- Each party keeps its **Background IP**; the agreement grants only the **limited
  licences** the collaboration needs (e.g. to use logos for co-marketing, or to
  demonstrate/resell the product).
- Decide ownership of **Foreground / jointly created IP** explicitly — joint ownership
  of UK IP is often impractical (each co-owner needs consent to licence); usually it is
  cleaner for one party to own and licence back.
- Brand and trade-mark use must be controlled with **brand guidelines, approval rights
  and quality control**; uncontrolled trade-mark licensing can weaken the mark.
- Any assignment of UK copyright must be **in writing and signed**.

## Revenue, Commercials and Tax

- Define the **revenue model** precisely: margin/discount (reseller), commission
  (referral), revenue/profit share (alliance/JV) — with the **base amount, rate,
  qualifying events, exclusions (refunds, taxes, chargebacks), payment timing, reporting
  and audit rights**.
- Clarify **VAT** treatment of commissions and revenue shares, and who invoices whom.
- **Referral/introducer** arrangements may, in some circumstances, engage the
  **Commercial Agents (Council Directive) Regulations 1993** (compensation on
  termination) — check whether the partner is a mere introducer or a true agent.
- **Anti-bribery:** referral and reseller commissions are a classic **Bribery Act 2010**
  risk — include ABC warranties, no facilitation payments, and audit/termination rights.

## Data Sharing Between Partners

- Where partners share **personal data**, decide the UK GDPR roles: a controller-to-
  controller [Data Sharing Agreement]({R_BIZ_DSA}) for independent/joint controllers,
  or a [Data Processing Agreement]({R_BIZ_DPA}) where one party processes on the other's
  behalf. Follow the **ICO Data Sharing Code**.
- Lead-passing in referral deals is personal-data sharing — confirm lawful basis
  (often legitimate interests or consent) and transparency before sharing contacts.

## Governance

- For ongoing alliances and JVs, establish a **Joint Steering Committee** with named
  representatives, cadence, decision thresholds, escalation and deadlock resolution.
- Define **KPIs/success metrics**, review points, and a change mechanism so the
  partnership can evolve without a full re-paper.

## Exit and Termination

- Provide for **term, renewal, termination for cause/convenience/insolvency and change
  of control**, plus an **orderly wind-down**: run-off of existing deals, treatment of
  the pipeline and trailing commissions, licence survival, customer and data handover,
  and confidentiality survival.
- Address **transitional protection** for live customers so neither party's customers
  are stranded on exit.

## Internal Approval (Director Sign-off) Triggers

Exclusivity; minimum-commitment or volume guarantees; equity or a new JV entity;
revenue/profit share above a threshold; competition-sensitive terms; IP assignment or
wide licences of Background IP; brand/trade-mark licensing; cross-border partners or
foreign governing law; uncapped or unusual liability/indemnities; sub-licensing rights;
special-category personal data sharing; non-compete or non-solicit covenants.

## Practical Operating Rules

1. Sign a Mutual NDA before exchanging confidential information.
2. Use a non-binding LOI/MOU to align intent before investing in a full agreement.
3. Never let "partner" language create an unintended legal partnership or agency.
4. Run a competition-law check on exclusivity, pricing and information-sharing terms.
5. Keep each party's Background IP separate; licence only what is needed.
6. Put the full economics (base, rate, exclusions, reporting, audit) in a schedule.
7. Share personal data only under the correct UK GDPR instrument.
8. Agree governance, KPIs and a deadlock mechanism for ongoing partnerships.
9. Agree exit, run-off and customer/data handover before go-live, not after.
10. Use a solicitor for exclusive, equity, cross-border or competition-sensitive deals.

## Official References

- [GOV.UK — Partnership Act 1890](https://www.legislation.gov.uk/ukpga/Vict/53-54/39/contents)
- [CMA — Competing fairly: advice for businesses](https://www.gov.uk/government/collections/competing-fairly-in-business)
- [ICO — Data sharing: a code of practice](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/data-sharing-a-code-of-practice/)
- [GOV.UK — Bribery Act 2010 guidance](https://www.gov.uk/government/publications/bribery-act-2010-guidance)
- [UK IPO — Ownership of copyright works](https://www.gov.uk/guidance/ownership-of-copyright-works)
- [GOV.UK — Electronic execution of documents](https://www.gov.uk/government/publications/electronic-execution-of-documents)

## Related Resources

- [Partnership Documentation Index](README.md)
- [UK Contracting Framework (client delivery)]({R_BIZ_FRAMEWORK})
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide]({R_GUIDE})
- [All Phase 05 Skills]({R_SKILLS})
- [AIBOS Root Specification]({R_SPEC})

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | UK partnership framework reference for the Partnership Documentation skills. |
"""
    return "\n".join(fm) + "\n\n" + body


def render_readme() -> str:
    core = [d for d in DOCS if d["num"] <= CORE_MAX]
    extended = [d for d in DOCS if d["num"] > CORE_MAX]

    def rows(docs):
        return "\n".join(
            f"| {d['num']:02d} | [{d['title']}]({file_name(d)}) | {d['binding'].split('.')[0]}. |"
            for d in docs
        )

    fm = [
        "---",
        "id: PARTDOC-INDEX",
        "title: Partnership Documentation Skills — Index",
        "document_type: Index",
        "category: Partnership Documentation",
        "phase: Phase 05",
        "owner: Commercial and Partnerships Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "jurisdiction: England and Wales",
        "tags:",
        "  - partnership-documentation",
        "  - skills",
        "  - index",
        "---",
    ]

    body = f"""# Partnership Documentation Skills — Index

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Phase 05 Skills]({R_SKILLS}) · [UK Framework]({FRAMEWORK_FILE}) · [Business Docs]({R_BIZ_INDEX})

## Overview

This skill set turns AIBOS into a UK-compliant **partnership-document generator** for
company-to-company collaborations: strategic alliances, teaming/joint bids, reseller
and referral channels, co-marketing, joint ventures and joint delivery. Each skill is
**generate-ready**: reference it and an AI agent (or a person) can produce the
corresponding document, using an embedded blueprint aligned to the
[UK Partnership Framework]({FRAMEWORK_FILE}).

Jurisdiction is **England and Wales**. Lemuran Ltd is used as the default example
party; skills use reusable Party A / Party B (or Supplier / Partner) placeholders.
This set complements, and cross-references, the client-delivery
[Business Documentation]({R_BIZ_INDEX}) set (NDA, DPA, Data Sharing, SOW).

## Legal Notice

{LEGAL_NOTICE}

## How to Use These Skills

- **Generate a document:** reference the relevant skill (e.g. "use the Memorandum of Understanding skill" or "use the Reseller Agreement skill") and provide the *Inputs Required*; the skill's blueprint drives the draft.
- **Sequence a partnership:** follow the lifecycle in the [UK Partnership Framework]({FRAMEWORK_FILE}) — NDA → LOI/MOU → due diligence → binding agreement → schedules → governance → exit.
- **Stay compliant:** each skill embeds UK legal notes (competition law, "no legal partnership", IP, data sharing, anti-bribery) and a solicitor-review reminder for high-risk deals.

## Core Pack (Formation)

| # | Document | Binding status |
| --- | --- | --- |
{rows(core)}

## Extended Pack (Models, Operation and Exit)

| # | Document | Binding status |
| --- | --- | --- |
{rows(extended)}

## Foundational Reference

- [UK Partnership Framework]({FRAMEWORK_FILE}) — lifecycle, binding vs non-binding, competition law, "no legal partnership", IP, revenue/tax, data sharing, governance, exit, official references.

## Which Document When

- **Before disclosure:** [Mutual NDA]({R_BIZ_NDA}) (from Business Docs).
- **To align intent (non-binding):** Letter of Intent / Heads of Terms, then Memorandum of Understanding.
- **For an ongoing alliance:** Strategic Partnership / Alliance Agreement (+ Governance ToR).
- **To bid for one opportunity together:** Teaming Agreement.
- **To deliver a joint engagement:** Partnership Statement of Work.
- **Partner resells your product/SaaS:** Reseller / Channel Partner Agreement (+ Revenue Share Schedule).
- **Partner introduces leads:** Referral / Introducer Agreement (+ Revenue Share Schedule).
- **Joint go-to-market/brand:** Co-Marketing and Co-Branding Agreement.
- **Shared venture/entity:** Joint Venture Agreement.
- **Sharing personal data:** Partnership Data Sharing Agreement (or the Business Docs DPA where one party processes for the other).
- **To run it:** Partnership Governance and Joint Steering Committee Terms of Reference.
- **To end it cleanly:** Partnership Exit / Disengagement Deed.

## Related Resources

- [UK Contracting Framework (client delivery)]({R_BIZ_FRAMEWORK})
- [Business Documentation Index]({R_BIZ_INDEX})
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide]({R_GUIDE})
- [All Phase 05 Skills]({R_SKILLS})
- [Enterprise Rules]({R_RULES})
- [Enterprise Templates]({R_TEMPLATES})
- [AIBOS Root Specification]({R_SPEC})
- [Enterprise Glossary]({R_GLOSSARY})

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | Initial Partnership Documentation skill set: 13 generate-ready UK documents + framework. |
"""
    return "\n".join(fm) + "\n\n" + body


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    written = []

    fw = OUT / FRAMEWORK_FILE
    fw.write_text(render_framework(), encoding="utf-8")
    written.append(fw)

    for d in DOCS:
        p = OUT / file_name(d)
        p.write_text(render_skill(d), encoding="utf-8")
        written.append(p)

    readme = OUT / "README.md"
    readme.write_text(render_readme(), encoding="utf-8")
    written.append(readme)

    print(f"Generated {len(written)} files in {OUT.relative_to(REPO)}:")
    for p in written:
        print(f"  - {p.name}")


if __name__ == "__main__":
    main()
