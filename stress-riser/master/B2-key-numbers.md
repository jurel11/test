## B2. Key numbers and facts, in one place

Every row says what was measured, the grade, and where to read more (a chapter in Part D or an appendix). Nothing here is new beyond the reports; it is a consolidated ledger. Where reports disagree, see B3.

### B2.1 Platform: specs, display, measurement, testing, policy

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
| Mobile Home experiment | YouTube varies thumbnail and video sizes; "some thumbnails may appear cropped" | [A] Team YouTube 2026-04-29 (page script-rendered) | D1 |
| CTR definition | "how often viewers watched a video after seeing a thumbnail"; tells "how eye-catching your video idea or 'packaging' is" | [A] Help 7628154, 16767369 | D1 |
| CTR benchmark | "Half of all channels and videos … between 2% and 10%"; wider for new videos or fewer than 100 views; not a target | [A] Help | D1 |
| Why CTR varies | falls as reach widens (Help's example: 9% on 10,000 impressions to 3.5% on 100,000); search: fewer impressions, higher CTR; home: high volume, lower CTR; early CTR inflated by loyal fans | [A] Help | D1 |
| Subscribers' feed CTR | "probably … 10% or less"; "90% of the time your subscribed audience isn't deciding" | [B] Beaupré 2026-09-01 via ppc.land | D1, D8 |
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
| Real victims | not allowed: reveling in or mocking an identifiable person's death; avoid company logos | [A] Help 2802268 | D1 |
| Originality | not monetizable: "AI-generated content made with generic or unoriginal templates"; "repeatedly uses disturbing themes (such as violence or loss) without building a cohesive narrative"; allowed: the same intro and outro with different substance | [A] Help 1311392 | D1 |
| AI disclosure | not needed for clearly non-realistic or animated content; the rules list AI help with a thumbnail among exempt uses; realistic fake events need it; labels added automatically for YouTube's own AI tools and C2PA metadata | [A] Help 14328491 | D1 |
| Shorts covers | custom cover on desktop Studio only; verified account (Help) vs Partner Program first (blog 2026-07-24); no A/B testing for Shorts | [A] | D1, D8 |
| Shorts feed | plays the video, no thumbnail shown; covers appear on channel page, homepage, search | [A/B] | D1, D8 |
| Shorts crop | search serves 405×720 (9:16) and 405×608 (2:3) variants; advice: key content inside a central 2:3 crop | [B] measured; [C] Ritchie via ppc.land | D1 |

### B2.2 CTR evidence: datasets, company data and creator experiments

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
| Existence proofs for cartoon thumbnails | Ink Explainer: faceless stick-figure channel, 77.8K subscribers at month 8 (third-party case study), one video 9.7M views; The Infographics Show "AMERICA CLOSED" 2.5M in 2 weeks; Kurzgesagt 10–20M on latest uploads | [C] | D2 |

### B2.3 Psychology and perception: findings and principles

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

### B2.4 Audits of real thumbnails: what the data show

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
| Tragedy handling | most show the structure or vehicle and no bodies; some state a casualty count as the hook; Storified is sensational ("IMPALED", "BRUTAL DEATH") yet has the biggest numbers on its channel (14M, 5.7M, 2.7M): sensationalism gets views but conflicts with the brief |

**The 13 formulas found in the niche** (full table with examples in D4): 1) two to four blunt heavy words over a full-bleed scene; 2) a worried face looking toward the hazard; 3) a giant one-word title over one lone object on plain sky or sea; 4) sepia or monochrome archive photo with gothic headline (photo-only); 5) red circle, arrow or dashed line (overused; banned by the brief); 6) cutaway or cross-section (translates well); 7) a tiny person for scale against something huge, or the moment just before; 8) a number as the hook; 9) gory dramatization with red arrows (avoid); 10) vehicle cut-out on a blue gradient with fire clip-art; 11) one object on plain light background with an accusatory caption; 12) an emotive cartoon character in a full scene with 2–3 words (native to your style); 13) "small thing, big outcome" split.

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
| No source compares stick or cartoon thumbnails with realistic ones on clicks | evidence either way is absent |

### B2.5 Design system numbers

| Fact | Value | Where |
|---|---|---|
| Palette lightness tiers (L*) | light: white 100, paper 93, sky 88, amber 75, tan 75, light green 72; mid: red 52, brown 49, dark green 48; dark: ink 9 | D6 |
| Rule of thumb | gap ≥ 50 text-safe (WCAG 4.5:1); 40–50 big bold text; 25–40 big flat shapes with an outline; < 25 invisible (hue only) | D6 |
| Universal outline | ink is at least 3:1 against every palette color (lowest: ink/dark green 3.59) | D6 |
| Strong pairs | ink/white 17.4:1; ink/paper 14.6; ink/sky 12.7; ink/amber 8.95; ink/light green 8.1; white/dark green 4.85; white/brown 4.6; white/red 4.2 | F1 |
| Weak or failing pairs | ink/red 4.1 (outline yes, ink text no); paper/red 3.5; red/sky 3.1 (best red accent background); sky/paper 1.15; white/paper 1.2; white/sky 1.37; tan/amber 1.01; light green/amber 1.11; light green/tan 1.09; dark green/brown 1.05; brown/red 1.09; dark green/red 1.15 | F1 |
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

