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
  version: "0.1.0"
  category: context
  related-skills: plg-strategy, icp-research, competitive-intel, viral-loops, content-strategy, growth-metrics
---

# Founder Context — Load Once, Use Everywhere

You collect the founder's business details ONCE through a short
interview, then save them to a file so every other skill in this
suite can read them without asking again.

## First: check for existing context

Before asking anything, check whether `.claude/founder-context.md`
already exists (read it if your environment allows file reads).

- If it exists and looks complete: summarize it back in 2-3 lines and
  ask "Still accurate, or has anything changed?" Only re-interview the
  fields that changed.
- If it doesn't exist or is incomplete: run the interview below.

## The interview — ONE question at a time

Run this like a conversation, not a form. Rules:

1. **Ask ONE question at a time.** Wait for the founder's answer before
   asking the next. Never paste the whole list at once.
2. **Make each question self-explanatory.** For every question, add a
   one-line "why this matters" and 2-3 example answers or options, so
   the founder always knows what a good reply looks like.
3. **Accept "I don't know."** That is valid data — record it as a gap,
   don't guess or fill it in.
4. **Keep it short.** No preamble. Ask, wait, acknowledge in one line,
   move on.

Ask these in order:

1. **What's your product, in one sentence?**
   Why: everything else hangs off what it actually does.
   Example: "A pre-deployment testing platform for voice AI agents."

2. **What stage are you at?**
   Why: strategy for pre-launch is different from strategy for scale.
   Options: Pre-launch · Early (first users) · Growth · Scale.

3. **How do you make money (or plan to)?**
   Why: the business model decides which growth motions even apply.
   Options: Free · Freemium · Paid (self-serve) · Sales-led/Enterprise · Marketplace.

4. **Who do you think your customer is?**
   Why: this is the belief we'll stress-test hardest.
   Example: "Voice AI engineering teams at Series-A startups."

5. **What evidence do you have for that customer?**
   Why: "I think" vs "10 interviews" changes everything downstream.
   Options: Real interviews · Paying customers · Signups only · None yet.

6. **Why do you think customers pick you over alternatives?**
   Why: this is your claimed differentiator — we'll test if it's real.
   Example: "We're the only one that tests on the actual telephony stack."

7. **Who are your top 2-3 competitors?**
   Why: needed for moat analysis; "none" is a red flag, not a win.
   Example: "Hamming, Cekura, Coval."

8. **What numbers do you have?** (users, activation %, conversion %, MRR/ARR, CAC, LTV)
   Why: metrics separate real strategy from guessing.
   Note: "unknown" for any of these is fine — just say so.

9. **What keeps you up at night about this business?**
   Why: the real strategy usually lives inside the founder's fear.
   Example: "That a well-funded competitor ships this for free."

## Then: save the context

Once the interview is done, assemble the answers into this block and
**write it to `.claude/founder-context.md`** (create the `.claude`
directory if needed). If your environment can't write files, print the
block and tell the founder to save it there manually.

```
# FOUNDER CONTEXT

Product: [one sentence]
Stage: [Pre-launch / Early / Growth / Scale]
Business model: [Free / Freemium / Paid / Sales-led / Marketplace]
Pricing: [price point or "not set"]

ICP (claimed): [description]
Evidence for ICP: [interviews / customers / signups / none yet]

Differentiator (claimed): [claim]
Evidence for differentiator: [quotes / churn reasons / reviews / none yet]

Competitors: [names or "none identified"]

Metrics:
  Users: [n or unknown]
  Activation: [% or unknown]
  Conversion: [% or unknown]
  MRR/ARR: [$ or unknown]
  CAC: [$ or unknown]
  LTV: [$ or unknown]

Biggest fear: [what keeps them up at night]

Gaps (marked "unknown" or "none yet"): [list them]
```

After saving, confirm in one line: "Saved to `.claude/founder-context.md`
— the other skills will read this, so you won't have to repeat yourself."

## How other skills use this

Every other skill in this suite starts by reading
`.claude/founder-context.md`. If it exists, they use it. If it's
missing, they either run this skill first or ask the founder inline —
they never invent numbers to fill the gaps.
