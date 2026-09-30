# Packaging research notes (Stress Riser) — working file
Date of research: 2026-09-30. Grades: [A] official/peer-reviewed/large dataset; [B] first-hand creator/company data; [C] opinion/anecdote.
Tools: helper scripts yt.py / chan.py / pop.py in this folder; thumbnails in thumbs/; raw pages in raw/; lists in lists/.

## 1. OFFICIAL YOUTUBE DOCS (fetched raw 2026-09-30)
### A/B testing ("Test & compare") — https://support.google.com/youtube/answer/13861714?hl=en  [A]
- Up to 3 titles and/or thumbnails; options: Title only / Thumbnail only / Title and thumbnail.
- DESKTOP Studio only; not available for Shorts, scheduled lives, Premieres (until converted), made-for-kids, private videos.
- Winner = highest WATCH TIME SHARE (not CTR). YouTube: "we optimize tests for overall watch time over other metrics, like click-through-rate." Reason given: great titles/thumbnails help viewers understand what the video is about "so that they don't waste their time clicking on the wrong videos".
- Results: Winner ("statistically significant"), Performed Same, Inconclusive. If no clear winner, FIRST uploaded option is shown to all (so put the option you prefer first).
- Completes "within two weeks"; "a few days or up to 2 weeks" depending on impressions, recency, other factors.
- If title or thumbnail is changed during test, test stops automatically.
- Tests run concurrently (true A/B/C at the same time). Third-party tools often run sequentially and optimise for CTR only -> can give conflicting results.
- "Testing titles and thumbnails that are too similar to each other can cause tests to run for longer." -> use diverse variants.
- Recommends testing OLDER videos first to limit impact on channel views.
- Small percentage of traffic may be held out as a control group that only sees default.
- Resolution: if any thumbnail is <720p (1280x720) all experiment thumbnails are downscaled to 480p (854x480).
- Why results differ: "early impressions are more likely to come from viewers who are already familiar with your channel, while later impressions are more likely to include viewers who haven't yet watched your channel" (audience composition drift).
- NO official minimum-impression number is published. "Not enough impressions" listed as a reason for no winner. (Third-party "1,000-5,000 impressions per variant, 10,000 total" = UNVERIFIED rule of thumb, from vidIQ-style blogs.)

### Impressions & CTR FAQ — https://support.google.com/youtube/answer/7628154?hl=en [A]
- "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%."
- "New videos or channels (like those less than a week old), or videos with fewer than 100 views can see an even wider range. If a video gets a lot of impressions (such as if it appears on the Home Page), it's natural for the CTR to be lower. Videos where most of the impressions are from sources like your channel page may have a higher rate."
- Avoid: "Deciding without enough data ... Avoid checking your click-through-rate immediately after uploading." "Improving for small changes in click-through-rate." "Testing several thumbnails or titles on the same video [manually]. It's difficult to make sure each video is being seen by the same audience. Differences in click-through-rate might be due to traffic sources, rather than the title or thumbnail."
- "Avoid trying to increase your CTR using thumbnails or titles that are clickbait. ... Clickbait videos tend to have low average view duration and therefore are less likely to get recommended by YouTube. You can tell if your thumbnail is clickbait if it's getting high CTR but low average view duration and lower than expected Impressions."
- CTR is only counted on registered impressions; not all views come from thumbnail impressions.

