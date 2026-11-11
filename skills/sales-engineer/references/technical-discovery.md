# Technical discovery

Discovery is not a needs analysis. It is finding the one constraint that decides whether this deal
can be won, and whether it should be.

## The seven things to establish

| # | Question | What it decides |
|---|---|---|
| 1 | What systems are in use, and which versions? | Whether the integration is possible at all |
| 2 | What is the integration surface - API, file, database, middleware? | The effort, and whether it is config or a project |
| 3 | What data, at what volume, at what frequency? | Performance, cost and the POC design |
| 4 | What compliance or data-residency rule applies? | Whether the product can legally be used |
| 5 | Who owns IT, and who signs off? | Whether the evaluation has a decision-maker in it |
| 6 | What is the deadline, and what drives it? | Whether the deal is real this quarter |
| 7 | What would make them say no? | The objection to design around |

If you cannot answer 1, 2 and 5, you are not in an evaluation. You are in a conversation.

## The environment map, drawn in five minutes

```
[Their systems]                                        [Yours]
  ERP / Tally  ----?---->  data export / API  ----?---->  ingestion
  CRM          ----?---->  webhook             ----?---->  sync
  Warehouse    ----?---->  CSV on a drive      ----?---->  manual import
  Identity     ----?---->  SSO / SAML          ----?---->  login
```

Draw it live on the call and ask them to correct it. The corrected picture is the discovery output,
and it is worth more than a page of notes.

| Integration type | Effort | Risk |
|---|---|---|
| Native connector, documented | Hours | Low |
| REST API, their side exposes it | Days | Medium - auth, rate limits, pagination |
| File drop (CSV, SFTP) | Days | Low effort, high operational fragility |
| Direct database read | Weeks, and often refused | High - schema changes, locks, security review |
| Middleware or iPaaS | Days to weeks, plus a licence | Medium - a third party in the critical path |
| No surface at all | Not possible today | Say so immediately |

## Qualification, written as a verdict

| Verdict | Meaning | Next step |
|---|---|---|
| **Fit** | The constraint is addressable with the product as it is | Demo, then POC |
| **Fit with conditions** | Works if X happens - a config, a custom job, a process change, a third party | Name X, its owner and its cost in the proposal |
| **Not a fit today** | The constraint needs a capability that does not exist | Say it, offer the workaround, and keep the relationship |
| **Unknown** | One fact is missing and it decides everything | One specific question, with a date to answer |

A "not a fit today" said in week one is worth more than a technical win in week ten that fails in
implementation. It also gets you referred to the next deal.

## The questions that surface the real constraint

| Ask | Because |
|---|---|
| "Walk me through what happens today, screen by screen." | The workaround is where the pain and the budget are |
| "Who is affected when this goes wrong, and what do they do?" | The real cost of the problem, in a person's time |
| "What have you already tried?" | The failed attempt tells you what they will not accept again |
| "If this worked perfectly, what would change on a Monday?" | The outcome they will be measured on |
| "Who has to say yes, and what will they ask?" | The gatekeeper and the question to pre-answer |
| "What is the deadline driven by?" | A fiscal year, an audit, a contract renewal - each changes urgency |
| "What would make this a no?" | The objection, offered by them, in their words |
| "Which of these three matters most?" | Forces the trade-off that a feature list avoids |

## Red flags, and what they mean

| Signal | Reading |
|---|---|
| No IT owner in any conversation | The evaluation has no decision-maker, or IT will veto late |
| "We just need it to do everything our current system does" | A replacement deal with a migration you have not scoped |
| Requirements that contradict each other | No single owner, or a committee |
| A POC request before discovery | Free development, usually for a competitor comparison |
| Compliance asked about in week six | The deal can die after all the work |
| A deadline that moves twice | The project is not funded, or not prioritised |
| The technical contact cannot name the budget owner | Champion without authority |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| A feature checklist instead of discovery | You demo what you have, not what they need |
| Skipping the environment map | Integration effort is discovered in implementation, at your cost |
| Accepting "we need an API" without the surface | The API is on their side, and it does not exist |
| Never asking what would make it a no | The objection arrives after the demo, and it is fatal |
| No verdict written | The deal stays in evaluation for three months |
| Discovery done by the salesperson alone | The technical questions go unanswered, and the buyer notices |
