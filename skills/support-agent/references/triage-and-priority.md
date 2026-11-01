# Triage and priority

Triage is the highest-leverage five seconds in support. A correctly triaged ticket reaches the right person once; a badly triaged one is bounced three times and the customer tells the story four times.

## The triage line

Always four fields, always in this order.

```
Category: <what it is about>
Severity: <S1-S4>
Owner:    <who can actually resolve it>
First response due: <time>
```

## Severity, defined by money and risk - not by volume

| Level | Definition | First response | Examples |
|---|---|---|---|
| **S1 - Critical** | Money, safety, legal or data. Someone could be harmed or the business is exposed | Within 1 hour, any hour | Product injury, allergic reaction, data breach, legal notice, payment taken twice, wrong medicine |
| **S2 - High** | The customer cannot use what they paid for, or is actively public | Within 4 working hours | Order not delivered past SLA, wrong item, failed payment with money deducted, damaged goods, public complaint |
| **S3 - Normal** | A real question or issue with a workaround | Within 1 working day | Exchange request, invoice copy, how-to, warranty query |
| **S4 - Low** | Information, feedback, praise, feature request | Within 2 working days | Store timings, "love the product", suggestion |

Rules:

- **Loud is not severe.** The angriest customer of the day may be S3. Severity follows the consequence.
- **Money already taken is always S2 or above.** Nothing corrodes trust faster than a payment with no product.
- **A public channel raises severity by one level** while it is public.
- **Repeat contact raises severity by one level.** Third message on the same ticket is an S2 whatever it is about.
- **When unsure between two levels, choose the higher one** and downgrade later. Under-triaging is the expensive error.

## Categories worth having

Twelve to fifteen is right. More, and nobody uses them consistently.

| Category | Goes to |
|---|---|
| Order status / not delivered | Logistics owner |
| Wrong / damaged / missing item | Warehouse owner |
| Return / exchange | Returns owner |
| Refund not received | Accounts owner |
| Payment failed / double charged | Accounts or gateway owner |
| Product question (pre-sale) | Sales or the product owner |
| Product how-to / usage | Support with a help article |
| Warranty / repair | Service partner |
| Billing / invoice / GST | Accounts owner |
| Account access / login | Technical owner |
| Feature request | Product owner (logged, not answered) |
| Complaint about staff or service | Operations head |
| Legal / regulatory / media | Founder, immediately |
| Safety or injury | Founder, immediately |

## Routing rules that save a day

- **Route to a role, not a person**, and have the role map to a name. People leave; the queue should not.
- **Every ticket has exactly one owner at a time.** Shared ownership means nobody owns it.
- **The owner is the person who can resolve it, not the person who is closest to it.** Routing a refund query to support so support can ask accounts is a wasted hop.
- **Anything requiring a write action** (refund, replacement, address change, cancellation) goes to whoever holds that authority - see `references/escalation-and-refund-authority.md`.
- **Bulk-close duplicates against the first ticket**, and tell the customer which one is the live one.

## Batching and the inbox rhythm

| Slot | What to do |
|---|---|
| First 30 minutes of the day | Clear S1/S2 and anything past SLA. Nothing else |
| Mid-morning | S3 batch, grouped by category so the context switches once |
| Mid-afternoon | Follow-ups promised for today, then new arrivals |
| Last 20 minutes | Set tomorrow's promises; nothing new gets a "today" reply |

Two rules: **never let an S2 sit past its first-response window to clear S3s**, and **never end the day with an unanswered promise dated today**.

## What to do with a message you cannot classify

1. Read it twice. Most unclassifiable messages contain two issues stapled together - split them.
2. If the customer wrote in a language or script you can reply in, reply in it; do not route it away because it is unfamiliar.
3. Ask one clarifying question, and in the same message do the part you can already do. "I have found your order and raised a trace; to know what you want, do you want a replacement or a refund?"
4. Never send a bare "please provide more details". It is the most-ignored reply in support.

## Volume signals worth noticing

Write these in the journal weekly; they are the cheapest product feedback the business gets.

- **Top three repeat questions** - each one is a missing help article or a confusing page.
- **Spike in one category** - a batch problem, a broken courier route, a bad listing.
- **First-response time trend** - the leading indicator of everything else.
- **Reopen rate** - the honest measure of whether replies actually solved anything.

## Anti-patterns

- Triaging by how angry the customer sounds.
- A category list of forty that nobody maintains.
- Routing to a person who is on leave.
- Leaving a ticket in a "pending customer" state when the ball is actually with you.
- Closing a ticket because a reply was sent, rather than because the issue was resolved.
- Answering the easy half and silently dropping the hard half of a two-issue message.
