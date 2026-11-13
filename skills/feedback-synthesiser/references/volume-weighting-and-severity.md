# Volume, severity and trend

Frequency tells you what is common. Severity tells you what is expensive. A ranking that uses only one
of them is either a popularity contest or a panic.

## The two axes

| | Low severity | High severity |
|---|---|---|
| **High volume** | Annoyance - fix in a batch, communicate meanwhile | The emergency - fix now, staff for it |
| **Low volume** | Ignore, or note it | The silent killer - investigate, it is losing customers quietly |

The fourth cell is where the money is. A rare theme that makes a customer leave is worth more than a
common theme about a label, and volume-only rankings never surface it.

## The ranking rule

Write the rule down and apply it identically to every theme. Three defensible rules:

| Rule | Formula | Use when |
|---|---|---|
| Volume-first | rank by record share | The decision is about support staffing |
| Cost-weighted | share x average cost per occurrence | The decision is about money |
| Severity gate | anything that causes churn, refund or a public review ranks top; the rest by volume | The decision is about roadmap order |

State which one you used. A founder who disagrees with the ranking is usually disagreeing with the
rule, and that is a productive conversation; a founder who disagrees with an unstated rule is just
confused.

## Estimating cost per occurrence

| Theme type | What to count | Where the number comes from |
|---|---|---|
| A failed transaction | Lost order value x refund rate | Order data |
| A support contact | Minutes x loaded hourly cost | Desk volume and payroll |
| A churn reason | Average revenue per account x months lost | CRM and billing |
| A public bad review | Estimated lost acquisition, conservatively | Traffic and conversion, marked as an estimate |
| A rework or return | Reverse freight + forward freight written off + markdown | Ops records |

Where the cost cannot be estimated, say "cost not quantified" rather than inventing a number. An
unquantified severity judgement is honest; an invented one is a liability in the readout.

## Trend, done properly

| Comparison | Claim you may make |
|---|---|
| One period only | "Snapshot of <period>" - no direction |
| Two comparable periods | "Up from 12% to 19% of tickets" |
| Three or more | "Rising for three months" - the only real trend |
| Volume change without share change | "Volume grew with the business; the rate did not" |
| Share change with flat volume | "The mix changed" - often a new segment, not a new problem |

Two rules that prevent most bad trend claims: normalise by total volume (share, not count), and check
whether the business itself changed size or mix in the period.

## Severity, in customer terms

| Level | Definition | Example |
|---|---|---|
| S1 | Loses the customer or the money | Payment fails, data lost, order never arrives |
| S2 | Blocks the core job | Cannot complete the main workflow |
| S3 | Costs time every use | Slow, three clicks where one would do |
| S4 | Cosmetic or preference | Wording, colour, a missing nice-to-have |

Severity is assigned by impact on the customer's job, never by how loudly it was reported. A polite
ticket about a failed payment outranks an angry one about a font.

## The "what should we fix first" answer

Four sentences:

1. The theme with the highest cost, with its count and its share.
2. The theme with the highest volume, with what it costs in support time.
3. The rare theme that is losing customers, with the number of records that support it.
4. What the business should communicate this week while none of it is fixed.

Then the caveat: which sources were not read, and what would change the order.

## Anti-patterns

- **Ranking by count and calling it priority.** The 40-record theme about a slow report outranks the
  3-record theme about failed payments, and the business loses three customers.
- **Treating one angry customer as severity.** Severity is impact, not volume of complaint.
- **A cost estimate with no method.** Say where the number came from or say it is unquantified.
- **Comparing raw counts across a period of growth.** Share, not count.
- **Ignoring the theme that is falling.** It tells you what a previous fix achieved, which is the
  cheapest evidence of progress the business has.
