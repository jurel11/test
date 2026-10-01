# Stress Riser: title research

Research date: 2026-10-01. The companion to `thumbnail-styles.md`: what is known about video titles, what our own data says, what the brief fixes, eight title formulas that fit the brief, a bank of 36 draft titles for the twelve candidate stories, and a testing plan.

**Grades** (same as the thumbnail research): [A] official documentation, peer-reviewed study or large randomized dataset. [B] a measurement made by us on public data, or first-hand creator or company data. [C] vendor blog, opinion or inference. UNVERIFIED means it could not be confirmed. "Hypothesis" means untested.

**Language:** the owner reads Slovenian; everything that goes into the channel (titles, descriptions) is English. This file is English.

**Precedence:** the channel brief (`channel-brief.md`) wins over everything here. Where this research disagrees with an earlier file (`STRESS-RISER-AI.md` B4.7, D7), this file is newer for titles; the differences are listed in section 9.

## Contents

1. The short version
2. What the brief already fixes, and what is only a brand choice
3. Evidence
   - 3.1 What YouTube says about titles [A]
   - 3.2 Our own measurement: 854 titles, controlled by channel [B]
   - 3.3 Studies on YouTube titles [C]
   - 3.4 Studies on headlines in general [A, C]
   - 3.5 Contradictions and myths
4. Who already owns each story's search results [B]
5. How people phrase their searches [B]
6. Eight title formulas that fit the brief
7. The title bank: 36 titles and 12 Shorts titles
8. Testing titles
9. Corrections to the earlier drafts
10. Checklist and tool
11. Decisions I need from you
12. Caveats and what I could not do
13. Sources and files

## 1. The short version

1. **The brief's "every title is a question" is a brand choice, not a performance rule.** Questions are a minority in the niche (a question mark in 15% of the 392 niche titles we measured, and 25 of the 54 channels with five or more titles use none) and no study finds a reliable click advantage. The one large matched-pair test on YouTube (7,935 titles that passed 1M views) found question and statement titles winning equally often: 445 to 446 pairs, median view ratio 1.000 [C]. Keep the question format because it fits the voice and differentiates (only 20 of 182 existing videos on our twelve stories have a question mark in the title), but do not expect the question mark itself to lift clicks.
2. **What does separate stronger from weaker titles in our data is naming the outcome**: a word like collapse, disaster, explosion, sinking, meltdown, fire. In the niche, 35% of the titles in the channels' top groups name an outcome against 18% in their weak groups (+15 percentage points per channel, 95% interval +8 to +23). Across both datasets: +9 points (+5 to +14) [B, correlation]. A question can name the outcome: *Why did a rubber ring destroy a space shuttle?*
3. **Length does not matter in the data.** Median length is 46 characters in both top and weak groups; all three length bands (40 or fewer, 41 to 60, more than 60) show no difference within channels. A 2,622-title vendor study agrees (no best length). One vendor study of 61,838 videos finds shorter wins, but it compares across channels and is uncontrolled [C]. The brief's guidance (about 60 characters or fewer, hook in the first 40) stays, because YouTube itself says viewers "may only see part of your title" [A], not because length was shown to change clicks.
4. **Concrete beats vague, until the title is already crammed with detail.** In 8,977 randomized headline tests a more concrete headline raised clicks 5.5% when the test's headlines were vague and cut them 9.9% when they were already very concrete; 50.9% of headlines were too concrete and 8.7% too vague [A, news headlines]. One named object or one number, not four.
5. **Simple words win clicks.** In more than 30,000 field experiments, headlines with common words and an informal style were clicked more than complex ones; character count did not predict clicks [A, news headlines]. This matches the brief's "plain spoken English".
6. **Negative words lift clicks, but the topic already does the work.** Each negative word added about 2.3% to the click rate in 105,000 Upworthy headline variants [A, news headlines]. Our data finds no benefit from loud adjectives (insane, terrifying, deadly): 12% of top titles, 13% of weak ones. The brief bans them anyway.
7. **The search results for our stories are almost all statements and labels, and several angles are already taken.** Practical Engineering owns *What Really Happened During the 2003 Blackout?* (5.5M views); *167 Men Died From Reasonable Decisions: Piper Alpha* (3.7M) already uses the "chain of reasonable decisions" angle; *This Tiny Change KILLED 114 People* and *The Design Change That Took 114 Lives* cover the Hyatt "small change" angle. The bank in section 7 avoids copying them.
8. **Eight formulas** (section 6) cover the brief-compliant ways to write a question title: paradox, small cause, age contrast, odd true detail, mechanism, searchable, decision seat, evidence demo. Each bank entry says which one it uses, so a three-way Test & Compare compares patterns, not wording.
9. **The earlier draft titles need fixing.** Five of the twelve titles in `STRESS-RISER-AI.md` D7 are over 70 characters, and one of those (102) is over YouTube's hard limit of 100; six more are over the 60-character guide. Section 9 lists them; the bank replaces them.
10. **A checker now exists**: `tools/title_check.py` applies the brief's title rules mechanically (question, no colon, opener, length, loud words, blame words, gore words, spelling). All 36 bank titles pass it. It cannot check facts.

## 2. What the brief already fixes, and what is only a brand choice

The brief's title rules (`channel-brief.md`, "Never" list and speech patterns): every title is a question a curious stranger would ask; no colon; no case name first; no statement; no clickbait the video does not deliver; no blaming individuals; no graphic injury or death wording; American spelling; casualties stated factually. The brief's own example: *Why did 1,900 people die under a dam that never broke?* (54 characters).

| Rule | Basis | Notes |
|---|---|---|
| Question form | Brand choice [C] | Not supported or contradicted by evidence (section 3). Differentiates from the label-style titles that dominate disaster results. |
| No colon, no series tags | Brand choice; YouTube advises saving "episode numbers and branding for the end" [A] | Our data shows separators slightly more common in top groups (+5 points, interval -1 to +12, both sets). Most are series or channel tags ("OverSimplified (Part 1)" or a channel name after a vertical bar), not a title device. Keep the ban. |
| No case name first | Brand choice | The name may sit later in the question (slot C in the bank). |
| No clickbait | YouTube policy [A] and brief | The deceptive-metadata policy covers "maliciously misleading titles, thumbnails, descriptions, or imagery to trick users into clicking on a video that does not deliver what was promised"; YouTube's CTR FAQ says clickbait shows up as high CTR with low average view duration. |
| Blame systems, not people | Brief | "Who sank the Vasa?" (Atomic Frontier, 365K) and "Ego in Engineering" (Brick Immortar, 678K) are the framing to avoid. The checker fails "Who ..." openers and blame words. |
| About 60 characters, hook in the first 40 | Guidance in the earlier research [C] | YouTube: "Viewers may only see part of your title ... put the most important words near the beginning" [A]. Exact truncation not measured (section 12). |

