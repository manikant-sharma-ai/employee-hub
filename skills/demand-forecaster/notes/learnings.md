# Learnings - demand-forecaster

1. **A stockout month is censored demand, not low demand.** Left in the history, it becomes a downward seasonal
   index and a permanent under-order in the peak.
2. **The festival moves every year.** An index built on calendar months without aligning the festival week is
   wrong the moment Diwali shifts by a fortnight.
3. **The distributor stocks before the retail peak.** Two peaks, one cause; model both or be short in the second.
4. **Uplift is increment minus pull-forward minus cannibalisation.** A promotion that lifts 40% for a week and
   leaves a 25% hole after it has lifted very little.
5. **Margin, not revenue, decides whether a promotion worked.** A 30% discount that doubles units usually loses
   money.
6. **Accuracy is out-of-sample.** In-sample fit is a description of the past and it is always flattering.
7. **Bias matters more than error in a purchase plan.** Unbiased errors average out; a consistent under-forecast
   means a stockout on every SKU at once.
8. **The naive forecast is the benchmark.** If the method cannot beat "same period last year", it is not used.
9. **A forecast is not a target.** Adjusting the number upward to motivate anyone destroys the only thing the
   number is for.
10. **The interval is the deliverable, not the point estimate.** A planner can hold stock against a range; a single
    number invites a purchase order that is wrong half the time.
