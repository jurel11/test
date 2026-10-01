# B. Master synthesis

This part gathers, in one place, everything the research established: the context and method, the key numbers, the myths and contradictions, and every recommendation. It is written to be read straight through. Part C has the ten styles in full; parts D to G are the underlying reports and data. When a statement here needs more detail, the "Where" column or the closing reference in each section names the chapter.

**Evidence grades used everywhere:** **[A]** official documentation, peer-reviewed study, or a large dataset; **[B]** first-hand data from a creator or company, a correlational dataset, or a measurement by one of our agents; **[C]** opinion, vendor blog, or inference. **UNVERIFIED** means the agent could not confirm it. Rounded view counts are as listed by YouTube on 2026-09-30.

## B1. Context, constraints and method

### B1.1 The question

The channel owner runs a new YouTube channel, **Stress Riser** (documentary-style stories of engineering disasters and failed inventions, told as a chain of small, reasonable decisions; English voiceover; hand-drawn stick-figure animation; viewers 18–50 in the US, UK, Canada and Australia, mostly on a phone). The request was to launch as many agents as needed, research in detail and with precision, and deliver **10 different thumbnail styles and approaches that suit the videos, would work well and have a high click-through rate**, with as much time as needed. A later request (this file) was to put **all the data, all the recommendations and everything learned in one very extensive file**.

### B1.2 What in the brief shaped the thumbnails

| Brief rule | What it means for thumbnails |
|---|---|
| Every title is a question, no colon, no case name first, no statement | Titles are fixed; the thumbnail must complement a question, not repeat it |
| Audience arrives from the home feed on "a question-title and a thumbnail that made them curious" | Thumbnails matter most on browse; viewers decide on a phone in about a second |
| Never clickbait the video does not deliver | The thumbnail may show only what the video shows by second 15; no invented drama |
| Outcome first: what broke and the human stakes in plain numbers within 10–15 seconds | The outcome image can be shown honestly in the thumbnail |
| Failure is the villain, not people; never mock the dead; no graphic injury | No victims, no bodies, no faces in agony; culprits are objects and systems |
| Art: clean black outlines, soft flat colors, whole richly illustrated places with near/middle/far layers; text cards on plain flat paper | Lit scenes; no empty flat backgrounds except plain paper cards |
| Palette: #1a1a1a, #ffffff, #f3ead8, #bfe2ea, #8fbf5a, #4f7d3a, #9a6b43, #d2b48c, #e6b23a, #d94a38 | Ten colors only; only three lightness tiers; many pairs fail |
| Characters: stick figures per a character sheet; limbs are single black lines; dot eyes; one prop; no smile unless asked | Figures need light surfaces; close-ups stay thin-limbed; no smiling shock faces |
| Must never appear in images: text, letters, numbers, arrows, dashed lines, motion lines, diagram symbols, collage, multiple panels, empty flat background | Words are a separate overlay layer; no arrows, no split panels, no black voids |
| Forbidden topics: ongoing legal cases, disasters less than 2 years old, terrorism, medical or financial advice, politics beyond regulatory facts | Story filter; as of 2026-10-01 nothing after about 2024-10-01 |
| Description must say AI-assisted narration and animation; sources listed | Disclosure line is already consistent with YouTube's rules |
| Shorts 45–60 s; outcome in the first 3 seconds; Shorts never ask | A Short's "thumbnail" is frame 0 to 1 s |

### B1.3 Observations about the brief itself

These are points where the brief is silent, ambiguous or internally inconsistent. They were handled by explicit assumptions and are listed so the owner can confirm them.

1. **No character sheet exists.** The brief says every person is a stick figure "exactly as on their character sheet", but no sheet is given. Each story needs one (front view, three expressions, prop). The closest real reference, Ink Explainer, draws circle eyes with lids; the brief specifies dot eyes.
2. **Text in images versus text on thumbnails.** The brief bans text and numbers in images, yet its own pacing rule uses "a text card, a label" on screen, and about 70% of niche thumbnails carry words. Assumption: thumbnail words are a **separate overlay layer** added in a design tool; the generated image never contains letters.
3. **Plain paper.** The brief bans an "empty flat background" but allows beat drawings and text cards on plain flat paper. Assumption: one style (Exhibit A) is a plain paper card with an ink frame.
4. **Spelling.** The rule says American spelling ("meters"), but several examples inside the brief use "metres" and "humour". Assumption: output uses American spelling; the examples show only the shape.
5. **The "two years old" rule moves with the date.** On 2026-10-01 a disaster from before about 2024-10-01 qualifies; the cutoff must be recomputed on each publication date.
6. **"Every title is a question"** is firm, but the evidence on questions in headlines is mixed (see B2.3). The fix is to make questions concrete and let the thumbnail carry the specific stakes.
7. **Forbidden-topic overlap with the best-known stories.** Several famous cases fail the filter today (Morandi Bridge: first-instance verdict 16 July 2026, appeal announced; Boeing 737 MAX: civil trials continue; Grenfell: charging decisions pending, trials 2029 or later). Lac-Mégantic is borderline.
8. **The brief's own examples all point to Vajont** (1,900 people, 270 million cubic metres, Edoardo Semenza, a dam that never broke). It is a natural first story, but the brief says of its own examples that each "shows the shape, never copy it".

