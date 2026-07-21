# SEO

An evidence-based, sacrifice-first SEO skill suite (11 skills) — parallel to PLG-Architect. Takes a domain to a full SEO strategy and the plays to execute it, built for the 2026 landscape (AI search + entities, not just keywords). Overlapping concerns are merged, not split.

Install from the [repo root README](../README.md#quick-install).

## Run them in this order

**Context -> Audit -> Research -> Strategy -> Execution -> Measurement.** Each skill reads `.claude/seo-context.md` (and `.claude/seo-snapshot.md` once written), so context flows forward.


**Context**
1. `seo-context`

**Audit**
2. `technical-seo-audit`

**Research**
3. `ai-search-optimization`
4. `keyword-research`

**Strategy**
5. `seo-strategy`

**Execution — On-page**
6. `on-page-seo`
7. `content-strategy-seo`

**Execution — Off-page**
8. `link-building`
9. `local-seo`

**Execution — Advanced**
10. `programmatic-seo`

**Measurement**
11. `seo-analytics`

## Context: standalone, but inherits when it can
The suite is independent — it works with only `.claude/seo-context.md`. But `seo-context` reads `.claude/founder-context.md` if PLG-Architect already wrote it, so business basics aren't re-entered. No hard dependency between the suites; the coupling is just the shared `.claude/` file.

## Principles
Founder-first · bet-driven · sacrifice-focused · evidence-typed · elaborate + honest.
