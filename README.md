# Employee Hub

AI employees for any business. One folder per employee, five new ones every morning at 06:00 IST.

You install the hub once. Each employee becomes a skill your agent picks up - the way a new hire picks up a role, with the experience already in place, and with the habit of telling you what it needs before it starts.

## The idea

A person you hire brings four things: experience, tool access, a brief about your business, and a schedule. An AI employee is the same four parts.

| Part | Where it lives |
|---|---|
| Experience | `SKILL.md` + `references/` - the craft, written down |
| Tool access | Connectors you authorise (IndiaMART, Shopify, Gmail, Sheets, Canva, Razorpay...) |
| The brief | Your context files, brand assets, examples of good output |
| The schedule | A cron run, a webhook, or you asking it |

The skill file carries the experience. The hub carries something else that most skill collections miss: a shared standard for how every employee behaves when it lacks access.

## The Employee Standard

Every employee here follows `core/employee-standard.md`. Four obligations:

1. **Check the connectors before answering.** No employee produces a report it had no way to compute, or claims to have sent something it never sent. It says what it needs, by name.
2. **Keep notes.** `notes/learnings.md`, `notes/contacts.md`, a dated journal, a decision log. It reads them at the start of a task and writes them at the end, so it gets better instead of repeating itself.
3. **Track itself on the calendar.** One event per task, a weekly review, a monthly scorecard. It knows its own first-pass acceptance rate and its repeat mistakes.
4. **Never fake the part it cannot do.** It delivers the part it can, names the gap, and offers a manual fallback.

### What that looks like in practice

You are a clothing brand with leftover stock. You hand over your sales file and ask what to do.

The employee answers in three lines:

```
Right now I can: from your sales file, 9 of 22 SKUs have not moved in 90 days and are
holding roughly ₹X at your stated cost; clearing those in bulk protects your retail price.
To finish it, connect: IndiaMART - unlocks live verified bulk buyers and enquiries.
Best tool for this job: IndiaMART - because surplus apparel in India sells to wholesale
buyers, not to your D2C storefront.
```

No invented market prices. No "I've listed it". A real answer from the one connector it had, plus the specific connector that would finish the job, plus a reason grounded in your market. That behaviour is written down in `core/connector-preflight.md`, and every skill is required to wire it in.

## What's in here

```
skills/<employee>/
  SKILL.md          accountability, inputs, routing, workflow, standards, guardrails
  references/       the craft, one file per discipline, loaded only when needed
  scripts/          anything deterministic, so the model does not reason about it
  assets/           templates and examples of good output
  notes/            learnings, contacts, journal, decisions - the employee's memory
core/               the Employee Standard every skill follows
registry.json       machine-readable index: name, version, date added, connectors
skills/employee-hub-router/  the dispatcher - which employee to hire for the job in front of you
CHANGELOG.md        one dated block per drop
BACKLOG.md          117 roles queued, five a day
.claude-plugin/     plugin manifest, so the hub installs as one unit
.github/workflows/  CI validation on every push, and the 06:00 IST drop ticket
docs/daily-drop.md  the standing procedure for the 06:00 drop
docs/scheduling.md  how to put an employee on a cron, a webhook or an Action
```

## Employees

