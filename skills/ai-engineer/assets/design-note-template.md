# Design note: <system name>

**Date:** <YYYY-MM-DD>  **Owner:** <name>  **Version:** <0.1>

## The job
One sentence: what comes out the other end, and who uses it.

## Definition of done
The pass bar, written so a second person could grade it.
- Pass: ...
- Fail: ...

## Failure cases
| # | Input | What a naive attempt does | What correct looks like |
|---|---|---|---|
| 1 | | | |

## Architecture
Chosen shape (single call / loop / graph) and why. If a graph, list the nodes and the state schema.

## Context plan
What is in the window, what is fetched just in time, what is compressed, what is externalised.

## Tools
| Tool | Purpose | Read/Write | Confirmation gate |
|---|---|---|---|

## Budget
Max steps, max tokens, max wall clock, max cost per run, expected runs per day.

## Evals
| Version | Date | Model | Pass rate | Cost per success | Latency p95 |
|---|---|---|---|---|---|
| | | | | | |

## Known gaps
What was not tested, what is assumed, what would break first at 10x volume.
