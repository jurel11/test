# PACKAGING STRATEGY, PAIRING, TESTING AND SHORTS: research report for Stress Riser

Full notes with URLs, quotes and evidence grades: `/tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/packaging/notes.md`. Thumbnails and contact sheets are in `.../packaging/thumbs/` and `.../packaging/lists/sheet_*.jpg`.

Grades: [A] official or large dataset. [B] first-hand creator or company statement. [C] opinion, vendor blog, or my own inference.

## Key findings

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

## Real examples (views as fetched 2026-09-30, abbreviated by YouTube)

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

## What this means for Stress Riser thumbnails
- **Aim for complement, not repeat.** The question title carries the who or what and the "why". The thumbnail shows the outcome scene (what broke, drawn with the brief's silhouette-and-cutaway style) plus 0–4 words that tease the answer or name the outcome ("NO JOBS" style), never a second question.
- **Text budget.** Two or three words in huge outlined type. The brief bans text inside generated images, so the words must be added in compositing.
- **Glance test at phone size.** One stick figure with one clear emotion, one focal object, and a high-contrast scene.
- **Honesty.** The thumbnail shows what the video shows by second 15. The brief's outcome-first opening already enforces this.
- **Variety.** Pick the concept type per video: answer-tease, outcome plus mystery, scale anomaly, or contrast.

## Packaging workflow (one long video per week)
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

## Sources
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

## Caveats and unverified items
- YouTube transcripts were blocked, so Veritasium's, Kurzgesagt's, Colin and Samir's and Jon Youshaei's own talks were not read. Their points here are secondary or not covered. I found no Kurzgesagt thumbnail video (only an announcement post), no Mark Rober or Wendover primary statements on packaging, and no Think Media or Nathan Graham material.
- Title truncation limits and the Shorts feed-versus-channel behavior are not from official documentation.
- UNVERIFIED: vendor impression thresholds, the false-positive rates, the Shorts "85% CTR", "Veritasium gets 50% more views from testing", and the "70/30" consistency rule.
- The Beaupré quotes come from ppc.land's reporting, not the video itself.
- I fetched 16 of the 17 example thumbnails at full size; view counts are abbreviated.