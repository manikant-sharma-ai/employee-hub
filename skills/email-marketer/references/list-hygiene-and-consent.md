# List hygiene and consent

The list is the asset. Hygiene is what keeps it one. Most "deliverability problems" are list problems wearing a technical costume.

## Consent, in the form you can defend

| Source | Consent | Usable? |
|---|---|---|
| Checkout box, unticked, with a stated purpose | Explicit | Yes |
| Signup form with a confirmed email (double opt-in) | Explicit and verified | Yes, the strongest |
| Business card handed at an event | Implied for a short window, not for a newsletter | Ask first, once, personally |
| Trade-show attendee list shared by the organiser | Depends on the notice given at registration | Only if the organiser confirms opt-in language; otherwise no |
| Imported from a previous tool | Only if the original consent travels with it | Usually no - re-permission |
| Scraped, bought, or "enriched" | None | Never |
| Customers who bought, no marketing opt-in | Transactional only | No marketing sends |

Two questions decide every borderline case: **did this person knowingly give this address to this business, and were they told they would get marketing email?** If either answer is unclear, the answer is re-permission, not a send.

**India, DPDP Act:** consent must be free, specific, informed, unconditional and unambiguous, with a clear affirmative action, and it must be withdrawable as easily as it was given. Keep a record of when and how each address consented - a timestamp, a source and the wording shown. If a data principal withdraws, the address stops receiving marketing, and the record of the withdrawal matters as much as the consent.

## The hygiene pass, monthly

| Problem | Test | Action |
|---|---|---|
| Hard bounces | Repeated 5xx from the domain | Suppress immediately, never retry |
| Soft bounces | 4xx, mailbox full, greylisting | Retry twice over 72 hours, then suppress |
| Never-openers | Zero opens in 90-180 days | Sunset: one re-permission email, then remove |
| Role addresses | info@, sales@, admin@ | Keep only if a person asked; they rarely convert and often complain |
| Duplicates | Same address, different case or plus-tag | Deduplicate on lower-cased address |
| Typo domains | gmial.com, yaho.com, .con | Fix or drop; they are spam traps in waiting |
| Spam traps | Addresses that never existed as people | Remove on first hard bounce; never re-add |
| Complaint rate | Above 0.1% of delivered | Stop, find the segment, fix the promise |

A list of 4,000 engaged addresses beats 40,000 unengaged ones on every metric that matters, including revenue. The larger list is not an asset, it is a liability with a delivery cost.

## The sunset sequence

For anyone who has not opened in 180 days:

1. **One email, honest subject**: "Should we stop emailing you?" One link to stay, one to go. No offer.
2. **Seven days.** Non-openers and non-clickers are suppressed, not deleted - keep the record, stop the sending.
3. **Never re-add a suppressed address** without a fresh, explicit signup.

Sunsetting feels like shrinking. It is the only thing that keeps the remaining 70% landing in the inbox.

## Re-permission when a list is suspect

Do not send an offer to a list whose consent is unclear. Send one plain email: who you are, how you got the address, what you would send, and one button to confirm. Everyone who does not confirm is gone. That email is worth the loss - it converts a liability into a small, clean list.

## Anti-patterns

- "We'll send once and see what happens" to a bought list. The domain pays for it for months.
- Buying a list for a launch because the timeline was short.
- Deleting unsubscribes instead of suppressing them - they get re-imported and complain.
- Re-adding bounced addresses because the CRM sync put them back.
- Treating a trade-show badge scan as consent for a monthly newsletter.
- Keeping never-openers "because they might come back" - they will not, and they cost deliverability.
