# Readout and decision handoff

The synthesis is finished when a decision is assigned, not when the themes are counted.

## The one-page readout

| Section | Content | Length |
|---|---|---|
| Coverage | Records read of records available, period, sources, gaps | 2 lines |
| The answer | Top three themes with shares, the one to fix first | 5 lines |
| Theme table | Theme, records, share, severity, trend, cost, owner | 8-12 rows |
| Quotes | Two or three per top theme, verbatim | 6-9 lines |
| What this asks of whom | One action per theme, one owner, one date | 3-5 lines |
| What I could not verify | Sources, samples, segments | 3 lines |

Everything else is an appendix. A readout that needs a meeting to explain itself has failed.

## The decision handoff table

| Theme | Evidence | Decision implied | Owner | By when | What would change the call |
|---|---|---|---|---|---|
| Onboarding takes over a day | 34 records, 24% of tickets, S2 | Fix the import step | product-manager | next cycle | If the 34 are all one segment |
| Invoice mismatch | 19 records, 13%, S1, 4 churns | Fix before the next billing run | finance-ops | this week | If the mismatches are all one customer |
| Delivery a day late | 61 records, 22% of reviews, S3 | Change the courier SLA | ops | this month | If the delay is seasonal |

The "what would change the call" column is what makes the readout honest. It tells the decision-maker
exactly how much confidence the evidence supports.

## Who receives what

| Recipient | What they need | What they do not need |
|---|---|---|
| Founder | The five-line answer and the three decisions | The coding sheet |
| Product | The themes with counts, quotes and severity | The finance estimate |
| Support | The themes that are tickets, with the wording customers use | The roadmap discussion |
| Marketing | The themes that are expectations, and the exact customer language | Ticket volumes |
| Sales | The objections and the competitor mentions | Internal cost estimates |
| Board | Three themes, the trend, and what was done about the last three | Raw quotes with any risk |

## Writing the theme sentence

Format: **<what happens> - <how often> - <what it costs> - <what to do>**.

> "Onboarding takes more than a day for a third of new accounts - 34 records, 24% of tickets, two
> churned accounts - because the product import fails on duplicate SKUs. Fix the import before the
> next cohort."

One sentence, four facts, one action. If it needs a second sentence to be actionable, the theme is
still a category.

## Closing the loop

- **Record the decision** in `notes/decisions.md` and in the next readout's opening line.
- **Re-check the theme next period.** A theme that was fixed and fell from 24% to 6% is the most
  useful slide in the next readout.
- **Report repeat themes loudly.** The same theme with no decision recorded for two periods is a
  management finding, not a product one.
- **Never re-run the same synthesis to feel productive.** If nothing changed, the answer is the
  previous answer plus "no decision was taken".

## Anti-patterns

- **A readout with no owner column.** It is a report, not a handoff.
- **Themes without the decision they imply.** The reader has to do the thinking the synthesis was
  meant to do.
- **Twelve themes ranked by count** with no severity. The founder fixes the loudest and the expensive
  one stays.
- **A readout that recommends a roadmap.** Say what the evidence supports; the roadmap is somebody
  else's accountability.
- **Presenting the same data twice** as a new finding because the period label changed.
