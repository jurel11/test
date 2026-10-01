# Stress Riser: knowledge base for thumbnails and packaging (AI edition)

- Document type: one-file knowledge base for an AI assistant. Plain Markdown. No images, no HTML, no scripts. Layered from the most important content to the least important.
- Subject: the YouTube channel "Stress Riser" (documentary-style stories of engineering disasters and failed inventions; English voiceover; hand-drawn stick-figure animation). The research covers thumbnails and packaging (ten thumbnail styles, title and thumbnail pairing, A/B testing, Shorts frames) and holds a fact base for twelve candidate stories.
- Research date: 2026-09-30. Compiled: 2026-10-01. Platform rules, view counts and legal-case status change over time (see 0.5).
- Origin: eight research agents (platform rules, CTR evidence, psychology, niche audit, cartoon audit, design system, story facts, packaging) and three independent reviewers. All reviewer corrections are applied. A larger human-readable edition (HTML with images, raw notes and indexes) exists in the repository; this file is the AI-readable edition of the same research.
- Language: the channel owner writes in Slovenian, so answer the owner in Slovenian. Everything that goes into the channel itself (voiceover, titles, descriptions, thumbnail words, image prompts) is English. This file is English.

## 0. READ FIRST

### 0.1 Precedence (when sources disagree)

1. The channel brief (H2, verbatim) wins over everything else.
2. Parts A, B, C and F are the corrected, authoritative layer (three independent reviews applied).
3. Part D holds the eight research reports verbatim. They were written before the reviews. Where a report disagrees with Parts A, B, C or F, Parts A, B, C and F win. Known disagreements between reports are listed in B3.2.
4. Your own background knowledge ranks last. Do not add facts about disasters, YouTube policy or study results that are not in this file; say "not in the research, verify" instead. The channel's own rule is "nothing invented, ever".

### 0.2 Conventions

- Evidence grades: [A] official documentation, peer-reviewed study or large dataset; [B] first-hand creator or company data, a correlational dataset, or a measurement by one of the research agents; [C] opinion, vendor blog or inference. UNVERIFIED means the agent could not confirm it. A statement in Parts C or D without its own grade takes the grade of its row or section.
- "Hypothesis" means an untested idea. All ten thumbnail styles are hypotheses.
- In Parts C and D the author writes "I" (the research lead, an AI assistant) and "you" (the channel owner). "Your brief" is the channel brief in H2.
- IDs: A1 to A6 (core card); B1 to B6 (synthesis chapters, sections such as B2.1); C1 to C12 (sections of the styles report); D1 to D8 (research reports); F1 to F3 (data); H2 to H4 (appendices). "Style N" (N = 1 to 10) is a thumbnail style in C5.
- Paths in backticks (for example `research/platform.md`, `thumbnails/01-tiny-under-the-giant.png`) are files in the repository folder stress-riser/. They are not included here. The ten mockup images are not included; each style's "Example" line describes its picture in words.
- Pixel sizes refer to a 1280x720 master unless stated. Money is in US dollars. Dates are YYYY-MM-DD. View counts are as listed by YouTube on 2026-09-30.

### 0.3 Map of this file

Format: line number, heading, size in words. Lines are counted from the first line of the file; use them to jump to a section.

```text
L115   ## A. Core card: read this even if you read nothing else (2,711 words)
L117     ### A1. What this is (145 words)
L123     ### A2. Fifteen findings that matter (783 words)
L141     ### A3. Hard rules for every thumbnail (checklist) (425 words)
L157     ### A4. The ten styles at a glance (425 words)
L176     ### A5. Next steps and open decisions (276 words)
L189     ### A6. Task recipes (645 words)
L214   ## H. Reference: the channel brief (verbatim), file map, glossary (H2 to H4) (3,317 words)
L218     ### H2. The channel brief (verbatim; it overrides everything else) (2,449 words)
L319     ### H3. Repository file map (316 words)
L345     ### H4. Glossary (528 words)
L379   ## C. The ten thumbnail styles: house system, evidence, testing playbook, fact registry (C1 to C12) (8,223 words)
L386     ### C1. The short version (369 words)
L395     ### C2. Hard constraints (every thumbnail must pass) (475 words)
L407     ### C3. What the research found (condensed) (549 words)
L429     ### C4. The house system: what never changes and what varies (631 words)
L452     ### C5. The ten styles (3,514 words)
L562     ### C6. Comparison and phone-size results (513 words)
L596     ### C7. Testing playbook (539 words)
L607     ### C8. Registry of facts used in the examples (706 words)
L628     ### C9. Decisions I need from you (198 words)
L635     ### C10. Shorts (156 words)
L642     ### C11. Caveats (209 words)
L651     ### C12. Files (94 words)
L658   ## B. Synthesis: key numbers, myths, contradictions, recommendations, roadmap, risks (14,630 words)
L664     ### B1. Context, constraints and method (1,660 words)
L738     ### B2. Key numbers and facts, in one place (5,494 words)
L940     ### B3. Myths, unsupported claims and contradictions (1,739 words)
L1032    ### B4. All recommendations, consolidated (3,554 words)
L1191    ### B5. Roadmap, decisions, risks and gaps (1,634 words)
L1289    ### B6. Review status and spend (compact) (399 words)
L1299  ## D. The eight research reports (verbatim source layer) (18,153 words)
L1303    ### D1. Platform mechanics, specs, policies and testing (2,614 words)
L1473    ### D2. Empirical evidence on what gets thumbnails clicked (2,246 words)
L1632    ### D3. Psychology and visual perception of clicking (1,837 words)
L1726    ### D4. Audit of the engineering-disaster and documentary niche (2,075 words)
L1845    ### D5. Audit of cartoon and stick-figure explainer channels (2,004 words)
L1997    ### D6. Design system, color math and production workflow (2,544 words)
L2185    ### D7. From story to thumbnail moment (fact-checked) (2,210 words)
L2338    ### D8. Packaging, title-thumbnail pairing, testing and Shorts (2,559 words)
L2484  ## F. Data tables: palette math, fonts, legibility experiments (F1 to F3) (3,042 words)
L2488    ### F1. Palette pairs and single-color values (1,598 words)
L2557    ### F2. Font measurements (624 words)
L2592    ### F3. Legibility, saliency and color-blindness experiments (789 words)
L2718  ## Z. Final reminders (248 words)
```

### 0.4 Not included in this edition

All of these exist in the repository (folder stress-riser/) and in the full HTML dossier. References to them in the text (for example "G8", "E1", "F4") point there.

| ID | What it is | Where |
|---|---|---|
| E1 to E3 | the three reviewers' reports, verbatim | `master/reports/review-factcheck.md`, `review-design.md`, `review-synthesis.md` |
| F4, F5 | video indexes (405 niche rows, 462 cartoon rows: video ID, title, channel, views, group) | `data/niche-video-index.csv`, `data/cartoon-video-index.csv` |
| F6 | phone-size QA sheet and mockup measurements | `thumbnails/qa-phone-sizes.png` |
| G1 to G10 | raw working notes of the eight agents (G3 to G10) and the exact prompts the agents received (G2) | `research/*.md`, `master/G2-research-briefs.md` |
| H1 | consolidated list of all 193 cited sources | `STRESS-RISER-MASTER.html` (each report in Part D also ends with its own sources) |
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

## A. Core card: read this even if you read nothing else

### A1. What this is

The channel owner asked for 10 different thumbnail styles and approaches that suit the channel's videos, work well and have a high click-through rate (CTR). The answer is ten distinct, brief-compliant concepts (Part C, section C5) built on one house system (C4), plus a test program (C7, B4.6) to find out which ones work, because no public evidence says in advance which thumbnail features raise CTR on YouTube.

The channel (from the brief, H2): documentary-style stories of engineering disasters and failed inventions, told as a chain of small, reasonable decisions; English voiceover; hand-drawn stick-figure animation. Audience: curious adults 18 to 50 in the US, UK, Canada and Australia, watching on phones and arriving from the home feed on a question title and a thumbnail. Titles are always questions. Long videos run 8 to 12 minutes, Shorts 45 to 60 seconds.

### A2. Fifteen findings that matter

1. **No controlled evidence.** No controlled study of what raises YouTube thumbnail CTR was found. The evidence is correlational (samples of videos that already did well), lab attention studies, headline experiments, company data (Netflix) and creator anecdotes. YouTube's own A/B tool optimizes watch-time share, not CTR. So all ten styles are hypotheses to be tested. (C1, B4.1)
2. **Testing mechanics [A].** Test & Compare: up to 3 variants; titles, thumbnails or both; long-form only; desktop Studio; ends at significance or after up to 2 weeks; outcomes Winner, Performed Same or Inconclusive; judged by watch-time share. If any variant is under 1280x720, all are downscaled to 480p. Upload the preferred variant first. (B2.1)
3. **Only big differences are detectable.** Per variant, at 80% power and 5% significance, CTR only: 4% to 8% needs about 550 impressions; 4% to 6% about 1,860; 4% to 5% about 6,700. Three variants triple the total. So test radically different concepts, never font or color tweaks. (B2.6, B4.6)
4. **The niche gap (an untested advantage).** Engineering-disaster thumbnails are mostly photographic, dark and text-heavy: mean brightness 0.43 over 268 thumbnails (cartoon channels 0.52). Almost nobody uses flat hand-drawn illustration and almost nobody shows the moment before the failure. Whether standing out raises CTR is unknown. (B2.4, C1)
5. **Best-supported principles.** One dominant subject; at most three people (Netflix win rates fall above three); a readable emotion; few words or none; a promise the video pays off by second 15; a medium, not maximal, curiosity gap. (B2.3, B4.1)
6. **Contested or unsupported.** "Faces always win" (contested: face and no face perform about the same in the largest dataset); shocked open-mouth faces (contested); "3 words is optimal" (convention, no study); "red wins" (not supported: cyan, green and yellow/orange are ahead in the 1of10 data); "bright thumbnails win" (hypothesis: our audits found no within-channel separation); rule of thirds and F-pattern (no CTR evidence). (B3.1)
7. **The Ink Explainer format.** The brief's model channel uses a full illustrated scene, 1 to 3 stick figures and 2 to 3 all-caps words that tease the answer without repeating the title. Clone channels with the same template get very different view counts, so the idea carries the result, not the template. (B2.4, Style 7)
8. **Titles.** The brief requires question titles. Evidence on question headlines is mixed (written headlines, not YouTube): keep them, but make them concrete (a named object or a number). The thumbnail must add a fact the title lacks and must not repeat the title's first ~40 characters; the key idea belongs in the first ~40 characters. (B4.1, B4.7)
9. **Specs [A].** 16:9; recommended 3840x2160 (the old "1280x720, 2 MB" rule is out of date); minimum width 640 px; 2 MB from a phone, 50 MB from desktop; YouTube serves 1280x720; the duration badge sits bottom-right; an experiment may crop thumbnails on mobile Home, so keep key content central. (B2.1, C2)
10. **Policy [A].** A misleading thumbnail risks a strike; no blood, gore or shock imagery; advertiser-friendly rules apply to thumbnails (disaster with visible harm gets limited ads); clear animation is treated differently from live action; AI disclosure is not needed for clearly non-realistic animation; unoriginal templated AI content risks monetization. (B2.1, B4.9, C2)
11. **Color system.** The ten-color palette has only three lightness tiers; 21 color pairs differ by less than 25 lightness units (list in B4.3) and need the ink outline. Text: Lilita One, white fill, ink outline at 12% of cap height, 1 to 3 caps words, main-word cap height at least 90 px on the 1280x720 master. (B2.5, B4.3, B4.4)
12. **Own conventions (untested).** Red #d94a38 always means "the thing that went wrong"; scenes are lit with no dark backgrounds; figures stand on light surfaces, because single black limbs vanish on black. (B4.3)
13. **Story facts.** Twelve candidate stories have a fact base (B2.7). All pass the age filter; legal status is not fully verified. Morandi Bridge, Boeing 737 MAX and Grenfell fail the legal filter. Myths to avoid include Comet's "square windows", Tacoma "resonance" as settled and "a light wind", Vasa "the king added a deck", Quebec "Iron Rings from the wreckage", and blaming individuals at Piper Alpha (full list in B3.1).
14. **Casualty numbers.** Never use a death toll as a thumbnail hook (recommendation; the brief says to state casualties factually and move on). Use non-casualty numbers such as mph, tons or a time of day. (B4.9)
15. **Shorts.** The Shorts feed shows no thumbnail, so the "thumbnail" is frame 0 to 1 s: the outcome image plus a 3 to 6 word line. Custom covers are desktop-only and eligibility must be checked; there is no A/B testing for Shorts. (B4.8, C10)

### A3. Hard rules for every thumbnail (checklist)

1. Words are never inside the generated image. Add 1 to 3 caps words (at most about 16 characters per line, at most 2 lines) as a separate live-text layer. This is a working assumption pending the owner's confirmation (A5, decision 1).
2. Use only the ten palette colors: #1a1a1a, #ffffff, #f3ead8, #bfe2ea, #8fbf5a, #4f7d3a, #9a6b43, #d2b48c, #e6b23a, #d94a38. Flat color with gentle cel shading, no gradients, ink outline about 12 to 16 px on the 1280x720 master.
3. Lit scenes only. No dark backgrounds and no empty flat backgrounds (the one exception is a plain paper card with an ink frame, Style 4).
4. People are stick figures exactly as on the character sheet: round white head with black outline, two dot eyes, line eyebrows and mouth, small white body, single-line arms and legs, one prop; no hands, feet, clothes or fingers. At most three people. Figures stand on light surfaces.
5. Red #d94a38 marks the culprit, the thing that went wrong. Amber #e6b23a is at most a small warm light. Red and amber never touch. Never put red on dark green or brown.
6. No arrows, dashed lines, motion lines or diagram symbols. No text, letters or numbers in the image: signs, gauges, screens and panels are blank.
7. No victims, injuries, gore, bodies, mockery or company logos. Never a death toll as a hook. Show structures and objects; attribute failures to systems, incentives and assumptions, never to individuals.
8. On the 1280x720 master: margins 64 px at the sides and 36 px top and bottom; keep 230x90 px free at bottom-right (duration badge) and about 110x110 px free at top-right. Scale by 1.5 for 1920x1080 and by 3 for 3840x2160.
9. Text: Lilita One, white fill, ink outline outside the letters at 12% of cap height, caps, main-word cap height at least 90 px (the number in Style 6 is deliberately larger).
10. Everything the thumbnail shows or says must be visible or explained in the video by second 15. The thumbnail adds a fact the title lacks and does not repeat the title's first 40 characters.
11. Export sRGB, 16:9, at least 1280x720 for every variant (otherwise all variants drop to 480p), under 2 MB, PNG or JPG.
12. Check at 168 px wide, in grayscale, blurred, on a light and a dark feed, and zoom to 100% to look for stray letters and numbers.
13. Use only facts from the registry (C8, B2.7) and re-verify each against the primary report before publishing.

### A4. The ten styles at a glance

Details, image prompts, layouts and watch-outs are in C5. Slots and cousins are explained in C6 and B4.2.

| # | Style | Slot | Example story and overlay words | Needs | At 168 px | Close cousins |
|---|---|---|---|---|---|---|
| 1 | Tiny Under the Giant | scale or scene | Vajont 1963; THE MOUNTAIN | a huge structure or force | words and red slab read; dam and wave small | 8 |
| 2 | The Moment Before | scale or scene | Quebec Bridge 1907; no words | one visible wrong detail before the failure (fits almost any story) | bridge and red chord read clearly | 8, 9 |
| 3 | The Impossible Scene | scale or scene | Comet 1954; no words | a true, odd image | airliner in the tank reads; figures vanish | none |
| 4 | Exhibit A | mechanism | Hyatt Regency 1981; LOAD DOUBLED | one small part with a big consequence | words and red nut read | 5 |
| 5 | The Cutaway | mechanism | Big Dig 2006; 26 TONS | a hidden mechanism | red anchors read; figure tiny | 4 |
| 6 | The Giant Number | mechanism slot (swap in) | Tacoma Narrows 1940; 42 MPH | a surprising non-casualty number | strongest; number survives blur | none |
| 7 | The Odd True Detail | human | Challenger 1986; ICE WATER | an odd, documented detail | words carry it; props tiny | none |
| 8 | The Crowd on the Shore | scale or scene | Vasa 1628; CALM DAY | a visible flaw and a calm crowd | words carry it; red ports vanish | 1, 2, 9 |
| 9 | Seat of the Decider | human | 2003 Blackout; LAST ALARM / 2:14 PM | a decision room | words carry it; scene small | 2, 8 |
| 10 | Close-Up Gaze | human | Flixborough 1974; NO DRAWING | one visible defect (fits almost any story) | strongest; survives blur | none |

Rule for tests: one human style (10, 7 or 9), one mechanism style (4 or 5; Style 6 can replace it when the story has a surprising number) and one scale or scene style (1, 2, 3 or 8), never two close cousins together (1 and 8; 4 and 5; 2, 8 and 9). When unsure, use Styles 10, 2 and 1.

### A5. Next steps and open decisions

- **Before the first upload (P1):** answer the four decisions below; make the character sheet (front view, three expressions, one prop; dot eyes with a gaze shift toward the hazard; a very large head version for Style 10); build the thumbnail template (a 1920x1080 or 3840x2160 master with guides for the margins and keep-out boxes, the Lilita One text style with the ink outline, and a paper-card variant); check in Studio whether Test & Compare and custom Shorts covers are available; choose the first two stories from the registry and re-verify their facts; draft three radically different concepts before scripting each video.
- **Per video (P2):** the eight-step packaging workflow in B5.1.
- **After 8 to 10 videos (P3):** tabulate per style (tests run, outcomes, CTR by traffic source, average view duration, direction of watch-time share); narrow to three or four house styles; keep one exploratory variant per video.

Decisions needed from the owner (B5.3):

1. **Text on thumbnails.** The brief bans text inside images, yet about 70% of the niche's inspected thumbnails carry words. Working assumption: the words are a separate overlay layer, never inside the generated image. If the owner refuses overlay text, all ten styles become wordless and Styles 4, 5, 6 and 9 lose their hooks.
2. **Plain paper (Style 4).** Confirm that a paper card with an ink frame counts as a "beat drawing" that the brief allows.
3. **Character sheet.** Approve dot eyes with a gaze shift toward the hazard, and a very large head for Style 10.
4. **Numbers.** Confirm that a death toll is never used as a thumbnail hook (recommended).

### A6. Task recipes

**R1. Thumbnail concepts for a new video**

