# Social Media

Organic social-media growth skills — parallel to PLG-Architect and the SEO suite. A **gatekeeper that picks your platform**, then **one skill per platform**, each built to grow a *real, revenue-tied audience* (not vanity followers), the sacrifice-first, evidence-based way the other suites work.

**Install the whole suite** — the gatekeeper (`social-context`) routes to the platform skills, so they only work installed together:
- **Claude Code:** `/plugin install social-media@growth-skills`
- **Any agent:** `npx skills add ranjeeetvimal/growth-skills` (installs every suite)

Then reload — see the [root Quick Start](../README.md#quick-start). (Avoid `--skill social-context` on its own — you'll get a gatekeeper that routes to skills you didn't install.)

## The skills

| Skill | Platform | Status | What it does |
|---|---|---|---|
| **social-context** | entry / router | ✅ Live | **Start here.** Reframe followers → revenue, pick the 1-2 platforms your ICP is actually on (and name what to skip), then route to the platform skill. |
| **x-growth** | X (Twitter) | ✅ Live | Design the profile funnel + reply game, honest post craft (hook → value → proof → CTA), the 2026 realities (AI-slop, Premium, Community Notes), and the anti-patterns to avoid. |
| linkedin-growth · instagram-growth · tiktok-growth · youtube-growth · threads-growth | various | 🚧 Planned | Same pattern, one per platform. |
| content-repurposing | cross | 🚧 Planned | Turn one idea into platform-native posts across the suite. |

## How to use

**Start with `social-context`** — it decides which platform(s) you should even be on, then routes you. Already know it's X? Jump straight to `x-growth`.

```
Which platform should I be on for my B2B SaaS?      → social-context
Help me grow on X. My handle is @ranjeetvimal3.     → x-growth
How do I get more reach on X for my SaaS?           → x-growth
What content lane should I pick on X?               → x-growth
Turn my X profile into an email funnel.             → x-growth
My X posts get no engagement — what am I doing wrong? → x-growth
```

`social-context` inherits your founder-context, reframes "more followers" into a revenue goal, picks the 1-2 platforms your ICP actually uses, and writes `.claude/social-context.md`. `x-growth` then reads that and designs the X strategy + funnel — it starts by asking for your handle, then walks you through option-prompts (goal, traction, cadence, lane) before drafting the plan.

## How context flows

- `social-context` reads `.claude/founder-context.md` (if PLG-Architect wrote it) and writes `.claude/social-context.md` — the platform decision + reframed goal.
- `x-growth` reads both, then writes `.claude/x-context.md`.
- No hard dependency between suites; the coupling is just the shared `.claude/` files.

## Principles

Founder-first · audience-to-revenue (not vanity followers) · focus (pick your platform, skip the rest) · sacrifice-focused · evidence-typed · elaborate + honest · never ban-risk.
