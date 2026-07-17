---
name: founder-context
description: >
  Collects founder-specific business context the magic way — ask for a URL,
  auto-draft the whole context from the site, and have the founder confirm or
  correct via TERMINAL MULTIPLE-CHOICE OPTIONS (not free-text typing). Then
  asks only for what a site can't know (evidence, assumptions, constraints,
  goals, fears), each as a pick-an-option question. Saves to
  .claude/founder-context.md so every other growth skill reads it. Use at the
  start of any growth conversation, or when a skill reports context is missing.
license: MIT
metadata:
  author: Ranjeet Vimal
  version: "0.6.0"
  category: context
  related-skills: plg-strategy, icp-research, competitive-intel, viral-loops, content-strategy, growth-metrics
---

# Founder Context — URL In, Context Out

Collect the founder's context ONCE, and make it feel like magic: they give you a URL,
you draft everything you can from it, and they confirm and correct by **picking options
in the terminal** — not by typing paragraphs. You only *ask* for what a website can't tell you.

## How to ask — options in the terminal, not prose (IMPORTANT)
Ask every question as a **multiple-choice option prompt** using the host's interactive
picker (in Claude Code, the terminal option selector). Rules:
- Present concrete, selectable options for every question that has discrete answers.
- Always include an **"Other"** choice so the founder can type a custom answer.
- Never ask a discrete-answer question as free-text prose. The founder should mostly
  *click*, not type.
- Use multi-select when more than one answer can apply (e.g. evidence types).
- If the host has no picker, fall back to a numbered list the founder answers with a number.
- The ONLY things typed freely are genuinely open (the URL, the one-sentence product
  if there's no site, a custom "Other" value).

## Step 1 — Ask for the URL
One ask: "Drop your URL and I'll draft your whole context — you just confirm and correct.
No site yet? Describe it in a sentence." (Free text here — a URL or a sentence.)

## Step 2 — Auto-draft from the URL
Read the public site (and a quick competitor search if useful). Draft every field you can,
each marked **(from your site)** — solid — or **(my guess — confirm)** — inferred:
Product · Stage · Business model + pricing · ICP ("first 100 will be ___ because ___") ·
Problem (before/after) · Alternatives (top 3) · Why-you (differentiator).

## Step 3 — Confirm the draft as ONE option prompt
Show the draft, then ask a pick-an-option question:
- **"Looks good — save it"** (accept all)
- **"Fix [guessed field]"** — one option per inferred field (e.g. "Fix the ICP", "Fix the stage")
- **Other** — the founder types any correction
If they pick a "Fix", re-ask just that field as its own option prompt, then continue.

## Step 4 — Ask the internal fields as option prompts
Each of these is a pick-an-option question with an "Other" escape. Offer a best-guess
default option where the business makes one reasonable.
- **Evidence for the ICP** (multi-select): None · Personal experience · Interviews · Waitlist · Active users · Paying customers · Revenue · Referrals.
- **Top assumptions** (offer 3 drafted assumptions to confirm/deselect + Other to add).
- **Biggest unknown** (offer 2-3 likely unknowns you inferred + Other).
- **Constraints** — ask as a few quick picks: team size (Solo · 2-3 · 4+), runway (<6mo · 6-12mo · 12mo+ · n/a), and founder strength (Building · Distribution · Sales · Design · Other). Budget/eng-capacity via Other if needed.
- **The ONE 90-day goal** (single-select): First paying customers · Validate PMF · Hit $X MRR · N activated users · Raise funding · Other.
- **Biggest fear** (offer 2-3 inferred fears + Other).
- **Failure condition** — "If ___ happens, we rethink" (offer 2-3 inferred + Other).
- **Won't-do list** (multi-select): No paid ads · Bootstrap only · Privacy-first · No enterprise · No agency model · Other.

## Step 5 — Save the context
Assemble into the block below and **write it to `.claude/founder-context.md`** (create `.claude/`
if needed). If you can't write files, print it and say where to save it.

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
Evidence for ICP: [selected] — strongest: [...]

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

Confirm in one line: "Saved to `.claude/founder-context.md` — every other skill reads this."

## How other skills use this
Every skill reads `.claude/founder-context.md`. plg-strategy also uses the assumptions,
constraints, failure condition, and won't-do list directly. If the file is missing, skills
run this one or ask inline — they never invent numbers.
