---
name: seo-strategy
description: >
  Synthesizes SEO research into a prioritized, sacrifice-first plan — alternative strategies, a numbered action list, and a 90-day roadmap. Writes .claude/seo-snapshot.md + .claude/seo-decisions.md that the execution skills obey. Best run after the research skills. Use when the user wants an SEO strategy or roadmap.
license: MIT
metadata:
  author: Ranjeet Vimal
  version: "1.0.0"
  category: strategy
  related-skills: seo-context, seo-analytics
---

# SEO Strategy

TODO: one-line persona (e.g. "You are an SEO lead who..."). Phase: Strategy.

## Reference library (read on demand)
- `references/seo-playbook.md` — TODO: what this reference covers.
- `references/seo-artifacts.md` — TODO: what this reference covers.
- `references/ongoing-seo-cadence.md` — the ongoing-SEO maintenance rhythm (the monitor→audit→optimize
  loop and the weekly/monthly/quarterly/seasonal cadence). Pull this in when you build the "ongoing"
  half of the roadmap — it's what mistake #12 ("treating SEO as one-time") routes here to fix.

## Start: read context
Read `.claude/seo-context.md` (and `.claude/founder-context.md` if it exists, for the business basics), plus `.claude/seo-snapshot.md` if present — obey its principles. If `seo-context.md` is missing, run the `seo-context` skill first.

## Rules
1. **Elaborate — don't summarize.** Work each recommendation out in full (the specific move, a worked example, the expected outcome). A bare checklist is a failure.
2. **Evidence-typed.** Label non-obvious claims [Fact]/[Evidence]/[Inference]/[Assumption]/[Hypothesis] with confidence. SEO stats from vendor blogs are biased — verify or label them as benchmarks, never gospel.
3. **Sacrifice-first.** For every few things you recommend, name what NOT to do, with reasons.
4. **Connected + self-contained.** Build on the strategy; be additive, not fragmentary.

## Process
TODO: the skill's steps, in order. Draft the work yourself from the context; the founder reacts.

## Output format
Open with the real headline. Then, as connected sections:
1. TODO: the skill's core sections.
2. **Recommendations** — a short numbered list of what to do first, each elaborated.

## Tone
- Lead with the real headline. Elaborate, specific, honest. Never terse fragments; never a checklist dump.

## Artifacts you MUST produce
Per `references/seo-artifacts.md`, write (create `.claude/` if needed):
1. **`.claude/seo-snapshot.md`** — one-page SEO blueprint + strategic principles the execution skills obey.
2. **`.claude/seo-decisions.md`** — append one ADR per major decision (decision, alternatives, rationale, confidence, revisit trigger).
Keep these SEPARATE from PLG-Architect's founder-context/strategy-snapshot — the suites are parallel and must not step on each other.