## 2. PADDY GALLOWAY (first-hand posts via api.fxtwitter.com, fetched 2026-09-30) [B]/[C]
- 2024-07-10 https://x.com/PaddyG96/status/1811083499044044951 : "19. Make sure thumbnail passes the 'glance test' - can you process everything in just a quick glance? Viewer gets just milliseconds to view it as they are scrolling. 20. Don't forget to view the title and thumbnail as one, do they compliment each other or contradict/repeat?"
- 2024-05-10 https://x.com/PaddyG96/status/1788967959882346991 : "22. Always plan your title and thumbnail before recording, everyone knows this, few do this."
- 2022-08-29 https://x.com/PaddyG96/status/1564326373170319360 : "4. Thumbnail concepts are (seriously) underrated. The psychology behind enticing the click in the thumbnail > the colours, design or beauty."
- 2023-07-13 https://x.com/PaddyG96/status/1679470163308019717 : when to change packaging. Video ranked "8/10 (bad)" at first hour became "1/10" with NO change. Four considerations: (1) topic (news vs evergreen), (2) audience fit (algorithm re-targets regular viewers faster than finding new audience), (3) metrics "carefully" — people over-value CTR/AVD; in first hours they give "some insight"; if views are low but AVD and CTR look great relative to impressions, give it more time, (4) subjective opinion of team on packaging pre-upload — "I'm always going to be more loyal to a thumbnail and title that we all felt strong about". Scenario: 8/10 in first hour + non-urgent + experimental + good metrics + team likes packaging -> wait; 8/10 + trending topic + good audience fit + bad metrics + team on the fence -> change thumbnail.

