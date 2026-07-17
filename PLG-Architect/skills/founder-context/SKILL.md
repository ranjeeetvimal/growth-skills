---
name: founder-context
description: >
  Collects founder-specific business context the magic way — ask for a URL,
  auto-draft the whole context from the site (plus light research), and have
  the founder confirm/correct instead of typing it all. Then asks only for
  what a site can't know (evidence, assumptions, constraints, goals, fears).
  Saves to .claude/founder-context.md so every other growth skill reads it
  instead of asking again. Use at the start of any growth conversation, or
  when another skill reports that founder context is missing.
license: MIT
metadata:
  author: Ranjeet Vimal
  version: "0.5.0"
  category: context
  related-skills: plg-strategy, icp-research, competitive-intel, viral-loops, content-strategy, growth-metrics
---

# Founder Context — URL In, Context Out

Collect the founder's context ONCE, and make it feel like magic: they give you
a URL, you draft everything you can from it, they confirm and correct. You only
*ask* for what a website genuinely can't tell you. Never make them type what you
can already see.

## First: check for existing context
If `.claude/founder-context.md` exists, read it, summarize in 2-3 lines, ask
"Still accurate?" and only re-do what changed. Otherwise start below.

## Step 1 — Ask for the URL (the ONE thing you need to start)
Open with: "Drop your URL and I'll draft your whole context — you just confirm
and correct. No site yet? Describe it in a sentence and we'll go from there."
Nothing else. One ask.

## Step 2 — Auto-draft from the URL (do the work FOR them)
Read the public site (and do a quick competitor search if useful). Draft every
field you can infer. Mark each as **(from your site)** — solid — or **(my guess —
confirm)** — inferred. Fields to fill from the URL:
- **Product** — one sentence.
- **Stage** — best guess from site maturity [Idea / MVP / Private Beta / Public Launch / Early Revenue / Growth / Scale].
- **Business model + pricing** — [Free / Freemium / Subscription / Usage-based / Marketplace / Enterprise / Ads / Hybrid].
- **ICP** — "your first 100 will be ___ because ___" (a guess to confirm; avoid "everyone").
- **Problem** — "before us, customers… / after us, customers…" (from the copy).
- **Alternatives** — top 3 they compete with (from research).
- **Why you** — the claimed differentiator, one sentence.

## Step 3 — Present the draft, invite corrections (not field-by-field)
Show the whole draft as one scannable block. Say: "Here's what I pulled — reply
**'looks good'** to accept it all, or just tell me what's wrong." Accept natural
corrections; don't force a yes/no on every line. This is the magic moment — make
it feel like you already understand the business.

## Step 4 — Ask only what the site can't know (brief, pre-guess where you can)
Now the internal-only fields. Ask these one at a time or in tight logical groups,
and offer a best-guess draft for the founder to confirm wherever the business type
makes one reasonable. "I don't know" is valid — record it as a gap.
- **Evidence** for the ICP — [none / personal experience / interviews / waitlist / active users / paying / revenue / referrals] + their strongest proof.
- **Top 3 assumptions** that must be true for this to work.
- **Biggest unknown** — "we don't know whether…".
- **Constraints** — team size, runway, budget, eng capacity, founder strengths + weaknesses.
- **The ONE 90-day goal** — a single objective (first 20 paying, validate PMF, $5k MRR, 1,000 activated, raise seed).
- **Biggest fear** — one sentence.
- **Failure condition** — "if ___ happens, we'll rethink the strategy."
- **Won't-do list** — hard lines (no paid ads, bootstrap only, privacy-first, no enterprise…).

## Step 5 — Save the context
Assemble into the block below and **write it to `.claude/founder-context.md`**
(create `.claude/` if needed). If you can't write files, print it and tell them to save it.

```
# FOUNDER CONTEXT

## Business
Product: [one sentence]
Stage: [Idea / MVP / Private Beta / Public Launch / Early Revenue / Growth / Scale]
Business model: [Free / Freemium / Subscription / Usage-based / Marketplace / Enterprise / Ads / Hybrid]
Pricing: [price or "not set"]

## Customer & Problem
ICP (first 100): [who] because [why]
Problem: before us [...] → after us [...]
Evidence for ICP: [none / personal / interviews / waitlist / active users / paying / revenue / referrals] — strongest: [...]

## Competition & Positioning
Alternatives today: [top 3]
Why us: [one sentence]

## Strategy & Validation
Key assumptions (must be true): [1; 2; 3]
Biggest unknown: we don't know whether [...]

## Constraints & Priorities
Constraints: [team / runway / budget / eng capacity / founder strengths / weaknesses]
90-day goal (ONE): [...]

## Risk & Decisions
Biggest fear: [...]
Failure condition: if [...] we rethink
Won't do: [...]

## Gaps
[fields still unknown / to validate]
```

Confirm in one line: "Saved to `.claude/founder-context.md` — every other skill
reads this, so you won't repeat yourself."

## How other skills use this
Every skill starts by reading `.claude/founder-context.md`. plg-strategy also uses
the assumptions, constraints, failure condition, and won't-do list directly (its
stress-test, kill/pivot signals, and sacrifices). If the file is missing, skills
run this one or ask inline — they never invent numbers.
