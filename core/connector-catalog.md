# Connector catalog

Which kind of tool does which job - and which one to recommend for a business operating in India.

**This catalog does not mean anything here is connected to you.** It is a map for the preflight. Check your own tool list before claiming access.

## Selling and commerce

| Job | Connector | Note |
|---|---|---|
| B2B wholesale, surplus stock, bulk buyers in India | IndiaMART | Best first call for surplus or wholesale in India - verified bulk buyers, enquiry-driven |
| Direct-to-consumer storefront | Shopify | Best for own-brand D2C, catalogue, discounts, abandoned carts |
| Marketplace volume | Amazon Seller, Flipkart Seller | Higher reach, higher fees, stricter listing rules |
| Government and institutional tenders | GeM | Where public procurement actually happens in India |
| Quick catalogue-first listing | Wix, Zoho Commerce | Lighter than Shopify, fine for small catalogues |
| Payments and collections | Razorpay, Stripe, PayPal | Razorpay for UPI-heavy Indian retail |
| Shipping and last mile | Shiprocket, Delhivery | Shiprocket aggregates couriers; use for rate comparison |

## Money and books

| Job | Connector | Note |
|---|---|---|
| Invoicing, GST-ready books | Zoho Books, Tally | Tally where the accountant already runs it |
| Expenses and bills | Zoho Expense, Google Drive (bills folder) | Drive is enough to start |
| Banking and reconciliation | bank statement export, Zoho Books | Direct bank connectors are rare - plan for CSV |
| Payroll | Zoho Payroll, RazorpayX | |
| Spreadsheet analysis | Google Sheets, Excel | The most underrated connector in any business |

## Customers and communication

| Job | Connector | Note |
|---|---|---|
| Email | Gmail, Outlook | The default inbox connector |
| Team chat | Slack, Microsoft Teams | |
| Customer conversation in India | WhatsApp Business | Where Indian customers actually reply |
| CRM | HubSpot, Zoho CRM | Zoho is common in Indian SMBs |
| Support desk | Zendesk, Freshdesk | |
| Email marketing at scale | Mailchimp, SendGrid, Zoho Campaigns | Mailchimp for newsletters and journeys; SendGrid for transactional and high volume; Zoho Campaigns where the CRM is already Zoho |
| WhatsApp campaigns | WhatsApp Business API, Interakt, AiSensy | Template messages need prior opt-in and Meta approval - plan a week, not an hour |
| Calendar and scheduling | Google Calendar, Outlook Calendar | Also how an employee tracks its own performance |
| Files | Google Drive, OneDrive, Dropbox | |
| Docs | Google Docs, Word, Notion | |
| Meetings and transcripts | Google Meet, Zoom, Otter.ai | Transcripts are the cheapest source of truth about a business |

## Growth

| Job | Connector | Note |
|---|---|---|
| Social publishing | LinkedIn, Instagram/Meta, X, YouTube | |
| Paid acquisition | Meta Ads, Google Ads | Write access needs care - confirm before spending |
| Search visibility | Google Search Console, GA4 | |
| Analytics and warehouse | GA4, BigQuery, Supabase | |
| BI and dashboards | Looker Studio, Metabase, Sigma Computing | Looker Studio is free with GA4; Metabase when the data sits in Postgres or Supabase; Sigma when the numbers live in the warehouse and finance owns them |
| Design and brand assets | Canva, Figma | Canva for speed and for people who are not designers; Figma for a system, components and developer handoff |
| Production design suite | Adobe Photoshop, Illustrator, InDesign, Adobe Express | When the printer or the agency needs layered PSD, AI or INDD source files. Express is the cheap Canva equivalent inside the Adobe account |
| Video editing and finishing | Premiere Pro, After Effects, DaVinci Resolve | Resolve is free and enough for cuts, colour and audio; After Effects only for motion graphics, never for a plain cut |
| Vector and illustration source | Illustrator, Inkscape | Print-safe outlined vectors; Inkscape when the licence budget is zero |
| Image generation | an image model connector | For original visuals, not for copying an artist's style |

## Building and internal tools

| Job | Connector | Note |
|---|---|---|
| Database and backend | Supabase, Google BigQuery | |
| Repos and code | GitHub | |
| Project tracking | Jira, Google Tasks, Asana | |
| Automation and hosting | Cloudflare, Netlify, Replit | |
| Forms and intake | Tally, Google Forms | |
| Design-to-code handoff | Figma dev mode, Zeplin | Dev mode gives real spacing, tokens and assets; a screenshot does not |
| Browser and device testing | BrowserStack, Playwright | BrowserStack for real devices and Safari; Playwright for repeatable scripted checks in CI |
| Translation and localisation | Bhashini, Google Cloud Translation, DeepL | Bhashini is India's own language stack and the right first call for Indic languages; DeepL for European languages, not Indic ones |

## How to choose when several fit

1. **Fit for the job**, not popularity. A CRM cannot raise an invoice.
2. **Fit for the market.** IndiaMART over a generic marketplace for B2B surplus in India; Razorpay over Stripe for UPI-heavy retail; WhatsApp over SMS for customer conversation.
3. **What the person already owns.** Recommending a new subscription to someone whose accountant already runs Tally is a bad answer.
4. **Smallest scope that works.** Read-only first; write access once the output is trusted.
5. **The licence, not just the tool.** A printer that wants CMYK and bleed needs InDesign or Illustrator source, not a Canva export. A client who will edit the file next month needs an editable Figma or PSD, not a flat PNG.
