#!/usr/bin/env python3
"""Generate the Branding skills set for AIBOS Phase 05.

Creates 02_ARTEFACTS/PHASE_05_SKILLS/Branding/ with:
  * 00_22_IMMUTABLE_LAWS_OF_BRANDING.md  — the 22 immutable laws reference
  * NN_<SKILL>_SKILL.md                  — one detailed doc per branding skill
  * README.md                            — the Branding skills index

Content is competency-oriented (each "skill" is a capability a human or AI agent
applies), grounded in the 22 Immutable Laws of Branding (Al & Laura Ries) and in
current practice: Aaker & Keller brand-equity models, the positioning framework
(POD vs POP), a structured naming methodology, and mental-availability / Category
Entry Point measurement.

Re-run any time; it overwrites only files inside the Branding/ folder.
"""

from __future__ import annotations

import pathlib

REPO = pathlib.Path(__file__).resolve().parents[1]
OUT = REPO / "02_ARTEFACTS" / "PHASE_05_SKILLS" / "Branding"
CREATED = "2026-07-25"
LAWS_FILE = "00_22_IMMUTABLE_LAWS_OF_BRANDING.md"

# --------------------------------------------------------------------------- #
# The 22 Immutable Laws of Branding (Al & Laura Ries) — number, name, summary.
# --------------------------------------------------------------------------- #
LAWS = [
    (1, "Expansion", "A brand's power is inversely proportional to its scope; trying to be everything to everyone weakens it."),
    (2, "Contraction", "A brand becomes stronger when you narrow its focus; specialisation builds leadership."),
    (3, "Publicity", "Brands are born with publicity, not advertising; being first to earn media builds the perception of leadership."),
    (4, "Advertising", "Advertising does not build a brand, it defends one; its job is to maintain a position publicity created."),
    (5, "The Word", "A brand should own a single word or idea in the prospect's mind."),
    (6, "Credentials", "An authentic proof of leadership (the 'credential') makes every other claim believable."),
    (7, "Quality", "Quality matters, but brands are not built on quality alone; they are built on perception and a narrow focus."),
    (8, "The Category", "A leading brand should promote the category, not just the brand; grow the category and you grow the leader."),
    (9, "The Name", "In the long run a brand is nothing more than a name; choose it with care."),
    (10, "Extensions", "The easiest way to destroy a brand is to put its name on everything (line extension dilutes meaning)."),
    (11, "Fellowship", "A brand should welcome competitors; a cluster of brands grows the category for everyone."),
    (12, "The Generic", "One of the fastest routes to failure is giving a brand a generic name; brands need distinctive names."),
    (13, "The Company", "Brands are brands; the company is the company. The brand name should usually lead, not the company name."),
    (14, "Subbrands", "What branding builds, subbranding can destroy; sub-brands fragment focus if used carelessly."),
    (15, "Siblings", "There is a time and a place to launch a second brand — as a distinct sibling, not an extension."),
    (16, "Shape", "A brand's logotype should be designed to fit the eyes — both eyes, favouring a horizontal shape."),
    (17, "Color", "A brand should use a colour that is the opposite of its major competitor's."),
    (18, "Borders", "There are no barriers to global branding; a brand should know no borders."),
    (19, "Consistency", "A brand is built over years by staying consistent; do not change what a brand stands for."),
    (20, "Change", "Brands can be changed, but only rarely, and only very carefully."),
    (21, "Mortality", "No brand lives forever; sometimes euthanasia (a graceful end) is the best option."),
    (22, "Singularity", "The most important aspect of a brand is its single-minded focus on one attribute or idea."),
]
# Note on numbering: the user's brief summarised the laws in a different order and
# wording (Focus, Leader, Opposite, Division, Persuasion, Uniqueness, Eternity).
# We keep the canonical Ries list above and cross-map the brief's concepts in the
# reference document, so both vocabularies resolve to the same principles.

LAW_BY_NUM = {n: name for n, name, _ in LAWS}


def law_ref(num: int) -> str:
    """Render an in-document link to a law heading in the laws reference file."""
    name = LAW_BY_NUM[num]
    anchor = f"law-{num}-the-law-of-{slugify_anchor(name)}"
    return f"[Law {num}: The Law of {name}]({LAWS_FILE}#{anchor})"


def slugify_anchor(text: str) -> str:
    import re
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return s.replace(" ", "-")


# Relative paths from a skill file inside Branding/ (depth: 02_ARTEFACTS/PHASE_05_SKILLS/Branding/).
R_HOME = "../../../README.md"
R_INDEX = "../../../ROOT_INDEX.md"
R_PROMPT = "../../../01_PHASES/PHASE_05_SKILLS_MASTER_PROMPT.md"
R_SPEC = "../../../00_ROOT/AIBOS_ROOT_SPECIFICATION.md"
R_GLOSSARY = "../../../00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md"
R_SKILLS = "../README.md"
R_RULES = "../../PHASE_06_RULES/README.md"
R_CHECKLISTS = "../../PHASE_07_CHECKLISTS/README.md"
R_PLAYBOOKS = "../../PHASE_08_PLAYBOOKS/README.md"
R_TEMPLATES = "../../PHASE_09_TEMPLATES/README.md"
R_KNOWLEDGE = "../../PHASE_10_KNOWLEDGE/README.md"
R_CERT = "../../PHASE_17_CERTIFICATION/README.md"

