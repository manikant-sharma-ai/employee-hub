# SaaS licence audit

A SaaS bill is seats times price, and both halves drift. This file is how each half is measured.

## Seats: bought against active

| Evidence | Quality | What it proves |
|---|---|---|
| SSO / identity provider login log, 30 and 90 days | Best | Who actually authenticated, and when |
| The vendor's own last-login column | Good | Same, scoped to one vendor |
| A survey of the team | Weak | Intentions, not usage |
| An invoice and an assumption | None | Nothing |

The rule: 30-day active is the working number, 90-day active is the reinstatement risk. A seat inactive for
90 days is a candidate; a seat inactive for 30 is a question for the owner.

| Pattern | Reading | Action |
|---|---|---|
| 30 seats, 11 active, 9 people in the team | Bought at a peak and never revisited | Downgrade at renewal to active + 20% |
| 30 seats, 29 active | Genuinely used | Look at the tier, not the count |
| 10 seats, 22 people using the tool | Shared logins | A compliance and security finding, and a renewal surprise |
| Seats active but only for one feature | The tool is being used as something else | Find the cheaper tool for that job |

Shared logins are common in Indian SMBs and are always worth naming, once, factually: the vendor's audit
clause, the lost audit trail, and the person who leaves with the password.

## Tiers: what the plan actually includes

| Upgrade trigger the vendor sells | Ask first |
|---|---|
| "Unlimited projects" | How many do you have, and what is the limit on the current plan |
| "Advanced analytics" | Who has opened the analytics tab in the last 90 days |
| "Priority support" | What the SLA actually is, and whether it has ever been used |
| "API access" | Whether the integration exists yet |
| "SSO" | Whether the business has an identity provider at all |
| "Audit logs" | Whether a compliance obligation requires them - if yes, this one is not optional |

Downgrading is the cheapest saving in the whole review and the one nobody does, because the upgrade happened
during a trial and the invoice has looked the same since.

## Overlap: the consolidation map

| Function | Typical stack in an Indian SMB | Consolidate to |
|---|---|---|
| Design | Canva + Figma + Adobe + a stock subscription | One primary, one for stock |
| Communication | Slack + Teams + WhatsApp + email | One internal, WhatsApp for customers |
| Project tracking | Trello + Notion + Asana + a spreadsheet | One, plus the sheet for the numbers |
| Analytics | GA4 + a BI tool + a dashboard tool + a heatmap | GA4 plus one BI |
| Files | Drive + Dropbox + a NAS + WhatsApp | One cloud, one backup |
| Support | A helpdesk + a shared inbox + WhatsApp | One helpdesk |
| CRM | A CRM + a spreadsheet + the founder's phone | One CRM |

Consolidation is not always the answer. Two tools that overlap by feature but differ in the job people
actually do are not duplicates. The test: could the owner move their work to the other tool this week without
losing something they use daily? If not, it is not an overlap.

## The renewal calendar and its arithmetic

| Field | Why |
|---|---|
| Charge date | When the card is debited |
| Notice period | 30, 60 or 90 days - the real deadline |
| Auto-renew clause | Whether silence renews for a year |
| Price escalation clause | The annual uplift already agreed |
| Minimum commitment | What must be paid even if cancelled |
| Data export window | How long after cancellation the data is available |

Sort the calendar by **notice deadline**, not charge date. A 90-day notice on a charge in March is a decision
in December, and that is the date that belongs in the founder's diary.

## The negotiation levers, in order of strength

1. **A credible alternative.** A quote from a competitor changes the conversation more than any argument.
2. **Timing.** The last week before renewal is the worst time to ask; three months before is the best.
3. **Term.** A two-year commitment for a 15-20% discount is real value if the tool is load-bearing, and a trap
   if it is not.
4. **Payment terms.** Annual prepay in exchange for a discount, if the cash position allows - check with
   `treasury-ops`.
5. **Seat true-up.** A commitment to a realistic seat count is often worth more to the vendor than the price.
6. **Bundling.** Two products from one vendor can be cheaper than one from each - and lock you in further.

## Anti-patterns

- **Cancelling on the last day.** The auto-renew has already run, and the year is committed.
- **Downgrading without exporting.** The plan change can remove history, and the history is the business.
- **Consolidating onto the tool the loudest person prefers** rather than the one with the data in it.
- **Reading the invoice as the contract.** The order form and the terms decide the notice period; the invoice
  only tells you the price.
- **Ignoring the seat count on a usage-based plan.** Per-active-user pricing punishes a team that shares
  logins, and rewards the audit.
