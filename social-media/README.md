# Social Media

Organic social-media growth skills — parallel to PLG-Architect and the SEO suite. **One skill per platform**, each built to grow a *real, revenue-tied audience* (not vanity followers), the sacrifice-first, evidence-based way the other suites work.

Install from the [repo root Quick Start](../README.md#quick-start), or grab one skill:
`npx skills add ranjeeetvimal/growth-skills --skill x-growth`.

## The skills

| Skill | Platform | Status | What it does |
|---|---|---|---|
| **x-growth** | X (Twitter) | ✅ Live | Reframe followers → revenue, gate on "is your ICP even on X?", design the profile funnel + reply game, honest post craft (hook → value → proof → CTA), the 2026 realities (AI-slop, Premium, Community Notes), and the anti-patterns to avoid. |
| social-context | — | 🚧 Planned | Optional gatekeeper: inherit founder-context, pick the platform(s) worth being on, route to the right skill. |
| linkedin-growth · instagram-growth · tiktok-growth · youtube-growth · threads-growth | various | 🚧 Planned | Same pattern, one per platform. |
| content-repurposing | cross | 🚧 Planned | Turn one idea into platform-native posts across the suite. |

## How to use

Each skill stands alone — just describe your goal and it activates:

```
Help me grow on X. My handle is @acme.
How do I get more followers / reach on Twitter?
What should I post on X to grow my SaaS?
```

`x-growth` reads your profile, reframes "more followers" into the real outcome (email / leads / distribution), checks whether your ICP is even on X, designs the loop + funnel, and writes `.claude/x-context.md`.

## How context flows

- `x-growth` reads `.claude/founder-context.md` if PLG-Architect already wrote it — business basics carry over, nothing re-asked — and writes `.claude/x-context.md`.
- No hard dependency between suites; the coupling is just the shared `.claude/` files.

## Principles

Founder-first · audience-to-revenue (not vanity followers) · sacrifice-focused · evidence-typed · elaborate + honest · never ban-risk.
