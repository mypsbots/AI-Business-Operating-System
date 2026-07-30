#!/usr/bin/env python3
"""Generate the Business Documentation skill set for AIBOS Phase 05.

Creates 02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/ with:
  * 00_UK_CONTRACTING_FRAMEWORK.md      — shared reference: architecture, hierarchy,
                                          signing order, minimum-clause checklist,
                                          due diligence, IP/payment/liability
                                          principles, official references.
  * NN_<DOC>_SKILL.md                   — one generate-ready skill per business document.
  * README.md                           — the Business Documentation index.

Each skill embeds a full, UK (England & Wales) blueprint so that when the skill is
referenced, an AI agent (or a person) can produce the actual document. Content is
based on the Lemuran Ltd — UK Client Project Engagement Legal & Contracting Guide
(00_ROOT/) and standard UK best practice (UK GDPR / ICO, PECR, IPO, late-payment
statute, electronic-execution guidance).

These are practical drafting aids, NOT legal advice. High-value, regulated,
international, security-sensitive or complex engagements must be reviewed by a
UK-qualified solicitor before signing.

Re-run any time; it overwrites only files inside the Business_Documentation/ folder.
"""

from __future__ import annotations

import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parents[1]
OUT = REPO / "02_ARTEFACTS" / "PHASE_05_SKILLS" / "Business_Documentation"
CREATED = "2026-07-30"
FRAMEWORK_FILE = "00_UK_CONTRACTING_FRAMEWORK.md"

# Relative paths from a skill file inside Business_Documentation/.
R_HOME = "../../../README.md"
R_INDEX = "../../../ROOT_INDEX.md"
R_PROMPT = "../../../01_PHASES/PHASE_05_SKILLS_MASTER_PROMPT.md"
R_SPEC = "../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md"
R_GLOSSARY = "../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md"
R_SKILLS = "../README.md"
R_GUIDE = "../../../00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md"
R_RULES = "../../PHASE_06_RULES/README.md"
R_TEMPLATES = "../../PHASE_09_TEMPLATES/README.md"

STANDARDS_DEFAULT = [
    "UK GDPR",
    "Data Protection Act 2018",
    "ISO 27001",
    "ISO 42001",
    "SOC 2",
]

LEGAL_NOTICE = (
    "> **Legal notice.** This skill produces a **draft** business document to speed up "
    "preparation. It is **not legal advice** and is **not a substitute for review by a "
    "UK-qualified solicitor**. For high-value, regulated, international, security-sensitive "
    "or complex engagements, obtain solicitor sign-off before signing. Unless otherwise "
    "agreed, the governing law is **England and Wales**. Do not store passwords, API keys "
    "or production credentials in generated documents."
)

GENERATE_INSTRUCTION = (
    "When this skill is invoked, generate the document by expanding each blueprint "
    "section below into clear, formal UK business English, filling every placeholder "
    "from the *Inputs Required*, resolving or flagging any missing input, marking the "
    "output as a draft, and appending a dated signature block for the authorised "
    "signatories. Keep numbering and the order of precedence consistent with the "
    "[UK Contracting Framework](" + FRAMEWORK_FILE + ")."
)

