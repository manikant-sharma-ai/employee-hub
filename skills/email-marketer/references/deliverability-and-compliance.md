# Deliverability and compliance

Deliverability is plumbing, not copy. When it is wrong, nothing else you write
matters, because nobody sees it.

## The setup that must exist before the first send

| Item | What it is | Why |
|---|---|---|
| SPF | A DNS record listing who may send for the domain | Without it, receivers cannot verify you |
| DKIM | A signature on each mail | Proves the mail was not altered |
| DMARC | A policy record, starting at `p=none` | Tells receivers what to do with failures, and gives you reports |
| A sending subdomain | e.g. `mail.yourbrand.com` | Protects the main domain's reputation from campaign mistakes |
| A real reply address | A monitored mailbox | Replies are a positive signal; `noreply@` wastes them |
| A verified list source | Consent records | Bounces and complaints are the two metrics that kill a domain |

## The numbers that matter

- **Bounce rate**: keep hard bounces near zero, remove them immediately. Above 2% is a problem.
- **Complaint rate**: above 0.1% is dangerous territory. One in a thousand is already high.
- **Unsubscribe rate**: a spike means frequency or relevance is wrong, not that people stopped caring.
- **Placement**: check the spam and promotions folders for a sample send, not just the inbox count.

## Volume discipline

- **Warm up a new domain**: 200-500 mails a day for the first week, doubling while complaint and bounce rates stay low.
- **Sudden spikes are the classic trigger** - a 50,000-mail blast from a domain that sends 500 a week looks like a spam run.
- **Consistency beats volume**: a steady weekly send is trusted more than an irregular large one.

## Content signals

- **Text-to-image ratio**: a mail that is one big image reads as an advertisement. Keep real text.
- **One clear unsubscribe** in the footer, plus the sender's postal address in most jurisdictions.
- **No link shorteners with bad reputation**, no misleading display names, no attachments on a first send.
- **Plain-text alternative** for every campaign - some filters treat its absence as a signal, and some readers prefer it.

## Indian specifics

- **DPDP Act 2023**: consent must be free, specific, informed and revocable; the person can ask what you hold and ask for erasure. Keep a record of consent, purpose and withdrawal.
- **IT Rules and TRAI rules** apply to commercial communication over SMS and calls; email is governed more by consent and the DPDP framework, but a business that also sends SMS or WhatsApp should assume the stricter of the two.
- **WhatsApp templates** need Meta approval and prior opt-in; plan a week for approval.
- **GST details** on a commercial mail are not required, but the sender identity and a working contact are expected by both recipients and platforms.

## When you land in spam

Diagnose in this order: authentication records, bounce and complaint rates, list
quality, then content. Do not "resend with a different subject" - that is how a
temporary placement problem becomes a permanent reputation problem.

## Anti-patterns

- Sending a launch to the whole list from a cold domain.
- Buying a "warmed" sending service and assuming the domain is safe.
- Ignoring DMARC reports because `p=none` is set.
- Using one domain for transactional and marketing mail without a fallback.
- Deleting the consent record because the spreadsheet got messy.
