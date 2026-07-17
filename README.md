# Growth Skills by Ranjeet Vimal

> A collection of open-source agent skills for growth, marketing, and analytics.
> Built by founders, for founders. Works across Claude Code, Codex, Cursor, Windsurf, and 40+ agent platforms.

## Skill Suites

| Suite | Skills | Status | What It Covers |
|---|---|---|---|
| **[PLG-Architect](PLG-Architect/)** | 6 | ✅ Live | Product-Led Growth strategy, ICP research, competitive moats, viral loops, content strategy, growth metrics |
| **Paid-Marketing** | 0 | 🚧 Coming soon | Meta Ads, Google Ads, TikTok Ads, creative testing, attribution |
| **SEO** | 0 | 🚧 Coming soon | Keyword research, technical SEO, link building, programmatic SEO |
| **Analytics** | 0 | 🚧 Coming soon | Event tracking, cohort analysis, experiment design, data pipelines |

## Installation

### Option A: Cross-Agent CLI (Recommended)

Works in Claude Code, Codex, Cursor, Windsurf, and any agent on the [Agent Skills spec](https://github.com/anthropics/skills).

```bash
# Install all skills from this repo
npx skills add ranjeeetvimal/growth-skills

# Install a specific skill
npx skills add ranjeeetvimal/growth-skills --skill plg-strategy

# Install multiple specific skills
npx skills add ranjeeetvimal/growth-skills --skill plg-strategy icp-research

# List available skills before installing
npx skills add ranjeeetvimal/growth-skills --list

# Install globally (available across all projects)
npx skills add ranjeeetvimal/growth-skills -g
```

After installing, reload:
```bash
/reload-skills
```

Verify installation:
```bash
npx skills list
# or for global installs:
npx skills ls -g
```

### Option B: Claude Code Native Plugin

```bash
# Add this repo as a marketplace
/plugin marketplace add ranjeeetvimal/growth-skills

# Browse and install
/plugin
# Then select plg-architect → Install now

# Or install directly
/plugin install plg-architect@growth-skills
```

### Option C: Claude.ai Web (ZIP Upload)

1. ZIP an individual skill folder (e.g. `PLG-Architect/skills/plg-strategy/`), so `SKILL.md` sits at the root of the ZIP
2. Go to [claude.ai](https://claude.ai) → Customize → Skills
3. Click **Upload skill** and select the ZIP (repeat per skill)
4. Skills auto-activate when relevant

*Requires code execution / file creation enabled, on a plan that supports custom Skills. Verify the exact menu path in your own account — Claude.ai's UI changes.*

### Option D: Project-Local (Team Sharing)

```bash
# In your project root
mkdir -p .claude/skills
cp -r /path/to/growth-skills/PLG-Architect/skills/* .claude/skills/
```

Commit `.claude/skills/` to your repo. Everyone on the team gets the skills on clone.

### Option E: Git Submodule

```bash
git submodule add https://github.com/ranjeeetvimal/growth-skills.git .claude/skills/growth-skills
```

---

## How to Use These Skills

> **TL;DR:** Start with `plg-strategy`. It is designed to ask hard questions first. The other skills load contextually once assumptions are validated.

### The Skill Sequence

These 6 skills are designed to work in order, but **you can invoke any skill directly**. The sequence is a recommendation, not a lock.

| # | Skill | When to Use | What It Does |
|---|---|---|---|
| 1 | `plg-strategy` | **Start here if you have no strategy.** | Asks hard questions, red-teams your business, produces a sacrifice-first strategy memo. |
| 2 | `icp-research` | After you have a rough strategy but need to validate who you serve. | Finds your "desperate customer" (not just ideal). Tests if you can name 10 real people who fit all 5 criteria. |
| 3 | `competitive-intel` | After you know your ICP. | Analyzes what competitors can copy in 30 days vs. 3 years. Finds real moats, not feature lists. |
| 4 | `viral-loops` | After strategy + ICP + moats are clear. | Designs 1-2 viral loops as quantified bets. Models K-factor realistically. |
| 5 | `content-strategy` | After you know where your ICP hangs out. | Picks 1-2 channels (not 10). Sacrifice-first. SEO only if your ICP actually searches. |
| 6 | `growth-metrics` | After you have bets to measure. | Defines North Star + 3 experiments max. Every metric needs a "kill criteria." |

**How to invoke:** Just describe your problem naturally. Skills auto-activate by context. Or name one explicitly:
```
"Use plg-strategy to red-team my business model."
"Run icp-research on my target audience."
"Apply growth-metrics to define my North Star."
```

### Example Prompts (Copy-Paste Ready)

Replace bracketed placeholders with your details.

**plg-strategy:**
```
"I need a PLG strategy for my SaaS. We [describe what your product does]."
```
```
"Red-team my business model. I think our moat is [your assumed moat]."
```

**icp-research:**
```
"Validate my ICP. I think it is [describe your target audience]."
```
```
"Run the Desperate Customer Test on my target audience."
```

**competitive-intel:**
```
"Find my real moats. Our competitors are [Competitor A] and [Competitor B]."
```
```
"What can [top competitor] copy from us in 30 days? What would take 3 years?"
```

**viral-loops:**
```
"Design a viral loop for my product. Users invite team members to collaborate."
```
```
"Model the K-factor for our referral program. Be realistic, not optimistic."
```

**content-strategy:**
```
"Pick my channels. My ICP hangs out on [Platform A] and [Platform B]."
```
```
"Should we do SEO? Our ICP discovers tools on [Platform], not Google."
```

**growth-metrics:**
```
"Define my North Star metric. We are a [type of product] with [pricing model]."
```
```
"Set up 3 growth experiments with kill criteria."
```

### How plg-strategy Works (Staged, Not Gated)

`plg-strategy` produces output in stages. It recommends this order, but **cannot technically prevent you from using other skills**. The staging is a design pattern, not enforcement.

**Stage 1: Assumption Validation**
- "You believe [X] is your #1 differentiator. What evidence proves this?"
- "You believe [Y] is your ICP. Have you talked to 10 of them?"

**Stage 2: Red-Team**
- "Here are 3 ways your business could fail..."
- "How do we build strategy that SURVIVES these failures?"

**Stage 3: Strategy Memo (Sacrifice-First)**
- "For every 3 things we recommend, here are 5 we are telling you NOT to do."

**Stage 4: Tactics**
- Contextually loads other skills or recommends you invoke them next.

### Direct Skill Use

If you already validated your assumptions, invoke any skill directly:

```
"Use icp-research directly. I already have 10 customer interviews."
```
```
"Use growth-metrics directly. I need experiment kill criteria."
```

Skills will still ask hard questions — they don't skip validation rules.

### VS Code / Claude Code Tips

**In VS Code Claude Chat:**
- Skills auto-activate based on context. Just describe your problem.
- To force a skill: say `"Use [skill-name] to..."`
- If skills don't load: type `/reload-skills` or restart the chat panel.

**In Claude Code CLI:**
```bash
claude
# Then just talk naturally, or:
/plugin           # Browse plugins
/reload-skills    # Refresh after installing
```

**Check installed skills:**
```bash
npx skills list
# or for global:
npx skills ls -g
```

---

## Philosophy

Every skill in this repo follows the same principles:

1. **Founder-first** — Asks hard questions before giving answers
2. **Bet-driven** — Every recommendation is a quantified bet, not a tactic list
3. **Sacrifice-focused** — Strategy is what you WON'T do, not what you will
4. **Evidence-based** — Every claim has confidence level + validation plan
5. **Human tone** — Short sentences, opinions, "I think," "I worry"

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide. Quick version:

1. Fork the repo
2. Add your skill suite under `Suite-Name/skills/`
3. Follow the [skill template](PLG-Architect/skills/plg-strategy/SKILL.md)
4. Add evals in `Suite-Name/skills/your-skill/evals/evals.json`
5. Submit a PR

## Changelog

See [VERSIONS.md](VERSIONS.md).

## License

MIT — Ranjeet Vimal
