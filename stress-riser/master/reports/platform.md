# Platform mechanics, specs, policies and testing: report for Stress Riser thumbnails

Notes with full quotes and URLs: `/tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/platform/notes.md`. Raw pages are saved in the same folder.

Every YouTube Help page below was fetched raw with curl on 2026-09-30. Grades: [A] official, [B] first-hand or reported by a creator or company, [C] opinion.

## 1. Specs and display

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

## 2. Impressions, CTR, packaging, clickbait

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

## 3. Test & Compare (A/B)

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

## 4. Policies for disaster thumbnails

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

## 5. AI and disclosure

- **Cartoon animation [A] (Help 14328491):** disclosure is required only for realistic content. It lists as not needing disclosure "non-realistic content," an "AI-generated or altered animation of a missile in a fully animated video," "Cloning one's own voice to create voice overs," and "generative AI tools to create or improve a video outline, script, thumbnail, title, or infographic." A realistic depiction of a disaster that did not happen does need it.
- **Labels:** the May 27, 2026 update [A/B] puts labels for photorealistic AI content below the player. Animated or unrealistic content gets a label in the expanded description only (TechCrunch). The rules do not label thumbnails separately.
- **Auto-labels:** labels are added automatically for content made with YouTube's own AI tools, content with C2PA metadata, or content YouTube's systems detect as AI. Whether C2PA metadata embedded in a generated thumbnail triggers a label is UNVERIFIED.
- **Description line:** the channel's description line "This video uses AI-assisted narration and animation" is consistent with all of this.
- **Ask Studio caveat:** ppc.land says YouTube has not addressed whether Ask Studio-generated thumbnails fall under the disclosure rules. UNVERIFIED.

## Hard-constraint checklist for every Stress Riser thumbnail

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

## Caveats

- I could not read Creator Insider transcripts, because watch pages are bot-gated and I did not try to bypass that. The Beaupré interview, the Shorts 2:3 remark and the dynamic-thumbnails details come via ppc.land, SEJ and TechCrunch, so they are secondary [B/C].
- I found no official phone, TV or suggested-video pixel sizes and no official safe-zone geometry.
- The blog post on AI-label placement was partly truncated when fetched. I corroborated it with TechCrunch.
- I found no source on the Test & Compare statistical thresholds or on segment formation for dynamic thumbnails.

## Sources

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