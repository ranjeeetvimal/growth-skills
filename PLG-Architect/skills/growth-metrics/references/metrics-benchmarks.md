# Metrics Benchmarks + Templates

## North Star patterns by model
Pick ONE metric that reflects delivered customer value, leads revenue, is
team-influenceable, and is cleanly measurable. Patterns:
- Usage/creation product → "weekly [core value action]s completed"
- Marketplace → "weekly matched transactions"
- Content/consumption → "weekly active [value] consumed"
Always pair with a **guardrail** that must not degrade as the NSM grows (e.g.
opt-out rate < 1%, error rate, refund rate). NSM up + guardrail down = the failure
mode that kills the brand.

## AARRR benchmark targets (starting hypotheses — recalibrate on real cohorts)
| Stage | Metric | Reasonable day-90 target |
|---|---|---|
| Acquisition | Visitor → signup | 3-5% (free/no-card can beat this) |
| Acquisition | Loop K-factor | ≥ 0.15 |
| Activation | Signup → aha < 24h | ≥ 50% |
| Activation | Median TTV | < 5 min |
| Retention | Week-4 active rate | ≥ 25% |
| Revenue | Free → paid (90-day cohort) | 2-5% |
| Revenue | Trial → paid | 8-12% |
| Referral | % signups from loops | ≥ 20% |
Label these as benchmarks, not promises. Every target needs a source or a "hypothesis" tag.

## The "So what?" test (kill useless metrics)
For each metric: what decision does it inform? what do we do if it moves up/down?
can we influence it? can we measure it accurately? If any answer is "nothing/no", kill it.

## Funnel instrumentation
Visit → Signup → [riskiest setup step, its own event] → aha → power-usage → PQL → paid.
Cohort retention table: weekly cohorts, metric = "did the core value action this week."

## Experiment template
```
Hypothesis: If [change], then [metric] because [reason]
Success metric: [one] | Guardrail: [one that must not drop]
Expected lift: [%, with source] | Confidence: H/M/L | Effort: [days]
Kill criteria: [when to stop]
```
Run 3 experiments, not 10. Every experiment needs a kill criteria BEFORE it starts.

## PMF check
At ~500 activated users, run the Sean Ellis survey. ≥40% "very disappointed if this
went away" = signal to scale spend. Below that, fix activation/retention first.

## Ceiling / TAM check (when the founder's fear is "can I scale past $X?")
If the fear is a revenue ceiling, MODEL it — don't just name it. Rough math:
`reachable segment size × realistic paying % × annual price = ceiling estimate`.
- Reachable segment = the beachhead, not the whole TAM (be honest about "reachable").
- Paying % for a self-serve freemium tool is often low single digits of active users.
- Then compare to the fear. Example shape: "200k reachable creators × 2% paying ×
  $120/yr ≈ $480k — the ceiling isn't the segment, it's ARPU/conversion" OR "...×
  0.5% × $120 ≈ $120k — the segment IS the ceiling; you need a wider beachhead or
  a higher-ARPU tier." State every input as a labeled assumption to validate.
This answers the founder's actual question instead of deferring it.
