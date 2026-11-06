# Levels, categories, permissions and cost

Every employee in `registry.json` declares the same seven facts, because "an AI
employee" is not a job description. A role that cannot say what it may touch, what
it costs and whether it has ever been checked is a demo, not a colleague.

`scripts/validate_repo_v2.py --strict` enforces this file. A field that is missing,
guessed or out of the enumerated set fails the build.

## Level - how far the employee may act without a person

Level is about **action**, never about quality or seniority. A brilliant analyst
that may only read is L0. A mediocre one that may send is L3.

| Level | Name | May do | May not do |
|---|---|---|---|
| **L0** | Read and report | Read connected systems, analyse, answer in chat | Produce a file, change anything |
| **L1** | Draft for approval | Produce the artefact - email, article, deck, update - for a person to send or publish | Send, publish, post, pay, or write to a system of record |
| **L2** | Prepare the write | Stage a record in a connected system (a ticket, an article, an event, a CRM note) with a named approver and a diff | Complete the write without that approval, or repeat a rejected write |
| **L3** | Execute approved actions at scale | Run a sequence of writes inside a pre-agreed limit - recipients, spend, records per run | Exceed the limit, change the limit, or act outside the written policy |
| **L4** | Autonomous within policy | Run on a schedule inside a written policy, with a log and a reversal path | Act on anything the policy does not name |

Two rules sit above the table:

1. **A new employee ships at L1 or L2, never higher.** Level rises on evidence
   from `notes/journal/`, not on ambition. `status: probation` and
   `reliability: unverified` are the honest defaults for a first drop.
2. **Money out and money in are L1 until measured.** Anything that moves cash,
   changes a price, or contacts a customer about a debt is drafted, never sent,
   until the first-pass acceptance rate is known.

## Category - the mix the drop is balanced against

| Category | What it means | Examples shipped |
|---|---|---|
| `revenue` | Brings money in, or stops it leaking | `sales-outreach`, `affiliate-manager`, `webinar-producer` |
| `operations` | Saves hours every week inside the business | `bookkeeper`, `compliance-watch`, `collections-agent` |
| `founder-leverage` | Work the founder would otherwise do personally, and badly | `chief-of-staff`, `pricing-analyst`, `investor-relations` |
| `product` | Makes the thing the business sells exist | `product-manager`, `ui-designer`, `qa-tester` |
| `infrastructure` | The hub itself - routing, validation, scheduling | `employee-hub-router` |

The daily mix is two `revenue`, two `operations`, one `founder-leverage`. A
`product` or `infrastructure` role only ships when it closes a boundary a shipped
employee already routes to.

## Permissions - what it may touch

Permissions are declared per resource, not per tool, because the same connector
carries a read and a write. Each entry is `<resource>:<scope>`, where scope is one
of `read`, `write`, `send`, `spend`, `delete`.

```json
"permissions": {
  "read": ["mail.inbox", "calendar", "crm.deals", "sheets"],
  "write": ["helpdesk.articles:draft"],
  "send": [],
  "spend": [],
  "delete": []
}
```

- **`send` and `spend` are empty for every employee at L1.** An empty list is a
  claim; a missing list is a bug.
- **`delete` is empty for every employee in the hub.** Nothing here deletes a
  record it did not create in the same run.
- **Write scopes carry the mode** - `draft`, `staged`, `approved` - so a reader can
  see how far the write actually goes.

## Cost - what a task costs, as a range

Cost is per typical task, not per token, because that is the number a founder can
compare with a salary.

```json
"cost": {
  "model_tier": "standard",
  "est_tokens_per_task": 18000,
  "est_cost_inr_per_task": [4, 12],
  "paid_tools": ["Zoom Webinars (optional, replaces Google Meet)"],
  "basis": "one task = one artefact; a 60-ticket batch costs 6-8x"
}
```

- `model_tier` is `small`, `standard` or `frontier` - the smallest tier that does
  the job, and the reason belongs in `basis`.
- The range is honest: a thin brief costs less and delivers less.
- A paid tool is listed even when it is optional. Recommending a subscription the
  person does not need is a cost, not a feature.

## Connector availability - the four states

Every employee states what it needs and whether the hub can actually reach it.
This is the preflight in `core/connector-preflight.md`, written down once.

```json
"connectors": {
  "available": ["Google Sheets", "Gmail", "Google Calendar"],
  "needs_setup": ["Zoho Books (receivables ledger)", "Razorpay (payment status)"],
  "usable_on_day_one": true,
  "fallback": "paste the ageing export; the ladder and the letters still ship"
}
```

| State | Meaning | What the employee does |
|---|---|---|
| `available` | A connector in the hub's own inventory that most users already have | Uses it, and says which one it read |
| `needs_setup` | Right tool, not connected | Names it, one line, and delivers the part that does not need it |
| `unavailable` | No connector exists for the job (audio, capture, signature) | Says so and hands over a manual path - never a substitute |
| `paid` | Works, but costs money per use | Says the cost before using it |

`usable_on_day_one` is `true` only when at least one item in `available` is enough
for a real first task. A skill that cannot answer anything without a paid tool is
not shippable.

## Status and reliability

| Field | Values | Meaning |
|---|---|---|
| `status` | `probation`, `stable`, `retired` | `probation` = shipped, not yet trusted with a write; `stable` = survived a monthly scorecard |
| `reliability` | `unverified`, `measured`, `degraded` | `unverified` = no scorecard exists; `measured` = a month of `notes/journal/` exists with a first-pass acceptance number |

A drop sets `probation` and `unverified` on every new employee. Promoting either
field is a separate commit with the journal entry that justifies it, so "stable"
means something.
