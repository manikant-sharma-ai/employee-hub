# ICP and list building

The list is the strategy. A mediocre email to a perfect list outperforms a perfect email to a mediocre one, every time, and it is not close.

## Define the ICP as a test

An ICP you cannot test is a wish. Write it as three must-haves, two nice-to-haves and three disqualifiers, then run every row through it.

| Element | Example - inventory software for auto-parts makers | Why it is written this way |
|---|---|---|
| Must-have 1 | Manufactures or stocks physical parts, 20-500 employees | Below 20 there is no process to fix; above 500 the sale is a tender |
| Must-have 2 | Runs 2+ warehouses or godowns | The pain is reconciliation across locations; one location needs a spreadsheet |
| Must-have 3 | Sells to OEMs or tier-1 suppliers | OEM contracts impose audit and traceability requirements |
| Nice-to-have | Uses Tally already | Data is there to migrate; shortens the first call |
| Nice-to-have | Listed on IndiaMART | Digital already, so a reply is likely |
| Disqualifier | Already on SAP or Oracle | Procurement cycle measured in quarters, not weeks |
| Disqualifier | Group company of an existing customer | Route through the account owner instead |
| Disqualifier | Government or PSU buyer | GeM tender, not outbound |

## Sanity-check the arithmetic before building

Do the maths out loud, because it usually kills the plan in one line.

| Input | Value |
|---|---|
| Meetings needed per month | 12 |
| Meeting rate from reply | 30% |
| Replies needed | 40 |
| Reply rate on a verified list | 5% |
| Contacts to reach per month | 800 |
| New contacts per working day | ~40 |

If the ICP can only produce 300 contacts in total, outbound cannot carry the number - say that and propose the alternative (partner channel, marketplace, inbound) instead of quietly running a 300-person list six times.

## Where the rows actually come from, for an Indian business

| Source | Best for | What it gives | Check before use |
|---|---|---|---|
| LinkedIn / Sales Navigator | Roles in mid and large firms | Name, title, company, tenure | Confirm the person is still in the role |
| IndiaMART buyer enquiries and seller listings | B2B trade, wholesale | Company, product line, city, phone | Verify the business exists; many listings are stale |
| MCA21 company master data | Legal existence, directors, incorporation date | CIN, status, registered state | Check status is Active, not Strike Off |
| GeM bid history | Who buys what from government | Past orders, quantities, values | Only for suppliers already registered on GeM |
| GSTIN check (public validation) | Whether a B2B buyer is registered and active | Registration status, state code | Never assume turnover from a GSTIN |
| Trade associations and exhibitions | Niche industrial segments | Member lists, exhibitor lists | Exhibitor lists age fast - confirm the company still exists |
| Google Maps / JustDial | Local retail, clinics, restaurants, studios | Address, phone, hours | Phone numbers are often the owner's, so respect DND |
| Lookalikes of best customers | The highest-yield list there is | Same size, same trigger, same role | Do not simply copy a competitor's customer list |

## The list schema

Every row carries these columns, and nothing else is optional.

| Column | Rule |
|---|---|
| `company` | Legal or trading name, no "Pvt Ltd" duplication in two spellings |
| `domain` | The real corporate domain, not a Gmail address |
| `contact_name` | First and last, spelled as on LinkedIn |
| `role` | The title that matters for this offer |
| `email` | Work address only, one per contact, verified |
| `phone` | E.164 with +91, only if the channel will be used |
| `city`, `state` | For territory and send-window rules |
| `trigger` | The one line explaining why this row exists now |
| `source` | Where the row came from, with the date |
| `verified_on` | Date the email was checked |
| `status` | new / contacted / replied / meeting / disqualified / suppressed |

## Verification, in order of cheapness

1. **Syntax and domain** - reject obvious typos and free-mail domains for B2B.
2. **MX record** - a domain with no mail server cannot receive.
3. **Catch-all detection** - catch-all domains accept everything, so a "valid" result proves nothing; cap them or drop them.
4. **Pattern check** - if the company uses `first.last`, one verified address confirms the pattern for the rest. Never guess a pattern without one confirmed sample.
5. **Suppression** - remove existing customers, open deals, unsubscribed, competitors, and anyone who said no.

## Dedupe rules that prevent real damage

- Same domain + same contact = one row, keep the newest verified email.
- Same company, two contacts = keep both, but sequence them 7+ days apart, and never send to both in the same week if they report to each other.
- Open deal in the CRM = do not touch; the account owner is already talking.
- Former customer = route to the account owner, not to outbound.

## Anti-patterns

- **Buying a 50,000-row database.** Bounce rates above 3% get a domain filtered, and the loss is the whole mailbox, not one campaign.
- **Building the list after writing the email.** You end up writing to whoever you could find rather than to who buys.
- **Counting "decision-makers" you cannot name.** A row without a named human is not a row.
- **Personalising with a field that is wrong.** "Love what you're doing in logistics" sent to a pharma company is worse than no personalisation at all.
- **Reusing last year's list.** Roles change; 30-40% of a B2B list is stale within a year.
- **Ignoring the trigger.** The reason to write now is the only thing that separates outreach from spam.
