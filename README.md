# Growth Skills by Ranjeet Vimal

> Open-source agent skills for growth, marketing, and analytics — built by founders, for founders.
> Works across Claude Code, Cursor, Gemini CLI, GitHub Copilot, Antigravity, and any agent on the
> [Agent Skills spec](https://github.com/anthropics/skills).

## Skill suites

Each suite is self-contained — click through for its skills, run order, and copy-paste example prompts.

| Suite | Skills | Status | What it covers |
|---|---|---|---|
| **[PLG-Architect →](PLG-Architect/)** | 7 | ✅ Live | Founder-context intake, PLG strategy, ICP research, competitive moats, viral loops, content strategy, growth metrics |
| **[SEO →](seo-suite/)** | 11 | 🚧 In progress | Gatekeeper (`seo-context`) live; technical + AI-crawler audit, AI-search & entity optimization, keyword & competitor research, strategy, on-page, content, link building, local, programmatic, analytics |
| **[Social Media →](social-media/)** | 1 | 🚧 In progress | Organic, per-platform audience-to-revenue growth. `x-growth` (X / Twitter) live; LinkedIn, Instagram, TikTok, YouTube planned |
| **Paid-Marketing** | 0 | 🚧 Coming soon | Meta Ads, Google Ads, TikTok Ads, creative testing, attribution |
| **Analytics** | 0 | 🚧 Coming soon | Event tracking, cohort analysis, experiment design, data pipelines |

## Quick start

Zero to running a skill in four steps.

**1. Install** — one command. Works in Claude Code, Cursor, Gemini CLI, GitHub Copilot, and Antigravity (installs into `.agents/skills/`, shared across agents):

```bash
npx skills add ranjeeetvimal/growth-skills
```

Just want one suite or skill? Add `--skill`, e.g. `npx skills add ranjeeetvimal/growth-skills --skill seo-context`.

**2. Reload** so the agent discovers the new skills — **this is not a shell command:**

- **Claude Code:** type `/reload-skills` in the session.
- **Cursor / Gemini CLI / Copilot / Antigravity / others:** restart the session.

**3. Invoke by describing your goal** — skills auto-activate by context, so you rarely name them:

```
I need SEO help for my site, acme.com
```

`seo-context` reads your site, reframes "more traffic" into a revenue goal, triages what's likely broken, and writes `.claude/seo-context.md` — then points you to the right specialist.

**4. Follow the hand-off.** Each skill leaves a shared `.claude/*.md` file and recommends the next one, so context flows forward — **Context → Research → Strategy → Execution** — and you never re-enter the same information.

**More one-line examples** (each auto-activates the right skill):

```
Set up my founder context — interview me about my business.   → founder-context
I need a PLG strategy for my SaaS. We help [X] do [Y].        → plg-strategy
Audit my SEO and tell me what's actually broken.             → seo-context
Help me grow on X. My handle is @acme.                        → x-growth
```

> **New here?** Run `founder-context` once. Every suite (PLG, SEO, Social) reads that file, so you explain your business only once.

## Other install methods

<details>
<summary><b>Claude Code native plugin</b> — <code>/plugin marketplace add …</code></summary>

Run these **inside a Claude Code session** (not the shell):

```
/plugin marketplace add ranjeeetvimal/growth-skills
/plugin install plg-architect@growth-skills       # or: seo@growth-skills · social-media@growth-skills
```

Browse interactively with `/plugin`. Later updates: `/plugin marketplace update growth-skills` then `/plugin update <plugin>@growth-skills`.
</details>

<details>
<summary><b>claude.ai web</b> — ZIP upload, or org GitHub sync</summary>

- **ZIP upload (any plan):** ZIP an individual skill folder so `SKILL.md` sits at the ZIP root → [claude.ai](https://claude.ai) → Customize → Skills → **Upload skill**. Requires code execution enabled.
- **Org GitHub sync (Team / Enterprise admins):** Organization settings → Plugins → Add plugin → GitHub, in `owner/repo` format.
  > ⚠️ Web GitHub sync only accepts **private / internal** repos with the [Claude GitHub App](https://support.claude.com/en/articles/10167454) installed. This repo is public — fork it private first, or just use the CLI / `/plugin` methods.
</details>

<details>
<summary><b>Project-local or Git submodule</b> — team sharing</summary>

```bash
# Copy skills into your repo so the whole team gets them on clone
mkdir -p .claude/skills && cp -r /path/to/growth-skills/PLG-Architect/skills/* .claude/skills/

# ...or track this repo as a submodule
git submodule add https://github.com/ranjeeetvimal/growth-skills.git .claude/skills/growth-skills
```
</details>

## Updating & reloading

```bash
npx skills add ranjeeetvimal/growth-skills   # pulls NEW skills and updates existing ones
```

Then reload (`/reload-skills` in Claude Code, or restart your agent).

<details>
<summary>Why <code>add</code> and not <code>update</code>?</summary>

`npx skills update` only refreshes skills you already have — it **skips new skills** added since your last install. Re-running `add` installs what's missing and overwrites the rest. A `Failed to check for deleted skills` warning is harmless.

- Plugin users: `/plugin marketplace update growth-skills` then `/plugin update <plugin>@growth-skills`.
- Verify / remove: `npx skills list` · `npx skills remove --skill <name>`.
</details>

## Philosophy

Every skill follows the same principles:

1. **Founder-first** — hard questions before answers.
2. **Bet-driven** — every recommendation is a quantified bet, not a tactic list.
3. **Sacrifice-focused** — strategy is what you WON'T do, with reasons.
4. **Evidence-typed** — claims labeled Fact / Evidence / Inference / Assumption / Hypothesis, with confidence.
5. **Human tone** — short sentences, real opinions, "I think," "I worry."

## Contributing

1. Fork the repo.
2. Add your skill under `<Suite>/skills/<skill-name>/` (`SKILL.md` + `evals/evals.json`).
3. Follow an existing skill as the template — e.g. [`seo-context`](seo-suite/skills/seo-context/SKILL.md).
4. Run `python3 scripts/validate_skills.py` (CI runs it too), then open a PR.

Full guide in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — Ranjeet Vimal. Changelog: the [commit history](https://github.com/ranjeeetvimal/growth-skills/commits/main).
