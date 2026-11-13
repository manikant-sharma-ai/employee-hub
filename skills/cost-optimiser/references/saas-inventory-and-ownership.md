# SaaS inventory and ownership

The inventory is the whole job. Everything else - the cuts, the savings, the renewals - is a query
against it. Build it from the money, and build it once properly.

## Where the lines actually hide

| Source | What it catches | What it misses |
|---|---|---|
| Card statements, 3 months | Trials that converted, personal-card tools, annual debits | Anything paid by invoice |
| Bank debits (NACH, standing instruction) | Annual contracts, minimum commitments | Card-only spend |
| Accounting vendor ledger | Invoiced vendors, GST-registered ones | Small card subscriptions |
| The team's memory | The tools people like | Exactly the ones worth finding |
| The email inbox, searched for "invoice" and "renewal" | Notice periods, price increases | Tools billed to a departed employee's inbox |
| The browser's saved passwords, if shared | Shadow IT, free tiers about to expire | Mobile-only tools |

Run the card statements first and the memory last. A review built from memory finds the ten tools
everyone knows about and misses the two that matter.

## The inventory columns

| Column | Why it earns its place |
|---|---|
| Vendor (normalised) | "Google Workspace", "Google Ireland Ltd" and "GOOGLE *GSUITE" are one line |
| Product / plan | The tier decides the price and the downgrade option |
| Seats or units | The quantity the price is multiplied by |
| Unit price and currency | In USD for anything foreign; convert with a stated rate and date |
| Billing period | Monthly or annual, and the debit month for annual |
| Annualised cost | The number that makes comparisons honest |
| Renewal date | The date the decision must be made *before* |
| Notice period | The date it must be cancelled by - usually earlier than the renewal |
| Payment method | Card ending 4421, or invoice, or a personal card |
| Owner | A person's name, not a team |
| Usage signal | Last login, active users, API calls, or "unverified" |
| Criticality | Stops the business / stops a team / nice to have |

Two columns decide whether the review is credible: **owner** and **usage signal**. A tool with no
owner is the one that survives three reviews and gets cancelled by accident in the fourth.

## Normalising vendors

The same vendor appears three ways and the duplicate detector then misses it. Rules:

- Strip the payment-processor prefix: `GOOGLE *`, `SP *`, `PAYPAL *`, `RAZORPAY*`.
- Strip legal suffixes: Ltd, Pvt Ltd, Inc, GmbH, Ireland, Technologies.
- Keep the product if the vendor sells several with different billing. Google Workspace and Google
  Ads are one vendor and two completely different conversations.
- Record the foreign-currency line in its own currency and convert once, at a stated rate.

## The overlap map

Group by job-to-be-done, never by vendor category. Vendors describe themselves in the same words;
jobs are what actually collide.

| Job | Common overlaps | The question that resolves it |
|---|---|---|
| Notes and documents | Notion, Confluence, Coda, Google Docs, Slite | Where does the team actually write? |
| Meeting capture | Otter, Fireflies, Zoom AI, Teams | One recorder, one retention policy |
| Analytics | GA4, Mixpanel, Amplitude, Metabase, Looker | Product analytics and BI are different jobs |
| Design | Canva, Figma, Adobe Express | Speed versus system - both can be justified |
| Support | Freshdesk, Zendesk, Intercom, a shared inbox | Volume decides; two desks never |
| Email marketing | Mailchimp, SendGrid, Zoho Campaigns, Brevo | Newsletter, transactional, CRM - pick per job |
| Project management | Asana, Trello, ClickUp, Jira, Notion | Two tools is one too many, always |
| Storage | Drive, OneDrive, Dropbox | Files follow the document suite, not preference |
| Passwords and security | 1Password, LastPass, Bitwarden | Never zero, never three |
| Scheduling | Calendly, Cal.com, Zoom scheduler | Free tiers usually enough |

The keep rule: the one with the data, the integrations and the highest real usage. Not the newest,
not the cheapest, not the one the loudest person prefers.

## Ownership, the part everyone skips

Assign every line to a person by name. Then the three questions:

1. **Does the owner still work here?** Subscriptions billed to a departed employee's card are the
   most common leak in a 20-50 person business.
2. **Does the owner know the price?** Most do not. Telling them is half the saving.
3. **Does the owner know the renewal date?** If not, the calendar has not been built yet.

## Anti-patterns

- **Reviewing from an expense-tool export alone.** It misses invoiced contracts, which are the
  expensive ones.
- **Leaving vendor names unnormalised.** The duplicate detector then reports four vendors and the
  founder sees four legitimate tools.
- **Listing tools without owners.** The list becomes a document that changes nothing.
- **Assuming "we use it" means it is used.** The admin console has last-login dates; ask for them.
- **Converting foreign currency at a round number.** State the rate and the date, or the annualised
  total is wrong by enough to matter.
