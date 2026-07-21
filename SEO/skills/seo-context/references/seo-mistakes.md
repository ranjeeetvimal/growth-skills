# Common SEO Mistakes — Diagnostic Lens

A triage checklist for `seo-context`. Use it to flag which mistakes *likely* apply
from a light intake + a glance at the site, and route to the skill that investigates
each. Flag them as **hypotheses to confirm**, never as a verdict — the deep, evidence-based
work happens in the specialist skills.

**Evidence note (read this):** the thresholds below (word counts, click depth, link counts)
are common heuristics from SEO practitioner content, not laws. Treat them as `[Hypothesis]`
and verify against **primary sources** — Google Search Central (crawling/indexing/guidelines),
web.dev (Core Web Vitals: LCP <2.5s, INP <200ms, CLS <0.1), Schema.org (structured data),
and the AI crawlers' own docs (GPTBot/ClaudeBot/PerplexityBot). Never state a number as fact.

## The mistakes → what to check → which skill fixes it

| # | Mistake | Quick tell (confirm in the skill) | Fixed by |
|---|---|---|---|
| 1 | **Wrong keyword targeting** | Chasing broad head terms; ignoring long-tail intent | `keyword-research` |
| 2 | **Keyword cannibalization** | Several pages target the same term, splitting rankings | `on-page-seo` + `technical-seo-audit` |
| 3 | **Wrong search intent** | Content format doesn't match what ranks (blog vs product vs listicle) | `content-strategy-seo` |
| 4 | **Poor content quality** | Thin pages, no E-E-A-T signals, stale/outdated posts | `content-strategy-seo` |
| 5 | **Missing/duplicate metadata** | No/duplicate title tags or meta descriptions | `on-page-seo` |
| 6 | **Slow / poor Core Web Vitals / not mobile** | Slow mobile load, failing LCP/INP/CLS, unresponsive | `technical-seo-audit` |
| 7 | **Unoptimized images** | No alt text, oversized files, no next-gen formats | `on-page-seo` |
| 8 | **Weak internal linking / architecture** | Orphan pages, deep click depth, thin internal links | `technical-seo-audit` (architecture) + `on-page-seo` |
| 9 | **Poor / toxic backlinks** | Bought links, link networks, over-optimized anchors | `link-building` |
| 10 | **Crawl / indexability debt** | Blocked in robots.txt, noindex mistakes, Search Console coverage errors | `technical-seo-audit` |
| 11 | **No conversion focus** | Traffic with ~zero revenue; SEO without CRO | `content-strategy-seo` + `seo-analytics` |
| 12 | **Treating SEO as one-time** | No refresh cycle, no monthly process, no monitoring | `seo-strategy` + `seo-analytics` |
| 13 | **Invisible to AI answer engines (2026)** | Not cited in AI Overviews/ChatGPT/Perplexity; JS-rendered content AI crawlers can't see; no entity/schema signals | `ai-search-optimization` |

Mistake 13 is the one the classic lists miss — it's the 2026-specific failure and often
the highest-leverage opening, because most competitors haven't fixed it yet. But frame it right:
AI visibility is **not a separate track from ranking**. Ranking well in organic is the reliable
path to AI citation — one vendor analysis found ~97% of AI Overviews cite a source from the top
20 organic results ([Evidence]: seoClarity, vendor — verify). So `ai-search-optimization` is
"rank well first, then structure content to be citable," not a parallel game with its own rules.

## How to use it in the intake
- Don't run all 13 as a heavy audit — that duplicates the specialist skills. Pick the 2-4
  most likely from the intake signals (e.g. client-side rendering → flag 6, 8, 13).
- Record them in `seo-context.md` under "Mistakes triage" as `[likely-critical/high] mistake -> skill`.
- Route to the single highest-leverage one as the recommended next skill.

## Severity, honestly
Rank flagged mistakes Critical / High / Medium / Low by **revenue impact under the founder's
constraints**, not by how bad they look. A perfect technical site that converts nothing has a
bigger problem (11) than a fast site missing a few alt tags (7).

## Never recommend — dead & black-hat tactics
If any of these turn up in the intake, flag them as a mistake to *undo*, not a lever to pull.
They range from long-dead to actively penalized:
- **Keyword-density stuffing** — 2026 ranking is semantic (topical coverage + entity relationships), not a density target.
- **Meta keywords tag** — ignored by Google for over a decade; a tell of outdated advice.
- **Exact-match domains** as a ranking play — no longer a shortcut.
- **Private blog networks (PBNs) / bought links / link exchanges** — link-scheme violations → `link-building` fixes the profile.
- **Article spinning / AI content spam** — fails helpful-content; ship original, first-hand, useful content instead.
- **Cloaking, hidden/white text, or doorway pages** — showing crawlers something users don't see is a policy violation. This includes near-duplicate **"city pages"** (same body, swapped location) — real local coverage is `local-seo` / `programmatic-seo` done with genuinely distinct content.
- **Outdated link & indexing chores** — mass directory submissions, RSS/article-directory blasts, reciprocal-link schemes, keyword-in-every-heading. Dead for years; still parroted by stale guides.
- **Review & reputation manipulation** — fake reviews, review gating (only soliciting happy customers), or negative SEO against competitors. Against platform policy (often against the law) → clean `local-seo` instead.

## Never fabricate — the SEO data traps
The three numbers it's most tempting to invent, and never should:
- **Search volume, keyword difficulty (KD), CPC, and current rankings.** Don't make these up. Either
  pull real data (a connected SEO API, Search Console, a live SERP check) or say plainly you don't have
  it and give a framework/relative estimate instead. A confident fake number is worse than an honest gap.
- **No guarantees.** Never promise a specific rank (#1), a traffic figure, or a date. SEO has no
  guarantees — commit to a *process* and ranges, not outcomes. Add that results take weeks-to-months to show.
