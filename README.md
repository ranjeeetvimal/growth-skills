# Growth Skills by Ranjeet Vimal

> A collection of open-source Claude skills for growth, marketing, and analytics.
> Built by founders, for founders.

## Skill Suites

| Suite | Skills | What It Covers |
|---|---|---|
| **[PLG-Architect](PLG-Architect/)** | 6 skills | Product-Led Growth strategy, ICP research, competitive moats, viral loops, content strategy, growth metrics |
| **Paid-Marketing** | *Coming soon* | Meta Ads, Google Ads, TikTok Ads, creative testing, attribution |
| **SEO** | *Coming soon* | Keyword research, technical SEO, link building, programmatic SEO |
| **Analytics** | *Coming soon* | Event tracking, cohort analysis, experiment design, data pipelines |

## Quick Install

```bash
# Install everything
npx skills add ranjeeetvimal/growth-skills

# Install just one suite
npx skills add ranjeeetvimal/growth-skills --suite PLG-Architect

# Install specific skills
npx skills add ranjeeetvimal/growth-skills --skill plg-strategy icp-research
```

After installing, reload skills:
```bash
/reload-skills
```

## How to Use These Skills (Step-by-Step)

> **TL;DR:** Start with `plg-strategy`. It gates you through validation before pulling in the other 5 skills. Do not skip stages.

### 1. Installation

#### Option A: Claude Code CLI / VS Code (Recommended)

```bash
# Install globally (works in VS Code Claude, Claude Code CLI, Cursor, etc.)
npx skills add ranjeeetvimal/growth-skills

# Or install just the PLG suite
npx skills add ranjeeetvimal/growth-skills --suite PLG-Architect

# Or install specific skills
npx skills add ranjeeetvimal/growth-skills --skill plg-strategy icp-research
```

After installing, reload skills in your Claude session:
```bash
/reload-skills
```

#### Option B: Claude Web (claude.ai) — Important Note

**These skills are built for Claude Code (CLI/VS Code), not the Claude web interface.** The Claude web app uses a different plugin architecture (MCP servers) that requires a different format than `SKILL.md` files.

**To use these skills in a web-like environment:**

1. **Use Claude Code in your terminal** (works identically to the web chat):
   ```bash
   claude
   ```
   Then chat naturally — skills auto-activate based on context.

2. **Use VS Code with the Claude extension:**
   - Install the Claude extension in VS Code
   - Open the Claude chat panel
   - Skills auto-activate when you describe your problem

3. **If you must use claude.ai web:**
   - Copy the relevant `SKILL.md` content from this repo
   - Paste it as a system prompt at the start of your conversation
   - Or use the copy-paste prompts below directly in the web chat

**Why the difference?** Claude web's "Plugins" tab (Settings → Plugins) is for MCP servers — external tools that connect to APIs. These skills are "persona prompts" that shape how Claude thinks. They install into Claude Code's skill system, not the web plugin system.

### 2. The Skill Order (Don't Skip This)

These 6 skills are designed to work in a **staged sequence**. `plg-strategy` is the gatekeeper — it loads the others only after you validate core assumptions.

| Stage | Skill | When to Use | What It Does |
|---|---|---|---|
| **1** | `plg-strategy` | **Always start here.** | Asks hard questions, red-teams your business, and produces a staged strategy memo. It will NOT let you move to tactics until you validate assumptions. |
| **2** | `icp-research` | After plg-strategy flags your ICP as unvalidated | Finds your "desperate customer" (not just ideal). Tests if you can name 10 real people who fit all 5 criteria. |
| **3** | `competitive-intel` | After you know your ICP | Analyzes what competitors can copy in 30 days vs. 3 years. Finds your *real* moats, not feature lists. |
| **4** | `viral-loops` | After strategy + ICP + moats are clear | Designs 1-2 viral loops as quantified bets. Models K-factor realistically. No wishful thinking. |
| **5** | `content-strategy` | After you know your channels from ICP research | Picks 1-2 channels (not 10). Sacrifice-first. SEO only if your ICP actually searches. |
| **6** | `growth-metrics` | After you have bets to measure | Defines North Star + 3 experiments max. Every metric needs a "kill criteria." |

**Rule:** If `plg-strategy` hasn't validated your core assumptions, the other skills will ask you to go back and do Stage 1 first. This is intentional.

### 3. Example Prompts (Copy-Paste Ready)

Replace `[your product]` and `[your competitor]` with your actual details.

#### Stage 1: plg-strategy
```
"I need a PLG strategy for my SaaS. We [describe what your product does]."
```
```
"Red-team my business model. I think our moat is [your assumed moat]."
```
```
"Write a strategy memo for my startup. Stage 1 only — validate assumptions first."
```

#### Stage 2: icp-research
```
"Use icp-research to validate my ICP. I think it is [describe your target audience]."
```
```
"Run the Desperate Customer Test on my target audience."
```
```
"Is my ICP too broad? We serve [segment A], [segment B], and [segment C]."
```