1. Confirm the story is usable: not an ongoing legal case, at least two years old on the publication date, no terrorism, no medical or financial advice, politics only as regulatory facts (B1.2). Use only facts from the primary report and mark anything uncertain (B4.10). Compare with the registry (B2.7, C8).
2. Write one line for the outcome and the human-stakes number. Pick one documented odd detail, one surprising non-casualty number if there is one, and one object to plant in the opening and bring back at the end.
3. Draft three question titles of at most about 60 characters, no colon, key idea in the first 40 characters, concrete (a named object or a number) (B4.7).
4. Choose three styles from three different slots (A4 rule). Use the story-type table in C6 and the rotation in B5.1. Use Styles 3, 6, 7 and 8 only when the story has the special image, number, detail or contrast they need.
5. For each variant write: the idea in one sentence; 0 to 3 caps overlay words that add a fact the title lacks (never a death toll, never a repeat of the title's first 40 characters); the layout (hero, figure size, free area for the words); what is red (the culprit); the image prompt (the style's prompt in C5 with the story's nouns, plus the master prompt block); the facts to verify; the main risk.
6. Run the pair check (B4.7) and the production QA (B4.5, step 8), then publish with Test & Compare (B4.6).

Suggested output: one table with the columns variant, style, overlay words, image prompt, risk, facts to verify.

**R2. Write an image-generation prompt.** Structure: scene, subject, details, constraints (B4.5, step 3). Describe what is there in positive terms ("a blank plain board", "a gauge with a needle and no marks"), because image models often ignore "no text". Attach the character sheet and append the master prompt block (C5). Leave a calm area for the words. After generation zoom to 100% and look for stray letters, numbers, hands, shoes and thick limbs; fix with a masked edit or paint over; add the words as a separate live text layer (B4.4); export sRGB, 16:9, under 2 MB (B4.5, step 7).

**R3. Review a finished thumbnail.** Check in this order: (1) brief rules and the do-not list (B4.11); (2) policy (B4.9); (3) palette, fail pairs, red only on the culprit (B4.3); (4) text specification (B4.4); (5) the QA list at phone size, grayscale, blur, light and dark feed (B4.5, step 8); (6) the promise: everything shown is in the video by second 15 and the facts match the registry (B4.10). Report pass or fail per item with the measured value.

**R4. Plan or read an A/B test.** Rules in B4.6, mechanics in B2.1, sample sizes in B2.6, log template in B5.2. Test concepts, not tweaks; upload the preferred variant first; do not edit during a test; never judge by CTR alone; decide by the rules in B4.6 (heuristics [C]); look for patterns across 8 to 10 videos (B5.1, P3).

**R5. Use a story.** Re-check the age filter and the legal status on the publication date; use only registry facts (C8, B2.7, D7); mark contested causes (Flixborough, Tacoma) as contested and avoid a thumbnail that asserts a single cause; keep figures anonymous; never blame individuals; avoid the myths in B3.1.

**R6. A Short's first frame.** Frame 0 to 1 s: the outcome image plus a 3 to 6 word line; keep important content inside a central 2:3 crop; Shorts never carry an ask (brief); a custom cover is optional (B4.8, C10).

**R7. Answer an evidence question.** Give the grade; say "no controlled study found" instead of implying causation; use B3.1 for "is it true that...?" questions; do not repeat statistics that B3.1 lists as untraceable.

## H. Reference: the channel brief (verbatim), file map, glossary (H2 to H4)

H1 (consolidated source list) is not in this edition (see 0.4).

### H2. The channel brief (verbatim; it overrides everything else)

The standing brief for every script, title, description, scene list and image prompt made for the Stress Riser channel. The user pasted it on 2026-09-30. The wording below is theirs; only headings, line breaks and list markers were added. Notes such as "(user, 2026-09-24)" mark rules the user set explicitly.

#### CHANNEL

- **Niche:** Documentary-style stories of engineering disasters and inventions that failed or almost changed the world — what went wrong, the science behind it, and what we learned.
- **Unique angle:** Every story is told as a chain of small, reasonable decisions that added up to catastrophe — the viewer sees how they would have made the same call. Animation lets us show what no camera ever recorded: the inside of the reactor, the crack forming in the steel, the meeting where the warning was ignored.
- **Content language:** English. Write all voiceover text, titles and descriptions in this language.

#### AUDIENCE

Curious adults 18–50 in the US, UK, Canada and Australia who watch explainer videos on their phone or in the evening. Not engineers, but they like finding out how things actually work and feel smarter after watching. They come from the home feed on a question-title and a thumbnail that made them curious, and stay if the first 10 seconds pay it off.

**Prior knowledge:** intermediate — curious layperson, explain principles but not basics

**What frustrates them:**

- Most disaster content is either sensationalist clickbait or dry technical lectures.
- They want the real chain of causes, not 'human error' as the answer.
- They cannot tell which channels actually did the research.

#### TONE

**Voice:** Lively, curious explainer talking to one friend — the voice of someone who just found out something and cannot wait to tell you. Fast, plain, mostly in the second person and the present tense: the viewer stands where the person who decided stood. Asks the question the viewer was about to ask, then answers it. Dry understatement when the absurdity of a decision earns it. Never melodramatic, never mocking the dead: the failure is the villain, not the people. Modelled on Ink Explainer's narration (the speech patterns below are distilled from its transcripts), not on a Netflix documentary.

**Pacing:** Open with the outcome: in the first seconds the viewer must know what broke, the human stakes in plain numbers, and hear one line promising the chain of decisions behind it — only then rewind to the first decision. Long-form: outcome and stakes within the first 10–15 seconds. Shorts: within the first 3 seconds, one sentence. Then the story moves fast: something new on screen every 2–3 seconds (a new picture, a text card, a label), one idea per shot, and a reversal — 'but', 'except', a bigger number — every 45–90 seconds so stopping always feels expensive. Every act ends on a bridge that admits what the evidence so far cannot show and promises the next act. Long-form 8–12 minutes, Shorts 45–60 seconds.

**Always:**

- Every number, date, name, unit and quote is one you are certain of from the sources; when unsure, round it ('about', 'more than'), drop the number and keep the fact, or say what the report says — never a plausible guess. Nothing invented, ever: no made-up quotes, clock times or quantities. The timeline (construction, failure, report) must agree with itself.
- Plain spoken English at the level of a good newspaper feature. Everyday words first: 'brown, muddy water', not 'sediment-laden slurry'. A technical term only when the story needs it — and then with a five-word plain explanation the first time it appears.
- Write for the ear, not the page: contractions, varied sentence length, one thought per sentence, a natural breath between ideas. If you would not say it to a friend over dinner, rewrite it.
- After the opening, anchor every act in a concrete scene with time and place — never a general statement.
- Explain the physics or engineering principle at the exact moment the story needs it, with one clear analogy.
- Name the specific decision, number, or assumption that turned out to be wrong.
- Include at least one original analytical angle or comparison that a viewer cannot get from the Wikipedia article.
- End with the concrete change in engineering practice, regulation or thinking that followed.
- Cite the primary source (accident report, patent, memoir) by name in the script so it can be listed in the description.
- Long videos ask exactly twice, woven into the story in the narrator's own voice: one subscribe sentence between minute 3 and 5, and near the middle a contested question from the story followed by 'tell me in the comments'. Shorts never ask (user, 2026-09-24).
- Every fact carries a number, a name or a year; when a number is big, put it next to something the viewer knows ('270 million cubic metres — a mountain the size of Manhattan's skyline').
- Plant the next story in the last line: end on a question this video did not answer, one that another engineering failure will.
- American spelling throughout (color, story, meters, defense); units as the story's own country used them, translated once for the other audience.
- Every scene opens with a sentence that stands on its own after a cut; the join to the previous scene is a picked-up noun or thread, not a fragment. No rhetorical device more than twice per video.

**Never:**

- Clickbait promises the video does not deliver.
- Phrases like 'in this video we will look at' or 'let's dive in'.
- Blaming individuals; attribute failures to systems, incentives and assumptions.
- Graphic descriptions of injuries or death — state casualties factually and move on.
- Speculation presented as fact; mark uncertainty explicitly.
- Filler recaps and repeated sentences to stretch duration.
- Any ask beyond those two: no likes, no bell, no 'watch next', no ask in the opening or at the end, none at all in Shorts — and never an ask that sounds like an ad break instead of part of the story.
- Titles with a colon, a case name first, or a statement; every title is a question a curious stranger would ask ('Why did 1,900 people die under a dam that never broke?').
- Runs of short sentences (three or more in a row under seven words) — the short sentence is the landing, not the walk.

**Speech patterns** — how a sentence sounds, not what it says. Each rule has an example in our own subject; the example shows the shape, never copy it:

1. Second person, present tense, the viewer inside the scene — in the seat of the person who decided, never in the place of the dead: 'You're the engineer on the night shift. The gauge reads three meters over the line, and the phone is ringing.' Roughly one 'you' or 'your' every 25 words across the whole script.
2. Sentences of two lengths, average about twelve words and never above fourteen on average across the script — count. Most sentences are ten to eighteen words and carry a clause; no sentence passes twenty-two words: when one does, split it at its 'and', 'because' or 'so' and start the second half with 'And', 'So' or 'But'. After every long explaining sentence comes a short one that lands it, six words or fewer — about one sentence in six, never three in a row: 'So the water rose another meter a day, past the mark the geologists had drawn on the wall. Nobody lowered it.' A script where nearly every sentence is short is a telegram, not a story.
3. Sentences chain. About a third of them start with 'And', 'So' or 'But', and each one picks up the one before it: 'So the crack widened. And a wider crack drinks more water. But more water is more weight, and the weight is what the crack was about.'
4. Cause and effect as a ladder — the last noun of one sentence is the subject of the next, three or four rungs, then a short line that snaps shut: 'More load means more heat. More heat softens the steel. Softer steel lets the load move. And then the roof comes down.'
5. Pivot words: 'Now,' opens a change of direction or the viewer's objection; 'So,' draws the conclusion; 'But' turns the story. One of them at the start of a sentence every few lines, never two in a row.
6. Say the viewer's objection out loud before they think it, then answer it with a person who went and checked: 'Now, you're probably thinking a steel dam doesn't just bend. That's a fair doubt — and one inspector had it too, in 1955, with a tape measure and a notebook.'
7. Once per video, a guess: ask the viewer to pick, give the answer most people give, then flip it: 'So which pier went first — the new one or the old one? Take a guess. Most people say the old one. It was the new one, and that is the whole story.'
8. Translate every big number twice: say it, say what it is not, then put it next to the viewer's own life: 'Two hundred and seventy million cubic metres. Not the lake — the mountain. Picture every building in Manhattan dropped into a bathtub, in forty-five seconds.'
9. One metaphor per act that turns the technical thing into something the viewer owns, in a sentence of the shape 'X is a Y': 'A crack is a receipt: it tells you exactly what the structure has already paid for.' 'The spillway is the dam's fuse.'
10. Every act ends with a bridge that admits a limit and promises the next: 'But the drawings can only tell you so much. They can't show you what the night shift heard. So let me walk you through that shift.' Or a promise: 'And here's the part the inquiry buried on page 212.'
11. Introduce a person by year, role, name and one physical action in a place, never by title alone: 'In 1959, a young geologist named Edoardo Semenza walked up the north slope with a hammer and started hitting the rock.'
12. Dry humour by understatement, aimed only at decisions and institutions, never at victims: 'The committee met, which is what committees do.' 'The manual called it a safety margin. The margin was one bolt.'
13. Lists come in threes, the last item the longest or the sharpest: 'No alarm, no drill, and nobody whose job it was to press the button.'
14. Plant one object in the opening and bring it back at the turn and at the end: 'Remember the gauge from the first minute? It's still reading three metres over.' The last lines return to the opening image before the final question.
15. Close with the whole story in three parallel sentences of the same shape, then one contrast pair: 'The rock took two years. The water took one night. The warning took a paragraph. They had the map. They had the map in the wrong drawer.'
16. Engineering as a friendly guide: every technical fact is exact to the source, and then it is explained the way a good engineer explains it to a friend at a kitchen table — what the part does, why it matters here, in everyday words, one fact per sentence. The number comes first in a size the viewer can feel (a ten-storey building, a football field, a day of rain), the exact figure right after it only if the story needs it; never two numbers in one sentence, never a unit the viewer has to convert. The viewer should finish feeling they understood the engineering and enjoyed it, not that they sat through a lecture.

#### VISUAL STYLE

**Art style:** Hand-drawn cartoon illustration like a modern animated explainer: clean black outlines, soft flat colours with gentle cel shading, warm natural light. Explaining is drawn as the real world, never as a diagram: no arrows, no dashed lines, no motion lines — movement and force show in the poses and in what the world does (spray, dust, a bent pole, water pouring); the part that matters may be in its colour with the rest pale, or seen in a see-through cutaway. Friendly and clear; never realistic, photographic or 3D.

**Backgrounds:** Every picture shows a whole, richly illustrated place that fills the frame: a near, middle and far layer, the things that belong there, soft shadows and light from the sky or a window. Detailed but tidy — the person stays the clear subject. Beat drawings and text cards sit on plain flat paper.

**Color palette:** #1a1a1a, #ffffff, #f3ead8, #bfe2ea, #8fbf5a, #4f7d3a, #9a6b43, #d2b48c, #e6b23a, #d94a38

**Characters:** Every person is a stick figure exactly as on their character sheet: a round white head with a black outline, two dot eyes, simple line eyebrows and a line mouth that show the feeling the picture asks for (worried, surprised, scared, angry, calm), a small white body, and arms and legs that are single black lines. The limbs stay single lines in every shot, even in a close-up of a foot or a hand — never thick arms or legs, never trousers, sleeves, shoes or fingers. The only extra is the character's own prop. The pose and the small face act together; no smile unless the picture asks for one.

**Must never appear in images:** text, letters, numbers, captions, logos, watermarks, arrows, dashed lines, motion lines, diagram symbols, photorealism, 3D render, realistic people, thick limbs, trousers, sleeves, shoes, fingers, gore, blood, collage, multiple panels, empty flat background

#### CONSTRAINTS

**Forbidden topics:**

- ongoing legal cases or disasters less than 2 years old
- terrorism and deliberate attacks
- medical or financial advice
- politics beyond the regulatory facts of the case

**Video ending (CTA):** The ending must land, not trail off. Close the loop: return to the opening moment or image, state the lasting lesson in one memorable plain sentence, then finish on a question this story did not answer — the kind another engineering failure will ('If a dam can hold and still kill 1,900 people, what does a bridge do when nobody is watching?'). That question is the last line. No 'watch this', no pointer to another video, no ask at the end — the subscribe and comment asks came earlier (minute 3–5 and the middle; user, 2026-09-24).

**The video description must always include:** Sources are listed below. This video uses AI-assisted narration and animation; the research, script editing and analysis are done by a human.

### H3. Repository file map

Everything is in the repository `jurel11/test`, branch `claude/stress-riser-channel-o2tnfv`, folder `stress-riser/`. The `isotrack-*.html` files in the repository root are unrelated to the channel.

| Path | What it is |
|---|---|
| `STRESS-RISER-AI.md` | This file: the AI-readable edition of the research (plain Markdown) |
| `STRESS-RISER-MASTER.html` | The full human-readable dossier in one HTML page: images, raw notes, reviews, video indexes, consolidated sources |
| `channel-brief.md` | The channel brief, verbatim (also loaded automatically through `CLAUDE.md`) |
| `thumbnail-styles.md` | The corrected report of the ten styles (Part C of this file) |
| `thumbnail-lookbook.html` | Visual gallery of the ten mockups with Slovenian captions |
| `thumbnails/NN-*.png` | The ten final composites (1280x720, with the text overlay) |
| `thumbnails/art-only/NN-*-art.png` | The layer an image generator would produce (no words); Styles 2 and 3 have no words, so no separate file |
| `thumbnails/svg/NN-*.svg` | Editable vector sources |
| `thumbnails/qa-phone-sizes.png` | Each style at 360 px, 168 px (light and dark feed), grayscale and blurred |
| `research/*.md` | The eight agents' working notes (G3 to G10 of the HTML dossier) and the palette pair report |
| `master/*.md`, `master/reports/*.md`, `master/ai/*.md` | Text sources of the two dossier editions: summary, synthesis, briefs, the eleven reports (eight research reports and three reviews), and the AI-edition front matter |
| `data/` | CSV tables (niche and cartoon video indexes, palette pairs, fonts, OCR) and small reports |
| `tools/thumb_preview.py` | Feed preview rig: light and dark feed, several sizes, badge, grayscale, blur, safe zones (needs Pillow) |
| `tools/scenes.py`, `lib.py`, `render.py`, `fonts/` | The mockup generator (needs a headless Chromium) |
| `tools/build_master.py`, `tools/build_ai.py` | Scripts that rebuild the HTML dossier and this file from the sources above |

Preview tool usage: `python3 tools/thumb_preview.py image.png --title "..." --duration 10:24 --safezone`.

Rebuilding this file: `python3 tools/build_ai.py` (Python 3 only, no packages needed).

### H4. Glossary

| Term | Meaning |
|---|---|
| **Thumbnail** | The still image shown in feeds and search; on Shorts, a custom cover |
| **Packaging** | The title and thumbnail seen together: the promise that makes a viewer click |
| **Impression** | A thumbnail shown for more than 1 second with at least 50% visible (YouTube's definition) |
| **CTR (click-through rate)** | Clicks divided by impressions; "how often viewers watched a video after seeing a thumbnail" |
| **AVD / average view duration** | Average time watched per view; used with CTR to tell clickbait from honest packaging |
| **Watch-time share** | The metric Test & Compare uses to pick a winner (the exact formula is unpublished) |
| **Test & Compare** | YouTube Studio's A/B test: up to 3 titles and/or thumbnails on a long-form video |
| **Browse, suggested, search** | The main traffic sources; CTR differs a lot between them |
| **Outlier score (1of10)** | A video's views divided by the median views of its channel |
| **Correlational / observational** | A pattern in existing data that cannot show cause |
| **Cold start** | A new channel's first uploads, judged by strangers rather than subscribers |
| **Art-only layer** | The generated picture without any words; the words are a separate overlay |
| **Composite** | The art layer plus the text overlay |
| **Overlay (text layer)** | Live text added in a design tool (Figma, Canva, Photopea) on top of the picture |
| **Cap height** | Height of capital letters; sets legibility at small sizes |
| **Safe zone / keep-out** | Parts of the 1280×720 frame left free of important content because a YouTube overlay (duration badge, hover icons) or a possible crop covers them |
| **Master** | The thumbnail file at full size (1280×720 in the mockups; 1920×1080 or 3840×2160 allowed) |
| **L\*** | Lightness in the CIELAB color space (0 black, 100 white); the difference ΔL\* shows how different two colors look in grayscale |
| **ΔE2000** | A standard measure of color difference |
| **WCAG contrast ratio** | The accessibility standard for text contrast (4.5:1 for normal text) |
| **APCA (Lc)** | A newer contrast measure (Lc 60 about the minimum for fluent text) |
| **Color-blind simulation** | A calculation of how colors look to protan, deutan and tritan viewers |
| **Squint test** | Looking at a blurred version: if the accent, main word and silhouette survive, the thumbnail reads |
| **Culprit color** | The house rule here: red marks the thing that went wrong |
| **Plan view** | A picture looking straight down on a scene (used for the Comet tank) |
| **Cutaway** | A see-through cross-section of the part that matters |
| **Beat drawing** | A simple drawing on plain flat paper, used by the brief for key moments |
| **Primary source** | The official report, patent or memoir (for example NBS for the Hyatt walkways) |
| **Legal filter** | The brief's rule: no ongoing legal cases and nothing less than two years old |

## C. The ten thumbnail styles: house system, evidence, testing playbook, fact registry (C1 to C12)

Research date: 2026-09-30. Eight research agents read official YouTube documentation, peer-reviewed studies and creator data, and looked at real thumbnails (about 105 in the engineering-disaster niche and about 300 in cartoon channels were inspected by eye, out of 860+ downloaded). Their full notes, with every URL, are in `research/`. The first draft of this report and the mockups were then reviewed by two independent reviewers (one checked every claim against sources, one checked the brief, the palette and the design); this is the corrected version. A third reviewer later checked the master file built from this report (`STRESS-RISER-MASTER.html`); the corrections that touch this report are applied here too. Ten vector mockups are in `thumbnails/` (open `thumbnail-lookbook.html` to see them side by side).

**Read this first: what the evidence can and cannot tell you.**
The research found no controlled study of what makes YouTube thumbnails get clicked, and YouTube's own A/B tool optimizes watch-time share, not click-through rate (CTR). Almost every "rule" online rests on samples of videos that already went viral: it shows what winners look like, not what caused the clicks. Related lab and headline experiments exist, but none tests cartoon or stick-figure thumbnails on YouTube. So the ten styles below are **hypotheses built on the best evidence available, designed to be tested against each other**, not guaranteed winners. Each claim carries an evidence grade: **[A]** official documentation, peer-reviewed, or a large dataset; **[B]** first-hand data from a creator or company, or a correlational dataset; **[C]** opinion, vendor blog, or my own inference.

### C1. The short version

- **Why this set should stand out (untested).** The engineering-disaster niche is photographic, dark and text-heavy: across 268 direct-niche thumbnails the average brightness was 0.43 on a 0–1 scale (the figure for eight cartoon-style channels was 0.52). Among the channels checked, almost nobody in the disaster niche uses flat hand-drawn illustration (the closest are the Infographics Show's flat vector and Storified's stylized 3D). And almost nobody shows the moment *before* the failure, which is your whole angle. Whether standing out lifts CTR is unknown.
- **What the evidence supports.** One dominant subject; at most three people (Netflix's artwork tests); a readable emotion; few or no words; a promise the video keeps by second 15.
- **What is contested or unsupported.** *Faces always win*: contested (faces and no faces perform about the same in the largest dataset). *Shocked, open-mouth faces*: contested (only about 5% of vidIQ's breakout videos use an exaggerated expression, but that figure has no base rate; YouTube's own tips page recommends "a shocked face"). *Exact word counts*: convention, no study. *Red wins*: 1of10 found cyan, green and yellow/orange ahead. *Bright and saturated*: 1of10 supports it (winners only), but both of our audits found that brightness, saturation and clutter did **not** separate top from weak videos within a channel (coin-flip tallies: 12–19 of 32 channels, and 17–29 of 44). Treat brightness as a hypothesis.
- **The test rule.** Small tweaks cannot be detected on a small channel: 4% → 5% CTR needs about 6,700 impressions per variant, while 4% → 8% needs about 550. So test **radically different concepts** (these ten styles), never font or color tweaks.
- **What fits almost any story.** Styles 2 (Moment Before), 10 (Close-Up Gaze) and 1 (Tiny Under the Giant). Styles 3, 6, 7 and 8 need a special true image, number, odd detail or contrast in the story.
- **Four decisions I need from you** are in section 9. The biggest: the brief bans text inside images, yet about 70% of the thumbnails inspected in the niche (75 of about 105; median 3–4 words, maximum 7) carry words. I assume the words are a separate overlay added in your design tool, never inside the generated image.

### C2. Hard constraints (every thumbnail must pass)

From YouTube's own documentation [A] unless marked. Sources in `research/platform.md` and `research/design-system.md`.

1. **Format.** 16:9, JPG or PNG. Official recommendation 3840×2160, minimum width 640 px (the old "1280×720" advice is out of date on the official page). YouTube serves thumbnails at 1280×720 (measured on YouTube's own responses, 2026-09-30). Upload limit: 2 MB from a phone, 50 MB from desktop (announced Oct 2025 [B]). My mockups are 1280×720 PNG-24 at about 100 KB each.
2. **Testing.** Every variant must be at least 1280×720, or **all** variants are downscaled to 480p. Up to 3 variants; long-form only; desktop Studio only. The winner is chosen by **watch-time share**, not CTR.
3. **Where things sit.** The duration badge is bottom-right and watched videos show a red progress bar along the bottom edge. I keep **230×90 px free at bottom-right** and about **110×110 px free at top-right** of the 1280×720 master (neither box is official geometry: the badge box comes from a [C] source and the top-right size is unverified). Margins: 64 px on the sides, 36 px on top and bottom (outline included). YouTube is running an experiment that may crop thumbnails on mobile Home (Team YouTube post, 2026-04-29; the page is script-rendered, so a reviewer could not re-open it), so keep everything important central.
4. **Impressions count** only when the thumbnail is on screen for more than 1 second with at least 50% visible, and not on the mobile website, embeds or email.
5. **Policy.** Never a thumbnail that "misleads viewers to think they're about to view something that's not in the video" (strike risk). No "violent imagery that intends to shock or disgust", no blood or gore. Advertiser-friendly rules apply to the thumbnail too: disaster footage with visible harm to people gets limited ads; content that "profits from or exploits" a sensitive event gets none. YouTube treats clearly animated depictions differently from live action. Your rules (no injuries, no victims, no mockery) already fit. YouTube's performance FAQ also lists "Loud: ALL CAPS or !!!!!" among things to avoid: keep to one to three words, never use exclamation marks, and consider testing sentence case against caps.
6. **AI disclosure.** Not required for clearly non-realistic animation; YouTube's rules list "generative AI tools to create or improve a … thumbnail" among uses that do not need disclosure. A realistic depiction of an event that did not happen would need it, so stay flat and cartoonish.
7. **Originality.** YouTube's monetization policy lists "AI-generated content made with generic or unoriginal templates" among content that is not monetizable, and reviewers look at thumbnails. Its language about repetitive content is about "giving the impression of mass production without adding the creator's original, authentic insights or perspective". My reading, not YouTube's words: a house style is fine as long as each thumbnail is specific to its story.

### C3. What the research found (condensed)

| Finding | Grade | Source (details in `research/`) |
|---|---|---|
| Face vs no face performs about the same overall; faces help mainly channels above 200K subscribers; multiple faces beat a single face in that sample | [B] correlational, 300K+ videos of 2025 | 1of10 (2026-02-06) |
| Thumbnails with text got about 19% fewer views; best were no text, or under 10 characters covering under 7% of the image | [B] correlational | 1of10 |
| Cyan (+36%), green and yellow/orange do well; dark thumbnails underperform | [B] correlational | 1of10 |
| Among 500 breakout videos: face 69%, high contrast 56%, overlay text 72% (median 5 words), exaggerated expression about 5%. No base rate, so convention, not cause | [B] | vidIQ 2026 (page blocked; via a secondary summary) |
| Titles with numbers got about 11% fewer views on average | [B] correlational, viral videos only | 1of10 |
| Netflix artwork tests: complex emotion beats stoic faces; win rates dropped sharply above 3 people | [B] company data, films not YouTube | Netflix, "The Power of a Picture" |
| Closing the mouth in thumbnails raised watch time in 30 of 30 videos, "a small difference" | [B] | MrBeast's thumbnail lead |
| Strong sentiment in the thumbnail raises views (16,215 covers); visual complexity has an inverted-U relationship with popularity | [A] observational (the second study's platform is not verified as YouTube) | Cui 2024; Fang 2026 |
| Curiosity peaks with a **medium** information gap, not a maximal one | [A] | Kang 2009; Le Quéré & Matias 2025 (8,977 headline tests, headline plus image); Frede 2026 |
| Question-framed **headlines** reduced engagement on average (news headlines, not YouTube) | [A] | Fang & Wheeler 2026 |
| Question vs statement **titles** on 891 matched million-view pairs: no difference | [C] | OverseerOS |
| A figure looking at the object (not at the viewer) shifts attention to that object and raises recall. The study used real faces on banner ads | [A] | Sajjacholapunt & Ball 2014 (n=72) |
| More cartoonised faces let people identify emotion more accurately at short exposures | [A] | Kendall 2016 |
| A Google ranking paper: "Ranking by click-through rate often promotes deceptive videos that the user does not complete ('clickbait')", so it ranks by expected watch time. It is from 2016; YouTube staff now also cite surveys and satisfaction | [A] | Covington, Adams & Sargin, RecSys 2016 |
| CTR: half of all channels sit between 2% and 10%; CTR naturally falls as reach widens | [A] | YouTube Help 7628154 |

**Unsupported or untraceable claims** (researched; none traced to a primary source): "3 words is optimal"; "faces give 2.3× CTR"; "eye contact adds 20%"; "median +32.7% uplift from A/B testing"; "80% brand recognition from color"; "13 ms to stop the scroll" (a lab picture-detection result, not a feed effect); "99.9% of Shorts views come from the feed" (a creator's remark, misattributed online); "38% higher CTR from a consistent template" and the "70/30 rule" (no method). **Contested rather than false:** the rule of thirds and the F-pattern for single-subject phone thumbnails have no CTR evidence, but YouTube's own tips page suggests the rule of thirds.

### C4. The house system: what never changes and what varies

Ten different concepts still have to look like one channel. Fixed anchors (from `research/design-system.md`, plus my own choices marked "I"):

1. **The 10-color palette only.** Measured on the mockups: 97.6–99.1% of pixels are exact palette colors; the rest are one- or two-pixel blends at edges.
2. **Ink outline** #1a1a1a on every shape, about 12–16 px on the 1280×720 master.
3. **The stick figure exactly as on the character sheet** (round white head, two dot eyes, line brows and mouth, small white body, single-line limbs, one prop). *There is no character sheet in the brief: make one (front view, three expressions, prop) and attach it to every generation.* Figures stand on **light surfaces**: single black limbs vanish on an ink-black background.
4. **One accent, and it always means "the thing that went wrong"** (I). Red #d94a38 marks the culprit: the slid slope, the bowed chord, the nut, the anchors, the twisting deck, the rubber ring, the bypass pipe, the frozen screen. Measured share of the frame on the mockups: 0.2–5.1%. Large culprits reach 2–5%; small parts are drawn oversized and still stay under about 1%. That is fine only if they still read at 168 px.
5. **Text:** Lilita One (free, OFL), white fill, ink outline drawn outside the letters at 12% of cap height, caps, 1–3 words, at most about 16 characters per line, at most 2 lines, cap height at least 90 px for the main word. One exception: the number in Style 6 is deliberately huge.
6. **Flat color with gentle cel shading.** No gradients.
7. **Lit scenes, no dark backgrounds** (I). Dark thumbnails underperform in 1of10's data [B]; the brief bans an "empty flat background"; and one of Ink Explainer's three weakest thumbnails is a dark cave. The first draft had two ink-black styles; both were redrawn as lit scenes. Amber #e6b23a is only a small warm light if used at all (it is weak against every palette color except ink).
8. **The safe zones in section 2.**

Variables per video: composition, hero object, background family, emotion, text position, word count, camera distance, cutaway or not. Alternate the background family between consecutive uploads so the feed alternates.

**Color math** (my computations, `research/design-system.md`). The palette has only three lightness tiers: **light** (white, paper, sky, amber, tan, light green), **mid** (red, brown, dark green) and **dark** (ink). Colors in one tier cannot be told apart by lightness, in grayscale or with color-blindness. Rules I used:

- A lightness gap (L*) of 50 or more is safe for text; 40–50 for big bold text; 25–40 for big flat shapes with an outline; under 25 is invisible.
- **Ink** works as text on every light color and as the outline everywhere (at least 3:1 against every palette color).
- **White or paper text needs the ink outline** on sky, paper, amber, tan and light green. Never use red, brown or green as a text fill.
- **Fail pairs (lightness gap under 25: all 21 pairs, smallest gap first, ΔL* after each pair):** tan/amber 0.5, dark green/brown 1.4, brown/red 2.5, light green/tan 2.9, light green/amber 3.3, dark green/red 4.0, paper/sky 5.3, white/paper 7.0, sky/amber 12.2, white/sky 12.3, sky/tan 12.7, sky/light green 15.6, paper/amber 17.5, paper/tan 18.0, light green/red 20.4, paper/light green 20.8, light green/brown 22.9, tan/red 23.2, amber/red 23.7, light green/dark green 24.3, white/amber 24.6. Red and green also merge for red-green color-blind viewers: red turns olive. Outlines carry these pairs in the mockups; check every real image.
- **Pale thumbnails on the white feed lose their edge.** Against the #ffffff page, sky scores about 1.37:1, paper 1.20:1 and white 1.00:1. Keep a mid or dark band along the image edges (Style 4 uses an ink frame). The dark-mode feed is #0f0f0f.

### C5. The ten styles

Mockups are vector drawings that show composition, color and text placement. They are **not final art**, and details are simplified (see each style's watch-out). Each example lists the story, a draft question title, and the overlay words. **All facts in the examples are in the registry in section 8.** Draft titles are questions with no colon, at most 60 characters, and the thumbnail words add something the title does not say. Phones truncate long titles (real limits vary by device [C]).

Files: `thumbnails/NN-*.png` (final composite), `thumbnails/art-only/NN-*-art.png` (the layer an image generator would produce: no words; styles 2 and 3 have no words so they have no separate file), `thumbnails/svg/` (editable).

**Master prompt block** (append to every image-generation prompt below). It is written in positive terms because image models often ignore "no text" instructions, so also check every output at 100% for stray letters and numbers:

> Hand-drawn flat cartoon illustration in the style of a modern animated explainer: clean black outlines of even weight, soft flat colors with gentle cel shading, warm natural light, 16:9 landscape, one dominant subject, simple bold shapes, a lit scene. Use only these colors: ink black #1a1a1a, white #ffffff, paper cream #f3ead8, sky blue #bfe2ea, light green #8fbf5a, dark green #4f7d3a, brown #9a6b43, tan #d2b48c, amber #e6b23a, red #d94a38. Any person is a stick figure exactly as on the attached character sheet: round white head with black outline, two dot eyes, simple line eyebrows and mouth, small white body, arms and legs as single thin black lines, no hands, feet or clothes. Every sign, gauge, screen and panel is blank and unmarked. A calm, quiet area is left free for a title.

#### Style 1 — Tiny Under the Giant
*A huge structure or force fills the frame; one small figure watches. The culprit is the only red.*

- **Example:** Vajont Dam, 1963. Draft title: *Why did 1,900 people die under a dam that never broke?* Words: **THE MOUNTAIN**. Image: a pale mountain with a red slab sliding into the reservoir, a big wave over the still-standing thin dam, a small figure watching from the far ridge.
- **Why it should work:** scale contrast is a real attention driver (a large object captures attention, Proulx 2010 [A]); "safe danger" is why people enjoy fear (Rozin 2013 [A]). Similar images are seen among high-view videos: Practical Engineering "Why Are Beach Holes So Deadly?" (tiny figure in a huge trench, 7M views, 0kQXOTcEB_E) and Zenn "Why Hasn't Anyone Raised the Titanic?" (706K, IlCq6a0sDCk) [B; a correlation, with no CTR data]. "THE MOUNTAIN" completes the title instead of repeating it.
- **Layout:** the structure and wave take most of the frame; the figure is about 18–22% of the frame height (figures under about 12% read only by posture, not by face); the figure stands on a ridge, never below the harm; words top-left.
- **Watch out:** never place the figure where victims were. The dam in the mockup is drawn thin and tall (Vajont is an arch dam); check the profile against a reliable drawing before final art.
- **Prompt:** *A tall thin concrete dam standing intact while a huge wave of dark green water arches over its top; on the left a pale tan mountain slope with a jagged red slab sliding into the reservoir and a white splash; a small stick figure stands on a brown ridge on the far right looking at the scene with a worried face. Sky blue background with two clouds. The upper left is calm and empty.* + master block.
- **Also fits:** Banqiao, Sleipner, any dam or slope failure, Titanic-type stories.

#### Style 2 — The Moment Before
*The calm scene just before the failure, with one wrong thing in the middle of the frame and a worried figure who has noticed.*

- **Example:** Quebec Bridge, 1907. Draft title: *Why did engineers keep building a bending bridge?* Words: **none**. Image: a half-built cantilever truss stopping in mid-air, its red lower chord visibly bowed, a small inspector pointing up from the bank. The Quebec facts are low-confidence: see the registry.
- **Why it should work:** this is the niche gap: only two of the roughly 105 thumbnails inspected by eye came close to showing a cause or decision (Storified "26 PEOPLE", 613K, 0QXvhtPaKoY; Infographics Show's decisions video, 957K, vRAsU_ov84Q) [B]. Curiosity is strongest at a medium gap (Kang 2009; Le Quéré & Matias 2025 [A]). Mobbs 2007 (threat feels larger when nearer) is a maze-task mechanism, not evidence about thumbnails [A, untested here]. It is also your unique angle drawn as a picture.
- **Layout:** the whole intact structure plus the wrong detail **in the center of the frame, where the eye already lands** (anomalies away from fixation are often missed: Vö & Henderson 2009, 2011 [A]); figure 15–20% of frame height, looking at the detail.
- **Watch out:** the wrong detail must be visible at 168 px (here the red chord is), and everything shown must be in the video by second 15. Add 1–2 words only if they add a fact the title lacks.
- **Prompt:** *A half-built steel cantilever bridge reaching out from a brown stone pier and stopping in mid-air, a long red lower beam clearly bowed downward, a straight tan upper beam and thin crossing braces; a small stick figure with a worried face stands on a green bank pointing up at the red beam; dark green river, sky blue background with clouds.* + master block.
- **Also fits:** Challenger at the cold pad, Tacoma's bouncing deck, Hyatt's empty atrium, Vasa at the quay.

#### Style 3 — The Impossible Scene
*A scene that looks absurd but is true, with no words needed.*

- **Example:** de Havilland Comet, 1954. Draft title: *Why did a jet airliner end up in a water tank?* Words: **none**. Image, in plan view: a whole airliner fuselage in a water tank, wings protruding out through seals in the tank walls, a red ring on the roof near the front where a fatigue crack began, two calm engineers on the floor.
- **Why it should work:** the most extreme "zero-text anomaly" pattern: Veritasium "Why Are 96,000,000 Black Balls on This Reservoir?" (112M, uxPdPpi5W4o) and Mark Rober's jello pool (223M, DPZzrlFCD_I) show the image *is* the hook (both are 7-year cumulative totals) [B]; 1of10's best text setup is none, or under 10 characters [B]. Muller's "legitbait" idea: the picture hints at the real content [B, secondary].
- **Layout:** the bright water rectangle is the focal point on a warm floor; hero 65% of frame width; figures small and calm.
- **Watch out:** only use it when the true image exists; never invent an odd picture. The tank test is documented (Withey 1997); windows are not visible in plan view, so the "square windows" myth is neither drawn nor claimed. The red ring marks where a fatigue crack began (the tank-test crack started near the forward escape hatch; the Elba crack near the roof antenna cut-out): say which in the video.
- **Prompt:** *A plan view from above of a large rectangular water tank in a brown-walled hall: a complete white jet airliner fuselage lies in the light blue water with its swept wings passing out through two brown seals in the tank walls, small tailplane inside the tank, a thin red ring painted on the roof near the nose; two calm stick figures stand on the tan floor in front, one with a clipboard.* + master block.
- **Also fits:** Vasa raised from the seabed, Sleipner, "nothing broke but it failed" cases.

#### Style 4 — Exhibit A
*One small part, drawn enormous, alone on a plain paper card with a thick ink frame. The part is red.*

- **Example:** Hyatt Regency walkways, 1981. Draft title: *Why did one small change help bring down two hotel walkways?* Words: **LOAD DOUBLED**. Image: a giant red nut and washer pulling through a split steel box beam, two separate rods (one above, one below).
- **Why it should work:** one dominant subject is the best-supported composition principle (Netflix win rates fall as scenes get more complex [B]; visual complexity has an inverted-U relationship with popularity [A]). A lone object on a plain field appears among high-view niche videos (Brick Immortar "El Faro", 4.8M, -BNDub3h2_I; Beyond Sky's clean object-on-light thumbnails, 1.6M and 1.2M) [B, correlational]. The brief explicitly allows beat drawings and text cards on plain flat paper, so this is the one style with a plain background by design.
- **Layout:** hero about 30–40% of the frame, off-center; words top-left; an ink frame keeps the pale card from dissolving on the white feed.
- **Watch out:** the geometry is generic and the rods are offset only to signal "two rods": check the connection detail against NBS report NBSIR 82-2465 before final art. The full story is two causes (the original detail would not have met code, and the change "essentially doubled" the load): the words "LOAD DOUBLED" are only half; the video must tell both.
- **Prompt:** *A plain cream paper card with a thick black frame; in the center a giant red hexagonal nut and a round white washer pulled up into a tan steel box beam whose welded seam has split open, a brown rod entering the beam from above and a second brown rod hanging below and slightly to the right.* + master block.
- **Also fits:** Challenger's rubber ring, Flixborough's bellows, Comet's bolt hole, Big Dig's anchor.

#### Style 5 — The Cutaway
*A see-through cross-section of the part no camera ever recorded.*

- **Example:** Big Dig ceiling, 2006. Draft title: *Why did a Boston tunnel ceiling fall after glue let go?* Words: **26 TONS**. Image: the roof slab cut open, three red anchors sliding out of their epoxy-filled holes with dark gaps above, a heavy panel hanging tilted below, a small worried figure standing clear of it.
- **Why it should work:** cutaways are common among high-view engineering videos (Jared Owen "What's inside the Titanic?", 22M, HLrBUwNSEo0; Sabin Civil "Golden Gate", 19M, E6tp8DCAJ-0) [B, correlational], and a cartoon precedent exists (Ink Explainer's mammoth-carcass cutaway, 756K, dp3jYZXKOos) [B]. It delivers your promise, "what no camera ever recorded", and the brief explicitly allows a see-through cutaway.
- **Layout:** the cutaway is the central band; the red parts are oversized; words on the earth band; nothing important in the bottom-right corner.
- **Watch out:** the hardest style to draw correctly. Cause: epoxy with poor creep resistance (NTSB HAR-07/02); the mockup shows three anchors as an illustration, so check the count and details against the NTSB report. One person died in a car under the ceiling: keep every vehicle and person out from under the panel.
- **Prompt:** *A cross-section cutaway of a tan speckled concrete roof slab under brown earth: three white epoxy-filled holes each with a thick red anchor bolt that has slid down leaving a dark gap above it, the anchors holding a large white ceiling panel that hangs tilted in a bright cream tunnel; a small worried stick figure stands far to the left on a dark road.* + master block.
- **Also fits:** Comet's fatigue crack, Challenger's joint, Tacoma's cable band, Flixborough's bellows.

#### Style 6 — The Giant Number
*One figure, huge, is the hook. The number is in the words layer, not the picture.*

- **Example:** Tacoma Narrows, 1940. Draft title: *Why did a four-month-old bridge twist itself apart?* Words: **42 MPH** (number cap height 250 px, unit 110 px). Image: a suspension bridge with the roadway drawn as a red-and-brown twisting ribbon, a small worried figure on a mound.
- **Why it should work:** it survived every phone-size test with the number still readable at 168 px. Numbers as the hook are common among high-view niche videos (Dark Records "1,500 TONS OF TNT", 4.8M, NgQ7jh9mrWs; Sabin Civil "27000!", 19M; Banqiao "62 DAMS GONE", 358K, CFnh54FeNo0) and in cartoon channels (Explain In Paint "-58°F?", 398K, Q3_htAFS7wg) [B, correlational]. 1of10 found titles with numbers got about 11% fewer views [B, correlational, viral videos only]; that is not a reason to avoid numbers, but putting the number in the thumbnail and not the title keeps the two complementary. Test it.
- **Layout:** the number takes the left 40%; picture on the right; nothing in the bottom-right zone.
- **Watch out:** this style deliberately breaks 1of10's "text under 10 characters and under 7% of the image" pattern: the words cover about a fifth of the frame. That is why it must be tested against a smaller-number variant. Pick a surprising number that is **not** a death toll. WSDOT measured 42 mph at 9:30 a.m.; the twisting began about 10:03: "42 mph" is a gale, so never write "light wind". The exact cause is still debated (torsional flutter is the usual explanation).
- **Prompt:** *A suspension bridge with two tall brown towers, thin cables and vertical hangers; the roadway is a ribbon twisting in the air, its face red and its underside brown; green hills, dark green water, a small worried stick figure with hands on head on a light green mound. Sky blue background with two clouds; the left 40% of the frame is calm and empty.* + master block.
- **Also fits:** Blackout ("50 MILLION"), Challenger ("36°F"), Banqiao, any story with a good non-casualty number.

#### Style 7 — The Odd True Detail
*Two or three figures doing something odd that is documented, in a lit scene, with a two-word tease. This is Ink Explainer's format.*

- **Example:** Challenger, 1986 (the televised demonstration). Draft title: *Why did a rubber ring destroy a space shuttle?* Words: **ICE WATER**. Image: a hearing-room table with a glass of ice water and a clamped red rubber ring, three anonymous figures behind it.
- **Why it should work:** Ink Explainer's six top thumbnails all share this recipe: a full scene, one to three stick figures, and two or three words that tease the answer without repeating the title (e.g. "NO JOBS", 9.7M, 49_Ph2q6uIM; 106K subscribers) [B]. The same template gave very different results on clone channels, so the *idea* carries it, not the template. Three figures respect the Netflix limit.
- **Layout:** figures behind a long table; the two hero props (glass, ring) at the left, clear of the words; window at the right for light.
- **Watch out:** the demonstration was on 11 Feb 1986 (Rogers Commission Vol. 4 transcript; the quote was seen through a search summary): keep the figures anonymous and do not name or caricature the real people. The glass and ring are small at 168 px: the words carry the style there.
- **Prompt:** *A hearing room with a tan wall and a window: a long cream table with a dark green front; on the table a large glass of ice water with three white ice cubes and, beside it, a red rubber ring held in a small black clamp; behind the table three stick figures, two calm and one worried, looking at the ring.* + master block.
- **Also fits:** Tacoma's lemon-chewing workmen (documented by WSDOT), Vasa's stability test, Piper Alpha's permit boxes.

#### Style 8 — The Crowd on the Shore
*The viewer sees the flaw while the calm crowd watches. The flaw is red.*

- **Example:** Vasa, 1628. Draft title: *Why did a brand-new warship sink in front of its own crowd?* Words: **CALM DAY**. Image: the grand ship upright with its lower gunports open (red) just above the waves, three calm figures on the shore.
- **Why it should work:** dramatic irony is the brief's core promise ("the viewer sees how they would have made the same call"). Storified's bus-heading-to-a-broken-bridge thumbnail is a cousin (613K, 0QXvhtPaKoY) [B]. Three figures respect the Netflix limit.
- **Layout:** the ship is the horizontal mass on the right; the crowd sits small on the left; words in the sky.
- **Watch out:** do not claim "nobody noticed": a stability test was stopped shortly before, so someone did. The style is about the *spectators'* view. The sources for the day and the wind are secondary: one says a calm day with a light breeze, then a gust, then a stronger gust; check the Vasa Museum. The red ports are small at 168 px, so the words carry the style there.
- **Prompt:** *A tall wooden warship with three masts and cream square sails floating in dark green water, a high curved stern, a row of black gunports on the brown hull and a lower row of open red gunports just above small cream waves; on the left a tan shore with three calm stick figures and a few small brown buildings behind them. Sky blue background, two clouds.* + master block.
- **Also fits:** Tacoma's drivers, Titanic-type stories, the Hyatt atrium before the collapse (empty).

#### Style 9 — Seat of the Decider
*The viewer sits in the control room and sees what the operator does not.*

- **Example:** the 2003 Northeast Blackout. Draft title: *Why did a dead alarm help black out 50 million people?* Words: **LAST ALARM / 2:14 PM**. Image: a calm operator (front view, eyes toward the screens) at a console, one working screen and one frozen screen with a red frame; through the window a power line still clear of a tree.
- **Why it should work:** it is the brief's speech pattern #1 (second person, the viewer in the seat) as a picture; none of the roughly 105 disaster-niche thumbnails inspected by eye showed a decision room; cartoon channels use a single figure with props in a room (StickFigure Explains, 4.5M, Yh_7y2PYH1o; easy, actually, 9.7M, C5OJJD3Eytk) [B].
- **Layout:** the figure calm, the frozen screen red-framed, the window at the right; words top-left, clear of the window.
- **Watch out:** the timeline must stay separate: the Task Force report says the alarm software failed "shortly after 14:14 EDT" (the last valid alarm), while lines touched trees from about 15:05, so the picture shows the line still clear of the tree. The four cause groups in the report include much more than the alarm, and the title says "help black out". Do not draw a ringing phone: it is not documented. The figure is a front view with a gaze shift (no side view needed).
- **Prompt:** *A bright control room with a tan wall and brown floor: a calm stick figure sits behind a cream console desk, looking to the left at two monitors, one with a blue screen and white bars, the other with a blank cream screen in a thick red frame; on the right a window showing a green tree under a power line that droops but does not touch it.* + master block.
- **Also fits:** Challenger's teleconference, Piper Alpha's control room, Big Dig's inspection office.

#### Style 10 — Close-Up Gaze
*A huge worried face looks sideways at the hazard. The hazard is red.*

- **Example:** Flixborough, 1974. Draft title: *Why did one bypass pipe blow up a whole chemical plant?* Words: **NO DRAWING**. Image: a head filling the left of the frame, eyes shifted toward two tan reactors joined by a red dog-legged bypass over the empty stand where a third reactor had been.
- **Why it should work:** it passed every phone-size test, including blur. The nearest real precedent: The Hydraulic Record puts the same worried presenter looking toward the hazard on the six of its thumbnails that were viewed (25K subscribers; 2M and 1M views on two recent videos; the Oroville example, mwwdnfaNKxk, has 132K) [B, causation unverified]. Netflix: complex emotion beats stoic [B]. A figure looking at the object shifts attention and recall to it (Sajjacholapunt & Ball 2014; real faces on banner ads [A]). Schematic faces still read emotion (Kendall 2016 [A]). MrBeast's team reported a small benefit from a closed mouth [B].
- **Layout:** head at least 25% of the frame height (mockup: about 55%); eyes shifted 20% toward the hazard; brows angled up in the middle; hazard in the right third; words in the sky.
- **Watch out:** two-dot eyes with no eye whites are **untested** for fear signals (Whalen 2004 concerns real eye whites [A]); test a subtle "worried" version against an open-mouth one. HSE's page says "bypass" (not "temporary"); it says no drawing and no calculations existed for the dog-leg or the bellows. Its statement that the bypass failure "may have been caused by" a fire on a nearby 8-inch pipe means the cause is contested: the red pipe marks the *modification*, not a proven cause, and the video must say so.
- **Prompt:** *A single huge round white stick-figure head filling the left third of the frame with a worried face, two black dot eyes shifted to the right, eyebrows angled up in the middle, small downturned mouth; on the right two tan chemical reactors with an empty tan stand between them, joined by a thick red zig-zag pipe with cream accordion joints; green ground, sky blue background.* + master block.
- **Also fits:** any story with one visible defect: Quebec's bowed chord, Big Dig's anchor, Tacoma's cable band.

### C6. Comparison and phone-size results

`thumbnails/qa-phone-sizes.png` shows each style at 360 px and 168 px on the light feed, 168 px on the dark feed, in grayscale and blurred. My reading (a visual check, not a human study):

| # | Style | Words | At 168 px | Fit to any story | Main risk |
|---|---|---|---|---|---|
| 1 | Tiny Under the Giant | 2 | words and red slab read; dam and wave are small | high | figure size; dam profile |
| 2 | The Moment Before | 0 | bridge and red chord read clearly | **high** | the wrong detail must be central |
| 3 | The Impossible Scene | 0 | airliner in a tank reads; figures vanish | low (needs a true odd image) | must be true |
| 4 | Exhibit A | 2 | words and red nut read | medium | half the cause only |
| 5 | The Cutaway | 1 | red anchors read; figure is tiny | medium | drawing difficulty |
| 6 | The Giant Number | 1 | **strongest**; number survives blur | medium (needs a good number) | breaks the "<7% text" pattern |
| 7 | The Odd True Detail | 2 | words carry it; props are tiny | low-medium (needs an odd true detail) | real-person depiction |
| 8 | The Crowd on the Shore | 2 | words carry it; red ports vanish | low-medium | small flaw at phone size |
| 9 | Seat of the Decider | 2 | words carry it; scene is small | medium | timeline; small scene |
| 10 | Close-Up Gaze | 2 | **strongest**; survives blur | **high** | dot-eye fear untested |

**Which styles are close cousins** (do not put them in the same test): 1 and 8 (big object plus small figures), 4 and 5 (a small part shown huge), 2, 8 and 9 (a calm scene plus a hidden cause). **Suggested test trios:** one *human* style (10, 7 or 9), one *mechanism* style (4 or 5) and one *scale/scene* style (1, 2, 3 or 8), never two cousins together (9 goes with 1 or 3, not with 2 or 8). Alternate background families across consecutive videos.

**Style × story type** (my judgment, not tested):

| Story type | Best | Also good |
|---|---|---|
| Dam, flood, slope | 1 | 2, 6, 10 |
| Bridge (collapse, flutter) | 6, 2 | 1, 7, 10 |
| Building, walkway | 4 | 2, 5 |
| Aircraft | 3, 5 | 10, 4 |
| Rocket, spacecraft | 7, 4 | 2, 9 |
| Plant, offshore, industrial | 10, 4 | 5, 9 |
| Tunnel, mine | 5, 2 | 10, 1 |
| Control system, software, blackout | 9, 6 | 2, 10 |
| Failed product, invention | 4, 10 | 7, 3 |
| "Nothing broke but it failed" | 8, 3 | 2, 7 |

### C7. Testing playbook

- **Use Test & Compare** on every long-form video: up to 3 variants, desktop Studio, winner by watch-time share, up to 2 weeks. Upload your preferred variant **first**: if the result is inconclusive, the first upload stays. Outcomes are Winner, Performed Same and Inconclusive; YouTube says it is normal not to get a winner. Editing the title or thumbnail during a test stops it. Do **not** swap thumbnails by hand and compare: early viewers are your fans and the traffic-source mix distorts CTR.
- **Test concepts, not tweaks.** Sample size per variant for 80% power at 5% significance, CTR only (my arithmetic with the standard two-proportion formula; the real tool uses watch-time share, so treat as indicative): 4% → 8%: about 550; 4% → 6%: about 1,860; 4% → 5%: about 6,700 (6,745 exactly); 4% → 4.8%: about 10,300. Three variants triple the total.
- **Cadence.** Run a test at publish (core audience), read it at 48–72 hours, and re-test older videos with a new concept if the topic is evergreen. Re-testing after 72+ hours matches official guidance [A].
- **Log every video:** style, overlay words, CTR by traffic source, average view duration, test outcome. After 8–10 videos look for patterns across videos: single tests will rarely reach significance at small volumes.
- **Never judge CTR alone.** YouTube says clickbait shows as high CTR with low average view duration. If CTR rises and average view duration falls, the thumbnail over-promised.
- **Decision rules (my heuristics [C], not from a source):** do not touch anything for 48 hours; "Winner" means adopt it; "Performed Same" means keep your favorite and log it; "Inconclusive" means accept the default; consider a manual swap only if after about 5,000 impressions CTR is under 70% of your own same-source baseline and average view duration is healthy, and then change the whole concept.
- **Title–thumbnail pairing** (Galloway, Ritchie, the MrBeast memo, YouTube staff [B]): plan the title and thumbnail before recording. The thumbnail must add what the title does not, must not repeat its first ~40 characters, and everything it promises must be visible or explained by second 15 (your outcome-first opening already enforces this). Keep your question titles, but make them concrete (a named object or a number) so they do not read as vague; the evidence on questions is mixed and comes from headlines. Note that several draft titles here have their key idea after character 40 (for example titles 3, 6 and 9): shorten them before publishing if you want the hook to survive truncation.
- **Per-thumbnail QA** (run `tools/thumb_preview.py`): 1) squint (blur): the accent, main word and silhouette survive; 2) phone size: main word cap height at least 90 px on the master; 3) grayscale: word vs background lightness gap at least 50 (the ink outline carries white words on pale colors), figure vs background at least 25; 4) light and dark feed: image edges do not dissolve; 5) color-blind: red never on green or brown; 6) badge zone free of anything important; 7) zoom to 100% and look for stray letters or numbers on signs, gauges and clocks, and for hands, shoes or thick limbs; 8) 3 words or fewer; 9) export sRGB, 16:9, under 2 MB.

### C8. Registry of facts used in the examples

Every fact shown in a mockup or title, with its source and the confidence of that source. The channel rule is "nothing invented": **re-verify each against the primary report before publishing.** Detailed quotes are in `research/story-visuals.md`.

| Story | Fact used | Primary source read? | Confidence |
|---|---|---|---|
| Vajont, 1963 | 1,917 dead (Italian Civil Protection), other counts 1,919–2,056, so "about 1,900"; the 262 m dam stayed standing; the slope slid, not the dam | secondary (Civil Protection page, ASDSO, Fondazione Vajont) | [B] |
| Quebec Bridge, 1907 | Bent lower chords were noticed before the collapse; no numbers used; the drawing is illustrative | Wikipedia-level; Royal Commission report not read | [C] |
| Comet, 1954 | Whole fuselage tested in a water tank with the wings out through seals; the tank-test crack began at the forward port escape hatch (Withey); the Elba failure began at a bolt hole near the roof ADF antenna cut-out; the passenger windows were rectangles with rounded corners and were not the cause | Withey 1997 paper and Aerossurance; the Cohen inquiry report (CAP 127) was not opened | [B/C] |
| Hyatt Regency, 1981 | NBS gives two causes: the original continuous-rod detail would not have met code (about 60% of capacity), and the as-built change "essentially doubled" the load on the fourth-floor connection; 113 dead; the box beam is a pair of welded 8-inch channels resting on washers and nuts | **NBS report read** | [A] |
| Big Dig, 2006 | About 26 tons fell on 10 July 2006 at 11:01 pm; cause: epoxy with poor creep resistance (the anchor slowly let go); number of anchors in the picture is illustrative | **NTSB HAR-07/02 read** | [A] |
| Tacoma Narrows, 1940 | Opened 1 July, collapsed 7 Nov: four months; wind 42 mph measured at 9:30 a.m., twisting began 10:03; WSDOT says the cause "remains a mystery" with torsional flutter the primary explanation; the textbook "resonance" account is disputed (Billah & Scanlan 1991, not fetched here) | **WSDOT history read** | [A] |
| Challenger, 1986 | Air temperature 36°F at launch, 15°F colder than any earlier launch; Thiokol engineers advised against launching below 53°F; the televised ice-water demonstration was 11 Feb 1986 (Rogers Vol. 4) | **Rogers Commission Vol. 1 read**; the Vol. 4 quote seen through a search summary | [A] |
| Vasa, 1628 | Sank on the maiden voyage after about 1,300 m; lower gunports open; a calm day, a light breeze, then gusts (sources differ); a stability test had been stopped earlier | secondary; the museum page returned 404 | [C] |
| 2003 Blackout | About 50 million people; the alarm and logging software failed "shortly after 14:14 EDT" (the last valid alarm) and stayed dead; overgrown trees tripped lines from about 15:05; the report lists four cause groups | **Task Force final report read** | [A] |
| Flixborough, 1974 | HSE: a 20-inch bypass; no drawing of the modification, no calculations for the dog-leg or bellows, no pressure test; the failure "may have been caused by" a nearby 8-inch pipe fire (contested) | **HSE page read** | [A] |

**Dropped by the legal filter (searched 2026-09-30):** Morandi Bridge (verdict 16 July 2026, appeal announced), Boeing 737 MAX (civil trials continue), Grenfell (charging decisions pending, trials 2029 or later). Lac-Mégantic is borderline (sources conflict on the year of the Supreme Court decision): not used. Not verified in this research pass: Chernobyl, Three Mile Island, Apollo 13, Columbia, Mars Climate Orbiter, Millennium Bridge, St. Francis Dam, Sleipner, Ronan Point, Tay Bridge, Kaprun, Sampoong, Banqiao, Therac-25, and the Titan submersible and Baltimore Key Bridge (the last two were not checked at all). Piper Alpha and the Note 7 were researched at lower confidence (secondary sources; the Cullen Report and Samsung's findings were not opened). Several of these appear under "Also fits" only as suggestions.

**Myths to avoid when drawing or writing:** Comet's "square windows"; Tacoma's "resonance" and "a light wind"; the Vasa "king added a deck" story (no evidence); Quebec's "Iron Rings from the wreckage" (no support found); Piper Alpha blamed on the two workers named by the court.

### C9. Decisions I need from you

1. **Text on thumbnails.** The brief bans text inside images, but about 70% of the thumbnails inspected in the niche (75 of about 105; median 3–4 words, max 7) and all of Ink Explainer's top videos carry two or three words. I assumed the words are a separate overlay layer in Figma, Canva or Photopea, never in the generated image; the `art-only/` files show the generated layer. Confirm, or tell me to make all ten wordless.
2. **Plain paper (Style 4).** The brief bans an "empty flat background" but allows beat drawings and text cards on plain flat paper. Style 4 is a plain paper card with an ink frame. Confirm it counts as a beat drawing.
3. **The character sheet.** There is none in the brief. Ink Explainer's figures have circle eyes with lids; yours have dot eyes. Approve dot eyes with a *gaze shift* toward the hazard, and a *very large head* for Style 10.
4. **Numbers on thumbnails.** I used only non-casualty numbers (mph, tons, a time of day). Should a death toll ever appear as a hook, given "state casualties factually and move on"? I recommend no.

### C10. Shorts

- The Shorts feed plays the video without showing a thumbnail; covers appear on the channel page, in search and on the homepage [B/C: search is our own JSON check; the rest is secondary]. A custom cover can only be set on a computer in Studio, is rolling out (Partner Program creators first; the Help page says "verified account": check which applies to your channel), and there is **no A/B testing for Shorts** [A].
- Covers are 9:16 (2160×3840). Keep everything important inside a central 2:3 crop [B].
- The first-frame equivalent of a thumbnail is **frame 0 to 1 s**: the outcome image plus a 3–6 word line (matches the brief's "outcome within the first 3 seconds"). Styles that translate best to vertical: 6 (Giant Number), 10 (Close-Up Gaze), 4 (Exhibit A).
- "99.9% of Shorts views come from the feed" is a creator remark, misattributed online: do not rely on it.

### C11. Caveats

- No CTR or impression data exists outside your own Studio, so every "should work" is an inference from view counts, lab attention studies and headline experiments. Views depend on video age, topic and channel size: I compared only within a channel and only as patterns. Several cited view counts are cumulative over many years.
- Several sources could not be opened (YouTube watch pages and transcripts, vidIQ's study page, ScienceDirect, Springer, ACM). Those findings rest on abstracts or secondary reports and are marked as such in `research/`.
- Beaupré's and Ritchie's statements come through Search Engine Journal and ppc.land, not the original videos. The MrBeast production memo is unauthenticated.
- The saliency and OCR checks in the design report are proxies, not human studies. The duration-badge geometry is approximate.
- The mockups are vector art, not generated images: real generated images will differ, and you must check every one for stray letters and numbers. Several drawings simplify the real objects (see each style's watch-out).
- About 300 of the 405 niche thumbnails were measured programmatically but not visually inspected. The counts "about 105 inspected by eye", "75 with text" and "about 300 cartoon thumbnails inspected" come from the agents' reports, not from their saved notes.

### C12. Files

- `thumbnail-lookbook.html`: all ten mockups, the phone-size test, and the comparison in one page (Slovenian captions).
- `thumbnails/`: the ten composites, `art-only/` layers, editable `svg/`, and `qa-phone-sizes.png`.
- `tools/`: `thumb_preview.py` (feed preview rig: light and dark feed, several sizes, badge, grayscale, blur, safe zones; usage `python3 thumb_preview.py image.png --title "..." --duration 10:24 --safezone`, needs Pillow) and the mockup generator (`scenes.py`, `lib.py`, `render.py`, `fonts/`; rendering needs a headless Chromium).
- `research/*.md`: the eight research agents' notes with URLs, quotes and evidence grades: `platform`, `ctr-evidence`, `psychology`, `niche-audit`, `cartoon-audit`, `design-system` (and `design-system-palette-pairs`), `packaging`, `story-visuals`.

## B. Synthesis: key numbers, myths, contradictions, recommendations, roadmap, risks

This part gathers, in one place, everything the research established: the context and method, the key numbers, the myths and contradictions, and every recommendation. It is written to be read straight through. Part C has the ten styles in full; Part D holds the underlying reports and Part F the data tables (raw notes, reviews and indexes are not in this edition: see 0.4). When a statement here needs more detail, the "Where" column or the closing reference in each section names the chapter.

**Evidence grades used everywhere:** **[A]** official documentation, peer-reviewed study, or a large dataset; **[B]** first-hand data from a creator or company, a correlational dataset, or a measurement by one of our agents; **[C]** opinion, vendor blog, or inference. **UNVERIFIED** means the agent could not confirm it. Rounded view counts are as listed by YouTube on 2026-09-30.

### B1. Context, constraints and method

#### B1.1 The question

The channel owner runs a new YouTube channel, **Stress Riser** (documentary-style stories of engineering disasters and failed inventions, told as a chain of small, reasonable decisions; English voiceover; hand-drawn stick-figure animation; viewers 18–50 in the US, UK, Canada and Australia, mostly on a phone). The request was to launch as many agents as needed, research in detail and with precision, and deliver **10 different thumbnail styles and approaches that suit the videos, would work well and have a high click-through rate**, with as much time as needed. A later request (this file) was to put **all the data, all the recommendations and everything learned in one very extensive file**.

#### B1.2 What in the brief shaped the thumbnails

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

#### B1.3 Observations about the brief itself

These are points where the brief is silent, ambiguous or internally inconsistent. They were handled by explicit assumptions and are listed so the owner can confirm them.

1. **No character sheet exists.** The brief says every person is a stick figure "exactly as on their character sheet", but no sheet is given. Each story needs one (front view, three expressions, prop). The closest real reference, Ink Explainer, draws circle eyes with lids; the brief specifies dot eyes.
2. **Text in images versus text on thumbnails.** The brief bans text and numbers in images, yet its own pacing rule uses "a text card, a label" on screen, and about 70% of niche thumbnails carry words. Assumption: thumbnail words are a **separate overlay layer** added in a design tool; the generated image never contains letters.
3. **Plain paper.** The brief bans an "empty flat background" but allows beat drawings and text cards on plain flat paper. Assumption: one style (Exhibit A) is a plain paper card with an ink frame.
4. **Spelling.** The rule says American spelling ("meters"), but several examples inside the brief use "metres" and "humour". Assumption: output uses American spelling; the examples show only the shape.
5. **The "two years old" rule moves with the date.** On 2026-10-01 a disaster from before about 2024-10-01 qualifies; the cutoff must be recomputed on each publication date.
6. **"Every title is a question"** is firm, but the evidence on questions in headlines is mixed (see B2.3). The fix is to make questions concrete and let the thumbnail carry the specific stakes.
7. **Forbidden-topic overlap with the best-known stories.** Several famous cases fail the filter today (Morandi Bridge: first-instance verdict 16 July 2026, appeal announced; Boeing 737 MAX: civil trials continue; Grenfell: charging decisions pending, trials 2029 or later). Lac-Mégantic is borderline.
8. **The brief's own examples all point to Vajont** (1,900 people, 270 million cubic metres, Edoardo Semenza, a dam that never broke). It is a natural first story, but the brief says of its own examples that each "shows the shape, never copy it".

#### B1.4 Method

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

#### B1.5 Access limits (what could not be read)

- YouTube watch pages and transcripts were bot-gated: the Veritasium, Kurzgesagt, Colin and Samir and Jon Youshaei talks were not read; their points are secondary or absent.
- vidIQ's study page, ScienceDirect, Springer, ACM and Medium were blocked: those findings rest on abstracts or secondary summaries.
- Rene Ritchie's and Todd Beaupré's statements come through Search Engine Journal and ppc.land, not the original videos. The MrBeast production memo is unauthenticated.
- The official Comet inquiry report (CAP 127) and the Cullen Report on Piper Alpha were not opened; the Quebec Royal Commission report was not read; the Vasa Museum page returned 404.
- No source gives official pixel sizes for native phone apps or TV, or an official safe-zone map.
- The Team YouTube thread on the mobile-feed crop experiment is rendered by script and could not be re-opened by the reviewer.

*For detail see Appendix G (raw notes) and Part D (final reports).*

### B2. Key numbers and facts, in one place

Most rows say what was measured, the grade and where to read more (a chapter in Part D or an appendix). The tables in B2.4, B2.5 and B2.7 have no grade column: their rows are counts, measurements and arithmetic by our own agents ([B]) unless a grade is shown inline, and the lower-confidence stories carry [C]. Nothing here is new beyond the reports; it is a consolidated ledger. Where reports disagree, see B3.

#### B2.1 Platform: specs, display, measurement, testing, policy

| Fact | Value | Grade | Where |
|---|---|---|---|
| Official thumbnail spec | 16:9; recommended 3840×2160; minimum width 640 px; JPG or PNG; Shorts 2160×3840 (9:16), minimum height 640 px | [A] YouTube Help 72431 | D1 |
| Upload size limit | 2 MB from a phone, 50 MB from desktop (limit change reported Oct 2025) | [A] Help; [B] 9to5google 2025-10-30 | D1 |
| The old "1280×720, under 2 MB" rule | Out of date on the official page, still repeated by third-party sites | [A] | D1, D6 |
| What YouTube serves | 1280×720, 4:2:0 JPEG, about quality 90 (72–367 KB across 20 samples) | [B] measured by the design agent, 2026-09-30 | D6 |
| Desktop search tile | 360×202 (720×404 for high-DPI) | [B] measured | D1, D6 |
| Watch-page sidebar tile | 168×94 (336×188); sometimes 196×110 or 246×138 | [B] measured | D6 |
| Mobile web | requests up to 686×386 (2×343 CSS px) | [B] measured | D6 |
| Desktop home card width | 310–500 px (from YouTube's skeleton CSS) | [B] measured | D6 |
| Page backgrounds | #ffffff (light), #0f0f0f (dark) | [B] read from YouTube's CSS | D6 |
| Phone widths in US, UK, CA, AU | 414 px most common (21–30%), then 390 (12–14%), then 393, 402, 375, 360 (StatCounter, Aug 2026) | [B] | D6 |
| Native app card sizes, TV sizes | not found; official safe-zone map not found | UNVERIFIED | D1, D6 |
| Duration badge | bottom-right; red progress bar along the bottom for watched videos; desktop hover icons top-right | [B] YouTube via SEJ; geometry unverified | D1 |
| Impression counted when | thumbnail on screen more than 1 second with at least 50% visible; counted on apps, TV, Search, Home, feeds, Up Next, playlists | [A] Help | D1 |
| Impression not counted on | mobile website, YouTube Kids, YouTube Music, external embeds, cards, end screens, email, notifications | [A] Help | D1 |
| Mobile Home experiment | YouTube varies thumbnail and video sizes; "some thumbnails may appear cropped" | [A] Team YouTube 2026-04-29 (the page is script-rendered; the reviewer could not re-open it, so the wording rests on the agent's reading) | D1 |
| CTR definition | "how often viewers watched a video after seeing a thumbnail"; tells "how eye-catching your video idea or 'packaging' is" | [A] Help 7628154, 16767369 | D1 |
| CTR benchmark | "Half of all channels and videos … between 2% and 10%"; wider for new videos or fewer than 100 views; not a target | [A] Help | D1 |
| Why CTR varies | falls as reach widens (Help's example: 9% on 10,000 impressions to 3.5% on 100,000); search: fewer impressions, higher CTR; home: high volume, lower CTR; early CTR inflated by loyal fans | [A] Help | D1 |
| Subscribers' feed CTR | "probably … 10% or less"; "90% of the time your subscribed audience isn't deciding" | [B] Beaupré 2026-09-01 via ppc.land (one secondary source; no sample or method given) | D1, D8 |
| What YouTube optimizes | "long-term viewer satisfaction"; signals: clicks, watch time, survey responses, sharing, likes, dislikes; "No metric on its own is a good indicator of value" | [A] Help 141805, Goodrow 2021; [B] Beaupré | D1 |
| Clickbait signature | high CTR with low average view duration and lower-than-expected impressions | [A] Help | D1 |
| Test & Compare | up to 3 variants (titles, thumbnails or both); long-form only; desktop Studio; ends at significance or up to 2 weeks; outcomes Winner, Performed Same, Inconclusive; judged by **watch-time share**, not CTR | [A] Help 16391400 | D1 |
| Test & Compare details | first uploaded variant becomes default if no winner; small control group; excluded: Shorts, Premieres, made-for-kids, private, age-restricted; editing mid-test stops it; any variant under 720p makes all downscale to 480p | [A] Help | D1 |
| Official testing advice | test bigger differences first (layouts, image elements); run at launch and again 72+ hours later; be patient; test older videos first; similar variants take longer | [A] Help | D1 |
| Scale of testing | more than 40 million experiments since 2024 | [A] Made on YouTube blog, 2026-09 | D1 |
| New testing features (2026-09-23) | "dynamic thumbnails" (best of three per audience segment), cut testing "coming soon", an Ask Studio agent | [B/C] via ppc.land, TechCrunch | D1 |
| Metric name for tests | Help: "watch time share"; SEJ, ppc.land: "watch time per impression"; formula unpublished | UNVERIFIED which | D1 |
| Thumbnails policy | forbidden: thumbnails that mislead; "violent imagery that intends to shock or disgust"; blood or gore | [A] Help 9229980 | D1 |
| Penalties | usually a warning first; later a strike (3 in 90 days risks termination); repeat violations can remove custom thumbnails for 30 days | [A] Help | D1 |
| Animation | YouTube "make[s] a distinction between dramatized violence featuring real human actors and content featuring animations" | [A] Help 2802008 | D1 |
| Advertiser-friendly rules | apply to thumbnail, title, description, tags; full ads: tragedies with limited display, building collapses, implied death in documentary context; limited ads: disaster footage with visible harm or extreme distress; no ads: gore, heavy blood, severe agony, and content that profits from a sensitive event | [A] Help 6162278 | D1 |
| Real victims | not allowed: content "reveling in or mocking the death or serious injury of an identifiable individual" (the Help text). "Avoid company logos" is D1's inference from trademark enforcement, not Help wording | [A] Help 2802268; [C] the logo point | D1 |
| Originality | not monetizable: "AI-generated content made with generic or unoriginal templates"; "repeatedly uses disturbing themes (such as violence or loss) without building a cohesive narrative"; the repetitive-content wording is about "giving the impression of mass production without adding the creator's original, authentic insights or perspective" (full wording from reviewer 1's live check); allowed: the same intro and outro with different substance. "A house style is fine" is my reading, not YouTube's words | [A] Help 1311392 | D1 |
| AI disclosure | not needed for clearly non-realistic or animated content; the rules list AI help with a thumbnail among exempt uses; realistic fake events need it; labels added automatically for YouTube's own AI tools and C2PA metadata | [A] Help 14328491 | D1 |
| Shorts covers | custom cover on desktop Studio only; verified account (Help) vs Partner Program first (blog 2026-07-24); no A/B testing for Shorts | [A] | D1, D8 |
| Shorts feed | plays the video, no thumbnail shown; covers appear on channel page, homepage, search | [B/C]: search is our own JSON check; the homepage and channel-page part is secondary (Ritchie via ppc.land); no official page confirms it (D8) | D1, D8 |
| Shorts crop | search serves 405×720 (9:16) and 405×608 (2:3) variants; advice: key content inside a central 2:3 crop | [B] measured; [C] Ritchie via ppc.land | D1 |

#### B2.2 CTR evidence: datasets, company data and creator experiments

| Fact | Value | Grade | Where |
|---|---|---|---|
| 1of10 dataset | 300K+ high-performing 2025 videos, 62.6B views, 52K channels; metric is outlier score (views ÷ channel median), not CTR | [B] correlational | D2 |
| Faces (1of10) | face vs no face about the same overall; multiple faces beat a single face; faces help mainly channels above 200K subscribers; help lifestyle, finance, beauty; hurt health and fitness, movies and TV | [B] | D2 |
| Text (1of10) | 84% of thumbnails have text; those got about 19% fewer views; best: no text, or under 10 characters covering under 7% of the image | [B] | D2 |
| Color (1of10) | cyan about +36% views; green and yellow/orange do well; views rise with brightness; dark thumbnails underperform (units of the "100–110" brightness peak undefined) | [B] | D2 |
| Educational vs entertainment (1of10) | entertainment about 44% more median views than educational | [B] | D2 |
| Titles (1of10) | titles with numbers about 11% fewer views on average; negative titles about 22% more than positive | [B] | D2 |
| vidIQ 2026 | 500 breakout long-form videos across 30 niches; face in 69% (75% of top 100, 80% of top 50); high contrast 56%; face or high contrast 89%; overlay text 72%, median 5 words; exaggerated expression about 5%; no base rate | [B] (study page blocked; via secondary summary) | D2 |
| Netflix artwork tests | faces with complex emotion beat stoic; villains beat heroes in kids and action; win rates "dramatically dropped" above 3 people; 2014 research: artwork biggest driver, over 82% of browsing focus; about 1.8 seconds per title | [B] company data, films | D2 |
| MrBeast | closing the mouth raised watch time "on every video"; lead: about 30 videos, "a small difference"; "easy to understand", design for small size, consistent face and colors | [B] (memo unauthenticated) | D2 |
| Cui et al. 2024 | 16,215 covers: strong sentiment in the thumbnail, positive or negative, raises views; strong sentiment in caption text lowers views; positive titles beat negative (contradicts 1of10) | [A] observational, J. Business Research 183:114849 | D2 |
| Fang et al. 2026 | 22,958 thumbnails and two experiments: visual complexity has an inverted-U relation with popularity; stronger for utilitarian videos (platform not verified as YouTube) | [A] J. Academy of Marketing Science | D2 |
| Koh and Cui 2022 | 3,745 branded videos: coherent colorfulness and brightness work best, with moderate image quality (abstract only) | [A] | D2 |
| Attention studies | faces and text draw gaze 16.6× and 11.1× more than matched regions (Cerf 2009); thumbnails got about 2× the attention of titles (ETRA 2018) | [A] attention, not clicks | D2 |
| Google ranking paper | "Ranking by click-through rate often promotes deceptive videos that the user does not complete ('clickbait')"; ranks by expected watch time (2016) | [A] Covington, Adams, Sargin | D2 |
| Veritasium | adding "What can we do?" to a title did not help; a big thumbnail change with a simpler title made a 10M+ video; "legitbait" vs "clicktraps" | [B] secondary summary | D2 |
| Ali Abdaal | a rushed thumbnail replaced after an A/B test showed "much higher" CTR; video reached almost 1M views; no numbers published | [B] secondary | D2 |
| OverseerOS | 16,152 million-view videos: 25% no thumbnail text; about 75% of text-bearing ones do not mostly repeat the title; 891 matched question vs statement pairs: 445 vs 446; only 6.8% of million-view titles contain "?" | [C] vendor, survivors only | D2 |
| No published numbers for | Mark Rober, D'Avella, Kurzgesagt, Wendover, Real Engineering, Practical Engineering, Polymatter, Johnny Harris, Vox | not found | D2 |
| Existence proofs for cartoon thumbnails | Ink Explainer: faceless stick-figure channel, 106K subscribers on its channel page (2026-09-30; a third-party case study says 77.8K "at month 8", which does not fit "first video about 5 months ago": see B3.2 #22), one video 9.7M views; The Infographics Show "AMERICA CLOSED" 2.5M in 2 weeks; Kurzgesagt 10–20M on latest uploads | [C] | D2 |

#### B2.3 Psychology and perception: findings and principles

| Finding | Grade | Source |
|---|---|---|
| Curiosity peaks at a **medium** information gap (confidence about 0.45–0.55), not a maximal one | [A] | Kang 2009 |
| In 8,977 headline tests (headline plus image), more concrete wording raised CTR when the baseline was too vague and lowered it when too concrete | [A] | Le Quéré and Matias 2025 |
| A moderate knowledge gap raised the chance of reading; full knowledge lowered it | [A] | Frede 2026 |
| Question-framed headlines reduced engagement on average (22,743 news tests, 53,030 Reddit posts, a 400-person lab study; written headlines, not YouTube) | [A] | Fang and Wheeler 2026 |
| Earlier question-headline work is mixed (3 of 9 experiments negative, 2 positive, 4 null) | [A] | Le Quéré table |
| When meaning and salience are separated, only meaning explains unique variance in gaze | [A] | Henderson and Hayes 2017 |
| Clutter, including color variability, hurts visual search | [A] | Rosenholtz 2007 |
| More cartoonised faces let people identify emotion more accurately at short exposures (high contrast and low feature complexity helped) | [A] | Kendall 2016 |
| Upright emoticons drive a face-type neural signal (n=20) | [A] | Churches 2014 |
| Schematic threat faces were found faster than friendly ones; later work found no angry pop-out and a happy advantage | [A] contested | Öhman 2001; Becker 2011 |
| Photographic faces capture saccades at 100–110 ms; schematic-face pop-out is doubtful | [A] | Crouzet 2010; Hershler and Hochstein 2005 |
| Averted gaze raised attention to the product and text and recall: recognised brands per person 1.50 (averted), 1.06 (mutual), 0.54 (no face); real faces on banner ads, n=72 | [A] | Sajjacholapunt and Ball 2014 |
| Pupil direction on a schematic face still cues attention | [A] (via summary) | Friesen and Kingstone 1998 |

**The 15 design principles** from the psychology report, each with its grade, and how to use it in a cartoon stick-figure disaster thumbnail:

| # | Principle | Evidence | How to use it |
|---|---|---|---|
| 1 | Middle-sized curiosity gap | Kang, Le Quéré, Frede [A] | Show the object and the stakes, not the failure mechanism |
| 2 | Curiosity raises retention | Gruber 2014 [A] | A gap the video closes in the first 10 seconds pays off the click |
| 3 | Picture first; large text is read early | ETRA 2018 [A-]; Rayner 2001 (print ads) [A] | Let the picture carry the idea; keep words to one large, short phrase |
| 4 | One dominant subject | Pieters and Wedel 2004 (1,363 print ads: the pictorial captures attention regardless of size, text in proportion to size) [A]. A reviewer noted this does not itself show that one dominant subject raises clicks; the stronger support is Netflix's three-person finding and the complexity studies | One figure or structure at least about a third of the frame |
| 5 | Sparse texture, meaningful design | Pieters, Wedel and Batra 2010 (249 ads) [A] | Flat color, few outlines, a composed scene with a clear story |
| 6 | Pop-out is relative contrast; saturation and brightness drive emotion more than hue | Wolfe and Horowitz; Rosenholtz; Valdez and Mehrabian 1994 [A] | One element differs from the rest: red or amber against a calm field |
| 7 | Gaze direction | Sajjacholapunt and Ball [A] | Put the eyes on the hazard: shift the dots, turn the head |
| 8 | Tension before the event | Loewenstein; Mobbs 2007 (a maze task, mechanism only) [A] | Show the moment before; the aftermath closes the gap; untested for thumbnails |
| 9 | Anomalies need a second look | Võ and Henderson 2009, 2011 [A]; Loftus and Mackworth 1978 said the opposite | Put the wrong thing where the eye already lands |
| 10 | Scale | Proulx 2010 [A] | Huge structure and tiny figure; the awe link for thumbnails is unverified |
| 11 | Negativity | Robertson 2023 (+2.3% CTR per extra negative headline word); Soroka 2019 [A] | Worried face plus a wrong structure; headline words, not images |
| 12 | Safe danger | Rozin 2013 [A] | A cartoon is the safe frame; no gore |
| 13 | Fluency | Reber, Schwarz, Winkielman 2004; Alter and Oppenheimer 2009 [A] | Clear silhouette, strong outline contrast |
| 14 | Center composition | Palmer 2008 (a preference study, not CTR) [A] | Center one subject; the rule of thirds is unsupported for single subjects |
| 15 | Familiarity is an inverted U | Montoya 2017 meta-analysis (268 curves, 81 articles); Anderson 2011 [A] | Keep a fixed identity element; rotate scene, emotion, color |

#### B2.4 Audits of real thumbnails: what the data show

**Niche audit (engineering disasters and documentaries).** 58 channel pages parsed (Latest and Popular sort); 405 thumbnails downloaded; about 105 classified by eye in nine 12-up sheets; about 300 only measured by script. View counts are as listed on 2026-09-30 and compared within a channel only (age and topic confound).

| Statistic | Value |
|---|---|
| Average brightness, 268 direct-niche thumbnails (0–1) | 0.43; near-white pixels 8%; dark pixels 21% |
| Cartoon-style channels (eight channels) | 0.52; near-white 20%; dark 15% |
| Top vs lowest-viewed thumbnails within 32 channels | mean differences brightness +0.012, saturation +0.004, edge density −0.002; the top thumbnail had "more" of a trait in only 12–19 of 32 channels (a coin flip) |
| Text among about 75 viewed thumbnails with text | median 3–4 words, maximum 7; usually top-left or right third; heavy condensed sans or gothic serif |
| Hard numbers as the hook | "62 DAMS GONE", "1,500 TONS OF TNT", "161 PEOPLE", "8,000 FEET DOWN" |
| Questions on the thumbnail | almost never (exceptions: "WHAT REALLY HAPPENED?", "WHAT WAS BOEING THINKING?", "Worst Recall in History?") |
| Faces | rare: only The Hydraulic Record (25K subscribers; 2M and 1M views on two recent videos) puts a worried presenter looking toward the hazard on every thumbnail viewed |
| The "moment before" | almost never shown; closest: Storified "26 PEOPLE" (613K) and The Infographics Show "Small Decisions That Caused HUGE Impacts" (957,455 views, 957K; search page) |
| Ink Explainer in this niche | 106K subscribers; "What Did Ancient Humans Actually Do All Day?" 9.7M views, a roughly 28× outlier against a median of about 340K for its top 14; style proven for prehistory, not yet for disasters |
| Tragedy handling | most show the structure or vehicle and no bodies; some state a casualty count as the hook; Storified is sensational ("IMPALED", "BRUTAL DEATH") yet has the biggest numbers on its channel (14M, 5.7M, 2.7M): sensationalism can get views (a correlation) but conflicts with the brief |

**The 13 formulas found in the niche** (full table with examples in D4): 1) two to four blunt heavy words over a full-bleed scene; 2) a worried face looking toward the hazard; 3) a giant one-word title over one lone object on plain sky or sea; 4) sepia or monochrome archive photo with gothic headline (photo-only); 5) red circle, arrow or dashed line (overused; the brief bans arrows and dashed lines); 6) cutaway or cross-section (translates well); 7) a tiny person for scale against something huge, or the moment just before; 8) a number as the hook; 9) gory dramatization with red arrows (avoid); 10) vehicle cut-out on a blue gradient with fire clip-art; 11) one object on plain light background with an accusatory caption; 12) an emotive cartoon character in a full scene with 2–3 words (native to your style); 13) "small thing, big outcome" split.