## 3. Evidence

### 3.1 What YouTube says about titles [A]

Fetched 2026-10-01 from YouTube Help; quotations as returned by the fetch tool.

- **Thumbnail & title tips** (https://support.google.com/youtube/answer/12340300): "Be accurate. Make sure your title accurately represents the video." "Be succinct. Viewers may only see part of your title" and "aim to keep it short and put the most important words near the beginning." "Save episode numbers and branding for the end." "Limit ALL CAPS and emoji." YouTube names two kinds of title: **searchable titles** "that clearly outline what to expect so you can easily reach viewers searching for similar content" and **intriguing titles** "that spark curiosity and appeal to viewers who may not be looking for topic-specific content." The brief's question titles are the second kind; the bank's slot C is the first.
- **Deceptive metadata policy** (https://support.google.com/youtube/answer/2801973): "maliciously misleading titles, thumbnails, descriptions, or imagery to trick users into clicking on a video that does not deliver what was promised." Consequences: removal, warning or strike.
- **Title limit:** 100 characters (YouTube Help "Edit video settings", as quoted in search results; the earlier research also lists it as widely documented).
- **Test & Compare** (earlier research, `research/packaging.md`): up to three titles and/or thumbnails; winner is the highest watch-time share, not CTR; titles that are too similar make tests run longer; changing the title mid-test stops it; not available for Shorts.
- **CTR FAQ** (earlier research): half of channels have an impressions CTR between 2% and 10%; clickbait "tend[s] to have low average view duration".

### 3.2 Our own measurement: 854 titles, controlled by channel [B]

**Data:** `data/niche-video-index.csv` (disaster, engineering and documentary niche, 392 usable titles from 58 channels) and `data/cartoon-video-index.csv` (cartoon and stick-figure explainers, 462 titles from 52 channels), fetched 2026-09-30. Thirteen niche rows with empty titles were dropped. Fourteen channels and 44 videos appear in both sets, so the "both sets" rows count them twice. Script: `tools/title_analysis.py`; full tables in `data/title-analysis-report.md`; per-title features in `data/title-features.csv`.

**Method.** Each channel has a top group (its most-viewed videos) and a weak group (its weakest recent uploads). For each title feature we compute (1) the share of top-group titles with the feature minus the share of weak-group titles with it, per channel, averaged over channels that have both groups, and (2) the gap in within-channel z-score of log views between titles with and without the feature. Intervals are bootstrap 95% intervals over channels. This removes the biggest confounder (big channels have big views) but not all: view counts are the rounded figures YouTube lists (11M, 172K), age is uncontrolled, and the weak group is recent by construction.

| Feature | Niche: top minus weak (95% interval) | Both sets: top minus weak | Both sets: within-channel z gap | Reading |
|---|---|---|---|---|
| Names the outcome (collapse, disaster, explosion, sinking ...) | **+15 pp (+8 to +23)** | **+9 pp (+5 to +14)** | **+0.24 (+0.08 to +0.40)** | The only feature with an interval clear of zero in both views. Correlation: it may partly reflect which stories channels cover. |
| Contains a question mark | +6 pp (-3 to +14) | +3 pp (-2 to +8) | +0.14 (-0.06 to +0.33) | Leans positive, not distinguishable from zero. |
| Starts with What | +2 pp (-4 to +8) | +2 pp (-2 to +5) | +0.21 (-0.03 to +0.48) | Leans positive (n = 49). The "What" question shape has the highest median views of any shape (9.7M, n = 33). |
| Starts with Why | +2 pp (-4 to +9) | -2 pp (-7 to +3) | -0.11 (-0.40 to +0.14) | Nothing (n = 99). |
| Starts with How | -1 pp (-6 to +4) | +1 pp (-2 to +4) | +0.06 (-0.14 to +0.26) | Nothing (n = 70). |
| Yes/no question (Is, Can, Did, Would ...) | 0 pp (-5 to +4) | -1 pp (-3 to +2) | -0.26 (-1.05 to +0.52) | Inconclusive (n = 19), leans weak. Do not bet on it. |
| Contains a digit | -1 pp (-11 to +8) | -1 pp (-7 to +6) | -0.05 (-0.23 to +0.12) | Nothing (n = 212). |
| 40 characters or fewer / 41 to 60 / more than 60 | +4 / -4 / 0 pp | +3 / -1 / -1 pp | -0.05 / +0.08 / -0.06 | No length effect; every interval spans zero. Median 46 characters in both groups. |
| ALL-CAPS word | 0 pp (-7 to +8) | -1 pp (-6 to +5) | -0.11 (-0.40 to +0.14) | Cartoon set alone: -6 pp, z -0.29 (-0.70 to +0.01), leans weak. YouTube advises limiting caps. |
| Loud word (insane, terrifying, deadly, secret ...) | -2 pp (-8 to +5) | +1 pp (-3 to +5) | +0.07 (-0.18 to +0.32) | Nothing. |
| Exclamation mark | 0 pp | 0 pp | -0.11 (-0.58 to +0.31) | Nothing (n = 24). |
| Uses "you" | 0 pp | 0 pp | +0.11 (-0.14 to +0.36) | Nothing. |
| Colon | +5 pp (-2 to +12) | +3 pp (-2 to +7) | +0.08 (-0.14 to +0.28) | Nothing clear. |

**Other facts from the same data.**

- Questions are rare. A question mark appears in 15% of niche titles and 18% of cartoon titles. In the niche, 25 of the 54 channels with five or more titles used no question at all (among them Fascinating Horror, Mayday: Air Disaster, Oceanliner Designs, Real Engineering, Brick Immortar, Dark Docs, Storified, USCSB, Tom Scott, Wendover and LEMMiNO). The most question-heavy are explainers (Jared Owen 5 of 6, Ink Explainer 4 of 6, Two Bit da Vinci 4 of 7, Mentour Pilot 4 of 8, Mustard 3 of 6, Kurzgesagt 3 of 6). The brief's format places Stress Riser in the explainer tradition, not the disaster-documentary one.
- The most-viewed question titles are about the unknown or the odd, with an object or a number in them: *Why Are 96,000,000 Black Balls on This Reservoir?* (112M, Veritasium), *What's the Deepest Hole We Can Possibly Dig?* (48M), *What If We Detonated All Nuclear Bombs at Once?* (32M), *What Happened To The Nautilus?* (20M), *How Do Sinkholes Form?* (13M), *What Really Happened at the Arecibo Telescope?* (9.4M), *Why Are Beach Holes So Deadly?* (7M).
- Weak-group question titles are more often yes/no, opinion or vague (*Are America's Students Falling Behind?*, *Can Switzerland Stay Neutral?*, *Why Can't Every Country Do This?*).
- The most-viewed disaster titles name the thing and the outcome: *The Crash that KILLED Concorde* (16M), *Oceangate Submarine Disaster - What REALLY Happened* (15M), *The Wild Story of the Taum Sauk Dam Failure* (11M), *Why Shanghai Tower Failed* (7.8M).

**What this does not show.** It is correlation inside two non-random samples. It cannot separate the title from the thumbnail, the topic or the channel's audience, and it measures views, not CTR. The right use is as a prior: name the outcome, keep titles plain and concrete, do not rely on the question mark, and let tests decide.

### 3.3 Studies on YouTube titles [C]

All are vendor studies; none gives CTR; each has the survivorship or comparison problem noted.

- **OverseerOS, "Should YouTube titles be questions?"** (https://www.overseeros.com/blog/should-youtube-titles-be-questions): 7,935 titles from videos with at least 1M views, 196 English-language channels. 536 (6.8%) have a question mark; 1,051 (13.2%) use a broader question frame; 47.7% of established channels used no question mark. 891 matched pairs (same channel, same format, published within 30 days): questions won 445, statements 446; median view ratio 1.000. Long-form 0.945 (47.8% question win rate), Shorts 1.066 (52.9%). Question-mark share by niche: Education 20.3%, News 13.6%, AI and technology 10.3%, Entertainment 3.0%, Gaming 1.9%. First words of question titles: What 17.4%, How 9.7%, Why 8.8%, Can 4.7%, Is 4.1%. Their conclusion: "A question mark alone did not produce a measurable public-view advantage." Only videos that passed 1M views are included.
- **OverseerOS, title length** (https://www.overseeros.com/blog/best-youtube-title-length-study): 2,622 titles, 59 channels; "breakout" means initial view velocity above twice the channel's baseline. Breakout median 58 characters and normal median 58; correlation of length with breakout -0.0001; 76.1% of breakouts stayed within 25% of the channel's usual title length. "We found no evidence for one performance-optimal YouTube title length."
- **ViewsKit** (https://viewskit.com/blog/youtube-title-length-curve): 61,838 long-form videos pulled through the YouTube API "ordered by view count"; median views fall as titles lengthen (3.97M at 20 characters or fewer, 2.08M at 41 to 50, 1.20M at 81 to 100). The sample is chosen by views and is not controlled by channel, so a short-title format (music, clips) can drive it. It contradicts both our within-channel result and the OverseerOS length study, which control for the channel; I weight it least.
- **AIR Media-Tech** (https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches): 18,080 English-language channels, 11 niches, four size tiers. As summarized by search results, question marks "work when the viewer already has the question": strongly positive in Education, Business and Science and tech, weak or neutral in Gaming, Food and Kids. The page body was truncated for the fetch tool, so I could not read numbers.
- **Reading across the four:** a question helps, if at all, for explainer topics where the viewer arrives with the question, which is our niche. The effect, if any, is too small for a vendor sample to see.

### 3.4 Studies on headlines in general [A, C]

None is about YouTube. They are the best randomized evidence on how wording changes clicks.

- **Robertson et al. 2023, Nature Human Behaviour**, "Negativity drives online news consumption" (https://pmc.ncbi.nlm.nih.gov/articles/PMC10202797/) [A]: 22,743 randomized tests, about 105,000 headline variants, 5.7 million clicks, more than 370 million impressions (Upworthy). Each additional negative word raised the click rate by 2.3% for a headline of average length (about 15 words); each positive word lowered it by about 1.0%; sadness words raised clicks, joy and fear words lowered them by under one percent each; anger had no significant effect. For us: the topic is already negative; adding loud adjectives is not needed and the brief bans it.
- **Rogers, Shulman and Markowitz 2024, Science Advances**, "Reading dies in complexity" (read through Journalist's Resource, Phys.org and Harvard Magazine summaries; DOI 10.1126/sciadv.adn2555) [A]: more than 30,000 field experiments (about 20,000 Washington Post headlines, 2021 to 2022, and 105,000 or more Upworthy, 2013 to 2015). Headlines written with common words, an informal style and better readability were clicked more; **character count did not correlate with clicks**. The effect is modest. Professional journalists did not prefer the simple versions, which is a warning that our own taste is a poor guide.
- **Quere and colleagues, registered report "When curiosity gaps backfire: effects of headline concreteness on information selection decisions"** (https://pmc.ncbi.nlm.nih.gov/articles/PMC11704130/; the digest dates it 2024 to 2025) [A]: 17,867 Upworthy tests (85,830 headlines); confirmatory sample 8,977 tests. Concreteness has a curved effect: where the test's headlines were vague (mean concreteness 2.06 of 5), a more concrete headline raised the click rate by about 5.5%; where they were already very concrete (4.41), a more concrete one lowered it by about 9.9%. 50.9% of headlines were too concrete and 8.7% too vague. "There is such a thing as omitting too much information" and also too much detail. For us: a named object or a number is right; a title with four facts is not (the earlier D7 drafts).
- **Question headlines, mixed and secondhand** [C]: a literature digest (https://gist.github.com/NHagar/77c3f2e9df9c211d2abce7982f794135) reports Kuiken et al. 2017 ("questions may not lead to higher click-rate for all topics"), a Chartbeat analysis of 250,000 headlines (interrogative words such as what and why tend to raise engagement, a literal question mark can hurt) and Liu et al. 2022 (questions raised click ratios). A search summary mentions an analysis of 9,000 headline tests across 57 media titles in which a question did not necessarily win. The original Kuiken and Lai and Farbrot pages returned 403 errors, so these are secondhand.
- **Vendor claims I did not use:** "numbers raise CTR by 15%" and "odd numbers beat even by 20%" (digest of Optimizely and Outbrain; no method). Our own data and a YouTube-specific study (section 3.2) show no digit effect.

### 3.5 Contradictions and myths

| Claim | Verdict |
|---|---|
| "Question titles get more clicks." | Not supported. Matched-pair evidence on YouTube says equal; our data leans slightly positive without certainty; news studies are mixed. |
| "Shorter titles get more views." | Not supported within channels (our data; OverseerOS). One uncontrolled vendor study says yes. |
| "Put a number in the title." | No effect in our data (-1 pp, z -0.05). Use a number only when it is the hook (Vajont's 1,900), and only one. |
| "Use power words." | No effect in our data; the brief bans loud words; negativity is already in the topic. |
| "Title and thumbnail must not repeat each other." | See `STRESS-RISER-AI.md` B4.7: complement is better on browse feeds, repetition is harmless on search intent. The bank's titles carry the who, what and why; the thumbnail adds the outcome or the object. |
| "YouTube picks the title with the best CTR." | No. Test & Compare picks watch-time share. |
| "A good title has the event name first." | That is search-intent writing. It is also the label style that dominates our stories' results. The brief forbids it first; the name may come later. |

## 4. Who already owns each story's search results [B]

Collected 2026-10-01 with `tools/title_competition.py` (logged out, English, US): the top ten results for two phrases per story, exact view counts as listed. Full tables: `data/title-competition.md` and `.csv`.

| Story | Distinct videos | With a question mark | 1M views or more | Biggest on-topic video (views) |
|---|---|---|---|---|
| Comet airliner 1954 | 14 | 2 | 1 | Mustard: Why You Wouldn't Want to Fly The First Jet Airliner: De Havilland C... (6,474,949) |
| Tacoma Narrows 1940 | 16 | 1 | 5 | Tony C: Tacoma Narrows Bridge Collapse "Gallopin' Gertie" (15,416,901) |
| Vajont 1963 | 16 | 0 | 3 | Smithsonian Channel: One of the Worst Man-Made Disasters in History (11,576,098) |
| Vasa 1628 | 17 | 3 | 2 | IT'S HISTORY: This Warship Sank in Minutes—And Was Raised Centuries Later (2,609,806) |
| Challenger 1986 | 15 | 3 | 5 | WESH 2 News: Astronauts Likely Survived Challenger Explosion (8,797,428) |
| Northeast blackout 2003 | 20 | 4 | 4 | Practical Engineering: What Really Happened During the 2003 Blackout? (5,530,267) |
| Galaxy Note 7 2016 | 16 | 4 | 5 | JerryRigEverything: Note 7 Battery Explosion!! CAUGHT LIVE ON CAMERA!! (14,598,030) |
| Quebec Bridge 1907 | 13 | 1 | 0 | Brick Immortar: Ego in Engineering: The Quebec Bridge Collapse (678,400) |
| Big Dig ceiling 2006 | 13 | 0 | 0 | Industrial Empire and 3 more: Boston Suspended 26 Tons of Concrete With Glue—Then the Glue Began ... (800,846) |
| Hyatt Regency 1981 | 13 | 0 | 5 | Tom Scott: The Disaster That Changed Engineering: The Hyatt Regency Collapse (2,672,820) |
| Piper Alpha 1988 | 16 | 1 | 2 | Waterline Stories and 2 more: 167 Men Died From Reasonable Decisions: Piper Alpha (3,741,376) |
| Flixborough 1974 | 13 | 1 | 1 | Plainly Difficult: The Flixborough Disaster (1974) Where Did it go so Wrong? | Plainly... (1,013,459) |

Across all twelve stories, 20 of 182 distinct videos have a question mark (11%). Most results are labels or statements: *The Vajont Dam Disaster | A Short Documentary*, *The Tacoma Narrows Bridge Disaster*, *The Hyatt Regency Walkway Collapse*. So a question title stands out in the results. The least contested stories are Big Dig, Quebec and Flixborough, where no on-topic result passes about 1M views; Comet has one big video (Mustard, 6.5M) and nothing that uses the water-tank angle.

**Angles already taken, to avoid copying** (all from the same results):

- *Blackout:* Practical Engineering, "What Really Happened During the 2003 Blackout?" (5.5M). Do not reuse the title. Half as Interesting blames "The Software Bug", which the Task Force report does not say (see `STRESS-RISER-AI.md` D7).
- *Piper Alpha:* "167 Men Died From Reasonable Decisions: Piper Alpha" (3.7M) is exactly the channel's unique angle. It is a statement with a colon, so a question like *How can a safety valve go missing without anyone knowing?* is differentiated, but expect viewer comparison.
- *Hyatt:* "This Tiny Change KILLED 114 People" (410K), "The Design Change That Took 114 Lives" (1.1M). The "small change" angle is crowded; the bank leads with the mechanism instead (slot B).
- *Vasa:* "Who Sank the Vasa?" (365K) blames a person; "Destroyed by a Breeze" (880K) is the stock explanation.
- *Big Dig:* "Boston Suspended 26 Tons of Concrete With Glue—Then the Glue Began to Creep" (801K, three weeks old) already tells the glue story. A rival with the same angle is a month old, so check again before publishing.
- *Challenger:* "What really happened to the Challenger? Was it a preplanned disaster?" (684K) already holds the "what really happened" phrasing; the ice-water and rubber-ring angles are free.

## 5. How people phrase their searches [B]

Collected 2026-10-01 with `tools/title_autocomplete.py` from the public suggest endpoint behind YouTube's search box (English, US; 144 queries). Full lists: `data/title-autocomplete.md`. Suggestions show how people word a search, not how many search, and they vary by region and person.

- **Where people already ask a "why" or "what" question:** *why did the tacoma narrows bridge collapse*, *why did the vasa sink*, *why did challenger explode*, *what caused the challenger disaster*, *what really happened to the challenger shuttle*, *what caused the 2003 blackout*, *what really happened during the 2003 blackout*, *why did the galaxy note 7 explode*, *what caused the piper alpha disaster*. For these, a question title matches the search habit.
- **Where people search only the label:** Vajont ("vajont dam disaster", "vajont dam documentary"), Comet ("de havilland comet crashes", "... documentary"), Hyatt ("hyatt regency walkway collapse"), Quebec ("quebec bridge collapse"), Big Dig ("big dig ceiling collapse", with no question form at all) and Flixborough ("flixborough disaster 1974 documentary", "... animation"). A title without the event name will not match these searches, so the name should appear in the description and, for slot C titles, in the title.
- **Several stories show "documentary" and "animation" as suffixes** (Vajont, Piper Alpha, Flixborough: "flixborough disaster 1974 animation"). Demand for an animated explainer exists; the word belongs in the description, not the title.
- **Dropped suggestions are data too:** "galaxy note 7 explained" returned nothing, and "why did piper alpha" and "why did flixborough" returned none. Those stories have little question-shaped search demand; they will be found through browse and suggested video, where the title's job is curiosity.

## 6. Eight title formulas that fit the brief

Every formula produces one question, no colon, no case name first, 60 characters or fewer, hook in the first 40. "Pairs with" uses the thumbnail styles in `thumbnail-styles.md` (1 Tiny under the giant, 2 The moment before, 3 The impossible scene, 4 Exhibit A, 5 The cutaway, 6 The giant number, 7 The odd true detail, 8 The crowd on the shore, 9 Seat of the decider, 10 Close-up gaze) so title and thumbnail are planned together.

| # | Formula | Shape | Example | Why it should work | Risk | Pairs with |
|---|---|---|---|---|---|---|
| F1 | Paradox | Why did [number] [fate] [where it should have been safe]? | *Why did 1,900 people die under a dam that never broke?* | The brief's own title. Number plus an oddity, like Veritasium's 96,000,000 black balls (112M). | The number must be rounded exactly as the source allows; a death toll stays in the title, not the thumbnail. | 3 Impossible scene, 1 Tiny under the giant |
| F2 | Small cause | Why did [small named object] [big outcome]? | *Why did a rubber ring destroy a space shuttle?* | Names the outcome (the one feature our data supports) and one concrete object (the concreteness result). | Over-claiming a single cause: Flixborough and Tacoma are contested; use "help" or a mechanism question. | 4 Exhibit A, 5 The cutaway |
| F3 | Age contrast | Why did a [age]-old [thing] [fail]? | *Why did a four-month-old bridge twist itself apart?* | A number the viewer can feel, with a built-in surprise. | None beyond fact-checking the age. | 2 The moment before |
| F4 | Odd true detail | Why were [people] [doing a strange documented thing] [at the event]? | *Why were workers chewing lemons on a twisting bridge?* | An information gap anchored on a concrete object, the "moderate concreteness" case. | The video must show and explain it within 15 seconds; only for details with a documented source. | 7 The odd true detail |
| F5 | Mechanism | How can [ordinary thing] [do the impossible-seeming thing]? | *How can glue slowly lose its grip on a tunnel ceiling?* | Explainer idiom: *How Do Sinkholes Form?* (13M), *How does an Escalator work?* (19M). | "How" shows nothing special in our data (+1 pp); it is a content choice, not a hack. | 5 The cutaway |
| F6 | Searchable | What / Why [did the event] [year]? | *What went wrong with the Quebec Bridge in 1907?* | YouTube's "searchable title" type; matches how people search (section 5); "What" questions have the best median views in our data (9.7M, n = 33). | Name and year land late (keep them after the hook); collides with big existing titles; "really" is a stock word, use it rarely. | 6 The giant number, any |
| F7 | Decision seat | Why did [people] keep [doing the reasonable thing]? | *Why did engineers keep building a bending bridge?* | The brief's unique angle: the viewer stands where the decider stood. | Reads as blame if "you" or a named role is the culprit; avoid yes/no ("Would you have launched?"), which is weaker in our data (n = 19). | 9 Seat of the decider, 10 Close-up gaze |
| F8 | Evidence demo | Why did [a simple demonstration] explain [event]? | *Why did a glass of ice water explain Challenger?* | Promises evidence, like Veritasium's "We tested it" (9.3M). | The demo must be real and documented (Feynman, 11 Feb 1986). | 4 Exhibit A |

**Patterns to avoid (all fail the checker):** statements and labels ("The Vajont Dam Disaster"); colons and series tags; "Who ..." (invites blame); yes/no questions as the default; ALL CAPS or exclamation marks; two or more numbers; vague words ("this", "thing", "something"); a year tag in parentheses; loud words (shocking, insane, secret); anything about bodies or blood.

## 7. The title bank: 36 titles and 12 Shorts titles

Each story has three titles built from different formulas, so one Test & Compare run (up to three variants, title only) compares patterns. **Slot A** is the strongest hook and the one to publish first; **slot B** uses a different formula; **slot C** is searchable and carries the event name late. Every title passes `tools/title_check.py`. The fact basis comes from the registry (`STRESS-RISER-AI.md` C8, B2.7, D7); **re-verify every number against the primary report before publishing** (the channel rule is "nothing invented"). Source grades: [A] primary report read, [B] secondary, [C] weak sourcing (Piper Alpha, Note 7, Quebec, Vasa).

The "Short" column gives a Shorts title of 40 characters or fewer, because vendor sources say Shorts titles are truncated at about 40 characters in the mobile feed [C, unverified]. Shorts follow the same brief: a question, no ask. The title is separate from the first frame, which carries the outcome (`thumbnail-styles.md` and `STRESS-RISER-AI.md` B4.8).

| Story | Slot | Pattern | Title | Chars | Short (40 or fewer) | Fact basis | Source grade |
|---|---|---|---|---|---|---|---|
| Comet 1954 | A | Odd true detail | Why did a jet airliner end up in a water tank? | 46 | Why did engineers test a jet in water? (38) | Whole fuselage tested in a water tank (Withey 1997; Aerossurance) | B/C |
| Comet 1954 | B | Paired failures | Why did two Comet airliners break apart in flight in 1954? | 58 |  | 35 died 10 Jan (Elba), 21 died 8 Apr (Naples), both 1954 | B/C |
| Comet 1954 | C | Searchable mechanism | How did a tank of water solve the Comet airliner mystery? | 57 |  | Tank test failed after 3,057 cycles; fatigue crack, not the windows | B/C |
| Tacoma Narrows 1940 | A | Age contrast | Why did a four-month-old bridge twist itself apart? | 51 | Why did a new bridge twist itself apart? (40) | Opened 1 July, fell 7 Nov 1940 (WSDOT) | A |
| Tacoma Narrows 1940 | B | Odd true detail | Why were workers chewing lemons on a twisting bridge? | 53 |  | Workers chewed lemons against nausea (documented, D7) | B |
| Tacoma Narrows 1940 | C | Searchable plus number | Why did the Tacoma Narrows Bridge collapse in a 42 mph wind? | 60 |  | Wind 42 mph measured 09:30; collapse 11:02 (WSDOT) | A |
| Vajont 1963 | A | Paradox with a number | Why did 1,900 people die under a dam that never broke? | 54 | Why did 1,900 die under a dam that held? (40) | 1,917 dead (Italian Civil Protection), counts 1,919 to 2,056, so about 1,900; dam stood | B |
| Vajont 1963 | B | Mechanism | How can a dam hold and still flood a village below it? | 54 |  | Slope slid about 260 million cubic meters into the lake; wave over the crest; village below (D7) | B |
| Vajont 1963 | C | Searchable | What really happened at the Vajont Dam in 1963? | 47 |  | 9 Oct 1963 (Civil Protection) | B |
| Vasa 1628 | A | Contrast with a crowd | Why did a brand-new warship sink in front of its own crowd? | 59 | Why did a new warship sink on day one? (38) | Sank on maiden voyage after about 1,300 m; crowd on shore (secondary) | C |
| Vasa 1628 | B | Distance contrast | Why did a warship sink under a mile into its first voyage? | 58 |  | About 1,300 m is 0.8 mile (so 'under a mile') | C |
| Vasa 1628 | C | Searchable | Why did the Vasa sink on its maiden voyage? | 43 |  | Autocomplete: 'why did the vasa sink' | C |
| Challenger 1986 | A | Small cause | Why did a rubber ring destroy a space shuttle? | 46 | Why did a rubber ring doom a shuttle? (37) | O-ring joint; breakup at 73 s (Rogers Commission Vol. 1) | A |
| Challenger 1986 | B | Evidence demo | Why did a glass of ice water explain Challenger? | 48 |  | Feynman's ice-water demonstration, 11 Feb 1986 (Rogers Vol. 4) | A |
| Challenger 1986 | C | Decision seat | Why did Challenger launch in the coldest weather yet? | 53 |  | 36°F, 15°F colder than any earlier launch (Rogers Vol. 1) | A |
| Northeast blackout 2003 | A | Small cause with a number | Why did a few trees help black out 50 million people? | 53 | Why did trees help black out 50 million? (40) | About 50 million people; lines tripped on overgrown trees from 15:05; the report lists four cause groups, so 'help' (Task Force) | A |
| Northeast blackout 2003 | B | Mechanism | How can a silent alarm hide a failing power grid? | 49 |  | Alarm system failed after 14:14 and stayed dead; operators 'remained unaware' (Task Force) | A |
| Northeast blackout 2003 | C | Searchable | Why did the lights go out across the Northeast in 2003? | 55 |  | 14 Aug 2003 (Task Force) | A |
| Galaxy Note 7 2016 | A | Paradox | Why did the same phone fail for two different reasons? | 54 | Why did a replaced phone fail again? (36) | Two defects: electrodes touching at a fold (original), welding defects (replacement); secondary | C |
| Galaxy Note 7 2016 | B | Contrast | Why did a recalled phone fail again after it was replaced? | 58 |  | Discontinued 10 Oct 2016; FAA/PHMSA flight ban 14 Oct | C |
| Galaxy Note 7 2016 | C | Searchable | Why did the Galaxy Note 7 catch fire? | 37 |  | Autocomplete: 'why did the galaxy note 7 explode' | C |
| Quebec Bridge 1907 | A | Decision seat | Why did engineers keep building a bending bridge? | 49 | Why keep building a bending bridge? (35) | Bent lower chords noticed for weeks (secondary) | C |
| Quebec Bridge 1907 | B | Time contrast | Why did an unfinished bridge fall in just 15 seconds? | 53 |  | Collapse took about 15 seconds; 29 Aug 1907 (secondary) | C |
| Quebec Bridge 1907 | C | Searchable | What went wrong with the Quebec Bridge in 1907? | 47 |  | 29 Aug 1907 | C |
| Big Dig ceiling 2006 | A | Small cause | Why did a Boston tunnel ceiling fall after glue let go? | 55 | Why did a tunnel ceiling fall in Boston? (40) | Epoxy with poor creep resistance (NTSB HAR-07/02) | A |
| Big Dig ceiling 2006 | B | Mechanism | How can glue slowly lose its grip on a tunnel ceiling? | 54 |  | Anchors slowly let go through creep (NTSB) | A |
| Big Dig ceiling 2006 | C | Searchable | What caused the Big Dig ceiling collapse in Boston? | 51 |  | 10 July 2006, 11:01 pm; about 26 tons fell (NTSB) | A |
| Hyatt Regency 1981 | A | Small cause | Why did one small change help bring down two hotel walkways? | 60 | Why did two hotel walkways fall in 1981? (40) | As-built change essentially doubled the load; original detail was about 60% of code (NBS 1982) | A |
| Hyatt Regency 1981 | B | Mechanism | How did swapping one steel rod for two double the load? | 55 |  | Two sets of rods replaced one continuous rod (NBS) | A |
| Hyatt Regency 1981 | C | Searchable | What really happened to the Hyatt Regency walkways? | 51 |  | 17 July 1981, Kansas City (NBS) | A |
| Piper Alpha 1988 | A | Object | Why did one hand-tightened steel disc start a platform fire? | 60 | Why did a steel disc start a rig fire? (38) | Blind flange fitted 'hand-tightened only' after the safety valve was removed (secondary summary of Cullen); other failures followed | C |
| Piper Alpha 1988 | B | Systems | How can a safety valve go missing without anyone knowing? | 57 |  | Permits filed in different boxes (secondary) | C |
| Piper Alpha 1988 | C | Searchable | Why did the Piper Alpha oil platform burn in 1988? | 50 |  | 6 July 1988, North Sea | C |
| Flixborough 1974 | A | Small cause | Why did one bypass pipe blow up a whole chemical plant? | 55 | Why did a bypass pipe blow up a plant? (38) | 20-inch bypass; 1 June 1974 (HSE); trigger contested, say so | A |
| Flixborough 1974 | B | Decision chain | How could a chemical plant fit a pipe with no drawing? | 54 |  | HSE: no drawing, no calculations, no pressure test | A |
| Flixborough 1974 | C | Searchable | What happened at Flixborough in 1974? | 37 |  | 1 June 1974, 16:53 (HSE) | A |

**What already exists next to each title** (so the pair can be differentiated, section 4):

| Story | Slot | What already exists on the results page |
|---|---|---|
| Comet 1954 | A | Nobody in the top 8 results uses the tank angle |
| Comet 1954 | B | Mustard (6.5M) uses 'Why You Wouldn't Want to Fly...' |
| Comet 1954 | C | Disaster Breakdown has 'What Really Caused The Comet Crashes?' |
| Tacoma Narrows 1940 | A | Crowded: five results over 1M views, mostly film clips |
| Tacoma Narrows 1940 | B | Nobody in the top results uses it |
| Tacoma Narrows 1940 | C | Practical Engineering: 'Why the Tacoma Narrows Bridge Collapsed' (1.7M); cause still argued, say so in the video |
| Vajont 1963 | A | All top results are labels or statements |
| Vajont 1963 | C | Top results are statements: 'The Vajont Dam Disaster' |
| Vasa 1628 | A | RealLifeLore: 'Destroyed by a Breeze'; Atomic Frontier: 'Who Sank the Vasa?' (blame framing, avoid) |
| Challenger 1986 | A | Saturated; the rubber-ring angle is not in the top results |
| Challenger 1986 | C | Bailey Sarian already has 'What really happened to the Challenger?' (684K) |
| Northeast blackout 2003 | A | Practical Engineering owns 'What Really Happened During the 2003 Blackout?' (5.5M): do not copy it |
| Northeast blackout 2003 | B | Half as Interesting blames 'the software bug' (unverified in the report) |
| Galaxy Note 7 2016 | A | Tech channels dominate (JerryRigEverything 14.6M); weakest fit for the channel |
| Quebec Bridge 1907 | A | Brick Immortar (678K) and Iron and Memory frame it as ego: avoid blame |
| Big Dig ceiling 2006 | A | Industrial Empire (800K, 3 weeks old) already has 'Then the Glue Began to Creep' |
| Big Dig ceiling 2006 | C | Autocomplete shows people search 'big dig ceiling collapse' |
| Hyatt Regency 1981 | A | Crowded angle: 'This Tiny Change KILLED 114 People' (410K), 'The Design Change That Took 114 Lives' (1.1M) |
| Hyatt Regency 1981 | B | Explains the change instead of just naming it |
| Piper Alpha 1988 | A | '167 Men Died From Reasonable Decisions' (3.7M) already uses the chain-of-decisions angle |
| Piper Alpha 1988 | C | Smithsonian: 'What Caused the Giant Piper Alpha Oil Rig Explosion?' (1.1M) |
| Flixborough 1974 | A | Raven's Eye already has 'Temporary Bypass Pipe Failed' |
| Flixborough 1974 | C | Plainly Difficult (1M): 'Where Did it go so Wrong?' |

## 8. Testing titles

- **Use Test & Compare in title-only mode** after the thumbnail test, not at the same time. YouTube lets one test cover title, thumbnail or both, and any edit mid-test stops it. Testing the title while the thumbnail is also changing mixes two effects. Plan: at publish, test thumbnails (existing plan, `STRESS-RISER-AI.md` B4.6) with slot A as the title; after the thumbnail winner is clear, run a title-only test with A, B and C on the same video. Upload the one you prefer first, since an inconclusive test keeps the first.
- **Make the three variants structurally different** (YouTube: tests of "too similar" options run longer). The bank is built that way.
- **Expect "Performed Same" for small differences.** The sample-size table in `STRESS-RISER-AI.md` B2.6 says a 25% relative CTR gain needs about 6,700 impressions per variant, and a 100% gain about 550. Title wording moves CTR by far less than a thumbnail concept does, so a small channel will mostly see ties. That is not a failure; it says the wording does not matter much at this size.
- **The question worth the tests is slot A versus slot C: with or without the event name.** It is the one real structural choice (browse curiosity against search match). Decide it across 8 to 10 videos, not one.
- **Log every video:** title slot and formula (F1 to F8), characters, whether it names the outcome, whether it has a number, whether the event name appears, CTR by traffic source, average view duration, test result. After 8 to 10 videos compare slots. Do not judge by CTR alone: a rising CTR with falling average view duration means the title over-promised.
- **No manual swaps and no CTR checks in the first hours** (YouTube's own advice; early impressions skew to familiar viewers).
- **Shorts:** no Test & Compare for Shorts. Pick the Shorts title by formula, not by test.

## 9. Corrections to the earlier drafts

Run through `tools/title_check.py` on 2026-10-01.

- **`STRESS-RISER-AI.md` B4.7 (ten drafts):** all ten pass. The brief's own example gets only a "vague word" notice, which is a false alarm for the relative pronoun "that" (since removed from the checker).
- **`STRESS-RISER-AI.md` D7 (twelve titles):** five fail the checker's hard length limit (70 characters) and six more exceed the 60-character guide. Only the Vajont title (the brief's own, 54 characters) is clean.

| D7 story | Draft title | Characters | Problem | Replacement in the bank |
|---|---|---|---|---|
| Challenger | Why did a piece of rubber that stopped working in the cold destroy a space shuttle? | 83 | Far too long; too much detail (concreteness result) | A: Why did a rubber ring destroy a space shuttle? (47) |
| Piper Alpha | Why did an oil platform burn because the night shift never learned a safety valve was missing? | 94 | Too long; points at the night shift | A: Why did one hand-tightened steel disc start a platform fire? (60); B: How can a safety valve go missing without anyone knowing? (57) |
| Big Dig | Why did the ceiling of a Boston tunnel fall after glue slowly let go of its bolts? | 82 | Too long | A: Why did a Boston tunnel ceiling fall after glue let go? (55) |
| Blackout | Why did a few overgrown trees and a silent alarm black out 50 million people? | 77 | Too long; two causes | A: trees (53), B: silent alarm (49) |
| Vasa | Why did the most powerful warship in the Baltic sink in front of the crowd that came to watch it sail? | 102 | Over YouTube's 100-character limit; "most powerful warship in the Baltic" is not in the fact registry | A: Why did a brand-new warship sink in front of its own crowd? (59) |
| Tacoma | Why did a four-month-old bridge twist itself apart in a 42 mph wind? | 68 | Over 60 | A: without the wind (51); C carries the wind (60) |
| Hyatt | Why did a small change to one steel rod bring down two hotel walkways? | 70 | Over 60; "bring down" overstates (NBS: the original design was already about 60% of code) | A: "help bring down" (60) |
| Comet | Why did engineers put an entire jet airliner in a tank of water? | 64 | Over 60 | A: Why did a jet airliner end up in a water tank? (46) |
| Flixborough | Why did a temporary pipe with no drawing blow up a chemical plant? | 66 | Over 60 | A (55), B: How could a chemical plant fit a pipe with no drawing? (53) |
| Note 7 | Why did the phone that was recalled and replaced keep catching fire? | 68 | Over 60; "keep" implies more fires than the registry documents | A or B |
| Quebec | Why did engineers keep building a bridge that was already bending? | 66 | Over 60 | A: Why did engineers keep building a bending bridge? (49) |

- **B4.7's warning** that titles 3, 6 and 9 (Comet, Tacoma, Blackout) carry the end of their key idea after character 40 stands. Most bank titles are 45 to 60 characters, so the tail of some will be cut on a small screen; where it matters, the Shorts column shows a version of 40 characters or fewer that keeps the hook in view.

I did not edit `STRESS-RISER-AI.md` or `STRESS-RISER-MASTER.html` (generated files). If you want them updated, the sources are `master/` and `master/ai/`, rebuilt with `tools/build_ai.py` and `tools/build_master.py`.

## 10. Checklist and tool

`python3 tools/title_check.py "Why did ...?"` checks one or more titles; `--short` applies the Shorts limit (40 characters); `--bank data/title-bank.csv` checks the whole bank. It fails: no single closing question mark; colon, dash or pipe; an opener that is not a question word (case name first or statement); "Who ..." openers; a long title (more than 70 characters, or more than 60 for a Short); an exclamation mark, ALL-CAPS word or emoji; loud or clickbait words and phrases; blame words; gore words. It warns: soft length (above 60, or above 40 for a Short); yes/no openers; British spelling; two or more numbers; vague words; a trailing year tag. It cannot check facts, tone or honesty.

By hand, for every title:

1. Is every number and name in the fact registry and re-verified against the primary report? Is it rounded the way the source allows ("about 1,900")?
2. Does the title name the outcome, and one concrete object or number (not four facts)?
3. Is the hook inside the first 40 characters?
4. Does the thumbnail say something the title does not? (`STRESS-RISER-AI.md` B4.7, four pair-check questions.)
5. Will the video show or explain everything the title promises by second 15?
6. Does it blame a system and not a person? Is any contested cause (Tacoma, Flixborough, Vasa) worded as contested?
7. Is it unlike an existing big title on the same story (section 4)?
8. For Shorts: 40 characters or fewer, a question, no ask.

## 11. Decisions I need from you

1. **Event name in the title.** The brief forbids a case name first but not later. Slot C titles carry the name ("What went wrong with the Quebec Bridge in 1907?"). Do you accept them as test variants, or should every title keep the name out and the name live in the description only?
2. **"What really happened ...?"** is Practical Engineering's formula (Arecibo 9.4M, Oroville 5.3M, the 2003 blackout 5.5M). It works and is a question, but it is theirs and "really" is a stock word. I used it twice in the bank (Vajont C, Hyatt C). Keep or replace?
3. **Yes/no titles** (the decision seat: "Would you have launched at 36 degrees?"). The brief allows them and they fit the voice, but our data leans weak (n = 19). I left them out of the bank. Allow as a test only?
4. **A death toll in a title.** The brief's example uses one (1,900). The thumbnail research advises against it in thumbnails. Vajont A uses it; the other bank titles avoid it. Confirm.
5. **Colon ban.** Series tags are slightly more common in top groups, but the brief bans them and I did not weaken the rule. No action needed unless you want a series name (for example a recurring "Stress Riser" tag) at the end; YouTube itself says to save branding for the end.
6. **Update the generated files** (`STRESS-RISER-AI.md`, the master HTML) with this research, or leave them as the thumbnail edition?

## 12. Caveats and what I could not do

- **Title truncation was not measured.** I tried to measure the real cut-off with a headless mobile browser. YouTube's logged-out home feed and search page did not render in this environment, so only a channel's video list rendered, which uses a different layout (14 px Roboto, a three-line clamp, a text column about 142 px wide). That is not the home feed, so the "about 40 characters on a phone" guideline remains an unverified vendor figure [C]. YouTube's own statement is only that viewers "may only see part of your title".
- **Our title analysis is correlation** in two non-random samples with rounded views and uncontrolled age (section 3.2). It is a prior, not a test.
- **Competition and autocomplete are one logged-out snapshot** (2026-10-01, US, English). They change by region, time and person. They show who is there, not search volume. I did not find a way to get search volume.
- **Headline studies are about news, not YouTube.** They are randomized and large, which is why they are in section 3.4, but the audience and the task differ. The Lai and Farbrot 2014, Kuiken 2017 and Chartbeat findings are secondhand; the original pages returned 403 errors or I could not reach them.
- **Vendor studies** (OverseerOS, ViewsKit, AIR) were read through the fetch tool's summaries. The AIR page was truncated. None measures CTR.
- **The bank's facts come from the earlier registry**, including its weakly sourced stories (Piper Alpha, Note 7, Quebec, Vasa are [C]). Re-verify before use; legal status of the stories is not fully verified either (`STRESS-RISER-AI.md` B2.7).
- Nothing here changes the brief's age and legal filters: nothing less than two years old, no ongoing legal cases.

## 13. Sources and files

**YouTube Help [A]:** https://support.google.com/youtube/answer/12340300 (thumbnail and title tips), https://support.google.com/youtube/answer/2801973 (spam, deceptive practices and scams, misleading metadata), plus the Test & Compare and CTR FAQ pages in `research/packaging.md`.

**Headline research [A]:** Robertson et al. 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10202797/ ; Quere et al. 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC11704130/ ; Rogers, Shulman and Markowitz 2024 (Science Advances, DOI 10.1126/sciadv.adn2555), summarized at https://www.harvardmagazine.com/2024/06/simple-headlines-are-better and https://phys.org/news/2024-06-simple-headlines-online-news-readers.html .

**Secondhand [C]:** https://gist.github.com/NHagar/77c3f2e9df9c211d2abce7982f794135 (digest of question, length, number and negativity studies); https://journalistsresource.org/media/simple-headlines-online-news-readers/ (summary of Rogers et al. 2024).

**YouTube title studies [C]:** https://www.overseeros.com/blog/should-youtube-titles-be-questions ; https://www.overseeros.com/blog/best-youtube-title-length-study ; https://viewskit.com/blog/youtube-title-length-curve ; https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches

**Our data and tools (all in `stress-riser/`):**

| Path | What |
|---|---|
| `title-research.md` | this file |
| `data/title-bank.csv` | the 36 bank titles with Shorts titles, fact basis, grade, competitor notes |
| `data/title-analysis-report.md`, `data/title-features.csv` | all tables of the 854-title analysis; per-title features |
| `data/title-competition.md`, `.csv` | top ten results for two phrases per story, exact views |
| `data/title-autocomplete.md`, `.json` | YouTube search-box suggestions for 12 stories, 12 phrasings each |
| `tools/title_analysis.py` | the title analysis (stdlib only) |
| `tools/title_competition.py`, `tools/title_autocomplete.py` | collect competition and suggestions (need outbound HTTPS and curl) |
| `tools/title_check.py` | the brief-rule checker |
