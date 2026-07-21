# Growth Skills by Ranjeet Vimal

> A collection of open-source agent skills for growth, marketing, and analytics.
> Built by founders, for founders. Works across Claude Code, Cursor, Gemini CLI,
> GitHub Copilot, Antigravity, and other agents on the [Agent Skills spec](https://github.com/anthropics/skills).

## Skill Suites

| Suite | Skills | Status | What It Covers |
|---|---|---|---|
| **[PLG-Architect](PLG-Architect/)** | 7 | ✅ Live | Founder context intake, PLG strategy, ICP research, competitive moats, viral loops, content strategy, growth metrics |
| **Paid-Marketing** | 0 | 🚧 Coming soon | Meta Ads, Google Ads, TikTok Ads, creative testing, attribution |
| **SEO** | 11 | 🚧 In progress | Technical + AI-crawler audit (with site architecture), AI-search & entity optimization, keyword & competitor research, SEO strategy, on-page, content, link building, local, programmatic, analytics |
| **Analytics** | 0 | 🚧 Coming soon | Event tracking, cohort analysis, experiment design, data pipelines |

## Installation

### Option A: Cross-Agent CLI (Recommended)

Works in Claude Code, Cursor, Gemini CLI, GitHub Copilot, Antigravity, and any
agent on the [Agent Skills spec](https://github.com/anthropics/skills). The CLI
detects which agents you have and installs into `.agents/skills/`, shared across
all of them.

```bash
# Install all skills from this repo
npx skills add ranjeeetvimal/growth-skills

# Install a specific skill
npx skills add ranjeeetvimal/growth-skills --skill plg-strategy

# Install multiple specific skills
npx skills add ranjeeetvimal/growth-skills --skill plg-strategy icp-research

# List available skills before installing
npx skills add ranjeeetvimal/growth-skills --list

# Install globally (available across all your projects)
npx skills add ranjeeetvimal/growth-skills -g
```

By default this installs into the current project. Add `-g` for a global
install at `~/.agents/skills/`. **After installing, you must reload** — see
[Reloading](#reloading) below (it is not a terminal command).

### Option B: Claude Code Native Plugin

Run these **inside a Claude Code session** (not the shell). Add this repo as a
plugin marketplace, then install the `plg-architect` plugin from it.

```
# Add the marketplace — GitHub shorthand
/plugin marketplace add ranjeeetvimal/growth-skills

# ...or the full Git URL (works the same way)
/plugin marketplace add https://github.com/ranjeeetvimal/growth-skills.git

# Browse and install interactively
/plugin
# Then select plg-architect → Install now

# ...or install directly
/plugin install plg-architect@growth-skills
```

The GitHub link and the `owner/repo` shorthand are equivalent — use whichever you
have handy. After installing, reload (see [Reloading](#reloading)). To pull later
updates: `/plugin marketplace update growth-skills` then `/plugin update plg-architect@growth-skills`.

### Option C: Claude.ai Web

Two ways, depending on your plan:

**C1 — ZIP upload (any plan, per user).** The simplest route for this public repo.
1. ZIP an individual skill folder (e.g. `PLG-Architect/skills/plg-strategy/`), so `SKILL.md` sits at the root of the ZIP
2. Go to [claude.ai](https://claude.ai) → Customize → Skills
3. Click **Upload skill** and select the ZIP (repeat per skill)
4. Skills auto-activate when relevant

*Requires code execution / file creation enabled. Available on Free, Pro, Max, Team, and Enterprise.*

**C2 — GitHub plugin marketplace (Team / Enterprise org admins).** claude.ai can sync a plugin marketplace straight from a GitHub repo — the same `.claude-plugin/marketplace.json` used by Claude Code.
1. As an org Owner/Primary Owner: **Organization settings → Plugins → Add plugin → GitHub**
2. Enter the repo in `owner/repo` format; the marketplace's plugins become installable org-wide

> ⚠️ **Public repos aren't allowed on the web GitHub sync** — claude.ai only accepts **private or internal** repos, and the [Claude GitHub App](https://support.claude.com/en/articles/10167454) must be installed on that repo. Since **this repo is public**, fork it into a private repo in your org first, then point the plugin there. (Public-repo, no-login installs use Option A `npx skills`, or Option B `/plugin` inside Claude Code.)

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

## Updating, Reloading & Uninstalling

### Updating

**If you installed with the CLI (`npx skills`):**

```bash
# Refresh skills you already have to their latest version
npx skills update
```

> ⚠️ **`update` only refreshes skills you already installed. It does NOT pull
> new skills added to the repo since your last install.** When this repo adds a
> skill (e.g. `founder-context`), `update` will skip it. To pick up new skills,
> re-run `add` — it installs anything missing and overwrites the rest:
>
> ```bash
> npx skills add ranjeeetvimal/growth-skills
> ```
>
> A `Failed to check for deleted skills` warning during update is harmless — it
> just means the repo removed some files (old reference templates) and the CLI
> noted it. Your skills still update.

**If you installed as a Claude Code plugin (Option B):** run inside Claude Code:

```
/plugin marketplace update growth-skills
/plugin update plg-architect@growth-skills
```

If `/plugin update` reports "already up to date" but you know the repo changed,
run `/plugin marketplace update` first (it re-pulls the files), or remove and
re-add the marketplace to force a clean pull.

### Reloading

Installing or updating writes files to disk — your agent still needs to pick
them up. **None of these are shell commands.**

- **Claude Code:** type `/reload-skills` inside the session (or restart Claude Code).
- **Cursor / Gemini CLI / GitHub Copilot / Antigravity / others:** restart the
  session — skills are discovered on startup.

### Verifying & Uninstalling

```bash
# See what's installed, where, and for which agents
npx skills list

# Remove a skill (interactive), or name one:
npx skills remove --skill plg-strategy
```

CLI-installed skills live at `~/.agents/skills/<name>` (global) or
`.agents/skills/<name>` (project), symlinked into each detected agent.

---

## How to Use These Skills

> **TL;DR:** The suite runs **Context → Research → Strategy → Execution**. Start with
> `founder-context`, then the two research skills (`icp-research`, `competitive-intel`),
> then `plg-strategy` to synthesize — then the three execution skills. Strategy is built
> *from* research, not guessed ahead of it. You can still invoke any skill directly; the
> sequence is a recommendation, not a lock.

### The Skill Sequence

| # | Skill | Phase | What It Does |
|---|---|---|---|
| 1 | `founder-context` | **Context** | Ask for a URL, auto-draft the whole business context, confirm via terminal options. Saves `.claude/founder-context.md` so nothing gets re-asked. |
| 2 | `icp-research` | Research | Drafts the beachhead + personas as hypotheses, scores desperation, and gives a 30-day validation plan. |
| 3 | `competitive-intel` | Research | Finds 8–12 competitors itself, builds the positioning matrix, separates real moats from table-stakes. |
| 4 | `plg-strategy` | **Strategy** | Synthesizes the research into alternative strategies, a numbered action list, and a 30-day plan. Writes the Strategy Snapshot + Decision Log the execution skills obey. |
| 5 | `viral-loops` | Execution | Designs the loops, the step-by-step activation, and the retention playbook. Models K-factor honestly. |
| 6 | `content-strategy` | Execution | Picks 1–2 channels, drafts the SEO clusters + free-tool ideas, lays out a week-by-week 90-day calendar. |
| 7 | `growth-metrics` | Execution | North Star + guardrail, an AARRR target table, and 3 experiments with kill criteria. |

**Why this order:** `plg-strategy` is the synthesizer, not the opener — running it *after*
the research means its Snapshot (and every execution skill downstream) rests on real
customer and market findings, not first-pass assumptions.

**How to invoke:** Just describe your problem naturally — skills auto-activate by context. Or name one explicitly:
```
"Use plg-strategy to red-team my business model."
"Run icp-research on my target audience."
"Apply growth-metrics to define my North Star."
```

### Example Prompts (Copy-Paste Ready)

Replace bracketed placeholders with your details.

**founder-context:**
```
"Set up my founder context — interview me about my business."
```

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

`plg-strategy` produces output in stages and pauses for your input between them.
It recommends an order but **cannot technically prevent you from using other
skills** — the staging is a design pattern, not enforcement.

**Stage 1: Assumption Validation**
- "You believe [X] is your #1 differentiator. What evidence proves this?"
- "You believe [Y] is your ICP. Have you talked to 10 of them?"

**Stage 2: Red-Team**
- "Here are 3 ways your business could fail..."
- "How do we build strategy that SURVIVES these failures?"

**Stage 3: Strategy Memo (Sacrifice-First)**
- "For every 3 things we recommend, here are 5 we are telling you NOT to do."

**Stage 4: Tactics**
- Recommends which skill to run next — **you** invoke it. `plg-strategy` can't load other skills itself.

### Direct Skill Use

If you already validated your assumptions, invoke any skill directly:

```
"Use icp-research directly. I already have 10 customer interviews."
```
```
"Use growth-metrics directly. I need experiment kill criteria."
```

Skills will still ask hard questions — they don't skip validation rules.

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

Contributions welcome:

1. Fork the repo
2. Add your skill suite under `Suite-Name/skills/`
3. Follow the [skill template](PLG-Architect/skills/plg-strategy/SKILL.md)
4. Add evals in `Suite-Name/skills/your-skill/evals/evals.json`
5. Submit a PR

## Changelog

Tracked in the [commit history](https://github.com/ranjeeetvimal/growth-skills/commits/main).

## License

MIT — Ranjeet Vimal