| Employee | What it does | Added |
|---|---|---|
| [`ai-engineer`](skills/ai-engineer/SKILL.md) | Designs, builds and ships AI systems - prompts, context, loops, graphs, MCP tools, images, evals and automation. | 2026-10-31 |
| [`graphic-designer`](skills/graphic-designer/SKILL.md) | Social visuals, thumbnails, carousels, deck slides, packaging labels and print-ready files that hold the brand at the size they are seen. | 2026-11-01 |
| [`content-writer`](skills/content-writer/SKILL.md) | Long and short form content in the founder's voice, with a proof table, a humanizer pass and a distribution map. | 2026-11-01 |
| [`research-analyst`](skills/research-analyst/SKILL.md) | Market, competitor and vendor research that ends in a one-page decision memo with every claim labelled verified or assumed. | 2026-11-01 |
| [`support-agent`](skills/support-agent/SKILL.md) | First-line customer replies - triage, tone, the actual words, and an escalation that says what it is authorised to promise. | 2026-11-01 |
| [`data-analyst`](skills/data-analyst/SKILL.md) | A spreadsheet turned into an answer - cleaning, a written metric definition, decomposition, a chart and a one-page readout. | 2026-11-01 |
| [`sales-outreach`](skills/sales-outreach/SKILL.md) | Outbound that gets replies - ICP test, verified list, first touches written to one person, a cadence that adds something each time, objection answers and a CRM contract. | 2026-11-02 |
| [`video-editor`](skills/video-editor/SKILL.md) | Raw footage into cuts that hold past three seconds - hook, pacing, captions, sound and the right export per platform, as a cut list anyone can execute. | 2026-11-02 |
| [`finance-ops`](skills/finance-ops/SKILL.md) | Invoices, bank and gateway reconciliation, expense categorisation and a month-end close whose exception list says exactly what is unexplained. | 2026-11-02 |
| [`hr-recruiter`](skills/hr-recruiter/SKILL.md) | A scorecard before a JD, screening with a recorded reason per candidate, a structured interview kit and candidate comms that do not ghost anyone. | 2026-11-02 |
| [`brand-strategist`](skills/brand-strategist/SKILL.md) | The position with a named alternative and an exclusion, the messaging hierarchy, naming that can be cleared, and a tone-of-voice guide with rules. | 2026-11-02 |
| [`seo-specialist`](skills/seo-specialist/SKILL.md) | Which searches are winnable, intent read off the results page, on-page fixes as a copy-paste table, and a brief a writer can follow. | 2026-11-03 |
| [`presentation-designer`](skills/presentation-designer/SKILL.md) | The deck that argues - an arc ending in a decision, one claim per title, numbers as evidence, speaker notes, sized to the slot. | 2026-11-03 |
| [`bookkeeper`](skills/bookkeeper/SKILL.md) | Day-to-day entries from the bank statement, a document behind each one, an exception list instead of a suspense ledger, and a payment tracker. | 2026-11-03 |
| [`legal-drafter`](skills/legal-drafter/SKILL.md) | First-draft contracts, NDAs and policies in plain language, with the review boundary and a five-item risk list attached. | 2026-11-03 |
| [`product-manager`](skills/product-manager/SKILL.md) | What to build and what to cut - PRD with the problem first, a written prioritisation rule, sliced stories and a launch checklist. | 2026-11-03 |
| [`social-media-manager`](skills/social-media-manager/SKILL.md) | Calendar, posting, repurposing and engagement across platforms - a week planned from one idea, with the reply rules written down. | 2026-11-03 |
| [`ui-designer`](skills/ui-designer/SKILL.md) | Screens, states and component specs a developer can build - the flow, the empty and error states, the spacing scale, the handoff. | 2026-11-03 |
| [`email-marketer`](skills/email-marketer/SKILL.md) | Newsletters and sequences that get opened - subject-line tests, a list that is clean and consented, and a send that respects deliverability. | 2026-11-03 |
| [`qa-tester`](skills/qa-tester/SKILL.md) | Test plans, edge-case matrices and bug reports a developer can act on - reproduction, severity and the release call. | 2026-11-03 |
| [`translator-localiser`](skills/translator-localiser/SKILL.md) | Indian-language localisation with tone and idiom - transliteration, formality, number and date formats, and a glossary that stays consistent. | 2026-11-03 |
| [`pr-writer`](skills/pr-writer/SKILL.md) | Earned coverage - a real news hook, a press note a journalist can file from, a 120-word pitch, a named media list with a reason per name, and an honest record of what published. | 2026-11-04 |
| [`partnerships`](skills/partnerships/SKILL.md) | Revenue through other people's customers - a fit test before the first call, a one-pager in the partner's numbers, terms that survive a thin margin, and 90 days with a kill date. | 2026-11-04 |
| [`procurement`](skills/procurement/SKILL.md) | The right thing at a defensible price - a spec before any quote, landed cost and TCO, vendor checks, negotiation with a walk-away, and a purchase-to-pay trail. | 2026-11-04 |
| [`analytics-instrumenter`](skills/analytics-instrumenter/SKILL.md) | What the business will be able to know, decided before the code ships - event taxonomy, tracking plan, written funnel definitions, dashboard spec and a QA pass that proves events fire. | 2026-11-04 |
| [`pricing-analyst`](skills/pricing-analyst/SKILL.md) | What to charge and how to package it - willingness-to-pay evidence, plans with fair fences, a contribution floor, a discount ladder and a rollout with a reversal trigger. | 2026-11-04 |
| [`employee-hub-router`](skills/employee-hub-router/SKILL.md) | Reads the job, names the employee, says what to hand over and which connector is missing - the hire desk for the other twenty-six. | 2026-11-03 |
| [`hiring-manager`](skills/hiring-manager/SKILL.md) | The people manager after the offer - onboarding that has someone useful in week one, a 30-60-90 with checkable milestones, a quarterly review cycle on evidence, underperformance named inside four.... | 2026-11-05 |
| [`compliance-watch`](skills/compliance-watch/SKILL.md) | Knows what this business must file, hold and prove - an obligation register derived from entity, state, headcount and turnover, a calendar built on work-back dates, change watching from primary.... | 2026-11-05 |
| [`chief-of-staff`](skills/chief-of-staff/SKILL.md) | The founder-leverage role - the operating rhythm: a 45-minute weekly review on four numbers, a decision log with a reversal condition, commitments tracked to closure, meetings with an outcome, and.... | 2026-11-05 |
| [`growth-marketer`](skills/growth-marketer/SKILL.md) | The growth decider - one named constraint from the funnel, a channel mix justified by payback and marginal return, message tested before media, experiments with a sample and a stop rule, and a.... | 2026-11-05 |
| [`performance-ads-buyer`](skills/performance-ads-buyer/SKILL.md) | The paid media operator - structure sized to the learning threshold, audiences without overlap, one creative variable per test, pacing that holds the month, tracking verified before spend, and a.... | 2026-11-05 |
| [`voice-and-audio`](skills/voice-and-audio/SKILL.md) | The audio employee - an edit decision list with timecodes, a nine-step processing chain ending at -16 LUFS, chapters named for the payoff, a voiceover script written to the clock, and clip briefs.... | 2026-11-06 |
| [`copy-editor`](skills/copy-editor/SKILL.md) | The consistency employee - a one-page house style sheet, a terminology ledger with locations, four separate passes, and numbered author queries with a proposed fix instead of a silent rewrite. | 2026-11-06 |
| [`influencer-outreach`](skills/influencer-outreach/SKILL.md) | The creator employee - a shortlist built on audience evidence, a rate ceiling computed from margin, six negotiation levers with rights priced, a one-page brief with the do-not-say list, and a.... | 2026-11-06 |
| [`affiliate-manager`](skills/affiliate-manager/SKILL.md) | The performance-partner employee - commission design under the margin ceiling, recruitment at a scale one person can run, last-click attribution with brand-issued codes, a published fraud ladder,.... | 2026-11-06 |
| [`fundraising-analyst`](skills/fundraising-analyst/SKILL.md) | The raise employee - a model that passes the cash check, a valuation argued from comparables, ten metrics each with a definition, dilution shown after this round and the next, a staged data room.... | 2026-11-06 |
| [`webinar-producer`](skills/webinar-producer/SKILL.md) | The webinar employee - a promise worth an hour, a promotion sequence that fills the room, a run of show with the host's lines, a live room that is actually worked, a 24-hour follow-up split three.... | 2026-11-07 |
| [`customer-success`](skills/customer-success/SKILL.md) | The account employee - a health score with evidence behind every input, a QBR that ends in a decision, a renewal run 120 days out, an expansion play the data has earned, and a save plan with the.... | 2026-11-07 |
| [`knowledge-base-writer`](skills/knowledge-base-writer/SKILL.md) | The help-centre employee - the question counted before it is written, the article titled as the search, the answer in the first line, a task-based structure, deflection measured on tickets and not.... | 2026-11-07 |
| [`collections-agent`](skills/collections-agent/SKILL.md) | The receivables employee - an ageing read that classifies accounts, a per-account dunning ladder with the words ready to send, promises to pay checked on the promised day, a weekly cash view that.... | 2026-11-07 |
| [`investor-relations`](skills/investor-relations/SKILL.md) | The investor employee after the cheque clears - the same date every month, the same five numbers with definitions, last month's promises closed out, misses before wins, bad news to the lead within.... | 2026-11-07 |
| [`board-reporter`](skills/board-reporter/SKILL.md) | The board employee. | 2026-11-07 |
| [`mis-reporter`](skills/mis-reporter/SKILL.md) | The weekly numbers employee. | 2026-11-07 |
| [`inventory-planner`](skills/inventory-planner/SKILL.md) | The stock employee. | 2026-11-07 |
| [`marketplace-lister`](skills/marketplace-lister/SKILL.md) | The listing employee for Indian marketplaces. | 2026-11-07 |
| [`proposal-writer`](skills/proposal-writer/SKILL.md) | The proposal employee. | 2026-11-07 |

