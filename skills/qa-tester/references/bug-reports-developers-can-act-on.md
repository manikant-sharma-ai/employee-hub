# Bug reports a developer can act on

A bug report has one job: let someone who was not there reproduce the failure on the first attempt. Everything else is commentary.

## The eight fields

```
1. Title        One line: what breaks, where, under what condition.
2. Build        Commit SHA, version, environment (staging/prod), date and time IST.
3. Environment  Browser and version, OS, device, screen size, network.
4. Account      Which test account and role. Never a real customer's credentials.
5. Steps        Numbered, from a fresh state. Include the click that starts it.
6. Expected     What should happen, and where that is written down.
7. Actual       What did happen, in the same terms. Paste the error text verbatim.
8. Evidence     Screenshot or short recording, the request/response, the log line,
                the trace ID.
```

Then: **severity**, **frequency** (always / 1 in 3 / seen once), and **workaround** if one exists.

## Titles that work

| Bad | Good |
|---|---|
| "Payment not working" | "UPI payment of ₹499 shows success, order stays pending (staging, build 4f2a1c)" |
| "UI issue" | "Coupon field overlaps the Pay button at 360px width on Chrome Android" |
| "Login broken" | "Login loop after session expiry when the tab was left open overnight" |
| "Report wrong" | "GST report totals ₹1 less than the invoice when the item price has paise" |

The pattern: **what, where, under which condition**. A title that names the condition is half the diagnosis.

## Severity, as a rule

| Sev | Definition | Example |
|---|---|---|
| 1 | Money, data loss, security, or the product unusable for everyone | Double charge; orders vanish |
| 2 | A core flow is broken for some users, with no workaround | Checkout fails for one payment method |
| 3 | A flow is broken but there is a workaround, or a wrong but recoverable output | Coupon fails, user can pay full price |
| 4 | Cosmetic, or affects a rare path | Misalignment at 320px |

Severity is impact. Priority is order, and it belongs to whoever owns the release. Do not raise severity to move a ticket up the queue - it destroys the scale's meaning within a month.

## Frequency matters as much as severity

"Seen once, on a bad connection" is a different report from "every time, on every device". State how many attempts produced it, out of how many. If you cannot reproduce it, say that plainly and include everything you know - a non-reproducing report with good evidence is still useful; a non-reproducing report that claims certainty is not.

## Evidence that ends the argument

- **The request and the response**, with the status code and the body.
- **The trace ID**, if the stack has one - it turns a symptom into a log search.
- **The console or server error, verbatim.** Not paraphrased.
- **A screenshot with the URL and timestamp visible.**
- **A ten-second recording** of the click that triggers it, for anything timing-related.

## Writing it without blame

Describe the build and the behaviour. "The retry fires twice on a slow connection" is a fact. "The retry logic is broken again" invites a defence instead of a fix. The person reading the report is the person who has to care about it.

## Anti-patterns

- Steps that start with "log in" and skip which account.
- "It doesn't work" with a screenshot of a blank screen.
- Three unrelated defects in one ticket.
- Severity 1 on a cosmetic issue to get attention.
- Marking a defect fixed without a re-test.
- Reporting against production with a real customer's data in the screenshot.
- A report that names a person rather than a build.
