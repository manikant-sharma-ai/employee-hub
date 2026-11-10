# Technical discovery

Technical discovery exists to answer one question early: will this work here, and if not,
what would it take? Everything else in the sale is cheaper to fix than that.

## The ten questions

Ask them in this order, on the call, and write the answers down.

1. **What happens today?** The current process, the tool, the spreadsheet, the person who
   does it manually. The incumbent is the real competitor.
2. **What breaks if it stays like this?** The cost of the status quo in money, hours or
   risk. Without this there is no urgency and no deal.
3. **What are the systems this must talk to?** Names, versions, whether an API exists,
   who owns it. "We use SAP" is not an answer; "S/4HANA, on-premise, no external API
   exposed" is.
4. **What is the data, in volume and shape?** Records, transactions a month, peak, file
   sizes, formats, and where it lives.
5. **Who has to approve this technically?** IT, security, a parent company, a regulator.
   An unnamed approver is a deal that stalls at signature.
6. **What must be true for you to say yes?** Their success criteria, in their words.
7. **What have you already tried?** A failed project teaches more than a requirement
   document.
8. **What is the timeline, and what is driving it?** A deadline with a reason is a deal;
   a deadline without one is a wish.
9. **What would make this a no?** Ask it directly. Buyers answer this question honestly
   more often than any other.
10. **Who else is being evaluated, and what do you like about them?** Not to attack it -
    to know which technical claim we must beat.

## The stack map

One table, drawn on the call and sent in the follow-up:

| Layer | Their system | How we connect | Owner | Status |
|---|---|---|---|---|
| Identity | Azure AD | SAML SSO | IT | documented |
| ERP | SAP S/4HANA on-prem | flat-file export, nightly | IT | needs their export |
| Data warehouse | BigQuery | native connector | data team | tested |
| Messaging | WhatsApp Business | API, template approval | ops | not started |

Status values: documented, tested, needs work, not possible. A map where every row says
"documented" and none says "tested" is a map of assumptions.

## The disqualifier hunt

Every deal has one thing that would kill it. Find it on purpose:

- **Data residency** - the buyer needs data inside India, or inside their own VPC.
- **Protocol** - they need an on-prem connector we do not ship, or a batch mode we do not
  support.
- **Volume** - their peak is ten times the largest deployment we have run.
- **Approval workflow** - they need a four-level approval with delegation, and we have
  two.
- **Compliance** - a certification we do not hold and cannot get in their timeline.
- **Procurement** - a vendor registration, an empanelment or a security audit that takes
  six months.

Write the disqualifier in the discovery note even when it is resolved. A deal that has
been explicitly cleared on its hardest point is a deal that survives procurement.

## Fit call

Three outcomes, and only three:

- **Fit** - proceed to demo, with the integration risk named.
- **Conditional** - proceed only if a specific thing is confirmed by a date, with a named
  owner on both sides.
- **No fit** - say it, in one paragraph, with the reason and what would change it. Then
  hand the account back with a referral if there is a better tool for them.

## Anti-patterns

- **Discovery by demo.** Showing the product to learn the requirements means learning them
  in front of the buyer, at the cost of the buyer's confidence.
- **The requirements document as the only source.** It describes the ideal; the call
  describes the reality.
- **Talking to the champion only.** The champion cannot approve the architecture.
- **Recording "we can do that"** without the row in the stack map that proves it.
- **Skipping the "what would make this a no" question** because it is uncomfortable.
