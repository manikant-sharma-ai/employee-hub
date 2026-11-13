# Quotes and privacy

A quote is the most persuasive thing in a readout and the easiest way to break a customer's trust.
Both facts are permanent.

## Selecting a quote

| Test | Pass | Fail |
|---|---|---|
| Verbatim | Copied exactly, including the typo | Tidied into better English |
| Representative | Says what the theme says | The most extreme sentence in the file |
| Specific | Names the moment and the detail | "Bad service" |
| Attributed | Segment, tenure, date | A name, a company, a phone number |
| Permission-safe | Nothing that identifies a person | "Our founder, Mr X, told me..." |

Two or three per theme is enough. A readout with twelve quotes per theme is a readout nobody reads.

## The attribution line

The useful attribution is the one that makes the quote credible without identifying anyone:

> "SMB, 8 months, ticket 14/10" | "Enterprise, renewal call, Sept" | "Play Store, 2 stars, 03/11"

Not: a name, a company, a city small enough to identify a single shop, a job title plus a company.

## Personal data, in the Indian context

- **DPDP Act, 2023** governs personal data. A feedback readout is a secondary use, and the safest
  position is to keep it internal, aggregate it, and never publish a quote that identifies a person
  without consent.
- **Never put exports in the repo.** Ticket bodies, survey CSVs, WhatsApp threads - none of them
  belong in version control, and the repo is public.
- **Never quote a health, financial or family detail** even when the customer volunteered it. It is
  irrelevant to the theme and it is the detail that makes a complaint identifiable.
- **Public reviews are public, not free to reuse.** Quoting a Google review internally is normal;
  putting it in marketing without permission is a different act.

## The permission question

| Use | Permission needed |
|---|---|
| Internal readout, segment attribution | No, if unidentifiable |
| Board or investor deck, segment attribution | No, if unidentifiable |
| Marketing, website, case study | Yes, in writing, and say where it will appear |
| A public post quoting a named customer | Yes, in writing, with the exact wording approved |
| A quote in a job posting or pitch | Yes - and never paraphrase it |

## Anonymising without destroying the point

| Original | Anonymised | Why it still works |
|---|---|---|
| "Ramesh from Sharma Traders said the invoice was wrong" | "A 12-person distributor: 'the invoice did not match the PO'" | The detail that matters is the failure, not the person |
| "Our ₹40 lakh order was delayed" | "A large order was delayed by nine days" | Scale without identification |
| "The founder, Ms Iyer, called us" | "A senior stakeholder called directly" | The escalation is the point |

If a quote cannot survive anonymisation, it is not a quote for a readout. Use the count instead.

## Quoting a customer who is angry

- Quote the substance, not the insult.
- Never quote profanity or a personal attack, even verbatim. Paraphrase the complaint and mark it as
  a paraphrase.
- Never quote something said in confidence in a call without permission.
- Never quote a customer who is in an active dispute with the business.

## Anti-patterns

- **A quote with a name in a public repo.** It is a data-protection incident, not a style choice.
- **Fixing grammar inside quotation marks.** If it needs fixing, paraphrase and mark it.
- **Choosing the quote that makes the point most strongly** rather than the one that represents the
  theme. That is how a readout becomes advocacy.
- **Quoting the same three customers every quarter.** The readout starts to look like their agenda.
- **A quote with no date.** It may be three years old and describing a product that no longer exists.