**Overused in the niche:** red circle and arrow, fire and explosion clip-art, all-caps condensed text, monochrome archival photos, brand corner logos, the intact-structure-on-water shot.

**Cartoon audit.** 52 channels, 462 rows, about 35 truly cartoon or illustrated, about 300 thumbnails viewed. Excluded from conclusions: Bobby Duke, Kaptain Kristian, Professor Of How, Yellow Dude, Fascinating Horror, Wendover, HowMoneyWorks.

| Finding | Value |
|---|---|
| Ink Explainer (real channel @Inkexplainer96) | 106K subscribers, 16 long videos; its top 6 all share: a full illustrated scene (cave, savanna, desert or snow), 1–3 stick figures (round white head, circle eyes with lids, single-line limbs, one costume as the only prop), 2–3 ALL-CAPS words in the top third (yellow or white, thick black outline) that tease the answer instead of repeating the question |
| Its weakest three | a white-background thumbnail (15K), a dark cave (37K), a crowded battle (42K); topic differs, so not a clean comparison |
| Clone channels | Explain In Paint, Zenn, Axen, HUMAN-ISH; HUMAN-ISH (4.2K subscribers) has one 548K video beside 4–12K videos on the identical layout |
| Metrics that did not separate top from weak | brightness, saturation, edge density, yellow, white and black share (44 channels; top beat weak in 17–29 of 44, a coin flip) |
| Phone test at 176 px | pale or white-background thumbnails lose their edge on the white feed; saturated full scenes keep a clear boundary in both modes; 1–3 words at about 30% of frame height stay legible; small labels and two-line text do not; figures under about 12% of frame height read only by posture |
| Lab study | cartoon faces get faster, larger early neural responses; real faces get more late attention (Zhao 2019, N=17; neural response, not clicks) [A] |
| V-shaped brow geometry | detected faster than upward (Larson 2007); only weak behavioural effects (Wang and Zhang 2016) [A] |
| No YouTube study was found that compares stick-figure or cartoon thumbnails with realistic ones on clicks | indirect evidence only: Zhao 2019 (neural response) and a December 2023 Journal of Advertising study of illustrated vs photographic public-service ads (donation clicks; not YouTube) |

#### B2.5 Design system numbers

