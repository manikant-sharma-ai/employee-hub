# Technical objections and competitive comparison

The technical buyer is not looking for a reason to buy. They are looking for a reason it will fail,
so they are not blamed for choosing it. Your job is to be the person who found the failure first.

## The six objections that decide most deals

| Objection | What it really means | The answer that works |
|---|---|---|
| "Can it integrate with our ERP?" | "Will I have to re-key data forever?" | The specific surface, the sync direction and frequency, and a tested example |
| "Is our data safe?" | "Will I be the one who lost it?" | The control, the certificate, the region, the deletion date - named |
| "Will it scale to our volume?" | "Will it be slow in month six?" | A tested number with the condition it holds under |
| "How long does implementation take?" | "Will this be my project for a year?" | A phased plan with the first value date, and who does what |
| "We already have a system" | "Will I have to defend a switch?" | What stays, what moves, what the migration costs, and the coexistence option |
| "What if it does not work?" | "What is my exit?" | The exit criteria, the data export, the notice period, the support terms |

## Answer patterns

**The capability answer, when it is yes:**
"Two-way sync of item master and stock, every 15 minutes. We tested 4,200 SKUs at 11 minutes median
in the sandbox. Your API's rate limit is the one thing that could change that - I will confirm it
this week."

**The capability answer, when it is no:**
"Not today. There is no native approval workflow. The workaround is a status field plus an email
alert, which your team would run; a proper workflow is on the roadmap as planned, not committed. If
approval routing is a must-have for go-live, that is a condition on this deal, not a detail."

**The "we do not know" answer:**
"I do not know, and I am not going to guess on something you will hold me to. I will confirm with
the product owner today and send it in writing before 6pm."

Three things never to say: "absolutely", "fully customizable" and "we can build anything". Each one
converts a technical objection into an implementation dispute.

## The competitive comparison that survives scrutiny

| Criterion | Weight | Us | Them | Where we lose |
|---|---|---|---|---|
| Native Tally sync | High | Yes, two-way | Via middleware | - |
| Offline billing | High | Yes | No | - |
| Multi-currency | Medium | Yes | Yes | - |
| Workflow approvals | High | No | Yes | **We lose here** |
| Implementation time | Medium | 2-3 weeks | 6-8 weeks | - |
| Price at 20 users | Low | ₹X | ₹0.7X | **We lose here** |

Rules:
- **Weights come from the buyer's own criteria**, not from a template.
- **Concede at least one row.** A table where you win everything is read as a sales document.
- **Never state a competitor's price or feature you have not seen** in their document or a public
  source. Attribute it: "according to their published pricing page, dated".
- **Name the losing row in the meeting before they find it.** The person who concedes first keeps
  credibility for everything else.

## Where you lose, and how to handle it

| Situation | Response |
|---|---|
| A must-have they have and you do not | Say it is a condition, and offer the workaround with its cost and date |
| Cheaper competitor | Compare on total cost of ownership, not licence: implementation, integration, support |
| A bigger vendor | Compare on implementation time and the named person who will do the work |
| An incumbent with switching cost | Propose coexistence first, and a phased move with a defined exit |
| A free or open-source option | Price the internal effort honestly; sometimes they are right |

If the honest answer is that the competitor is a better fit, say so and keep the relationship. That
answer wins the deal two years later more often than a stretch does.

## The security questionnaire, answered without risk

| Question type | How to answer |
|---|---|
| Certification | The certificate name, the date, the scope - attach it |
| Data residency | The specific region and the sub-processors, named |
| Encryption | At rest and in transit, with the standard |
| Access control | SSO, roles, MFA, audit log - and whether each is available on this plan |
| Breach notification | The commitment and the hours, per the DPA |
| Backup and recovery | Frequency, retention, tested restore date |
| Sub-processors | The list, with the purpose |
| Deletion | The method and the timeline, on request and on exit |
| Penetration test | The date of the last one, and the summary |
| Unknown | "Not applicable to this deployment" or "I will confirm in writing" - never a guess |

Two rules: answer every row (a blank row fails the review), and never overstate a control that is
only available on a higher plan.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| "Absolutely" | The deal that dies in implementation |
| A comparison where you win every row | Read as marketing, then discarded |
| Quoting a competitor's price from memory | Wrong, and the buyer checks |
| Answering a security question with a marketing phrase | The review fails, and it is your fault |
| Hiding a gap to win the evaluation | The gap is found in UAT, at the worst moment |
| No written follow-up on an answer given verbally | It is disputed later, and memory loses |
| Blaming the competitor's product | The buyer trusts the competitor more, not you |
