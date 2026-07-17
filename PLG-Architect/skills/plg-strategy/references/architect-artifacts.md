# Architect Artifacts — Templates the strategy skill produces

plg-strategy is the Architect: it doesn't just advise, it produces durable,
reusable artifacts other skills and future sessions build on. Write these to
`.claude/` alongside `founder-context.md`. Keep them tight — one page each.

---

## 1. Evidence Framework (a labeling discipline, use everywhere)
Tag every load-bearing claim so the reader knows what they're standing on:
- **[Fact]** — verifiable, sourced, not in dispute.
- **[Evidence]** — real data point that supports a claim (with source).
- **[Inference]** — a reasoned conclusion FROM facts/evidence.
- **[Assumption]** — taken as true without proof; load-bearing if wrong.
- **[Hypothesis]** — a bet to be tested; pair with a validation task.

Rule: no **[Inference]** or strategy rests on an unlabeled **[Assumption]**.
Confidence (High/Med/Low) still tags the claim; the label tags its *type*.

## 2. Strategy Snapshot → write to `.claude/strategy-snapshot.md`
The one-page canonical blueprint. Every downstream skill reads this first (after
founder-context) instead of re-parsing the full report. Start with a YAML header
so it's semi-machine-readable without a separate JSON artifact:

```
---
icp: <one line>
positioning: <one line>
moat: <the 1-2 earnable ones>
gtm_motion: <PLG / sales-led / hybrid>
primary_bet: <the #1 bet>
top_risk: <the single biggest>
confidence: <High/Med/Low overall>
updated: <date — passed in, never invented>
---

# Strategy Snapshot — <product>
ICP: ... | Positioning: ... | Moat: ... | GTM: ...
Top 3 risks: ...
Confidence: ... (why)

## Strategic principles (5-10, immutable — downstream skills obey these)
1. <e.g. "Beachhead before breadth — no 'all creators' messaging.">
2. <e.g. "Never pitch safety as the headline; it's the architecture.">
...
```

## 3. Decision Log (ADR) → append to `.claude/decisions.md`
Append-only. One entry per major decision, never rewrite history:
```
## ADR-<n>: <decision title>  (<date>)
Decision: <what we chose>
Alternatives considered: <A, B — and why not>
Rationale: <why this one>
Confidence: <High/Med/Low>
Revisit when: <the trigger/metric that should reopen this>
```

## 4. Alternative Strategies (present, don't hide)
Don't hand over one thesis as if it were the only option. Offer 2-3:
```
Strategy A — <name>: <one line>. Win probability: <rough %>.
  Pros: ... | Cons: ... | Best if: <condition>
Strategy B — ... 
Recommended: <A/B/C> — because <the deciding factor>.
```
This is the antidote to single-thesis convergence: make the fork visible.

## 5. Trade-off + second-order (attach to every major rec)
- **Trade-off:** what this GAINS vs what it SACRIFICES (both explicit).
- **Second-order:** the downstream consequence of the first-order effect
  ("faster onboarding → more free users → higher infra cost → free-tier economics matter sooner").

## 6. Risk Register + Unknowns Register
```
RISKS         | Probability | Impact | Mitigation | Contingency
UNKNOWNS      | Why it matters | How to validate | Cost of being wrong
```
Risks = things that could go wrong. Unknowns = things you don't yet know that
change the plan. Both get an owner action.

## 7. Kill & Pivot criteria (per strategy, not just per experiment)
For each bet: **Continue if** <signal>, **Kill if** <signal>, **Pivot if** <signal>.

## 8. Strategic Timeline (Now / 30 / 90 / Post-PMF)
Organize the plan by horizon, not by skill:
- **Now (this week):** the 1-3 highest-leverage, lowest-regret moves.
- **30 days:** validation + first bets.
- **90 days:** scale what validated, kill what didn't.
- **Post-PMF:** the second-act moves (pricing tiers, expansion) — flagged, not started.

## 9. Opportunity ranking
Rank by: **Impact × Confidence ÷ Effort**, then break ties with **Time-sensitivity**
(decaying window?) and **Strategic importance** (moat-building vs one-off). Show the ranking.
