# Cloud right-sizing and unit economics

Cloud is the one line where the bill is a design document. It shows what was built, whether anyone used it,
and what the architecture assumed about scale.

## Read the bill in this order

| Step | Look at | What it tells you |
|---|---|---|
| 1 | Total by service, month over month | Which service is moving, and by how much |
| 2 | The top five services as a share | Usually 80-90% of the bill sits in five |
| 3 | Cost by tag or by account | Which environment and which team |
| 4 | The untagged remainder | The part nobody owns, and where the waste hides |
| 5 | Storage and data transfer separately | The two lines that grow silently |
| 6 | Commitments and credits | What is already prepaid, and what expires |

## The idle-resource checklist

These are the same twelve findings in almost every review. Walk them once.

| Resource | The finding | The saving shape |
|---|---|---|
| Dev and staging instances | Running 24x7 at production size | Schedule to working hours, or downsize |
| Orphaned volumes and snapshots | Attached to nothing, retained forever | Delete after the retention policy says so |
| Old AMIs, images and machine snapshots | Every deploy left one | Keep the last three |
| Idle load balancers | In front of a service with no traffic | Remove |
| Elastic IPs not attached | Billed for being unattached | Release |
| Over-provisioned databases | Sized for a launch that did not happen | Downsize, or move to a serverless tier |
| Multi-AZ in a single-region internal tool | Paying twice for a tool with no SLA | Single-AZ |
| Log storage with no retention | Every log line since day one | Set retention, archive to cold storage |
| NAT gateway data charges | A design that routes internal traffic through NAT | VPC endpoints |
| Cross-region replication | Configured once "for safety", never reviewed | Keep it for what is actually critical |
| Unused reserved instances or savings plans | Bought for a workload that moved | Exchange or let expire knowingly |
| Managed services for a workload that is idle | A queue or cluster with no consumers | Delete, do not pause |

## Right-sizing without guessing

| Signal | Reading | Action |
|---|---|---|
| CPU p95 under 20% for a month | Over-provisioned | Downsize one step, watch for a week |
| Memory p95 under 30% | Over-provisioned, or leaking slowly | Downsize, and check the leak |
| CPU p95 above 80% | Genuinely loaded | Right size, or fix the query first |
| Bursty with a low mean | A scheduling or serverless candidate | Not a bigger instance |
| Steady with a high mean | A commitment candidate | Reserved or savings plan |
| Traffic flat, cost rising | Storage, logs, or data transfer | Look there, not at compute |

Use p95, not average. An average hides the spike that decides the instance size, and a p95 hides the outlier
that does not.

## Unit economics: divide the bill by the business

| Business | The denominator | The number that matters |
|---|---|---|
| D2C store | Orders shipped | Cloud cost per order |
| SaaS | Monthly active users | Infrastructure cost per MAU |
| Marketplace | Transactions | Cost per transaction |
| API product | 1,000 requests | Cost per thousand requests |
| Agency | Client accounts | Cost per account |
| Internal tool | Employees served | Cost per employee per month |

The comparison that earns its keep is **cost per unit against three months ago and against last year**. A bill
that doubled while orders tripled is a business scaling. A bill that doubled while orders grew 20% is an
architecture that does not know how to be small.

## The five architectural causes of a bill that will not stop growing

1. **Chatty services.** Ten internal HTTP calls where one query would do, each billed in data transfer.
2. **No caching.** Every page view hits the database, so the database is sized for peak page views.
3. **Logging everything at debug, forever.** Observability is 10-25% of many bills and nobody looks.
4. **A per-tenant database or instance** that was right at ten customers and is not at a thousand.
5. **Egress.** Serving media from compute instead of a CDN, or replicating between regions for no reason.

None of these are fixed by a cheaper instance. Say which one it is, and price the fix as an engineering cost,
not a saving.

## Commitments, honestly

| Instrument | What it is | The risk |
|---|---|---|
| Reserved instances | 1 or 3 years on a specific instance family | The workload changes family and the commitment is stranded |
| Savings plans | A spend commitment, more flexible | Still a commitment against a forecast |
| Spot / preemptible | Cheap, interruptible | Only for stateless or checkpointed work |
| Enterprise discount | Negotiated against a spend commitment | Requires a forecast the business can actually make |

The rule: commit only against a baseline that has been stable for six months, and only to the level of that
baseline. Committing to the peak is how a business pays for capacity it stopped needing.

## Anti-patterns

- **Optimising the biggest line only.** The top line is often already efficient; the twelve small ones are not.
- **Deleting without a retention decision.** An orphaned volume may be the only copy of something.
- **Downsizing the database before fixing the query.** The next month it is back, and the migration was wasted.
- **Treating a savings plan as a saving.** It is a discount on spend that continues; if the spend stops, it is
  a loss.
- **A cost review with no denominator.** Absolute rupees cannot tell growth from waste, and the founder will
  read a rising bill as a failing team.
