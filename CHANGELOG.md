# Changelog

One dated block per drop. What shipped, and why it is shaped that way.

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
