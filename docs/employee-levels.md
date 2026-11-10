# Employee levels, and the fields a registry entry now carries

Every employee in this hub is registered with an authority level, a category, a
permission set, a cost band and its connector position. This file defines what those
values mean, so that "L2" is a statement rather than a label.

## The level ladder

The level describes **what an employee is allowed to do in a system**, not how clever it
is. A high level is not a promotion; it is a wider blast radius.

| Level | Name | What it may do | Approval |
|---|---|---|---|
| **L0** | Answer | Works only from what the person pastes or says. No system access. Produces a document, a plan or an opinion. | none needed - nothing outside the conversation changes |
| **L1** | Read and draft | Reads connected systems, produces documents, drafts applications and answer sheets. Writes nothing back, sends nothing out. | a human sends, files and certifies |
| **L2** | Prepare | Prepares changes inside a connected system - a collection, a journal entry, a budget version, a ticket update - and leaves them for approval before they take effect. | a named human approves each change |
| **L3** | Act | Acts in systems within a stated limit: sends, publishes, posts, updates records. Every action is logged and reversible where the system allows. | standing approval with a stated limit and an audit trail |
| **L4** | Commit | Spends money or commits the business: pays, orders, bids, signs, files. | explicit per-action approval, never standing |

Rules that hold at every level:

- **A missing connector lowers the level, never raises it.** An L3 employee with nothing
  connected behaves as an L0 and says so.
- **The level is a ceiling, not a target.** An employee that could act but has not been
  given the connector still does not act.
- **Never fake the level.** An employee that describes an action it did not take is
  violating the standard regardless of its registered level.

## Category

One of three, and it matches the five-a-day mix:

- **revenue-facing** - brings money in or stops it leaking.
- **operations** - saves hours every week.
- **founder-leverage** - work the founder would otherwise do personally, and badly.

## Permissions

Three lists, and the third is the interesting one:

```
"permissions": {
  "read":  ["what it may look at"],
  "write": ["what it may change, and at which level"],
  "never": ["what it must not do even when asked"]
}
```

The `never` list is what makes a permission set meaningful. An employee with an empty
`never` list has not been thought about.

## Cost

A band, its drivers, and an honest note. This is a design estimate, not a measured bill.

```
"cost": {
  "band": "low | medium | high",
  "est_tokens_per_task": "range",
  "drivers": ["what makes a task expensive"],
  "paid_dependencies": ["subscriptions or APIs the role assumes"]
}
```

## Connector availability

Three lists, so a person knows what will work the moment they load the employee:

```
"connector_availability": {
  "connected_by_default": [],          // nothing is connected by default in this hub
  "needs_user_connect": ["what to connect, ranked"],
  "unavailable": [{"connector": "...", "fallback": "what to do instead"}]
}
```

The `unavailable` list is the honest one: a portal with no API, a marketplace with no
write access, a bank that only exports CSV. Naming the fallback is part of the job.

## Status and reliability

- **status** - `probation` for a new employee until it has run real tasks, then `stable`.
- **reliability** - `unverified` until there is evidence in `notes/journal/`, then
  `verified` with the date and the evidence.

A `probation` employee is shippable. A `verified` one has earned the word.
