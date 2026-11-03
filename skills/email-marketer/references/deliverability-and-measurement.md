# Deliverability and measurement

Landing in the inbox is a reputation problem, not a copy problem. Measurement is where most email reporting quietly lies.

## The technical floor

| Record | What it does | Failure looks like |
|---|---|---|
| SPF | Lists the servers allowed to send for the domain | Mail lands in spam or is rejected outright |
| DKIM | Cryptographically signs the message | Spoofing protection missing, reputation hurt |
| DMARC | Tells receivers what to do when SPF/DKIM fail | Gmail and Yahoo bulk-sender rules are not met |
| Custom sending domain | Sends as `mail.yourbrand.in`, not the ESP's shared domain | One bad sender on the shared IP damages you |
| One-click unsubscribe | Required for bulk senders by major providers | Complaints instead of unsubscribes, which is worse |

**Warm up a new domain** over 3-4 weeks: 200 sends, then 500, then 2,000, watching bounces and complaints. Sending 20,000 on day one from a new domain is the fastest way to lose the domain.

**Bulk sender rules (Gmail, Yahoo, 2024 onwards):** authentication for anyone sending 5,000+ a day, one-click unsubscribe with the header honoured within two days, and spam complaint rates kept under 0.3% - aim for under 0.1%.

## What the numbers mean

| Metric | Healthy range (small B2C list) | What it actually tells you |
|---|---|---|
| Delivered | 97%+ | Whether the list is clean |
| Open rate | 20-40%, inflated | Almost nothing on its own - privacy features and scanners add phantom opens |
| Click rate (of delivered) | 1.5-5% | The real engagement signal |
| Click-to-open | 10-25% | Whether the body delivers on the subject |
| Unsubscribe | Under 0.5% per send | Whether the promise drifted |
| Spam complaint | Under 0.1% | Stop and fix at 0.1% |
| Bounce (hard) | Under 2% | List age |
| Reply rate | Any replies at all | The strongest signal available |

B2B lists in India typically open less and click more than D2C. A 12% open rate on a 400-person B2B list with a 6% click rate is a good send; comparing it to a vendor benchmark is how good sends get "fixed".

## Reading a bad result

| Symptom | Likely cause | First fix |
|---|---|---|
| Opens fell, clicks flat | Apple MPP / scanner noise | Ignore; watch clicks |
| Opens and clicks both fell | Subject or segment mismatch | Check the last two sends against this one |
| Delivered fell | List hygiene | Run the bounce and trap pass |
| Complaints rose | Frequency or a promise drift | Cut frequency, check the offer |
| Unsubscribes spiked on one send | The send was off-promise | Read the send as a subscriber would |
| Everything lands in promotions | Sender reputation, links, images | Authenticate, reduce image-only emails, ask for replies |

## Reporting honestly

Every report carries three lines: the number, what it is compared against, and what it cannot tell you.

> Opens 24% (last four sends: 22-27%). Inflated by machine opens, so treat as directional. Clicks 3.1% of delivered, up from 2.4%. Unsubscribes 0.3%, normal for this list. Revenue attributed ₹48,200 over 72 hours, last-click only.

## Anti-patterns

- Reporting an open rate with no comparison and no caveat.
- Blaming the ESP for a list that has not been cleaned in a year.
- Sending from a shared domain and wondering why one bad neighbour hurts.
- Judging a sequence on its first email only.
- Attributing all revenue in a 30-day window to the last email sent.
- Adding an image-only email "because it looks better" and losing the plain-text readers.