#### Stage 3: competitive-intel
```
"Use competitive-intel to find my real moats. Our competitors are [Competitor A] and [Competitor B]."
```
```
"What can [top competitor] copy from us in 30 days? What would take 3 years?"
```
```
"Red-team our positioning. What if [platform] changes API pricing tomorrow?"
```

#### Stage 4: viral-loops
```
"Design a viral loop for my product. Users invite team members to collaborate."
```
```
"Model the K-factor for our referral program. Be realistic, not optimistic."
```
```
"What is our Time-to-Value? How do we get users to their aha moment in under 2 minutes?"
```

#### Stage 5: content-strategy
```
"Use content-strategy to pick my channels. My ICP hangs out on [Platform A] and [Platform B]."
```
```
"Should we do SEO? Our ICP discovers tools on [Platform], not Google."
```
```
"Build a 90-day content bet for one channel only."
```

#### Stage 6: growth-metrics
```
"Define my North Star metric. We are a [type of product] with [pricing model]."
```
```
"Set up 3 growth experiments with kill criteria."
```
```
"What metrics should I kill? I currently track 20 KPIs."
```

### 4. The Staged Workflow (How plg-strategy Gates You)

When you run `plg-strategy`, it will NOT dump a full strategy on you. It works in gates:

**Gate 1: Assumption Validation**
- "You believe [X] is your #1 differentiator. What evidence proves this?"
- "You believe [Y] is your ICP. Have you talked to 10 of them?"
- If you can't answer: It stops here and tells you to run `icp-research` first.

**Gate 2: Red-Team**
- "Here are 3 ways your business could fail..."
- "How do we build strategy that SURVIVES these failures?"

**Gate 3: Strategy Memo (Sacrifice-First)**
- "For every 3 things we recommend, here are 5 we are telling you NOT to do."
- Only after you confirm this gate does it load other skills.

**Gate 4: Tactics (Other Skills Load Here)**
- `icp-research` → `competitive-intel` → `viral-loops` → `content-strategy` → `growth-metrics`
- Each loads only when the previous gate is confirmed.

### 5. Direct Skill Use (Skip the Gates)

If you already validated your assumptions and want to jump to a specific skill, just name it:

```
"Use icp-research directly. I already have 10 customer interviews."
```
```
"Use growth-metrics directly. I need experiment kill criteria."
```

But be warned: the skills will still ask hard questions. They don't skip their own validation rules just because you named them.

### 6. VS Code / Claude Code Specific Tips

**In VS Code Claude Chat:**
- Skills auto-activate based on context. Just describe your problem naturally.
- To force a skill: say `"Use [skill-name] to..."`
- If skills don't load: type `/reload-skills` or restart the chat panel.

**In Claude Code CLI:**
```bash
claude
# Then just talk naturally, or:
/plugins          # See installed skills
/reload-skills    # Refresh after installing new ones
```

**Check if installed:**
```bash
ls ~/.claude/skills/ranjeeetvimal-growth-skills/
```

### 7. Common Mistakes

| Mistake | Why It Fails | Fix |
|---|---|---|
| "Give me all 6 skills at once" | `plg-strategy` is staged. It won't load others until you confirm gates. | Go through the gates one by one. |
| "I want 20 tactics" | These skills are strategy-first. Tactics come after sacrifice. | Accept the "5 things NOT to do" list. |
| "Skip the validation questions" | The skills are designed to catch bad assumptions early. | Answer the hard questions honestly. |
| "I have no data" | Every claim needs evidence or a 30-day validation plan. | Say "I don't know yet — help me validate." |
| "Why can't I see this in Claude web Plugins?" | Claude web uses MCP servers, not SKILL.md files. | Use Claude Code CLI or VS Code instead. |

### 8. Quick Decision Tree

```
What do you need?
├── "I don't have a strategy yet" → plg-strategy (Stage 1)
├── "I have a strategy but need to validate my customer" → icp-research
├── "I know my customer but need moats" → competitive-intel
├── "I need viral growth / onboarding" → viral-loops
├── "I need content / SEO plan" → content-strategy
└── "I need metrics / experiments" → growth-metrics
```

## Philosophy

Every skill in this repo follows the same principles:

1. **Founder-first** — Asks hard questions before giving answers
2. **Bet-driven** — Every recommendation is a quantified bet, not a tactic list
3. **Sacrifice-focused** — Strategy is what you WON'T do, not what you will
4. **Evidence-based** — Every claim has confidence level + validation plan
5. **Human tone** — Short sentences, opinions, "I think," "I worry"

## Contributing

1. Fork the repo
2. Add your skill suite under `Suite-Name/skills/`
3. Follow the [skill template](PLG-Architect/skills/plg-strategy/SKILL.md)
4. Submit a PR

## License

MIT — Ranjeet Vimal
