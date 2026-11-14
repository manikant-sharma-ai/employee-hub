# Vendor negotiation and renewal

This file is about the twenty minutes that decides a year of spend. It is not a script; it is the preparation
that makes the conversation short.

## The leverage table

| Lever | Strength | How to create it |
|---|---|---|
| A competing quote | Strongest | Ask two alternatives for a written quote, for the same scope |
| A renewal date | Strong | Start 60-90 days out; the vendor's quarter end is often better |
| A term commitment | Medium | Offer 24 months for a real discount on a load-bearing tool |
| Seat consolidation | Medium | Fewer products from one vendor, honestly counted |
| Annual prepay | Medium | Only if the cash allows - check with `treasury-ops` |
| A public reference | Medium | A case study or a logo is worth more to them than a discount is to you |
| Silence | Weak | Works once |
| Threatening to leave | Weak, and it burns the account manager | Never unless it is true |

## What to ask for, in order

1. **The price held flat** for another term. In a market where list prices rise 5-10% a year, flat is a real
   saving and the easiest yes.
2. **A seat true-up** to the actual active count, at the same rate.
3. **A tier correction** if the plan was upgraded for a feature nobody uses.
4. **A discount** for term or prepay, in exchange for something you were going to give anyway.
5. **Terms**: a shorter notice period, a price cap on renewal, a data export clause, a termination-for-
   convenience after year one.
6. **Payment terms**: net 30 or net 45 instead of card-upfront, which is worth more than a 2% discount at most
   Indian working-capital costs.

The first ask is almost always the best value. A founder who opens with a 40% discount demand gets a polite
no and a worse relationship; the one who opens with "hold the price and true up the seats" gets both.

## The clauses that cost money later

| Clause | The trap | Ask for |
|---|---|---|
| Auto-renewal | Silence renews for 12 months | Written notice by email, 30 days |
| Price escalation | "Up to 7% annually" | A cap, or a fixed price for the term |
| Minimum commitment | Pay for what you do not use | A true-up, or a lower floor |
| Overage | A usage cap with punitive rates | A soft cap with a notification |
| Data export | Available "on request", slowly | Self-serve export, 30 days after termination |
| Suspension for late payment | Service off in 7 days | 30 days, with notice |
| Unilateral change | Terms updated at will | Notice period and a right to exit |
| Audit clause | A true-up bill after a review | A cap, and notice before the audit |

Any clause in the last column that the business cannot live with goes to `legal-drafter` for the wording. This
role flags it; it does not draft it.

## Benchmarks, without pretending to precision

| Category | The shape of a fair Indian price | The tell that you are overpaying |
|---|---|---|
| CRM per seat | ₹800-2,500 a month for SMB tiers | Paying enterprise tier at under 20 seats |
| Helpdesk per agent | ₹1,200-3,500 a month | Paying per "contact" on low volume |
| Design tool per seat | ₹400-1,500 a month | Full-suite seats for people who export a PNG a week |
| Project tracking per seat | ₹350-900 a month | Paying per seat for read-only users who could be free |
| Cloud, small SaaS | 4-9% of revenue at early stage | Above 15% with no GPU or media workload |
| Analytics / BI per seat | ₹700-2,500 a month | Two BI tools |

Treat these as shapes, not facts. Quote the vendor's own list page with the date if a number is going into a
document, and never present a benchmark as a market survey.

## The conversation, in five lines

1. "Our renewal is on <date>. Here is the seat count we actually use, from our login data."
2. "Here is the price we have been offered elsewhere for the same scope." (Only if true.)
3. "We would like to continue. To do that, we need <the specific ask>."
4. "If that works, we can commit to <term or prepay or reference>."
5. "Can you confirm in writing by <date>?" - always in writing, always dated.

## When to walk

Walk when the switch cost is genuinely lower than the renewal, and only then. The arithmetic: annual renewal
minus the alternative's annual cost, minus migration hours at a real hourly rate, minus the risk of a worse
tool. A 15% saving that needs three weeks of engineering is usually a loss; a 40% saving on a tool used by two
people is usually a win.

## Anti-patterns

- **Negotiating after the auto-renew.** The contract has renewed; the conversation is now about next year.
- **Asking for a discount with no alternative.** The vendor knows you have nowhere to go and prices accordingly.
- **Taking the multi-year deal on a tool that is not load-bearing.** The discount is real; the lock-in is
  longer.
- **Letting the person who loves the tool negotiate.** They will trade price for features.
- **No written confirmation.** A verbal "we'll take care of it" is not a term.
