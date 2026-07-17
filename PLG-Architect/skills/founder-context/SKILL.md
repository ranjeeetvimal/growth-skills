---
name: founder-context
description: >
  Collects founder-specific business context through a short guided
  interview, then saves it to .claude/founder-context.md so the other
  growth skills can read it instead of asking again or assuming.
  Use at the start of any growth conversation when the founder has
  not yet shared their product details, or when another skill reports
  that founder context is missing.
license: MIT
metadata:
  author: Ranjeet Vimal
  version: "0.4.0"
  category: context
  related-skills: plg-strategy, icp-research, competitive-intel, viral-loops, content-strategy, growth-metrics
---

# Founder Context — Load Once, Use Everywhere

You collect the founder's business details ONCE, fast, then save them
to a file so every other skill in this suite reads them without asking
again. Keep this short — the other skills do their own research
(competitors, benchmarks, keywords), so you only need what ONLY the
founder knows.

## First: check for existing context
Check whether `.claude/founder-context.md` exists (read it if you can).
- Exists and complete: summarize it in 2-3 lines, ask "Still accurate?"
  Only re-ask what changed.
- Missing/incomplete: run the interview below.

## The interview — ONE question at a time
Rules:
1. **Ask ONE question at a time.** Wait for the answer. Never paste the list.
2. **Make each self-explanatory** — one line of "why it matters" + 2-3
   example answers, so the founder knows what a good reply looks like.
3. **Offer a best-guess draft when you can.** If the founder gave a URL,
   read the public site first and pre-fill your guess for them to confirm
   or correct — don't make them type what you can already see.
4. **"I don't know" is valid** — record it as a gap, never guess a number.
5. **Keep it to 8 questions.** Don't ask for competitors — `competitive-intel`
   finds those. Don't ask for benchmarks — the skills supply those.

Ask, in order:
1. **Product, in one sentence?** (why: everything hangs off it) — pre-fill from their URL if given.
2. **Stage?** (why: pre-launch vs scale change everything) — Pre-launch · Early · Growth · Scale.
3. **How do you make money (or plan to)?** — Free · Freemium · Paid · Sales-led · Marketplace.
4. **Who do you think your customer is?** (why: the belief we'll stress-test) — one specific slice, not "everyone".
5. **What evidence do you have for that customer?** — Interviews · Paying users · Signups · None yet.
6. **Why do customers pick you over alternatives?** (why: your claimed wedge) — one sentence.
7. **What's your constraint?** (why: strategy is sequenced by it) — runway, team size, eng capacity, founder's strength/weakness, and the ONE metric that must move in 90 days. "Solo, 6 months runway, need first paying users" is a fine answer.
8. **What keeps you up at night about this business?** (why: the real strategy hides in the fear).

## Then: save the context
Assemble into this block and **write it to `.claude/founder-context.md`**
(create `.claude/` if needed). If you can't write files, print it and tell
the founder to save it there.

```
# FOUNDER CONTEXT

Product: [one sentence]
Stage: [Pre-launch / Early / Growth / Scale]
Business model: [Free / Freemium / Paid / Sales-led / Marketplace]
Pricing: [price or "not set"]

ICP (claimed): [description]
Evidence for ICP: [interviews / customers / signups / none yet]

Differentiator (claimed): [claim]
Evidence for differentiator: [quotes / churn reasons / reviews / none yet]

Metrics: [users / activation / conversion / MRR / CAC / LTV — or "unknown"]

Constraints: [runway / team size / eng capacity / founder strength+weakness / the one 90-day metric]

Biggest fear: [what keeps them up at night]

Gaps (unknown / none yet): [list them]
```

Confirm in one line: "Saved to `.claude/founder-context.md` — the other
skills will read this, so you won't repeat yourself."

## How other skills use this
Every other skill starts by reading `.claude/founder-context.md`. If it's
missing they run this skill or ask inline — they never invent numbers.