## 3. MRBEAST PRODUCTION MEMO (leaked Sept 2024; text via alexanderjarvis.com copy, raw HTML fetched) [B — leaked, authenticity widely reported but not officially confirmed by grader; treat as B/C]
- Source: https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/
- "The three metrics you guys need to care about is Click Thru Rate (CTR), Average View Duration (AVD), and Average View Percentage (AVP)."
- "The title and thumbnail on the videos you will be producing set the expectations for the viewer for your video." Bouncy castle example: yellow in thumbnail, red in video -> "You'd feel like you were lied to and click off". "THIS IS WHY YOU MUST KNOW THE TITLE AND THUMBNAILS OF THE VIDEOS YOU ARE MAKING!" "How can you know how to start your video if you don't even know what expectations the viewers have of you?"
- "I Spent 50 Hours In My Front Yard is lame ... 'I Spent 50 Hours In Ketchup' ... easily 100x more viral" (his claim, no data). "In general the more extreme the better." (NOT suitable for this channel's honest tone, but the expectation-matching part is.)
- The first minute is "the most important minute"; front-load; the video's opening must match the clickbait promise.
- "Critical components": title/thumbnail elements (e.g. the bouncy castle colour) must appear in the video.

## 4. THE OVERSEER OS STUDY (vendor blog; methodology stated) [C+ / B-]
- https://www.overseeros.com/blog/youtube-thumbnail-text-vs-title-study (dated Aug 12, 2026, per page).
- Corpus: 16,152 long-form videos with >=1M views across 986 channels; text-comparison sample: 300 videos (from 9,279 title-compatible), 202 channels; 298 processed; 217 classifiable text-bearing thumbnails.
- Thumbnail text vs title: exact match 4.1% (9); mostly repeated 21.2% (46); mixed overlap+new wording 28.6% (62); completely complementary 46.1% (100). 74.7% did not mostly repeat; 25.2% had no reliable text detected.
- CAVEAT: only videos that already reached >=1M views (survivorship); no CTR data; text overlap is vocabulary overlap, not meaning. Shows what winners look like, not that complementarity CAUSES higher CTR.

## 5. VERITASIUM / DEREK MULLER
- Video: "Clickbait is Unreasonably Effective" https://www.youtube.com/watch?v=S2xHZPH5Sng — fetched page: 8,297,543 views, Aug 17, 2021 (as of 2026-09-30); originally titled "We Need to Talk About Clickbait" (renamed; per IMDb/HN). Veritasium page https://www.veritasium.com/videos/2021/8/17/we-need-to-talk-about-clickbait says only: "The title and thumbnail play a huge role in a video's success or failure."
- Transcript could not be fetched (youtube-transcript-api IpBlocked). Details below are from secondary summaries (gigazine 2021-08-30 https://gigazine.net/gsc_news/en/20210830-clickbait-effective/; IMDb/HN) -> [C]: Type 1 clickbait ("legitbait", clearly conveys the main content) vs Type 2 (misleading; "clicktrap"); old video "Strange Applications of the Magnus Effect" renamed "Backspin Basketball Flies Off Dam" (fetched: 2OSrvzNW9FE 60M views, 11 years ago in popular list); asteroid video re-titled "These are the asteroids to worry about" (4Wrc4fHSCpw 81M views 5 years ago). Muller reports view peaks after re-packaging.
- The Ringer, 2026-03-09 https://www.theringer.com/2026/03/09/pop-culture/youtube-face-thumbnails-history-explained : Muller: internal research found faces "[not] that important" for Veritasium; Rene Ritchie (YouTube head of editorial): algorithm measures watch retention/satisfaction, and "thumbnail that makes the best promise that the video then delivers on is the one that we measure as the winner." [B/C via journalist]
- "50% more views from thumbnail testing" and "tests 10+ variants" claims from influencermarketinghub etc. = UNVERIFIED (no primary source).

## 6. INK EXPLAINER (the brief's stated narration model) — fetched channel pages 2026-09-30
- Handle @Inkexplainer96: 106K subscribers, 16 videos (per channel page, 2026-09-30); first video ~5 months ago. Stick-figure cartoon animation, question titles. VERY relevant cold-start case.
- Popular list (view counts abbreviated by YouTube, as fetched 2026-09-30): "What Did Ancient Humans Actually Do All Day?" 9.7M (1 mo ago); "What Did Ancient Humans Do When It Rained All Week?" 1.5M; "Why Are We the Only Human Species Left? What happened to others..." 1.2M; "When Did Ancient Humans Start Drinking Alcohol?" 886K; "How Did Ancient Humans Travel the World?" 801K; "The Disturbing Ways Ancient Humans Survived Winter" 756K; ... down to 15K-42K for weakest. => enormous spread (15K-9.7M) inside one template; the template does not decide the outcome, the idea + text tease does.
- Thumbnails (viewed): all use: one stick figure (round white head, dot eyes) in rich illustrated scene; 1-3 words of BIG outlined text at top (yellow or white), often a 'tease/answer' word rather than title repeat: title "What Did Ancient Humans Actually Do All Day?" -> text "NO JOBS"; "...Rained All Week?" -> "RAINED ALL WEEK" (repeats title words); "Why Are We the Only Human Species Left?" -> "Why Us?"; "...Drinking Alcohol?" -> "DRINKS ALL DAY"; "How Did Ancient Humans Travel the World?" -> "TRAVEL HOW?"; "Disturbing Ways...Survived Winter" -> "COZY INSIDE?"; "Real Reason Humans Started Wearing Clothes" -> "WHY CLOTHES?"; "When Did ... Smoking Weed?" -> "STONED ALL DAY"; "Why Ancient Humans Were The Most TERRIFYING Animal Alive" -> "BORN TO KILL?" (blood, grin - outlier style).
- Contact sheets: lists/sheet_ink1.jpg, lists/sheet_ink2.jpg

(to be continued below)

## 7. FETCHED EXAMPLES (title / thumbnail / channel / videoID / views as fetched 2026-09-30 from channel "Popular" tab, abbreviated by YouTube; exact counts were blocked by YouTube bot-check after ~20 watch-page requests)
Thumbnails as currently shown (may differ from original upload). Contact sheets: lists/sheet_a.jpg, sheet_b.jpg, sheet_c.jpg, sheet_ink1.jpg, sheet_ink2.jpg, sheet_shorts.jpg. Files: thumbs/<id>.jpg
| # | Channel | Title (chars) | ID | Views / age (as fetched) | Thumbnail | Analysis (my inference = [C]) |
|1| Veritasium | Why Are 96,000,000 Black Balls on This Reservoir? (49) | uxPdPpi5W4o | 112M, 7y | host on boat pointing at sea of black balls, NO text | image = the anomaly at human scale; title = number + question. Zero-text pairing works when the image alone raises "what is that?" |
|2| Veritasium | Why It Was Almost Impossible to Make the Blue LED (49) | AF8d72mA41M | 55M, 2y | 3 LEDs, "EASY EASY ALMOST IMPOSSIBLE" + arrow | text = the contrast the title only implies; image = the comparison. Text overlaps 2 title words but adds the 'easy' baseline |
|3| Veritasium | How A Student's Question Saved This NYC Skyscraper (50) | Q56PMJbCFXQ | 26M, 1y | stylised illustrated engineer on phone + red-highlighted structure + arrow, no text | illustrated (not photo) rendering of an engineering-disaster story; person + object; title carries the story |
|4| Veritasium | Is spider web really stronger than steel? (41) | wt4p2oalmRY | 9.3M, 1mo | "We tested it" + fingers stretching spider silk | QUESTION title + text that promises EVIDENCE not repeating title |
|5| Practical Engineering | What Really Happened at the Arecibo Telescope? (46) | 3oBCtTv6yOw | 9.4M, 5y | aerial of holed dish, text "ARECIBO TELESCOPE COLLAPSE" + small logo | title = mystery ('what really'); thumbnail = the OUTCOME (word 'collapse' + holed dish) the title never states. Text repeats nouns but adds outcome |
|6| Practical Engineering | What Really Happened at the Oroville Dam Spillway? (50) | jxNM4DGBRMU | 5.3M, 5y | broken spillway photo, text "OROVILLE DAM" | pure label + damage image; title supplies the tension |
|7| Practical Engineering | Why Are Beach Holes So Deadly? (30) | 0kQXOTcEB_E | 7M, 1y | tiny figure with shovel in huge sand trench, no text | scale image = danger; title = question |
|8| Practical Engineering | The Wild Story of the Taum Sauk Dam Failure | zRM2AnwNY20 | 11M, 1y | cut-out of breached reservoir wall over aerial | statement-style title (not a question) |
|9| Real Engineering | The Questionable Engineering of Oceangate | 6LcGrLnzYuU | 4.9M, 3y | submersible + arrow, "DOOMED TO FAIL?" | statement title + QUESTION in image (reverse of our format) |
|10| Kurzgesagt | Why Blue Whales Don't Get Cancer - Peto's Paradox | 1AElONvi9WQ | 27M, 6y | monster illustration, "CANCER PARADOX" | whale in title, concept word in image; no whale shown |
|11| Kurzgesagt | How Are Memories Stored Inside Your Brain? (42) | PqtggjVAi8M | 3.1M, 3mo | glowing neuron cluster + red arrow, "THIS IS A MEMORY" | question title + image/text that 'shows the answer object' |
|12| Mark Rober | World's Largest Jello Pool- Can you swim in Jello? (50) | DPZzrlFCD_I | 223M, 7y | man in red jello pool, no text | image = the answer/experiment; title superlative+question |
|13| Ink Explainer | What Did Ancient Humans Actually Do All Day? (44) | 49_Ph2q6uIM | 9.7M, 1mo | relaxed stick figure on rock in savanna scene, "NO JOBS" | QUESTION title + 2-word ANSWER-TEASE. Closest model for this channel |
|14| Ink Explainer | What Did Ancient Humans Do When It Rained All Week? | SD7XyG2wd1k | 1.5M, 2mo | cave in rain, "RAINED ALL WEEK" | text repeats title words (weaker complement) |
|15| Ink Explainer | Why Are We the Only Human Species Left? What happened to others... (66) | OCr6NteWSQ8 | 1.2M, 3mo | 5 hominins, "Why Us?" | title long (66 chars) and trails; text is short question |
|16| TED-Ed | How do solar panels work? - Richard Komp | xKxrkht7CpY | 26M, 10y | hand-lettered "HOW SOLAR PANELS WORK" + TED-Ed badge | FULL REPEAT of title, yet 26M: works for search-intent evergreen topics (my inference); counterexample to 'never repeat' |
|17| TED-Ed | Can you solve the prisoner hat riddle? - Alex Gendler | N5vJSNXPEwA | 37M, 10y | "CAN YOU SOLVE THE HAT RIDDLE?" over coloured figures | full repeat again |
- Brief's example title "Why did 1,900 people die under a dam that never broke?" = 54 characters.
- Veritasium latest titles in 2026 also use question form (e.g. "Is spider web really stronger than steel?", "Why does every mammal get 1 billion heartbeats in their life?" tL9Lw250spc 6.4M 2mo) — question titles are normal for top educational channels, not only TED-Ed.

## 8. TITLE LENGTH / TRUNCATION
- YouTube hard limit 100 characters (widely documented; not re-fetched). Visible length on phones: vendor/SEO blogs claim ~40-50 chars in mobile home feed, 50-55 typical, 50-60 in search (e.g. fluxnote.io, charactercounter.com, channelpreview.vercel.app) = [C], device-dependent, NOT official. I could not measure it. Top examples above are 30-54 chars (median ~49). Ink Explainer's 66-char title is the longest among examples.
- Rule: put subject + tension in the first ~40 characters; thumbnail text must NOT re-say the first 40 characters and must not depend on words that sit in the truncated tail.

## 9. TESTING MATH (my arithmetic: standard two-proportion sample size, alpha 0.05 two-sided, power 80%; CTR only — YouTube's tool uses watch-time share so this is indicative)
- 4% vs 5% (+25% rel): ~6,735 impressions per variant. 4% vs 6% (+50%): ~1,859 per variant. 4% vs 8% (+100%): ~549. 3% vs 4.5%: ~2,512. 4% vs 4.8% (+20%): ~10,302 per variant.
- Meaning: a small channel can only detect RADICALLY different concepts (+50% or more). Tweaks (colour, font) are undetectable at small-channel volumes. Three variants triple the requirement.
- Vendor claims (thumbnailcreator.com): "<1,000 impressions per variant = 43% false-positive rate"; "23% of day-3 winners flip by day 7"; "5,000+ impressions definitive" -> UNVERIFIED (no method, no source; a cited 'Dr. William Sen' test looks unverifiable). "1,000-5,000 impressions per variant, 10,000 total" (vidIQ-type blogs) -> UNVERIFIED rule of thumb.

## 10. COLD START
- YouTube Help [A]: half of channels' impressions CTR 2-10%; wider for <1 week / <100 views; Home-feed impressions lower CTR; channel-page higher; don't judge right after upload.
- Todd Beaupre (YouTube senior director of growth & discovery), Creator Insider interview 2026-09-01, reported by ppc.land https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ [B via reporting; quotes as extracted by tool]: "we see diverse audiences" in the early window; "videos are reaching people who've never watched the channel before" inside the first hour; "probably all your videos have about maybe a 10% or less click-through rate" in the subscribers row; "even your best videos, 90% of the time, your subscribed audience isn't deciding to watch."; "No metric on its own is a good indicator of value."
- YouTube growth team (SEJ 2024-03-04 https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/): "The algorithm for Discovery is focused more on individual videos" rather than channel averages [B]. => every video's packaging is judged fresh; no penalty from earlier weak videos.
- Claim "YouTube tests new channels with small diverse cohorts for 24-72h" (outlierkit-type blog) = UNVERIFIED specifics; only the qualitative 'diverse early audiences' is supported.
- Implication: cold viewers do not know the brand; thumbnail must communicate TOPIC + TENSION in one glance; brand layer is secondary.

## 11. RENE RITCHIE (YouTube Creator Liaison) via SEJ 2023-08-14 https://www.searchenginejournal.com/youtube-algorithm-insights-from-creator-liaison-renee-ritchie/493901/ (from The Editing Podcast) [B]
- "The first act can't just be an introduction. The first act has to be a reward. The thumbnail makes a promise, and the video has to deliver on it."
- "… I change the thumbnail, change the title, and now I'm targeting the broader audience." (on re-targeting a video)
- The Ringer 2026-03-09 attributes to him: thumbnail "that makes the best promise that the video then delivers on is the one that we measure as the winner" [C via journalist; could not confirm original wording].

## 12. SHORTS
- Official [A] support.google.com/youtube/answer/72431 (desktop tab): custom Shorts thumbnails only in YouTube Studio on a computer; account must be verified; upload 9:16; recommended 2160x3840, min width 640 px; 50MB desktop limit. A/B testing NOT available for Shorts [A] (answer/13861714).
- Mobile frame selector (pencil icon > choose frame) per vidIQ/RouteNote/CapCut how-tos [C].
- Where the cover shows [C, consistent across many vendor blogs, NOT confirmed in official doc I fetched]: never in the swipe-up Shorts player (video autoplays); shows in channel Shorts tab/grid, Shorts shelf, search, subscriptions, home. => cover matters for search/channel/shelf; in the swipe feed the FIRST FRAMES are the only 'thumbnail'.
- UNVERIFIED: "85% higher CTR in search with custom Shorts thumbnails; 0% effect in feed; 500 Shorts/50 channels/1M impressions" — appeared in a search-engine summary; the page I fetched (wbcomdesigns.com) does NOT contain it and states "YouTube has not published Shorts-specific thumbnail data". Treat as unsourced.
- Observed (contact sheet lists/sheet_shorts.jpg; views from Shorts tab 2026-09-30): Kurzgesagt Shorts covers = designed title-card frames ("This Organ Regrows Every Month!" oNTaHYXQ4MM 1M views; "Your Bones Produce Real Electricity!" RQprZZJIb6Y 404K) and also auto frames with burned-in captions ("gets much looser." b1EMX3wyqCY 537K; NIifnIP_NnQ 859K). Veritasium Shorts covers: face/object + 2-4 word serif title at bottom ("Scariest Chart In Engineering" O3a99HNskNk 1.4M; "Rome's Escalator Disaster" oR94cicO7xM 5.5M). Practical Engineering: series card "NAME THAT INFRASTRUCTURE / PAUSE HERE TO MAKE A GUESS" 3guUpquh6ctc... (3GUpquh6ctc 3.2M). 
- First-frame equivalent: frame 0-1 s = outcome image + 3-6 word on-screen outcome line; same frame usable as custom cover.

## 13. IDENTITY VS VARIETY
- Ink Explainer (16 videos, 106K subs): near-identical template on all thumbnails; views 15K to 9.7M -> template does not determine result; idea/tease does.
- Practical Engineering: recognisable = real-place photo + 2-3 word caps label + small logo; variance allowed (beach holes no text). Kurzgesagt: colour-coded neon palette + character illustration + 1-3 words. Veritasium: high variety (face+object, typographic 'We tested it', illustrated skyscraper); Muller (Ringer 2026) says faces not that important for them. TED-Ed: strict template (hand-lettered title, red badge).
- 'Series blindness' for YouTube thumbnails: NO rigorous public study found. Adjacent literature: banner blindness (eye-tracking; Springer Cognitive Processing 2023 https://link.springer.com/article/10.1007/s10339-023-01131-7 on banner type/theme consistency) [A for ads, not thumbnails]. '70% consistent / 30% variable' rule (vendor blogs) = UNVERIFIED opinion. Recommendation: fixed identity layer + variable concept layer.

## 14. MYTHS / CONTRADICTIONS
1. 'Thumbnail text must never repeat title' - TED-Ed 26M/37M fully repeat; but only 4.1% of the >=1M sample were exact matches (survivorship, vendor study). Truth: repetition is wasted space on browse surfaces; harmless on search-intent.
2. 'Maximise CTR' - YouTube's own test optimises watch-time share; third-party CTR tools can disagree.
3. 'Check CTR at hour 1 and swap' - YouTube says avoid checking right after upload; early impressions skew to familiar viewers.
4. 'Faces required' - Muller: faces not that important; Ink Explainer/Kurzgesagt have no real faces.
5. 'X% CTR is good' - YouTube: half of channels 2-10%.
6. Vendor stats on false-positive rates, Shorts 85% CTR, '50% more views' for Veritasium testing, '10+ variants' = UNVERIFIED.
