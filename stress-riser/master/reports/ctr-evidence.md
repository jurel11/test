# CTR EVIDENCE REPORT (Stress Riser). Research date 2026-09-30

Notes file with URLs and quotes: `/tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/ctr-evidence/notes.md`. Contact sheets: `thumbs/ink_grid.jpg` and `thumbs/animated_sheet.jpg` in the same folder.

Grades: [A] official documentation, peer-reviewed or large dataset. [B] first-hand creator or company data. [C] opinion or anecdote.

## Bottom line
1. **No public, controlled dataset of CTR by thumbnail feature exists.** YouTube's own A/B tool reports watch-time share, not CTR. Nearly all "rules" rest on outcome-selected samples of already-viral videos, which show correlation only. Treat the confident percentages in SEO blogs as folklore.
2. **The evidence that survives scrutiny points one way.** Thumbnails should be simple and legible at phone size, with one dominant subject and few or no words. They should be bright, carry a readable emotion, and promise something the video actually delivers.
3. **Effects of single tweaks are small.** MrBeast's team reported a "small difference" that was consistent across 30 videos. Big gains come from a different concept or packaging, not from polish.

## Key findings

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

## Verdict table
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

## Illustrated/cartoon and educational niches
- No controlled data on illustrated vs photographic thumbnails exists. Only existence proofs [C].
  - Ink Explainer: faceless stick-figure channel, 77.8K subscribers, one video at 9.7M views in about a month.
  - The Infographics Show: a panicked cartoon controller thumbnail, "AMERICA CLOSED", 2.5M views in 2 weeks.
  - Kurzgesagt: no faces, 10-20M views on its latest uploads.
- The shared traits, descriptive only: one dominant subject, 1 to 3 caps words, saturated color, high figure-ground contrast.
- OverSimplified and Historia Civilis have older videos, so their views are cumulative and not comparable.
- Educational content has lower median views than entertainment (1of10, about -44%) and needs a curiosity hook without misleading. Derek Muller, YouTube and MrBeast's memo agree on delivery of the promise.
- MrBeast entertainment tactics (extreme concept, wide-open faces) are not what educational breakouts show: vidIQ found only about 5% shocked faces.

## What this means for Stress Riser
- **Subject and legibility.** One large stick-figure face (round head, dot eyes and brows read at small size) against one clear disaster object. Keep it to 3 characters or fewer and test at about 120 px width. Use a specific emotion such as dread or realization, not a generic scream. Test a subtle or closed-mouth variant against an open-mouth one.
- **Text.** Use none, or 1 to 3 words under 10 characters that add a fact the title lacks, rather than repeating the title. The brief bans text in scene art, so any thumbnail text would be composited separately. That is a decision for you.
- **Color.** Lean bright with high figure-ground contrast. Your palette's sky blue `#bfe2ea` and yellow `#e6b23a` fit 1of10's cyan and yellow/orange signals. Avoid dark frames.
- **Promise and delivery.** Show the real outcome, which the outcome-first opening pays off in seconds. YouTube's retention report flags when the first 30 seconds fail to match the thumbnail and title.
- **Question titles.** Question titles are neutral in data (OverseerOS matched pairs), so keep them for brand fit, not as a CTR lever.
- **Shorts.** About 99.9% of Shorts views come from the Shorts feed (ppc.land; original not verified), where no thumbnail shows. Custom Shorts thumbnails only began rolling out 2026-07-25, with no A/B testing. Thumbnail work matters mainly for long-form.
- **Testing your 10 styles.** Use Test & Compare on long-form. Make styles clearly different, since small tweaks yield "Performed Same". Judge on watch-time share, not CTR alone.

## Sources
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

## Caveats
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
