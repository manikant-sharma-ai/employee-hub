# Learnings - churn-analyst

1. **A churn percentage without its base is a rumour.** The base table is computed first, every month, before any
   rate is quoted.
2. **"Other" is the taxonomy failing, not the customer refusing to explain.** When it crosses 10% the codes get
   rebuilt that month, from the free text.
3. **The form records the last conversation; the tickets record the cause.** Ninety days of support history
   outrank the cancellation picklist, every time.
4. **Logo and revenue churn are two different businesses.** A fall in one with a rise in the other is the most
   common way a read is wrong.
5. **Net revenue churn hides a dying segment behind expansion from ten accounts.** Gross, net and expansion are
   reported as three lines, never one.
6. **A signal without a lead time and a false-positive rate is a story.** Two signals that pass the test beat
   eight that do not.
7. **A save without a control group is the market, not the play.** Customers who were staying anyway are not
   evidence.
8. **Downstream survival at six months decides whether a save was a save or a delay.** A play that buys sixty
   days is renting time at margin.
9. **Churn falls for five reasons that are not improvements** - a definition change, a mix change, an ageing base,
   an unmeasured save play, or deferred collection. All five are checked before a fall is called a win.
10. **Account IDs, never names.** Churn data is personal data under the DPDP Act and the repo is public.
