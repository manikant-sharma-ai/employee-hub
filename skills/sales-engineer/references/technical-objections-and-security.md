# Technical objections and security answers

The technical objection is rarely about the technology. It is about risk - of looking
foolish, of an outage, of an audit finding, of being the person who signed.

## The five objections that stall deals

| Objection | What it usually means | What to do |
|---|---|---|
| "We need it on-premise" | a data-residency or IT-control requirement | map the actual requirement; offer the private-cloud or VPC option if it exists |
| "It won't integrate with X" | they have been burned by an integration promise | a tested integration, or a scoped integration spike with a date |
| "What happens at our volume" | a fear of the peak, not the average | a load test on their data shape, or the largest comparable deployment with the numbers |
| "Security won't approve it" | an unnamed approver with a checklist | get the checklist, answer it in writing, meet the reviewer |
| "We could build this ourselves" | they want control, or the build is a pet project | the cost of the build and its maintenance, honestly, plus where we are genuinely worse |

## Answering with evidence

Structure every technical answer the same way:

1. **The direct answer** - yes, no, or yes with a condition.
2. **The evidence** - a document, a test, a reference deployment, a named engineer.
3. **The limit** - where it stops working, stated before they find it.
4. **The workaround** - if there is one, and what it costs.

An answer with no limit is not believed. The limit is what makes the rest credible.

## The security questionnaire

This is where deals are lost quietly, three weeks after everyone thought it was won.

- **Ask for the full questionnaire at the start**, not the summary in the email.
- **Answer only from documents.** Certifications, the pen-test summary, the data-flow
  diagram, the sub-processor list, the retention policy, the incident process.
- **Where there is no document, write "gap - not currently documented" and the plan.**
  An invented answer that fails an audit is worse than a gap with a date.
- **The commercial boundary**: this role answers the technical and security content.
  Where the answers have to be assembled into a formal bid document, `proposal-writer`
  owns the document and this role supplies the content.

Common items an Indian buyer's IT team will ask:

- **Data residency** - where the data is stored and processed, and whether it can be
  kept in India.
- **DPDP Act readiness** - consent, purpose limitation, breach notification, the
  data-processor agreement, and who is the data fiduciary in their reading.
- **Access control** - SSO, MFA, role model, admin actions logged.
- **Sub-processors** - the list, with what each one does.
- **Backup and restore** - frequency, retention, the last tested restore.
- **Incident history and process** - notification timeline and who is told.
- **Exit** - how their data comes back, in what format, and how it is deleted.

Never give a legal opinion on DPDP, GDPR or a contract clause. State the fact, cite the
document, and route the interpretation to `legal-drafter` and a lawyer.

## Scale questions

Answer with a shape, not a boast: "the largest deployment we run today is X records a
month at p95 Y milliseconds; your peak is Z, which is N times that, so we would load-test
before committing to the SLA."

## Anti-patterns

- **"Yes, we can do that"** as a reflex, followed by a discovery in delivery.
- **Certification names used loosely** - saying "SOC 2 compliant" when the report is a
  Type I, or "ISO certified" without the scope.
- **Security answers over a call only**, with nothing in writing.
- **Sending a competitor comparison** the buyer did not ask for.
- **Winning the technical argument and losing the relationship** - the reviewer who was
  made to feel stupid in front of their boss will find another reason.