## Install

**As a plugin (Claude Code and compatible hosts):**

```
/plugin marketplace add manikant-sharma-ai/employee-hub
/plugin install employee-hub
```

**Manually:** copy the employee folder you want into your skills directory - `~/.claude/skills/` or `.claude/skills/` inside a project.

**Not sure which employee to hire?** Start with `skills/employee-hub-router/`. Give it the job in one sentence; it names the right employee, what to hand over, and which connector is missing.

**Connectors are separate, on purpose.** A skill tells the employee what to do; it does not grant access. Connect the connectors listed under each employee's *Tools it assumes* before expecting it to act. The same employee then works for a business with Gmail and one with Outlook - and it will tell you which connector it needs for the job in front of you.

## Using an employee

Give it the five things in its *What you must be handed* section - the job, a definition of done, connector access, a budget, and what happens if it is wrong. Then let it work. The employees ask for what is missing rather than invent it, so a thin brief produces a question, not a confident wrong answer.

## Putting an employee on a schedule

A skill is the experience; the schedule is what makes it a colleague. `docs/scheduling.md`
covers the four ways to fire a job - your own cron, a GitHub Actions schedule, a
webhook from n8n or Make, or a platform cron - with the exact lines, plus the
weekly and monthly reviews that make the notes and scorecards real.

Two rules travel with every schedule: a schedule does not grant connector access,
and no write action (send, publish, pay, delete) goes on a timer until the same
job has run in draft mode for two weeks.

## The daily drop

Five new employees every morning at 06:00 IST, following `docs/daily-drop.md`. The mix is fixed: two revenue-facing, two operations, one founder-leverage. See `CHANGELOG.md` for what has shipped.

## Adding your own

```
python3 scripts/validate_repo.py        # skills, standard, registry, backlog, secrets
python3 scripts/validate_manifests.py   # plugin.json vs marketplace.json vs registry
```

The first checks the core standard, frontmatter, description quality, required sections,
reference links, the standard wiring (preflight, notes, tracking), registry drift,
backlog runway and accidental secrets. The second catches version and publisher drift
between the three manifest files. Both run on every push via `.github/workflows/validate.yml`.

Read `CONTRIBUTING.md` before you write a skill - it is the contract the validator enforces.

## Licence

MIT. Take what is useful.
