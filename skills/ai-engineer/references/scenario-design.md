# Scenario design

A scenario is a concrete situation the system will meet in the wild, written so it can be replayed. Scenarios are how you find out what breaks before a customer does, and how you rehearse a decision you cannot afford to get wrong live.

## Anatomy of a usable scenario

Seven fields. If a field is missing, the scenario cannot be run twice the same way.

1. **Persona** - who is speaking and what they want.
2. **Opening** - the literal first message or input.
3. **Context** - what the system knows that the persona does not say.
4. **Constraints** - budget, timing, policy, prior history.
5. **The twist** - the thing that makes it hard. Every scenario needs one.
6. **Expected behaviour** - what a good response does, and what it must not do.
7. **Failure signal** - the observable sign that it went wrong.

## The matrix

Six to ten scenarios spanning these axes. Deliberately include the uncomfortable ones - a set that only confirms is not a test.

- **Happy path** - the ordinary case, done well.
- **Edge** - boundary values, empty data, one item, a thousand items.
- **Adversarial** - a hostile or manipulative input, an attempt to extract something it should not give.
- **Missing information** - the user has not said the thing the answer depends on.
- **Contradictory** - two requirements that cannot both hold. Does it notice, or does it invent a compromise?
- **Volume and repetition** - the tenth identical request in a row. Consistency drifts here.
- **Permission denied** - the tool fails or access is refused.
- **Time and locale** - wrong timezone, Indian date format read as US, ₹ and lakh/crore, a festival-week calendar.

## Where scenarios come from

Real material beats imagination: support tickets, sales call objections, your own worst day last quarter, logs of the prompts people actually type. Invented scenarios tend to be polite; real ones are not.

## Use them for

- **Pre-launch validation** - each scenario becomes an eval case with a pass condition.
- **Pricing and what-if** - "what if we drop the smallest plan", run against your numbers, with the failure signal being a margin below your floor.
- **Rehearsal** - a founder practising a hard investor question, or a salesperson facing a procurement objection.
- **Prompt stress testing** - feed the adversarial set and watch what leaks.

## Writing the expected behaviour

Write it as a checkable claim, not a feeling. "Asks for the budget once, then gives a range with the assumption stated" - not "handles it well". The checkable version can be graded by a person in seconds, or by a script.

## Keep the set

Scenarios live in the repo alongside the system. Re-run the whole set after any change to prompt, model or tools. A scenario that has never failed is either very well handled or not hard enough - check which.
