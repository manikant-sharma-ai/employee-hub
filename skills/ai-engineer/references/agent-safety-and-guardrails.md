# Agent safety and guardrails

An agent with tools can do damage that a chatbot cannot. The guardrail is not a
polite instruction in the prompt; it is a boundary the system enforces.

## The four boundaries

| Boundary | Enforced by | Example |
|---|---|---|
| Permission | The tool's own auth, scoped per user | The agent reads only the files this user can read |
| Consequence | Human approval before an irreversible action | Send, publish, pay, delete, deploy |
| Content | Input and output filters, plus a refusal path | No PII into a third-party model; no unverified medical claim |
| Blast radius | Limits per run | Max 20 emails per run, max ₹5,000 per transaction, max 50 file writes |

A prompt line is not a boundary. If the rule must hold when the model is wrong,
confused or manipulated, it belongs in code.

## Prompt injection, in practice

Anything the model reads can carry instructions: a web page, a PDF, an email, a
ticket, a spreadsheet cell, a filename. Rules:

- **Treat retrieved and fetched content as data, never as instructions.** Delimit it, label it, and tell the model that content inside the block is not a command.
- **Never let a tool call be justified only by content the model read.** The user's request authorises actions, not the document.
- **Strip or ignore instructions found in data**, and surface them: "this document contained an instruction to email a file; I did not act on it."
- **No tool that can exfiltrate on the same run as a tool that can read secrets.** Separate them or require approval.

## The approval gate

Require explicit human approval for: sending on someone's behalf, spending money,
publishing, deleting, changing permissions, deploying, and any write to a system
of record. Two design rules:

- **Show the exact payload** being approved, not a summary. "Send this email" with no body is not an approval.
- **One approval, one action.** A batch approval that covers 200 sends is a single keystroke with 200 consequences.

## PII and data handling

- **Classify before you send.** Names, phone numbers, addresses, health and financial data do not go into a third-party model unless the contract and the law allow it.
- **Under India's DPDP Act, consent and purpose limitation apply to AI processing** exactly as they do to a database. Keep the record of what was sent where.
- **Redact in logs.** Prompts and completions are logs, and logs get shared.
- **Say where data goes.** A user handing over a spreadsheet deserves to know which model provider sees it.

## Output guardrails that matter

- **Ground every factual claim** in a retrieved source or the user's input; refuse otherwise.
- **Refuse to produce content for a prohibited category**, and say why in one line.
- **Check numbers with code, not with the model.** Arithmetic, dates, totals and unit conversions go through a function.
- **Never let the model state a legal, tax or medical conclusion as fact.** It drafts and flags; a professional signs.

## Monitoring that catches the failure

- Log every tool call: what, on whose behalf, what was returned.
- Alert on: a spike in refusals, a spike in tool errors, any action above the blast-radius limit, and any run that touched a new system for the first time.
- Keep a kill switch that stops the agent without a deploy.

## Anti-patterns

- "Please do not delete anything" as the only protection.
- An agent with write access to production and read access to everything.
- Approval fatigue: 40 prompts a day, so the human clicks yes.
- No audit log, so an incident cannot be reconstructed.
- Shipping with no refusal path because refusals looked bad in the demo.
