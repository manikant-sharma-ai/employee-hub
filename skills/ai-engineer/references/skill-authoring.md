# Skill authoring

A skill is an employee's experience written down. Two things decide whether it earns its place: the **description** decides whether it ever wakes up, and the **body** decides whether it does good work when it does.

## The description is the product

A skill that never triggers is worthless, and a skill that triggers on everything is worse - it floods every conversation with instructions meant for a narrow case.

Formula: **what it does** + **when to use it, in the words a human would actually type** + **what it is not for**.

- Weak: "Helps with prompts."
- Strong: "Writes and repairs prompts for production AI features. Use when a prompt is vague, the model ignores instructions, or output format drifts. Trigger phrases: 'write me a prompt', 'the model keeps ignoring this'. Not for general writing or copy editing."

Include the trigger phrases literally. Include the negative case - it is what keeps sibling skills from colliding.

## The body

Order that works:

1. **Accountability** - what this employee is answerable for, in one paragraph. Not a personality.
2. **Inputs required** - what must be handed over before work starts, and what to ask for if it is missing.
3. **Routing** - a table from symptom to reference file. This is how one skill carries many crafts without a bloated manifest.
4. **Workflow** - the sequence, ordered by cost of being wrong.
5. **Standards** - the non-negotiables, stated as rules you can check.
6. **Output contract** - what the deliverable looks like.
7. **Guardrails** - what it must never do.
8. **Trigger test** - three prompts that should load it, two that should not.

## Progressive disclosure

Keep `SKILL.md` under roughly 500 lines. Everything that is depth rather than direction goes in `references/`, one craft per file, loaded on demand. A skill that front-loads 3,000 lines of theory is a skill nobody reads and every conversation pays for.

## Scripts over instructions

Anything deterministic - arithmetic, date maths, string surgery, sorting, validation, file wrangling - belongs in `scripts/`, not in prose the model must follow. A script is reproducible; a described procedure is a re-derivation every time.

## Testing a skill

- Write the trigger test and check it against sibling skills for collisions.
- Run the three "should fire" prompts cold, in a fresh session, and see whether the skill actually loads.
- Run the two "should not fire" prompts and confirm it stays quiet.
- If the skill produces a file, run its validator and confirm the file opens.

## Versioning

Semver per skill, a date, and a changelog line for every change. Record what changed and why - six months later, the "why" is the only part you will need.
