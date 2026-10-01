# Stress Riser: knowledge base for thumbnails and packaging (AI edition)

- Document type: one-file knowledge base for an AI assistant. Plain Markdown. No images, no HTML, no scripts. Layered from the most important content to the least important.
- Subject: the YouTube channel "Stress Riser" (documentary-style stories of engineering disasters and failed inventions; English voiceover; hand-drawn stick-figure animation). The research covers thumbnails and packaging (ten thumbnail styles, title and thumbnail pairing, A/B testing, Shorts frames) and holds a fact base for twelve candidate stories.
- Research date: 2026-09-30. Compiled: 2026-10-01. Platform rules, view counts and legal-case status change over time (see 0.5).
- Origin: eight research agents (platform rules, CTR evidence, psychology, niche audit, cartoon audit, design system, story facts, packaging) and three independent reviewers. All reviewer corrections are applied. A larger human-readable edition (HTML with images, raw notes and indexes) exists in the repository; this file is the AI-readable edition of the same research.
- Language: the channel owner writes in Slovenian, so answer the owner in Slovenian. Everything that goes into the channel itself (voiceover, titles, descriptions, thumbnail words, image prompts) is English. This file is English.

## 0. READ FIRST

### 0.1 Precedence (when sources disagree)

1. The channel brief (R1, verbatim) wins over everything else.
2. Parts A, B, C and F are the corrected, authoritative layer (three independent reviews applied).
3. Part D holds the eight research reports verbatim. They were written before the reviews. Where a report disagrees with Parts A, B, C or F, Parts A, B, C and F win. Known disagreements between reports are listed in B3.2.
4. Your own background knowledge ranks last. Do not add facts about disasters, YouTube policy or study results that are not in this file; say "not in the research, verify" instead. The channel's own rule is "nothing invented, ever".

### 0.2 Conventions

- Evidence grades: [A] official documentation, peer-reviewed study or large dataset; [B] first-hand creator or company data, a correlational dataset, or a measurement by one of the research agents; [C] opinion, vendor blog or inference. UNVERIFIED means the agent could not confirm it. A statement in Parts C or D without its own grade takes the grade of its row or section.
- "Hypothesis" means an untested idea. All ten thumbnail styles are hypotheses.
- In Parts C and D the author writes "I" (the research lead, an AI assistant) and "you" (the channel owner). "Your brief" is the channel brief in R1.
- IDs: A1 to A6 (core card); B1 to B6 (synthesis chapters, sections such as B2.1); C1 to C12 (sections of the styles report); D1 to D8 (research reports); F1 to F3 (data); R1 to R3 (reference: the channel brief, file map, glossary). "Style N" (N = 1 to 10) is a thumbnail style in C5.
- Paths in backticks (for example `research/platform.md`, `thumbnails/01-tiny-under-the-giant.png`) are files in the repository folder stress-riser/. They are not included here. The ten mockup images are not included; each style's "Example" line describes its picture in words.
- Pixel sizes refer to a 1280x720 master unless stated. Money is in US dollars. Dates are YYYY-MM-DD. View counts are as listed by YouTube on 2026-09-30.

### 0.3 Map of this file

Format: line number, heading, size in words. Lines are counted from the first line of the file; use them to jump to a section.

{{MAP}}

### 0.4 Not included in this edition

All of these exist in the repository (folder stress-riser/) and in the full HTML dossier. References to them in the text (for example "G8", "E1", "F4", "H1") point there.

| ID | What it is | Where |
|---|---|---|
| E1 to E3 | the three reviewers' reports, verbatim | `master/reports/review-factcheck.md`, `review-design.md`, `review-synthesis.md` |
| F4, F5 | video indexes (405 niche rows, 462 cartoon rows: video ID, title, channel, views, group) | `data/niche-video-index.csv`, `data/cartoon-video-index.csv` |
| F6 | phone-size QA sheet and mockup measurements | `thumbnails/qa-phone-sizes.png` |
| G1 to G10 | raw working notes of the eight agents (G3 to G10) and the exact prompts the agents received (G2) | `research/*.md`, `master/G2-research-briefs.md` |
| H1 (HTML dossier) | consolidated list of all 193 cited sources | `STRESS-RISER-MASTER.html` (each report in Part D also ends with its own sources) |
| images | ten mockups, art-only layers, editable SVG sources, gallery | `thumbnails/`, `thumbnail-lookbook.html` |
| Slovenian summary | summary for the owner | `master/A-summary-sl.md` (replaced here by the English core card A) |

### 0.5 Freshness: what to re-check

- The "two years old" rule: a disaster must be at least two years old on the publication date. On 2026-10-01 anything after about 2024-10-01 is excluded; recompute on the day.
- Platform specs, Test & Compare features, Shorts covers and the AI-label rules changed several times in 2026. Re-read the YouTube Help pages each quarter.
- Legal status of the candidate stories is not fully verified (B2.7). Check again before choosing a story.
- View counts and subscriber counts are as of 2026-09-30.

### 0.6 Which sections to read for which task

| Task | Read |
|---|---|
| Make thumbnail concepts for a new video | A2 to A6, C4, C5, C6, C8, B4.2, B5.1 |
| Write an image-generation prompt | C5 (master prompt block and the style's prompt), B4.3, B4.5 |
| Review a finished thumbnail | A3, B4.3, B4.4, B4.5 (QA list), B4.9, B4.11 |
| Choose a title and thumbnail pair | B4.7, C7 |
| Plan or read an A/B test | B4.6, B2.1, B2.6 (sample sizes), B5.2 |
| Check or choose a story | B2.7, C8, B3.1 (story myths), B4.10, D7 |
| Shorts | B4.8, C10 |
| Answer "is X true about thumbnails?" | B3.1, B3.2, B2.2 to B2.4, D2, D3 |
| Technical specs and policy | B2.1, C2, D1 |
| Colors, fonts, text overlay | B2.5, B4.3, B4.4, D6, F1 to F3 |
