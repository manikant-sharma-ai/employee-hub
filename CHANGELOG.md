# Changelog

One dated block per drop. What shipped, and why it is shaped that way.

## 2026-10-31 - repo created

**Employee 1 of the backlog: `ai-engineer`** (`skills/ai-engineer`, v1.0.0)

The worker role rather than a narrow one: a single employee that carries eleven disciplines, because in practice the same person who writes the prompt is the one asked to fix the loop and wire the tool.

- `SKILL.md` - accountability, the five things it must be handed before starting, a symptom-to-craft routing table, an eight-step build loop ordered by cost of being wrong, standards, output contract, guardrails, and a trigger test (three prompts that should load it, two that should not).
- `references/` - eleven craft files, loaded on demand rather than front-loaded: prompt engineering, context engineering, loop engineering, graph engineering, vibe coding, MCP and tools, image generation, scenario design, automation engineering, model selection and evals, skill authoring.
- `scripts/validate_skill.py` - checks frontmatter, description triggering quality, required sections and reference links. Passes clean.
- `assets/design-note-template.md` - the one-page note every non-trivial build ships with.

Repo scaffolding: `registry.json`, `BACKLOG.md` (30 roles queued), plugin manifest, `scripts/validate_repo.py`, `docs/daily-drop.md`.
