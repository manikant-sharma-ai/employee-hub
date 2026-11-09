# Seasonality and lead time

Seasonal businesses fail in the buying, not the selling. The order date is the only date
that matters, and it is computed backwards from the shelf.

## The Indian season calendar

| Window | Peak | Buy by | Watch |
|---|---|---|---|
| Diwali and festive | Sep-Oct (dates move) | 60-90 days before, earlier for imports | Gifting, packaging, electronics, home |
| Rakhi and sibling gifting | Aug | 45-60 days | Fast-moving, low unit value |
| Wedding season | Nov-Feb, plus Apr-May | 45 days per cluster | Apparel, jewellery, gifting, banqueting |
| Back to school | May-Jun | 60-90 days | Stationery, uniforms, bags |
| Monsoon | Jun-Sep | 30-45 days | Footwear, outdoor, agri inputs, logistics delays |
| Summer | Mar-Jun | 45 days | Cooling, beverages, apparel |
| Year-end corporate | Jan-Mar | 30-60 days | B2B gifting, software budgets |
| Harvest and mandi cycles | Region-specific | Follow the crop calendar | Agri inputs, rural demand |

Festive dates move every year. Use the actual date, not "October", and work backwards
from it.

## The build date

```
Order date = Selling window start
             - lead time (P90, not average)
             - inward QC and put-away
             - buffer for one slipped shipment
```

Worked example - Diwali selling starts 20 September, import lead time 45 days at P90
with a 12-day spread:

| Step | Date |
|---|---|
| Selling window opens | 20 Sep |
| Less P90 lead time | 45 days → 6 Aug |
| Less inward QC and put-away | 7 days → 30 Jul |
| Less buffer for one slip | 12 days → 18 Jul |
| **Order must be placed by** | **18 July** |

Miss that date and the choice is air freight (which eats the margin), a part quantity
(which loses the season's best SKU), or nothing (which is honest and cheaper than
discounting in November).

## Sizing the seasonal buy

| Input | Use |
|---|---|
| Last season's units, by week | The baseline |
| Growth or decline in the category | Adjust, with a number |
| Distribution change (new channel, new city) | Add, with a number |
| Price or pack change | Adjust for elasticity, cautiously |
| Stock left from last season | Subtract - this is the number everyone forgets |
| Supplier reliability | Apply the P90 lead time, not the promise |

Then split the buy: 60-70% committed, 30-40% reorderable. A single committed buy for a
season with a reorder option is the cheapest insurance a seasonal business can buy.

## The end-of-season rule

Decide the exit date before the season starts: "any festive stock unsold by 31 December
goes to the ladder". Deciding it afterwards produces the discount spiral that trains
customers to wait.

## Lead time, by source

| Source | Typical | Variability | Plan with |
|---|---|---|---|
| Local manufacturer | 7-21 days | Low-medium | Observed P90 |
| Domestic distributor | 3-10 days | Low | Promise + 2 days |
| Import by sea (China) | 30-45 days port to port | High | P90 + customs buffer |
| Import by air | 7-12 days | Medium | P90, and only for the hero SKU |
| Own production | Capacity-dependent | High in peak | Capacity plan, not a lead time |

Customs, port congestion and festival freight surcharges are the three things that turn a
45-day import into a 70-day one. The buffer is not pessimism; it is the cost of the
season.

## What goes wrong, and the early signal

| Failure | Early signal | Fix |
|---|---|---|
| Order placed late | The order date has passed and the PO is unsigned | Decide today: air, part quantity, or skip |
| Supplier slips | No dispatch confirmation at lead time minus 7 | Escalate, then switch the reorderable share |
| Demand higher than plan | Sell-through above plan in week 1 | Pull the reorderable share forward |
| Demand lower than plan | Sell-through below 70% of plan by mid-window | Stop reorders, plan the exit date |
| Stock arrives after the window | The shipment date is past the selling start | Price it for the next window, not this one |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Buying to the average lead time | Half the seasons start short |
| Using "October" instead of the festive date | The order is two weeks late every year |
| Forgetting last season's leftover stock | Double the stock, half the price |
| 100% committed buy | No ability to respond to a hit or a miss |
| No exit date | The discount spiral, and a trained customer |
| Air freight to fix a late order | Margin gone, and the same mistake next year |
