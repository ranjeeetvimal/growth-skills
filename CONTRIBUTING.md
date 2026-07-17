# Contributing to Growth Skills

Thanks for wanting to improve this. Whether it's fixing a skill, adding one, or
starting a new suite — here's how.

## Ground rules (the house style)

Every skill in this repo follows the same principles. New or edited skills should too:

1. **Founder-first** — ask the hard questions before giving answers.
2. **Bet-driven** — every recommendation is a quantified bet, not a tactic list.
3. **Sacrifice-focused** — say what NOT to do, with reasons.
4. **Evidence-typed** — label claims Fact / Evidence / Inference / Assumption / Hypothesis, with a confidence level.
5. **Elaborate + honest** — worked-out plays, not fragments; no cheerleading.
6. **Generic** — no real company names or one-off business specifics baked into a skill. Use "a competitor," not a brand.

## Repo layout

```
<Suite>/
  README.md
  skills/
    <skill-name>/
      SKILL.md                 # required — frontmatter + instructions
      references/*.md          # optional — deep detail, loaded on demand
      evals/evals.json         # optional — trigger tests
.claude-plugin/marketplace.json  # repo-level plugin marketplace
<Suite>/.claude-plugin/plugin.json  # per-suite plugin manifest
```

## Adding or editing a skill

1. **Folder = name.** Put it at `<Suite>/skills/<skill-name>/SKILL.md`, and make the
   frontmatter `name:` **exactly match the folder**.
2. **Frontmatter.** Required: `name` and `description`. The `description` is what the
   agent scans to decide when to load the skill — front-load the *what* and the *when*
   (the verbs/triggers a user would type). Keep it under ~1,000 characters.
   ```yaml
   ---
   name: my-skill
   description: >
     One-liner on what it does and WHEN to use it (the triggers).
   license: MIT
   metadata:
     author: Your Name
     version: "1.0.0"
     category: <category>
     related-skills: skill-a, skill-b
   ---
   ```
3. **Keep SKILL.md lean.** Push heavy detail into `references/*.md` and point to it from
   the body ("read `references/foo.md` when you need X") — it loads on demand.
4. **Add evals** in `evals/evals.json` — a few inputs with the `expected_skill` they
   should (or should not) trigger. Include negative cases.
5. **Register it.** If it's a new skill in an existing plugin, it's picked up from the
   suite's `skills/` folder automatically. A new *suite* needs its own
   `.claude-plugin/plugin.json` and a row in the root `.claude-plugin/marketplace.json`.

## Before you open a PR

Run the validator (stdlib only, no install):

```bash
python3 scripts/validate_skills.py
```

It checks that all JSON parses, every `SKILL.md` has valid frontmatter, each skill's
`name` matches its folder, and every referenced `references/*.md` exists. CI runs the
same check on every PR.

## PR process

1. Fork, branch, make the change.
2. Run the validator; make sure it passes.
3. Open a PR describing what the skill does and why. Screenshots or an example run help.

## License

By contributing, you agree your contribution is licensed under the repo's [MIT License](LICENSE).