### B2.6 Packaging, testing, cold start, Shorts

| Fact | Value | Grade | Where |
|---|---|---|---|
| Title and thumbnail as one unit | Galloway: "view the title and thumbnail as one … complement or contradict/repeat"; plan them before recording; pass the "glance test" | [B] | D8 |
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

### B2.7 The twelve candidate stories (fact base)

All twelve pass the channel's filter as of 2026-09-30 (not ongoing legal cases; nothing after 2024-09-30; no terrorism; no medical advice; politics only as regulatory facts). Full facts, quotes and sources are in D7 and G8. Ranked by thumbnail strength by the story-research agent (its judgment, not a test).

| Rank | Story | Headline facts | Thumbnail moment | Planted object |
|---|---|---|---|---|
| 1 | Comet, 1954 | 35 died 10 Jan (Elba), 21 died 8 Apr (Naples); whole fuselage tested in a water tank; failure after 3,057 cycles (1,221 real plus 1,836 simulated; another source 3,060); about 70% of the Elba wreck recovered | an entire airliner in a purpose-built tank, flown thousands of times faster than real life | a bolt hole |
| 2 | Tacoma Narrows, 1940 | opened 1 July, fell 7 Nov; wind 42 mph measured 09:30; twisting began 10:03; roadway tilted up to 28 ft each side; a 600-ft section fell 11:02; cause "remains a mystery", torsional flutter primary explanation | the tilted roadway; lemon-chewing workmen | a lemon |
| 3 | Vajont, 1963 | 1,917 dead (Italian Civil Protection; counts 1,919–2,056); about 260 million m³ slide; wave about 250 m over the crest; 262 m dam stood; criminal case closed 1971; final civil settlement 23 June 1999 | dam intact with a wave over it; at noon workers saw the mountain moving; at 13:00 a 50 cm crack | gravel-on-a-plank model |
| 4 | Vasa, 1628 | sank after about 1,300 m; about 30 died; a stability test with 30 men stopped after three trips; four rulers found (two Swedish feet, two Amsterdam feet); raised 1961 | huge ship heeling with open gunports, a crowd on the shore | a wooden ruler |
| 5 | Challenger, 1986 | 11:38 liftoff, breakup at 73 s; air temperature 36°F, 15°F colder than any earlier launch; Thiokol advised against launching below 53°F; foot-long icicles; Feynman's ice-water demonstration 11 Feb 1986 | a glass of ice water and a clamped rubber ring | the O-ring |
| 6 | 2003 Blackout | about 50 million people; 61,800 MW; alarm and logging software failed shortly after 14:14 EDT; trees tripped lines from about 15:05 | a frozen screen and a sagging line near a tree | the frozen screen |
| 7 | Samsung Galaxy Note 7, 2016 | discontinued 10 Oct 2016; FAA and PHMSA flight ban 14 Oct; two different defects (original and replacement); lost revenue estimate $17bn or more [C] | the replacement phone failing again | the phone |
| 8 | Quebec Bridge, 1907 | 75 of 86 workers died, 33 of them Mohawk ironworkers; about 15 seconds; span 549 m; bent chords noticed for weeks; second collapse 1916 (13 died) [C] | a visibly bowed chord while work continued | the bowed chord |
| 9 | Big Dig ceiling, 2006 | 10 July 11:01 pm; about 26 tons fell; 1 death; epoxy with poor creep resistance; anchor movement seen in 1999 | a bolt sliding out of a glued hole over years | an epoxy anchor |
| 10 | Hyatt Regency, 1981 | 17 July about 7:05 pm; 113 dead, 186 injured (NBS; others 114/216); the as-built change "essentially doubled" the load; at collapse 31% of code capacity; even the original design about 60% | one long rod vs two rods through a box beam | the nut and washer |
| 11 | Piper Alpha, 1988 | 226 aboard, 167 dead including 2 rescuers, 61 survived; pump's safety valve removed and a blind flange "hand-tightened only"; permits in different boxes; fire pumps on manual since 19:00 [C] | a steel disc fitted out of sight, two paper permits | the blind flange |
| 12 | Flixborough, 1974 | 1 June 16:53; 28 killed, 36 injured on site, 53 off site; a 20-inch bypass after reactor 5 cracked 27 March; no drawing, no calculations for the dog-leg or bellows, no pressure test; cause of failure contested | a dog-legged pipe with bellows and a gap where reactor 5 had been | the bellows |

**Dropped by the legal filter:** Morandi Bridge (verdict 16 July 2026, appeal announced), Boeing 737 MAX (civil trials continue, a jury verdict May 2026), Grenfell (charging decisions pending, trials 2029 or later). **Borderline, not used:** Lac-Mégantic. **Not verified in this pass (reserves):** Chernobyl, Three Mile Island, Apollo 13, Columbia, Mars Climate Orbiter, Millennium Bridge, St. Francis Dam, Sleipner A, Ronan Point, Tay Bridge, Kaprun, Sampoong, Banqiao, Therac-25, and the Titan submersible and Baltimore Key Bridge (recent, with legal matters).

*For detail see Part D (final reports), Appendix G (raw notes) and Part F (data tables).*
