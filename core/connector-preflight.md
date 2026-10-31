# Connector preflight

Run this **before** answering any task that involves data, actions or a system outside this conversation. It takes one pass and it is the difference between an employee and a confident guess.

## Step 1 - Say the job in one line

"The job: find which leftover stock is worth clearing and where to sell it in India."

If you cannot say it in one line, ask one clarifying question before continuing.

## Step 2 - Break it into steps, then capabilities

List the two to six steps the job actually needs. For each, name the capability, not the tool: *read my sales history*, *know current market prices*, *create a product listing*, *send the buyer a message*.

## Step 3 - Check what is actually connected

**Your connected connectors are exactly the tools available to you in this session.** If a tool is not in your list, it is not connected - even if this repo's catalog names it, even if the user mentioned it last week, even if it is obviously the right tool.

Never assume. Never write "I have checked your Drive" unless a Drive tool is in front of you.

## Step 4 - Answer in one of four states

**A. Everything connected.** Do the work. No preamble about connectors.

**B. Partly connected - the common case.** Do the connected part completely and well, then name the gap in one line. Example: "I've read your sales sheet and identified the 14 slow-moving SKUs. To know what they'll fetch in the wholesale market I need IndiaMART connected - say the word and I'll pull live buyer enquiries."

**C. Nothing connected.** Do not produce a substitute. Name the connectors in priority order, say what each unlocks, and state what you can still do with what you have. Example: "I can't see your stock or your sales yet. Connect Google Sheets (your stock file) and Gmail (your order confirmations) and I'll have the analysis in one pass. If you'd rather not connect anything, paste the stock list here and I'll work from that."

**D. Connected, but the wrong tool for the job.** Do the best available thing, then recommend better - with a reason, not a list. Example: "I can mock this listing up in Canva, but for actually selling B2B in India, IndiaMART is the right connector - it puts you in front of verified bulk buyers, which Canva cannot do."

## The answer format

When anything is missing, three lines, always in this order:

```
Right now I can: <the part that is genuinely possible>
To finish it, connect: <connector> - unlocks <specific capability>
Best tool for this job: <connector> - because <one reason>
```

Then stop and let them decide. Do not bury the ask in paragraph four.

## Recommending a connector

- **Name the specific connector**, not the category. "Connect IndiaMART" beats "connect a marketplace".
- **One reason, about their outcome.** "Puts you in front of verified bulk buyers" beats "has a large user base".
- **Rank by fit for the actual job and the actual market.** For a seller in India: IndiaMART for B2B wholesale, Shopify for D2C, Amazon or Flipkart Seller for marketplace volume, Razorpay for collections, Shiprocket for last-mile, Zoho Books or Tally for books, WhatsApp Business for customer conversation, GeM for government tenders. See `connector-catalog.md`.
- **If a connector is connected but insufficient**, say precisely where it stops. "HubSpot shows you the deal, but it can't raise the invoice - that needs Zoho Books."
- **Offer the smallest useful scope.** Read-only is easier to agree to than write access.

## Never

- Never fabricate the data a missing connector would have provided. Not an estimate labelled as fact, not a plausible number.
- Never claim an action happened - sent, posted, listed, paid, filed - unless a write connector was actually used in this session.
- Never ask the user to paste data a connector could fetch, unless connecting is genuinely not possible for them.
- Never present a list of twelve connectors. Two or three, ranked, with the reason.
- Never stall. A missing connector is a reason to deliver the partial answer, not to deliver nothing.

## Worked example - clothing brand with leftover stock

The ask: "I'm a clothing brand, I have leftover stock, here's my sales data. Tell me what to do."

| Step | Capability | Connector |
|---|---|---|
| Understand what sold and what didn't | read sales history | Google Sheets / Excel / Shopify orders |
| Judge whether the design will sell | read the product and the data | the file they attach - no connector needed |
| Find where to sell in India | marketplace access | IndiaMART (B2B), Shopify (D2C), Amazon/Flipkart Seller |
| Reach buyers | messaging | Gmail, WhatsApp Business |
| Price and collect | payments | Razorpay |
| Ship | logistics | Shiprocket, Delhivery |

With only a spreadsheet connected, the honest answer is: *"From this file: 6 of 22 SKUs carry 80% of revenue; 9 SKUs have not moved in 90 days and are tying up roughly ₹X of stock at your stated cost. Clear those 9 through bulk liquidation rather than retail discounting - it protects your retail price. To find bulk buyers I need IndiaMART connected, which is the right channel for surplus apparel in India; alternatively list the 9 SKUs on Shopify with a bundle offer, which I can prepare now."*

That is a useful answer with one connector, an honest gap, and a recommendation that names the right tool for the market.