SKILLS = [
{
  "num": 1, "slug": "FOCUS_AND_SIMPLIFICATION", "title": "Focus and Simplification",
  "discipline": "Brand Strategy",
  "oneliner": "Narrow a brand to a single, memorable idea so it can dominate a space in the customer's mind.",
  "collaborators": "Executive Leadership, Brand Positioning, Category Creation, Product Management",
  "ai_level": "AI-assisted (option analysis, scenario modelling); humans own the sacrifice decision.",
  "laws": [1, 2, 22],
  "definition": [
    "Focus and simplification is the discipline of deliberately narrowing what a brand is about until it stands for one clear idea. It is the foundational branding skill because every other skill depends on there being a single thing to position, name, defend and grow.",
    "The core move is sacrifice: choosing what the brand will *not* do, sell or say. A focused brand can be described in a few words; an unfocused brand needs a paragraph and is forgotten.",
  ],
  "why": [
    "A brand's power is inversely proportional to its scope — breadth dilutes meaning.",
    "Human memory stores brands as a single association; two ideas halve recall.",
    "Focus enables premium pricing, faster word-of-mouth and cheaper marketing.",
    "It is the prerequisite for owning a word (positioning) and for category leadership.",
  ],
  "concepts": [
    ("Sacrifice as strategy", "You cannot be the leader in a category and be everything at once. Decide the one attribute, audience or use-case to win, and consciously give up the rest."),
    ("The contraction test", "If narrowing the offering would make the brand *more* memorable and valuable, it is currently too broad. Keep contracting until the idea is sharp."),
    ("Single-minded proposition", "Reduce the brand to one word or short phrase a stranger could repeat after one exposure. If it needs a list, it is not yet focused."),
  ],
  "steps": [
    "Inventory everything the brand currently claims, sells and serves; list every audience and attribute.",
    "Score each item on distinctiveness (can we own it?) and demand (do buyers care?).",
    "Choose ONE attribute/idea to be famous for; mark everything else as supporting or to be dropped.",
    "Write the single-minded proposition in <=7 words and pressure-test recall with people outside the company.",
    "Realign portfolio, messaging and roadmap to the chosen focus; retire or spin off what does not fit.",
    "Guard the focus over time — treat every new request to broaden as a threat to be justified.",
  ],
  "techniques": [
    "'One word' exercise: force the team to defend a single word before any adjectives are added.",
    "Subtraction workshops: start from zero and add back only what is essential.",
    "Category-of-one framing: describe the brand so narrowly that it has no direct substitute.",
  ],
  "antipatterns": [
    "Line-extending into adjacent categories to chase short-term revenue.",
    "Adding a second 'pillar' because a stakeholder felt left out.",
    "Confusing a long feature list with a value proposition.",
  ],
  "metrics": [
    "Unaided recall of the brand's single attribute.",
    "Message consistency score across channels (variance in claimed attributes).",
    "Price premium vs unfocused competitors.",
  ],
  "tools": [
    "Positioning canvas / one-page brand strategy",
    "Perceptual maps",
    "AI summarisation to detect message drift across assets",
  ],
  "ai": "AI agents can rapidly cluster the brand's existing claims, surface where messaging has drifted, model the trade-offs of each focus option, and draft candidate single-minded propositions. The sacrifice decision itself stays with human leadership because it is a strategic bet, not a data lookup.",
  "example": "A cloud tool marketed as an 'all-in-one platform for teams' had flat recall. Contracting the promise to 'the fastest way to ship a status page' made it the default in that niche, after which adjacent features were reintroduced as supporting evidence — not competing headlines.",
},
{
  "num": 2, "slug": "BRAND_POSITIONING", "title": "Brand Positioning",
  "discipline": "Brand Strategy",
  "oneliner": "Establish a distinct, defensible place in the customer's mind that no competitor can credibly claim.",
  "collaborators": "Focus and Simplification, Differentiation, Competitor Analysis, Product Marketing",
  "ai_level": "AI-assisted (research synthesis, draft statements); humans validate defensibility.",
  "laws": [5, 22, 8],
  "definition": [
    "Brand positioning is the deliberate act of owning a single idea, word or concept in the prospect's mind relative to the alternatives. It is not a tagline or a logo — it is the one thought people reach for when they compare you to everyone solving the same problem.",
    "A position is captured in an internal positioning statement and then expressed consistently across every touchpoint. Positioning is subtraction, not addition: you win by choosing one point of difference, not by listing many.",
  ],
  "why": [
    "The mind ranks brands; owning a word means being the default choice for that need.",
    "It aligns product, marketing, sales and partnerships on one market position.",
    "It converts a commodity into a preference and supports pricing power.",
    "It prevents message drift as the organisation and channels multiply.",
  ],
  "concepts": [
    ("The positioning statement", "Use the standard structure: *For [target audience] who [need/opportunity], [brand] is the [frame of reference] that [point of difference] because [reasons to believe].* It is an internal alignment tool, not an ad headline."),
    ("Point of difference vs point of parity", "Points of parity (POP) are table-stakes you must have to be credible; points of difference (POD) are what you uniquely own. Build the position entirely from PODs and meet POPs quietly."),
    ("Own a word", "Following the Law of the Word, aim to own one concept (safety, speed, overnight, search). If a competitor already owns it, do not fight for it — find the opposite (see Competitor Analysis)."),
    ("Frame of reference", "The category you ask to be judged in changes everything; choosing (or creating) the right frame is half the positioning."),
  ],
  "steps": [
    "Define the specific target segment you serve best and the job they are hiring the brand for.",
    "Choose the frame of reference (the category customers compare you within).",
    "List category points of parity; confirm you credibly meet them.",
    "Select ONE point of difference that is true, distinctive and hard to copy.",
    "Gather concrete reasons to believe (data, credentials, proof points, methodology).",
    "Draft the positioning statement; stress-test it against each competitor for defensibility and vacancy.",
    "Translate the position into a messaging hierarchy and roll it out consistently.",
  ],
  "techniques": [
    "Perceptual mapping to find an unoccupied, valuable space.",
    "'Only' test: can you say 'the only X that Y'? If not, the POD is weak.",
    "Laddering from features -> functional benefit -> emotional benefit to find the ownable idea.",
  ],
  "antipatterns": [
    "Leading with points of parity ('reliable', 'easy to use') as if they were differentiators.",
    "Positioning on a benefit a stronger competitor already owns.",
    "Writing a positioning statement and never enforcing it in messaging.",
    "Different, conflicting positions for different segments (a sign the brand is stretched too far).",
  ],
  "metrics": [
    "Unaided association between the brand and its chosen word/attribute.",
    "Win/loss reasons citing the point of difference.",
    "Consideration and preference vs the frame-of-reference competitors.",
  ],
  "tools": [
    "Positioning statement worksheet",
    "Perceptual maps",
    "Message house / messaging hierarchy",
    "Keller CBBE and Aaker equity models for diagnosis",
  ],
  "ai": "AI can synthesise reviews, forums and sales calls to reveal the language customers actually use, map competitor claims to expose unoccupied space, and generate and critique candidate positioning statements. Humans must verify the chosen POD is genuinely defensible and deliverable — AI over-generates plausible-but-generic claims.",
  "example": "A backup product competing on 'reliable storage' (a parity claim) repositioned as 'the backup that restores in one click' — a single, testable point of difference — and reframed the category from 'storage' to 'recovery', where it could lead.",
},
{
  "num": 3, "slug": "NAMING_EXPERTISE", "title": "Naming Expertise",
  "discipline": "Brand Identity",
  "oneliner": "Craft distinctive, memorable, legally defensible names that carry the brand's essence.",
  "collaborators": "Brand Positioning, Legal/Trademark Counsel, Product Management, Global Brand Building",
  "ai_level": "AI-assisted for generation; NEVER for legal/availability verification (hallucination risk).",
  "laws": [9, 12, 5],
  "definition": [
    "Naming expertise is the structured practice of creating brand, product and category names that are distinctive, easy to say and spell, and clearable for trademark and domain use. In the long run a brand is a name, so the choice compounds for decades.",
    "Good naming is a risk-aware methodology, not a vote on favourites. It moves from strategy to generation to rigorous screening (linguistic, trademark, digital) to a scored selection.",
  ],
  "why": [
    "The name is the single most permanent brand asset and the hook for all recall.",
    "Generic names cannot be owned or defended; distinctive names can become category-defining.",
    "A poor name creates permanent legal, linguistic and search-visibility costs.",
    "In AI-mediated discovery, a distinctive name is easier for models to attribute and cite.",
  ],
  "concepts": [
    ("Naming types", "Descriptive, evocative/suggestive, invented (portmanteau/coined), lexical (compound/altered spelling), acronymic, geographic, and founder names. Evocative, compound and invented names generally win on distinctiveness and trademark viability."),
    ("Avoid the generic", "Per the Law of the Generic, a name that merely describes the category cannot separate the brand from competitors; distinctiveness is the point."),
    ("Sound symbolism", "Phonetics carry meaning — hard consonants signal strength, soft fricatives signal ease; syllable count affects memorability (1-3 syllables preferred)."),
    ("Screening gates", "Every candidate must pass memorability, pronounceability, cross-language safety, domain/social availability and trademark clearance before selection."),
  ],
  "steps": [
    "Write a naming brief: positioning, audience, desired feeling, constraints, names you admire and avoid.",
    "Generate in linguistic territories (descriptive, metaphorical, invented, compound) — breadth first.",
    "Categorise and score candidates on memorability, processing fluency, category fit and scalability (1-5).",
    "Screen linguistically across target-market languages for negative connotations.",
    "Run trademark clearance (USPTO/WIPO and relevant registers) and check domains and social handles.",
    "Validate with a say-and-recall test on real prospects (can they spell it a day later?).",
    "Select, then immediately secure domain, handles and file for trademark protection.",
  ],
  "techniques": [
    "Word banks, roots, and morpheme mashing for invented names.",
    "Two-axis competitor map (name type x construction) to find whitespace.",
    "Native-speaker review for each priority market.",
  ],
  "antipatterns": [
    "Choosing a descriptive/generic name that cannot be trademarked.",
    "Skipping trademark clearance or relying on AI for legal verification.",
    "Group voting instead of objective scoring.",
    "Names that only work in one language or that mis-spell easily.",
  ],
  "metrics": [
    "Recall and spell-back accuracy in validation tests.",
    "Trademark clearance rate and class coverage.",
    "Domain/handle availability at launch.",
  ],
  "tools": [
    "USPTO / WIPO Global Brand Database",
    "Domain and social-handle checkers",
    "Linguistic screening (native speakers, multi-language checks)",
    "AI ideation for candidate generation (not verification)",
  ],
  "ai": "AI is excellent at generating large, varied candidate lists within defined linguistic territories and at flagging obvious phonetic problems. It must not be trusted for trademark, availability or legal conclusions — those require authoritative databases and qualified counsel. Treat AI output as raw material to be screened.",
  "example": "Instead of 'CloudInvoice' (descriptive, unclearable), a structured process produced an invented compound that cleared trademark in the relevant classes, secured the exact-match domain, and scored highest on a next-day spell-back test.",
},
{
  "num": 4, "slug": "MESSAGING_CONSISTENCY", "title": "Consistency in Messaging",
  "discipline": "Brand Communications",
  "oneliner": "Keep a coherent message over time and across channels to build familiarity, trust and recall.",
  "collaborators": "Brand Positioning, Content Strategist, Advertising, Perception Management",
  "ai_level": "Heavily AI-assisted (drift detection, on-brand drafting) with human editorial control.",
  "laws": [19, 20, 5],
  "definition": [
    "Consistency in messaging is the discipline of expressing the same core idea, voice and visual identity everywhere and over years, resisting the urge to change what the brand stands for. Brands are built by repetition, not variety.",
    "Consistency does not mean saying the identical sentence forever; it means every expression rolls up to one position, tone and set of distinctive assets, so exposures compound instead of competing.",
  ],
  "why": [
    "Familiarity is built by repetition; inconsistency resets the learning curve.",
    "Distinctive, consistent assets (colour, logo, voice, tagline) drive mental availability.",
    "Consistency lowers cost — each impression reinforces the last.",
    "Trust depends on the brand behaving predictably across every touchpoint.",
  ],
  "concepts": [
    ("Distinctive brand assets", "Colours, logos, characters, sounds and phrases that trigger the brand without the name. Protect and repeat them; do not refresh them casually."),
    ("Message house", "A single core message supported by 3-4 pillars and proof points, cascaded to every channel so all teams say the same thing in their own words."),
    ("Consistency vs change", "Per the laws of Consistency and Change, change the brand rarely and only with strong evidence; consumer-driven, gradual, and rare."),
    ("Voice and tone system", "Define voice (constant personality) separately from tone (varies by context) so writers stay on-brand while adapting to the moment."),
  ],
  "steps": [
    "Codify the core message, pillars and proof points in a message house.",
    "Define voice, tone, and the distinctive verbal/visual assets in brand guidelines.",
    "Create channel-specific templates that inherit from the message house.",
    "Train humans and configure AI assistants with the guidelines as source of truth.",
    "Audit assets regularly for drift; correct deviations quickly.",
    "Change the position only through a deliberate, evidence-based, rarely-used process.",
  ],
  "techniques": [
    "Brand guidelines + do/don't examples for voice.",
    "Automated 'on-brand' linting of copy against the message house.",
    "Asset libraries and locked templates to prevent one-off reinvention.",
  ],
  "antipatterns": [
    "Rebranding or re-messaging with every new campaign or CMO.",
    "Letting each channel/team invent its own claims and tone.",
    "Refreshing distinctive assets (logo/colour) without evidence, resetting recognition.",
  ],
  "metrics": [
    "Distinctive-asset recognition (linkage of asset to brand).",
    "Message consistency score across audited assets.",
    "Brand-search volume and unaided salience trend over time.",
  ],
  "tools": [
    "Brand guidelines / design system",
    "Message house",
    "DAM (digital asset management) and locked templates",
    "AI copy review against brand rules",
  ],
  "ai": "AI can enforce consistency at scale: draft on-brand copy from the message house, review thousands of assets for tone/claim drift, and flag unauthorised deviations. Editorial judgement and the decision to *change* the message remain human — AI optimises for local fluency and will happily drift if unconstrained.",
  "example": "A company running five agencies had five voices. Publishing a message house and an AI copy-reviewer wired to it cut claim variance sharply, and unaided brand salience rose over the following year without new spend.",
},
{
  "num": 5, "slug": "STRATEGIC_BRAND_EXTENSION", "title": "Strategic Brand Extension",
  "discipline": "Brand Architecture",
  "oneliner": "Decide when and how to extend a brand into new products or markets without diluting its core.",
  "collaborators": "Executive Leadership, Brand Positioning, Product Management, Portfolio/Finance",
  "ai_level": "AI-assisted (fit scoring, cannibalisation modelling); humans own architecture decisions.",
  "laws": [10, 14, 15, 2],
  "definition": [
    "Strategic brand extension is the disciplined evaluation of whether to stretch an existing brand into a new category, add a sub-brand, or launch a distinct sibling brand. The default bias is caution: line extension is the most common way strong brands are weakened.",
    "The skill is choosing the right brand architecture — branded house, house of brands, endorsed brands, or sub-brands — so growth adds value instead of blurring the core idea.",
  ],
  "why": [
    "Extending a focused brand into unrelated space erodes the single idea that made it strong.",
    "The right architecture lets a company grow revenue without cannibalising brand meaning.",
    "Sometimes a new category deserves a *new* brand (a sibling), not a stretched one.",
    "Poor extensions confuse customers and hand focus to specialist competitors.",
  ],
  "concepts": [
    ("Brand architecture models", "Branded house (one master brand), house of brands (independent brands), endorsed brands, and sub-brands. Choose based on how related the offerings are and the risk of diluting focus."),
    ("Line extension trap", "Per the Law of Extensions, putting the name on everything trades long-term brand strength for short-term sales; the leader that line-extends invites a focused challenger."),
    ("Sibling strategy", "Per the Law of Siblings, launch a second, distinct brand when the new category or audience is genuinely different — keep each sibling narrowly focused."),
    ("Sub-brand caution", "Per the Law of Subbrands, sub-brands can segment a market but must not confuse or contradict the master brand's core idea."),
  ],
  "steps": [
    "Clarify the master brand's single idea and the boundaries it implies.",
    "Assess the opportunity's fit: does it reinforce or contradict that idea?",
    "Model cannibalisation, halo and dilution risk, not just incremental revenue.",
    "Choose the architecture: extend, endorse, sub-brand, or launch a sibling/new brand.",
    "If extending, define guardrails that keep the core promise intact.",
    "If a new brand, apply the full positioning and naming disciplines to the sibling.",
    "Review post-launch for erosion of the master brand's key associations.",
  ],
  "techniques": [
    "Fit scoring: rate each opportunity on strategic, perceptual and operational fit.",
    "Architecture decision tree (relatedness x risk).",
    "Pre/post brand-association tracking to detect dilution.",
  ],
  "antipatterns": [
    "Reflexive line extension to hit a quarterly number.",
    "Stretching the master brand into a category it has no permission to enter.",
    "Proliferating sub-brands until the portfolio is incoherent.",
  ],
  "metrics": [
    "Master-brand association stability before/after extension.",
    "Incremental vs cannibalised revenue.",
    "Customer clarity on what each brand stands for.",
  ],
  "tools": [
    "Brand architecture map",
    "Fit-scoring rubric",
    "Portfolio and cannibalisation models",
  ],
  "ai": "AI can score portfolio fit, simulate cannibalisation and halo effects, and monitor whether an extension is eroding the master brand's associations in tracking data. The architecture choice is a strategic, often irreversible bet that must stay with human leadership.",
  "example": "A premium safety-focused brand was tempted to badge a budget line under the same name. Modelling showed dilution of the 'safety' association; leadership launched a separately named sibling instead, protecting the core while capturing the new segment.",
},
{
  "num": 6, "slug": "CATEGORY_LEADERSHIP", "title": "Creating Category Leadership",
  "discipline": "Brand Strategy",
  "oneliner": "Become and stay the reference brand in a category by leading and growing the category itself.",
  "collaborators": "Category Creation, Publicity, Advertising, Executive Leadership",
  "ai_level": "AI-assisted (market/share analysis, content scale); humans set leadership strategy.",
  "laws": [8, 6, 4],
  "definition": [
    "Category leadership is the skill of establishing a brand as the recognised leader of a category and then defending that position. The leader benefits from a self-reinforcing perception: being seen as #1 becomes the credential that keeps it #1.",
    "Leaders win by promoting the category, not only themselves. Growing the whole category grows the leader most, while advertising is used to defend, not create, the position.",
  ],
  "why": [
    "Buyers equate leadership with quality and safety, so the leader is the default choice.",
    "Leadership is the strongest credential a brand can own (see Perception Management).",
    "Growing the category expands the leader's absolute volume more than any rival's.",
    "A defended leadership position compounds over time and deters challengers.",
  ],
  "concepts": [
    ("Promote the category", "Per the Law of the Category, a leader should market the category ('why do X at all') because it captures the largest share of new demand it creates."),
    ("Leadership as credential", "'The #1 X' is a proof point competitors cannot copy; per the Law of Credentials, it makes every other claim believable."),
    ("Defend, do not rest", "Use advertising and continuous innovation to defend leadership; the leader that stops investing invites the challenger's 'opposite' move."),
    ("First-mover and mind-share", "Being first into the mind (not always the market) tends to secure leadership; if you are not first, create a sub-category you can lead."),
  ],
  "steps": [
    "Define the category you can realistically lead (narrow it until you can).",
    "Claim and substantiate the leadership credential (share, firsts, adoption, authority).",
    "Invest in growing the category — educate the market on the problem and solution.",
    "Publish authoritative content and data so the brand becomes the category's reference source.",
    "Defend with consistent advertising, innovation and rapid response to challengers.",
    "Track category growth and relative share; reinvest to hold the lead.",
  ],
  "techniques": [
    "Category-defining content, benchmarks and 'state of' reports.",
    "Own the category's vocabulary and standards.",
    "Analyst/press relations to be cited as the leader.",
  ],
  "antipatterns": [
    "Marketing only the brand while ignoring category education.",
    "Claiming leadership without a credible, checkable credential.",
    "Complacency — under-investing once leadership feels secure.",
  ],
  "metrics": [
    "Relative market share and share of category search.",
    "Category growth rate (and the brand's capture of it).",
    "Analyst/press citations as category leader; share of model (AI citations).",
  ],
  "tools": [
    "Market share and share-of-voice tracking",
    "Category thought-leadership content engine",
    "Analyst relations programme",
  ],
  "ai": "AI can quantify category share and growth, monitor who is cited as leader across media and AI answer engines, and scale authoritative category content. Deciding which category to lead and how aggressively to defend it is a leadership call informed by that analysis.",
  "example": "A monitoring vendor grew faster by publishing the industry's benchmark 'incident response' report every year; owning the category's reference data made it the brand analysts and buyers named first.",
},
{
  "num": 7, "slug": "PUBLICITY_AND_MEDIA_RELATIONS", "title": "Publicity and Media Relations",
  "discipline": "Brand Communications",
  "oneliner": "Launch and build brands through earned media and third-party credibility, not paid claims.",
  "collaborators": "Category Creation, Perception Management, Content Strategist, Executive Leadership",
  "ai_level": "AI-assisted (media monitoring, drafting, targeting); humans own relationships and narrative.",
  "laws": [3, 6, 4],
  "definition": [
    "Publicity and media relations is the skill of earning third-party coverage and conversation to create the perception of leadership, especially at launch. Brands are born with publicity: what others say about you is far more credible than what you say about yourself.",
    "It sequences correctly with advertising — publicity builds the position first; advertising defends it later. Being first with a genuinely new story is the raw material of publicity.",
  ],
  "why": [
    "Earned coverage carries credibility that paid advertising cannot buy.",
    "Publicity creates the initial perception of leadership for a new brand or category.",
    "Media mentions are now a discovery signal for search engines and AI answer engines.",
    "A strong launch narrative compounds into analyst, investor and customer confidence.",
  ],
  "concepts": [
    ("Publicity before advertising", "Per the Law of Publicity, spend the launch window earning coverage; per the Law of Advertising, switch to paid media to defend the position once publicity wanes."),
    ("Newsworthiness = firstness", "Media cover what is new or first; a first-in-category story, surprising data, or a strong point of view earns attention."),
    ("Credential building", "Coverage, awards and notable customers become the credentials that make future claims believable."),
    ("Owned narrative + earned amplification", "Control the core story (owned) and equip journalists, analysts and creators to amplify it (earned)."),
  ],
  "steps": [
    "Craft a newsworthy angle — a first, a bold point of view, or proprietary data.",
    "Build a target map of journalists, analysts, podcasters and creators in the category.",
    "Prepare the press kit, spokespeople and proof points.",
    "Sequence a launch: exclusives, embargoes, then broad outreach.",
    "Amplify earned coverage through owned and social channels.",
    "Convert momentum into durable credentials (quotes, logos, awards).",
    "Transition to advertising to defend the position once the news cycle fades.",
  ],
  "techniques": [
    "Data-driven PR (original research as the hook).",
    "Executive thought leadership and commentary.",
    "Newsjacking relevant category moments responsibly.",
  ],
  "antipatterns": [
    "Trying to launch a brand with advertising before earning any credibility.",
    "Press releases with no genuine news.",
    "Chasing vanity coverage unrelated to the brand's single idea.",
  ],
  "metrics": [
    "Quality earned mentions and share of voice in target media.",
    "Message pull-through (coverage that repeats the brand's key idea).",
    "Referral traffic and branded search lift after coverage.",
  ],
  "tools": [
    "Media monitoring and PR CRM",
    "Original-research / data-PR engine",
    "AI drafting and journalist-targeting assistance",
  ],
  "ai": "AI accelerates media monitoring, identifies relevant journalists and outlets, drafts tailored pitches, and tracks message pull-through across coverage. The relationships, the narrative judgement and the on-record spokesperson remain human.",
  "example": "A fintech launched with an original 'state of subscriptions' data study rather than a product press release; the surprising numbers earned tier-one coverage that positioned it as the category's authority before any ad ran.",
},
{
  "num": 8, "slug": "ADVERTISING_AND_PROMOTION", "title": "Advertising and Promotion",
  "discipline": "Brand Communications",
  "oneliner": "Use paid media to defend and reinforce an established position, sustaining salience over time.",
  "collaborators": "Messaging Consistency, Publicity, Growth Marketing, Perception Management",
  "ai_level": "Heavily AI-assisted (targeting, creative variants, optimisation) with human brand control.",
  "laws": [4, 8, 19],
  "definition": [
    "Advertising and promotion is the skill of deploying paid media to defend a position that publicity established and to keep the brand mentally available. Advertising rarely builds a brand from nothing; its job is maintenance, reinforcement and reach.",
    "Effective advertising is consistent (same core idea and distinctive assets over years) and balances long-term brand building with short-term activation — the widely used 60/40 split.",
  ],
  "why": [
    "Once publicity fades, advertising is what keeps the position defended and top-of-mind.",
    "Consistent creative compounds recognition through distinctive assets.",
    "Reach builds mental availability across category entry points; activation converts demand.",
    "It insulates the leader against challengers and share erosion.",
  ],
  "concepts": [
    ("Defend, do not create", "Per the Law of Advertising, use paid media to hold the ground publicity won, not to invent a position advertising cannot sustain."),
    ("Brand vs activation (60/40)", "Balance long-term brand-building reach against short-term response; the evidence-based default is roughly 60% brand, 40% activation."),
    ("Distinctive assets in every ad", "Consistently use the brand's colours, logo, characters and phrases so each impression reinforces recognition."),
    ("Reach over frequency for growth", "Broad, consistent reach across light buyers grows brands more than narrow, high-frequency targeting."),
  ],
  "steps": [
    "Confirm the position and distinctive assets before buying media.",
    "Set the brand/activation split and per-channel roles.",
    "Develop consistent creative expressing the single idea with distinctive assets.",
    "Plan for broad, efficient reach across relevant category entry points.",
    "Run activation to capture in-market demand.",
    "Measure incrementality and brand lift, not just last-click.",
    "Iterate creative variants while holding the core idea constant.",
  ],
  "techniques": [
    "Media mix modelling and incrementality testing.",
    "Creative testing of variants within a fixed brand frame.",
    "Always-on brand reach plus bursts of activation.",
  ],
  "antipatterns": [
    "Expecting advertising to build a brand with no underlying position.",
    "Chasing short-term ROAS at the expense of long-term brand building.",
    "Reinventing creative every campaign, wasting accumulated recognition.",
  ],
  "metrics": [
    "Brand lift (awareness, association, consideration).",
    "Incremental conversions vs holdout, not just attributed clicks.",
    "Reach across category entry points and distinctive-asset attribution.",
  ],
  "tools": [
    "Media mix modelling / incrementality platforms",
    "Creative testing tools",
    "Programmatic and channel platforms with brand-safety controls",
  ],
  "ai": "AI optimises targeting, budget allocation and bid strategy, generates and tests creative variants at scale, and forecasts incrementality. Guardrails are essential: constrain AI to the approved position and distinctive assets so optimisation does not erode brand consistency.",
  "example": "After a PR-led launch, a SaaS brand shifted to an always-on 60/40 plan, kept one visual system across all ads for two years, and measured incremental sign-ups against a geo holdout rather than last-click ROAS.",
},
{
  "num": 9, "slug": "PERCEPTION_MANAGEMENT", "title": "Perception Management",
  "discipline": "Brand Strategy",
  "oneliner": "Shape and defend how customers perceive quality, credibility and relevance — perception is the brand.",
  "collaborators": "Brand Positioning, Publicity, Messaging Consistency, Customer Experience",
  "ai_level": "AI-assisted (sentiment/perception tracking); humans own credibility and ethics.",
  "laws": [7, 6, 5],
  "definition": [
    "Perception management is the skill of influencing what customers believe about a brand's quality, authority and relevance. Brands live in the mind: perceived quality drives choice and pricing more directly than measured quality alone.",
    "It works by pairing a narrow claim with credible proof (credentials), then reinforcing it consistently so the perception becomes the accepted reality of the category.",
  ],
  "why": [
    "Buyers decide on perceived quality; the best product can lose to a better-perceived one.",
    "Credentials (leadership, heritage, notable customers, authority) make claims believable.",
    "Perception, once established and reinforced, is durable and hard for rivals to dislodge.",
    "Managing perception protects premium pricing and resilience in downturns.",
  ],
  "concepts": [
    ("Perceived vs actual quality", "Per the Law of Quality, real quality is necessary but not sufficient; narrow focus plus a credible perception is what builds the brand."),
    ("Credentials engine", "Per the Law of Credentials, leadership claims, authority content, awards and marquee customers are the proof that make perception stick."),
    ("Own a quality cue", "Attach the brand to one concrete, believable proof of quality (a specialisation, a guarantee, a signature detail) rather than generic 'high quality' claims."),
    ("Consistency reinforces perception", "Every consistent, on-brand experience deepens the perception; every inconsistency erodes it."),
  ],
  "steps": [
    "Define the specific perception you want to own (the single quality cue).",
    "Inventory and build credentials that substantiate it.",
    "Align product, service and communications so experience matches the claim.",
    "Reinforce the perception consistently across every touchpoint.",
    "Monitor perception vs reality and close gaps quickly.",
    "Defend against misperception and competitor framing.",
  ],
  "techniques": [
    "Signature proof points and demonstrable specialisation.",
    "Third-party validation (reviews, certifications, authority content).",
    "Experience design that dramatises the quality cue.",
  ],
  "antipatterns": [
    "Claiming quality without proof, creating a perception/reality gap.",
    "Over-promising in marketing while under-delivering in experience.",
    "Chasing many quality attributes instead of owning one credible cue.",
  ],
  "metrics": [
    "Perceived-quality and credibility scores in tracking studies.",
    "Sentiment and review ratings vs competitors.",
    "Price premium sustained vs the category.",
  ],
  "tools": [
    "Brand/perception tracking studies",
    "Social listening and review analytics",
    "Keller CBBE 'judgments/feelings' diagnostics",
  ],
  "ai": "AI can continuously track perception through social listening, review mining and survey analysis, and detect emerging perception/reality gaps early. The obligation to make the perception *true* — real credentials, real experience, ethical claims — is a human responsibility.",
  "example": "A consultancy replaced generic 'trusted advisor' language with a single credential — publishing the outcomes of 200 engagements — which moved perceived credibility scores more than any brand campaign had.",
},
{
  "num": 10, "slug": "COLLABORATIVE_NETWORKING_FELLOWSHIP", "title": "Collaborative Networking (Fellowship)",
  "discipline": "Brand Strategy",
  "oneliner": "Welcome competitors and build alliances so the whole category grows and every member benefits.",
  "collaborators": "Category Leadership, Category Creation, Partnerships, Ecosystem/Platform teams",
  "ai_level": "AI-assisted (ecosystem mapping, partner analytics); humans own alliances and trust.",
  "laws": [11, 8, 18],
  "definition": [
    "Collaborative networking — the Law of Fellowship — is the counter-intuitive skill of welcoming competition and building alliances because a cluster of brands attracts more total demand than any brand alone. A healthy, contested category signals legitimacy and gives buyers confidence to choose.",
    "It includes ecosystems, integration partnerships, co-marketing, standards bodies and marketplaces that make the whole category more valuable, with the leader capturing the largest share of the growth.",
  ],
  "why": [
    "A category with visible competition looks legitimate and grows faster than a monopoly of one.",
    "Clusters enable comparison shopping, which increases total category demand.",
    "Alliances and integrations expand reach and category entry points.",
    "Ecosystems create switching costs and defensibility around the brand.",
  ],
  "concepts": [
    ("Grow the pie, not just the slice", "Per the Law of Fellowship, welcoming competitors grows the category; the leader benefits most from a bigger pie."),
    ("Ecosystem and integrations", "Partnerships, integrations and marketplaces multiply the situations in which the brand is relevant and easy to buy."),
    ("Standards and fellowship", "Contributing to open standards and category bodies builds trust and expands the addressable market."),
    ("Co-branding fit", "Alliances strengthen a brand only when partners are aligned in values and quality; mismatch dilutes both."),
  ],
  "steps": [
    "Map the category ecosystem: complements, competitors, channels and standards.",
    "Identify where collaboration grows total demand or credibility.",
    "Prioritise partnerships and integrations by strategic and brand fit.",
    "Establish co-marketing and integration programmes with clear brand rules.",
    "Participate in or seed category standards and communities.",
    "Measure category growth and the brand's capture of it, not just direct rivalry.",
  ],
  "techniques": [
    "Integration/partner marketplaces.",
    "Co-branded research and events.",
    "Open standards contribution and community building.",
  ],
  "antipatterns": [
    "Treating every competitor as a zero-sum enemy in a nascent category.",
    "Co-branding with misaligned partners that dilute quality perception.",
    "Building a walled garden that stunts category growth.",
  ],
  "metrics": [
    "Total category growth and the brand's share of it.",
    "Number and quality of active integrations/partners.",
    "Partner-sourced pipeline and ecosystem engagement.",
  ],
  "tools": [
    "Ecosystem/partner maps",
    "Partner and marketplace platforms",
    "Co-marketing frameworks and brand-usage guidelines",
  ],
  "ai": "AI can map the ecosystem, score partner fit, and analyse where collaboration expands category entry points and demand. Trust, negotiation and alliance strategy are inherently human.",
  "example": "An early automation vendor published an open integration framework and promoted rivals' interoperability; the category's credibility rose, adoption accelerated, and the vendor — as the hub — captured the largest share of the growth.",
},
{
  "num": 11, "slug": "GLOBAL_BRAND_BUILDING", "title": "Building a Global Brand",
  "discipline": "Brand Strategy",
  "oneliner": "Carry one consistent brand idea across borders while adapting expression to local context.",
  "collaborators": "Messaging Consistency, Naming Expertise, Regional Marketing, Legal/Trademark",
  "ai_level": "AI-assisted (localisation, cross-market monitoring); humans own cultural judgement.",
  "laws": [18, 19, 13],
  "definition": [
    "Building a global brand is the skill of taking one brand idea worldwide, keeping the core positioning and distinctive assets constant while adapting language, channels and cultural nuance locally. There are no borders to a strong idea — but there are local realities to respect.",
    "The discipline balances global consistency (one position, one identity) with local relevance ('glocalisation'), and manages the practicalities of naming, trademarks and linguistics across markets.",
  ],
  "why": [
    "A single global idea compounds recognition and efficiency across markets.",
    "Perceived origin and authenticity can be part of the brand's appeal.",
    "Inconsistent country-by-country brands waste equity and confuse global customers.",
    "Digital and AI-mediated discovery are inherently borderless.",
  ],
  "concepts": [
    ("No borders for a strong idea", "Per the Law of Borders, a genuinely strong positioning travels; do not assume a market is 'too different' to grasp the core idea."),
    ("Global core, local expression", "Keep positioning, name and distinctive assets constant; adapt language, examples, imagery and channels to each market."),
    ("Linguistic and legal fit", "Names and taglines must be checked for meaning and trademark clearance in every target market (see Naming Expertise)."),
    ("Consistency across markets", "Per the Law of Consistency, resist letting each region reinvent the brand; govern with global guidelines."),
  ],
  "steps": [
    "Codify the global brand core (position, identity, distinctive assets, guidelines).",
    "Assess each priority market for linguistic, cultural and legal fit.",
    "Decide what is fixed globally vs adaptable locally (the 'freedom within a frame').",
    "Localise expression (language, imagery, channels) without changing the core idea.",
    "Clear names/taglines for trademark and meaning in each market.",
    "Govern with global guidelines and regional enablement; monitor consistency.",
  ],
  "techniques": [
    "Transcreation (not literal translation) of key messages.",
    "Global brand guidelines with local adaptation playbooks.",
    "Market-entry brand and trademark clearance checklists.",
  ],
  "antipatterns": [
    "Fragmenting into inconsistent country brands with different positions.",
    "Literal translation that loses or distorts meaning.",
    "Ignoring local trademark/linguistic risks until after launch.",
  ],
  "metrics": [
    "Cross-market consistency of position and distinctive assets.",
    "Awareness/consideration by market vs plan.",
    "Localisation quality and time-to-market for new regions.",
  ],
  "tools": [
    "Global brand guidelines + local playbooks",
    "Transcreation and localisation workflows",
    "Multi-market trademark clearance (WIPO/local registers)",
  ],
  "ai": "AI accelerates localisation, transcreation and cross-market consistency monitoring, and flags linguistic risks in candidate names and messages. Cultural nuance, local partnerships and final trademark decisions require human and expert judgement.",
  "example": "A brand kept one global positioning and colour system, transcreated (not translated) its tagline for each market, and cleared the name in every target register before entry — preserving one identity worldwide while reading as native locally.",
},
{
  "num": 12, "slug": "BRAND_MONITORING_AND_ADAPTATION", "title": "Brand Monitoring and Adaptation",
  "discipline": "Brand Governance",
  "oneliner": "Track perception, competitors and trends, and adapt carefully without compromising the core identity.",
  "collaborators": "Perception Management, Competitor Analysis, Messaging Consistency, Insights/Analytics",
  "ai_level": "Heavily AI-assisted (always-on tracking, anomaly detection) with human interpretation.",
  "laws": [19, 20, 21],
  "definition": [
    "Brand monitoring and adaptation is the skill of continuously measuring how a brand is perceived and performing, watching competitors and market shifts, and making measured adjustments that keep the brand relevant without abandoning what it stands for.",
    "It is the sensing system for every other branding skill: it detects drift, dilution, emerging category entry points and threats early enough to act while adaptation is still cheap and reversible.",
  ],
  "why": [
    "Perception changes even when the brand does not; you cannot manage what you do not measure.",
    "Early detection of drift or threats keeps corrections small and low-risk.",
    "Markets and category entry points evolve; relevance must be actively maintained.",
    "Data disciplines the urge to change on a whim (see Change Management).",
  ],
  "concepts": [
    ("Modern brand-health metrics", "Beyond awareness and NPS, track mental availability via Category Entry Points: Mental Market Share, Mental Penetration, Network Size and Share of Mind, which predict real market share."),
    ("Distinctive-asset tracking", "Measure how strongly assets (colour, logo, phrases) link back to the brand, and watch for erosion."),
    ("Share of model", "Track how often AI answer engines cite the brand for category prompts — an emerging discovery metric."),
    ("Adapt within the frame", "Per the laws of Consistency and Change, adapt expression and tactics continuously but change the core position rarely and deliberately."),
  ],
  "steps": [
    "Define the brand-health metric set (equity + mental availability + distinctive assets + share of model).",
    "Identify the category entry points that matter and baseline the brand against them.",
    "Stand up always-on tracking (surveys, social listening, search, AI-citation checks).",
    "Review dashboards on a cadence; separate signal from noise.",
    "Diagnose drift, dilution or new opportunities; decide adapt vs hold.",
    "Feed insights into positioning, messaging and portfolio decisions.",
  ],
  "techniques": [
    "Quarterly brand tracker including light and non-buyers.",
    "Social listening and review mining for perception shifts.",
    "Competitor and category-entry-point monitoring.",
  ],
  "antipatterns": [
    "Optimising vanity metrics (aided awareness, NPS) that do not predict growth.",
    "Over-reacting to noise with knee-jerk brand changes.",
    "Monitoring only current buyers and missing the 90% who are non-buyers.",
  ],
  "metrics": [
    "Mental Market Share, Mental Penetration, Network Size, Share of Mind.",
    "Distinctive-asset attribution trend.",
    "Share of model / AI-citation rate; sentiment trend.",
  ],
  "tools": [
    "Brand tracking platforms (CEP-based)",
    "Social listening and review analytics",
    "AI-answer-engine monitoring; BI dashboards",
  ],
  "ai": "AI is central here: it runs always-on listening, mines reviews and calls, checks AI-engine citations, and flags anomalies and drift in near real time. Humans interpret what the signals mean for the brand and decide whether to adapt or hold.",
  "example": "A tracker built on category entry points revealed the brand was losing recall for a fast-growing use case; the team added that use case to messaging (adaptation) without touching the core position (consistency), and recovered share.",
},
{
  "num": 13, "slug": "CRISIS_AND_CHANGE_MANAGEMENT", "title": "Crisis and Change Management",
  "discipline": "Brand Governance",
  "oneliner": "Manage brand changes and crises with caution, protecting integrity and continuity of meaning.",
  "collaborators": "Brand Monitoring, Perception Management, Legal/PR, Executive Leadership",
  "ai_level": "AI-assisted (scenario/response drafting, monitoring); humans own crisis decisions.",
  "laws": [20, 19, 21],
  "definition": [
    "Crisis and change management is the skill of altering a brand — or defending it under threat — rarely, carefully and in a consumer-driven way, so that its core meaning and trust survive. Brands can be changed, but only slowly and with strong justification.",
    "It spans two related jobs: managing deliberate change (repositioning, rebrand, name change) and responding to crises (reputational threats, failures) without doing lasting damage to equity.",
  ],
  "why": [
    "Careless change destroys accumulated recognition and trust overnight.",
    "Crises test the brand's promise; a poor response can permanently redefine it.",
    "Consumer-driven, gradual change preserves continuity while allowing evolution.",
    "Knowing when to retire a brand (mortality) is part of responsible stewardship.",
  ],
  "concepts": [
    ("Change rarely and carefully", "Per the Law of Change, only change the brand when evidence demands it, gradually, and in a way customers accept — never on internal whim."),
    ("Protect continuity", "Retain distinctive assets and core meaning through change so equity transfers rather than resets."),
    ("Crisis response principles", "Speed, transparency, accountability and alignment to brand values; a values-consistent response can strengthen a brand."),
    ("Brand mortality", "Per the Law of Mortality, sometimes the right move is a graceful sunset or migration rather than forcing a fading brand to live on."),
  ],
  "steps": [
    "Establish a change/crisis governance model and decision thresholds in advance.",
    "For change: gather evidence, define what stays constant vs what evolves, and phase it.",
    "For crisis: activate the response team, assess facts, and communicate promptly and honestly.",
    "Act consistently with brand values; align every channel on one response.",
    "Protect and carry over distinctive assets and core meaning.",
    "Review impact on equity/perception; adjust and document lessons.",
  ],
  "techniques": [
    "Pre-agreed crisis playbooks and spokesperson training.",
    "Phased rebrands with asset continuity (migration, not reset).",
    "Scenario planning and message pre-drafting for likely risks.",
  ],
  "antipatterns": [
    "Rebranding for internal fashion rather than customer evidence.",
    "Slow, defensive or inconsistent crisis responses.",
    "Discarding distinctive assets during a rebrand and resetting recognition.",
  ],
  "metrics": [
    "Perception/trust recovery time after an incident.",
    "Equity retention through a change (association continuity).",
    "Share-of-voice and sentiment during and after events.",
  ],
  "tools": [
    "Crisis playbooks and RACI",
    "Rebrand migration plans",
    "Real-time monitoring and response tooling",
  ],
  "ai": "AI supports rapid monitoring, scenario simulation, and first-draft response and migration messaging under time pressure. Crisis and change decisions — what to say, admit, change or retire — carry legal, ethical and strategic weight and must be made by accountable humans.",
  "example": "Facing a product failure, a brand responded within hours with an honest, values-consistent statement and remedy, kept its identity intact, and emerged with trust scores higher than before — while a rival that stayed silent lost ground.",
},
{
  "num": 14, "slug": "DIFFERENTIATION_AND_ATTRIBUTE_OWNERSHIP", "title": "Differentiation and Ownership of Attributes",
  "discipline": "Brand Strategy",
  "oneliner": "Develop and own a single distinctive attribute that competitors cannot credibly claim.",
  "collaborators": "Brand Positioning, Competitor Analysis, Focus and Simplification, Product Marketing",
  "ai_level": "AI-assisted (attribute/whitespace analysis); humans choose the attribute to own.",
  "laws": [22, 5, 2],
  "definition": [
    "Differentiation and attribute ownership is the skill of identifying, building and owning one distinctive attribute or word in customers' minds — the single-minded idea that separates the brand from every alternative.",
    "It converts focus (a strategic choice) into a defensible mental asset: an attribute the brand is famous for and competitors cannot take without looking like imitators.",
  ],
  "why": [
    "Owning an attribute makes the brand the default answer for that need.",
    "A single owned attribute resists competitive claims better than a bundle.",
    "It underpins pricing power, loyalty and word-of-mouth.",
    "It gives the whole organisation one thing to optimise and defend.",
  ],
  "concepts": [
    ("Singularity", "Per the Law of Singularity, the most powerful brands own one idea; a second attribute weakens the first."),
    ("Own the word", "Per the Law of the Word, translate the attribute into one word or phrase you can dominate."),
    ("Attribute selection", "Choose an attribute that is important to buyers, true of the brand, and not already owned by a stronger competitor."),
    ("Proof and reinforcement", "Ownership is earned by consistently demonstrating the attribute across product, experience and communication."),
  ],
  "steps": [
    "Enumerate the attributes buyers value in the category.",
    "Map which attributes competitors already own.",
    "Select one important, true, un-owned attribute to claim.",
    "Reduce it to a single word/phrase and build proof for it.",
    "Reinforce the attribute consistently across every touchpoint.",
    "Defend the attribute; if a rival owns your target, pivot to the opposite (see Competitor Analysis).",
  ],
  "techniques": [
    "Attribute-ownership mapping vs competitors.",
    "Laddering to find the ownable, meaningful attribute.",
    "Signature proof that dramatises the attribute.",
  ],
  "antipatterns": [
    "Claiming several attributes and owning none.",
    "Fighting for an attribute a stronger brand already owns.",
    "Choosing an attribute buyers do not actually value.",
  ],
  "metrics": [
    "Unaided brand-attribute association vs competitors.",
    "'Only brand that...' association strength.",
    "Preference lift among buyers who value the attribute.",
  ],
  "tools": [
    "Attribute-ownership / perceptual maps",
    "Driver analysis (which attributes drive choice)",
    "Brand tracking of association strength",
  ],
  "ai": "AI can quantify which attributes drive choice, reveal which are already owned, and surface un-owned whitespace from large text and survey datasets. Selecting the attribute to bet the brand on is a strategic human decision.",
  "example": "In a crowded CRM market, a brand stopped claiming 'powerful, easy and affordable' and committed to owning 'fastest to implement', backing it with a guarantee — becoming the default for teams who valued speed.",
},
{
  "num": 15, "slug": "COMPETITOR_ANALYSIS_AND_POSITIONING", "title": "Competitor Analysis and Positioning",
  "discipline": "Brand Strategy",
  "oneliner": "Read competitors' strengths and position against them, often by owning the opposite.",
  "collaborators": "Brand Positioning, Differentiation, Brand Monitoring, Product Marketing",
  "ai_level": "AI-assisted (competitive intelligence at scale); humans choose the strategic stance.",
  "laws": [17, 5, 8],
  "definition": [
    "Competitor analysis and positioning is the skill of understanding rivals' positions and strengths and then choosing a stance that wins — frequently by deliberately taking the opposite position to the leader rather than imitating it.",
    "Against a strong leader you cannot beat, being the opposite gives buyers a clear reason to choose you and converts the leader's strength into a liability.",
  ],
  "why": [
    "You position in a competitive context, not a vacuum; rivals define the whitespace.",
    "Imitating the leader concedes the ground it already owns.",
    "The 'opposite' stance turns a leader's strength into a weakness for a segment.",
    "Continuous competitive reading prevents being out-positioned.",
  ],
  "concepts": [
    ("Be the opposite", "When a leader owns an attribute (e.g., a colour, a claim), choose the opposite so buyers can tell you apart instantly — the branding analogue of the Law of Color."),
    ("Find un-owned whitespace", "Map competitor claims and attributes to locate valuable, defensible positions no one holds."),
    ("Challenger strategy", "A well-chosen challenger position ('the alternative for X') can grow fast by reframing the leader's strength as a trade-off."),
    ("Category framing", "Sometimes the best move is to change the frame of reference so the comparison favours you."),
  ],
  "steps": [
    "Profile key competitors: positioning, owned attributes, distinctive assets, proof.",
    "Map the perceptual space and identify what each rival owns.",
    "Find valuable, defensible whitespace or a credible 'opposite' to the leader.",
    "Choose the stance (opposite, challenger, niche leader, reframe).",
    "Build the positioning and proof around that stance.",
    "Monitor competitor moves and re-position as the landscape shifts.",
  ],
  "techniques": [
    "Perceptual mapping and attribute-ownership analysis.",
    "Win/loss analysis for real decision drivers.",
    "Messaging teardown of competitor assets.",
  ],
  "antipatterns": [
    "Copying the leader's position and assets (looking like an imitator).",
    "Fighting head-on for an attribute the leader owns.",
    "Positioning without validating that the whitespace is valued by buyers.",
  ],
  "metrics": [
    "Competitive win rate and win/loss reasons.",
    "Distinctiveness vs competitors in tracking.",
    "Share shift within the frame of reference.",
  ],
  "tools": [
    "Competitive intelligence platforms",
    "Perceptual maps and battlecards",
    "Win/loss programmes",
  ],
  "ai": "AI can continuously gather and structure competitive intelligence — messaging, pricing, assets, reviews — and surface whitespace and 'opposite' opportunities at scale. Choosing the stance and committing the brand to it is a human strategic decision.",
  "example": "Against an incumbent that owned 'enterprise-grade and comprehensive', a challenger positioned as 'radically simple' — the opposite — and won the segment that found the leader's complexity a burden.",
},
{
  "num": 16, "slug": "CATEGORY_CREATION", "title": "Creating New Categories",
  "discipline": "Brand Strategy",
  "oneliner": "Identify and create new categories by narrowing focus, then lead them as the defining brand.",
  "collaborators": "Focus and Simplification, Category Leadership, Publicity, Product Strategy",
  "ai_level": "AI-assisted (trend/whitespace detection, content scale); humans design the category.",
  "laws": [2, 8, 3],
  "definition": [
    "Creating new categories is the skill of dividing an existing market to open a new, narrower category the brand can define and lead — rather than expanding within a crowded one. The best way to be first in the mind is to invent the category you are first in.",
    "Category creation combines contraction (narrowing focus), naming (a name for the new category and the brand), publicity (earning the launch narrative) and leadership (growing and defending the category).",
  ],
  "why": [
    "It is easier to lead a new category than to overtake a leader in an old one.",
    "Categories tend to divide over time, continually opening new whitespace.",
    "A category creator becomes the reference brand and captures most of its growth.",
    "New categories attract disproportionate publicity and investment.",
  ],
  "concepts": [
    ("Division opens whitespace", "Categories split into sub-categories over time; spotting the next division reveals a category to create and own."),
    ("Contract to create", "Per the Law of Contraction, narrowing focus is what makes a new, ownable category possible."),
    ("Name the category", "Give the new category (and the brand) a distinctive name so the market can talk about it and attribute it to you."),
    ("Lead from day one", "Per the Law of the Category, promote the category itself; educate the market and set the standards."),
  ],
  "steps": [
    "Spot an emerging division or unmet job the current categories serve poorly.",
    "Define and narrow the new category until it is ownable.",
    "Name the category and position the brand as its definition.",
    "Build the launch narrative and earn publicity (be first in the mind).",
    "Educate the market and establish the category's vocabulary and standards.",
    "Grow and defend the category as its leader.",
  ],
  "techniques": [
    "Jobs-to-be-done and trend analysis to find divisions.",
    "Category-design narrative ('from/to' point of view).",
    "Own the category's language, benchmarks and events.",
  ],
  "antipatterns": [
    "Expanding within a crowded category instead of dividing it.",
    "Creating a category too broad or too niche to sustain.",
    "Failing to name and educate, so a competitor defines the category you started.",
  ],
  "metrics": [
    "Category awareness and adoption growth.",
    "Attribution of the category to the brand (who defined it).",
    "Share of category search and AI citations.",
  ],
  "tools": [
    "Trend / jobs-to-be-done research",
    "Category-design point-of-view narrative",
    "Thought-leadership and PR engine",
  ],
  "ai": "AI can detect emerging divisions and unmet jobs from large datasets, test category names and narratives, and scale the educational content a new category needs. Designing the category and committing to lead it is a human strategic bet.",
  "example": "Rather than competing in 'analytics', a brand narrowed and named 'product analytics', wrote the definitive point of view, earned launch publicity, and became the category's reference brand as it grew.",
},
{
  "num": 17, "slug": "PERSISTENCE_AND_LONG_TERM_VISION", "title": "Persistence and Long-term Vision",
  "discipline": "Brand Leadership",
  "oneliner": "Build and sustain a brand as a long-term asset through patience, consistency and strategic foresight.",
  "collaborators": "Executive Leadership, Messaging Consistency, Brand Monitoring, Finance",
  "ai_level": "AI-assisted (long-horizon tracking, forecasting); humans hold the vision and discipline.",
  "laws": [19, 20, 21],
  "definition": [
    "Persistence and long-term vision is the meta-skill of treating the brand as a compounding asset built over years, resisting short-term temptations that erode it, and staying consistent long enough for equity to accumulate.",
    "It is the discipline that holds all the other branding skills together over time: focus maintained, position defended, message kept consistent, and change made only rarely and carefully.",
  ],
  "why": [
    "Brand equity compounds; it is destroyed by impatience and constant change.",
    "Consistency over years is what turns a name into a brand.",
    "Long-term brand investment out-performs short-term activation alone.",
    "Foresight anticipates category evolution before it forces reactive change.",
  ],
  "concepts": [
    ("Consistency compounds", "Per the Law of Consistency, staying the course for years is the single biggest driver of brand strength."),
    ("Rare, careful change", "Per the Law of Change, evolve slowly and deliberately; frequent reinvention resets equity."),
    ("Brand as an asset", "Manage the brand on a multi-year horizon with equity metrics, not just quarterly response metrics (the 60/40 logic)."),
    ("Stewardship and mortality", "Steward the brand for the long term, and recognise when graceful renewal or sunset (mortality) serves the portfolio."),
  ],
  "steps": [
    "Articulate a multi-year brand vision and the single idea to compound.",
    "Set long-term equity goals and the metrics that track them.",
    "Protect brand investment against short-term pressure (defend the 60/40 balance).",
    "Hold consistency across leadership changes and campaigns.",
    "Anticipate category evolution and plan measured adaptation.",
    "Review equity annually; renew or retire brands responsibly.",
  ],
  "techniques": [
    "Multi-year brand plans and equity scorecards.",
    "Governance that protects brand investment from quarterly cuts.",
    "Succession/continuity playbooks so vision survives leadership change.",
  ],
  "antipatterns": [
    "Chasing quarterly results by cutting brand investment or changing position.",
    "Rebranding with each new leader.",
    "Measuring only short-term activation and ignoring equity.",
  ],
  "metrics": [
    "Multi-year brand equity and mental-availability trends.",
    "Brand-driven revenue and pricing power over time.",
    "Consistency of position across years and leaders.",
  ],
  "tools": [
    "Long-term brand plan + equity scorecard",
    "Brand-investment governance",
    "Longitudinal tracking dashboards",
  ],
  "ai": "AI can maintain longitudinal equity tracking, forecast category shifts, and quantify the long-term cost of short-term cuts. Holding the vision and the discipline to stay consistent through pressure is fundamentally a human leadership responsibility.",
  "example": "Through three CEOs and multiple downturns, a brand kept one position and visual system and protected a 60/40 investment split; a decade later it commanded a durable price premium while rivals that reinvented constantly stayed commoditised.",
},
]

# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
import re  # noqa: E402

LAW_SUMMARY = {n: summary for n, _, summary in LAWS}


def github_slug(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = s.replace(" ", "-")
    return s


def law_heading(num: int) -> str:
    return f"Law {num}: The Law of {LAW_BY_NUM[num]}"


def law_ref(num: int) -> str:  # noqa: F811  (override the early stub)
    heading = law_heading(num)
    return f"[{heading}]({LAWS_FILE}#{github_slug(heading)})"


def file_name(s: dict) -> str:
    return f"{s['num']:02d}_{s['slug']}_SKILL.md"


def bullets(items) -> str:
    return "\n".join(f"- {i}" for i in items)


def numbered(items) -> str:
    return "\n".join(f"{n}. {i}" for n, i in enumerate(items, 1))


def render_skill(s: dict) -> str:
    tag_slug = s["slug"].lower().replace("_", "-")
    laws_line = ", ".join(f"Law {n} ({LAW_BY_NUM[n]})" for n in s["laws"])
    fm = [
        "---",
        f"id: SKILL-BRAND-{s['num']:03d}",
        f"title: {s['title']} Skill",
        "document_type: Skill",
        "category: Branding",
        "phase: Phase 05",
        "owner: Brand Strategy Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "tags:",
        "  - skill",
        "  - branding-skill",
        f"  - {tag_slug}",
        "related_documents:",
        "  - ROOT_INDEX.md",
        "  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md",
        "  - 01_PHASES/PHASE_05_SKILLS_MASTER_PROMPT.md",
        f"  - 02_ARTEFACTS/PHASE_05_SKILLS/Branding/{LAWS_FILE}",
        "standards:",
        "  - ISO 42001",
        "  - ISO 27001",
        "  - NIST AI RMF",
        "  - SOC 2",
        "  - WCAG 2.2 AA",
        "---",
    ]

    concepts = "\n\n".join(f"**{h}.** {b}" for h, b in s["concepts"])
    laws_applied = "\n".join(
        f"- {law_ref(n)} — {LAW_SUMMARY[n]}" for n in s["laws"]
    )

    body = f"""# {s['title']} Skill

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Skills]({R_SKILLS}) · [Branding Skills](README.md) · [22 Immutable Laws]({LAWS_FILE}) · [Phase 05 Prompt]({R_PROMPT})

## At a Glance

{s['oneliner']}

| Field | Detail |
| --- | --- |
| Skill | {s['title']} |
| Category | Branding |
| Discipline | {s['discipline']} |
| Primary laws | {laws_line} |
| AI automation | {s['ai_level']} |
| Key collaborators | {s['collaborators']} |

## How to Use This Document

- **Brand & marketing leaders** — use *What This Skill Is*, *Core Concepts* and *How to Apply It* as a working method and a hiring/coaching rubric.
- **AI / automation teams** — use *Core Concepts*, *How to Apply It* and *AI Assistance* as the basis for an AI agent's instructions and guardrails.
- **Practitioners** — use *Techniques*, *Anti-Patterns* and the *Worked Example* on live brand work.
- **Quality & governance leads** — use *How Success Is Measured* to set expectations and track brand health.

## What This Skill Is

{(chr(10) + chr(10)).join(s['definition'])}

## Why It Matters

{bullets(s['why'])}

## Immutable Laws This Skill Applies

This skill is a direct application of the following [22 Immutable Laws of Branding]({LAWS_FILE}):

{laws_applied}

## Core Concepts and Frameworks

{concepts}

## How to Apply It (Step by Step)

{numbered(s['steps'])}

## Techniques and Tactics

{bullets(s['techniques'])}

## Anti-Patterns to Avoid

{bullets(s['antipatterns'])}

## How Success Is Measured

{bullets(s['metrics'])}

## Tools and Enablers

{bullets(s['tools'])}

## AI Assistance and Automation

{s['ai']}

## Worked Example

{s['example']}

## Related Resources

- [Branding Skills Index](README.md)
- [The 22 Immutable Laws of Branding]({LAWS_FILE})
- [All Phase 05 Skills]({R_SKILLS})
- [Enterprise Rules]({R_RULES})
- [Enterprise Checklists]({R_CHECKLISTS})
- [Enterprise Playbooks]({R_PLAYBOOKS})
- [Enterprise Templates]({R_TEMPLATES})
- [Enterprise Knowledge]({R_KNOWLEDGE})
- [Certification & Maturity]({R_CERT})
- [AIBOS Root Specification]({R_SPEC})
- [Enterprise Glossary]({R_GLOSSARY})

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | Complete, ready-to-use branding skill reference. |
"""
    return "\n".join(fm) + "\n\n" + body


def render_laws() -> str:
    # Map each law to the skills that apply it.
    law_to_skills: dict[int, list[str]] = {n: [] for n, _, _ in LAWS}
    for s in SKILLS:
        for n in s["laws"]:
            law_to_skills[n].append(s["title"])

    fm = [
        "---",
        "id: SKILL-BRAND-000",
        "title: The 22 Immutable Laws of Branding",
        "document_type: Reference",
        "category: Branding",
        "phase: Phase 05",
        "owner: Brand Strategy Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "tags:",
        "  - branding",
        "  - laws",
        "  - reference",
        "related_documents:",
        "  - ROOT_INDEX.md",
        "  - 00_ROOT/AIBOS_ROOT_SPECIFICATION.md",
        "  - 01_PHASES/PHASE_05_SKILLS_MASTER_PROMPT.md",
        "---",
    ]

    law_sections = []
    for n, name, summary in LAWS:
        skills = law_to_skills[n]
        applied = ", ".join(skills) if skills else "General brand strategy"
        law_sections.append(
            f"## {law_heading(n)}\n\n{summary}\n\n"
            f"**Applied by skill(s):** {applied}."
        )

    # Cross-map of the brief's vocabulary to the canonical Ries laws.
    crossmap = [
        ("Law of Focus", "Contraction (2) + Singularity (22)"),
        ("Law of the Leader", "The Category (8) + Credentials (6)"),
        ("Law of the Opposite", "Color (17) — position as the opposite of the leader"),
        ("Law of Division", "Contraction (2) + The Category (8) — categories divide over time"),
        ("Law of Persuasion", "Consistency (19) — persistent, consistent messaging"),
        ("Law of Uniqueness", "Singularity (22) + The Word (5)"),
        ("Law of Eternity", "Consistency (19) + Change (20) + Mortality (21)"),
    ]
    crossmap_rows = "\n".join(f"| {a} | {b} |" for a, b in crossmap)

    skills_index = "\n".join(
        f"- [{s['title']}]({file_name(s)}) — applies {', '.join('Law ' + str(n) for n in s['laws'])}"
        for s in SKILLS
    )

    body = f"""# The 22 Immutable Laws of Branding

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Skills]({R_SKILLS}) · [Branding Skills](README.md) · [Phase 05 Prompt]({R_PROMPT})

## Overview

This is the foundational reference for the AIBOS Branding skills. The 22 Immutable
Laws of Branding (Al Ries & Laura Ries) describe how brands are built and destroyed
in the customer's mind. Every branding skill in this folder is an application of one
or more of these laws. Use this document as the shared vocabulary and first principles
for brand strategy, and link to it from any brand work.

> **On quality and ethics:** these laws describe how perception works, not a licence
> to mislead. AIBOS requires that every brand claim be true, deliverable and
> substantiated (see [Perception Management](09_PERCEPTION_MANAGEMENT_SKILL.md)).

## The Laws

{(chr(10) + chr(10)).join(law_sections)}

## Vocabulary Cross-Map

Some summaries of these laws use different names (for example *Focus*, *Leader*,
*Opposite*, *Division*, *Persuasion*, *Uniqueness*, *Eternity*). They map to the
canonical laws above as follows:

| Term | Canonical law(s) |
| --- | --- |
{crossmap_rows}

## Laws to Skills Map

{skills_index}

## Related Resources

- [Branding Skills Index](README.md)
- [All Phase 05 Skills]({R_SKILLS})
- [AIBOS Root Specification]({R_SPEC})
- [Enterprise Glossary]({R_GLOSSARY})

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | Reference for the 22 Immutable Laws with skill cross-mapping. |
"""
    return "\n".join(fm) + "\n\n" + body


def render_readme() -> str:
    skills_rows = "\n".join(
        f"| {s['num']:02d} | [{s['title']}]({file_name(s)}) | {s['discipline']} | "
        f"{', '.join(str(n) for n in s['laws'])} |"
        for s in SKILLS
    )
    fm = [
        "---",
        "id: SKILL-BRAND-INDEX",
        "title: Branding Skills — Index",
        "document_type: Index",
        "category: Branding",
        "phase: Phase 05",
        "owner: Brand Strategy Lead",
        "status: Published",
        "lifecycle: Active",
        "classification: Internal",
        "version: 1.0.0",
        f"created: {CREATED}",
        f"updated: {CREATED}",
        "tags:",
        "  - branding",
        "  - skills",
        "  - index",
        "---",
    ]
    body = f"""# Branding Skills — Index

> **Navigate:** [Home]({R_HOME}) · [Catalogue]({R_INDEX}) · [All Phase 05 Skills]({R_SKILLS}) · [Phase 05 Prompt]({R_PROMPT})

## Overview

The Branding skill set gives AIBOS a complete, ready-to-use branding capability for
two jobs: **(1)** building, developing and managing the AI Agency's own brand and its
SaaS products, and **(2)** designing brand strategy for customers as part of AI
automation, integration and implementation engagements.

Each skill is a competency a human or an AI agent can apply, and every skill is a
direct application of the [22 Immutable Laws of Branding]({LAWS_FILE}) grounded in
current practice (Aaker and Keller brand-equity models, the positioning framework of
points of difference vs points of parity, a structured naming methodology, and
mental-availability / Category Entry Point measurement).

## Start Here

- **New to branding?** Read [The 22 Immutable Laws of Branding]({LAWS_FILE}) first.
- **Building a brand from scratch?** Focus and Simplification → Brand Positioning →
  Naming Expertise → Messaging Consistency.
- **Growing an existing brand?** Category Leadership, Differentiation, Global Brand
  Building, Persistence and Long-term Vision.
- **Defending a brand?** Perception Management, Competitor Analysis, Brand Monitoring,
  Crisis and Change Management.

## The Skills

| # | Skill | Discipline | Laws applied |
| --- | --- | --- | --- |
{skills_rows}

## Foundational Reference

- [The 22 Immutable Laws of Branding]({LAWS_FILE})

## How These Fit AIBOS

- **Internal use:** develop and manage the company's own brand across HR, product,
  marketing, sales and strategy following industry best practice.
- **Client delivery:** scope and deliver brand strategy alongside AI automation and
  integration work — positioning, naming, messaging, measurement and governance.
- **AI agents:** each skill doubles as an instruction set / system-prompt basis for
  brand-focused AI agents, with explicit anti-patterns and human-in-the-loop guardrails.

## Related Resources

- [All Phase 05 Skills]({R_SKILLS})
- [Enterprise Rules]({R_RULES})
- [Enterprise Playbooks]({R_PLAYBOOKS})
- [Enterprise Templates]({R_TEMPLATES})
- [Enterprise Knowledge]({R_KNOWLEDGE})
- [AIBOS Root Specification]({R_SPEC})
- [Enterprise Glossary]({R_GLOSSARY})

## Version History

| Version | Date | Summary |
| --- | --- | --- |
| 1.0.0 | {CREATED} | Initial Branding skill set: 17 skills + 22-laws reference. |
"""
    return "\n".join(fm) + "\n\n" + body


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    written = []

    laws_path = OUT / LAWS_FILE
    laws_path.write_text(render_laws(), encoding="utf-8")
    written.append(laws_path)

    for s in SKILLS:
        p = OUT / file_name(s)
        p.write_text(render_skill(s), encoding="utf-8")
        written.append(p)

    readme_path = OUT / "README.md"
    readme_path.write_text(render_readme(), encoding="utf-8")
    written.append(readme_path)

    print(f"Generated {len(written)} files in {OUT.relative_to(REPO)}:")
    for p in written:
        print(f"  - {p.name}")


if __name__ == "__main__":
    main()




