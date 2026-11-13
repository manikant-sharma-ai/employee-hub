# Cloud cost structure

A cloud bill is not one number, it is six, and the one that doubled is rarely the one being
discussed. This file is how to read an invoice without a finance background.

## The six lines that make up most bills

| Line | What drives it | The usual surprise |
|---|---|---|
| Compute | Instance hours, vCPU and memory, autoscaling | An environment nobody turned off |
| Storage | GB-month by tier, snapshots, backups, versions | Snapshots retained forever |
| Database | Instance class, IOPS, provisioned capacity, backups | Provisioned IOPS on a dev database |
| Network egress | GB leaving the region or the cloud | A backup or analytics export leaving the region monthly |
| Managed services | Queues, functions, logs, CDN, search | Log ingestion, which is cheap per GB and enormous per month |
| Support and commitments | Support tier, reserved or committed use | A support plan bought for a migration and never removed |

## Reading the invoice in the right order

1. **Compare three months, not one.** One month is a spike or a rounding of last month's change; three
   months shows the trend and the step change.
2. **Find the step change first.** Which service line moved, in which month, and what shipped or
   changed that month. Usually there is a deploy, a launch, a new environment, or a new customer.
3. **Then find the steady waste.** Idle instances, unattached volumes, old snapshots, unused elastic
   IPs, orphaned load balancers, dev environments that have not been rebuilt since the launch.
4. **Then the structural cost.** Instance family too large for the workload, storage tier too hot,
   cross-region traffic that could be co-located, logs at full retention.
5. **Only then the commitment.** Reserved instances or savings plans cut 30-60% of a *stable*
   baseline - and lock you in. Never commit before the waste is removed, or you commit to the waste.

## The idle-resource checklist

Every item here is a line on a bill that produces nothing.

| Resource | How to find it | What it costs |
|---|---|---|
| Stopped-but-attached instances | Console: stopped, still has EBS volumes and an IP | Storage plus IP charges |
| Unattached volumes | Volume list filtered by "available" | Full GB-month |
| Old snapshots | Snapshot list sorted by age | GB-month, quietly, forever |
| Unused elastic IPs | IP list filtered by "unassociated" | Per-hour charge |
| Orphaned load balancers | LB list with zero healthy targets | Per-hour plus LCU |
| Dev and staging environments | Tag `env=dev`, last deploy date | The whole stack, 24x7 |
| Log groups with no retention set | "Never expire" | Ingest plus storage |
| Old container images and build caches | Registry storage, CI minutes | Per-GB and per-minute |
| Unused managed databases | Connection count near zero | The instance class |

## The three legitimate levers

| Lever | Saving shape | Risk | When to use |
|---|---|---|---|
| Remove waste | 5-20% of bill, immediate, no risk | None if the resource is genuinely idle | Always first |
| Right-size | 15-40% of compute, needs a week of metrics | Under-provisioning at peak | After waste, with metrics |
| Commit | 30-60% of the stable baseline | Lock-in for 1-3 years | Last, on the post-waste baseline |

The order matters and it is the most common error in a cloud review: teams commit first because it
is the easiest conversation with the vendor, and then cannot remove the waste they committed to.

## Storage tiers

| Tier | Right for | Wrong for |
|---|---|---|
| Hot / standard | Data read weekly | Backups, logs, archives |
| Infrequent access | Read monthly | Anything a dashboard queries |
| Archive / cold | Compliance retention, old backups | Anything that may need a restore this week |
| Lifecycle rules | Everything older than N days | Nothing - this is the free win |

A lifecycle rule that moves objects older than 90 days to a colder tier costs nothing to add and is
usually the single largest storage saving available.

## Multi-cloud and the hidden second account

The most common cloud finding in a small business is not a misconfiguration - it is a second account.
An old account from a contractor, a personal account that became production, a subsidiary's billing
account. Ask explicitly: "how many cloud accounts does this business pay for?" before analysing any
of them.

## What not to do

- **Do not propose a migration to save 20%.** A migration costs engineering weeks and a class of bugs
  that appears only in production. The case has to be much larger than 20%.
- **Do not compare list prices across clouds.** Nobody pays list, and the workload shapes the answer.
- **Do not treat a reserved-instance recommendation as a saving** until the waste is gone.
- **Do not recommend turning off logging to save money.** It is the line that tells you why the bill
  moved next month.
- **Do not read a bill without the account it belongs to.** Analysing the wrong account is a
  confident answer about someone else's business.
