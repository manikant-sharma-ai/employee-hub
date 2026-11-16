# Billing case - <invoice or dispute id>

**Customer:** <account id> | **Plan:** <plan> | **Amount:** <currency> <amount> | **Owner:** <name>
**Opened:** <YYYY-MM-DD> | **Deadline (if a dispute):** <YYYY-MM-DD> | **Status:** <open / waiting on customer / closed>

## Diagnosis

| Field | Value |
|---|---|
| What failed | <renewal / one-off payment / refund / dispute> |
| Gateway code | <code> - <the gateway's own message> |
| Date and time of the attempt | <YYYY-MM-DD HH:MM IST> |
| Attempts so far | <n>, on <dates> |
| Ours or theirs | <our configuration / the customer's card / the issuer / unknown> |
| Access right now | <full / grace until <date> / downgraded / suspended> |

## The reply (draft - the owner sends)

> Subject: <what happened, with the date>
>
> Hi <name>,
>
> <Line 1: what happened, in plain words, and whether it was our fault.>
> <Line 2: what it means for their access, with the date.>
> <Line 3: the one action, with the link.>
> <Line 4: what happens if they do nothing, and when.>
>
> <Name>, <role>

**Language:** <English / Hindi / other> | **Checked for gateway jargon:** <yes>

## Ladder position

| Rung | Date | Message sent | Delivered | Recovered |
|---|---|---|---|---|
| 0 | <date> | <template key> | <yes/no> | <yes/no> |
| 1 | <date> | <template key> | <yes/no> | <yes/no> |

Next action: <rung, date, channel, owner>

## Dispute pack (if applicable)

| Evidence | Have it? | Where it is | Proves |
|---|---|---|---|
| Terms accepted at checkout (timestamp, IP) | <yes/no> | <link> | Authorisation |
| Dispatch and delivery proof | <yes/no> | <link> | Received |
| Usage or consumption log | <yes/no> | <link> | Service delivered |
| Customer's own messages | <yes/no> | <link> | Context |
| Refund or cancellation record | <yes/no> | <link> | No duplicate |

Response due: <YYYY-MM-DD> | Submitted: <YYYY-MM-DD> | Outcome: <won / lost / pending>

## Refund trail (if applicable)

| State | Date | Reference | Note |
|---|---|---|---|
| Initiated | <date> | <gateway refund id> | <method> |
| Settled | <date> | <reference> | <confirmed by> |

## The one process fix

- **Fix:** <what changes - the retry schedule, the template, the suspension rung, the delivery proof>
- **Owner:** <name> | **Date:** <YYYY-MM-DD>
- **Metric it moves:** <recovery rate / days to reply / disputes lost>

## What I could not verify

- <gateway not connected / credit note not posted / no delivery proof>
- Verified by: <connector used, or "not verified - <what is missing>">