### B1.4 Method

Eight research agents ran in parallel, each with one slice and the same rules: rigor and precision, no invented statistics, every quantitative claim with a URL, date and what was measured, an evidence grade on every finding, myths called out, and a final report of at most about 1,500 words plus saved notes. Agents could search the web, fetch pages with a command-line tool, download real YouTube thumbnails and look at them. The exact instructions each agent received are in Appendix G2.

| Agent (slice) | Tool calls | Duration | Est. cost | Main outputs |
|---|---|---|---|---|
| Platform mechanics, specs, policies, testing | 113 | about 12 min | $3.44 | Official specs, feed sizes, impressions definition, Test & Compare mechanics, policies, AI disclosure, Shorts covers |
| Empirical CTR evidence | 135 | about 14 min | $3.27 | 1of10, vidIQ, Netflix, MrBeast, academic papers, creator cases, rule verdict table, myths |
| Psychology and perception | 80 | about 14 min | $1.97 | Five headline findings, 15 design principles, myths, caveats |
| Niche audit (disaster, documentary) | 49 | about 16 min | $1.61 | 58 channel pages, 405 thumbnails, about 105 viewed, 13 formulas, brightness statistics |
| Cartoon and stick-figure audit | 115 | about 14 min | $2.67 | 52 channels, 462 rows, about 300 viewed, 12 formulas, pose vocabulary, Ink Explainer recipe |
| Design system, color math, workflow | 100 | about 25 min | $2.45 | Palette math (45 pairs), feed sizes, text spec, fonts, workflow, preview tool |
| Story-to-visual (fact-checked) | 57 | about 16 min | $2.23 | 12 stories with facts, filter results, thumbnail moments, ranking |
| Packaging, testing, Shorts | 81 | about 15 min | $1.68 | Pairing patterns, testing arithmetic, cold start, identity vs variety, Shorts |
| **Total, eight agents** | **730** | | **about $19.3** | |
| Reviewer 1 (facts and claims) | 32 | about 10 min | $1.51 | 17 live spot-checks, 6 must-fix and 16 should-fix findings |
| Reviewer 2 (brief and design) | 29 | about 9 min | $0.72 | Palette audit, brief compliance, distinctness, 7 must-fix findings |
| **Subtotal, ten agents** | | | **about $21.6** | |
| Reviewer 3 (check of the master synthesis) | 26 | about 19 min | $1.82 | All 141 table rows of B2 checked against the reports and data; 5 must-fix and about 23 should-fix corrections |
| **Total, eleven agents** | | | **about $23.4** | |

Costs are estimates from token counts at the published Sonnet 5.5 prices ($2 per million input tokens, $10 output, $0.20 cache reads, $2.50 cache writes), with an error of about ±25%. A second computation by a reviewer with the same formula gave $17.4 for the eight research agents and $19.5 for ten (the per-agent figures above run 7–16% higher), so read the agent costs as ranges: $17–19 for eight, $19.5–21.6 for ten, $21–23 for eleven.

**Effort cap.** After the first measurement showed the agents were spending about $1.5 per minute with no limit, each was asked to wrap up within about 20 further tool calls. Nothing already saved was lost. The owner later raised the total ceiling to $60–70; planning kept the estimate under $55 so that even a +25% error stays below $70.

**Review cycle.** The first complete draft (report, ten mockups, lookbook) was reviewed by two independent agents who had no stake in it. Their reports are in Part E; the status of every finding is in B6. The result: the diptych was replaced, black backgrounds removed, several depictions redrawn to match the sources, and many claims corrected or hedged. The corrected version is Part C. When this master file was compiled, a third independent agent checked the synthesis in Part B against the reports and the data; its report is E3 and all its corrections are applied (B6.6).

### B1.5 Access limits (what could not be read)

- YouTube watch pages and transcripts were bot-gated: the Veritasium, Kurzgesagt, Colin and Samir and Jon Youshaei talks were not read; their points are secondary or absent.
- vidIQ's study page, ScienceDirect, Springer, ACM and Medium were blocked: those findings rest on abstracts or secondary summaries.
- Rene Ritchie's and Todd Beaupré's statements come through Search Engine Journal and ppc.land, not the original videos. The MrBeast production memo is unauthenticated.
- The official Comet inquiry report (CAP 127) and the Cullen Report on Piper Alpha were not opened; the Quebec Royal Commission report was not read; the Vasa Museum page returned 404.
- No source gives official pixel sizes for native phone apps or TV, or an official safe-zone map.
- The Team YouTube thread on the mobile-feed crop experiment is rendered by script and could not be re-opened by the reviewer.

*For detail see Appendix G (raw notes) and Part D (final reports).*