DOCS = [
{
  "num": 1, "slug": "MUTUAL_NDA", "title": "Mutual Non-Disclosure Agreement",
  "short": "Protects confidential information both parties share before the commercial contract is signed.",
  "binding": "Binding once signed by both parties.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "Fully AI-draftable from Inputs; human review before signing (solicitor review for high-sensitivity data).",
  "purpose": [
    "A Mutual NDA lets the Supplier (e.g. Lemuran Ltd) and a prospective customer exchange confidential information safely during discovery, scoping and due diligence, before any Master Services Agreement or Statement of Work is in place.",
    "It protects secrecy only; it does not authorise any work or transfer any intellectual property, and it is not a substitute for the main services contract.",
  ],
  "when_use": [
    "Discussing a customer's internal processes, systems or roadmap.",
    "Reviewing source code, credentials, datasets, financial information, customer records or architecture.",
    "Presenting the Supplier's confidential methods, reusable assets, pricing logic or product roadmap.",
    "Engaging a subcontractor or implementation partner who will see confidential information.",
  ],
  "blueprint": [
    ("Parties", "Full legal names, company numbers and registered addresses of both parties; effective date."),
    ("Purpose / permitted use", "The specific purpose for which information is shared; use limited strictly to that purpose."),
    ("Definition of Confidential Information", "Broad definition covering written, oral, visual and electronic information, and information about the discussions themselves."),
    ("Exclusions", "Information that is public, already known, independently developed, or lawfully received from a third party."),
    ("Persons permitted to receive", "Named roles / affiliates / advisers on a need-to-know basis, bound by equivalent obligations."),
    ("Security obligations", "Reasonable technical and organisational measures to protect the information."),
    ("Legally required disclosure", "Carve-out allowing disclosure required by law/regulator, with notice where lawful."),
    ("No IP transfer / no licence", "Nothing transfers ownership or grants any licence beyond the stated purpose."),
    ("Return or deletion", "On request or termination, return or securely delete confidential information (subject to legal retention)."),
    ("Duration of confidentiality", "Confidentiality survives for a stated period after termination (e.g. 3–5 years; trade secrets indefinitely)."),
    ("Remedies for breach", "Acknowledgement that damages may be inadequate and injunctive relief may be sought."),
    ("General / boilerplate", "No partnership, entire agreement, variation in writing, no waiver, severability, counterparts."),
    ("Governing law and jurisdiction", "England and Wales; courts of England and Wales have exclusive jurisdiction."),
    ("Signature block", "Name, title, signature and date for each authorised signatory."),
  ],
  "inputs": [
    "Supplier and Customer legal names, company numbers, registered addresses.",
    "Effective date and the specific purpose of disclosure.",
    "Confidentiality duration (default 3 years; longer for trade secrets).",
    "Named recipients / affiliates / advisers permitted to receive information.",
  ],
  "uk_notes": [
    "Mutual (two-way) form is standard when both sides disclose; use a one-way NDA only if disclosure is genuinely one-directional.",
    "Do not over-claim — a court will not protect genuinely public information.",
    "An NDA does not replace data-protection terms; if personal data is shared to be processed, a DPA is also required.",
  ],
  "best": [
    "Sign the NDA before detailed disclosure, not after.",
    "Keep the permitted purpose narrow and specific.",
    "Avoid perpetual blanket confidentiality except for genuine trade secrets.",
  ],
  "related": [4, 6, 21],
},
{
  "num": 2, "slug": "PROPOSAL", "title": "Proposal",
  "short": "Explains the recommended solution and the commercial offer to the customer.",
  "binding": "Not binding when marked \u201csubject to contract\u201d; can become binding if definite and accepted, or if incorporated into the signed Agreement.",
  "signatories": "Issued by the Supplier; customer acceptance recorded via signature or the signed Agreement.",
  "ai_level": "Fully AI-draftable from Inputs and discovery notes; human review of scope, price and assumptions before issue.",
  "purpose": [
    "A Proposal sets out what the Supplier recommends and the commercial terms of the offer, converting discovery into a clear solution, scope and price the customer can accept.",
    "It must be marked to control its legal status: 'Subject to contract' when not intended to bind, or 'Accepted as part of the Agreement' when it will form part of the signed contract.",
  ],
  "when_use": [
    "After a discovery call, to present a recommended solution and price.",
    "When the customer needs assumptions, exclusions and dependencies stated before committing.",
    "As the commercial narrative that the MSA and SOW then formalise.",
  ],
  "blueprint": [
    ("Title and status marking", "Clearly mark 'Subject to contract' or 'Accepted as part of the Agreement'; add version and date."),
    ("Customer problem and desired outcome", "The problem to solve and the outcome the customer wants."),
    ("Proposed solution", "The recommended approach, technology and how it meets the outcome."),
    ("Scope summary", "What is included, at a high level."),
    ("Deliverables", "Tangible outputs the customer will receive."),
    ("Assumptions", "The basis of the estimate; changes to assumptions may change price/timeline."),
    ("Exclusions", "What is explicitly not included."),
    ("Expected timeline", "Indicative phases and duration, subject to a signed SOW."),
    ("Fees and VAT position", "Fees, whether VAT applies, and expenses treatment."),
    ("Payment schedule", "Deposit, milestones and final balance."),
    ("Customer dependencies", "What the customer must provide (access, data, decisions)."),
    ("Optional services", "Add-ons the customer may select."),
    ("Validity period", "How long the offer stands (e.g. 30 days)."),
    ("Reference to contract terms", "Link/reference to the MSA/SOW that will govern the work."),
    ("Commencement statement", "Work begins only when the Agreement is signed and any required deposit is paid."),
  ],
  "inputs": [
    "Discovery findings: problem, outcome, constraints.",
    "Recommended solution, scope, deliverables, assumptions, exclusions.",
    "Fees, VAT position, payment schedule, validity period.",
    "Customer dependencies and any optional services.",
  ],
  "uk_notes": [
    "A proposal with sufficiently definite terms can form a binding contract if accepted — always mark its status.",
    "Keep assumptions and exclusions explicit to control scope and price.",
  ],
  "best": [
    "Always state a validity period and the 'work starts on signature + deposit' rule.",
    "Mirror the Proposal's scope into the SOW to avoid inconsistency.",
    "Reference (do not contradict) the MSA terms.",
  ],
  "related": [3, 4, 5],
},
{
  "num": 3, "slug": "QUOTATION", "title": "Quotation",
  "short": "A concise priced offer for a defined, lower-complexity piece of work.",
  "binding": "An offer that can become binding on acceptance within its validity period; mark status clearly.",
  "signatories": "Issued by the Supplier; accepted by the Customer in writing.",
  "ai_level": "Fully AI-draftable from a price basis; human check of pricing and VAT before issue.",
  "purpose": [
    "A Quotation is a short, priced offer for a clearly defined scope, used where a full Proposal is unnecessary. It states the price, what it covers, and how long it is valid.",
    "Like a Proposal, it can bind on acceptance, so its status and validity must be explicit.",
  ],
  "when_use": [
    "Small or well-defined work where a full Proposal is not needed.",
    "Responding quickly to a customer request for price.",
    "Fixed, catalogue-style services with known pricing.",
  ],
  "blueprint": [
    ("Quotation reference and date", "Unique quote number and issue date."),
    ("Supplier and Customer details", "Legal names and contacts."),
    ("Scope of the quoted work", "Precisely what is included."),
    ("Exclusions and assumptions", "What is not included; the basis of the price."),
    ("Price and VAT", "Net price, VAT position, total."),
    ("Payment terms", "Deposit and payment days."),
    ("Validity period", "How long the quoted price stands (e.g. 14–30 days)."),
    ("Acceptance mechanism", "How the customer accepts (signature / PO / written confirmation)."),
    ("Reference to governing terms", "The T&Cs / MSA that apply on acceptance."),
    ("Status marking", "'Subject to contract' unless intended to bind on acceptance."),
  ],
  "inputs": [
    "Defined scope and exclusions.",
    "Price basis, VAT position, payment terms, validity period.",
    "Governing terms reference and acceptance method.",
  ],
  "uk_notes": [
    "A quotation is generally treated as an offer capable of acceptance — keep scope tight and validity explicit.",
    "State which terms govern once accepted, to avoid a 'battle of the forms' with a customer PO.",
  ],
  "best": [
    "Use for defined work only; use a Proposal for anything with material assumptions.",
    "Always include a validity period and governing terms.",
  ],
  "related": [2, 26, 9],
},
{
  "num": 4, "slug": "MASTER_SERVICES_AGREEMENT", "title": "Master Services Agreement",
  "short": "The umbrella legal and commercial terms governing the whole customer relationship; individual projects run under separate SOWs.",
  "binding": "Binding once signed; governs all SOWs executed under it.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "AI-draftable from a firm-approved base; SOLICITOR review required before first use and for non-standard terms.",
  "purpose": [
    "The Master Services Agreement (MSA) contains the legal and commercial rules that apply across the entire customer relationship. It is signed once; each project is then documented via its own Statement of Work that incorporates the MSA.",
    "This separation lets the Supplier reuse stable legal terms while tailoring scope, price and risk per project in the SOW.",
  ],
  "when_use": [
    "Any ongoing or multi-project B2B relationship.",
    "Where the Supplier wants stable terms with per-project SOWs.",
    "As the backbone of the recommended MSA + SOW + DPA + SLA stack.",
  ],
  "blueprint": [
    ("1. Parties and company details", "Full legal names, company numbers, registered offices."),
    ("2. Definitions and interpretation", "Defined terms used throughout."),
    ("3. Contract structure and document priority", "How MSA, SOW, DPA, SLA and Change Requests fit together and the order of precedence."),
    ("4. Services and standard of performance", "Reasonable skill and care; conformance to the SOW."),
    ("5. Customer responsibilities and dependencies", "Access, data, decisions, approvals the customer must provide."),
    ("6. Project governance and authorised contacts", "Named contacts, escalation, meetings."),
    ("7. Fees, expenses, invoicing, taxes and payment", "Charging basis, invoicing cadence, VAT, payment days."),
    ("8. Late payment", "Interest and remedies for overdue amounts (see UK notes)."),
    ("9. Changes and Change Requests", "No changed work without an approved Change Request."),
    ("10. Intellectual property", "Ownership of deliverables vs Background IP; assignment on payment."),
    ("11. Licensing of pre-existing materials", "Licence for Supplier Background IP embedded in deliverables."),
    ("12. Open-source software", "Disclosure and licence compliance for OSS components."),
    ("13. AI and third-party technology", "Model/provider dependencies and limitations (see AI Schedule)."),
    ("14. Confidentiality", "Mutual confidentiality obligations."),
    ("15. Data protection", "UK GDPR roles; DPA applies where personal data is processed."),
    ("16. Information security", "Security obligations; Security Schedule where applicable."),
    ("17. Warranties", "Skill and care; qualified personnel; authority; AI-specific limitations."),
    ("18. Indemnities", "Carefully scoped indemnities (e.g. third-party IP, customer content)."),
    ("19. Limitation of liability", "Caps and excluded losses; non-excludable liabilities preserved."),
    ("20. Insurance", "Levels of cover the Supplier maintains, aligned to liability caps."),
    ("21. Subcontractors", "Right to subcontract; Supplier remains responsible."),
    ("22. Non-solicitation", "Reasonable, time-limited, where justified."),
    ("23. Compliance with laws", "Both parties comply with applicable law."),
    ("24. Anti-bribery and sanctions", "ABC and sanctions compliance."),
    ("25. Publicity and use of customer name", "Consent required to name the customer."),
    ("26. Suspension rights", "Suspend on non-payment or risk, after notice and cure."),
    ("27. Term and termination", "Duration; termination for cause / convenience / insolvency."),
    ("28. Consequences of termination", "Payment for work done; licence effects; survival."),
    ("29. Exit assistance and data return", "Handover, data return/deletion at exit."),
    ("30. Force majeure", "Relief for events beyond reasonable control."),
    ("31. Dispute escalation", "Escalation and, optionally, mediation before litigation."),
    ("32. Notices", "How formal notices are given."),
    ("33. Assignment", "Restrictions on assignment/novation."),
    ("34. Third-party rights", "Whether the Contracts (Rights of Third Parties) Act is excluded."),
    ("35. Entire agreement", "Supersedes prior discussions (with fraud carve-out)."),
    ("36. Variation", "Changes only in writing and signed."),
    ("37. Waiver and severability", "Standard boilerplate."),
    ("38. Electronic signatures and counterparts", "E-signature and counterpart execution permitted."),
    ("39. Governing law and jurisdiction", "England and Wales; exclusive jurisdiction of its courts."),
    ("Signature block", "Authorised signatories, titles, dates."),
  ],
  "inputs": [
    "Supplier and Customer legal details and authorised signatories.",
    "Firm-standard positions: liability cap basis, IP model, payment days, insurance levels.",
    "Any negotiated deviations (flag for solicitor review).",
  ],
  "uk_notes": [
    "Recommended governing law: the laws of England and Wales, with exclusive jurisdiction of the courts of England and Wales.",
    "Do not exclude non-excludable liabilities (death/personal injury from negligence, fraud, or others that cannot be limited by law).",
    "International customers may request arbitration/foreign law — obtain legal advice before agreeing.",
    "The MSA must expressly state the order of precedence with SOW/DPA/SLA/Change Requests.",
  ],
  "best": [
    "Keep the MSA stable; put project specifics in the SOW.",
    "Align the liability cap to available insurance.",
    "Have a UK commercial solicitor produce/review the first reusable MSA.",
  ],
  "related": [5, 6, 10, 11, 12, 26],
},
{
  "num": 5, "slug": "STATEMENT_OF_WORK", "title": "Statement of Work",
  "short": "Defines exactly what will be delivered for one project, with acceptance criteria and payment milestones, under the MSA.",
  "binding": "Binding once signed; incorporates and takes precedence over the MSA on project-specific matters.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "Fully AI-draftable from scope inputs; human review of acceptance criteria, fees and dependencies.",
  "purpose": [
    "The Statement of Work (SOW) describes a single project in precise, measurable terms: scope, deliverables, timeline, price, dependencies and acceptance. It is the document that most often prevents disputes.",
    "It sits under the MSA and should define objective acceptance criteria rather than vague quality statements.",
  ],
  "when_use": [
    "Every discrete project delivered under an MSA.",
    "Whenever deliverables, milestones and acceptance need to be fixed.",
  ],
  "blueprint": [
    ("SOW reference and effective date", "Unique SOW number; effective date; related MSA reference."),
    ("Background and objectives", "Why the project exists and the outcomes sought."),
    ("Detailed scope", "Exactly what is in scope."),
    ("Excluded items", "Explicitly out of scope."),
    ("Deliverables", "Each tangible output and its format."),
    ("Milestones and project plan", "Phased plan with dates and owners."),
    ("Customer dependencies and materials", "What the customer provides and by when."),
    ("Delivery method and location", "On-site/remote; environments."),
    ("Personnel and roles", "Key roles on both sides."),
    ("Assumptions", "The basis of estimates."),
    ("Fees, expenses and payment milestones", "Charges tied to milestones; expenses treatment."),
    ("Acceptance criteria", "Objective, measurable criteria per deliverable."),
    ("Testing process and acceptance period", "How acceptance is tested and the review window."),
    ("Deemed acceptance rule", "Acceptance is deemed if no defects raised within the period."),
    ("Support or warranty period", "Post-acceptance warranty/support."),
    ("Intellectual-property treatment", "Ownership/licence for this project's deliverables."),
    ("Data-processing details", "Whether personal data is processed (trigger DPA schedule)."),
    ("Special security requirements", "Any project-specific security (trigger Security Schedule)."),
    ("Signatories", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Related MSA reference; SOW number; dates.",
    "Scope, exclusions, deliverables, milestones, dependencies.",
    "Fees and payment milestones; acceptance criteria and testing.",
    "IP treatment; data-processing and security flags.",
  ],
  "uk_notes": [
    "Replace vague phrases like 'the system will work well' with measurable criteria (e.g. 'processes the approved test file and creates the specified output fields with no Severity 1 defects').",
    "For AI work, define performance metrics here rather than assuming them.",
  ],
  "best": [
    "Make acceptance criteria objective and testable.",
    "Tie payments to milestones and acceptance.",
    "Flag DPA/Security/AI schedules when triggered.",
  ],
  "related": [4, 6, 11, 12, 8],
},
{
  "num": 6, "slug": "DATA_PROCESSING_AGREEMENT", "title": "Data Processing Agreement",
  "short": "The UK GDPR-mandated controller\u2013processor contract used where the Supplier processes personal data on the customer's behalf.",
  "binding": "Binding; legally required where the Supplier acts as processor. Takes precedence on data-protection matters.",
  "signatories": "Authorised signatory of the Supplier (processor) and Customer (controller).",
  "ai_level": "AI-draftable from a compliant base + Inputs; DPO/solicitor review for special-category data or international transfers.",
  "purpose": [
    "A Data Processing Agreement (DPA) is required by UK GDPR Article 28 wherever the Supplier processes personal data on behalf of the customer as a processor. It sets the mandatory controller\u2013processor terms and records the processing details.",
    "Where both parties independently decide why and how personal data is used, a processor DPA is the wrong instrument and a Data Sharing Agreement should be used instead.",
  ],
  "when_use": [
    "The customer shares employee or customer records for the Supplier to process.",
    "The Supplier builds/operates an AI system using personal data, or hosts customer data.",
    "The Supplier accesses a CRM, email, help desk, HR or analytics system containing personal data.",
    "Support work provides access to identifiable user information.",
  ],
  "blueprint": [
    ("Parties and roles", "Identify controller and processor and the governing agreement."),
    ("Processing only on documented instructions", "Processor acts only on the controller's documented instructions."),
    ("Confidentiality of personnel", "Persons authorised to process are bound by confidentiality."),
    ("Security measures (Art. 32)", "Appropriate technical and organisational measures."),
    ("Sub-processors", "Prior authorisation and flow-down of equivalent terms; keep a Sub-processor List."),
    ("Assistance with data-subject rights", "Help the controller respond to access/erasure/other requests."),
    ("Breach notification and assistance", "Notify without undue delay; assist with obligations."),
    ("DPIA and prior-consultation assistance", "Assist with impact assessments where required."),
    ("Deletion or return at end", "Return or delete personal data at the controller's choice."),
    ("Audit information and inspections", "Make available information to demonstrate compliance; allow audits."),
    ("International transfers", "Only with a valid transfer mechanism (e.g. IDTA / UK Addendum to SCCs)."),
    ("Processing details schedule", "Subject matter; duration; nature and purpose; categories of personal data; categories of data subjects; controller rights/obligations; approved sub-processors; data locations; transfer mechanism; retention period; technical and organisational measures."),
    ("Signature block", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Controller and processor details; governing MSA/SOW reference.",
    "Processing details: subject matter, duration, nature/purpose, data categories, data-subject categories.",
    "Approved sub-processors, data locations, transfer mechanism, retention period.",
    "Technical and organisational security measures.",
  ],
  "uk_notes": [
    "UK GDPR Article 28 requires specific mandatory provisions — all must be present.",
    "For restricted international transfers, use the ICO IDTA or the UK Addendum to the EU SCCs.",
    "Special-category data or large-scale/high-risk processing warrants DPO/solicitor review and possibly a DPIA.",
  ],
  "best": [
    "Complete the processing-details schedule fully; blanks undermine compliance.",
    "Keep the Sub-processor List current and notify the controller of changes.",
    "Use a Data Sharing Agreement for controller-to-controller sharing.",
  ],
  "related": [16, 17, 11, 23],
  "refs": [
    ("ICO — Contracts between controllers and processors", "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/"),
    ("ICO — What needs to be in the contract", "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/"),
  ],
},
{
  "num": 7, "slug": "CHANGE_REQUEST", "title": "Change Request",
  "short": "Formalises any agreed change to scope, price, timeline or deliverables during delivery.",
  "binding": "Binding once signed by both parties; sits at the top of the order of precedence.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "Fully AI-draftable from the requested change; human review of price/timeline impact.",
  "purpose": [
    "A Change Request captures any material change to an in-flight project so that scope, price, timeline and acceptance stay controlled. No material change should be accepted only via a call or informal message.",
    "It protects both parties by documenting the impact of the change and the authorisation to proceed.",
  ],
  "when_use": [
    "Any change to scope, deliverables, price, timeline or resources.",
    "When customer requests would alter acceptance criteria.",
    "Whenever the impact must be agreed before work continues.",
  ],
  "blueprint": [
    ("Change Request reference", "Unique CR number; related SOW/MSA; date."),
    ("Requested change", "Precisely what is to change."),
    ("Reason", "Why the change is needed."),
    ("Effect on scope", "Additions/removals to scope and deliverables."),
    ("Effect on price", "Revised fees and payment impact."),
    ("Effect on timeline", "Revised dates/milestones."),
    ("Effect on resources", "People/skills impact."),
    ("Technical or security consequences", "Any risk or architecture impact."),
    ("Revised acceptance criteria", "Updated measurable criteria."),
    ("Authorisation clause", "Supplier is not required to start changed work until the CR is approved."),
    ("Signatures", "Both parties' authorised signatories and dates."),
  ],
  "inputs": [
    "Related SOW/MSA reference; CR number.",
    "The change, its reason, and impacts on scope/price/timeline/resources.",
    "Revised acceptance criteria.",
  ],
  "uk_notes": [
    "State expressly that changed work does not start until the CR is approved.",
    "A signed Change Request typically ranks above the SOW in the order of precedence.",
  ],
  "best": [
    "Never begin changed work on a verbal request.",
    "Quantify price and timeline impact precisely.",
  ],
  "related": [5, 4],
},
{
  "num": 8, "slug": "ACCEPTANCE_CERTIFICATE", "title": "Acceptance Certificate",
  "short": "Records the customer's written acceptance of deliverables and triggers warranty and final invoicing.",
  "binding": "A record/confirmation with contractual effect (starts warranty; authorises final invoice).",
  "signatories": "Authorised signatory of the Customer (accepting); countersigned by the Supplier.",
  "ai_level": "Fully AI-draftable from the SOW acceptance criteria; human confirmation of outstanding items.",
  "purpose": [
    "An Acceptance (or Completion) Certificate provides written confirmation that the customer has accepted the deliverables, closing the acceptance process defined in the SOW and starting the warranty/support period.",
    "It removes ambiguity about whether the work is done and unlocks the final invoice.",
  ],
  "when_use": [
    "At completion of a project or milestone with acceptance criteria.",
    "Before issuing the final invoice.",
    "To start the warranty/support clock.",
  ],
  "blueprint": [
    ("Reference and parties", "Related SOW/MSA; parties; date."),
    ("Deliverables received", "List of accepted deliverables."),
    ("Testing completed", "Confirmation acceptance testing was performed."),
    ("Outstanding minor items", "Snag list, if any, with target dates."),
    ("Effective acceptance date", "The date acceptance takes effect."),
    ("Start of warranty or support", "When the warranty/support period begins."),
    ("Approval to issue final invoice", "Authorisation to invoice the balance."),
    ("Signatures", "Customer acceptance; Supplier countersignature."),
  ],
  "inputs": [
    "Related SOW; list of deliverables and test results.",
    "Any outstanding minor items and dates.",
    "Acceptance date and warranty start.",
  ],
  "uk_notes": [
    "Tie acceptance to the SOW's objective criteria and any deemed-acceptance rule.",
    "Record snags separately so acceptance is not blocked by trivial items.",
  ],
  "best": [
    "Obtain written acceptance before final invoicing.",
    "Keep the signed certificate in the customer's closure records.",
  ],
  "related": [5, 9, 19],
},
{
  "num": 9, "slug": "INVOICE", "title": "Invoice",
  "short": "A compliant demand for payment referencing the SOW/PO and agreed milestones.",
  "binding": "A payment demand supported by the signed contract; not itself a contract.",
  "signatories": "Issued by the Supplier; no customer signature required.",
  "ai_level": "Fully AI-generatable from milestone + company data; human/finance check of VAT and totals.",
  "purpose": [
    "An Invoice requests payment for services delivered, referencing the governing SOW/PO and the agreed milestone so it is auditable and enforceable.",
    "It must contain the correct legal and (where applicable) VAT details to be valid and payable.",
  ],
  "when_use": [
    "At deposit, each milestone, and on acceptance/final balance.",
    "For recurring services billed in advance.",
  ],
  "blueprint": [
    ("Supplier legal name and address", "Legal name, registered/company address."),
    ("Company number", "Where appropriate."),
    ("Invoice number and date", "Unique sequential number; issue date."),
    ("Customer details", "Billing name and address."),
    ("Description of services", "What is being charged for."),
    ("SOW or PO reference", "Link to the governing document and milestone."),
    ("Net amount", "Amount before VAT."),
    ("VAT details", "VAT number and amount, only where applicable / registered."),
    ("Total due", "Gross total payable."),
    ("Payment terms", "e.g. payable within 14 days of invoice date."),
    ("Bank details", "Account for payment."),
    ("Late-payment wording", "Statutory interest/compensation notice where appropriate."),
  ],
  "inputs": [
    "Supplier company details and bank details; VAT registration status.",
    "Customer billing details; SOW/PO reference and milestone.",
    "Net amount, VAT position, payment terms.",
  ],
  "uk_notes": [
    "Only show VAT if VAT-registered; a valid VAT invoice has specific required content.",
    "For qualifying B2B debts, statutory late-payment interest is generally 8% above the Bank of England base rate plus fixed compensation; contractual interest wording can affect statutory rights.",
  ],
  "best": [
    "Reference the SOW/PO and milestone on every invoice.",
    "Keep invoice numbering sequential and auditable.",
  ],
  "related": [8, 5, 26],
  "standards": ["HMRC VAT rules", "ISO 27001"],
  "refs": [
    ("Small Business Commissioner — Late-payment guidance", "https://www.smallbusinesscommissioner.gov.uk/help-and-guidance/interest-calculator/"),
  ],
},
{
  "num": 10, "slug": "SERVICE_LEVEL_AGREEMENT", "title": "Service Level Agreement",
  "short": "Defines service levels, response/resolution targets and remedies for ongoing managed services, hosting or support.",
  "binding": "Binding schedule; takes precedence on service-level matters.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "AI-draftable from a service catalogue; human review of targets and service credits.",
  "purpose": [
    "A Service Level Agreement (SLA) sets measurable commitments for an ongoing service \u2014 support, hosting, maintenance or availability \u2014 and the consequences (e.g. service credits) if targets are missed.",
    "It protects the Supplier by defining exclusions and realistic targets, and protects the customer with clear, measurable service levels.",
  ],
  "when_use": [
    "Ongoing managed service, hosting or maintenance.",
    "Availability or support-response commitments.",
    "Any recurring service with performance obligations.",
  ],
  "blueprint": [
    ("Service description and hours", "Services covered and service hours."),
    ("Support channels", "How the customer raises issues."),
    ("Priority definitions", "Severity levels (P1\u2013P4) with examples."),
    ("Response times", "Time to first response per priority."),
    ("Resolution / workaround targets", "Target resolution or workaround per priority."),
    ("Uptime target", "Availability % and how measured."),
    ("Maintenance windows", "Planned maintenance timing and notice."),
    ("Exclusions", "Planned maintenance, customer systems, internet failures, third-party cloud/AI outages, force majeure, customer misuse."),
    ("Customer responsibilities", "What the customer must do for SLAs to apply."),
    ("Monitoring method", "How performance is measured."),
    ("Service credits", "Remedy for missed targets and how claimed."),
    ("Reporting", "Cadence and content of service reports."),
    ("Escalation path", "Who to escalate to and when."),
    ("Security incident contact", "Contact and process for security incidents."),
    ("Disaster recovery and business continuity", "RTO/RPO and continuity commitments."),
  ],
  "inputs": [
    "Service scope and hours; support channels.",
    "Priority definitions, response/resolution targets, uptime target.",
    "Exclusions, service credits, reporting and escalation.",
    "DR/BC commitments (RTO/RPO).",
  ],
  "uk_notes": [
    "Do not promise 100% uptime; define exclusions explicitly.",
    "Service credits are usually the sole financial remedy for SLA breaches \u2014 state this clearly.",
  ],
  "best": [
    "Set realistic, measurable targets you can evidence.",
    "Exclude third-party cloud/AI provider failures outside your control.",
  ],
  "related": [4, 11, 20],
},
{
  "num": 11, "slug": "SECURITY_SCHEDULE", "title": "Security Schedule",
  "short": "Sets the information-security controls the Supplier applies when handling sensitive data or privileged system access.",
  "binding": "Binding schedule to the MSA/SOW where incorporated.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "AI-draftable from the firm's security baseline; security lead review required.",
  "purpose": [
    "A Security Schedule documents the technical and organisational controls the Supplier maintains when handling sensitive information, privileged access or enterprise systems, giving the customer assurance and a basis for audit.",
    "It complements the DPA's Article 32 measures with concrete controls.",
  ],
  "when_use": [
    "Handling sensitive information or special-category data.",
    "Privileged access to customer production systems.",
    "Enterprise or regulated environments.",
  ],
  "blueprint": [
    ("Access control", "Least-privilege, role-based access, joiner/mover/leaver."),
    ("Multi-factor authentication", "MFA for privileged and remote access."),
    ("Encryption", "In transit and at rest."),
    ("Vulnerability management", "Scanning, patching cadence."),
    ("Logging and monitoring", "Audit logs and retention."),
    ("Backups", "Backup frequency, testing, retention."),
    ("Incident handling", "Detection, response, notification timelines."),
    ("Personnel security", "Vetting, training, confidentiality."),
    ("Secure development", "Secure SDLC, code review, dependency management."),
    ("Segregation of customer environments", "Isolation between customers."),
    ("Data deletion", "Secure deletion on exit/request."),
    ("Business continuity", "Continuity and recovery commitments."),
    ("Penetration testing", "Frequency and remediation."),
    ("Customer audit rights", "Scope and frequency of audits/evidence."),
  ],
  "inputs": [
    "The firm's security baseline and certifications (e.g. ISO 27001, Cyber Essentials).",
    "Project-specific controls, environments and audit rights.",
  ],
  "uk_notes": [
    "Align controls with ISO 27001 / NCSC guidance and the DPA's security obligations.",
    "Only commit to controls you actually operate and can evidence.",
  ],
  "best": [
    "Reference certifications you hold; do not overstate.",
    "Keep the schedule consistent with the DPA measures.",
  ],
  "related": [6, 16, 10],
  "standards": ["ISO 27001", "NCSC Cyber Essentials", "UK GDPR", "SOC 2"],
},
{
  "num": 12, "slug": "AI_RESPONSIBLE_USE_SCHEDULE", "title": "AI and Responsible Use Schedule",
  "short": "Sets the responsible-AI terms, limitations and risk allocation for AI-related deliverables.",
  "binding": "Binding schedule to the MSA/SOW where incorporated.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "AI-draftable from the firm's responsible-AI policy; human/solicitor review for regulated use.",
  "purpose": [
    "An AI (Responsible Use) Schedule governs AI-specific risks: intended and prohibited uses, human oversight, accuracy limitations, data rights, and allocation of residual risk the customer accepts.",
    "It makes clear that AI outputs require human review and that no regulated decision should rest solely on AI output unless expressly agreed and governed.",
  ],
  "when_use": [
    "Any deliverable that builds or integrates AI/LLM capabilities.",
    "Where model/provider dependencies and output rights need to be defined.",
    "Where the customer must accept AI accuracy/hallucination limitations.",
  ],
  "blueprint": [
    ("Intended and prohibited uses", "Permitted use cases and explicit prohibitions."),
    ("Human review responsibility", "Customer is responsible for appropriate human oversight."),
    ("Accuracy and hallucination limitations", "Outputs may be inaccurate, incomplete or non-unique."),
    ("Model and provider dependencies", "Named models/providers and their terms; changes may occur."),
    ("Training-data and input-data rights", "Rights to use data for the service."),
    ("Treatment of prompts and outputs", "How prompts/outputs are stored, used and secured."),
    ("Personal-data restrictions", "Limits on personal data in prompts/training."),
    ("Confidential-data restrictions", "Limits on confidential data in prompts/training."),
    ("Bias and fairness testing", "Testing approach where relevant."),
    ("Explainability expectations", "What explainability is/ isn't provided."),
    ("Model changes", "Effect of third-party model changes."),
    ("Output ownership and licensing", "Who owns/licenses generated output."),
    ("Regulatory responsibilities", "Each party's regulatory duties."),
    ("Logging, monitoring and safety controls", "Guardrails and monitoring."),
    ("Residual-risk acceptance", "Customer acceptance of stated residual risks."),
  ],
  "inputs": [
    "Intended/prohibited uses; models and providers.",
    "Data rights and restrictions; output ownership.",
    "Human-oversight and regulatory responsibilities; residual risks.",
  ],
  "uk_notes": [
    "State that no legal, medical, financial or regulated decision should be made solely from AI output unless expressly agreed and appropriately governed.",
    "Define AI performance metrics in the SOW rather than assuming them.",
    "Align with ISO/IEC 42001 and NIST AI RMF governance expectations.",
  ],
  "best": [
    "Require human-in-the-loop for consequential decisions.",
    "Be explicit about provider dependencies and change risk.",
  ],
  "related": [4, 5, 6],
  "standards": ["ISO 42001", "NIST AI RMF", "UK GDPR", "OWASP LLM Top 10"],
},
{
  "num": 13, "slug": "REQUIREMENTS_SPECIFICATION", "title": "Requirements Specification",
  "short": "Documents functional and non-functional requirements for development or automation work.",
  "binding": "Reference document; contractual where incorporated into the SOW.",
  "signatories": "Prepared by the Supplier; approved by the Customer's authorised contact.",
  "ai_level": "Fully AI-draftable from discovery; human validation with the customer.",
  "purpose": [
    "A Requirements Specification captures what a system or automation must do (functional) and how well (non-functional), forming the basis for design, build, testing and acceptance.",
    "Clear requirements reduce rework and anchor the SOW's acceptance criteria.",
  ],
  "when_use": [
    "Development, automation or integration projects.",
    "Whenever acceptance criteria depend on specified behaviour.",
  ],
  "blueprint": [
    ("Functional requirements", "What the system must do, as testable statements."),
    ("Non-functional requirements", "Performance, scalability, availability, usability."),
    ("Integrations", "Systems/APIs to integrate with."),
    ("Environments", "Dev/test/prod and access."),
    ("Data inputs and outputs", "Data sources, formats, fields."),
    ("Roles and permissions", "Who can do what."),
    ("Performance requirements", "Throughput, latency, volumes."),
    ("Security requirements", "Authentication, encryption, controls."),
    ("Testing requirements", "Test types and coverage."),
    ("Regulatory constraints", "Compliance requirements affecting the build."),
  ],
  "inputs": [
    "Discovery notes and stakeholder needs.",
    "Integration, environment and data details.",
    "Performance, security, testing and regulatory constraints.",
  ],
  "uk_notes": [
    "Make each requirement testable so it maps to SOW acceptance criteria.",
    "Capture data-protection and security requirements early.",
  ],
  "best": [
    "Number requirements for traceability to tests.",
    "Separate must-have from nice-to-have.",
  ],
  "related": [5, 12, 11],
},
{
  "num": 14, "slug": "PROJECT_PLAN", "title": "Project Plan",
  "short": "Sets out the work breakdown, milestones, owners, dependencies and cadence for larger projects.",
  "binding": "Working document; not itself contractual unless incorporated.",
  "signatories": "Owned by the Supplier project lead; shared with the Customer.",
  "ai_level": "Fully AI-generatable and maintainable; human owner validates dates and dependencies.",
  "purpose": [
    "A Project Plan organises delivery: what will be done, by whom, by when, and how progress and decisions are managed. It keeps larger engagements on track and transparent.",
    "It complements the SOW milestones with operational detail.",
  ],
  "when_use": [
    "Larger or multi-phase projects.",
    "Where dependencies and decision deadlines must be tracked.",
  ],
  "blueprint": [
    ("Work breakdown", "Phases, workstreams and tasks."),
    ("Milestones", "Key dates tied to SOW payments/acceptance."),
    ("Owners", "Responsible person per task/workstream."),
    ("Dependencies", "Internal and customer dependencies."),
    ("Risks", "Key risks and mitigations (link to Risk Register)."),
    ("Communication cadence", "Meetings, status updates."),
    ("Reporting", "What is reported and to whom."),
    ("Decision deadlines", "Dates by which customer decisions are needed."),
  ],
  "inputs": [
    "SOW scope, deliverables and milestones.",
    "Team and roles; customer dependencies.",
    "Reporting cadence and decision deadlines.",
  ],
  "uk_notes": [
    "Customer delay should entitle the Supplier to adjust the timeline (and, where appropriate, fees) \u2014 reflect this in the SOW.",
  ],
  "best": [
    "Tie milestones to SOW payments and acceptance.",
    "Make customer decision deadlines explicit.",
  ],
  "related": [5, 15, 19],
},
{
  "num": 15, "slug": "RISK_REGISTER", "title": "Risk Register",
  "short": "Tracks project risks with likelihood, impact, owners and mitigations.",
  "binding": "Internal working document.",
  "signatories": "Owned by the Supplier project lead; reviewed with the Customer as needed.",
  "ai_level": "Fully AI-generatable and continuously updatable; human owner validates ratings.",
  "purpose": [
    "A Risk Register captures what could go wrong, how likely and severe it is, who owns it, and what is being done about it \u2014 enabling proactive management rather than surprise.",
    "It feeds governance reporting and supports the liability/insurance posture.",
  ],
  "when_use": [
    "Any project with material delivery, security or commercial risk.",
    "As a standing artefact reviewed at governance checkpoints.",
  ],
  "blueprint": [
    ("Risk ID and description", "Unique ID and clear description."),
    ("Category", "Delivery, security, data, commercial, third-party, AI."),
    ("Likelihood and impact", "Ratings (e.g. 1\u20135) and resulting score."),
    ("Risk owner", "Accountable person."),
    ("Mitigation / controls", "Actions to reduce likelihood/impact."),
    ("Contingency", "Fallback if the risk materialises."),
    ("Status and review date", "Open/closed and next review."),
  ],
  "inputs": [
    "Identified risks from planning and due diligence.",
    "Rating scale and owners.",
  ],
  "uk_notes": [
    "Include data-protection and AI-specific risks explicitly.",
  ],
  "best": [
    "Assign a single accountable owner per risk.",
    "Review at every governance checkpoint.",
  ],
  "related": [14, 18, 12],
},
{
  "num": 16, "slug": "DATA_MAPPING_QUESTIONNAIRE", "title": "Data Mapping Questionnaire",
  "short": "Captures what personal data is involved, so the correct data-protection terms can be applied.",
  "binding": "Intake/record document informing the DPA and DPIA.",
  "signatories": "Completed jointly by the Supplier and Customer.",
  "ai_level": "AI-assisted intake; human/DPO validation of data categories and risk.",
  "purpose": [
    "A Data Mapping Questionnaire establishes whether and how personal data is processed, feeding the DPA processing schedule and any DPIA, and confirming whether the Supplier is a processor or joint/independent controller.",
    "It prevents processing personal data without the correct data terms in place.",
  ],
  "when_use": [
    "At scoping, whenever personal data may be involved.",
    "Before finalising the DPA schedule.",
  ],
  "blueprint": [
    ("Processing activities", "What processing will occur."),
    ("Categories of personal data", "Including any special-category data."),
    ("Categories of data subjects", "Whose data is involved."),
    ("Purpose and lawful basis", "Why data is processed and the basis."),
    ("Data sources and flows", "Where data comes from and goes."),
    ("Controller/processor determination", "Roles of each party."),
    ("Sub-processors and locations", "Who else processes and where."),
    ("International transfers", "Any restricted transfers and mechanism."),
    ("Retention", "How long data is kept."),
    ("Risk indicators", "Triggers for a DPIA."),
  ],
  "inputs": [
    "Scope and data flows from discovery.",
    "Customer information on data categories and subjects.",
  ],
  "uk_notes": [
    "Special-category data, large-scale or high-risk processing may require a DPIA.",
    "Use the output to complete the DPA processing schedule accurately.",
  ],
  "best": [
    "Complete before any personal data is shared.",
    "Escalate high-risk findings to the DPO/solicitor.",
  ],
  "related": [6, 23, 17],
},
{
  "num": 17, "slug": "SUB_PROCESSOR_LIST", "title": "Sub-processor List",
  "short": "The maintained register of approved sub-processors disclosed to the customer under the DPA.",
  "binding": "Record/schedule referenced by the DPA; changes trigger notice to the controller.",
  "signatories": "Maintained by the Supplier; provided to the Customer.",
  "ai_level": "AI-maintainable from the vendor register; human validation before publication.",
  "purpose": [
    "A Sub-processor List discloses the third parties the Supplier uses to process personal data on the customer's behalf, supporting UK GDPR transparency and the DPA's sub-processor authorisation terms.",
    "Keeping it current is a compliance obligation, not an optional courtesy.",
  ],
  "when_use": [
    "Whenever a DPA is in place and sub-processors are used.",
    "When adding, changing or removing a sub-processor.",
  ],
  "blueprint": [
    ("Sub-processor name", "Legal entity."),
    ("Service provided", "What they do for the Supplier."),
    ("Personal data processed", "Categories of data they handle."),
    ("Location(s)", "Country/region of processing."),
    ("Transfer mechanism", "Where relevant (IDTA / UK Addendum)."),
    ("Safeguards", "Security/compliance status (e.g. ISO 27001)."),
    ("Effective date and change log", "When added/changed; notice given."),
  ],
  "inputs": [
    "Approved vendor/sub-processor register.",
    "Processing locations and transfer mechanisms.",
  ],
  "uk_notes": [
    "Provide advance notice of sub-processor changes so the controller can object.",
    "Ensure each sub-processor is bound by equivalent data-protection terms.",
  ],
  "best": [
    "Keep a single source of truth and version it.",
    "Notify the controller before onboarding a new sub-processor.",
  ],
  "related": [6, 16, 10],
},
{
  "num": 18, "slug": "CUSTOMER_DUE_DILIGENCE_CHECKLIST", "title": "Customer Due-Diligence Checklist",
  "short": "The pre-engagement checks confirming who the customer is and whether the work is safe to accept.",
  "binding": "Internal record supporting the decision to engage.",
  "signatories": "Completed by the Supplier; approved per the internal approval matrix.",
  "ai_level": "AI-assisted (Companies House / sanctions / adverse-media lookups); human decision to proceed.",
  "purpose": [
    "A Customer Due-Diligence Checklist verifies the customer's identity, standing and risk before accepting work \u2014 covering legal identity, creditworthiness, sanctions, data legality and conflicts.",
    "It protects the Supplier from legal, financial, reputational and regulatory exposure.",
  ],
  "when_use": [
    "Before accepting any new customer or higher-risk engagement.",
    "Before signing the MSA/SOW.",
  ],
  "blueprint": [
    ("Legal identity", "Legal name, company number, Companies House record."),
    ("Addresses", "Registered office and trading address."),
    ("VAT and tax", "VAT number where relevant."),
    ("Authorised signatory", "Who can bind the customer."),
    ("Creditworthiness", "Ability to pay / credit check."),
    ("Sanctions and PEP screening", "Sanctions exposure."),
    ("Adverse media", "For higher-risk work."),
    ("Data source and use", "Source and intended use of data."),
    ("Regulated-sector requirements", "Sector-specific obligations."),
    ("Project legality", "Is the work lawful?"),
    ("Conflicts of interest", "Any conflicts to manage."),
    ("Decision and approver", "Outcome and who approved it."),
  ],
  "inputs": [
    "Customer-provided details; public registers.",
    "Internal approval matrix thresholds.",
  ],
  "uk_notes": [
    "Check the Companies House record for UK companies and screen for sanctions.",
    "Escalate to director approval per the internal matrix for higher-risk indicators.",
  ],
  "best": [
    "Complete before signing, not after.",
    "Record the decision and approver for audit.",
  ],
  "related": [4, 1, 15],
  "refs": [
    ("GOV.UK — Companies House", "https://www.gov.uk/government/organisations/companies-house"),
  ],
},
{
  "num": 19, "slug": "PROJECT_CLOSURE_REPORT", "title": "Project Closure Report",
  "short": "Formally closes a project: outcomes, acceptance, outstanding items, lessons and handover.",
  "binding": "Record document; supports final invoicing and warranty start.",
  "signatories": "Prepared by the Supplier; acknowledged by the Customer.",
  "ai_level": "Fully AI-draftable from project records; human review of outcomes and lessons.",
  "purpose": [
    "A Project Closure Report records what was delivered against the SOW, confirms acceptance, lists any outstanding items, captures lessons learned, and documents handover \u2014 providing a clean, auditable end to the engagement.",
    "It pairs with the Acceptance Certificate to close delivery and open support/renewal.",
  ],
  "when_use": [
    "At the end of a project or major phase.",
    "To transition into support, renewal or closure.",
  ],
  "blueprint": [
    ("Project summary", "Objectives and what was delivered."),
    ("Deliverables vs SOW", "Mapping of delivered items to scope."),
    ("Acceptance status", "Reference to the Acceptance Certificate."),
    ("Outstanding items", "Snags and follow-ups with owners/dates."),
    ("Budget and schedule outcome", "Planned vs actual."),
    ("Lessons learned", "What to repeat/improve."),
    ("Handover and documentation", "What was handed over."),
    ("Support and renewal", "Warranty/support start; renewal options."),
    ("Sign-off", "Supplier and customer acknowledgement."),
  ],
  "inputs": [
    "SOW, Acceptance Certificate, project records.",
    "Budget/schedule actuals and lessons.",
  ],
  "uk_notes": [
    "Confirm data return/deletion obligations are addressed at closure.",
  ],
  "best": [
    "Capture lessons while fresh.",
    "Confirm warranty start and support/renewal path.",
  ],
  "related": [8, 20, 14],
},
{
  "num": 20, "slug": "SUPPORT_AND_MAINTENANCE_AGREEMENT", "title": "Support and Maintenance Agreement",
  "short": "Governs ongoing support, maintenance and updates after go-live, usually with an SLA.",
  "binding": "Binding; typically recurring with an attached SLA.",
  "signatories": "Authorised signatory of the Supplier and of the Customer.",
  "ai_level": "AI-draftable from a service catalogue; human review of scope and fees.",
  "purpose": [
    "A Support and Maintenance Agreement covers what happens after delivery: bug fixes, updates, support and maintenance, with commercial terms for the recurring relationship. It usually incorporates an SLA for response/resolution.",
    "It converts a delivered project into an ongoing, revenue-generating service.",
  ],
  "when_use": [
    "After go-live, for ongoing support/maintenance.",
    "For subscription or retainer services.",
  ],
  "blueprint": [
    ("Scope of support and maintenance", "What is covered (fixes, updates, patches)."),
    ("Exclusions", "New features, third-party faults, misuse."),
    ("Service levels", "Reference the SLA (priorities, response/resolution)."),
    ("Fees and term", "Recurring fees, term, renewal, uplift."),
    ("Change and enhancement requests", "How new work is handled (Change Request)."),
    ("Customer responsibilities", "Access, environments, cooperation."),
    ("Data protection and security", "DPA/Security Schedule references."),
    ("Termination and exit", "Notice, exit assistance, data return."),
    ("Governing law", "England and Wales."),
  ],
  "inputs": [
    "Support scope, exclusions and SLA.",
    "Recurring fees, term and renewal.",
    "DPA/Security references.",
  ],
  "uk_notes": [
    "Bill recurring services in advance; state renewal and price-review mechanics.",
    "Reference the SLA rather than duplicating service levels.",
  ],
  "best": [
    "Separate support (covered) from enhancements (Change Requests).",
    "Attach the SLA and keep it current.",
  ],
  "related": [10, 7, 6],
},
{
  "num": 21, "slug": "SUBCONTRACTOR_AGREEMENT", "title": "Subcontractor Agreement",
  "short": "Governs work the Supplier subcontracts to a specialist, flowing down customer obligations.",
  "binding": "Binding between the Supplier and the subcontractor.",
  "signatories": "Authorised signatory of the Supplier and of the subcontractor.",
  "ai_level": "AI-draftable from a base; solicitor review for IP flow-down and liability.",
  "purpose": [
    "A Subcontractor Agreement lets the Supplier engage a specialist to deliver part of a customer project while remaining responsible to the customer. It flows down confidentiality, data-protection, IP and security obligations so the Supplier can meet its customer commitments.",
    "It protects the Supplier by ensuring the subcontractor's terms are compatible with the head contract.",
  ],
  "when_use": [
    "Engaging specialists, contractors or partners on a customer project.",
    "Whenever obligations from the MSA/SOW must flow down.",
  ],
  "blueprint": [
    ("Parties and scope", "Supplier, subcontractor, and the subcontracted scope."),
    ("Relationship to head contract", "Back-to-back obligations with the customer agreement."),
    ("Fees and payment", "Charges and payment terms."),
    ("Confidentiality", "Equivalent to the head NDA/MSA."),
    ("Data protection (sub-processing)", "UK GDPR flow-down; Supplier authorisation as controller-processor chain."),
    ("Intellectual property", "Assignment/licence so the Supplier can grant customer rights."),
    ("Security obligations", "Flow-down of the Security Schedule."),
    ("Warranties and liability", "Skill and care; liability aligned to head contract."),
    ("Insurance", "Required cover."),
    ("Term and termination", "Duration and exit."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Subcontracted scope and fees.",
    "Head-contract obligations to flow down (IP, data, security, confidentiality).",
  ],
  "uk_notes": [
    "You cannot grant the customer greater IP rights than you obtain from the subcontractor \u2014 ensure IP assignment/licence flows through.",
    "The Supplier remains responsible to the customer for subcontracted work.",
    "Confirm the subcontractor is an approved sub-processor where personal data is involved.",
  ],
  "best": [
    "Keep terms back-to-back with the customer agreement.",
    "Maintain an internal register of approved subcontractors.",
  ],
  "related": [4, 22, 17],
},
{
  "num": 22, "slug": "INDEPENDENT_CONTRACTOR_AGREEMENT", "title": "Independent Contractor Agreement",
  "short": "Engages an individual contractor, clarifying self-employed status, IP assignment and confidentiality.",
  "binding": "Binding between the Supplier and the contractor.",
  "signatories": "Authorised signatory of the Supplier and the contractor.",
  "ai_level": "AI-draftable from a base; review for employment-status (IR35) and IP.",
  "purpose": [
    "An Independent Contractor Agreement engages an individual on a self-employed basis, defining deliverables, fees, IP assignment and confidentiality while avoiding the creation of an employment relationship.",
    "It must address UK employment-status and tax considerations (including IR35/off-payroll where relevant).",
  ],
  "when_use": [
    "Engaging an individual freelancer/contractor.",
    "Where IP must vest in the Supplier and confidentiality is needed.",
  ],
  "blueprint": [
    ("Parties and services", "Contractor, Supplier, and the services."),
    ("Status and independence", "Self-employed; not an employee; substitution where genuine."),
    ("Fees and invoicing", "Rates, invoicing, expenses."),
    ("Intellectual property assignment", "Present assignment of IP in deliverables to the Supplier."),
    ("Confidentiality", "Protection of Supplier and customer information."),
    ("Data protection", "Compliance where personal data is handled."),
    ("Tax and IR35", "Contractor responsible for own tax; off-payroll status where applicable."),
    ("Warranties and liability", "Skill and care; right to enter."),
    ("Term and termination", "Duration and notice."),
    ("Restrictive covenants", "Reasonable, where justified."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Signatory and date."),
  ],
  "inputs": [
    "Contractor details and services; fees.",
    "IP and confidentiality requirements; IR35 status determination.",
  ],
  "uk_notes": [
    "Assess employment status and IR35/off-payroll rules; misclassification carries tax and employment risk.",
    "IP does not pass automatically \u2014 include a written, signed assignment.",
  ],
  "best": [
    "Include a present assignment of IP, effective on creation and payment.",
    "Keep genuine independence (control, substitution) consistent with contractor status.",
  ],
  "related": [21, 4],
},
{
  "num": 23, "slug": "DATA_SHARING_AGREEMENT", "title": "Data Sharing Agreement",
  "short": "Governs controller-to-controller personal-data sharing (where a processor DPA is not the right instrument).",
  "binding": "Binding; used for independent controller-to-controller sharing.",
  "signatories": "Authorised signatory of each controller.",
  "ai_level": "AI-draftable from a base; DPO/solicitor review recommended.",
  "purpose": [
    "A Data Sharing Agreement governs situations where both parties independently decide why and how personal data is used (controller-to-controller), setting out purposes, lawful bases, security and responsibilities \u2014 which a processor DPA does not cover.",
    "It aligns with the ICO's data sharing code of practice.",
  ],
  "when_use": [
    "Both parties act as independent (or joint) controllers.",
    "Sharing personal data for each party's own purposes.",
  ],
  "blueprint": [
    ("Parties and roles", "Each party as controller; joint vs independent."),
    ("Purpose of sharing", "Why data is shared and the lawful basis."),
    ("Data shared", "Categories of personal data and data subjects."),
    ("Method and frequency", "How and how often data is shared."),
    ("Security measures", "Protection in transit and at rest."),
    ("Data-subject rights and transparency", "How rights and privacy information are handled."),
    ("Retention and deletion", "How long each party keeps data."),
    ("International transfers", "Mechanism where relevant."),
    ("Breach handling", "Notification and cooperation."),
    ("Liability and indemnity", "Allocation between controllers."),
    ("Governing law", "England and Wales."),
    ("Signatures", "Authorised signatories and dates."),
  ],
  "inputs": [
    "Purpose, lawful basis, and data categories.",
    "Security, retention and transfer details.",
  ],
  "uk_notes": [
    "Use this instead of a processor DPA when both parties determine purposes and means.",
    "Follow the ICO data sharing code of practice; confirm a lawful basis for each party.",
  ],
  "best": [
    "Be explicit about who is controller for what.",
    "Provide clear privacy information to data subjects.",
  ],
  "related": [6, 16, 24],
},
{
  "num": 24, "slug": "WEBSITE_PRIVACY_NOTICE", "title": "Website Privacy Notice",
  "short": "The public UK GDPR transparency notice explaining how the business handles personal data on its website.",
  "binding": "Public statement (not a contract); a UK GDPR transparency obligation.",
  "signatories": "Published by the business; no signature.",
  "ai_level": "Fully AI-draftable from a data inventory; DPO/human review before publishing.",
  "purpose": [
    "A Website Privacy Notice tells visitors what personal data the business collects, why, the lawful basis, who it is shared with, how long it is kept, and their rights \u2014 satisfying UK GDPR Articles 13\u201314 transparency duties.",
    "It must be accurate to actual processing and kept up to date.",
  ],
  "when_use": [
    "Any public website or app collecting personal data.",
    "Whenever processing purposes or third parties change.",
  ],
  "blueprint": [
    ("Who we are", "Controller identity and contact (and DPO if any)."),
    ("What data we collect", "Categories of personal data."),
    ("How we collect it", "Direct, automated, third-party sources."),
    ("Purposes and lawful bases", "Why, and the UK GDPR lawful basis for each."),
    ("Cookies and tracking", "Reference the Cookie Notice."),
    ("Sharing and processors", "Who data is shared with."),
    ("International transfers", "Any transfers and safeguards."),
    ("Retention", "How long data is kept."),
    ("Your rights", "Access, rectification, erasure, objection, portability, complaint to the ICO."),
    ("Security", "How data is protected."),
    ("Changes and contact", "How updates are notified; contact details."),
  ],
  "inputs": [
    "Data inventory: what is collected, why, lawful bases.",
    "Processors/third parties, transfers, retention periods.",
    "Controller and (if any) DPO contact details.",
  ],
  "uk_notes": [
    "Must meet UK GDPR Articles 13\u201314; include the right to complain to the ICO.",
    "Keep it specific to actual processing \u2014 generic notices are non-compliant.",
  ],
  "best": [
    "Layer the notice for readability (summary + detail).",
    "Review whenever processing changes.",
  ],
  "related": [25, 6, 23],
  "standards": ["UK GDPR", "Data Protection Act 2018", "PECR"],
  "refs": [
    ("ICO — Right to be informed", "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/"),
  ],
},
{
  "num": 25, "slug": "WEBSITE_COOKIE_NOTICE", "title": "Website Cookie Notice",
  "short": "Explains cookies/similar technologies and obtains PECR-compliant consent for non-essential cookies.",
  "binding": "Public statement plus consent mechanism (PECR/UK GDPR obligation).",
  "signatories": "Published by the business; no signature.",
  "ai_level": "Fully AI-draftable from a cookie audit; human review of consent mechanics.",
  "purpose": [
    "A Website Cookie Notice discloses the cookies and similar technologies in use and supports a compliant consent mechanism (consent required for non-essential cookies under PECR, with UK GDPR-standard consent).",
    "It must reflect an actual cookie audit and allow users to accept, reject and manage cookies.",
  ],
  "when_use": [
    "Any website using cookies or similar tracking.",
    "Whenever analytics, advertising or embedded third-party content is used.",
  ],
  "blueprint": [
    ("What cookies are", "Brief explanation."),
    ("Cookies we use", "Table: name, provider, purpose, type, duration."),
    ("Strictly necessary vs optional", "Distinguish essential from non-essential."),
    ("Consent mechanism", "How consent is obtained, refused and withdrawn."),
    ("Third-party cookies", "Analytics, advertising, embeds."),
    ("Managing preferences", "How to change settings/browser controls."),
    ("Links", "Reference the Privacy Notice."),
    ("Updates", "How changes are handled."),
  ],
  "inputs": [
    "Cookie audit: each cookie's name, provider, purpose, duration.",
    "Consent tool/mechanism details.",
  ],
  "uk_notes": [
    "PECR requires prior consent for non-essential cookies; essential cookies are exempt.",
    "Consent must be as easy to refuse as to give \u2014 no pre-ticked boxes.",
  ],
  "best": [
    "Base the notice on a real, current cookie audit.",
    "Provide granular accept/reject controls.",
  ],
  "related": [24, 6],
  "standards": ["PECR", "UK GDPR"],
  "refs": [
    ("ICO — Cookies and similar technologies", "https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/"),
  ],
},
{
  "num": 26, "slug": "BUSINESS_CUSTOMER_TERMS", "title": "Business Customer Terms and Conditions",
  "short": "Standard B2B terms for lower-complexity engagements, or a combined Services Agreement for small projects.",
  "binding": "Binding on acceptance; can serve as the combined agreement for small projects.",
  "signatories": "Accepted by the Customer (signature/order); issued by the Supplier.",
  "ai_level": "AI-draftable from the MSA base; solicitor review before first use.",
  "purpose": [
    "Business Customer Terms and Conditions provide standard B2B contract terms for straightforward engagements without a full negotiated MSA. For a small, low-risk project they can be combined with an SOW into a single Services Agreement.",
    "They compress the essential MSA protections into a reusable, acceptance-based form.",
  ],
  "when_use": [
    "Small or standardised B2B engagements.",
    "As the combined Services Agreement + SOW for very small projects.",
    "Where a full negotiated MSA is disproportionate.",
  ],
  "blueprint": [
    ("Scope and services", "What is provided and exclusions."),
    ("Deliverables and acceptance", "Outputs and acceptance criteria."),
    ("Timeline", "Indicative delivery."),
    ("Fees and payment", "Charges, deposit, payment days, late payment."),
    ("Change control", "How changes are agreed."),
    ("Intellectual property", "Background IP vs deliverables; assignment on payment."),
    ("Confidentiality", "Mutual obligations."),
    ("Data protection", "UK GDPR; DPA where personal data is processed."),
    ("Warranties and AI limitations", "Skill and care; AI output caveats."),
    ("Liability", "Cap and excluded losses; non-excludable liabilities preserved."),
    ("Termination", "Duration and exit."),
    ("Governing law", "England and Wales; exclusive jurisdiction."),
    ("Acceptance and signatures", "How the customer accepts."),
  ],
  "inputs": [
    "Standard firm positions (payment, IP, liability).",
    "Scope, deliverables and acceptance for the specific engagement.",
  ],
  "uk_notes": [
    "State which document prevails if a customer PO conflicts with these terms.",
    "Preserve non-excludable liabilities; align the cap to insurance.",
  ],
  "best": [
    "Use for small/standard work; use MSA+SOW for complex engagements.",
    "Keep consistent with the MSA so they can scale up cleanly.",
  ],
  "related": [4, 5, 27],
},
{
  "num": 27, "slug": "CONSUMER_TERMS", "title": "Consumer Terms",
  "short": "Separate terms for individuals buying outside their trade, with mandatory consumer protections.",
  "binding": "Binding, subject to mandatory UK consumer-protection law.",
  "signatories": "Accepted by the consumer; issued by the Supplier.",
  "ai_level": "AI-draftable from a base; solicitor review strongly recommended before selling to consumers.",
  "purpose": [
    "Consumer Terms apply where the customer is an individual acting mainly outside their trade or profession. UK consumer law adds mandatory protections \u2014 fairness, transparency and cancellation rights for distance contracts \u2014 that B2B terms do not address.",
    "They must be fair and transparent; unfair terms are unenforceable.",
  ],
  "when_use": [
    "Selling bespoke services directly to individuals (consumers).",
    "Distance/online contracts with consumers.",
  ],
  "blueprint": [
    ("Who we are and how to contact us", "Trader identity and contact."),
    ("Services and price", "Clear description and total price (incl. VAT)."),
    ("Ordering and acceptance", "How the contract forms."),
    ("Right to cancel", "14-day cancellation for distance contracts and exceptions."),
    ("Performance and timing", "When services are provided; consumer consent to start early."),
    ("Consumer rights", "Statutory rights (reasonable care and skill; remedies)."),
    ("Payment", "Amounts and timing."),
    ("Liability", "Fair terms; statutory rights not excluded."),
    ("Complaints and dispute resolution", "How to complain; ADR/ODR information."),
    ("Data protection", "Reference the Privacy Notice."),
    ("Governing law", "England and Wales (consumer's statutory protections preserved)."),
  ],
  "inputs": [
    "Service description and total price (incl. VAT).",
    "Cancellation and performance-start details.",
  ],
  "uk_notes": [
    "Consumer Rights Act 2015 and Consumer Contracts Regulations 2013 apply; terms must be fair and transparent.",
    "Distance contracts carry a 14-day right to cancel (with limited exceptions); handle early-start consent correctly.",
    "Obtain legal advice before selling bespoke services directly to consumers.",
  ],
  "best": [
    "Never reuse B2B terms for consumers unchanged.",
    "Make cancellation rights and total price prominent.",
  ],
  "related": [26, 24],
  "standards": ["Consumer Rights Act 2015", "Consumer Contracts Regulations 2013", "UK GDPR"],
},
]

# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
DOC_BY_NUM = {d["num"]: d for d in DOCS}


def file_name(d: dict) -> str:
    return f"{d['num']:02d}_{d['slug']}_SKILL.md"


def pack_of(d: dict) -> str:
    return "Essential" if d["num"] <= 9 else "Extended"


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
        f"id: BIZDOC-{d['num']:03d}",
        f"title: {d['title']} — Generation Skill",
        "document_type: Skill",
        "category: Business Documentation",
        "phase: Phase 05",
        "owner: Commercial and Contracts Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "jurisdiction: England and Wales",
        "tags:",
        "  - skill",
        "  - business-documentation",
        f"  - {tag_slug}",
        "related_documents:",
        "  - ROOT_INDEX.md",
        "  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md",
        "  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md",
        f"  - 02_ARTEFACTS/PHASE_05_SKILLS/Business_Documentation/{FRAMEWORK_FILE}",
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
    related.append(f"- [UK Contracting Framework]({FRAMEWORK_FILE})")
    related.append(f"- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide]({R_GUIDE})")
    related.append(f"- [Business Documentation Index](README.md)")
    related.append(f"- [All Phase 05 Skills]({R_SKILLS})")
    related.append(f"- [Enterprise Templates]({R_TEMPLATES})")
    related.append(f"- [AIBOS Root Specification]({R_SPEC})")
    related.append(f"- [Enterprise Glossary]({R_GLOSSARY})")

    body = f"""# {d['title']} — Generation Skill

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Skills]({R_SKILLS}) · [Business Docs](README.md) · [UK Framework]({FRAMEWORK_FILE}) · [Source Guide]({R_GUIDE})

## At a Glance

{d['short']}

| Field | Detail |
| --- | --- |
| Document | {d['title']} |
| Category | Business Documentation |
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
| 1.0.0 | {CREATED} | Complete, generate-ready UK business-document skill. |
"""
    return "\n".join(fm) + "\n\n" + body


ARCH_DIAGRAM = """```text
Customer enquiry -> Discovery call -> NDA (where required)
   -> Proposal / Quotation -> Due diligence & risk review
   -> MSA + SOW + DPA/SLA (where applicable) -> Both parties sign
   -> Deposit / first milestone -> Delivery
   -> Change Requests (for scope changes) -> Testing & acceptance
   -> Acceptance Certificate -> Final invoice, support, renewal or closure
```"""


def render_framework() -> str:
    essential = [d for d in DOCS if d["num"] <= 9]
    extended = [d for d in DOCS if d["num"] > 9]

    def rows(docs):
        return "\n".join(
            f"| {d['num']:02d} | [{d['title']}]({file_name(d)}) | {d['short']} |"
            for d in docs
        )

    fm = [
        "---",
        "id: BIZDOC-000",
        "title: UK Contracting Framework (Reference)",
        "document_type: Reference",
        "category: Business Documentation",
        "phase: Phase 05",
        "owner: Commercial and Contracts Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "jurisdiction: England and Wales",
        "tags:",
        "  - business-documentation",
        "  - contracts",
        "  - reference",
        "related_documents:",
        "  - ROOT_INDEX.md",
        "  - 00_ROOT/Lemuran_Ltd_UK_Client_Engagement_Legal_Guide.md",
        "---",
    ]

    body = f"""# UK Contracting Framework (Reference)

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Skills]({R_SKILLS}) · [Business Docs](README.md) · [Source Guide]({R_GUIDE})

## Legal Notice

{LEGAL_NOTICE}

## Overview

This is the shared reference for the AIBOS Business Documentation skills. It captures
the recommended contract architecture, document set, order of precedence, signing
order and drafting principles for United Kingdom (England and Wales) B2B technology
engagements. It is derived from the
[Lemuran Ltd — UK Client Engagement Legal Guide]({R_GUIDE}) and standard UK best
practice. Each skill in this folder generates one document consistent with this
framework.

## Recommended Contract Architecture

{ARCH_DIAGRAM}

For most B2B AI and software projects use **MSA + SOW + DPA (where personal data is
processed) + SLA (where ongoing service commitments apply)**, supported by an **NDA**
before detailed disclosure, **Change Requests** during delivery, and an **Acceptance
Certificate** at completion. For a small, low-risk project, combine terms into one
well-drafted [Business Customer Terms and Conditions](26_BUSINESS_CUSTOMER_TERMS_SKILL.md)
(Services Agreement) with schedules.

## Essential Document Pack

| # | Document | Purpose |
| --- | --- | --- |
{rows(essential)}

## Extended Document Pack

| # | Document | Purpose |
| --- | --- | --- |
{rows(extended)}

## Order of Precedence (Contract Hierarchy)

State the hierarchy expressly in the MSA. Recommended order:

1. Signed Change Request
2. Statement of Work
3. Data Processing Agreement (for data-protection matters)
4. Service Level Agreement (for service-level matters)
5. Master Services Agreement
6. Proposal
7. Purchase Order

## Recommended Signing Order

**Standard project:** NDA (if required) → Proposal marked "subject to contract" →
customer due-diligence checks → MSA → SOW → DPA and Security Schedule (where
required) → SLA (where required) → both parties sign → deposit or first invoice
paid → kick-off.

**Very small project:** one combined Services Agreement and SOW covering scope,
deliverables, timeline, price, payment, IP, confidentiality, data protection,
liability, termination, acceptance, governing law and signatures.

## Minimum Clause Checklist

- Correct legal parties; scope and exclusions; deliverables; timeline and milestones
- Customer dependencies; fees and payment dates; expenses and taxes; change control
- Acceptance testing; intellectual property (incl. Background IP); third-party and open-source components
- Confidentiality; data protection; information security; AI-specific risks
- Warranties; liability cap; excluded losses; indemnities; insurance
- Subcontractors; suspension; termination; exit and data deletion; dispute escalation
- Governing law; signature authority

## Intellectual Property Principles

- The Supplier normally retains **Background IP** (frameworks, templates, libraries, prompts, reusable code, tools, know-how, models, connectors).
- The customer receives ownership or a broad licence to the **bespoke paid-for deliverables**; assignment or final licence takes effect **only after full payment**.
- **Third-party and open-source** components remain subject to their own licences — the Supplier cannot grant greater rights than it holds.
- UK copyright in commissioned work is not transferred automatically; assignment must be **in writing and signed**.

## Payment and Financial Protections

- New customers: 30%–50% deposit; milestone payments; final balance on acceptance; recurring services billed in advance.
- Clear payment terms (e.g. "payable within 14 days of the invoice date").
- Late payment: for qualifying B2B debts, statutory interest is generally **8% above the Bank of England base rate** plus fixed compensation; review contractual interest wording against statutory rights.
- Allow **suspension** after overdue payment, written notice and a reasonable cure period.

## Liability and Risk Allocation

- Cap ordinary contractual liability (e.g. fees under the relevant SOW, or fees paid in the previous 12 months) aligned to insurance.
- Exclude indirect/consequential loss, lost profits/revenue/business, loss of goodwill (where legally permitted).
- Do **not** exclude non-excludable liabilities (death/personal injury from negligence, fraud). A solicitor should draft this section.
- Use indemnities carefully — they can create uncapped exposure.

## Customer Due Diligence

Verify legal name, Companies House record, addresses, VAT number, authorised
signatory, creditworthiness, sanctions exposure, adverse media (higher-risk work),
data source/use, regulated-sector requirements, project legality, ability to pay and
conflicts of interest before accepting work.

## Insurance to Consider

Professional Indemnity; Cyber; Public Liability; Employers' Liability (if required);
Directors' and Officers'; Legal Expenses. Align liability caps with available cover.

## Internal Approval (Director Sign-off) Triggers

Value over threshold; unlimited liability; cap exceeding insurance; customer wants
Supplier Background IP; exclusivity; broad indemnities; special-category data;
complex international transfers; regulated decision-making; certifications not held;
extended payment terms; foreign law/courts; subcontracting prohibited; source-code
escrow; unusually high penalties or service credits.

## Practical Operating Rules

1. Do not start work without a signed agreement.
2. Do not start changed work without an approved Change Request.
3. Collect a deposit for new or higher-risk customers.
4. Define acceptance objectively.
5. Keep reusable IP outside customer ownership.
6. Do not process customer personal data without the correct data terms.
7. Do not accept unlimited liability without specialist legal review.
8. Keep all signed versions and audit trails.
9. Review the contract against insurance.
10. Use a solicitor for high-risk or high-value engagements.

## Official References

- [ICO — Contracts between controllers and processors](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/)
- [UK IPO — Ownership of copyright works](https://www.gov.uk/guidance/ownership-of-copyright-works)
- [GOV.UK — Electronic execution of documents](https://www.gov.uk/government/publications/electronic-execution-of-documents)
- [Small Business Commissioner — Late-payment guidance](https://www.smallbusinesscommissioner.gov.uk/help-and-guidance/interest-calculator/)

## Related Resources

- [Business Documentation Index](README.md)
- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide]({R_GUIDE})
- [All Phase 05 Skills]({R_SKILLS})
- [AIBOS Root Specification]({R_SPEC})

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | UK contracting framework reference for the Business Documentation skills. |
"""
    return "\n".join(fm) + "\n\n" + body


def render_readme() -> str:
    essential = [d for d in DOCS if d["num"] <= 9]
    extended = [d for d in DOCS if d["num"] > 9]

    def rows(docs):
        return "\n".join(
            f"| {d['num']:02d} | [{d['title']}]({file_name(d)}) | {d['binding'].split('.')[0]}. |"
            for d in docs
        )

    fm = [
        "---",
        "id: BIZDOC-INDEX",
        "title: Business Documentation Skills — Index",
        "document_type: Index",
        "category: Business Documentation",
        "phase: Phase 05",
        "owner: Commercial and Contracts Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "jurisdiction: England and Wales",
        "tags:",
        "  - business-documentation",
        "  - skills",
        "  - index",
        "---",
    ]

    body = f"""# Business Documentation Skills — Index

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Phase 05 Skills]({R_SKILLS}) · [UK Framework]({FRAMEWORK_FILE}) · [Source Guide]({R_GUIDE})

## Overview

This skill set turns AIBOS into a capable, UK-compliant business-document generator
for AI, automation, software, SaaS, consulting and implementation engagements. Each
skill is **generate-ready**: reference it and an AI agent (or a person) can produce
the corresponding document, using an embedded blueprint aligned to the
[UK Contracting Framework]({FRAMEWORK_FILE}) and the
[Lemuran Ltd — UK Client Engagement Legal Guide]({R_GUIDE}).

Jurisdiction is **England and Wales**. Lemuran Ltd is used as the default example
supplier; skills use Supplier/Customer placeholders so they are reusable.

## Legal Notice

{LEGAL_NOTICE}

## How to Use These Skills

- **Generate a document:** reference the relevant skill (e.g. "use the Statement of Work skill") and provide the *Inputs Required*; the skill's blueprint drives the draft.
- **Sequence an engagement:** follow the recommended signing order in the [UK Contracting Framework]({FRAMEWORK_FILE}).
- **Stay compliant:** each skill embeds UK legal and compliance notes and a solicitor-review reminder for high-risk work.

## Essential Pack

| # | Document | Binding status |
| --- | --- | --- |
{rows(essential)}

## Extended Pack

| # | Document | Binding status |
| --- | --- | --- |
{rows(extended)}

## Foundational Reference

- [UK Contracting Framework]({FRAMEWORK_FILE}) — architecture, hierarchy, signing order, checklists, IP/payment/liability principles, official references.

## Which Document When

- **Before disclosure:** Mutual NDA.
- **To win the work:** Proposal or Quotation.
- **To set the rules:** Master Services Agreement (+ Business Customer Terms for small jobs).
- **To define the project:** Statement of Work (+ Requirements Specification, Project Plan, Risk Register).
- **When personal data is involved:** Data Processing Agreement (+ Data Mapping Questionnaire, Sub-processor List), or a Data Sharing Agreement for controller-to-controller sharing.
- **For ongoing service:** Service Level Agreement, Support and Maintenance Agreement, Security Schedule.
- **For AI work:** AI and Responsible Use Schedule.
- **During delivery:** Change Request.
- **At completion:** Acceptance Certificate, Invoice, Project Closure Report.
- **For partners/people:** Subcontractor Agreement, Independent Contractor Agreement.
- **For your website/customers:** Website Privacy Notice, Website Cookie Notice, Business Customer Terms, Consumer Terms (if selling to individuals).

## Related Resources

- [Source guide: Lemuran Ltd UK Client Engagement Legal Guide]({R_GUIDE})
- [All Phase 05 Skills]({R_SKILLS})
- [Enterprise Rules]({R_RULES})
- [Enterprise Templates]({R_TEMPLATES})
- [AIBOS Root Specification]({R_SPEC})
- [Enterprise Glossary]({R_GLOSSARY})

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | Initial Business Documentation skill set: 27 generate-ready UK documents + framework. |
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









