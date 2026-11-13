# Enrichment and data quality

A batch of 200 names is a data problem before it is a qualification problem. Fix the fields, then
score - not the other way round.

## The minimum viable lead record

| Field | Required | Source | If missing |
|---|---|---|---|
| Company name | Yes | Form | Decline as unusable |
| Contact name and role | Yes | Form | D band - one question |
| Work email or phone | Yes | Form | Decline as unusable |
| Industry | Yes | Form, website, LinkedIn | Infer from website, mark inferred |
| Employee count or turnover band | Strongly preferred | LinkedIn, MCA, GSTIN | Unknown, scores zero |
| City and state | Yes | Form | Ask in the first reply |
| What they want, in their words | Yes | Form text | The enquiry is unusable without it |
| Source channel | Yes | Form metadata | Ask the person who forwarded it |
| Arrival timestamp | Yes | Form metadata | Ask; the SLA depends on it |

Two fields decide most scores and are almost always missing: **employee count** and **what they are
using today**. Both are answerable in one question, which is why D band exists.

## Verification, in order of cost

| Check | Cost | What it proves |
|---|---|---|
| Website homepage and pricing page | 30 seconds | What they sell, roughly how big |
| LinkedIn company page | 30 seconds | Headcount band, locations, recent hiring |
| MCA company master data | 1 minute | Entity exists, type, incorporation date, directors |
| GSTIN lookup | 1 minute | Registered, state, active status |
| Google Maps listing | 30 seconds | Physical presence, multiple branches |
| News search | 1 minute | Funding, expansion, distress |
| A call | 10 minutes | Everything else |

Do the cheap checks on A and B candidates only. Verifying 200 names to score them is a week of work
that produces the same twenty.

## Deduplication

| Rule | Match on | Action |
|---|---|---|
| Same company, same domain | Domain | Merge, keep the earliest arrival |
| Same phone, different company name | Normalised phone | Merge, flag the name discrepancy |
| Same person, different email | Name + company | Merge, keep the work email |
| Subsidiary of an existing customer | Parent company | Route to customer success, not sales |
| Same company, different enquiry | Domain + 30 days | Merge, treat as one lead with two interests |

Normalise before matching: strip `www.`, lowercase the domain, strip spaces and country codes from
phones, remove legal suffixes from company names. `scripts/score_lead.py` does the normalisation for a
single record; a batch needs the same rules applied in the sheet.

## What enrichment is not

- **It is not a reason to guess.** An inferred employee count is marked inferred and scores at half
  weight, or scores zero. Choose one rule and apply it everywhere.
- **It is not scraping personal data at scale.** Business contact data from a public company page is
  one thing; a scraped personal email list is a compliance problem under DPDP and a deliverability
  problem everywhere.
- **It is not a substitute for the enquiry text.** A perfectly enriched record with a one-word
  enquiry is still unqualifiable.

## The batch workflow

1. **Import and normalise** - domains, phones, company names, cities.
2. **Deduplicate** with the rules above, and record what merged.
3. **Drop the unusable** - no company, no contact route, no enquiry text. Log them, do not score them.
4. **Enrich the remainder cheaply** - website and LinkedIn only, in one pass.
5. **Score with the same rubric**, unknown where unknown.
6. **Rank, band, and cut** to what the business can actually call this week.
7. **Return the top N with the handover packet**, and the rest as a nurture list with dates.

Step 6 is where a 200-name list becomes useful. A batch returned with all 200 scored and no cut has
not made a decision.

## Anti-patterns

- **Scoring first and deduplicating later.** The same company gets three scores and one conversation.
- **Enriching every record to the same depth.** The effort is better spent on the top twenty.
- **Treating a missing field as a zero without saying so.** Unknown and bad are different findings.
- **Buying a list and calling it inbound.** Purchased lists are a different role and a different
  legal question; this one qualifies enquiries that arrived.
- **Letting the CRM fields drift from the form fields.** The mapping is part of the job, not the
  admin.
