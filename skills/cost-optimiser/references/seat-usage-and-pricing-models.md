# Seats, usage and pricing models

Most overspend is not a bad vendor. It is a good vendor priced on the wrong model for how the
business actually uses it.

## The four pricing shapes

| Shape | How it charges | Where it overcharges | The fix |
|---|---|---|---|
| Per seat | Per named user per month | Departed users, shared logins, viewers who could be free | Deprovision on exit day; use viewer roles |
| Per active user | Per user who logged in | Seasonal staff counted all year | Check the definition of active |
| Usage-based | Per call, per GB, per minute | Spikes, retries, a runaway integration | Caps, alerts, batching, caching |
| Tiered | Feature bundles | Paying for the top tier to get one feature | Move down a tier and replace the one feature |

## The seat audit

The five questions, in order, per tool:

1. **How many seats are paid for?** From the billing page, not the team's estimate.
2. **How many users logged in in the last 30 days?** From the admin console.
3. **How many in the last 90?** The gap between 30 and 90 is the seasonal or occasional user.
4. **How many never logged in at all?** These are the immediate cuts - often 10-20% of seats.
5. **How many are duplicates of a person with two accounts?** Common after a domain change or an SSO
   migration, and invisible without a user list.

Then the roles: an editor seat for someone who only reads is a downgrade, and a viewer seat is
usually free or a fifth of the price.

## When annual billing is right

| Condition | Annual | Monthly |
|---|---|---|
| Tool is core, used daily, no migration planned | Yes - take the discount | No |
| Usage is seasonal or uncertain | No | Yes - the premium is the option value |
| The tool is under review this quarter | No | Yes |
| The discount is under 10% | No | The cash flexibility is worth more |
| The vendor offers a refund on unused months | Either | Either |
| Cancelling means losing data | Yes, but export first | Either |

The trap in annual billing is not the commitment, it is the **auto-renewal on a card nobody watches**.
An annual plan that renews in March is a decision made in March whether or not anyone makes it.

## The usage-based traps

- **Retries.** A failing integration that retries five times bills five times. The cost is a symptom.
- **Chatty APIs.** A loop that calls per record instead of per batch multiplies the bill by the batch
  size.
- **No cache.** The same query answered from the vendor's API on every page load.
- **No cap.** A single runaway job can cost more than a year of the subscription.
- **Per-minute tools.** Meeting recorders and transcription services bill per minute of meeting, and
  the all-hands is a line item.

Every usage-based tool should have a spend alert set at 80% of the expected monthly figure. That is
the cheapest control in the whole review.

## Right-sizing a plan

| Symptom | Likely answer | Check first |
|---|---|---|
| Paying for a top tier for one feature | Move down, replace the feature | How often is that feature used? |
| Paying per seat for occasional users | Add a viewer or free tier | Does the vendor's free tier allow it? |
| Two products for one job | Consolidate to the one with the data | Migration cost and export path |
| Enterprise plan on a 12-person team | Business tier | Are the enterprise features actually used? |
| Storage or bandwidth add-on | Lifecycle and retention policy | Is the growth real or is it logs? |

## The exit cost nobody prices

Before recommending any switch, ask three questions and write the answers into the cut list:

1. **Can the data be exported, in what format, and at what cost?**
2. **What breaks on the day of the switch** - integrations, automations, shared links, SSO?
3. **Who does the migration, and how many hours?** Multiply by a real rate.

A tool at ₹8,000 a month that costs 30 hours to leave is a ₹8,000 a month tool for another year
unless the founder decides the migration is worth it.

## Anti-patterns

- **Auditing seats from a team list.** The admin console is the only count that matches the bill.
- **Downgrading to a tier that removes SSO or audit logs** to save a small amount. Security is not a
  cost centre.
- **Cancelling the cheapest tool and keeping the expensive duplicate**, because the cheap one is the
  one the reviewer happened to open.
- **Switching tools in the same month as a launch.** The migration will be abandoned half-done and
  the business will pay for both.
- **Reporting a saving that is a discount on a price nobody paid.** Compare contract to contract.