| Fact | Value | Where |
|---|---|---|
| Palette lightness tiers (L*) | light: white 100, paper 93, sky 88, amber 75, tan 75, light green 72; mid: red 52, brown 49, dark green 48; dark: ink 9 | D6 |
| Rule of thumb | gap ≥ 50 text-safe (WCAG 4.5:1); 40–50 big bold text; 25–40 big flat shapes with an outline; < 25 invisible (hue only) | D6 |
| Universal outline | ink is at least 3:1 against every palette color (lowest: ink/dark green 3.59) | D6 |
| Strong pairs | ink/white 17.4:1; ink/paper 14.6; ink/sky 12.7; ink/amber 8.95; ink/light green 8.1; white/dark green 4.85; white/brown 4.6; white/red 4.2 | F1 |
| Weak or failing pairs | ink/red 4.1 (outline yes, ink text no); paper/red 3.5; red/sky 3.1 (best red accent background); sky/paper 1.15; white/paper 1.2; white/sky 1.37; tan/amber 1.01; light green/amber 1.11; light green/tan 1.09; dark green/brown 1.05; brown/red 1.09; dark green/red 1.15 (these are contrast ratios; the complete list of 21 pairs with a lightness gap under 25 is in B4.3) | F1 |
| Against the white feed page | sky 1.37:1, paper 1.20:1, white 1.00:1: pale thumbnails lose their edge | D6 |
| Accent saliency (proxy, 168×94, 40 scenes per cell) | red disc was the most salient point in 95% of scenes, amber 69%; amber fails on light green (2%) and brown (8%); amber works on ink; red and amber must never touch | D6 [C] |
| Color-blindness | red becomes olive (#726835 protan, #968733 deutan), the same as dark green; about 8% of men and 0.5% of women of Northern European descent have red-green deficiency (NEI) | D6 |
| Text legibility | comfortable about 12 px displayed cap height; on a 1280 master: 91 px at 168 wide, 62 px at 246, 43 px at 360; OCR floor about 5–7 px displayed, i.e. 40–50 px on the master | D6 |
| Text recommendation | main word cap height 100–140 px (minimum 90), secondary at least 60; outline 12% of cap height (8% for condensed fonts) in ink, outside the letters, round joins; hard offset shadow optional (6–8 px), no blurred shadows | D6 |
| Fonts | Lilita One primary (about 143 px font size gives 100 px cap height; fits about 16 characters in 1152 px); alternates Titan One, Paytone One, Fredoka 700, Baloo 2 800; Luckiest Guy and Bangers (thin at 168 px) are comic alternatives; Anton and League Gothic for numbers only; handwriting faces too thin; all free under OFL or Apache-2.0 | D6, F2 |
| Margins and keep-outs (1280×720) | 64 px sides, 36 px top and bottom; 230×90 px free bottom-right; about 110×110 px free top-right (derived or unverified) | D6 |
| Export sizes measured | flat cartoon at 1280×720: PNG-24 33 KB; PNG-8 14.5 KB; JPEG q90 4:2:0 63 KB; q95 4:4:4 94 KB; 4:2:0 softens edges by about 2 px | D6 |
| Device share | TV passed mobile for US watch time in Dec 2024 (YouTube CEO letter, Feb 2025); Chartbeat: 69% of views on mobile but TV gives 42% of minutes | D6 [B] |
| Brand-asset research | distinctive assets need consistent repetition (Romaniuk, Ehrenberg-Bass); a 2026 paper reportedly finds shape assets strongest (snippet only, UNVERIFIED) | D6 |
| Banner blindness | NN/g: people ignore things that look like ads; not evidence against consistent templates; the risks are an ad-like look and habituation | D6 [A] |

#### B2.6 Packaging, testing, cold start, Shorts

| Fact | Value | Grade | Where |
|---|---|---|---|
| Title and thumbnail as one unit | Galloway (2024-07-10): "view the title and thumbnail as one, do they compliment each other or contradict/repeat?" (sic); "always plan your title and thumbnail before recording" (2024-05-10); pass the "glance test" | [B] | D8 |
| Complementarity data | 217 classifiable thumbnails of 1M+ videos: 46.1% fully complementary, 28.6% mixed, 21.2% mostly repeated the title, 4.1% exact match (survivors, no CTR) | [C] vendor | D8 |
| Counterexample | TED-Ed "How do solar panels work?" (26M) and "Can you solve the prisoner hat riddle?" (37M) repeat the title: search-intent evergreen | [C] | D8 |
| Pairing patterns for a question title | A answer-tease ("NO JOBS"); B evidence promise ("We tested it"); C outcome plus mystery (holed Arecibo dish); D zero-text anomaly; E contrast triplet ("EASY / EASY / ALMOST IMPOSSIBLE"); avoid the reverse pairing (statement title, question in image) | [C] synthesis | D8 |
| Title length | 100-character limit is widely documented; visible length on phones unverified; SEO blogs claim about 40–55 characters in the mobile feed, 50–60 in search; real top examples 30–54 characters; Ink Explainer's longest is 66 | [C] | D8 |
| Sample size per variant (80% power, 5% significance, CTR only) | 4%→8%: about 550; 4%→6%: about 1,860; 4%→5%: about 6,700 (6,745); 4%→4.8%: about 10,300; three variants triple the total | arithmetic | D8 |
| Vendor thresholds | "1,000–5,000 per variant", "43% false positives under 1,000" | UNVERIFIED | D8 |
| Veteran caution | a video ranked 8/10 in the first hour recovered to 1/10 with no change (Galloway) | [B] | D8 |
| Cold start | early audiences "diverse"; videos reach people "who've never watched the channel" within the first hour; discovery "focused more on individual videos" than channel averages | [B] | D8 |
| Series blindness | no rigorous YouTube evidence; vendor "70/30" and "+38%" figures untraceable | UNVERIFIED | D8 |
| Shorts covers observed | Kurzgesagt title-card frames ("This Organ Regrows Every Month!", 1M); Veritasium "Rome's Escalator Disaster" (5.5M); Practical Engineering series card (3.2M) | [B] | D8 |

#### B2.7 The twelve candidate stories (fact base)

All twelve pass the age filter as of 2026-09-30 (nothing after 2024-09-30; no terrorism; no medical advice; politics only as regulatory facts). Legal status is **not fully verified** (D7): litigation for Challenger, criminal status for Piper Alpha and the class action for Note 7 are marked UNVERIFIED, and the follow-up settlements for Hyatt and Big Dig and legal follow-ups for the Blackout were not checked. Check each story again before choosing it. Full facts, quotes and sources are in D7 and G8. Ranked by thumbnail strength by the story-research agent (its judgment, not a test).

| Rank | Story | Headline facts | Thumbnail moment | Planted object |
|---|---|---|---|---|
| 1 | Comet, 1954 | 35 died 10 Jan (Elba), 21 died 8 Apr (Naples); whole fuselage tested in a water tank; failure after 3,057 cycles (1,221 real plus 1,836 simulated; another source 3,060); about 70% of the Elba wreck recovered | the whole fuselage in a purpose-built tank, wings out through seals, "flown" in about 5 minutes per simulated flight | a bolt hole |
| 2 | Tacoma Narrows, 1940 | opened 1 July, fell 7 Nov; wind 42 mph measured 09:30; twisting began 10:03; roadway tilted up to 28 ft each side; a 600-ft section fell 11:02; cause "remains a mystery", torsional flutter primary explanation | the tilted roadway; lemon-chewing workmen | a lemon |
| 3 | Vajont, 1963 | 1,917 dead (Italian Civil Protection; counts 1,919–2,056); about 260 million m³ slide; wave about 250 m over the crest; 262 m dam stood; criminal case closed 1971; final civil settlement 23 June 1999 | dam intact with a wave over it; at noon workers saw the mountain moving; at 13:00 a 50 cm crack | gravel-on-a-plank model |
| 4 | Vasa, 1628 | sank after about 1,300 m; about 30 died; a stability test with 30 men stopped after three trips; four rulers found (two Swedish feet, two Amsterdam feet); raised 1961 | huge ship with open gunports, a crowd on the shore (the story agent suggested a heeling ship; the mockup draws it upright) | a wooden ruler |
| 5 | Challenger, 1986 | 11:38 liftoff, breakup at 73 s; air temperature 36°F, 15°F colder than any earlier launch; Thiokol's engineers advised against launching below 53°F; foot-long icicles; Feynman's ice-water demonstration 11 Feb 1986 | a glass of ice water and a clamped rubber ring | the O-ring |
| 6 | 2003 Blackout | about 50 million people; 61,800 MW; alarm and logging software failed shortly after 14:14 EDT; trees tripped lines from about 15:05 | a frozen screen and a sagging line near a tree | the frozen screen |
| 7 | Samsung Galaxy Note 7, 2016 | discontinued 10 Oct 2016; FAA and PHMSA flight ban 14 Oct; two different defects (original and replacement); lost revenue estimate $17bn or more [C] | the replacement phone failing again | the phone |
| 8 | Quebec Bridge, 1907 | 75 of 86 workers died, 33 of them Mohawk ironworkers; about 15 seconds; span 549 m; bent chords noticed for weeks; second collapse 1916 (13 died) [C] | a visibly bowed chord while work continued | the bowed chord |
| 9 | Big Dig ceiling, 2006 | 10 July 11:01 pm; about 26 tons fell; 1 death; epoxy with poor creep resistance; anchor movement seen in 1999 | a bolt sliding out of a glued hole over years | an epoxy anchor |
| 10 | Hyatt Regency, 1981 | 17 July about 7:05 pm; 113 dead, 186 injured (NBS; others 114/216); the as-built change "essentially doubled" the load; at collapse 31% of code capacity; even the original design about 60% | one long rod vs two rods through a box beam | the nut and washer |
| 11 | Piper Alpha, 1988 | 226 aboard, 167 dead including 2 rescuers, 61 survived; pump's safety valve removed and a blind flange "hand-tightened only"; permits in different boxes; fire pumps on manual since 19:00 [C] | a steel disc fitted out of sight, two paper permits | the blind flange |
| 12 | Flixborough, 1974 | 1 June 16:53; 28 killed, 36 injured on site, 53 off site; a 20-inch bypass after reactor 5 cracked 27 March; no drawing, no calculations for the dog-leg or bellows, no pressure test; cause of failure contested | a dog-legged pipe with bellows and a gap where reactor 5 had been | the bellows |

**Dropped by the legal filter:** Morandi Bridge (verdict 16 July 2026, appeal announced), Boeing 737 MAX (civil trials continue, a jury verdict May 2026), Grenfell (charging decisions pending, trials 2029 or later). **Borderline, not used:** Lac-Mégantic. **Not verified in this pass (reserves):** Chernobyl, Three Mile Island, Apollo 13, Columbia, Mars Climate Orbiter, Millennium Bridge, St. Francis Dam, Sleipner A, Ronan Point, Tay Bridge, Kaprun, Sampoong, Banqiao, Therac-25, and the Titan submersible and Baltimore Key Bridge (not checked).

*For detail see Part D (final reports), Appendix G (raw notes) and Part F (data tables).*

### B3. Myths, unsupported claims and contradictions

#### B3.1 Consolidated list of myths and unsupported claims

Every item was researched. "Untraceable" means no primary source was found for the figure; it may still circulate widely. Items are grouped by topic.

**Thumbnail craft and CTR folklore**

| Claim | Verdict | Why |
|---|---|---|
| "Three words is the optimal thumbnail text" | Unsupported (convention) | No study found; 1of10 found the best text setup is none or under 10 characters; vidIQ found a median of 5 words among winners (no base rate) |
| "Emotional faces give 2.3× CTR" | Untraceable | Cited to Creator Insider; not found |
| "Eye contact adds 20%" | Untraceable | No source |
| "Median +32.7% uplift from A/B testing" | Untraceable | No source |
| "Netflix found contrast is the biggest predictor" | Unsupported attribution | No support found for the claim on Netflix's own page |
| "13 ms to stop the scroll" | Misapplied | A lab picture-detection result (Potter 2014; not replicated at 27 ms by Maguire and Howe 2016), not a feed effect |
| "60,000× faster than text" | Untraceable to research | The only origin found is a 1982 advertisement claim |
| "80% brand recognition from color" | Unsupported | A marketing statistic; secondary sources say it came from colored vs monochrome documents |
| "Red wins" / "warm beats cool" | Not supported | The only large dataset (1of10; views, correlational, viral videos only) has cyan (+36%), green and yellow/orange ahead |
| "Faces always win" | Contested | 1of10: about the same overall; vidIQ: common among winners with no base rate |
| "Shocked, open-mouth faces win" | Contested | About 5% of vidIQ's breakouts; MrBeast's team moved to a closed mouth; YouTube's own tips page recommends "a shocked face" |
| "Rule of thirds" and "F-pattern" for single-subject phone thumbnails | No CTR evidence | A centre preference exists for single subjects (Palmer 2008); the F-pattern comes from text-page studies; YouTube's own tips page suggests the rule of thirds |
| "Never repeat the title in the thumbnail" | Too strong | TED-Ed's search-intent videos repeat it and reach 26M and 37M; on browse, repetition wastes the thumbnail's job |
| "Questions in titles boost clicks" | Not supported | The largest recent headline study found question framing reduced engagement on average, earlier work is mixed, and matched million-view pairs were neutral |
| "Hide as much as possible to maximize curiosity" | Contradicted | Too vague loses (Le Quéré and Matias 2025) |
| "Bright, saturated thumbnails win" | Weak | 1of10 (winners only) supports; both audits found brightness, saturation and clutter did not separate top from weak within a channel |
| "A consistent template gives +38% CTR" and the "70/30 rule" | Untraceable | No method behind either |
| "Series blindness" (viewers ignore a repeated template) | No YouTube evidence | Only banner-blindness work on ads exists |
| "Multiple faces beat a single face" | Contested | 1of10 says yes; a 2024 study of 30 videos on the RED platform (not YouTube; tiny sample, [C]) says group thumbnails got 37.4% fewer views |

**Platform folklore**

| Claim | Verdict | Why |
|---|---|---|
| "Thumbnails must be 1280×720 and under 2 MB" | Out of date | Official page now says 3840×2160 recommended, 2 MB from phone, 50 MB from desktop |
| "168×94 is the phone feed size" | Wrong | It is the desktop watch-page sidebar size |
| SEO size lists ("246×138 search", "156×88 mobile") | Match nothing measured | Measured sizes are in B2.1 |
| "99.9% of Shorts views come from the feed" | Misattributed | A creator's remark (Jenny Hoyos, YouTube blog 2025-01-28), not a YouTube statistic |
| "Shorts thumbnails raise search CTR by 85%" | Unverified | The page says YouTube has not published Shorts-specific thumbnail data |
| "YouTube confirmed in April 2026 that satisfaction replaced watch time" | Unverified | Vendor blogs only |
| "1,000–5,000 impressions per variant are needed; 43% false positives under 1,000" | Unverified | Vendor figures with no method |
| "Veritasium gets 50% more views from testing" | Unverified | Not found |
| Dark-mode share of viewers | Unsourced | No source |
| Whether C2PA metadata in a generated thumbnail triggers an AI label | Unverified | No source |

**Story facts to avoid**

| Claim | Verdict | Why |
|---|---|---|
| Comet's "square windows" caused the failures | Myth | Comet 1 windows were rectangles with rounded corners; failures began at bolt holes near antenna cut-outs or the forward escape hatch |
| Tacoma failed by "resonance" | Disputed | WSDOT: the cause "remains a mystery", primary explanation torsional flutter; the textbook resonance account is disputed (Billah and Scanlan 1991, not fetched here) |
| Tacoma failed in a "light wind" | Trap | 42 mph is a gale; the bridge bounced in winds as light as 4 mph |
| Vasa: the king added a deck late | No evidence | The source says there is no evidence |
| Quebec: "Iron Rings are made from the wreckage" | No support found | Do not use |
| Hyatt: a walkway "built to hold 100 people" | Unverified | Do not use |
| Flixborough: "designed in chalk on the floor" | Unverified | Do not use |
| Blackout: a software "race condition" bug | Not in the report text | Secondary reports only |
| Piper Alpha: blame on the two workers named in court | Do not use | The brief forbids blaming individuals |
| Vajont: "270 m³" for the slide | Typo | Printed that way on the Civil Protection page; the figure is about 260 million m³ (sources 200–300 million) |
| Challenger: icicles "on the pad" | Imprecise | They were on a lower level of the fixed service structure |

#### B3.2 Contradictions between sources, and how they were resolved

| # | Contradiction | Resolution used |
|---|---|---|
| 1 | Faces: 1of10 says multiple faces beat a single face; a 2024 study of 30 videos on the RED platform (not YouTube; tiny sample, [C]) says the opposite | Treat as contested; limit to at most three figures (Netflix) and test |
| 2 | Titles: 1of10 says negative titles get 22% more views; Cui 2024 says positive titles beat negative | Do not optimize sentiment of titles; keep the brief's neutral, curious question form |
| 3 | Questions: Fang and Wheeler 2026 negative; Le Quéré mixed (3 negative, 2 positive, 4 null); OverseerOS neutral | Keep questions (the brief); make them concrete; put stakes in the thumbnail |
| 4 | Brightness: 1of10 supports brightness; both audits found no within-channel separation | Treat bright and lit as a hypothesis; avoid dark scenes for other reasons (brief, limbs) |
| 5 | Psychology prefers sparse texture; the best Ink Explainer thumbnails use full scenes | Simplified scenes with big flat color blocks; few small details |
| 6 | The niche is dark; 1of10 says dark underperforms; Ink Explainer's dark cave is among its weakest | Avoid dark backgrounds; it also differentiates from the niche |
| 7 | "Never repeat the title" vs TED-Ed's repeats | Complement for browse thumbnails; repetition is acceptable for search-intent evergreen |
| 8 | "99.9% of Shorts views from the feed" appears in one report as a finding, in another as misattributed | Treated as unverified and not relied upon |
| 9 | "Every high-view niche thumbnail carries words" (first draft) vs the data (about 75 of about 105 carried text; some top ones had none) | Corrected: about 70% carry words; median 3–4, maximum 7 |
| 10 | Test & Compare metric: "watch time share" (Help) vs "watch time per impression" (SEJ, ppc.land) | Unresolved; the formula is unpublished; the tool favors watch time, not CTR |
| 11 | Custom Shorts cover eligibility: "verified account" (Help) vs "Partner Program first" (blog) | Unresolved; check the channel's own Studio |
| 12 | Title testing shipped 4 Dec 2025 (SEJ) vs 9 Dec (ppc.land) | Immaterial; noted |
| 13 | Vajont deaths: 1,917 (Civil Protection) vs 1,919–2,056 | Say "about 1,900" |
| 14 | Vajont slide volume: sources say 200–300 million m³; the Civil Protection page prints "270 m³" | Say "about 260 million m³" or avoid |
| 15 | Hyatt: 113 dead and 186 injured (NBS) vs 114 and 216 (others) | Use the NBS figures or "more than 110" |
| 16 | Comet test: 3,057 cycles (Withey, Wikipedia) vs 3,060 (Aerossurance) | Say "about 3,000" or cite one source |
| 17 | Comet crack origin: forward escape hatch (tank test, Withey) vs antenna cut-out bolt hole (Elba aircraft) | Different aircraft: the first report conflated them; say which |
| 18 | Tacoma wind: 42 mph measured 09:30; twisting began 10:03 | Say "42 mph that morning" |
| 19 | Flixborough: cause of failure contested (HSE: the bypass failure "may have been caused by" a pipe fire) | Mark the cause as contested; the picture marks the modification, not a proven cause |
| 20 | Blackout: alarm failure "shortly after 14:14"; trees tripped lines from about 15:05 | Keep the timeline separate; show the line still clear of the tree |
| 21 | Reviewer vs first draft: ranking claim "the Comet agent's own ranking" is not in any saved note | Removed from the report |
| 22 | Ink Explainer's subscriber count: 106K on the channel page and in three reports (2026-09-30; "first video about 5 months ago") vs 77.8K "at month 8" in a third-party case study (credited to a "vidIQ stats page" in one note) | Unresolved; use 106K (read from the channel page) and treat 77.8K as unreliable |
| 23 | Shorts cover minimum size: "minimum height 640 px" (D1) vs "minimum width 640" (D8) | Unresolved; irrelevant at the recommended 2160×3840 |
| 24 | Reviewer 1's verdict line says 14 spot-checks and 12 should-fix findings; its tables hold 17 spot-check rows and 16 should-fix items | The tables are counted (see B6.2) |

*For the full lists see D2 (CTR evidence), D8 (packaging) and G8 (story notes).*

### B4. All recommendations, consolidated

Priorities: **P1** do before the first upload; **P2** do for every video; **P3** do after the first 8–10 videos. Every recommendation is a hypothesis built on the evidence in B2, unless it is a platform rule or a constraint from the brief.

#### B4.1 Ten strategic principles

1. **Treat the styles as hypotheses and run a test program.** No controlled study of YouTube thumbnail features and clicks was found (indirect evidence only: Zhao 2019 and a December 2023 Journal of Advertising study of illustrated vs photographic ads); the only reliable evidence will be your own Test & Compare results. (P1)
2. **Differentiate where the niche is thin:** lit, flat, hand-drawn scenes; the moment before the failure; the decision room; the cutaway of what no camera recorded. Avoid the niche's clichés: annotation circles and arrows drawn over the picture (the brief bans arrows, dashed lines and diagram symbols anyway; Style 3's red ring is a painted object, not an annotation), fire and explosion clip-art, sepia archive photos, dark backgrounds. (P1)
3. **One idea per thumbnail:** one hero, at most three people, one accent. Netflix's tests saw win rates fall sharply above three people; visual complexity has an inverted-U relation with popularity. (P1)
4. **The thumbnail adds; it never repeats the title.** Browse thumbnails do the job the title cannot: show the outcome or the odd detail, add one fact in 1–3 words. Repetition is acceptable only for search-intent evergreen videos. (P2)
5. **Keep the promise.** Everything the thumbnail shows or says must be visible or explained by second 15 of the video. Your outcome-first opening already enforces this. YouTube treats a misleading thumbnail as a strike risk and malicious clickbait as a monetization risk. (P2)
6. **Keep your question titles, but make them concrete** (a named object or a number). The evidence on question headlines is mixed and comes from written headlines; vague questions read as uninformative. The thumbnail carries the specific stakes. (P2)
7. **Put a surprising non-casualty number in the thumbnail when the title does not carry it.** Numbers are a common hook in the niche; 1of10 found titles with numbers got about 11% fewer views (correlational, viral videos only), so test number-in-thumbnail against number-in-title rather than avoiding numbers. Draft titles 1 and 9 (B4.7) already carry a number ("1,900", "50 million"); there the thumbnail should add a different fact. Never use a death toll as a thumbnail hook. (P2)
8. **Choose worry and dread over shock.** Readable emotion is supported; exaggerated shock faces are contested. Test a subtle or closed-mouth variant against an open-mouth one. Make the figure look at the hazard. (P2)
9. **Recognition comes from fixed anchors, not identical layouts:** palette, outline weight, character style, text style, the red-means-culprit rule. Ten different concepts can still look like one channel. (P1)
10. **Test radically different concepts.** On a new channel only big differences are detectable (4% to 8% CTR needs about 550 impressions per variant; 4% to 5% needs about 6,700). Never test font or color tweaks. (P2)

#### B4.2 Which style, when

- **Starter trio for almost any story:** Style 10 (Close-Up Gaze), Style 2 (The Moment Before), Style 1 (Tiny Under the Giant).
- **Conditional on the story:** Style 3 (needs a true odd image), Style 6 (needs a good non-casualty number), Style 7 (needs an odd, documented detail), Style 8 (needs a visible flaw and a crowd), Style 9 (needs a decision room), Style 4 and 5 (a small part or hidden mechanism).
- **Close cousins: never put in the same test:** 1 and 8 (big object plus small figures), 4 and 5 (a small part shown huge), 2, 8 and 9 (a calm scene with a hidden cause; the design review counts them as one idea).
- **Suggested test trio:** one *human* style (10, 7 or 9), one *mechanism* style (4 or 5), one *scale or scene* style (1, 2, 3 or 8), never two cousins together (so 9 goes with 1 or 3, not with 2 or 8). Alternate background families between consecutive videos.
- **Strongest at phone size in the check:** Styles 6 and 10. For Styles 7, 8 and 9 the words carry the thumbnail; props and small details vanish at 168 px.
- The style × story matrix is in section C6.

#### B4.3 The house system

**Fixed anchors**

1. The ten palette colors only. Measured on the mockups: 97.6–99.1% of pixels are exact palette colors; the rest are one- or two-pixel blends.
2. Ink outline #1a1a1a on every shape, about 12–16 px on the 1280×720 master.
3. The stick figure exactly as on the character sheet. Figures stand on **light surfaces**: single black limbs vanish on a black background.
4. **One accent, meaning "what went wrong":** red #d94a38 on the culprit (the slid slope, bowed chord, nut, anchors, twisting deck, rubber ring, bypass pipe, frozen screen). Measured on the mockups: 0.2–5.1% of the frame; oversize small parts, and still check they read at 168 px. Amber #e6b23a only as a small warm light, if at all. Red and amber never touch.
5. Text: Lilita One, white fill, ink outline outside the letters at 12% of cap height, caps, 1–3 words, at most about 16 characters per line, at most two lines, cap height at least 90 px for the main word.
6. Flat color with gentle cel shading; no gradients.
7. Lit scenes; **no dark backgrounds**. Dark thumbnails underperform in 1of10; the brief bans empty flat backgrounds; limbs vanish on ink; one of Ink Explainer's weakest thumbnails is a dark cave.
8. The safe zones (values for the 1280×720 master; multiply by 1.5 on a 1920×1080 master and by 3 on 3840×2160): 64 px side margins, 36 px top and bottom, 230×90 px free bottom-right, about 110×110 px free top-right.

**Variables per video:** composition, hero object, background family, emotion, text position, word count, camera distance, cutaway or not. Vary about four of these each time.

**Color rules** (details in D6 and F1)

