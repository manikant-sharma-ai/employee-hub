# Changelog

One dated block per drop. What shipped, and why it is shaped that way.

## 2026-11-01 - daily drop: five employees (v1.2.0)

**The mix this drop: two revenue-facing, two operations, one founder-leverage.** `sales-outreach` was next in the queue and is a third revenue-facing role, so it was held and `support-agent` and `data-analyst` were taken ahead of it - the mix is the fixed constraint, the queue is the source. It stays at the top of the queue.

- **`graphic-designer`** (`skills/graphic-designer`, v1.0.0) - the production designer, not the art director. Accountable for an asset that does its job at the size it is seen, not for "looking nice", because the failure mode in a small business is a beautiful poster with an unreadable price. Six references split by surface: brand system, layout and type, social and thumbnail craft, print and production, brief and feedback, Indian market conventions. The print reference exists because a reprint costs more than every design hour combined, and the three numbers that cause one - colour mode, 300 DPI, 3 mm bleed - are cheap to check and expensive to miss. `image-generation` is explicitly handed to `ai-engineer` in the description, because that is the one trigger the two roles would otherwise fight over. The India reference carries the festival calendar, script pairing and marketplace image rules, because a pan-India festival creative reads as a brand that does not know its customer.

- **`content-writer`** (`skills/content-writer`, v1.0.0) - shaped around the one thing that makes written content work: the proof. The brief template puts the proof table before the outline, and the output contract makes a `[VERIFY]` marker an acceptable deliverable and an invented statistic a firing offence. The humanizer reference is a counting pass, not a vibe pass - one tell is invisible, three in 300 words is where a reader decides a machine wrote it - because "make it not sound like AI" is otherwise unactionable. Voice is treated as an input extracted from samples rather than a style invented in the session, which is the difference between writing for this founder and writing for a founder. Distribution is built into the same workflow, since the writing is the expensive part and repurposing is the part people skip.

- **`research-analyst`** (`skills/research-analyst`, v1.0.0) - the founder-leverage role, and the one with the strictest honesty rule in the repo: never invent a source, because a fabricated citation survives review and poisons every decision built on it. Structured as a funnel from topic to decision - actor, action, amount, date - because "research the market" is unanswerable and "should we spend ₹40 lakh on two bays in Pune in Q1" is not. Four confidence labels (verified, computed, inferred, assumed) are used consistently so an inference cannot arrive in a board pack dressed as a fact. The diligence reference is ordered by how often each check catches something, and puts bank-account-name-matches-entity at the top, which is where most advance-payment losses in Indian SMB trade actually happen. `india-market-sources.md` is the piece that makes the role usable locally: MCA21, GST validation, GeM bid history, DGFT trade data, and the warning that aggregators lag the registry.

- **`support-agent`** (`skills/support-agent`, v1.0.0) - the first operations role, built around one rule: never say "processed" when you mean "initiated", and never say either unless a system in front of you did it. That single guardrail prevents the most damaging support failure, a customer told their refund is done who then has to be disappointed twice. Triage is defined by money and risk rather than by how angry the customer sounds, because loud is not severe and triaging by volume puts the wrong tickets first. The authority ladder is written as a table to be filled in with the business's real limits, and the default when it is empty is that every monetary commitment needs approval - a safe default rather than an optimistic one. The India reference covers WhatsApp's 24-hour window, Hinglish register, COD refunds versus card reversals and marketplace off-platform rules, all of which cause real losses when ignored.

- **`data-analyst`** (`skills/data-analyst`, v1.0.0) - the second operations role, and deliberately adjacent to `research-analyst` rather than overlapping: this one works on the business's own numbers, that one on the outside world, and both descriptions say so. Built to prevent two specific failures - the number that does not tie to the accounting system, and the metric defined after seeing which version looks better - which is why the definition gets five written lines before any computation and the readout carries a data-quality log. Decomposition is the centre of the craft file because "why did revenue drop" is the question most often answered with a single guessed cause and no arithmetic. `statistical-honesty.md` exists because the confident wrong number usually comes from a percentage on nine rows or a correlation reported as a cause, and both survive review because they look like data.

**Standard wiring:** all five link `core/connector-preflight.md` before the first substantive step and `core/memory-and-notes.md` plus `core/performance-tracking.md` before the output contract. Each carries six craft references, one asset template, and seeded `notes/` (learnings, contacts, decisions, journal for 2026-11). Each ships its own `scripts/validate_skill.py`. `scripts/validate_repo.py` passes with zero errors and zero warnings.

## 2026-10-31 (evening) - renamed to Employee Hub, v1.1.0

**The repo is now `employee-hub`.** Same content, new name, because the product is the employees, not the skills.

**New: the Employee Standard (`core/`).** Every employee now follows four obligations, and `scripts/validate_repo.py` fails a skill that does not wire them in.

- `core/connector-preflight.md` - check access before answering. Say the job in one line, list the capabilities it needs, check which tools are actually in front of you, then answer in one of four states: all connected (do the work), partly connected (do that part completely, name the gap, ask for the specific connector), nothing connected (name two or three connectors, ranked, with what each unlocks), or connected-but-wrong-tool (do the best available thing, then recommend the better one with a reason). Fixed three-line answer format. Includes the clothing-brand worked example and the India-first ranking - IndiaMART for B2B surplus, Shopify for D2C, Razorpay for collections, Shiprocket for last mile.
- `core/connector-catalog.md` - job to connector map, ranked for a business in India, with an explicit warning that the catalog does not mean anything is connected.
- `core/memory-and-notes.md` - four notes files per employee (learnings, contacts, journal, decisions), when to read, when to write, what a good note is.
- `core/performance-tracking.md` - one calendar event per task, weekly review, monthly scorecard with seven metrics, and the monthly self-audit that fixes one thing.
- `core/employee-standard.md` - the four obligations and the one-line test for whether they were followed.

**Every skill now ships with memory.** `skills/<employee>/notes/` seeded with learnings, contacts, decisions and a dated journal. `ai-engineer` is seeded with three real rules from building it.

**`ai-engineer` v1.1.0** - added the connector preflight section, the notes and self-tracking section, and a routing row that sends any data-or-action task through the preflight first.

**Cadence changed from one employee a day to five**, at 06:00 IST, in a fixed mix: two revenue-facing, two operations, one founder-leverage. Backlog expanded from 30 to 150 roles - thirty days of runway.

## 2026-10-31 - repo created

**Employee 1: `ai-engineer`** (`skills/ai-engineer`, v1.0.0) - the worker role rather than a narrow one, because in practice the same person who writes the prompt is the one asked to fix the loop and wire the tool.

- `SKILL.md` - accountability, the five things it must be handed before starting, a symptom-to-craft routing table, an eight-step build loop ordered by cost of being wrong, standards, output contract, guardrails, trigger test.
- `references/` - eleven craft files loaded on demand: prompt engineering, context engineering, loop engineering, graph engineering, vibe coding, MCP and tools, image generation, scenario design, automation engineering, model selection and evals, skill authoring.
- `scripts/validate_skill.py`, `assets/design-note-template.md`.

Repo scaffolding: `registry.json`, `BACKLOG.md`, plugin manifest, `scripts/validate_repo.py`, `docs/daily-drop.md`.
