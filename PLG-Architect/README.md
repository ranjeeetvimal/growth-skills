# PLG-Architect

A 7-skill suite that takes a founder from a URL to an evidence-based, executable
growth strategy — and leaves behind durable artifacts (a one-page Strategy Snapshot
and a Decision Log) that the whole suite and future sessions build on.

Install from the [repo root Quick Start](../README.md#quick-start).

## Run them in this order

The suite is **Context → Research → Strategy → Execution**. Each skill reads the
shared `.claude/founder-context.md` (and, once written, `.claude/strategy-snapshot.md`),
so context flows forward and nothing gets re-asked.

| # | Skill | Phase | What it does |
|---|---|---|---|
| 1 | **founder-context** | Context | Ask for a URL, auto-draft the whole business context, confirm via terminal options. Saves `.claude/founder-context.md`. |
| 2 | **icp-research** | Research | Draft the beachhead + personas as hypotheses; score desperation; map trigger events, watering holes, and a 30-day validation plan. |
| 3 | **competitive-intel** | Research | Find 8–12 competitors itself; build the positioning matrix; separate real moats from table-stakes. |
| 4 | **plg-strategy** | **Strategy** | Synthesize the research into alternative strategies, a numbered action list, and a 30-day plan. **Writes the Strategy Snapshot + Decision Log** the execution skills obey. |
| 5 | **viral-loops** | Execution | Design the loops, the step-by-step activation, and the retention playbook — K-factor modeled honestly. |
| 6 | **content-strategy** | Execution | Pick 1–2 channels, draft the SEO clusters + free-tool ideas, lay out a week-by-week 90-day calendar. |
| 7 | **growth-metrics** | Execution | A North Star + guardrail, an AARRR target table, and 3 experiments with kill criteria. |

**Why this order:** strategy should be *built from* research, not guessed ahead of it.
Running `plg-strategy` after `icp-research` and `competitive-intel` means the Snapshot
it writes — and every execution skill downstream — rests on real customer and market
findings, not first-pass assumptions.

You can still invoke any skill directly; the order is a recommendation, not a lock.

## Example prompts (copy-paste)

Describe your problem and the right skill activates — or name one explicitly:

```
Set up my founder context — interview me about my business.
I need a PLG strategy for my SaaS. We help [X] do [Y].
Red-team my business model — I think our moat is [assumed moat].
Validate my ICP. I think it's [target audience].
Find my real moats. We lose deals to [Competitor A] and [Competitor B].
Design a viral loop — users invite teammates to collaborate.
Define my North Star metric. We're a [type] with [pricing].
```

## How context flows

- `founder-context` writes `.claude/founder-context.md` — every skill reads it.
- `plg-strategy` writes `.claude/strategy-snapshot.md` (principles the execution skills
  obey) and appends `.claude/decisions.md` (an ADR log with revisit triggers).
- These files are per-project and may hold private business data — they're gitignored.

## Principles every skill follows

1. **Founder-first** — hard questions before answers.
2. **Bet-driven** — every recommendation is a quantified bet, not a tactic list.
3. **Sacrifice-focused** — name what you WON'T do, with reasons.
4. **Evidence-typed** — claims are labeled Fact / Evidence / Inference / Assumption / Hypothesis, with confidence.
5. **Elaborate + honest** — worked-out plays, not fragments; the truth threaded in, not a cheerleading deck.