- Three lightness tiers only: light (white, paper, sky, amber, tan, light green), mid (red, brown, dark green), dark (ink). Colors in one tier cannot be told apart by lightness, in grayscale, or with color-blindness; a few pairs from neighboring tiers fail too (light green with red, brown or dark green; tan or amber with red).
- Ink is the universal outline and the text color on any light color. White or paper words need the ink outline on sky, paper, amber, tan and light green. Never use red, brown or green as a text fill.
- **Fail pairs (lightness gap ΔL* under 25: all 21 pairs from the data table, smallest gap first, ΔL* after each pair):** tan/amber 0.5, dark green/brown 1.4, brown/red 2.5, light green/tan 2.9, light green/amber 3.3, dark green/red 4.0, paper/sky 5.3, white/paper 7.0, sky/amber 12.2, white/sky 12.3, sky/tan 12.7, sky/light green 15.6, paper/amber 17.5, paper/tan 18.0, light green/red 20.4, paper/light green 20.8, light green/brown 22.9, tan/red 23.2, amber/red 23.7, light green/dark green 24.3, white/amber 24.6. Outlines carry these in the mockups; check every real image.
- Red against dark green or brown loses its accent for red-green color-blind viewers (red turns olive): never put red on those backgrounds.
- Pale thumbnails dissolve on the white feed (sky 1.37:1, paper 1.20:1, white 1.00:1 against #ffffff): keep a mid or dark band or an ink frame along the edges.

**Stick-figure face and pose vocabulary** (from the cartoon audit; [B]/[C])

| Mood | How it is drawn |
|---|---|
| Calm or chill | eyes closed or half-lidded, tiny smile or flat mouth, reclined diagonal body, arm behind head (Ink Explainer "NO JOBS") |
| Tired or miserable | half-lidded circle eyes with red rings, slumped shoulders |
| Worried | wide circle eyes with tiny pupils looking sideways, wavy mouth, sweat drop |
| Shock | huge circle eyes, small centered pupils, open O mouth, hands on head |
| Skeptical | one flat brow, sideways glance |
| Anger | V-shaped brows, gritted teeth |
| Dread from scale | a small, stiff figure whose gaze leads the eye to the huge object |
| Body language | single-line arms and legs still read: a pointing arm, crossed arms, a long lounging leg |
| Sizing | exaggerate the eyes (about a quarter of head width); when the face is the hero make it at least about 25% of frame height; mouth lines vanish at phone size; one prop, at least about 15% of the frame, tied to the question |

(The brief's characters have two dot eyes, line eyebrows and a line mouth; the vocabulary above is a reference from other channels, to be adapted to dot eyes.)

#### B4.4 Text overlay specification

- **Why overlay:** the brief bans text in images and image models often render text badly; thumbnail words are a separate live-text layer added in Figma, Canva, Photopea, GIMP or Affinity (Affinity became free in Oct 2025 with a Canva account).
- **Font:** Lilita One (free, OFL). Alternates: Titan One (wide), Paytone One, Fredoka 700, Baloo 2 800. Anton or League Gothic for numbers only. Do not use handwriting faces (too thin at 168 px).
- **Size on the 1280×720 master:** main word cap height 100–140 px (never below 90); secondary at least 60. Lilita One needs a font size of about 143 px for a 100 px cap height.
- **Outline:** ink, drawn outside the letters, round joins, about 12% of cap height (12–16 px); about 8% for condensed fonts. A hard 6–8 px offset shadow is optional; no blurred shadows (they vanish at small sizes).
- **Words:** 1–3 caps words (D6 tolerates a fourth; the brief sets no word limit for thumbnails), at most about 16 characters per line, at most two lines. The words add one fact that the title does not say. Where a number is the hook it can be much larger (the Giant Number style deliberately breaks 1of10's "under 10 characters, under 7% of the image" pattern, so test it).
- **Tone:** YouTube's performance FAQ lists "Loud: ALL CAPS or !!!!!" among things to avoid. Keep to a few words, never use exclamation marks, and consider testing sentence case against caps.
- **Placement:** top-left or the left third; margins 64 px sides, 36 px top and bottom (outline included; 1280×720 values, scale for larger masters); keep 230×90 px free bottom-right and about 110×110 px free top-right; do not place text where a YouTube overlay or a possible mobile crop could hide it.
- **Colors:** white or paper fill with the ink outline works on every palette color. Ink text fails on red, brown and dark green; use white with a thick outline or a paper caption box with an ink outline.
- **Check at 168 px:** the main word must still be readable; the OCR floor is about 5–7 px displayed cap height (40–50 px on the master at 168 wide), comfortable is about 12 px displayed (91 px on the master).

#### B4.5 Image-generation and production workflow

1. **Make one character sheet** (front view, three expressions, prop) on flat paper and attach it to every generation (P1).
2. **Compose for text:** generate at 16:9 with one big hero shape, the figure large in the lower third, and a calm empty third for the words.
3. **Prompt structure.** OpenAI's guidance: scene, subject, details, constraints. Google's: subject, action, location, composition, style. Use positive framing: image models often ignore "no text" (research on negation: FineGRAIN, NeIn). Say "blank plain board" and "gauge with a needle and no marks", then check.
4. **References and edits.** Up to 14 reference images are accepted by Google's model; Midjourney V7 uses `--oref` (secondary sources); FLUX Kontext does iterative edits that preserve the character. Documented weak points (D6, OpenAI's guidance): text placement, recurring-character consistency and precise placement. Hands, small figures and proportions are my own watch-list, not a documented finding; step 7 of the QA list checks them.
5. **Fix stray glyphs** with a masked edit ("change only X, keep everything else identical") or paint over with flat color.
6. **Add the words** as a live layer; keep the text block separate so the art-only layer can be reused.
7. **Export:** sRGB PNG-24 without alpha, 16:9, under 2 MB (measured: a flat cartoon at 1280×720 is about 33 KB as PNG-24). If a grainy image goes over, use JPEG q92 4:4:4. A master of 1920×1080 or 3840×2160 is fine if under 2 MB; YouTube delivers 1280×720 anyway. 4:2:0 chroma subsampling softens edges by about 2 px, which matters only where there is no ink outline.
8. **Per-thumbnail QA** (run `tools/thumb_preview.py`):
   1. squint (blur): the accent, main word and silhouette survive;
   2. phone size: read the 360 and 168 rows at 100% zoom; main word cap height at least 90 px on the master;
   3. grayscale: word vs background lightness gap at least 50 (the ink outline carries white words on pale colors), figure vs background at least 25;
   4. light and dark feed rows: image edges do not dissolve;
   5. color-blind: red never on green or brown; amber never on tan or light green;
   6. badge zone free of anything important;
   7. zoom to 100% and look for stray letters or numbers on signs, gauges and clocks, and for hands, shoes or thick limbs;
   8. three words or fewer;
   9. export sRGB, 16:9, under 2 MB;
   10. after publishing, run Test & Compare.

#### B4.6 Testing program

- Use **Test & Compare** on every long-form video: up to 3 variants, desktop Studio. Upload your preferred variant **first** (if inconclusive, it stays). Outcomes: Winner, Performed Same, Inconclusive; YouTube says it is normal not to get a winner.
- Run at publish (core audience), read at 48–72 hours, and re-test older evergreen videos with a new concept. Re-testing after 72+ hours matches official guidance.
- **Do not** swap thumbnails by hand and compare (early viewers are fans; traffic-source mix distorts CTR). Do not edit during a test (it stops). Every variant at least 1280×720 or all drop to 480p.
- **Concepts, not tweaks:** the sample-size table in B2.6 shows why.
- **Log every video:** style, overlay words, CTR by traffic source, average view duration, test outcome. A template is in B5.
- **Never judge CTR alone:** if CTR rises and average view duration falls, the thumbnail over-promised.
- **Decision rules (heuristics [C], not from a source):** do nothing for 48 hours; Winner means adopt; Performed Same means keep your favorite and log it; Inconclusive means accept the default; consider a manual swap only if after about 5,000 impressions CTR is under 70% of your own same-source baseline and average view duration is healthy, and then change the whole concept.
- **After 8–10 videos** look for patterns across videos (single tests rarely reach significance at small volumes): which style types win with which traffic sources, and whether watch-time share agrees with CTR.
- **Cold-start reality:** strangers judge topic plus tension in one glance; the brand is a secondary layer. One secondary source (Beaupré via ppc.land; no sample or method given) says subscribers' feed CTR is "probably 10% or less" and that the subscribed audience rarely decides; treat it as a hint that supports optimizing for strangers, not as a measured figure.

#### B4.7 Title and thumbnail pairing

- **Plan the pair before recording** (Galloway, MrBeast memo, Ritchie): the title promises, the thumbnail shows, the video delivers.
- **Pairing patterns that fit a question title:** A) answer-tease (the words are the answer's first word); B) evidence promise ("we tested it"); C) outcome plus mystery (the image shows what broke); D) zero-text anomaly (one image at human scale); E) contrast triplet. **Avoid the reverse pairing** (a statement title with a question in the image).
- **Four pair-check questions** (from the packaging report; drop any pair that fails): Does the thumbnail say something the title does not? Does it repeat the title's first 40 characters? Does the video show it by second 15? Would a stranger get the topic in one glance on a phone?
- **Title length:** put the subject and tension in the first about 40 characters (phones truncate; real limits vary by device [C]); keep to about 60 characters or fewer. Thumbnail words must not depend on the truncated tail.
- **Draft titles for the ten mockups** (questions, no colon, at most about 60 characters; verify the facts before use): 1 *Why did 1,900 people die under a dam that never broke?*; 2 *Why did engineers keep building a bending bridge?*; 3 *Why did a jet airliner end up in a water tank?*; 4 *Why did one small change help bring down two hotel walkways?*; 5 *Why did a Boston tunnel ceiling fall after glue let go?*; 6 *Why did a four-month-old bridge twist itself apart?*; 7 *Why did a rubber ring destroy a space shuttle?*; 8 *Why did a brand-new warship sink in front of its own crowd?*; 9 *Why did a dead alarm help black out 50 million people?*; 10 *Why did one bypass pipe blow up a whole chemical plant?* Titles 3, 6 and 9 carry the end of their key idea after character 40 (title 3 was already shortened, but "tank" still falls after it): shorten them further if the hook must survive truncation.

#### B4.8 Shorts

- A Short's "thumbnail" is **frame 0 to 1 second**: the outcome image plus a 3–6 word line (matches the brief's outcome-in-three-seconds rule).
- A custom cover is optional, desktop Studio only, 9:16 (2160×3840), eligibility to be checked in your Studio (Partner Program vs verified account). Keep important content inside a central 2:3 crop.
- There is **no A/B testing for Shorts.** The Shorts feed plays the video without a thumbnail [B/C: our own check covers search, the rest is secondary]; covers matter on the channel page, homepage and search.
- Styles that translate best to vertical: 6 (Giant Number), 10 (Close-Up Gaze), 4 (Exhibit A). Shorts never ask (the brief).

#### B4.9 Compliance and ethics

- **Never** a thumbnail that misleads; **never** gore, blood, shocking imagery, bodies or visibly harmed people; **never** mocking or reveling in a death; **no** company logos; **no** profanity; keep to few words, no exclamation marks.
- **Advertiser-friendly:** disaster footage with visible harm gets limited ads; content that "profits from or exploits" a sensitive event gets none. Your style (structures and objects, no victims) is the safe-but-dramatic zone: the structure at the moment of the decision or failure, a worried stick figure, no bodies.
- **Real events and real people:** keep stick figures anonymous; do not caricature named individuals; attribute failures to systems, incentives and assumptions (the brief).
- **Casualty numbers as hooks:** the niche sometimes uses them; the brief says to state casualties factually and move on; the recommendation is not to use a death toll as a thumbnail hook.
- **AI disclosure:** not required for clearly non-realistic animation; keep the description line "This video uses AI-assisted narration and animation". Avoid photorealistic depictions of events that did not happen.
- **Originality:** keep each thumbnail specific to its story; "a house style is fine" is my reading of the policy, not YouTube's words (the policy wording is in B2.1).

#### B4.10 Fact discipline for thumbnail content

- Use only facts in the registry (C8, G8), and re-verify each against the primary report before publication.
- Never draw anything flagged UNVERIFIED or inferred; draw only the documented moment. Where a depiction is illustrative (for example the number of anchors, the rods' geometry) say so in the description or check the source drawing.
- Mark contested causes (Flixborough, Tacoma) as contested in the video and avoid a thumbnail that asserts a single cause. For Challenger, avoid a "cover-up" framing in the title (story notes).
- Primary sources named in the script go into the description (the brief).

#### B4.11 The do-not list

1. Dark or empty flat backgrounds (except a plain paper card with an ink frame).
2. Arrows, dashed lines, motion lines, diagram symbols, and annotation circles drawn over the picture (the brief names the first four; a ring painted as an object in the scene, as in Style 3, is a design choice to confirm).
3. More than three people; tiny figures under about 12% of frame height; dark hero on dark scene.
4. More than three words; small captions, before/after labels, two-line captions at small size; grids of tiny labelled pictures.
5. Repeating the title; a statement title with a question in the image.
6. Words inside the generated image; yellow or white text on a pale background without the ink outline (with the outline, white works on every palette color: B4.4).
7. Pale-on-pale color pairs; red on green or brown.
8. Victims, injuries, gore, sexualized shock; mockery; logos.
9. Copying a template and expecting it to carry a weak topic.
10. Swapping thumbnails by hand and comparing; editing during a test; judging by CTR alone; testing tweaks on a small channel.
11. Relying on unverified statistics ("3 words", "2.3× CTR", "99.9% of Shorts views").
12. A death toll as a hook; invented drama; showing what the video does not show.
13. Breaking identity with one-off art (the cartoon audit found one-off plain thumbnails among the weakest).

*For the full style specifications see Part C; for the checklists as used in production see C7.*

### B5. Roadmap, decisions, risks and gaps

#### B5.1 Roadmap

**Before the first upload (P1)**

1. Answer the four decisions in B5.3.
2. Make the **character sheet**: front view, three expressions (worried, calm, one more), one prop; the dot-eye face with a gaze shift toward the hazard; a very large head version for Style 10.
3. Build the **thumbnail template** in Figma, Canva or Photopea: a 1920×1080 (or 3840×2160) master; guides for the margins and the two keep-out boxes (the values in B4.3 are for 1280×720: margins 64 and 36 px, boxes 230×90 and 110×110 px; on 1920×1080 use 96 and 54 px, 345×135 and 165×165 px; on 3840×2160 multiply the 1280×720 values by 3); the Lilita One text style with the ink outline preset; a paper-card variant with the ink frame (Style 4).
4. In Studio, check **Test & Compare** is available (advanced features on) and whether **custom Shorts covers** are available to the channel.
5. Choose the first two stories from the registry (C8): re-verify every fact against the primary report named there, and recompute the "two years old" cutoff on the day.
6. Draft three radically different thumbnail concepts **before** scripting each video.

**Per video (P2): the eight-step packaging workflow** (from the packaging report, adapted)

1. *Idea gate:* one line for the outcome plus the human stakes number; draft three question titles of about 60 characters or fewer, with the hook in the first 40.
2. *Concepts:* sketch three radically different thumbnails, each a different pattern; for each, the tease in 0–4 words.
3. *Pair check:* four questions (does the thumbnail add a fact the title lacks? does it repeat the title's first 40 characters? does the video show it by second 15? would a stranger get the topic on a phone?); drop the pair if any check fails.
4. *Script hook:* write the opening to pay off the chosen pair.
5. *Publish* with Test & Compare on three variants, preferred first.
6. *Decide* by the rules in B4.6.
7. *Log* every video (template in B5.2).
8. *Shorts:* frame 0 to 1 s is the outcome image plus a 3–6 word line; the same frame can be the custom cover.

**First 10 videos: a suggested rotation.** Each test has one human, one mechanism and one scale-or-scene variant, never close cousins together (slots as defined in B4.2; the cousins are 1 and 8, 4 and 5, and 2, 8 and 9); adapt to what fits each story (swap Style 6 in for a mechanism slot when the story has a surprising number).

| Video | Human variant | Mechanism variant | Scale or scene variant |
|---|---|---|---|
| 1 | 10 Close-Up Gaze | 4 Exhibit A | 1 Tiny Under the Giant |
| 2 | 7 Odd True Detail | 5 Cutaway | 2 Moment Before |
| 3 | 10 Close-Up Gaze | 5 Cutaway | 3 Impossible Scene |
| 4 | 9 Seat of the Decider | 4 Exhibit A | 1 Tiny Under the Giant |
| 5 | 7 Odd True Detail | 4 Exhibit A | 1 Tiny Under the Giant |
| 6 | 10 Close-Up Gaze | 5 Cutaway | 8 Crowd on the Shore |
| 7 | 9 Seat of the Decider | 4 Exhibit A | 3 Impossible Scene |
| 8 | 7 Odd True Detail | 5 Cutaway | 8 Crowd on the Shore |
| 9 | 10 Close-Up Gaze | 4 Exhibit A | 2 Moment Before |
| 10 | 9 Seat of the Decider | 5 Cutaway | 3 Impossible Scene |

**After 8–10 videos (P3).** Tabulate per style: tests run, Winner, Performed Same, Inconclusive, CTR by traffic source, average view duration, and the watch-time-share direction. Look for patterns across videos, not in single tests. Narrow to three or four house styles; keep one exploratory variant per video; retire a style that never wins; revisit the style × story matrix with real results.

**Quarterly.** Re-test older evergreen videos with a new concept; re-check the platform rules (specs, Shorts covers, Test & Compare features change often; several items in this research were weeks old).

#### B5.2 Log template

One row per video; keep it in a spreadsheet.

| Field | Example |
|---|---|
| Video, date, story | Vajont, 2026-10-14 |
| Title (final) | Why did 1,900 people die under a dam that never broke? |
| Variant A / B / C | Style 1 THE MOUNTAIN / Style 4 LOAD… / Style 10 NO… |
| Overlay words per variant | THE MOUNTAIN / … |
| Test outcome | Winner B / Performed Same / Inconclusive |
| Watch-time share per variant (if shown) | 41% / 33% / 26% |
| CTR by traffic source (browse, suggested, search) | 5.1% / 3.2% / 7.8% |
| Impressions at the time of reading | 8,400 |
| Average view duration and percentage | 5:12, 49% |
| Notes (title truncation, comments, surprises) | |

#### B5.3 Decisions needed from the owner

1. **Text on thumbnails.** The brief bans text in images, yet about 70% of the thumbnails inspected in the niche (75 of about 105; median 3–4 words, maximum 7) and all of Ink Explainer's top videos carry two or three words. Assumption made: words are a separate overlay layer, never in the generated image. Confirm, or all ten become wordless. (If wordless, the Giant Number style loses its hook and Styles 4, 5 and 9 lose theirs.)
2. **Plain paper (Style 4).** The brief bans an "empty flat background" but allows beat drawings and text cards on plain flat paper. Confirm that a paper card with an ink frame counts as a beat drawing.
3. **The character sheet.** None exists. Approve dot eyes with a gaze shift toward the hazard, and a very large head for Style 10.
4. **Numbers on thumbnails.** Only non-casualty numbers were used (mph, tons, a time of day). Recommendation: never a death toll as a hook, given "state casualties factually and move on".

Secondary decisions: whether the examples built on lower-confidence sources (Quebec Bridge, Vasa) may stay as illustrations; whether to pursue a custom Shorts cover once eligible; whether to test sentence case against caps because YouTube's FAQ lists "Loud: ALL CAPS or !!!!!" among things to avoid.

#### B5.4 Risks and open questions

| Risk or question | Why it matters | How to resolve |
|---|---|---|
| Cartoon thumbnails have no controlled evidence against realistic ones | Every style is a hypothesis | Run the test program; there is no shortcut |
| Dot eyes without eye whites for fear signals are untested | Style 10 relies on the face | Test a subtle "worried" face against an open-mouth one |
| Bright and lit may not matter within a channel | The differentiation argument rests on the niche being dark | Compare a lit style with a mid-tone style in the first tests |
| Overlay words are an assumption | The brief bans text in images | Decision 1 |
| Title truncation limits are unverified on devices | Hooks after character 40 may be cut | Check Studio previews on your own phone; shorten titles 3, 6 and 9 |
| Test & Compare thresholds and the exact metric are unpublished | The tool may report "Performed Same" often | Expect it; use big concept differences |
| Shorts cover eligibility is ambiguous | Custom covers may not be available | Check Studio |
| YouTube's mobile Home size experiment may crop thumbnails | Words or faces near edges could be cut | Keep everything important central |
| "Loud: ALL CAPS" guidance | A few caps words are standard in the niche, but YouTube lists loud thumbnails as something to avoid | Few words, no exclamation marks; test sentence case |
| The "two years old" filter moves with the date | Candidate stories change | Recompute at each publication |
| Contested stories (Flixborough, Tacoma) | A thumbnail that asserts one cause could be wrong | Mark the cause as contested; the picture marks the modification or object, not a proven cause. For Challenger, avoid a "cover-up" framing in the title |
| Lower-confidence sources (Quebec, Vasa, Piper Alpha, Note 7) | "Nothing invented" is the channel's rule | Verify against primary reports before publication |
| Policy drift (AI labels, Shorts covers, Test & Compare features) | The AI-label rules were updated on 27 May 2026 (TechCrunch), custom Shorts covers began rolling out in July 2026 (YouTube blog, 2026-07-24) and new testing features were announced on 2026-09-23 | Re-read the policy and Help pages each quarter |
| Whether C2PA metadata in a generated thumbnail triggers an AI label | Possible unwanted label | Strip or check metadata; keep the art clearly non-realistic |

#### B5.5 What the research did not cover (candidate future research)

- Emotional contagion from emoji or cartoon faces; caricature and exaggeration effects; faces without eyes; quantified habituation to a consistent thumbnail identity.
- A CTR-by-traffic-source benchmark with a stated method; the share of dark-mode viewers; native phone-app and TV card sizes; an official safe-zone map.
- Shorts-specific thumbnail data.
- Audience reactions (comments) to tragedy thumbnails: none were read.
- Primary reports not opened: the Comet inquiry (CAP 127), the Cullen Report (Piper Alpha), the Quebec Royal Commission report, the Vasa Museum material, Billah and Scanlan 1991 (Tacoma), Samsung's 2017 findings and the CPSC page.
- Reserve stories not verified: Chernobyl, Three Mile Island, Apollo 13, Columbia, Mars Climate Orbiter, Millennium Bridge, St. Francis Dam, Sleipner A, Ronan Point, Tay Bridge, Kaprun, Sampoong, Banqiao, Therac-25.
- A direct test of cartoon vs realistic thumbnails is only possible with your own data.

### B6. Review status and spend (compact)

Three independent reviewers (agents that had not written the material) audited the work in three rounds. The per-finding tables and the reviewers' reports are in the full HTML dossier (B6 and Part E); this is the status.

- **Reviewer 1, facts and claims (first draft).** 17 live source spot-checks: 13 confirmed, 2 partly (Blackout "shortly after 14:14"; vidIQ via a secondary summary), 1 not found (the Team YouTube crop thread is script-rendered), 1 contradicted (the Comet tank claim in the first draft). 6 must-fix and 16 should-fix findings, all fixed; one is only partly resolved: the Hyatt overlay "LOAD DOUBLED" is half the story (two causes) and is kept with a caveat.
- **Reviewer 2, brief compliance and design.** The palette was clean (97.5% to 99.7% exact palette pixels per mockup). 7 must-fix and 10 should-fix findings: the banned split-panel style was replaced, the two dark-background styles became lit scenes, and depictions of the Comet tank, Hyatt, Big Dig, Vasa and Blackout were corrected to the sources. Partly resolved: the red-accent share is 0.2% to 5.1% of the frame (the first guideline was relaxed), the safe zones are only mostly clear, and in Style 9 the left screen is still the same sky blue as the window. Open: owner decision 1 (A5): if overlay words are refused, Styles 4, 5, 6 and 9 lose their hooks.
- **Reviewer 3, check of the synthesis against the reports and data.** 5 must-fix and about 23 should-fix findings, all fixed: the complete list of 21 failing color pairs (B4.3), a test rotation without cousin pairs (B5.1), the Comet tank wording, review counts, evidence grades, a mis-attributed 30-video study (a 2024 study on the RED platform, not YouTube), the Ink Explainer subscriber conflict (106K on the channel page vs 77.8K in a case study), and several overstated verdicts.
- **Known residual issues.** Titles 3, 6 and 9 in B4.7 carry the end of their key idea after character 40. The Shorts-cover minimum size is given as height 640 (D1) and as width 640 (D8). Quebec Bridge and Vasa rest on secondary sources; legal status of the stories is not fully verified; the Test & Compare metric name and thresholds are not published.
- **Spend.** The research and its corrections cost roughly 46 to 49 US dollars at list prices (agents about 23, main conversation about 25).

## D. The eight research reports (verbatim source layer)

These are the final reports of the eight research agents, unedited except that long scratch-folder paths were shortened. They were written before the reviews. Where they disagree with Parts A, B, C or F, those parts win (known conflicts: B3.2). Read them for detail, quotations and the source list at the end of each report.

### D1. Platform mechanics, specs, policies and testing

Notes with full quotes and URLs: `research/platform.md`. Raw pages are saved in the same folder.

Every YouTube Help page below was fetched raw with curl on 2026-09-30. Grades: [A] official, [B] first-hand or reported by a creator or company, [C] opinion.

#### 1. Specs and display

**Official specs [A]** (https://support.google.com/youtube/answer/72431):
- **Resolution and ratio:** recommended 3840x2160 for videos (16:9), with a minimum width of 640 px. Shorts are 2160x3840 (9:16), minimum height 640 px. Formats are JPG or PNG.
- **File size:** 2 MB when uploading from a phone, 50 MB from desktop. The 2 MB to 50 MB change was announced in Oct 2025 [B: 9to5google 2025-10-30] to serve 4K thumbnails on TV.
- **Custom Shorts thumbnails:** desktop Studio only.
- **Stale spec:** the old "1280x720, under 2 MB, min width 640" is still repeated by third-party sites but is out of date on the official page. Design at 16:9 and export a sharp JPG.

**Other official specs [A]:**
- **Daily limit:** there is a daily custom-thumbnail upload limit that varies by channel.
- **Custom vs frame:** a thumbnail is a custom upload only if the account is verified. Otherwise creators pick a suggested frame.
- **Best-performers stat:** "90% of the best-performing videos have custom thumbnails" (Help answer 12340300).

**Surfaces:**
- **What YouTube serves on desktop [B, my own measurement]:** in youtube.com search and channel-page JSON I found long-form thumbnails served as 360x202 and 720x404 pairs. Desktop tiles therefore render at about 360x202 CSS px, with 720x404 for high-DPI screens.
- **Not found:** I found no official pixel sizes for phone or TV, and no official safe-zone map. Treat any published one as [C].
- **Impression counting [A]:** an impression counts only if the thumbnail is shown for more than 1 second with at least 50% visible. It counts on the apps, TV, Search, Home, feeds, Up Next and playlists. It does not count on the mobile website, YouTube Kids, YouTube Music, external embeds, cards or end screens, or email and notifications.
- **Mobile Home feed test [A, TeamYouTube community thread 18138167, 2026-04-29]:** YouTube is running a limited experiment that varies thumbnail and video sizes on the mobile Home feed. It says "some thumbnails may appear cropped." Keep the subject and any text centered, with margin.
- **TV [B]:** thumbnails are shown large on TV, and YouTube rebuilt its pipeline for 4K.
- **Desktop redesign [B]:** Beaupré says the larger-thumbnail desktop Home layout raised long-form engagement (SEJ). He gave no data.
- **Overlays:** the duration badge sits bottom-right. A red progress bar sits along the bottom edge on watched videos (YouTube via SEJ [B]). Desktop hover icons sit top-right. I could not verify exact geometry; the third-party "15% / about 44-62 px" figures are UNVERIFIED [C]. Treat the bottom-right corner and the bottom edge as unsafe.

**Shorts:**
- **Custom covers [A]:** the YouTube blog (2026-07-24) says custom Shorts thumbnails are rolling out to Partner Program creators first, with more creators to come. Creators can also pick from 3 suggested frames on desktop, or any frame on mobile.
- **Contradiction:** the Help page says "verified account," while the blog says the Partner Program first. Check whether the channel qualifies.
- **No A/B for Shorts [A]:** Help says A/B testing is not available for Shorts. Tubefilter implies it is coming; that is unsupported.
- **Where covers show:** the Shorts feed plays the video with no thumbnail. Thumbnails show on the channel page (Home and Shorts tabs), the homepage and search. The homepage and channel-page part is from Rene Ritchie via ppc.land [C, secondary; I could not read the Creator Insider transcript, YouTube blocks watch pages here]. Search is confirmed by my own JSON check.
- **2:3 crop [B, my measurement]:** search JSON serves Shorts thumbnails as 405x720 (9:16) and 405x608 (2:3) variants. This supports Ritchie's reported advice that the usable area is closer to a 2:3 crop of the 9:16 frame, with key content away from edges.
- **Myth:** "99.9% of Shorts views come from the feed" is a creator's remark. On the YouTube blog (2025-01-28) it is Jenny Hoyos's quote, not the Shorts product lead's, and ppc.land misattributes it. Treat it as UNVERIFIED as a YouTube statistic.

#### 2. Impressions, CTR, packaging, clickbait

- **Definition [A] (Help 7628154, 16767369):** CTR is "how often viewers watched a video after seeing a thumbnail." Help says it "tells you how eye-catching your video idea or 'packaging' is."
- **Benchmark [A]:** "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." Ranges are wider for new videos or fewer than 100 views. This is not a target.
- **Why CTR varies [A]:**
  - It falls as reach widens. Help's own example is 9% on 10,000 impressions dropping to 3.5% on 100,000, called "a sign of success."
  - Search gives fewer impressions and higher CTR.
  - Homepage gives high volume and lower CTR.
  - Early CTR is inflated by loyal fans.
  - A niche topic can show high CTR but low impressions.
- **Subscriber ceiling [B, ppc.land summary of Beaupré's 2026-09-01 Creator Insider interview]:** "probably all your videos have about maybe a 10% or less click-through rate" in the subscribers row.
- **What YouTube optimizes:**
  - It says it aims to "maximize long-term viewer satisfaction" (Help 141805).
  - Signals are "clicks, watchtime, survey responses, sharing, likes, and dislikes" (Goodrow, YouTube blog, 2021-09-15 [A]).
  - "Clicking ... doesn't mean you actually watched it," which is why watch time was added in 2012.
  - Beaupré: "No metric on its own is a good indicator of value." The weighting differs by person, device and moment. That is a secondary source [B].
- **Clickbait [A]:** "You can tell if your thumbnail is clickbait if it's getting high CTR but low average view duration and lower than expected Impressions." Help 141805 tells creators to avoid thumbnails that are "Deceiving, misleading, clickbaity or sensational," "Shocking," "Disgusting," "Gratuitous violence," or "Loud: ALL CAPS or !!!!!".
- **Packaging, per staff [A]:** Rene Ritchie (YouTube blog, June 2024) describes "thumbnails that make a promise and videos that deliver on it." In July 2024 he wrote: "Figure out a compelling thumbnail and title ... make a video that delivers on the thumbnail and title's promise."
- **Unverified claim:** vendor blogs claim YouTube "confirmed" in April 2026 that satisfaction replaced watch time. I could not verify it. UNVERIFIED.

#### 3. Test & Compare (A/B)

- **Mechanics [A] (Help 16391400/13861714; Ritchie, 2024-06-14):**
  - **Variants:** up to 3 titles and/or thumbnails, on long-form only, desktop Studio, with advanced features enabled.
  - **Traffic split:** roughly equal shares (a third each for 3). Each viewer always sees the same variant.
  - **Duration:** runs until a variant has significantly more watch time, or 2 weeks ("a few days or up to 2 weeks").
  - **Metric:** results are judged on watch time share, not CTR. Outcomes are Winner, Performed Same, or Inconclusive.
  - **No winner:** the first uploaded variant becomes the default. Put the preferred one first.
  - **Control group:** a small control group sees only the default and is excluded from the calculations.
- **Not eligible:** Shorts, Premieres, made-for-kids, private, or age-restricted videos.
  - Editing the title or thumbnail mid-test stops it.
  - An age-restricted video will not run the test.
  - Uploading age-restricted content without marking it costs the channel the feature.
- **Resolution trap [A]:** if any variant is under 1280x720, all variants are downscaled to 480p.
- **Why watch time [A]:** "we optimize tests for overall watch time over other metrics, like click-through-rate." Ritchie: "If you over-index on CTR, it could become click-bait."
- **Metric name conflict:** Help says "watch time share." SEJ and ppc.land say "watch time per impression." The formula is not published. UNVERIFIED.
- **Announcement date conflict:** title testing shipped in early Dec 2025. SEJ dates it Dec 4, ppc.land Dec 9.
- **Official use guidance [A]:**
  - Test bigger differences first (layouts and image elements), then finer ones.
  - Run a test at launch (core audience), then again 72+ hours in (wider audience).
  - Be patient. Test older videos first. Similar variants take longer.
  - Help warns that testing several thumbnails by hand on one video confounds traffic sources.
- **Scale [A]:** YouTube says more than 40 million title and thumbnail experiments have been run since 2024 (Made on YouTube blog, 2026-09).
- **New (2026-09-23) [A/B]:**
  - **Dynamic thumbnails:** YouTube "recommend[s] the best of three options to different segments of your audience." I could not find a release date, and how segments are formed is unexplained.
  - **Video-cut testing:** testing up to 3 cuts is "coming soon" (2027 per TechCrunch).
  - **Ask Studio agent:** an agent can retest old thumbnails.
  - **Read on these:** the Creator Insider details come only through ppc.land [C].

#### 4. Policies for disaster thumbnails

- **Community Guidelines (Thumbnails policy, answer 9229980) [A]:** not allowed are "Violent imagery that intends to shock or disgust," "Graphic or disturbing imagery with blood or gore," and "A thumbnail that misleads viewers to think they're about to view something that's not in the video."
  - **Age-restriction factor:** it weighs "whether violent or gory imagery is the focal point."
  - **Penalty:** first offense is usually a warning. Later ones are a strike (3 in 90 days risks termination). Repeat thumbnail violations can also remove custom-thumbnail rights for 30 days.
  - **Exception:** an educational or documentary context exception exists, but it is not a pass.
- **Animation [A] (answer 2802008):** YouTube "make[s] a distinction between dramatized violence featuring real human actors and content featuring animations." It generally does not remove dramatized violence that is apparent as animated.
- **Spam policy [A]:** "malicious clickbait" (a thumbnail that does not deliver what was promised) can suspend monetization or lead to termination.
- **Advertiser-friendly guidelines (answer 6162278) [A]:** they apply to "thumbnail, title, description, and tags."
  - **Full ads:** "Severe property damage where death or severe bodily harm likely occurred (such as ... fires, building collapses)." Also tragedies "with limited or no display of violent acts or their results," and an implied moment of death in an educational or documentary context.
  - **Limited ads:** "Footage of disasters that involve visible harm to people or their resulting suffering, such as extreme emotional distress." Also dramatized violence where the aftermath is visible.
  - **No ads:** focus on gore, "heavy display of blood," severe agony.
  - **Sensitive events (includes natural disasters):** no ads for content that "profits from or exploits" one, for example keywords used "to drive additional traffic."
  - **Profanity:** none in thumbnails.
- **Real victims [A] (Harassment policy, answer 2802268):** not allowed are content "reveling in or mocking the death or serious injury of an identifiable individual" and content that "realistically simulates deceased ... individuals describing their death." Trademark holders' rights are enforced, so avoid company logos.
- **Originality [A] (YPP policy, answer 1311392):** reviewers check "titles, thumbnails, and descriptions."
  - **Not monetizable:** "AI-generated content made with generic or unoriginal templates," and content that "repeatedly uses disturbing themes (such as violence or loss) without building a cohesive narrative."
  - **Allowed:** the same intro and outro with different substance, and "using AI to visualize a unique character and narrative you invented."
  - **Implication:** a consistent house style is fine, but each thumbnail should stay story-specific.

**A safe-but-dramatic thumbnail:**
- Show the structure at the moment of the decision or failure: a crack, a gauge, a collapsing span, smoke.
- Use stick figures with worried or shocked faces, not agony.
- Show no bodies, blood, or visibly harmed people.
- Use no real-victim likenesses or mocking tone.
- Do not imply the video shows something it does not.

#### 5. AI and disclosure

- **Cartoon animation [A] (Help 14328491):** disclosure is required only for realistic content. It lists as not needing disclosure "non-realistic content," an "AI-generated or altered animation of a missile in a fully animated video," "Cloning one's own voice to create voice overs," and "generative AI tools to create or improve a video outline, script, thumbnail, title, or infographic." A realistic depiction of a disaster that did not happen does need it.
- **Labels:** the May 27, 2026 update [A/B] puts labels for photorealistic AI content below the player. Animated or unrealistic content gets a label in the expanded description only (TechCrunch). The rules do not label thumbnails separately.
- **Auto-labels:** labels are added automatically for content made with YouTube's own AI tools, content with C2PA metadata, or content YouTube's systems detect as AI. Whether C2PA metadata embedded in a generated thumbnail triggers a label is UNVERIFIED.
- **Description line:** the channel's description line "This video uses AI-assisted narration and animation" is consistent with all of this.
- **Ask Studio caveat:** ppc.land says YouTube has not addressed whether Ask Studio-generated thumbnails fall under the disclosure rules. UNVERIFIED.

#### Hard-constraint checklist for every Stress Riser thumbnail

1. 16:9, made at 3840x2160 (never below 1280x720), JPG or PNG. Keep it under 2 MB if uploading from a phone, otherwise use desktop (50 MB).
2. All A/B variants must be at least 1280x720, or all are downscaled to 480p.
3. Keep the subject, faces and any text in the central area. Leave the bottom-right corner and the bottom edge empty (duration badge, progress bar). Leave the top-right free on desktop. Expect possible cropping on mobile Home.
4. It must read at about 360x202 px and smaller. Use very few words, if any.
5. Shorts covers are 9:16 and desktop Studio only. Keep key content within a central 2:3 crop.
6. Depict only what the video actually contains. Any misleading thumbnail is a strike risk, and malicious clickbait risks monetization.
7. No blood or gore, bodies, or visibly harmed or suffering people. No real victims' likenesses, mocking or reveling. No profanity. No ALL CAPS or "!!!!!" overload.
8. No company logos. No real-person likeness.
9. No photorealistic disaster imagery (this also avoids any AI-disclosure duty). Stay in the flat-color cartoon look.
10. Vary each thumbnail by story so the channel does not read as templated.
11. For testing: at most 3 variants per test, differing in layout or concept rather than small tweaks. Put the preferred one first. Expect a "Performed Same" result. Retest at 72+ hours. The winner is decided by watch time, not CTR.
12. Judge CTR by traffic source, not as one number.

#### Caveats

- I could not read Creator Insider transcripts, because watch pages are bot-gated and I did not try to bypass that. The Beaupré interview, the Shorts 2:3 remark and the dynamic-thumbnails details come via ppc.land, SEJ and TechCrunch, so they are secondary [B/C].
- I found no official phone, TV or suggested-video pixel sizes and no official safe-zone geometry.
- The blog post on AI-label placement was partly truncated when fetched. I corroborated it with TechCrunch.
- I found no source on the Test & Compare statistical thresholds or on segment formation for dynamic thumbnails.

#### Sources

- YouTube Help pages (support.google.com/youtube/answer/…):
  - 72431 (thumbnails) and 16391400 / 13861714 (A/B test)
  - 7628154, 9314486 and 16767369 (impressions and CTR)
  - 141805 (performance FAQ) and 12340300 (thumbnail and title tips)
  - 9229980 (thumbnails policy), 2802008 (violent or graphic content), 2802167 (age-restricted content) and 2801973 (spam)
  - 6162278 (advertiser-friendly), 2802268 (harassment), 1311392 (YPP policies) and 14328491 (GenAI disclosure)
- TeamYouTube thread: https://support.google.com/youtube/thread/18138167
- YouTube blog:
  - https://blog.youtube/news-and-events/youtube-studio-custom-thumbnail-updates/
  - https://blog.youtube/news-and-events/made-on-youtube-new-tools-power-creation-journey/
  - https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/
  - https://blog.youtube/creator-and-artist-stories/renes-top-five-june-14-2024/
  - https://blog.youtube/creator-and-artist-stories/renes-top-five-july-19-2024/
  - https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/
  - https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/
- YouTube pages:
  - https://www.youtube.com/howyoutubeworks/product-features/recommendations/
  - https://www.youtube.com/creators/grow/optimize-your-content/
- Secondary reporting:
  - ppc.land, three articles: Shorts thumbnails; Made on YouTube A/B and dynamic; Beaupré interview
  - searchenginejournal.com: title testing (2025-12-04); bigger thumbnails (Beaupré)
  - techcrunch.com: 2026-09-23 and 2026-05-27
  - androidauthority.com, 2026-04-30
  - 9to5google.com, 2025-10-30
  - tubefilter.com, 2026-07-24

### D2. Empirical evidence on what gets thumbnails clicked

Notes file with URLs and quotes: `research/ctr-evidence.md`. Contact sheets: `thumbs/ink_grid.jpg` and `thumbs/animated_sheet.jpg` in the same folder.

Grades: [A] official documentation, peer-reviewed or large dataset. [B] first-hand creator or company data. [C] opinion or anecdote.

#### Bottom line
1. **No public, controlled dataset of CTR by thumbnail feature exists.** YouTube's own A/B tool reports watch-time share, not CTR. Nearly all "rules" rest on outcome-selected samples of already-viral videos, which show correlation only. Treat the confident percentages in SEO blogs as folklore.
2. **The evidence that survives scrutiny points one way.** Thumbnails should be simple and legible at phone size, with one dominant subject and few or no words. They should be bright, carry a readable emotion, and promise something the video actually delivers.
3. **Effects of single tweaks are small.** MrBeast's team reported a "small difference" that was consistent across 30 videos. Big gains come from a different concept or packaging, not from polish.

#### Key findings

**1. 1of10 dataset [B, large, correlational, not peer-reviewed].** 300K+ high-performing 2025 videos, 62.6B views, 52K channels. The metric is outlier score, meaning views divided by the channel's median views. It measures views, not CTR. Published 2026-02-06 at https://1of10.com/blog/what-actually-makes-a-youtube-video-go-viral-in-2025/ (raw page fetched).
- Face vs no face performs about the same overall. Multiple faces beat a single face. Faces help mainly channels above 200K subscribers. They help lifestyle, finance and beauty, and hurt health/fitness and movies/TV.
- 84% of thumbnails have text, and those with text get about 19% fewer views. The best setups have no text, or under 10 characters covering under 7% of the image.
- Cyan thumbnails get about 36% more views than average. Green and yellow/orange also do well. Views rise with brightness, and dark thumbnails underperform. The "100-110" brightness peak has undefined units, so I mark it UNVERIFIED.
- Entertainment gets about 44% more median views than educational. Educational videos must "borrow entertainment framing, use emotional hooks" and avoid lecture-style packaging.
- Titles: numbers cost about 11% of views. Negative titles get about 22% more views than positive ones.

**2. vidIQ 2026 study [B, no control group].** 500 breakout long-form videos across 30 niches, published in the month to 2026-06-30. Page blocked; figures come from a search summary plus a critique at frameos.studio.
- A face appears in 69% of them, 75% of the top 100 and 80% of the top 50.
- High contrast appears in 56%. Face or high contrast appears in 89%.
- 72% have overlay text, median five words. Only about 5% use an exaggerated expression.
- These figures describe winners with no base rate, so they show convention, not cause.

**3. Netflix artwork A/B tests [B, company first-hand, movies not YouTube].** Source is Netflix's own newsroom page "The Power of a Picture", fetched raw.
- Faces with complex emotion beat stoic ones.
- Recognizable, polarizing characters engage more. Villains beat heroes in kids and action titles.
- Win rates "dramatically dropped" above 3 people, because images are too complex at small sizes.
- 2014 consumer research: artwork was the biggest decision driver and over 82% of browsing focus. Users spent about 1.8 seconds per title.

**4. MrBeast [B].**
- Tweet 2023-09-06: closing his mouth in thumbnails raised watch time "on every video".
- Thumbnail lead Chucky Appleby: "about 30 videos, all 30... higher watch time. It was a small difference... 30 in a row gave us the signal." This is watch-time share in YouTube's tool, not CTR, with no figures published.
- Appleby also says: "easy to understand", design for the small size, and consistency of face and colors.
- The leaked memo (2024) defines CTR/AVD/AVP and says title and thumbnail set expectations. I did not verify its authenticity. Its advice is about concept extremity, not thumbnail craft.

**5. Official YouTube [A].**
- Help center: "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." Wider for videos under a week old or under 100 views. Home-page impressions lower CTR naturally, and channel-page impressions raise it.
- Help center on clickbait: high CTR with low average view duration and lower-than-expected impressions is the clickbait signature.
- Help center on manual swapping: swapping thumbnails on the same video is unreliable because traffic sources differ.
- An impression counts only if the thumbnail shows for more than 1 second with at least 50% visible.
- Test & Compare: up to 3 variants, winner by watch-time share. Winner, Performed Same and Inconclusive are all common. YouTube publishes no percentages for these outcomes.
- Rene Ritchie (via Search Engine Journal): over-indexing on CTR "could become click-bait, which could tank retention".
- Todd Beaupré, Creator Insider 2026-09-01 (via ppc.land, secondhand): subscribers' feed CTR is "10% or less", and CTR "falls predictably as impressions widen". "No metric on its own is a good indicator of value." Mobile thumbnails used to be much smaller. The write-up notes no sample or methodology was given.
- Covington, Adams and Sargin (Google, RecSys 2016) [A, peer-reviewed]: ranking uses roughly expected watch time per impression, because "ranking by click-through rate often promotes deceptive videos... ('clickbait')".
- CTR by traffic source (search 12.5%, browse 3.5%, and so on) appears only in SEO blogs with no methodology. UNVERIFIED.

**6. Academic work [A].**
- Cui et al. 2024, Journal of Business Research 183:114849: 16,215 YouTube covers. Strong sentiment in thumbnails, positive or negative, raises views. Strong sentiment in caption text lowers views. Positive titles beat negative, which contradicts 1of10.
- Fang et al. 2026, Journal of the Academy of Marketing Science: 22,958 thumbnails plus two experiments. Visual complexity has an inverted-U relationship with popularity, with stronger effects for utilitarian videos. The platform is not verified as YouTube.
- Koh & Cui 2022, Decision Support Systems: 3,745 branded videos. Coherent colorfulness and brightness pairings work best, with moderate image quality. Abstract only.
- Attention studies:
  - Cerf et al. 2009 found faces and text draw gaze 16.6x and 11.1x more than matched regions.
  - Yangandul et al. (ETRA 2018) found about 2x attention on thumbnails vs titles.
  - Both show attention, not clicks.

**7. Creator cases.**
- Derek Muller / Veritasium [B, via Gigazine summary; no CTR numbers, transcript unretrievable].
  - Adding "What can we do?" to an asteroid video's title did not help. A big thumbnail change plus a simpler title made it a 10M+ video.
  - A viewer poll preferred "The Biggest Myth in Education" over "You Are NOT a Visual Learner", against Derek's prediction.
  - He separates "legitbait" (brief conveys the real content) from "clicktraps" (misleading, draws backlash).
- Ali Abdaal [B, via How to YouTube newsletter]: a rushed thumbnail was replaced after the A/B test showed a "much higher" CTR, and the video reached "almost 1m views". No exact CTR published.
- I found no published thumbnail numbers for Mark Rober, D'Avella, Kurzgesagt, Wendover, Real Engineering, Practical Engineering, Polymatter, Johnny Harris or Vox.

**8. Descriptive studies of million-view videos [B, weak, no controls].**
- OverseerOS on 16,152 videos with 1M+ views: 25% have no thumbnail text, and about 75% of text-bearing thumbnails do not mostly repeat the title.
- OverseerOS on 891 matched question vs statement pairs: question won 445 and statement won 446, median ratio 1.000. Only 6.8% of million-view titles contain "?".

#### Verdict table
| Rule | Verdict | Evidence |
|---|---|---|
| Human face vs none | CONTESTED | 1of10: similar overall, helps only large channels. vidIQ: faces common, no base rate. |
| Exaggerated shock face | CONTESTED, leaning myth | vidIQ: about 5% of breakouts. MrBeast moved to closed mouth. Cui: strong sentiment helps. Netflix: complex emotion beats stoic. |
| Readable emotion | SUPPORTED (moderate) | Netflix, Cui, MrBeast. |
| Fewer words (0 to 3) | SUPPORTED (moderate, correlational) | 1of10 text -19%, best under 10 characters. Caption text hurts in Cui. |
| Exact "3 words" or "30% higher CTR" | MYTH / UNVERIFIED | No source. |
| High brightness and saturation | SUPPORTED (weak to moderate) | 1of10 brightness. Koh & Cui coherence. |
| Warm beats cool ("red wins") | MYTH-ish | 1of10: cyan, green, yellow/orange lead. |
| Contrast | SUPPORTED | vidIQ 56%. Netflix small-size legibility. |
| Single subject, few elements | SUPPORTED (moderate) | Netflix drop above 3 people. JAMS inverted-U. Beaupré "less is more". |
| Multiple faces | CONTESTED | 1of10 says better. A 30-video RED study says group thumbnails got 37% fewer views. |
| Arrows, circles, red highlights | UNVERIFIED | No dataset found. |
| Before/after or two-panel | UNVERIFIED | No dataset. |
| Close-up vs wide | UNVERIFIED | Blog claims only. RED n=30 favors far shots. |
| Illustrated vs photographic | UNVERIFIED | No controlled study. |
| Mystery/hidden element | THEORY-supported only | Muller poll. Must deliver, per YouTube. |
| "?" in thumbnail | UNVERIFIED | No data. |
| "?" in title | NEUTRAL in data | OverseerOS matched pairs, ratio 1.000. |
| Logos/branding | UNVERIFIED | No data. |
| Consistent series template | PLAUSIBLE, unproven | Appleby's qualitative claim. The "+38%" figures are untraceable. |
| Title-thumbnail complementarity | DESCRIPTIVE only | OverseerOS. |

**Myths I could not trace** (attribution to Netflix or YouTube unsupported):
- "13 ms to stop the scroll": a lab picture-detection result (Potter 2014, not replicated at 27 ms by Maguire & Howe 2016).
- "60,000x faster than text": a 1982 advertisement.
- "Faces give 2.3x CTR", "median 32.7% uplift from A/B testing", "eye contact +20%", "Netflix found contrast the biggest predictor".

#### Illustrated/cartoon and educational niches
- No controlled data on illustrated vs photographic thumbnails exists. Only existence proofs [C].
  - Ink Explainer: faceless stick-figure channel, 77.8K subscribers, one video at 9.7M views in about a month.
  - The Infographics Show: a panicked cartoon controller thumbnail, "AMERICA CLOSED", 2.5M views in 2 weeks.
  - Kurzgesagt: no faces, 10-20M views on its latest uploads.
- The shared traits, descriptive only: one dominant subject, 1 to 3 caps words, saturated color, high figure-ground contrast.
- OverSimplified and Historia Civilis have older videos, so their views are cumulative and not comparable.
- Educational content has lower median views than entertainment (1of10, about -44%) and needs a curiosity hook without misleading. Derek Muller, YouTube and MrBeast's memo agree on delivery of the promise.
- MrBeast entertainment tactics (extreme concept, wide-open faces) are not what educational breakouts show: vidIQ found only about 5% shocked faces.

#### What this means for Stress Riser
- **Subject and legibility.** One large stick-figure face (round head, dot eyes and brows read at small size) against one clear disaster object. Keep it to 3 characters or fewer and test at about 120 px width. Use a specific emotion such as dread or realization, not a generic scream. Test a subtle or closed-mouth variant against an open-mouth one.
- **Text.** Use none, or 1 to 3 words under 10 characters that add a fact the title lacks, rather than repeating the title. The brief bans text in scene art, so any thumbnail text would be composited separately. That is a decision for you.
- **Color.** Lean bright with high figure-ground contrast. Your palette's sky blue `#bfe2ea` and yellow `#e6b23a` fit 1of10's cyan and yellow/orange signals. Avoid dark frames.
- **Promise and delivery.** Show the real outcome, which the outcome-first opening pays off in seconds. YouTube's retention report flags when the first 30 seconds fail to match the thumbnail and title.
- **Question titles.** Question titles are neutral in data (OverseerOS matched pairs), so keep them for brand fit, not as a CTR lever.
- **Shorts.** About 99.9% of Shorts views come from the Shorts feed (ppc.land; original not verified), where no thumbnail shows. Custom Shorts thumbnails only began rolling out 2026-07-25, with no A/B testing. Thumbnail work matters mainly for long-form.
- **Testing your 10 styles.** Use Test & Compare on long-form. Make styles clearly different, since small tweaks yield "Performed Same". Judge on watch-time share, not CTR alone.

#### Sources
- https://1of10.com/blog/what-actually-makes-a-youtube-video-go-viral-in-2025/
- https://www.searchenginejournal.com/do-faces-help-youtube-thumbnails-heres-what-the-data-says/563944/
- https://support.google.com/youtube/answer/7628154
- https://support.google.com/youtube/answer/7577430
- https://support.google.com/youtube/answer/16391400
- https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/
- https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/
- https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf
- http://about.netflix.com/en/news/the-power-of-a-picture
- https://www.socialmediatoday.com/news/youtube-shares-insights-mrbeasts-team-creates-compelling-thumbnail/709817/
- https://www.creatorhandbook.net/mrbeast-claims-closing-his-mouth-in-thumbnails-is-better-for-views/
- https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/
- https://frameos.studio/blog/youtube-thumbnail-best-practices
- https://vidiq.com/research/youtube-thumbnail-study/
- https://scholars.ln.edu.hk/en/publications/clicks-for-money-predicting-video-views-through-a-sentiment-analy/
- https://ideas.repec.org/a/spr/joamsc/v54y2026i3d10.1007_s11747-026-01152-6.html
- DOI 10.1016/j.dss.2022.113820 (Koh & Cui, abstract via search summary)
- DOI 10.1167/9.12.10 (Cerf et al.)
- ETRA 2018, Yangandul et al. (via search summary)
- https://www.overseeros.com/blog/youtube-thumbnail-text-vs-title-study
- https://www.overseeros.com/blog/should-youtube-titles-be-questions
- https://gigazine.net/gsc_news/en/20210830-clickbait-effective/
- https://www.veritasium.com/videos/2019/5/23/my-video-went-viral-heres-why
- https://youtubehowto.substack.com/p/is-ab-testing-useful
- https://cogdogblog.com/2016/05/stop-the-madness/
- https://link.springer.com/article/10.3758/s13414-013-0605-z

#### Caveats
- **Blocked or unverified sources.**
  - YouTube watch pages returned a captcha, so the Veritasium transcript was not retrievable.
  - The vidIQ study page, ScienceDirect, Springer, ACM and Medium were blocked. Those findings rest on abstracts or secondary summaries.
  - The Rene Ritchie quote and the Todd Beaupré interview come secondhand via Search Engine Journal and ppc.land. Beaupré's 10% claim has no published sample.
- **The MrBeast memo** is unauthenticated.
- **Correlational data.** 1of10 and vidIQ use viral or breakout samples, and Cui et al. and Fang et al. are observational. None isolates causes.
- **Contradictions.**
  - 1of10 has negative titles winning, while Cui et al. has positive titles winning.
  - 1of10 has multiple faces beating single faces, while the small RED study has the opposite.
  - vidIQ's high face frequency does not conflict with 1of10's "no lift", because frequency is not lift.
- **Not found.** Verified named-creator A/B numbers for the educational channels you asked about, and any CTR-by-traffic-source benchmark with a stated method.

### D3. Psychology and visual perception of clicking

Full notes with DOIs and per-claim grades are in `research/psychology.md`.

Grades: [A] peer-reviewed or large dataset, [B] company or creator data, [C] opinion. I retrieved the abstracts myself (PubMed, Crossref, Europe PMC, PDF text) unless marked UNVERIFIED.

#### Five headline findings

1. **Curiosity peaks at a middle gap, not a maximal one.** This is the best-supported rule for the slice.
   - Kang et al. 2009 (Psychol Sci): curiosity was highest when confidence in the answer was about 0.45 to 0.55 [A].
   - Le Quéré & Matias 2025 (Sci Rep, DOI 10.1038/s41598-024-81575-9): a meta-analysis of 8,977 Upworthy headline A/B tests [A]. When the baseline headline was too vague, more concrete wording raised CTR. When headlines were too concrete, more concrete wording lowered it. Upworthy tested headline plus image as one package.
   - Frede et al. 2026 (J Cognition): showing people a moderate knowledge gap (33% known) raised the chance they read. Showing full knowledge lowered it [A].
2. **The brief's "every title is a question" rule is contested.**
   - Fang & Wheeler 2026 (J Consumer Psychology 36:470, DOI 10.1002/jcpy.70031) ran four studies [A]. They included 22,743 news A/B tests, 53,030 Reddit posts and a preregistered lab study of 400 people. Question-framed titles reduced engagement because they read as less informative.
   - Earlier work is mixed. Le Quéré's table shows 3 of 9 experiments negative, 2 positive and 4 null. Lai & Farbrot 2014 was positive. The +150% and +175% click figures for Lai & Farbrot came from a search summary, so they are UNVERIFIED.
   - All of this is about written headlines, not YouTube. It is UNVERIFIED for video.
   - Implication: keep the question, but make it concrete (named object, number) and let the thumbnail carry the specific stakes, so the question does not read as vague.
3. **Meaning beats raw saliency, and clutter costs attention.**
   - Henderson & Hayes 2017: when meaning and salience are separated, only meaning explains unique variance in gaze [A].
   - Einhäuser 2008: recognised objects predict fixations better than early saliency [A].
   - Rosenholtz 2007: clutter, including colour variability, hurts search [A].
   - Wolfe & Horowitz 2017 (DOI 10.1038/s41562-017-0058): five guiding factors are salience, top-down features, scene meaning, search history and value [A].
4. **Iconic faces work, and they read emotion fast.**
   - Kendall et al. 2016 [A]: at short exposures, emotion was identified more accurately on more cartoonised faces. High contrast and low feature complexity helped.
   - Churches 2014 [A]: upright emoticons drive a face-type N170 signal (n=20).
   - Öhman 2001 [A]: schematic threat faces were found faster than friendly ones.
   - The pop-out claim is contested. Becker 2011 [A] found no angry pop-out and a happy advantage instead.
   - Photographic faces are the ones with strong capture. Crouzet 2010 [A] found saccades to faces at 100 to 110 ms. Schematic-face pop-out is doubtful; Hershler & Hochstein's own abstract says earlier studies found no pop-out for schematic faces.
5. **A figure looking at the story object is better than a figure staring out.**
   - Sajjacholapunt & Ball 2014 [A], n=72, eye tracking on web pages. Averted gaze raised attention to the product and text and raised recall. Recognised brands per person: 1.50 for averted, 1.06 for mutual gaze, 0.54 for no face. Mutual gaze held attention on the face itself.
   - Friesen & Kingstone 1998 [A] used a schematic face (circle, eye circles with pupils, line mouth), and pupil direction still cued attention. I know this only from a search summary. Ristic 2002 [A] found arrows work the same way, but arrows are banned in your images.

#### Principles for a cartoon stick-figure disaster thumbnail

| # | Principle (evidence) | How to use it |
|---|---|---|
| 1 | Middle-sized gap (Kang, Le Quéré, Frede) [A] | Show the object and the stakes, but not the failure mechanism. The viewer should know what and where, and want to know how. |
| 2 | Curiosity raises retention (Gruber 2014, Neuron) [A] | A gap the video closes in the first 10 seconds pays off the click. |
| 3 | Picture first, but large text is read early. ETRA 2018 [A-]: thumbnails got about 2x the attention of title text, looked at first. Rayner 2001 [A] (print ads): large print was read before small print and picture. | Let the picture carry the idea. Keep any text to one large, short phrase. |
| 4 | One dominant subject (Pieters & Wedel 2004 [A], 1,363 ads: the pictorial captures attention regardless of size; text captures attention in proportion to its size) | Make one figure or structure at least about a third of the frame. |
| 5 | Sparse texture, meaningful design (Pieters, Wedel & Batra 2010 [A], 249 ads: dense feature complexity hurts brand attention, designed complexity helps) | Flat colour, few outlines, but a composed scene with a clear story. Do not use the full richly detailed backgrounds from the brief. |
| 6 | Pop-out is relative contrast (Wolfe & Horowitz; Rosenholtz) [A]. Valdez & Mehrabian 1994 [A]: saturation and brightness drove emotion more than hue. | Make one element differ from the rest. Use the palette's #e6b23a or #d94a38 on the key object against pale paper. |
| 7 | Gaze direction (Sajjacholapunt & Ball) [A] | Put the eyes on the hazard. Shift the dots and turn the head. |
| 8 | Tension before the event (Loewenstein; Mobbs 2007 [A]: closer threat produces more dread) | Show the moment before. The aftermath closes the gap. I found no study comparing before and after thumbnails: UNVERIFIED. |
| 9 | Anomaly needs a second look. Vö & Henderson 2009 and 2011 [A]: inconsistent objects were not detected off-fixation. Loftus & Mackworth 1978 said the opposite. | Put the wrong thing on the subject, not in the corner. |
| 10 | Scale (Proulx 2010 [A]: an irrelevantly large object captured attention) | Huge structure with a tiny figure gives size contrast. The awe and small-self link is UNVERIFIED for thumbnails. |
| 11 | Negativity (Robertson 2023, Nat Hum Behav [A]: each extra negative headline word gave +2.3% CTR; Soroka 2019, PNAS [A], 17 countries) | Worried or scared face plus a "wrong" structure. The data are headline words, not images. |
| 12 | Safe danger (Rozin 2013 [A]: people enjoy fear when they feel safe; the preferred level is just below intolerable) | Cartoon rendering is the safe frame. No gore, matching the brief. |
| 13 | Fluency (Reber, Schwarz & Winkielman 2004; Alter & Oppenheimer 2009) [A]: symmetry, figure-ground contrast and clarity raise liking and judged truth | Clear silhouette and strong outline contrast. |
| 14 | Centre composition. Palmer 2008 [A] found a centre preference for single subjects (a preference study, not CTR). | Centre one subject. The rule of thirds is unsupported for single subjects. |
| 15 | Familiarity is an inverted-U (Montoya 2017 meta-analysis [A]: 268 curves from 81 articles, inverted-U for visual stimuli). Value-driven capture (Anderson 2011 [A]). | Keep a fixed identity element (figure style, paper background, one colour). Rotate scene, emotion and colour. |

#### Myths and unsupported creator advice

- "Questions boost clicks": see finding 2.
- "Hide as much as possible": too vague loses.
- "Angry or anomalous things pop out": contested or refuted, as in principles 9 and finding 4.
- "80% brand recognition from colour" is a marketing statistic with no verified source. Secondary sources [C] say it came from colour-versus-monochrome documents. It is unsupported for thumbnails.
- Colour "psychology" is context-dependent. Elliot & Maier 2014 [A] say applications need generalisation first, per a web summary; I did not open the full text.
- "Rule of thirds", the "F-pattern" and "faces always first" are unsupported for phone thumbnails. The F-pattern comes from text-page studies and I did not test it.
- Text word limits (such as "3 words"): I found no study, so this is convention [C].
  - My own arithmetic, with stated assumptions: a full-width phone thumbnail keeps text legible, and a list-size thumbnail about 3x smaller sits near the edge of the fluent range from Legge & Bigelow 2011 [A].
  - The assumptions are a viewing distance of 35 to 40 cm and a thumbnail width of about 6.5 cm.

#### Sources (DOIs are in notes.md)

- Curiosity: Loewenstein 1994 (secondary sources only; scanned PDF could not be read); Golman & Loewenstein 2018; Kang 2009; Gruber 2014; Kidd, Piantadosi & Aslin 2012; Kidd & Hayden 2015; Ten et al. 2025 (Open Mind); Frede et al. 2026.
- Headlines: Le Quéré & Matias 2025; Fang & Wheeler 2026; Lai & Farbrot 2014; Scacco & Muddiman 2020; Kuiken 2017; Robertson 2023; Cui 2024 (JBR, secondhand summary only).
- Attention: Wolfe & Horowitz 2004 and 2017; Henderson & Hayes 2017; Einhäuser 2008; Rosenholtz 2007; Tatler 2007; Bindemann 2010; Anderson 2011; Pieters & Wedel 2004; Pieters, Wedel & Batra 2010; Rayner 2001; Yangandul et al. ETRA 2018; Legge & Bigelow 2011; Potter 2014 and Maguire & Howe 2016; Proulx 2010.
- Faces and gaze: Crouzet 2010; Hershler & Hochstein 2005; VanRullen 2006; Öhman 2001; Becker 2011; Kendall 2016; Churches 2014; Wardle 2020; Keys 2021; Liu 2014; Looser & Wheatley 2010; Farroni 2005; Whalen 2004; Senju & Johnson 2009; Sajjacholapunt & Ball 2014; Friesen & Kingstone 1998; Ristic 2002; Frischen 2007.
- Threat and safe danger: Soroka 2019; New 2007; LoBue & DeLoache 2008; Mobbs 2007; Vuilleumier 2005; Võ & Henderson 2009 and 2011; Rozin 2013.
- Fluency, colour and composition: Reber 2004; Alter & Oppenheimer 2009; Valdez & Mehrabian 1994; Elliot & Maier 2014; Palmer 2008; Hunt 1995.
- Familiarity: Montoya 2017; Burke 2005; Bornstein 1989 (existence only).

#### Caveats and UNVERIFIED

- Nothing I found tests cartoon or stick-figure thumbnails for CTR. Every principle is an extrapolation from lab attention or headline data.
- Most headline evidence is news headlines from Upworthy in 2013 to 2015, not thumbnails or YouTube.
- Facebook's "1.7 seconds per mobile item" [B] is a company-commissioned figure. I did not open the primary document. Treat it as "about 2 seconds".
- I could not read the Loewenstein 1994 scan. The "priming dose" idea is from secondary sources.
- Not verified:
  - Bornstein 1989 numbers.
  - Campbell & Keller wear-out.
  - Meyers-Levy & Tybout's moderate-incongruity finding.
  - The Lee & Feeley identifiable-victim effect size (I recall r ≈ .05, UNVERIFIED).
  - Piff 2015.
  - Morbid-curiosity scales.
  - The Lindgaard 50 ms numbers.
  - Working-memory limits of 3 to 4 items and about 3 to 4 fixations per second, which I know from memory only.
- Not searched: emotional contagion from emoji or cartoon faces, caricature or exaggeration effects, and faces without eyes.
- The dot-eye, no-eye-white figure is untested for fear signals. Whalen 2004 is about real eye whites.
- Habituation to a consistent thumbnail identity has no quantified study. A/B test it.
- Ethics of tragedy thumbnails: no research found. The brief's rules are the only guide.

### D4. Audit of the engineering-disaster and documentary niche

Notes, index and images are in research/niche-audit/. The key files are notes.md, index2.csv, thumbs/ and sheet_*.jpg.

#### What I did, and what I did not do
- I parsed 58 channel /videos pages (Latest and Popular sort) and downloaded 405 thumbnails.
- **Visually classified: about 105 thumbnails**, in nine 12-up contact sheets, because of the budget cap. About 300 more were only measured programmatically.
- View counts are as listed on channel pages on 2026-09-30, rounded by YouTube. I could not parse exact counts from watch pages. A few exact counts come from search pages and are marked "search page".
- I did **not** read comments. Audience reactions are UNVERIFIED.
- No CTR data exists outside your own YouTube Studio. Nothing here shows a thumbnail caused views. Views depend on age, topic and search demand, so I only compare within a channel.

#### Channels checked
- **Verified and used, direct niche:** Practical Engineering, Real Engineering, Mentour Pilot, Fascinating Horror, Plainly Difficult, Disaster Breakdown, The B1M, Sabin Civil, Dark Records, Brick Immortar, Mayday, Oceanliner Designs, Kyle Hill and Two Bit da Vinci.
- **More direct niche:** USCSB (official 3D animations), Andy R Animations, Infographics Show, Scott Manley, Adam Something and Tom Scott.
- **Dark Docs:** exists, but mostly military history.
- **Newer or small channels I found by search:** The Hydraulic Record (25K subscribers), Overengineered (11.5K), Beyond Sky (38K), Forgotten Disasters (7K), Iron and Memory (19K), Storified (164K), What On Earth Is This? (109K) and That Chernobyl Guy.
- **Explainer neighbours:** Veritasium, Vox, Wendover, PolyMatter, Half as Interesting, LEMMiNO, Mustard, fern, Just Have a Think, Jared Owen, Cleo Abram, RealLifeLore and Joe Scott.
- **Cartoon analogues:** Ink Explainer (@Inkexplainer96, 106K subscribers; @InkExplainer is a different channel), OverSimplified, Simple History, Casual Geographic, Simple Paint, Kurzgesagt, TED-Ed and MinuteEarth.
- **Not relevant:** Insider and Grunge exist, but neither has disaster documentaries in its top 14. Insider is lifestyle and "how it works". Grunge is celebrity trivia.

#### Key findings

1. **The niche is photographic, dark and text-led.** [B/own analysis]
   - Across 268 direct-niche thumbnails, the average brightness is 0.43 (0 to 1). Near-white pixels are 8% and dark pixels are 21%.
   - Cartoon channels average 0.52 brightness, 20% near-white and 15% dark.
   - Nobody in the disaster niche uses flat hand-drawn illustration for the thumbnail. The nearest are Storified (dark, stylized 3D victims) and the Infographics Show (flat vector).

2. **Global colour, brightness and busyness do not separate strong from weak thumbnails within a channel.** [own analysis, confounded by video age]
   - I compared top-viewed with lowest-viewed thumbnails in 32 channels. Mean differences were tiny: brightness +0.012, saturation +0.004, edge density -0.002.
   - The top thumbnail was "more" of a trait in only 12 to 19 of 32 channels, a coin flip.
   - Within a channel, the strong and weak videos often share the same template. Brick Immortar's 4.8M El Faro and its 300K Forth Bridge use the same layout. Topic recognition and search demand appear to dominate. Do not copy a look on the strength of its views alone.

3. **Text is short and blunt.** [own eyeball tally]
   - Among about 75 viewed thumbnails with text, the median is 3 to 4 words and the maximum is 7.
   - Text is usually in the top-left or right third, in heavy condensed sans or gothic serif.
   - A hard number often carries the hook: "62 DAMS GONE", "1,500 TONS OF TNT", "161 PEOPLE", "8,000 FEET DOWN".
   - Thumbnails almost never carry a question. The title does that job. Exceptions: "WHAT REALLY HAPPENED?", "WHAT WAS BOEING THINKING?" and "Worst Recall in History?".

4. **Faces are rare in this niche.** [own tally]
   - Only The Hydraulic Record puts a person on every thumbnail: the same worried presenter, looking sideways toward the hazard. That is a 25K-subscriber channel with 2M and 1M views on recent videos. Causation is UNVERIFIED.
   - Practical Engineering shows a smiling host on 2 of 6.
   - Aviation and structure channels show no faces.

5. **The "moment before" is almost never shown.** [own observation]
   - Nearly all thumbnails show the intact structure (El Faro, Thresher), the explosion or fire, or the wreckage.
   - Only Storified's "26 PEOPLE" (a bus heading for a broken bridge) and the Infographics Show's "SMALL THING, BIG OUTCOME" (a key becoming a sinking Titanic) come close to a decision or cause.
   - The Infographics Show video, "Small Decisions That Caused HUGE Impacts on History", has 957,455 views (search page). It is the closest existing match to your "chain of small decisions" idea.

6. **A close analogue to your style is doing very well.** [B]
   - Ink Explainer uses stick-figure cartoons in full scenes, a question title, and a 2 to 3 word yellow or white caption ("NO JOBS", "RAINED ALL WEEK", "Why Us?").
   - "What Did Ancient Humans Actually Do All Day?" has 9.7M views in about a month, on a 106K-subscriber channel. The median of its top 14 is about 340K, so that video is a roughly 28x outlier. Whether it was organic is UNVERIFIED.
   - Its other videos run from 15K to 1.5M. The style is proven for prehistory, not yet tested for disasters.

7. **Tragedy handling runs on a spectrum.** [own observation]
   - Most channels show the structure or vehicle and no bodies. This covers Brick Immortar, Fascinating Horror, Plainly Difficult, Hydraulic Record and Mentour.
   - Some state a casualty count as the hook: "165 DEAD IN ONE NIGHTCLUB", "161 PEOPLE".
   - Storified is sensational: "IMPALED", "BRUTAL DEATH", "DIED IN 0.12 SECONDS". It still has the biggest numbers on its channel (14M, 5.7M, 2.7M). So sensationalism can get views, but it conflicts with your tone rules.
   - Plainly Difficult's "Worst Recall in History?" shows a crash-test dummy with an airbag.

8. **Low-view copycat channels are crowding the format.** [own inference from search pages]
   - Many tiny channels (hundreds of views) use titles like "One Small Change on a Drawing Killed 114 People". That phrasing is getting crowded.

#### Top formulas

Views are as listed on channel pages on 2026-09-30 unless marked otherwise.

| # | Formula | Examples (title, channel, ID, views) | Photo-dependent? |
|---|---|---|---|
| 1 | 2 to 4 blunt heavy words over a full-bleed scene | Nepal Flood, Hydraulic Record, 9pH_3n23_8o, 2M ("WHERE THE FLOOD WENT"). Banqiao Dam, CFnh54FeNo0, 358K ("62 DAMS GONE"). 400 km Wall Japan Built, Overengineered, Eg0djVfKXU8, 4.2M ("JAPAN DID IT") | Text idea translates. The scene photo does not. |
| 2 | Worried face looking toward the hazard | Oroville, Hydraulic Record, mwwdnfaNKxk, 132K ("3 FEET FROM DISASTER"). Glen Canyon, 5_hKEz4v0pw, 157K ("SAVED BY PLYWOOD"). Groundwater, Practical Engineering, bY1E2IkvQ3k, 14M (smiling host) | Translates: stick figure with a worried face and gaze direction. |
| 3 | Giant one-word title plus tiny letter-spaced tagline over one lone object on plain sky or sea | El Faro, Brick Immortar, -BNDub3h2_I, 4.8M. Thresher, g-uJ1do3yV8, 4.7M. Texas Tower 4, yal0RZvzW-0, 2.4M | Layout translates. The photo does not. |
| 4 | Sepia or monochrome archival photo plus gothic serif headline | Sunshine Skyway, Fascinating Horror, EPaBRegvkuQ, 4.6M. Halifax Explosion, VA8jIgvA8fo, 2.6M. Bath School, Forgotten Disasters, xa4d7sXaDgc, 178K | Photo-only. Sepia toning could be imitated but is not core. |
| 5 | Red circle, arrow or dashed line on a photo or diagram | Demon Core, Plainly Difficult, VE8FnsnWz48, 7.9M. Sodium Reactor, 7-NKdWV5SCg, 1.6M. 777X, Beyond Sky, 4UM9ZJx6fLI, 1.2M | Overused. Your brief bans arrows in scene images. |
| 6 | Cutaway or cross-section | What's inside the Titanic?, Jared Owen, HLrBUwNSEo0, 22M. Golden Gate, Sabin Civil, E6tp8DCAJ-0, 19M. Groundwater, Practical Engineering, bY1E2IkvQ3k, 14M | Translates well. The brief allows see-through cutaways. |
| 7 | Tiny person for scale against something huge, or the moment just before | Beach Holes, Practical Engineering, 0kQXOTcEB_E, 7M. Sunshine Skyway, Storified, 0QXvhtPaKoY, 613K ("26 PEOPLE") | Translates directly. |
| 8 | A number as the hook | Beirut, Dark Records, NgQ7jh9mrWs, 4.8M ("1,500 TONS OF TNT"). Kaprun, 0SFcWZx3L4g, 2.7M ("161 PEOPLE"). Golden Gate, E6tp8DCAJ-0, 19M ("27000!") | Translates. Matches your "stakes in plain numbers" rule. |
| 9 | Gory dramatization with red arrows | Killed in 4 Milliseconds, Storified, iorhSlFYpDc, 2.7M ("IMPALED"). Plate Taille Dam, 4_2BBjCJcvU, 2M ("BRUTAL DEATH") | Avoid. It breaks your "no graphic injury" rule. |
| 10 | Vehicle cut-out on a blue gradient with fire clip-art and a "real story?" caption | Concorde, Mentour Pilot, C-nALYF73hU, 16M. Tenerife, 2d9B9RN5quA, 11M. Air Canada, Disaster Breakdown, wSmtnuFoAv0, 1.4M | Partly. The layout translates, the fire clip-art does not. |
| 11 | One object on a plain light background plus an accusatory caption and curved arrow | China's A320 Clone, Beyond Sky, JeVIb9K6a5U, 1.6M ("CHINA'S BIG MISTAKE"). 777X, 4UM9ZJx6fLI, 1.2M ("BUILT BY CLOWNS") | Translates. It is clean and bright. |
| 12 | Emotive cartoon character in a full scene plus a 2 to 3 word caption | What Did Ancient Humans Do All Day?, Ink Explainer, 49_Ph2q6uIM, 9.7M. Rained All Week, SD7XyG2wd1k, 1.5M. Why Us?, OCr6NteWSQ8, 1.2M | Native to your style. |
| 13 | "Small thing, big outcome" split | Small Decisions That Caused HUGE Impacts, Infographics Show, vRAsU_ov84Q, 957,455 (search page) | Translates. It is your core concept. |

**Overused across the niche:** red circle and arrow, fire and explosion clip-art, all-caps condensed text, monochrome archival photos, brand corner logos, and the intact-structure-on-water shot.

**Series templates:** Real Engineering ("THE INSANE ENGINEERING OF X" on a glowing render), Disaster Breakdown and Hydraulic Record all repeat one layout. Repetition is normal in this niche.

**Weak thumbnails.** Weak ones often share the strong ones' template. Examples I saw:
- Fascinating Horror's typographic Shorts compilation: 74K.
- The Disaster Breakdown April Fools thumbnail: 67K.
- Real Engineering's 1926/2026 split of the Sagrada Familia: 413K.
- The B1M's text-less Tokyo aerial: 358K.
- Each is a single example, so treat these as weak signals.

#### What would translate to your flat cartoon style
- A single stick figure with one clear emotion, looking toward the threat, in a full illustrated scene (formulas 2, 7, 12).
- A tiny figure against a huge structure or hazard (formula 7).
- A see-through cutaway of the failing part (formula 6). The brief allows this and it is common in the niche.
- The "moment before": the calm ordinary scene just before the failure, or the decision moment. Almost nobody shows it. Pair it with a "small thing, big outcome" split (formula 13).
- 2 to 4 words of caption, ideally carrying a number (formulas 1 and 8), added in design. Your image rules ban text inside the picture, so the caption has to be composited on top.
- A bright, warm, light-filled scene (cream, sky blue, green, yellow, red) against a niche that skews dark and photographic. That should make a cartoon thumbnail stand out in a feed. Whether it lifts CTR is UNVERIFIED.
- A torn-paper cutout revealing the breach, as on Practical Engineering's Taum Sauk thumbnail. It could be redrawn in flat style.

**Does not translate:** archival and real-footage photos, fire and explosion clip-art, and real-face presenters. Arrows and red circles conflict with your "no arrows" rule. If you want that highlight effect, colour the key part and pale the rest, as your brief already suggests.

**Design conflict to flag:** your brief bans text in images, but every high-view thumbnail here carries 2 to 4 words. Decide whether thumbnails are exempt.

#### Sources (all fetched 2026-09-30)
- YouTube channel /videos pages for the 58 channels above, Latest and Popular sort. Handles are in notes.md.
- YouTube search result pages, queries such as "engineering disaster explained", "why did the dam fail" and "how small decisions caused disaster explained".
- i.ytimg.com thumbnails (maxresdefault, hqdefault fallback) for all 405 videos.
- The unrelated WebSearch snippets returned only general listings and were not used for any claim.

#### Caveats
- Grades: view counts and channel data are [B]. The visual classifications and the brightness, saturation and busyness statistics are my own analysis, not [A] sources. Comments were not read, so audience reactions are UNVERIFIED.
- The Popular-sort counts are rounded to two significant figures.
- The "top" group is older videos and the "low" group is recent ones, so age is a confound.
- About 300 of the 405 thumbnails were measured but not visually inspected.
- Grunge and Insider are not relevant to this niche.

### D5. Audit of cartoon and stick-figure explainer channels

Everything is in `research/cartoon-audit/`. Main files: `notes.md`, `index.csv`, `sheets/`, `ranksheets/`, `sheets/phone_test_176px.jpg`.
- `index.csv` has 462 thumbnail rows from 52 channels. About 35 of those channels are truly cartoon or illustrated. Views are YouTube's rounded strings scraped on 2026-09-30.
- I looked at the contact sheets, all-video rank sheets and one full-size montage. That covers roughly 300 of the 462 thumbnails, not all of them.
- I pulled Popular-sort lists through the YouTube browse API.
- "Weak" means the lowest-viewed of a channel's last 20 long-form uploads that are at least 21 days old.
- I excluded non-cartoon channels from the conclusions: Bobby Duke, Kaptain Kristian, Professor Of How, Yellow Dude, Fascinating Horror, Wendover, HowMoneyWorks.

#### Key findings

**1. [B] Ink Explainer's top 6 all share one recipe.**
- The real channel is `@Inkexplainer96` (106K subs, 16 long videos). `@InkExplainer` is a different, 39-sub channel.
- All six top thumbnails have a full illustrated scene behind the figures (cave, savanna, desert or snow).
- Each shows 1-3 stick figures with a round white head, circle eyes with lids, single-line limbs and one costume as the only prop.
- Each has 2-3 words of ALL-CAPS text in the top third, in yellow or white with a thick black outline.
- The text teases an answer instead of repeating the question. "What Did Ancient Humans Actually Do All Day?" (49_Ph2q6uIM, 9.7M) carries "NO JOBS".
- Its 3 weakest are a white-background IKEA-effect thumbnail (15K), a dark skeleton cave (37K) and a crowded battle (42K). Topic differs too, so this is not clean.

**2. [B] The same template gives wildly different results, so template is not enough.**
- Clone channels on the Ink Explainer format: Explain In Paint, Zenn, Axen, HUMAN-ISH.
- HUMAN-ISH (4.2K subs) has one 548K video (xkr2DJ_dlWI) beside 4-12K videos on the identical layout.
- I measured brightness, saturation, edge density (a clutter proxy), and yellow, white and black share in top versus weak thumbnails. None separated them (44 channels; top > weak in 17-29 of 44 for every metric, i.e. coin-flip).
- Topic, title and age dominate view counts. All-time top versus recent weak is confounded by age.

**3. [B] Phone test at 176 px wide, on light and dark feed.**
- Pale or white-background thumbnails lose their edge on the white feed and only pop in dark mode. Examples: the IKEA thumbnail, Zenn "ARE WE ALIENS?", MinuteEarth, Casually Explained, Sam O'Nella.
- Saturated full-scene thumbnails keep a clear boundary in both modes.
- 1-3 word text at about 30% of frame height stays legible. Small labels, before/after captions and 2-line text do not.
- Figures under about 12% of frame height read only by posture, not by face.

**4. [A] YouTube's own A/B tool optimizes watch time share, not CTR.**
- Quote: "we optimize tests for overall watch time over other metrics, like click-through-rate". Up to 3 variants.
- Source: support.google.com/youtube/answer/16391400.

**5. No source I found compares stick or cartoon thumbnails with realistic ones on clicks.**
- [A] The 1of10 Media dataset (300K+ "viral" 2025 videos) says thumbnails with and without faces "perform similarly". It covers real faces only and viral survivors only.
- [A] Lab study, Zhao et al. 2019 (PLoS One, N=17): cartoon faces get faster, larger early neural responses; real faces get more late attention. It measures brain response, not clicks.
- [A] Simple downward-V shapes (angry-brow geometry) are detected faster than upward ones (Larson et al. 2007). Wang & Zhang 2016 found only weak behavioural effects. I verified only the citations and abstract snippets.
- **Myths and UNVERIFIED claims:**
  - "Emotional faces give 2.3x CTR" (cited to Creator Insider): UNVERIFIED.
  - "60% of top thumbnails use complementary colors": UNVERIFIED.
  - Any claim that stick figures are better or worse than realistic people: no evidence either way.

#### Top 12 formulas (channel, title, video ID, views as fetched)

1. **Giant relaxed or close hero plus a 2-word twist.**
   - Ink Explainer, "What Did Ancient Humans Actually Do All Day?", 49_Ph2q6uIM, 9.7M.
   - Zenn, "What Did Ancient Humans Do at Night?", st_Ah6Ykbh4, 8M ("2 SLEEPS?").
   - Axen, "…Before Jobs Existed?", TQd2k1pEXp4, 3.3M ("FREE ALL DAY").
2. **Enclosed tableau with a light source (fire or moon) and 2-4 figures.**
   - Ink Explainer, "…When It Rained All Week?", SD7XyG2wd1k, 1.5M.
   - Ink Explainer, "The Disturbing Ways Ancient Humans Survived Winter", dp3jYZXKOos, 756K. This one is a see-through cutaway of a mammoth carcass, a precedent for your cutaway style.
   - Axen, "…Survive Deadly Winters?", wt_7Hp7d7I8, 932K.
3. **Tiny figure against a huge object or threat (scale contrast, object as hero).**
   - Zenn, "Why Hasn't Anyone Raised the Titanic?", IlCq6a0sDCk, 706K.
   - Axen, "…Deadliest Predators?", 2RJggsjlj4A, 1.3M (black predator silhouette).
   - Simple History, "Schwerer Gustav", GGPxesCB8ns, 16M.
4. **Split panel: before/after, start/end, then/now.**
   - JarToon, "The ENTIRE Story of Clarence…", L698u3f92eE, 7.7M.
   - ClipperFlipper, "Titanic VS Iceberg at Different Speeds", tMvpB6cBjYk, 4.6M (23 MPH vs 810 MPH).
   - Infographics Show, "How SEAL Team Took Down Osama bin Laden", knjliFs3gR8, 20M (3:33 AM vs 3:39 AM).
   - Animated History, "1500 Years of Russian History…", pBJpDpMqigw, 1.1M.
5. **A number or label as the hero.**
   - Explain In Paint, "How Ancient Humans Survived Brutal Winters?", Q3_htAFS7wg, 398K ("-58°F?").
   - Kurzgesagt, "The Largest Star in the Universe", 3mnSDifDSxQ, 35M.
6. **Question fragment, or the whole question, as thumbnail text.**
   - History Matters, "Why does Russia Own Kaliningrad…", H5K4tq-9osc, 6.8M (full question, big and rotated).
   - Explain In Paint, "How Ancient Humans Actually Created Dogs?", nv7HuwnofW0, 935K ("FIRST DOG?").
   - HUMAN-ISH, xkr2DJ_dlWI, 548K ("PREGNANT?").
7. **Series wrapper plus one keyword.**
   - OverSimplified, "WW2 (Part 1)", _uk_6vfqwTA, 105M.
   - OverSimplified, "The Cold War (Part 1)", I79TpDe3t2g, 74M.
   - Historia Civilis, "The Longest Year in Human History", fD-R35DSSZY, 7.3M. This one has no characters at all, only type and an icon.
8. **Host plus a lineup of exaggerated faces.**
   - Sam O'Nella, "Historical Misconceptions…", 0zMSMJZc9EA, 23M.
   - Casually Explained, "Is She Into You?", xa-4IAR_9Yw, 22M (10 years old).
9. **Anthropomorphized object with eyes.**
   - Kurzgesagt, "The Coronavirus Explained", BtN-goy9VOY, 89M.
10. **Direct address ("you're X" or a guide title) on a dark background with one figure and props.**
    - StickFigure Explains, "how to actually quit any addiction…", Yh_7y2PYH1o, 4.5M.
    - easy, actually, "becoming smart is easy, actually", C5OJJD3Eytk, 9.7M.
11. **One huge crying or shocked face plus a hand-drawn arrow and 2-4 words on white.**
    - Hypothetically, 24VpqQN2gfY, 2.9M.
    - Bernard, BNHe5KNOW6A, 2.5M.
    - StickTory, RB5OXgw6bvw, 2.1M.
    - These channels use shock and gore content that conflicts with your brief. Borrow the layout only.
12. **One person in one dramatic moment, with the caption as a headline.**
    - Simple History, "The Medic Who fought a War without a Weapon", b8AggbAVSNQ, 14M.
    - Simple History, "Sniper Decoys: Dummy Heads", zvBiIvKUiOQ, 23M.

**Disaster subjects:**
- Ship and bridge animations work as object-as-hero. ClipperFlipper's Titanic set reached 6.2M (8GfRo_IKlEA) and 4.6M.
- Joseph Engineering's Baltimore bridge video got 689K (GsjAjlTnLNg) on a 7.5K-sub channel. It looks news-driven and 3D with arrows.
- I found no large stick-figure engineering-disaster channel. That is not proof none exists.

#### Identity and template
- The top performers keep one layout and change only scene, emotion and scale. Ink Explainer, Zenn, Axen and Explain In Paint all put text on top, the figure lower, and a full scene behind.
- OverSimplified, Sam O'Nella and Historia Civilis use rigid branded templates. Kurzgesagt varies composition but keeps a constant palette, outline and eyes.
- Palette pattern on the strongest thumbnails: saturated mid-tone sky or dark warm interior, a fire-orange accent, and yellow text with a heavy black outline. This is my observation, not a measured rule.

#### Stick-figure face and pose vocabulary (from what I saw, [B]/[C])
- **Calm or chill:** eyes closed or half-lidded, tiny smile or flat mouth, reclined diagonal body, arm behind head (NO JOBS).
- **Tired or miserable:** half-lidded circle eyes with red rings, slumped shoulders (Ink Explainer "TRAVEL HOW?" and "RAINED ALL WEEK").
- **Worried:** wide circle eyes with tiny pupils looking sideways, wavy mouth, sweat drop (Ink Explainer "Why Us?", Zenn "THAT'S ME?").
- **Shock:** huge circle eyes, small centered pupils, open O mouth, hands on head (HUMAN-ISH "NO HOSPITAL?!").
- **Skeptical:** one flat brow, sideways glance.
- **Anger:** V-shaped brows and gritted teeth (Axen "NO SCHOOLS", StickFigure Explains "you're lazy").
- **Dread from scale:** a small, stiff figure whose gaze leads the eye to the huge object (Zenn "RAISE IT?").
- **Body language:** single-line arms and legs still read: a pointing arm, an X of crossed arms, a long lounging leg.
- **Sizing:** exaggerate the eyes (about a quarter of head width) and make the face at least about 25% of frame height when it is the hero. Mouth lines vanish at phone size. One prop, at least about 15% of frame, tied to the question.

#### Mistakes to avoid
1. Pale or white flat backgrounds. They vanish on the white feed (Ink IKEA, 15K).
2. Tiny figures in wide scenes. Faces become blobs (Ink "FIRST GUN?", 42K).
3. More than 3 words of text, or small captions and before/after labels.
4. Dark scene with dark hero and low contrast (Ink "I WILL DIE", 37K).
5. Grids of tiny labelled pictures. They work only on strong topics and are unreadable on a phone.
6. Repeating the title as thumbnail text.
7. Breaking identity with one-off art: Zenn's plain dog cartoon (14K) and an old-photo thumbnail (16K).
8. Copying a template and expecting it to carry a weak topic.
9. Gore or sexualized shock. It gets clicks on other channels but breaks your brief.
10. Yellow text on pale backgrounds or white text on pale backgrounds.

#### Implications for Stress Riser
- Your pictures already match the Ink Explainer look: scene-filled, flat colors with black outlines, and lidded-eye stick figures. The thumbnail levers left are figure scale, 1-3 words of text, and one prop or object as hero.
- Strong candidates for your 10 distinct styles are formulas 1-4, 6, 7, 10 and 12, plus a disaster object-hero version of 3 (bridge, dam or ship) and a number-hero version of 5. Formulas 8, 9 and 11 are the weakest fits.
- Your brief forbids text and arrows inside scene images. Thumbnail text has to be a separate overlay layer. Check this with the user.

#### Sources
- YouTube channel /videos pages and the Popular sort for 52 channels, fetched 2026-09-30 [B].
- YouTube Help, A/B test titles and thumbnails: https://support.google.com/youtube/answer/16391400?hl=en [A]
- YT Wealth Media, Ink Explainer case study: https://www.ytwealthmedia.com/case-studies/ink-explainer/ [B]. It gives 77.8K subs at month 8 and 3.7M views in 28 days. Revenue figures are third-party estimates.
- OutlierKit, Explain In Paint: https://outlierkit.com/channel/explaininpaint1 [B, tool estimate]
- Search Engine Journal on the 1of10 data: https://www.searchenginejournal.com/do-faces-help-youtube-thumbnails-heres-what-the-data-says/563944/ [A/B]
- Zhao et al. 2019, PLoS One: https://pmc.ncbi.nlm.nih.gov/articles/PMC6328201/ [A]
- Wang & Zhang 2016, Frontiers in Psychology: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00917/full [A]
- Larson, Aronoff & Stearns 2007, doi 10.1037/1528-3542.7.3.526 [A]
- Larson et al. 2009, doi 10.1162/jocn.2009.21111 [A]
- Citations verified in Crossref, abstracts not read [A]:
  - Aronoff et al. 1988, doi 10.1037/0022-3514.54.4.647
  - Lundqvist et al. 1999, doi 10.1080/026999399379041
  - Öhman et al. 2001, doi 10.1037/0022-3514.80.3.381
  - Sadr et al. 2003, doi 10.1068/p5027
- channelslike.com and facelesslist.com channel lists [C]; stickfiguremaker.com tips [C].

#### Caveats
- No CTR or impression data exists outside the channel owners. Every "what works" line is a pattern in view counts plus my visual coding, not causal.
- View strings are rounded, ages run from 3 days to 13 years, and top-versus-weak comparisons are confounded by topic and age. Old giants like Kurzgesagt and OverSimplified show what accumulated over years, not what a new channel can expect.
- Not verified: how these creators make their thumbnails (no interviews found), revenue figures, and the abstracts of the older schematic-face papers.
- A `rm` of the `thumbs/` folder was blocked by the safety check, so some stale weak-thumbnail files remain in it. I did not work around the block. `index.csv` references only the current files.

### D6. Design system, color math and production workflow

Folder: research/design-system/
Full notes with URLs: notes.md. All 45 pairs: palette_report.md and palette_pairs.csv.
**Preview script: research/design-system/tools/thumb_preview.py**
Usage: `python3 thumb_preview.py img.png --title "..." --duration 10:24 --safezone`, or `--demo`. Pillow is installed here; the other scripts also need numpy, fonttools, scipy and rapidocr-onnxruntime.

Grades: [A] official or peer-reviewed, or a measurement I made myself. [B] company or creator data. [C] opinion or SEO blog.

#### 1. Palette maths (my computations, checked against published reference values) [A]
The palette has only three lightness tiers.
- LIGHT: white L*100, paper 93, sky 88, amber 75, tan 75, light green 72.
- MID: red 52, brown 49, dark green 48.
- DARK: ink 9.
- Colours inside one tier cannot be told apart by lightness in grayscale, blur or colour-blind vision. Only hue separates them.

Thresholds I used:
- WCAG text needs 4.5:1, and non-text needs 3:1.
- Material's own code comment says an L* gap of 40 guarantees at least 3:1 and a gap of 50 guarantees at least 4.5:1.
- APCA Lc levels: 90 preferred body, 75 minimum body, 60 minimum fluent text, 45 minimum large text, 30 any text, 15 invisible.

My rule: a gap of 50 or more is text-safe, 40–50 suits big bold text, 25–40 suits big flat shapes only (add an outline), and under 25 is luminance-invisible.

| pair | WCAG | dL* | dE2000 | APCA Lc | worst colour-blind dE2000 | use |
|---|---|---|---|---|---|---|
| ink/white | 17.4 | 90.7 | 86 | 104 | 86 | text and outline |
| ink/paper | 14.6 | 83.7 | 84 | 92 | 83 | text |
| ink/sky | 12.7 | 78.4 | 79 | 84 | 77 | text |
| ink/amber | 8.95 | 66.2 | 66 | 65 | 62 | text; amber's best pairing |
| ink/light green | 8.1 | 62.9 | 61 | 60 | 57 | text |
| white/dark green | 4.85 | 52.2 | 45 | -79 | 42 | white text |
| white/brown | 4.6 | 50.8 | 42 | -77 | 40 | white text |
| white/red | 4.2 | 48.2 | 44 | -73 | 38 | white text |
| ink/red | 4.1 | 42.5 | 43 | 34 | 31 | outline yes, ink text no |
| paper/red | 3.5 | 41.2 | 41 | -60 | 31 | big text |
| red/sky | 3.1 | 35.9 | 52 | -51 | 40 | best red accent background |
| sky/paper | 1.15 | 5.3 | 18 | -8 | 14 | FAIL |
| white/paper | 1.2 | 7.0 | 9 | -11 | 8 | FAIL |
| white/sky | 1.37 | 12.3 | 14 | -21 | 9 | FAIL |
| tan/amber | 1.01 | 0.5 | 14 | 0 | 7.7 | FAIL |
| dark green/red | 1.15 | 4.0 | 54 | 0 | 5.5 | FAIL for colour-blind viewers |
| brown/red | 1.09 | 2.5 | 19 | 0 | 2.9 | FAIL |
| dark green/brown | 1.05 | 1.4 | 31 | 0 | 3.7 | FAIL |
| light green/amber | 1.11 | 3.3 | 26 | 0 | 4.3 | FAIL |
| light green/tan | 1.09 | 2.9 | 24 | 0 | 7.8 | FAIL |
| light green/red | 1.96 | 20.4 | 59 | -26 | 13 | weak |

Other findings:
- **(a) Text.** White or paper fill with an ink outline works on every palette colour. Ink text needs a light background. Never use red, brown or green as a text fill.
- **(b) Subject against background.** The white head pops on dark green, brown, red and ink (dL* 48–91). It relies on its outline on sky or paper.
- **(c) Outlines.** Ink is at least 3:1 against every palette colour (the minimum is ink/dark green at 3.59). It is the universal outline.
- **Accent.** Red is the default. Saliency proxy on 168x94 cluttered scenes (Achanta frequency-tuned saliency, 40 scenes per cell): the accent disc was the most salient point in 95% of scenes for red and 69% for amber.
  - Amber fails on light green (2%) and brown (8%).
  - Amber on ink is the only strong amber pairing (dL* 66).
  - Red is weaker on brown and ink.
  - The proxy overrates chroma, so it wrongly favours amber on tan. Treat amber/tan and red/brown as failures. This is a model, so [C].
  - The two accents must never touch: amber/red has dL* 23.7 and a colour-blind dE2000 of 17.7.
- **Colour-blind viewers.** NEI: about 8% of men and 0.5% of women of Northern European descent have red-green deficiency. In simulation (Machado 2009) red becomes olive (#726835 protan, #968733 deutan), the same as dark green. Red on green or brown scenes loses its accent for them.
- **Pale colours on the light feed.** Sky and paper against the white page score 1.37 and 1.15, so the card edge dissolves (see tools/out/demo1_sheet.png). Keep a mid or dark band or an ink border along the image edges.

#### 2. Feed sizes: first-hand measurements [A]
I requested YouTube's own JSON on 2026-09-30.
- Desktop search asks for 360x202 and 720x404.
- The watch-page sidebar asks for 168x94 and 336x188, and sometimes 196x110 and 246x138.
- Mobile web asks for up to 686x386, which is 2 x 343 CSS px.
- The desktop home card is 310–500 px wide. This comes from YouTube's skeleton CSS.
- Page background is #ffffff in light mode and #0f0f0f in dark mode, also read from YouTube's CSS.
- Phone widths (StatCounter, Aug 2026): 414 is the most common in the US, UK, CA and AU (21–30%), then 390 (12–14%), then 393/402/375/360. A full-width card is therefore about 360–414 px wide.
- Native app card sizes: UNVERIFIED, because the iOS and Android client APIs refused my requests.
- YouTube serves every thumbnail as a 1280x720, 4:2:0 JPEG of roughly quality 90 (72–367 KB in 20 samples).

Official upload spec (support.google.com/youtube/answer/72431) [A]: 3840x2160 recommended, minimum width 640, JPG or PNG, 16:9, 2 MB limit from mobile and 50 MB from desktop.
- Test & Compare allows up to 3 variants and picks the winner by watch-time share, not click-through rate.
- If any test thumbnail is under 720p, all are downscaled to 480p.

Myths:
- "1280x720, under 2 MB" is outdated.
- "168x94 on the phone feed" is wrong. It is the desktop sidebar size.
- SEO size lists such as "246x138 search" and "156x88 mobile" match nothing I measured [C].
- "38% higher click-through rate from consistency" and "70/30 rule" have no method behind them [C].

Device share:
- TV passed mobile for US watch time in December 2024 (YouTube CEO letter, Feb 2025) [B].
- Chartbeat: 69% of views are on mobile, but TV gives 42% of minutes [B].
- Phones dominate impressions, but thumbnails must also survive big screens.
- Dark-mode share numbers are unsourced: UNVERIFIED.

The rig renders light, dark, grayscale and blur columns at 360, 390, 310 (desktop home minimum), 246 and 168 px, with rounded corners, the badge, an optional title, a watch bar and a safe-zone overlay. The badge geometry is my approximation. The rig is pessimistic, because real phones are 2–3x sharper.

#### 3. Text overlay (1280x720 canvas)
Needed cap height on the master is the displayed cap height times 1280 divided by the displayed width.
- Comfortable is 12 px displayed (about 19 arc-min at 36 cm). That is 91 px on the master for a 168-wide thumbnail, 62 px at 246 wide, and 43 px at 360 wide.
- Sources for 12 px: Ohnishi & Oda 2020 (legibility plateaus at about 12 pixels per letter height) [A], ISO 9241-303 (16 arc-min minimum, 20–22 preferred) [B], and Bababekova 2011 (phone viewing distance 36.2 cm for texting, 32.2 cm for web) [A].
- My OCR proxy [C]: the floor is about 5–7 px displayed, or 40–50 px on the master at 168 wide. Fredoka, Baloo 2 and Rubik read at 40 px. Lilita One, Titan One, Paytone One and Luckiest Guy need 50 px. Anton needs 70 px and Passion One Black never stabilised.

Recommendation:
- **Main word.** Cap height 100–140 px, minimum 90 px. Secondary text at least 60 px.
- **Outline.** Ink #1a1a1a, drawn outside the letters with round joins, at 12% of cap height (12–16 px). Use about 8% for condensed fonts, or their counters fill in. Optional hard 6–8 px offset shadow. No blurred shadows, which vanish at small sizes.
- **Words.** 1–3 words (the brief allows 4), caps, no more than about 16 characters per line, at most 2 lines.
- **Font.** Lilita One is the primary: font size about 143 px for a cap height of 100 px, and it fits about 16 characters across 1152 px. Titan One (wide), Paytone One and Fredoka 700 or Baloo 2 800 are alternates.
  - Luckiest Guy and Bangers are comic alternatives, but Bangers is thin at 168 px.
  - Anton or League Gothic suit numbers only.
  - Handwriting faces (Patrick Hand, Kalam, Comic Neue) are too thin.
  - All are free, under OFL or Apache-2.0.
- **Placement.** Margins of 64 px left and right and 36 px top and bottom, because the corner radius is about 43–61 px on the master. Keep 230x90 px free at bottom-right (badge and watch bar). Keep roughly 110x110 px free at top-right (desktop hover icons, size UNVERIFIED). Put the text block top-left or in the left third.
- **Text on mid-tone colours.** Ink text fails on red, brown and dark green (Lc 29–34). Use white fill with a thick outline, or a paper caption box with an ink outline.

#### 4. Series consistency
- **Recognition.** Distinctive-brand-asset research (Romaniuk 2018, Ehrenberg-Bass) says recognisable, unique assets (characters, colours, shapes) need consistent repetition [B, via summaries]. A 2026 International Journal of Advertising paper reportedly finds shape assets strongest, but I saw only the snippet, so UNVERIFIED. If true, the stick-figure silhouette is the best anchor.
- **Banner blindness.** NN/g [A] shows people ignore things that look like ads (position, animation, fancy formatting). It is not evidence against consistent templates. The real risks are an ad-like banner or ribbon look and habituation.
- **Pop-out.** Pop-out needs feature contrast against a calmer surround (Nothdurft 1993, Wolfe & Horowitz 2017) [A]. Use one accent per image.

**Fixed anchors**
1. The 10-colour palette only.
2. An ink outline of 12–16 px on every shape.
3. The stick figure exactly as on the character sheet, with a head of at least 150 px if the face carries the emotion.
4. One accent object of 3–8% of frame area, red (amber only on ink scenes), never both.
5. One typeface (Lilita One), white or paper fill, ink outside stroke, 1–3 caps words.
6. Flat colour with gentle cel shading and no gradients.
7. The safe zones above.

**Variables:** composition, hero object, dominant background family (light, mid or dark tier), emotion, text position within the safe zone, word count, camera distance, cutaway or not.

Make consecutive thumbnails differ in background tier so the feed alternates. Keep about 5 anchors fixed and vary about 4 axes per video.

#### 5. Production workflow
Documentation [A]:
- **OpenAI.** Prompt order is scene, subject, details, constraints. The edit endpoint takes multiple references and an alpha mask. Text placement, recurring-character consistency and precise placement are documented weak points.
- **Google.** Use the formula Subject + Action + Location + Composition + Style. It accepts up to 14 reference images and does text-based mask edits. It also says "use positive framing" (describe what you want).
- **Midjourney.** V7 uses `--oref`, with `--ow` from 1 to 1000 and a default of 100 (docs page blocked, so secondary sources only).
- **FLUX Kontext.** Iterative edits that preserve the character.

A research finding matters here: image models often ignore negation (arXiv FineGRAIN and NeIn). So back the "no text" rule with positive wording ("blank plain board", "gauge with a needle and no marks"), and inspect or inpaint afterwards.

Workflow:
1. Make one character sheet (front, side, three expressions, prop) on flat paper and attach it to every generation.
2. Generate at 16:9 with one big hero shape, the figure large in the lower third, and a calm empty third for the text.
3. Fix stray glyphs with a masked edit ("change only X, keep everything else identical"), or paint flat colour over them.
4. Add the text as a live-text layer in Figma, Canva, Photopea, GIMP or Affinity (free since Oct 2025 with a Canva account).

Export, measured on a flat cartoon at 1280x720: PNG-24 was 33 KB, PNG-8 14.5 KB, JPEG q90 4:2:0 63 KB, and q95 4:4:4 94 KB. So use sRGB PNG-24 without alpha, under 2 MB. Use JPEG q92 4:4:4 only if a grainy image pushes it over. A master of 1920x1080 or 3840x2160 is fine if it stays under 2 MB, but YouTube delivers 1280x720 anyway. 4:2:0 chroma subsampling softens edges by 2 px (mean dE76 1.4–3.1 at a hard edge), which matters only where there is no ink outline.

**QA checklist** (run the rig on every thumbnail):
1. Squint (blur column): accent, main word and figure silhouette all survive.
2. Phone size: read the 360 and 168 rows at 100% zoom with the main cap at least 90 px.
3. Grayscale: word/background dL* at least 50, figure/background at least 25.
4. Light and dark rows: image edges must not dissolve on white.
5. Colour-blind: accent never red-on-green/brown, amber never on tan or light green.
6. Badge zone empty.
7. AI-glyph check at 100% (letters or numbers on signs, gauges, clocks; fingers, shoes, thick limbs).
8. Three words or fewer.
9. Export: 16:9, sRGB, under 2 MB.
10. After publishing, run Test & Compare with up to 3 variants.

#### Sources
- support.google.com/youtube/answer/72431
- support.google.com/youtube/answer/16391400
- gs.statcounter.com/screen-resolution-stats/mobile/{united-states-of-america, united-kingdom, canada, australia, worldwide}
- YouTube web/API responses, YouTube CSS (saved in raw/)
- github.com/material-foundation/material-color-utilities (hct.ts)
- github.com/Myndex/SAPC-APCA (minimum_compliance.md)
- w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- doi.org/10.1109/tvcg.2009.113 (Machado 2009)
- pmc.ncbi.nlm.nih.gov/articles/PMC7768324 (Ohnishi & Oda 2020)
- Bababekova 2011, Optom Vis Sci 88:795 (journals.lww.com)
- ISO 9241-303 / HFES 100 (via search summaries)
- nngroup.com/articles/banner-blindness-old-and-new-findings
- nature.com/articles/s41562-017-0058
- tvtechnology.com (Mohan letter, Feb 2025)
- advanced-television.com (Chartbeat, Jun 2025)
- developers.openai.com/api/docs/guides/image-generation
- developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- docs.bfl.ml/kontext
- arxiv.org/abs/2512.02161 and 2409.06481
- github.com/google/fonts (font licences)
- cgchannel.com and macrumors.com (Affinity free, Oct 2025)
- National Eye Institute colour-blindness figures (via secondary pages)

#### Caveats
- I could not read the duration-badge CSS or the native app card sizes. The 230x90 keep-out box is derived from a [C] source.
- The OCR and saliency results are proxies, not human studies.
- The Ohnishi & Oda figures and the Midjourney docs came through summaries, because the raw pages were blocked.
- I could not open the 2026 shape-asset paper.
- Dark-mode share is UNVERIFIED, and so is whether YouTube honours an embedded ICC profile.
- The phone pixel-size figure (about 0.166 mm per CSS px) is derived from a device spec I did not fetch.
- The rig is a 1:1 CSS-pixel simulation, so real phones look sharper than it does.

### D7. From story to thumbnail moment (fact-checked)

STORY-TO-THUMBNAIL-MOMENT REPORT (fact-checked 2026-09-30)
Full notes with every URL and quote: research/story-visuals.md (raw pages and PDFs are in ./raw/).
Grades: [A] official or peer-reviewed, [B] company or professional-body first-hand, [C] secondary or Wikipedia.
Primary texts actually read: NBS Hyatt report, Rogers Commission (Vol. 1), NTSB Big Dig report, Blackout Task Force report, HSE Flixborough page, WSDOT Tacoma history, Withey's Comet paper. All other facts are secondary and flagged.

THE 12 STORIES
(Format: facts | filter | thumbnail moment | title and honest promise | planted object)

1. VAJONT DAM, Italy, 9 Oct 1963 (dam/flood)
    - Facts: 1,917 dead [A, Italian Civil Protection]. Other counts run 1,919 to 2,056, so say "about 1,900". The slide was about 260 million m3 (sources say 200-300 million; the Civil Protection page prints "270 m3", a typo). The wave went about 250 m over the crest. The 262 m dam stayed standing, minus about 1 m of crest [B, ASDSO, Fondazione Vajont].
    - Filter: PASS. Criminal case closed at Cassation in 1971. Final Montedison-Longarone civil settlement signed 23 June 1999.
    - Moment: the dam intact with a wave pouring over it and a tiny village below. Documented, from trial records: at noon on 9 Oct workers on the crest saw the mountain moving by eye, and at 13:00 a crack 50 cm wide opened. Draw no people.
    - Title: the brief's own "Why did 1,900 people die under a dam that never broke?" Promise: the slope failed, not the dam. Deliver the 1960 slide, the gravel-and-plank model tests, and the lake-level rule.
    - Object: the gravel-on-a-plank model (documented).

2. TACOMA NARROWS, USA, 7 Nov 1940 (suspension bridge) [A, WSDOT]
    - Facts: opened 1 July, so it lasted 4 months. Wind was 42 mph. From 10:07 the roadway tilted up to 28 ft each side (45 degrees). A 600-ft section fell at 11:02. The only casualty was a dog. The deck was an 8-ft solid girder. Eldridge's 25-ft truss was estimated at $11M and the approved cap was $7M (Eldridge's own account [B]). The government's on-site engineer refused to recommend acceptance. The bridge bounced from May 1940, and the engineers said it was not dangerous.
    - MYTH: "resonance" is the textbook explanation. WSDOT says torsional flutter, with the exact cause still argued.
    - Filter: PASS (insurance settled 1941).
    - Moment: a tilted roadway between solid green walls. Workers chewed lemons against the nausea (documented). Do not show the dog.
    - Title: "Why did a four-month-old bridge twist itself apart in a 42 mph wind?" Do NOT say "light wind": 42 mph is a gale on the Beaufort scale.
    - Object: a lemon.

3. HYATT REGENCY WALKWAYS, Kansas City, 17 July 1981 (building)
    - Facts [A, NBS 1982]: about 7:05 pm, 113 dead and 186 injured (other sources say 114 and 216). Two sets of rods replaced one continuous rod, which "essentially doubled" the load on the 4th-floor connection. At collapse the load was 31% of code capacity, and even the original design gave only about 60%. The shop drawings carried stamps from the contractor, engineer and architect.
    - Filter: PASS. Missouri board ruling in 1985, upheld on appeal in 1988. The ">$140M settlements" figure is secondary and UNVERIFIED.
    - Moment: one long rod versus two short rods through a box beam, with a nut and washer under it. No crowd.
    - Title: "Why did a small change to one steel rod bring down two hotel walkways?" Do not claim "built for 100 people" (UNVERIFIED).
    - Object: the nut and washer.

4. DE HAVILLAND COMET, 1954 (aircraft)
    - Facts: 35 died on 10 Jan (Elba) and 21 on 8 Apr (Naples) [B/C]. The Cohen inquiry report came out 1 Feb 1955 as CAP 127. I could not open the official PDF (TLS error), so I used Withey 1997 and Aerossurance. In the Farnborough tank test the fuselage failed after 3,057 cycles (1,221 real plus 1,836 simulated; another source says 3,060). The Royal Navy recovered about 70% of the Elba wreck.
    - MYTH: "square windows". The failure began at a bolt hole by a roof radio-antenna cut-out, and the passenger windows were rounded rectangles.
    - Filter: PASS.
    - Moment: a whole airliner submerged in a purpose-built tank, "flown" in 5 minutes per flight. The test crack was under 2 mm.
    - Title: "Why did engineers put an entire jet airliner in a tank of water?" Promise: fatigue, the tank test, the wreck rebuilt from the sea, the myth busted.
    - Object: one rivet.

5. CHALLENGER, 28 Jan 1986 (rocket)
    - Facts [A, Rogers Commission]: liftoff 11:38 am, breakup at 73 seconds, 7 crew lost. Air temperature 36 F, 15 F colder than any earlier launch. The coldest joint spot was 28 F plus or minus 5. Thiokol's engineers advised against launching below 53 F. The pad had foot-long icicles. First smoke was at 0.678 s. Feynman's ice-water demonstration was on 11 Feb 1986 (Rogers Vol. 4 transcript).
    - Filter: PASS (litigation status UNVERIFIED, but 40 years old).
    - Moment: a glass of ice water and a clamped rubber ring that stays squashed. Show no crew or fireball.
    - Title: "Why did a piece of rubber that stopped working in the cold destroy a space shuttle?"
    - Object: the O-ring.

6. FLIXBOROUGH, UK, 1 June 1974 (chemical plant) [A, HSE]
    - Facts: 16:53, 28 killed, 36 injured on site, 53 injured off site. Reactor 5 cracked on 27 March, and a bypass was fitted between reactors 4 and 6. HSE says "no drawing", no calculations for the dog-leg or the bellows, and no pressure test.
    - CONTRADICTION: HSE itself says the 20-inch bypass failed "which may have been caused by" an 8-inch pipe fire. The cause is contested.
    - UNVERIFIED: "designed in chalk on the floor". Do not use.
    - Filter: PASS.
    - Moment: a dog-legged temporary pipe with accordion joints, and a gap where reactor 5 had been.
    - Title: "Why did a temporary pipe with no drawing blow up a chemical plant?"
    - Object: the bellows.

7. PIPER ALPHA, North Sea, 6 July 1988 (offshore platform)
    - Facts [C, summarizing the Cullen Report, which I did not fetch]: 226 aboard, 167 dead including 2 rescuers, 61 survived. The pump's safety valve had been removed and a blind flange fitted, "hand-tightened only". Permits were filed in different boxes. The fire pumps had been on manual since 19:00. The firewalls were not blast-rated.
    - Filter: PASS (civil trial 1997; criminal status UNVERIFIED). Do not blame the two workers the civil court named.
    - Moment: a steel disc hand-fitted out of sight, and two paper permits.
    - Title: "Why did an oil platform burn because the night shift never learned a safety valve was missing?"
    - Object: the blind flange.

8. BIG DIG CEILING, Boston, 10 July 2006 (tunnel) [A, NTSB HAR-07/02]
    - Facts: 11:01 pm, about 26 tons fell, 1 death. Cause: epoxy with poor creep resistance, meaning the bolts glued into the roof slowly let go. Anchor movement seen in 1999 was not traced to creep. No timely inspection program was in place.
    - Filter: PASS on age. The 2008 settlements are UNVERIFIED here.
    - Moment: a bolt sliding out of a glued hole over years. Draw no vehicle.
    - Title: "Why did the ceiling of a Boston tunnel fall after glue slowly let go of its bolts?"
    - Object: an epoxy anchor bolt.

9. NORTHEAST BLACKOUT, 14 Aug 2003 (software/control system) [A, Task Force final report, April 2004]
    - Facts: about 50 million people and 61,800 MW. After 14:14 the utility's alarm system failed and stayed dead. From 15:05 lines tripped on overgrown trees. The operators "remained unaware".
    - UNVERIFIED: the "race condition" software bug. It is not in the report text and comes only from secondary reporting.
    - Filter: PASS.
    - Moment: a frozen screen, a ringing phone, a hot sagging line touching a tree.
    - Title: "Why did a few overgrown trees and a silent alarm black out 50 million people?" (not "one tree").
    - Object: the frozen screen.

10. SAMSUNG GALAXY NOTE 7, 2016 (failed product) [C; Samsung's 23 Jan 2017 findings were not fetched]
    - Facts: discontinued 10 Oct 2016. The US FAA and PHMSA banned it from flights on 14 Oct. Two different defects: electrodes touching at a fold in the original batteries, and welding defects in the replacements. A Credit Suisse estimate put lost revenue at $17bn or more [C]. Injury counts and Samsung's own cost figure are UNVERIFIED (the CPSC page failed to load).
    - Filter: PASS (class-action status UNVERIFIED). Give no battery advice.
    - Moment: the replacement phone failing again.
    - Title: "Why did the phone that was recalled and replaced keep catching fire?"
    - Object: the phone.

11. QUEBEC BRIDGE, 29 Aug 1907 (collapse during construction) [C; the Royal Commission report on the Internet Archive was not read]
    - Facts: 75 of 86 workers died, 33 of them Mohawk ironworkers. The collapse took about 15 seconds. The span was 549 m. Bent lower chords were noticed for weeks. The stop-work telegram did not arrive in time. The dead-load estimate was never rechecked. A second collapse in 1916 killed 13.
    - MYTH: "Iron Rings are made from the wreckage". I found no support for it, so do not use it.
    - Filter: PASS.
    - Moment: a visibly bowed chord while work continued. Show no falling workers.
    - Title: "Why did engineers keep building a bridge that was already bending?"
    - Object: the bowed chord.

12. VASA, Stockholm, 10 Aug 1628 ("nothing broke") [C; the museum page returned 404]
    - Facts: sank after about 1,300 m. About 30 died. In a stability test 30 men ran across the deck and the admiral stopped it after 3 trips. The lower gunports went under water. Nobody was found guilty. Four rulers were found: 2 in Swedish feet, 2 in Amsterdam feet. Raised in 1961.
    - MYTH: the king added a deck late. The source says there is no evidence of that.
    - INFERRED only: that the two units made the ship heavier on one side.
    - Filter: PASS.
    - Moment: a huge ship heeling in a light breeze with its ports open, and a crowd on the shore.
    - Title: "Why did the most powerful warship in the Baltic sink in front of the crowd that came to watch it sail?"
    - Object: a wooden ruler.

CANDIDATES DROPPED BY THE LEGAL FILTER (searched today)
- Morandi bridge: verdict 16 July 2026, appeal announced. FAIL.
- Boeing 737 MAX: civil trials continue (jury verdict May 2026). FAIL.
- Grenfell: charging decisions still pending, trials 2029 or later. FAIL.
- Lac-Megantic: Supreme Court of Canada declined to hear the appeal. Sources conflict on 2025 versus 2026. Borderline, not used.
- Not verified this pass, so kept only as reserves: Chernobyl, Three Mile Island, Apollo 13, Columbia, Mars Climate Orbiter, Millennium Bridge, St. Francis Dam, Sleipner, Ronan Point, Kaprun, Sampoong, Therac-25. Titan and Baltimore Key Bridge were not checked.

RANKING (thumbnail strength)
| # | Story | Why |
|---|---|---|
| 1 | Comet | Unique "plane in a pool" image, zero graphic risk, curiosity gap, myth-busting |
| 2 | Tacoma | Instantly readable tilt; the famous film is differentiated by cartoon |
| 3 | Vajont | Size contrast, matches the channel's own title, safest to draw |
| 4 | Vasa | Big ship plus tiny crowd, bright colors, "nothing broke" hook |
| 5 | Challenger | One object (ice glass and ring), but very familiar |
| 6 | Blackout | Relatable, dark city and frozen screen |
| 7 | Note 7 | Phone-native for phone viewers, but weaker "disaster" and brand risk |
| 8 | Quebec | "Bending and ignored" works, though hard to show at phone size |
| 9 | Big Dig | The bolt-slipping cutaway fits the "what no camera saw" promise |
| 10 | Hyatt | Small object, needs text to hook |
| 11 | Piper Alpha | Complex scene, fire risk |
| 12 | Flixborough | Contested cause, less iconic |

WHAT THIS MEANS FOR THIS CHANNEL
- The rule "no text or numbers in images" favors stories with one drawable object: ice glass, lemon, ruler, rivet, bolt, nut, O-ring.
- Each story above lists a documented moment and an inferred part. Keep to the documented one.
- Use size contrast (dam versus village, ship versus crowd) because it reads on a phone.
- Avoid people at the moment of harm.
- Never draw claims marked UNVERIFIED.

CAVEATS
- Weakly sourced stories: Piper Alpha, Note 7, Quebec, Vasa. Their primary texts were not read.
- Legal follow-ups not verified: Big Dig, Blackout, Note 7 and Hyatt settlements.
- Not established: Tacoma's design wind speed, and the Vajont creep rates (Wikipedia and ASDSO disagree).
- Not read: the Comet CAP 127 PDF and the Cullen Report.

KEY SOURCES
- https://www.nasa.gov/history/rogersrep/genindex.htm
- https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir82-2465.pdf
- https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR0702.pdf
- https://www.energy.gov/sites/default/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
- https://wsdot.wa.gov/tnbhistory/
- https://www.hse.gov.uk/comah/sragtech/caseflixboroug74.htm
- https://damfailures.org/case-study/vajont-dam-italy-1963/
- https://fondazionevajont.org/wp-content/uploads/2024/09/TIMELINE_VAJONT_inglese.pdf
- https://servizio-nazionale.protezionecivile.gov.it/en/pagina-base/vajont-landslide/
- https://aerossurance.com/safety-management/comet-misconceptions/
- Withey, "Fatigue failure of the de Havilland Comet I", 1997: https://ae.iitm.ac.in/~nidish/courses/as3020/files/mod2/dehavcomet.pdf
- Wikipedia pages for Piper Alpha, Vasa, Quebec Bridge, Note 7 and Iron Ring
- Legal-status news: aljazeera.com/news/2026/7/16, aviationa2z.com 2026/05/14, itv.com 2026-05-19

### D8. Packaging, title-thumbnail pairing, testing and Shorts

Full notes with URLs, quotes and evidence grades: `research/packaging.md`. Thumbnails and contact sheets are in `.../packaging/thumbs/` and `.../packaging/lists/sheet_*.jpg`.

Grades: [A] official or large dataset. [B] first-hand creator or company statement. [C] opinion, vendor blog, or my own inference.

#### Key findings

**1. Title and thumbnail are one unit**
- [B] Paddy Galloway, 2024-07-10: "view the title and thumbnail as one, do they compliment each other or contradict/repeat?" He also says to pass the "glance test" (viewers get "milliseconds"). On 2024-05-10 he said to "always plan your title and thumbnail before recording". On 2022-08-29 he said the thumbnail concept (the psychology of the click) matters more than colors or polish.
- [B, leaked] The MrBeast memo (Sept 2024) says the title and thumbnail "set the expectations for the viewer". Every promised element must appear in the video (the "yellow vs red bouncy castle" example). Creative work starts from the title and thumbnail.
- [C] A vendor study (overseeros.com, 2026-08-12) looked at 217 classifiable thumbnails from videos with at least 1M views. 46.1% were completely complementary to the title, 28.6% mixed, 21.2% mostly repeated, and 4.1% were an exact match. This is survivorship data with no CTR, so it shows what winners look like, not that complementarity causes clicks.
- **Myth check:** "never repeat the title" is too strong. TED-Ed's "How do solar panels work?" (26M) and "Can you solve the prisoner hat riddle?" (37M) repeat the title fully, as search-intent evergreen videos. That reading is my inference [C]. On browse feeds, repetition wastes the thumbnail's one job.
- **Patterns that fit a question title** (my synthesis of the examples below [C]):
  - **A. Answer-tease.** The text or image is the answer's first word. Ink Explainer's "What Did Ancient Humans Actually Do All Day?" is paired with "NO JOBS".
  - **B. Evidence promise.** "We tested it" on Veritasium's "Is spider web really stronger than steel?"
  - **C. Outcome plus mystery.** The image shows what broke, and the title asks "what really happened". Practical Engineering does this with "ARECIBO TELESCOPE COLLAPSE" over the holed dish. The word "collapse" is never in the title.
  - **D. Zero-text anomaly.** A single image at human scale, as in Veritasium's black balls.
  - **E. Contrast triplet.** Veritasium's "EASY / EASY / ALMOST IMPOSSIBLE".
  - **Reverse pairing to avoid:** a statement title with a question in the image. Real Engineering does this ("DOOMED TO FAIL?"). Our title is already the question, so the thumbnail text should give the tease or answer word, not a second question.
- **Title length [C].** The 100-character limit is widely documented; I did not re-fetch the official page. Visible length on phones is unverified per device. SEO blogs claim about 40–55 characters in the mobile feed and 50–60 in search. Real top examples run 30–54 characters. The brief's example title is 54. Ink Explainer's 66-character title is the longest I found. Put the subject and tension in the first ~40 characters. Thumbnail text must not restate those characters or depend on the truncated tail.

**2. Curiosity versus clickbait**
- [A] The YouTube Help CTR FAQ says clickbait shows up as "high CTR but low average view duration and lower than expected impressions".
- [A] YouTube's Test & Compare picks winners by watch-time share, not CTR. The stated reason is that good packaging helps viewers not "waste their time clicking on the wrong videos".
- [B] Rene Ritchie (SEJ, 2023-08-14): "The thumbnail makes a promise, and the video has to deliver on it." Todd Beaupré (2026-09-01, via ppc.land): "No metric on its own is a good indicator of value."
- [C] Veritasium's "legitbait" versus "clicktrap" distinction comes from secondary summaries only. I could not get the transcript.
- **Working rule:** everything the thumbnail shows or says must be visible or explained by second 15. That matches the brief's outcome-first opening. Honest curiosity comes from showing the outcome (what broke) and withholding the cause chain.

**3. Testing**
- **Test & Compare mechanics [A]:**
  - Up to 3 variants of title only, thumbnail only, or both.
  - Desktop Studio only, and not available for Shorts.
  - Results are Winner, Performed Same or Inconclusive.
  - On "Inconclusive", the first uploaded variant stays live, so upload your best guess first.
  - Runs "a few days or up to 2 weeks".
  - Editing the title or thumbnail mid-test stops the test.
  - "Too similar" variants run longer. YouTube advises testing older videos first.
- **No official minimum impressions.** Vendor figures of "1,000–5,000 per variant" and "43% false positives under 1,000" are UNVERIFIED.
- **My arithmetic (standard two-proportion formula, 80% power, alpha 0.05, CTR only):**

| CTR change | Impressions needed per variant |
|---|---|
| 4% to 8% (+100%) | ~550 |
| 4% to 6% (+50%) | ~1,860 |
| 4% to 5% (+25%) | ~6,700 |
| 4% to 4.8% (+20%) | ~10,300 |

  Three variants triple the total. A small channel can therefore only detect radically different concepts, not font or color tweaks. The real tool uses watch-time share, so these figures are indicative only.
- [A] Do not manually swap thumbnails and compare. YouTube says early impressions skew to familiar viewers, and traffic-source mix distorts CTR. Third-party tools run sequentially and optimize CTR, so they can disagree with YouTube's tool.
- [B] Paddy (2023-07-13): a video ranked 8/10 in the first hour recovered to 1/10 with no change. Before changing packaging, weigh:
  - topic urgency
  - audience fit
  - metrics ("carefully")
  - the team's conviction in the packaging
- [B] Ritchie describes changing thumbnail and title to reach a broader audience.

**4. Cold start**
- [A] The YouTube Help CTR FAQ says half of channels have 2–10% impressions CTR. The range is wider for videos under one week old or under 100 views. Home-feed CTR is naturally lower, and channel-page CTR is higher.
- [B] Beaupré (2026-09-01, via ppc.land): early audiences are "diverse", and videos reach people "who've never watched the channel before" within the first hour. Subscribers' CTR is "10% or less", and "90% of the time, your subscribed audience isn't deciding to watch".
- [B] The growth team (SEJ, 2024-03-04) says discovery is "focused more on individual videos" than channel averages.
- **Implication:** strangers judge topic plus tension in one glance, and the brand is a secondary layer.
- The claim of "24–72 h small-cohort tests" is UNVERIFIED in its specifics.

**5. Identity versus variety**
- **Ink Explainer** (@Inkexplainer96, 106K subscribers, 16 videos, ~5 months old) is the brief's own model. All 16 thumbnails share one template: a stick figure in a rich scene with 1–3 outlined words. Views range from about 15K to 9.7M. The template does not decide the result; the idea and the tease do.
- **Practical Engineering** uses a real-place photo, a 2–3 word caps label, and a small logo, but drops the text when it isn't needed.
- **Kurzgesagt** uses a neon palette, a creature illustration, and 1–3 words.
- **Veritasium** varies widely (photo, typographic, illustrated).
- [C] Derek Muller (via The Ringer, 2026-03-09) says faces are "not that important" for Veritasium.
- **"Series blindness" has no rigorous YouTube evidence.** Only banner-blindness studies on ads exist, and vendor "70/30" rules are UNVERIFIED.
- **Recommendation:** fix the identity layer (character style, palette, text style and position) and vary the concept layer (scene, focal object, text word).

**6. Shorts**
- [A] Custom Shorts covers can only be set on a computer in Studio, and the account must be verified. Use 9:16 (recommended 2160×3840, minimum width 640). A/B testing does not exist for Shorts.
- [C] Many vendor blogs agree the cover never appears in the swipe feed, because the video autoplays. It shows on the channel Shorts tab, shelf, search and subscriptions. I could not confirm this in an official page.
- The "85% higher search CTR" claim is UNVERIFIED. The page I fetched does not contain it and says "YouTube has not published Shorts-specific thumbnail data".
- Observed covers (sheet_shorts.jpg):
  - Kurzgesagt uses title-card frames ("This Organ Regrows Every Month!", 1M views) as well as auto frames.
  - Veritasium uses a face or object plus 2–4 serif words ("Rome's Escalator Disaster", 5.5M views).
  - Practical Engineering runs a series card ("NAME THAT INFRASTRUCTURE / PAUSE HERE TO MAKE A GUESS", 3.2M views).
- **The Shorts "thumbnail" is frame 0 to 1 s:** the outcome image plus a 3–6 word on-screen line. The same frame can be the custom cover.

#### Real examples (views as fetched 2026-09-30, abbreviated by YouTube)

| Channel | Title | ID | Views, age | Thumbnail and pairing analysis |
|---|---|---|---|---|
| Veritasium | Why Are 96,000,000 Black Balls on This Reservoir? | uxPdPpi5W4o | 112M, 7y | Host on a boat with a sea of balls, no text. The image is the anomaly and the title adds the number and the question. |
| Veritasium | Why It Was Almost Impossible to Make the Blue LED | AF8d72mA41M | 55M, 2y | "EASY / EASY / ALMOST IMPOSSIBLE" over three LEDs. The image supplies the baseline contrast. |
| Veritasium | How A Student's Question Saved This NYC Skyscraper | Q56PMJbCFXQ | 26M, 1y | Illustrated engineer on a phone plus a highlighted structure, no text. A stylized (non-photo) engineering story. |
| Veritasium | Is spider web really stronger than steel? | wt4p2oalmRY | 9.3M, 1mo | "We tested it" over spider silk. A question title plus an evidence promise. |
| Practical Eng. | What Really Happened at the Arecibo Telescope? | 3oBCtTv6yOw | 9.4M, 5y | Holed dish plus "ARECIBO TELESCOPE COLLAPSE". Outcome image with a mystery title. |
| Practical Eng. | What Really Happened at the Oroville Dam Spillway? | jxNM4DGBRMU | 5.3M, 5y | Broken spillway plus "OROVILLE DAM". A label plus damage. |
| Practical Eng. | Why Are Beach Holes So Deadly? | 0kQXOTcEB_E | 7M, 1y | Tiny figure in a huge sand trench, no text. Scale conveys danger. |
| Real Eng. | The Questionable Engineering of Oceangate | 6LcGrLnzYuU | 4.9M, 3y | "DOOMED TO FAIL?" plus an arrow. A statement title with a question in the image (reverse pairing). |
| Kurzgesagt | How Are Memories Stored Inside Your Brain? | PqtggjVAi8M | 3.1M, 3mo | "THIS IS A MEMORY" plus an arrow. The image shows the answer object. |
| Kurzgesagt | Why Blue Whales Don't Get Cancer - Peto's Paradox | 1AElONvi9WQ | 27M, 6y | "CANCER PARADOX" plus a monster. The whale is in the title and the concept is in the image. |
| Mark Rober | World's Largest Jello Pool- Can you swim in Jello? | DPZzrlFCD_I | 223M, 7y | Man in a red jello pool, no text. The image is the answer. |
| Ink Explainer | What Did Ancient Humans Actually Do All Day? | 49_Ph2q6uIM | 9.7M, 1mo | Relaxed stick figure plus "NO JOBS". The answer-tease pattern, closest to our channel. |
| Ink Explainer | What Did Ancient Humans Do When It Rained All Week? | SD7XyG2wd1k | 1.5M, 2mo | "RAINED ALL WEEK" repeats the title words, a weaker complement. |
| TED-Ed | How do solar panels work? - Richard Komp | xKxrkht7CpY | 26M, 10y | Full title repeat. Search-intent counterexample. |

Views do not isolate the effect of packaging, so a "weaker complement" is a hypothesis, not a finding. Exact view counts were blocked by a YouTube bot-check after about 20 watch-page requests. Thumbnails shown are the current ones and may differ from the originals.

#### What this means for Stress Riser thumbnails
- **Aim for complement, not repeat.** The question title carries the who or what and the "why". The thumbnail shows the outcome scene (what broke, drawn with the brief's silhouette-and-cutaway style) plus 0–4 words that tease the answer or name the outcome ("NO JOBS" style), never a second question.
- **Text budget.** Two or three words in huge outlined type. The brief bans text inside generated images, so the words must be added in compositing.
- **Glance test at phone size.** One stick figure with one clear emotion, one focal object, and a high-contrast scene.
- **Honesty.** The thumbnail shows what the video shows by second 15. The brief's outcome-first opening already enforces this.
- **Variety.** Pick the concept type per video: answer-tease, outcome plus mystery, scale anomaly, or contrast.

#### Packaging workflow (one long video per week)
1. **Idea gate.** Write one line for the outcome plus the human stakes number. Draft 3 question titles of at most ~50 characters, with the hook in the first 40.
2. **Concepts.** Sketch 3 radically different thumbnail concepts before scripting. Each should be a different pattern from the list above. For each, write the tease word in 0–4 words.
3. **Pair check.** Ask: does the thumbnail say something the title does not? Does it repeat the first 40 characters? Does the video show it by second 15? Would a stranger get the topic in one glance on a phone? Drop any pair that fails.
4. **Script hook** is written to pay off the chosen pair.
5. **Publish** with Test & Compare on 3 variants. I recommend testing thumbnails only, so one variable class changes. Put your favorite first.
6. **Decision rules** (my heuristics [C], not from a source):
   - Do not touch anything before ~48 hours.
   - "Winner" means adopt it.
   - "Performed Same" means keep the one you prefer and log it.
   - "Inconclusive" means accept the default.
   - Only consider a manual swap if, after at least 5,000 impressions, CTR is under 70% of your own same-source baseline and average view duration is healthy. Change the whole concept, not a tweak.
7. **Weekly log.** Record concept type, tease word, CTR, average view duration and test result for each video. After 8–10 videos, look for patterns across videos. Single tests will rarely reach significance at small impression volumes.
8. **Shorts.** Frame 0 should be the outcome image plus a 3–6 word line, and it can double as the custom cover uploaded via desktop Studio.

#### Sources
- YouTube Help: https://support.google.com/youtube/answer/13861714 (A/B test), https://support.google.com/youtube/answer/7628154 (CTR FAQ), https://support.google.com/youtube/answer/72431 (custom thumbnails)
- Paddy Galloway posts: https://x.com/PaddyG96/status/1811083499044044951, https://x.com/PaddyG96/status/1788967959882346991, https://x.com/PaddyG96/status/1564326373170319360, https://x.com/PaddyG96/status/1679470163308019717
- MrBeast memo copy: https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/
- Vendor study: https://www.overseeros.com/blog/youtube-thumbnail-text-vs-title-study
- Veritasium: https://www.youtube.com/watch?v=S2xHZPH5Sng (8,297,543 views, Aug 17, 2021), https://www.veritasium.com/videos/2021/8/17/we-need-to-talk-about-clickbait, https://gigazine.net/gsc_news/en/20210830-clickbait-effective/
- The Ringer: https://www.theringer.com/2026/03/09/pop-culture/youtube-face-thumbnails-history-explained
- SEJ: https://www.searchenginejournal.com/youtube-algorithm-insights-from-creator-liaison-renee-ritchie/493901/ and https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/
- ppc.land: https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/
- thumbnailcreator.com (vendor, UNVERIFIED figures): https://www.thumbnailcreator.com/blog/thumbnail-a-b-testing-why-results-mislead
- Springer (banner blindness): https://link.springer.com/article/10.1007/s10339-023-01131-7
- YouTube channel pages (Popular tabs, Shorts tabs) for Veritasium, Kurzgesagt, Practical Engineering, Real Engineering, Wendover, Mark Rober, TED-Ed, Ink Explainer, fetched 2026-09-30.

#### Caveats and unverified items
- YouTube transcripts were blocked, so Veritasium's, Kurzgesagt's, Colin and Samir's and Jon Youshaei's own talks were not read. Their points here are secondary or not covered. I found no Kurzgesagt thumbnail video (only an announcement post), no Mark Rober or Wendover primary statements on packaging, and no Think Media or Nathan Graham material.
- Title truncation limits and the Shorts feed-versus-channel behavior are not from official documentation.
- UNVERIFIED: vendor impression thresholds, the false-positive rates, the Shorts "85% CTR", "Veritasium gets 50% more views from testing", and the "70/30" consistency rule.
- The Beaupré quotes come from ppc.land's reporting, not the video itself.
- I fetched 16 of the 17 example thumbnails at full size; view counts are abbreviated.

## F. Data tables: palette math, fonts, legibility experiments (F1 to F3)

F4 and F5 (the two video indexes) and F6 (phone-size QA sheet) are not in this edition (see 0.4).

### F1. Palette pairs and single-color values

Color names: grn_l = light green #8fbf5a, grn_d = dark green #4f7d3a. WCAG = contrast ratio; dL* = lightness difference (CIELAB); dE2000 = color difference; Lc = APCA contrast (a/b: a is the text, b the background; negative = light on dark); protan, deutan, tritan = dE2000 as seen with that color-vision deficiency. The 'use' column applies the rule of B4.3: a lightness gap of 50 or more is text-safe, 40 to 50 suits big bold text, 25 to 40 big flat shapes with an outline, under 25 is invisible by lightness.

#### Single colours (CIELAB D65)

| name | hex | L* | a* | b* | chroma | rel.lum | WCAG vs ink | vs white | vs paper |
|---|---|---|---|---|---|---|---|---|---|
| ink | #1a1a1a | 9.3 | -0.0 | 0.0 | 0.0 | 0.0103 | 1.0 | 17.4 | 14.56 |
| white | #ffffff | 100.0 | -0.0 | 0.0 | 0.0 | 1.0 | 17.4 | 1.0 | 1.2 |
| paper | #f3ead8 | 93.0 | 0.0 | 9.8 | 9.8 | 0.8286 | 14.56 | 1.2 | 1.0 |
| sky | #bfe2ea | 87.7 | -9.7 | -7.7 | 12.4 | 0.7141 | 12.67 | 1.37 | 1.15 |
| grn_l | #8fbf5a | 72.1 | -32.7 | 45.4 | 56.0 | 0.4384 | 8.1 | 2.15 | 1.8 |
| grn_d | #4f7d3a | 47.8 | -29.0 | 31.4 | 42.7 | 0.1663 | 3.59 | 4.85 | 4.06 |
| brown | #9a6b43 | 49.2 | 14.2 | 29.7 | 32.9 | 0.1779 | 3.78 | 4.61 | 3.86 |
| tan | #d2b48c | 75.0 | 5.0 | 24.4 | 24.9 | 0.4824 | 8.82 | 1.97 | 1.65 |
| amber | #e6b23a | 75.4 | 7.7 | 64.9 | 65.4 | 0.4897 | 8.95 | 1.95 | 1.63 |
| red | #d94a38 | 51.8 | 54.9 | 41.1 | 68.6 | 0.1993 | 4.13 | 4.21 | 3.52 |

#### All 45 pairs sorted by WCAG (APCA Lc: 'a on b' = a is text, b is background; sign = polarity)

| pair | WCAG | dL* | dE2000 | dE76 | Lc a/b | Lc b/a | dE2000 protan | deutan | tritan | use |
|---|---|---|---|---|---|---|---|---|---|---|
| ink / white | 17.4 | 90.7 | 86.4 | 90.7 | 104.3 | -106.5 | 86.4 | 86.4 | 86.4 | text-safe |
| ink / paper | 14.56 | 83.7 | 83.7 | 84.3 | 92.3 | -93.3 | 83.3 | 84.0 | 83.6 | text-safe |
| ink / sky | 12.67 | 78.4 | 78.8 | 79.4 | 83.7 | -84.0 | 79.5 | 77.0 | 79.7 | text-safe |
| ink / amber | 8.95 | 66.2 | 65.8 | 93.0 | 65.0 | -63.9 | 62.3 | 67.8 | 63.7 | text-safe |
| ink / tan | 8.82 | 65.7 | 61.8 | 70.3 | 64.1 | -63.0 | 59.4 | 62.8 | 61.7 | text-safe |
| ink / grn_l | 8.1 | 62.9 | 61.2 | 84.2 | 60.1 | -58.8 | 61.6 | 59.4 | 57.5 | text-safe |
| white / grn_d | 4.85 | 52.2 | 45.0 | 67.4 | -78.9 | 73.5 | 42.7 | 43.1 | 42.3 | text-safe |
| white / brown | 4.61 | 50.8 | 42.2 | 60.5 | -77.3 | 71.9 | 43.2 | 40.3 | 43.2 | text-safe |
| white / red | 4.21 | 48.2 | 44.2 | 83.9 | -73.5 | 68.0 | 46.1 | 38.4 | 45.4 | big bold text |
| ink / red | 4.13 | 42.5 | 42.8 | 80.7 | 34.3 | -32.3 | 31.4 | 43.8 | 43.7 | big bold text |
| paper / grn_d | 4.06 | 45.2 | 40.0 | 57.8 | -65.7 | 61.5 | 36.1 | 37.0 | 44.0 | big bold text |
| paper / brown | 3.86 | 43.7 | 36.5 | 50.1 | -64.1 | 59.9 | 36.9 | 34.0 | 36.9 | big bold text |
| ink / brown | 3.78 | 40.0 | 36.5 | 51.8 | 30.4 | -28.5 | 33.1 | 36.9 | 37.3 | big bold text |
| ink / grn_d | 3.59 | 38.5 | 37.3 | 57.5 | 28.8 | -26.8 | 36.3 | 33.7 | 33.4 | big shapes + outline |
| sky / grn_d | 3.53 | 39.9 | 40.8 | 59.1 | -56.4 | 52.9 | 41.5 | 41.8 | 32.4 | big shapes + outline |
| paper / red | 3.52 | 41.2 | 41.4 | 75.4 | -60.3 | 56.0 | 39.9 | 31.4 | 40.2 | big bold text |
| sky / brown | 3.35 | 38.4 | 42.8 | 58.8 | -54.7 | 51.2 | 41.2 | 39.7 | 50.5 | big shapes + outline |
| sky / red | 3.06 | 35.9 | 51.6 | 88.6 | -50.9 | 47.4 | 44.1 | 39.7 | 56.9 | big shapes + outline |
| grn_d / amber | 2.49 | 27.6 | 36.0 | 56.8 | 34.2 | -36.3 | 22.6 | 28.0 | 47.7 | big shapes + outline |
| grn_d / tan | 2.46 | 27.2 | 32.7 | 44.1 | 33.4 | -35.4 | 22.0 | 24.9 | 44.8 | big shapes + outline |
| brown / amber | 2.37 | 26.2 | 26.7 | 44.3 | 32.6 | -34.7 | 26.1 | 24.4 | 22.4 | big shapes + outline |
| brown / tan | 2.34 | 25.7 | 23.0 | 27.8 | 31.7 | -33.8 | 23.5 | 21.3 | 22.7 | big shapes + outline |
| grn_l / grn_d | 2.26 | 24.3 | 22.0 | 28.3 | -31.2 | 29.3 | 21.6 | 22.4 | 21.6 | invisible (hue only) |
| amber / red | 2.16 | 23.7 | 38.2 | 58.0 | -30.9 | 28.7 | 28.4 | 17.7 | 23.3 | invisible (hue only) |
| white / grn_l | 2.15 | 27.9 | 31.0 | 62.5 | -46.8 | 42.1 | 29.7 | 28.7 | 24.2 | big shapes + outline |
| grn_l / brown | 2.14 | 22.9 | 37.2 | 54.5 | -29.6 | 27.7 | 24.7 | 18.7 | 45.1 | invisible (hue only) |
| tan / red | 2.14 | 23.2 | 31.6 | 57.5 | -30.0 | 27.8 | 26.6 | 17.9 | 27.1 | invisible (hue only) |
| white / tan | 1.97 | 25.0 | 22.8 | 35.3 | -42.4 | 38.0 | 23.2 | 22.3 | 23.6 | big shapes + outline |
| grn_l / red | 1.96 | 20.4 | 59.0 | 90.1 | -25.7 | 23.8 | 27.2 | 13.0 | 53.7 | invisible (hue only) |
| white / amber | 1.95 | 24.6 | 30.8 | 69.8 | -41.5 | 37.2 | 32.3 | 30.0 | 27.9 | invisible (hue only) |
| paper / grn_l | 1.8 | 20.8 | 25.7 | 52.7 | -33.6 | 30.1 | 22.1 | 20.8 | 29.1 | invisible (hue only) |
| paper / tan | 1.65 | 18.0 | 15.2 | 23.7 | -29.2 | 26.0 | 15.2 | 14.1 | 16.0 | invisible (hue only) |
| paper / amber | 1.63 | 17.5 | 23.8 | 58.3 | -28.3 | 25.2 | 25.2 | 22.7 | 20.7 | invisible (hue only) |
| sky / grn_l | 1.56 | 15.6 | 31.8 | 59.9 | -24.2 | 21.5 | 32.8 | 33.1 | 12.8 | invisible (hue only) |
| sky / tan | 1.44 | 12.7 | 27.5 | 37.6 | -19.8 | 17.4 | 24.6 | 26.3 | 38.1 | invisible (hue only) |
| sky / amber | 1.42 | 12.2 | 36.1 | 75.7 | -18.9 | 16.6 | 35.7 | 36.4 | 41.2 | invisible (hue only) |
| white / sky | 1.37 | 12.3 | 14.1 | 17.5 | -20.9 | 18.3 | 8.8 | 11.1 | 17.7 | invisible (hue only) |
| white / paper | 1.2 | 7.0 | 9.1 | 12.1 | -11.1 | 9.5 | 9.1 | 9.4 | 8.4 | invisible (hue only) |
| paper / sky | 1.15 | 5.3 | 17.9 | 20.8 | -7.7 | 0.0 | 14.2 | 17.5 | 26.0 | invisible (hue only) |
| grn_d / red | 1.15 | 4.0 | 54.5 | 84.6 | 0.0 | 0.0 | 5.5 | 10.9 | 52.1 | invisible (hue only) |
| grn_l / amber | 1.11 | 3.3 | 25.8 | 45.0 | 0.0 | 0.0 | 4.3 | 7.4 | 40.5 | invisible (hue only) |
| grn_l / tan | 1.09 | 2.9 | 23.6 | 43.3 | 0.0 | 0.0 | 10.4 | 7.8 | 37.1 | invisible (hue only) |
| brown / red | 1.09 | 2.5 | 18.9 | 42.4 | 0.0 | 0.0 | 2.9 | 7.6 | 14.5 | invisible (hue only) |
| grn_d / brown | 1.05 | 1.4 | 30.7 | 43.2 | 0.0 | 0.0 | 4.2 | 3.7 | 41.4 | invisible (hue only) |
| tan / amber | 1.01 | 0.5 | 13.6 | 40.6 | 0.0 | 0.0 | 14.4 | 13.0 | 7.7 | invisible (hue only) |

### F2. Font measurements

Metrics of 28 display fonts measured by the design agent (source: `data/font-metrics.csv`). 'max cap px' is the largest cap height at which the line WHY DID IT FAIL? fits on one line in 1152 px (the 1280 master minus the 64 px margins). Lilita One is the recommended font (B4.4).

| font | class | cap/em | x/cap | stem/cap | e-ink | width per cap-height 'WHY DID IT FAIL?' | max cap px (1 line, 1152 px wide) |
|---|---|---|---|---|---|---|---|
| Sigmar One | rounded slab heavy | 0.675 | 0.87 | 0.533 | 0.8 | 15.2 | 75 |
| Sniglet ExtraBold | rounded playful | 0.722 | 0.76 | 0.498 | 0.79 | 13.36 | 86 |
| Gluten 900 | wobbly hand-drawn | 0.652 | 0.86 | 0.464 | 0.76 | 15.19 | 75 |
| Passion One Black | heavy rounded condensed | 0.622 | 0.77 | 0.454 | 0.84 | 11.62 | 99 |
| Titan One | rounded heavy display | 0.71 | 0.82 | 0.394 | 0.77 | 12.3 | 93 |
| Bowlby One | heavy display | 0.755 | 0.77 | 0.391 | 0.71 | 12.8 | 89 |
| Rubik 900 | soft-cornered grotesque | 0.7 | 0.74 | 0.368 | 0.77 | 12.35 | 93 |
| Coiny | rounded cartoon heavy | 0.688 | 0.69 | 0.335 | 0.71 | 12.94 | 89 |
| Paytone One | rounded heavy sans | 0.688 | 0.73 | 0.327 | 0.7 | 11.89 | 96 |
| Luckiest Guy | comic heavy display | 0.715 | 0.97 | 0.325 | 0.71 | 10.19 | 113 |
| Archivo Black | wide grotesque | 0.688 | 0.77 | 0.32 | 0.71 | 14.01 | 82 |
| Rowdies Bold | rounded bold | 0.708 | 0.67 | 0.311 | 0.75 | 13.18 | 87 |
| Grandstander 900 | kid-comic | 0.655 | 0.92 | 0.309 | 0.73 | 11.13 | 103 |
| Londrina Solid Black | hand-drawn heavy caps | 0.718 | 0.72 | 0.286 | 0.74 | 8.18 | 140 |
| Lilita One | rounded heavy display | 0.7 | 0.72 | 0.282 | 0.74 | 11.15 | 103 |
| Baloo 2 800 | rounded friendly | 0.625 | 0.81 | 0.28 | 0.7 | 12.08 | 95 |
| Fredoka 700 | rounded geometric | 0.7 | 0.75 | 0.261 | 0.74 | 11.24 | 102 |
| Oswald 700 | condensed grotesque | 0.81 | 0.71 | 0.222 | 0.76 | 8.52 | 135 |
| Chewy | comic rounded | 0.76 | 0.73 | 0.214 | 0.68 | 8.83 | 130 |
| Permanent Marker | marker hand-lettering | 0.752 | 0.83 | 0.206 | 0.6 | 12.0 | 96 |
| Bangers | comic condensed caps | 0.742 | 0.99 | 0.199 | 0.49 | 7.21 | 159 |
| Anton | condensed grotesque | 0.86 | 0.85 | 0.195 | 0.77 | 7.16 | 160 |
| Kalam Bold | handwriting | 0.732 | 0.71 | 0.191 | 0.6 | 11.18 | 103 |
| Boogaloo | comic light | 0.742 | 0.71 | 0.182 | 0.67 | 8.46 | 136 |
| Bebas Neue | condensed caps | 0.7 | 1.0 | 0.157 | 0.62 | 7.06 | 163 |
| Comic Neue Bold | comic text face | 0.68 | 0.74 | 0.147 | 0.55 | 12.03 | 95 |
| League Gothic | condensed grotesque | 0.735 | 0.74 | 0.146 | 0.72 | 6.31 | 182 |
| Patrick Hand | handwriting (thin) | 0.668 | 0.7 | 0.116 | 0.53 | 8.84 | 130 |

### F3. Legibility, saliency and color-blindness experiments

#### A. Accent saliency proxy (Achanta frequency-tuned saliency on a 168x94 downscale; 40 random scenes per cell)
hit = share of scenes in which the most salient pixel lies on the accent disc; ratio = median(mean saliency on disc / mean saliency elsewhere)

| accent | background | hit rate | saliency ratio |
|---|---|---|---|
| red | paper | 100% | 3.3 |
| red | sky | 100% | 3.4 |
| red | grn_l | 100% | 2.9 |
| red | grn_d | 100% | 2.9 |
| red | brown | 85% | 2.0 |
| red | tan | 100% | 3.4 |
| red | white | 100% | 3.2 |
| red | ink | 78% | 1.8 |
| amber | paper | 98% | 2.5 |
| amber | sky | 100% | 2.8 |
| amber | grn_l | 2% | 1.6 |
| amber | grn_d | 48% | 1.9 |
| amber | brown | 8% | 1.6 |
| amber | tan | 98% | 2.3 |
| amber | white | 98% | 2.5 |
| amber | ink | 100% | 1.9 |
| **red mean over backgrounds** | | 95% | 2.9 |
| **amber mean over backgrounds** | | 69% | 2.1 |

#### B. JPEG q90 edge damage (mean dE76 in a 16 px band at a hard edge with NO outline; transition width in px)

| pair | dL* | 4:2:0 dE76 | 4:2:0 width px | 4:4:4 dE76 | 4:4:4 width px |
|---|---|---|---|---|---|
| red/grn_d | 4.0 | 3.1 | 2 | 0.61 | 0 |
| red/brown | 2.5 | 1.87 | 2 | 0.57 | 0 |
| amber/grn_l | 3.3 | 1.61 | 2 | 0.24 | 0 |
| tan/grn_l | 2.9 | 1.78 | 2 | 0.45 | 0 |
| tan/amber | 0.5 | 1.43 | 2 | 0.21 | 0 |
| red/paper | 41.2 | 2.01 | 2 | 0.6 | 0 |
| red/sky | 35.9 | 2.96 | 2 | 0.61 | 0 |
| amber/ink | 66.2 | 1.88 | 2 | 0.0 | 0 |
| ink/paper | 83.7 | 0.69 | 0 | 0.34 | 0 |
| grn_d/brown | 1.4 | 1.84 | 2 | 0.65 | 0 |
| red/ink | 42.5 | 2.59 | 2 | 0.27 | 0 |

#### C. File size of a flat-colour cartoon thumbnail (demo_1, 1280x720)

| encoding | bytes |
|---|---|
| PNG (RGB, optimized) | 33,005 |
| PNG-8 (64 colours, no dither) | 14,506 |
| JPEG q85 4:2:0 | 55,713 |
| JPEG q85 4:4:4 | 66,623 |
| JPEG q90 4:2:0 | 63,058 |
| JPEG q90 4:4:4 | 75,690 |
| JPEG q95 4:2:0 | 76,428 |
| JPEG q95 4:4:4 | 93,797 |

#### CVD-simulated hex values

| name | normal | protan | deutan | tritan |
|---|---|---|---|---|
| ink | #1a1a1a | #1a1a1a | #1a1a1a | #1a1a1a |
| white | #ffffff | #ffffff | #ffffff | #ffffff |
| paper | #f3ead8 | #efe9d7 | #f1ecd8 | #f8e7e5 |
| sky | #bfe2ea | #dbdfeb | #d4d9ea | #b3e6e4 |
| grn_l | #8fbf5a | #c7b351 | #c0b060 | #92b8a8 |
| grn_d | #4f7d3a | #817434 | #7a703e | #4d796e |
| brown | #9a6b43 | #796f40 | #847943 | #a76161 |
| tan | #d2b48c | #c0b489 | #c7bb8d | #deaca9 |
| amber | #e6b23a | #c8b227 | #d5bf40 | #faa19a |
| red | #d94a38 | #726835 | #968733 | #ee2147 |

#### D. OCR legibility proxy (data/ocr-legibility.csv)

A machine proxy, not a human study: RapidOCR was run on a thumbnail with white text and a 12% ink outline, downscaled to the target size (168x94, 246x138, 360x202). Six test words (WHY, FELL, BROKE, WHO?, CRACK, SNAP) were scored; 5 is the practical maximum because 'WHO?' is usually misread. Columns capNN are the cap height in px on the 1280 master.

```csv
font,target,cap30,cap40,cap50,cap60,cap70,cap80,cap90,cap100,cap120
Lilita One,168x94,1,3,6,6,5,5,5,5,5
Lilita One,246x138,4,5,5,5,5,5,5,5,5
Lilita One,360x202,5,5,5,5,5,5,5,5,5
Titan One,168x94,0,3,5,4,5,5,5,5,5
Titan One,246x138,5,4,4,5,5,5,5,5,5
Titan One,360x202,5,5,5,5,5,5,5,5,5
Luckiest Guy,168x94,0,1,4,4,4,5,5,4,4
Luckiest Guy,246x138,3,4,5,5,5,4,4,4,4
Luckiest Guy,360x202,5,4,4,4,4,4,4,5,4
Bangers,168x94,0,0,1,4,5,5,5,5,5
Bangers,246x138,0,4,5,5,5,5,5,5,5
Bangers,360x202,4,5,5,5,5,5,5,5,5
Paytone One,168x94,0,2,5,5,6,5,5,5,5
Paytone One,246x138,4,6,5,5,5,5,5,5,5
Paytone One,360x202,5,5,5,5,5,5,5,5,5
Bowlby One,168x94,1,1,5,4,4,5,4,5,5
Bowlby One,246x138,3,4,5,5,4,4,4,5,5
Bowlby One,360x202,3,4,5,5,5,4,5,4,4
Passion One Black,168x94,0,2,4,2,3,2,1,3,2
Passion One Black,246x138,2,2,1,3,4,3,4,3,4
Passion One Black,360x202,2,3,3,5,4,5,4,4,4
Londrina Solid Black,168x94,0,0,5,5,4,5,4,5,5
Londrina Solid Black,246x138,4,4,5,5,4,5,6,5,5
Londrina Solid Black,360x202,4,5,5,5,5,5,5,5,5
Fredoka 700,168x94,1,5,4,6,5,5,5,5,5
Fredoka 700,246x138,4,6,5,5,5,5,5,5,5
Fredoka 700,360x202,5,5,6,6,5,5,5,5,5
Baloo 2 800,168x94,1,4,6,6,5,5,5,5,5
Baloo 2 800,246x138,5,5,5,5,5,5,5,5,5
Baloo 2 800,360x202,5,5,5,5,5,5,5,5,5
Rubik 900,168x94,1,4,4,5,5,6,5,6,6
Rubik 900,246x138,4,5,5,6,6,6,6,5,6
Rubik 900,360x202,4,6,5,6,5,5,5,5,5
Comic Neue Bold,168x94,0,2,5,6,6,6,6,6,6
Comic Neue Bold,246x138,5,6,6,6,6,6,6,6,6
Comic Neue Bold,360x202,5,6,6,6,6,6,6,6,6
Anton,168x94,0,0,3,3,5,5,5,5,5
Anton,246x138,1,3,5,5,5,5,5,5,5
Anton,360x202,4,5,5,5,5,5,5,5,5
League Gothic,168x94,0,0,4,5,5,6,6,6,6
League Gothic,246x138,0,2,5,6,6,6,6,6,6
League Gothic,360x202,5,6,6,6,6,6,6,6,6
Permanent Marker,168x94,0,3,5,5,4,4,4,6,5
Permanent Marker,246x138,2,4,6,5,5,5,5,6,5
Permanent Marker,360x202,4,5,5,6,6,6,6,5,5
Patrick Hand,168x94,0,2,4,6,6,6,4,6,5
Patrick Hand,246x138,3,6,6,5,6,6,5,5,5
Patrick Hand,360x202,5,6,4,5,5,5,5,5,5
```

## Z. Final reminders

The rules that matter most, repeated on purpose:

1. The channel brief (H2) overrides everything. Nothing is invented: every number, date, name and quote must come from this file's sources or be verified; when unsure, round it, drop the number, or say "not verified".
2. The ten styles are hypotheses. Say so, and recommend testing concepts, never tweaks.
3. Words are never inside a generated image; add 1 to 3 caps words as a separate text layer (pending the owner's confirmation, A5 decision 1).
4. Ten palette colors only; ink outline; lit scenes; red marks the culprit; no arrows, dashed lines, motion lines or diagram symbols; no text, letters or numbers inside the image.
5. Stick figures only, as on the character sheet: single-line limbs, at most three people, standing on light surfaces.
6. No victims, injuries, gore, mockery or logos; never a death toll as a hook; failures belong to systems, incentives and assumptions, never to individuals.
7. Titles are questions (no colon). The thumbnail adds a fact the title lacks and is paid off by second 15 of the video.
8. For stories use only registry facts; re-check the two-year rule and the legal status on the publication date; mark contested causes as contested.
9. Reply to the owner in Slovenian; everything for the channel is English.
10. Where Part D disagrees with Parts A, B, C or F, the latter win. When this file is silent, say so instead of guessing.
