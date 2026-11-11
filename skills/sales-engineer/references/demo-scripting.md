# Demo scripting

A demo is an argument with screens. If the buyer cannot retell it to their boss in three sentences,
it was a tour.

## The three-act structure

| Act | Length | Content |
|---|---|---|
| **1. Their world** | 3 min | Restate the problem in their words, on their data, with the cost |
| **2. The change** | 12-15 min | Three workflows, end to end, in the order their day happens |
| **3. The proof** | 5 min | The number that moved, the control that holds, the thing that surprised them |

Never open with the product. Open with their Monday morning.

## The demo plan, filled in before you build anything

| Field | Content |
|---|---|
| Audience | Name and role of each person, and what each cares about |
| The one decision | What they must decide as a result of this call |
| Three workflows | The exact paths, in their language |
| Data | Their extract, or a replica built from their field names and volumes |
| The two moments | The two places where they will say "oh" - one saved step, one saved hour |
| The known gaps | Where the product does not do it, and what you will say |
| The failure path | What you do if a step breaks |
| The close | The specific next step, with a date |

## Tell, show, tell

For every workflow:

```
TELL   "Today your team re-keys the PO into Tally. Two people, about 40 minutes a PO."
SHOW   [do it in 90 seconds, on their data, narrating what a user would click]
TELL   "So that is 40 minutes gone, and here is the error it causes at month end."
```

The second TELL is the one that gets repeated upward. Without it the buyer remembers features.

## Data preparation

| Rule | Why |
|---|---|
| Use their field names, not yours | A demo in their vocabulary is a demo of their future |
| Match their volume | A demo with 12 rows for a 40,000-row business reads as a toy |
| Include one dirty record | Because their data is dirty, and handling it builds credibility |
| Include a realistic exception | A cancelled order, a part shipment, a GST credit note |
| Never use "Acme Corp" and "John Doe" | It signals a rehearsed generic demo |
| Have a fallback: screenshots or a recording | The environment will fail at the worst moment |

## Handling the questions that come mid-demo

| Question | Answer pattern |
|---|---|
| "Can it do X?" (it can) | "Yes - I will show it in two minutes, after this step." Then do |
| "Can it do X?" (it cannot) | "Not today. The workaround is Y, and it costs Z. It is on the roadmap as planned, not committed." |
| "Can it do X?" (you do not know) | "I do not know - I will confirm today and send it in writing." Then do, same day |
| "Our process is different" | "Show me where it diverges - if it is a config, I will prove it now" |
| "How does it scale?" | A number you have read, with the condition: "at N records, ingestion takes M minutes" |
| "What about security?" | The specific control, not the word "enterprise-grade" |

Never answer a capability question with "absolutely". It is the phrase that ends deals in
implementation.

## The failure path

Decide before the call:

1. **The step is slow** - narrate the delay with the reason, and keep moving.
2. **The step errors** - say what the error means, show the log or the message, and switch to the
   fallback. Do not debug live for more than 60 seconds.
3. **The environment is down** - switch to the recording, and say plainly that you are doing so.
4. **The data is wrong** - acknowledge it, and note that it is exactly why the POC exists.

A handled failure builds more trust than a flawless script. An unhandled one, with silence, does the
opposite.

## The close of the demo

| Element | Example |
|---|---|
| Restate the decision | "You need to decide by the 28th whether to run a POC on the stock sync." |
| The next step | "I will send the POC plan today with three success criteria for your sign-off." |
| The named owner | "Ramesh owns the data extract; I need it by Tuesday to start on the 12th." |
| The risk named first | "The one thing that could stop this is your API's rate limit - I will spike it this week." |

## Remote demo hygiene

| Check | Why |
|---|---|
| Screen resolution and zoom set so text is readable | Half of remote demos are unreadable |
| Notifications off, tabs closed | A customer name in a browser tab is a confidentiality incident |
| Two people: one presents, one watches the chat | Questions in chat are lost otherwise |
| Recording, where permitted | The champion needs it to sell internally |
| A follow-up within 24 hours | With the recording, the answers, and the next step |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| A feature tour | Impressive, unmemorable, and not repeatable upward |
| Demo on generic data | The buyer cannot see themselves in it |
| Showing the roadmap as if it were the product | Discovered in implementation |
| "Absolutely, it can do that" | The most expensive sentence in software sales |
| Debugging live for ten minutes | The audience leaves the call |
| No clear next step | The deal drifts, and the champion has nothing to forward |
| Demoing to the wrong room | The technical buyer was not there, so it will be re-run |
| Ten workflows | Nobody remembers past three |
