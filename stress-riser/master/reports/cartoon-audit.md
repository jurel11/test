# Cartoon / stick-figure explainer thumbnail audit: final report

Everything is in `/tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/cartoon-audit/`. Main files: `notes.md`, `index.csv`, `sheets/`, `ranksheets/`, `sheets/phone_test_176px.jpg`.
- `index.csv` has 462 thumbnail rows from 52 channels. About 35 of those channels are truly cartoon or illustrated. Views are YouTube's rounded strings scraped on 2026-09-30.
- I looked at the contact sheets, all-video rank sheets and one full-size montage. That covers roughly 300 of the 462 thumbnails, not all of them.
- I pulled Popular-sort lists through the YouTube browse API.
- "Weak" means the lowest-viewed of a channel's last 20 long-form uploads that are at least 21 days old.
- I excluded non-cartoon channels from the conclusions: Bobby Duke, Kaptain Kristian, Professor Of How, Yellow Dude, Fascinating Horror, Wendover, HowMoneyWorks.

## Key findings

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

## Top 12 formulas (channel, title, video ID, views as fetched)

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

## Identity and template
- The top performers keep one layout and change only scene, emotion and scale. Ink Explainer, Zenn, Axen and Explain In Paint all put text on top, the figure lower, and a full scene behind.
- OverSimplified, Sam O'Nella and Historia Civilis use rigid branded templates. Kurzgesagt varies composition but keeps a constant palette, outline and eyes.
- Palette pattern on the strongest thumbnails: saturated mid-tone sky or dark warm interior, a fire-orange accent, and yellow text with a heavy black outline. This is my observation, not a measured rule.

## Stick-figure face and pose vocabulary (from what I saw, [B]/[C])
- **Calm or chill:** eyes closed or half-lidded, tiny smile or flat mouth, reclined diagonal body, arm behind head (NO JOBS).
- **Tired or miserable:** half-lidded circle eyes with red rings, slumped shoulders (Ink Explainer "TRAVEL HOW?" and "RAINED ALL WEEK").
- **Worried:** wide circle eyes with tiny pupils looking sideways, wavy mouth, sweat drop (Ink Explainer "Why Us?", Zenn "THAT'S ME?").
- **Shock:** huge circle eyes, small centered pupils, open O mouth, hands on head (HUMAN-ISH "NO HOSPITAL?!").
- **Skeptical:** one flat brow, sideways glance.
- **Anger:** V-shaped brows and gritted teeth (Axen "NO SCHOOLS", StickFigure Explains "you're lazy").
- **Dread from scale:** a small, stiff figure whose gaze leads the eye to the huge object (Zenn "RAISE IT?").
- **Body language:** single-line arms and legs still read: a pointing arm, an X of crossed arms, a long lounging leg.
- **Sizing:** exaggerate the eyes (about a quarter of head width) and make the face at least about 25% of frame height when it is the hero. Mouth lines vanish at phone size. One prop, at least about 15% of frame, tied to the question.

## Mistakes to avoid
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

## Implications for Stress Riser
- Your pictures already match the Ink Explainer look: scene-filled, flat colors with black outlines, and lidded-eye stick figures. The thumbnail levers left are figure scale, 1-3 words of text, and one prop or object as hero.
- Strong candidates for your 10 distinct styles are formulas 1-4, 6, 7, 10 and 12, plus a disaster object-hero version of 3 (bridge, dam or ship) and a number-hero version of 5. Formulas 8, 9 and 11 are the weakest fits.
- Your brief forbids text and arrows inside scene images. Thumbnail text has to be a separate overlay layer. Check this with the user.

## Sources
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

## Caveats
- No CTR or impression data exists outside the channel owners. Every "what works" line is a pattern in view counts plus my visual coding, not causal.
- View strings are rounded, ages run from 3 days to 13 years, and top-versus-weak comparisons are confounded by topic and age. Old giants like Kurzgesagt and OverSimplified show what accumulated over years, not what a new channel can expect.
- Not verified: how these creators make their thumbnails (no interviews found), revenue figures, and the abstracts of the older schematic-face papers.
- A `rm` of the `thumbs/` folder was blocked by the safety check, so some stale weak-thumbnail files remain in it. I did not work around the block. `index.csv` references only the current files.