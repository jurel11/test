# Stress Riser — 10 thumbnail styles

Research date: 2026-09-30. Eight research agents read official YouTube documentation, peer-reviewed studies, creator data, and looked at real thumbnails (about 105 visually classified in the engineering-disaster niche and about 300 in cartoon channels, out of 800+ downloaded). Their full notes, with every URL, are in `research/`. Ten vector mockups are in `thumbnails/` (open `thumbnail-lookbook.html` to see them side by side).

**Read this first: what the evidence can and cannot tell you.**
No public, controlled dataset links thumbnail features to click-through rate (CTR). YouTube's own A/B tool optimizes watch-time share, not CTR. Almost every "rule" online rests on samples of videos that already went viral, which shows what winners look like, not what caused the clicks. No study tests cartoon or stick-figure thumbnails against realistic ones. So the ten styles below are **hypotheses built on the best evidence available, designed to be tested against each other**, not guaranteed winners. Each claim carries an evidence grade: **[A]** official documentation, peer-reviewed or large dataset; **[B]** first-hand data from a creator or company, or a correlational dataset; **[C]** opinion, vendor blog, or my own inference.

---

## 1. The short version

- **Why this set should stand out.** The engineering-disaster niche is photographic, dark and text-heavy (268 direct-niche thumbnails: average brightness 0.43 on a 0–1 scale, versus 0.52 for cartoon channels). Among the channels checked, almost nobody in the disaster niche uses flat hand-drawn illustration for thumbnails (the closest are the Infographics Show's flat vector and Storified's stylized 3D). And almost nobody shows the moment *before* the failure, which is your whole angle (a chain of small decisions). Whether standing out lifts CTR is untested.
- **What the evidence supports.** One dominant subject, at most three people, a readable emotion, 0–3 words, a bright picture with strong figure-ground contrast, and a promise the video keeps by second 15.
- **What is contested or a myth.** Faces always win (contested). Shocked open-mouth faces (leaning myth: only about 5% of vidIQ's breakout videos use one). Exact word counts like "3 words" (convention, no study). "Red wins" (1of10 found cyan, green and yellow/orange ahead). Numbers such as "+38% from consistency" (untraceable).
- **The test rule.** Small tweaks cannot be detected on a small channel: a jump from 4% to 5% CTR needs about 6,700 impressions per variant, while 4% to 8% needs about 550. So test **radically different concepts** (these ten styles), never font or color tweaks.
- **What fits almost any story.** Styles 2 (Moment Before), 10 (Close-Up Gaze) and 1 (Tiny Under the Giant). Styles 3, 6 and 8 need a special true image, number or contrast in the story.
- **Four decisions I need from you**, in section 9. The biggest: the brief bans text inside images, yet every high-view thumbnail in the niche carries 2–4 words. I assume the words are a separate overlay added in your design tool, never inside the generated image.

---

## 2. Hard constraints (every thumbnail must pass)

From YouTube's own documentation [A] unless marked. Full sources in `research/platform.md` and `research/design-system.md`.

1. **Format.** 16:9, JPG or PNG. Official recommendation 3840×2160, minimum width 640 px. The old "1280×720" advice is out of date on the official page. YouTube serves thumbnails at 1280×720 (measured on YouTube's own responses, 2026-09-30). Upload limit: 2 MB from a phone, 50 MB from desktop (changed Oct 2025 [B]). My mockups are 1280×720 PNG-24 and about 100 KB each.
2. **Testing.** Every variant must be at least 1280×720, or **all** variants are downscaled to 480p. Up to 3 variants. Long-form only, desktop Studio only. The winner is chosen by **watch-time share**, not CTR.
3. **Where things sit.** Duration badge bottom-right and a red progress bar along the bottom edge for watched videos. Keep **230×90 px free at bottom-right** and about **110×110 px free at top-right** on the 1280×720 master (the exact geometry is not official; the badge box is derived from a [C] source, the top-right size is unverified). Margins: 64 px left and right, 36 px top and bottom. YouTube is running an experiment that may crop thumbnails on mobile Home (Team YouTube post, 2026-04-29), so keep everything important central.
4. **Impressions count** only if the thumbnail is on screen for more than 1 second with at least 50% visible, and not on the mobile website, embeds, or email.
5. **Policy.** Never a thumbnail that "misleads viewers to think they're about to view something that's not in the video" (strike risk). No "violent imagery that intends to shock or disgust", no blood or gore. Advertiser-friendly rules apply to the thumbnail too: disaster footage with visible harm to people gets limited ads; content that "profits from or exploits" a sensitive event gets none. YouTube treats clearly animated depictions differently from live action. Your rules (no injuries, no victims, no mockery) already fit.
6. **AI disclosure.** Not required for clearly non-realistic animation, and the rules list AI use for a thumbnail among things that do not need disclosure. A realistic depiction of an event that did not happen would need it, which is another reason to stay flat and cartoonish.
7. **Originality.** YouTube's monetization policy lists "AI-generated content made with generic or unoriginal templates" as not monetizable and checks thumbnails. A house style is fine; keep each thumbnail specific to its story.

---

## 3. What the research found (condensed)

| Finding | Grade | Source (details in `research/`) |
|---|---|---|
| Face vs no face performs about the same overall; faces help mainly channels above 200K subscribers; multiple faces beat a single face in that sample | [B] correlational, 300K+ videos of 2025 | 1of10 (2026-02-06) |
| Thumbnails with text got about 19% fewer views; best were no text, or under 10 characters covering under 7% of the image | [B] correlational | 1of10 |
| Cyan (+36%), green and yellow/orange do well; dark thumbnails underperform | [B] correlational | 1of10 |
| Among 500 breakout videos: face 69%, high contrast 56%, overlay text 72% (median 5 words), exaggerated expression about 5%. No base rate, so convention not cause | [B] | vidIQ 2026 |
| Netflix artwork tests: complex emotion beats stoic faces; win rates dropped sharply above 3 people | [B] company data, films not YouTube | Netflix, "The Power of a Picture" |
| Closing the mouth in thumbnails raised watch time in 30 of 30 videos, "a small difference" | [B] | MrBeast's thumbnail lead |
| Strong sentiment in the thumbnail raises views (16,215 covers); visual complexity has an inverted-U relationship with popularity | [A] observational (Fang's platform not verified as YouTube) | Cui 2024; Fang 2026 |
| Curiosity peaks with a **medium** information gap, not a maximal one | [A] | Kang 2009; Le Quéré & Matias 2025 (8,977 headline tests); Frede 2026 |
| Question-framed **headlines** reduced engagement on average (news headlines, not YouTube) | [A] | Fang & Wheeler 2026 |
| Question vs statement **titles** on 891 matched million-view pairs: no difference | [C] | OverseerOS |
| A figure looking at the object (not at the viewer) shifts attention to that object and raises recall | [A] | Sajjacholapunt & Ball 2014 (n=72) |
| More cartoonised faces let people identify emotion more accurately at short exposures | [A] | Kendall 2016 |
| Google's own ranking paper: ranking by CTR alone "promotes deceptive videos (clickbait)", so it uses expected watch time | [A] | Covington et al., RecSys 2016 |
| CTR: half of all channels sit between 2% and 10%; CTR naturally falls as reach widens | [A] | YouTube Help 7628154 |

**Myths and unsupported claims** (all researched, none traceable to a primary source): "3 words is optimal"; "faces give 2.3× CTR"; "eye contact adds 20%"; "median +32.7% uplift from A/B testing"; "80% brand recognition from color"; "13 ms to stop the scroll" (a lab picture-detection result, not a feed effect); "99.9% of Shorts views come from the feed" (a creator's remark, misattributed online); "38% higher CTR from a consistent template" and the "70/30 rule" (no method); the rule of thirds and the F-pattern for single-subject phone thumbnails (unsupported).

---

## 4. The house system: what never changes and what varies

Ten different concepts still have to look like one channel. Fixed anchors (from the design research, `research/design-system.md`):

1. **The 10-color palette only.**
2. **Ink outline** #1a1a1a on every shape: about 12–16 px on the 1280×720 master.
3. **The stick figure exactly as on the character sheet** (round white head, two dot eyes, line brows and mouth, small white body, single-line limbs, one prop). When the face carries the emotion, the head is at least about 150 px across. *There is no character sheet yet: make one per channel (front, side, three expressions, prop) and attach it to every generation.*
4. **One accent, and it always means "the thing that failed".** Red #d94a38 marks the culprit: the slid slope, the nut, the bolt, the bowed beam, the power line, the dog-leg pipe. It is 3–8% of the frame area. Amber #e6b23a appears **only on ink-black scenes** (a desk lamp), because it is weak against every other palette color. Red and amber never touch. This rule is my recommendation and matches the brief's "the part that matters may be in its colour with the rest pale".
5. **Text:** Lilita One (free, OFL), white fill, ink outline drawn outside the letters at 12% of cap height, 1–3 caps words, at most about 16 characters per line, at most 2 lines.
6. **Flat color with gentle cel shading.** No gradients.
7. **The safe zones above.**

Variables per video: composition, hero object, background family, emotion, text position, word count, camera distance, cutaway or not. Vary about four of these each time and alternate the background family between consecutive uploads so the feed alternates too.

**Color math** (my computations, `research/design-system.md`). The palette has only three lightness tiers: **light** (white, paper, sky, amber, tan, light green), **mid** (red, brown, dark green) and **dark** (ink). Colors inside one tier cannot be told apart by lightness, in grayscale or with color-blindness. Rules I used:

- Lightness gap (L*) of 50 or more is safe for text; 40–50 for big bold text; 25–40 for big flat shapes with an outline; under 25 is invisible.
- **Ink** works as text on every light color and as the outline everywhere (at least 3:1 against every palette color).
- **White or paper text needs the ink outline** on sky, paper, amber, tan and light green. Never use red, brown or green as a text fill.
- **Fail pairs:** sky/paper, white/paper, white/sky, tan/amber, light green/amber, light green/tan, dark green/brown, brown/red, dark green/red (red and green also merge for red-green color-blind viewers: red turns olive).
- **Pale thumbnails on the white feed lose their edge.** Sky, paper and white against the #ffffff page score as little as 1.15–1.37:1. Keep a mid or dark band along the image edges. In dark mode the feed is #0f0f0f, so give ink-black scenes a mid-tone edge band (the mockups use brown).

---

## 5. The ten styles

Mockups are vector drawings that show composition, color and text placement. They are **not final art**. Each example lists the story, a draft question title, and the overlay words. **All facts in the examples are in the registry in section 8.** All draft titles are questions with no colon, at most about 60 characters, with the hook in the first 40 (phones truncate long titles; real limits vary by device [C]). The thumbnail words always add something the title does not say.

Image files: `thumbnails/NN-*.png` (final composite), `thumbnails/art-only/NN-*-art.png` (the layer an image generator would produce: no words), `thumbnails/svg/` (editable).

**Master prompt block** (append to every image-generation prompt below; it is written in positive terms because image models often ignore "no text" instructions, so also check every output for stray letters):

> Hand-drawn flat cartoon illustration in the style of a modern animated explainer: clean black outlines of even weight, soft flat colors with gentle cel shading, warm natural light, 16:9 landscape, one dominant subject, simple bold shapes. Use only these colors: ink black #1a1a1a, white #ffffff, paper cream #f3ead8, sky blue #bfe2ea, light green #8fbf5a, dark green #4f7d3a, brown #9a6b43, tan #d2b48c, amber #e6b23a, red #d94a38. Any person is a stick figure exactly as on the attached character sheet: round white head with black outline, two dot eyes, simple line eyebrows and mouth, small white body, arms and legs as single thin black lines, no hands, feet or clothes. Every sign, gauge, screen and panel is blank and unmarked. A calm, quiet area is left free for a title.

---

### Style 1 — Tiny Under the Giant
*A huge structure or force fills the frame; one small figure looks at it. The culprit is the only red.*

- **Example:** Vajont Dam, 1963. Draft title: *Why did 1,900 people die under a dam that never broke?* Words: **THE MOUNTAIN**. Image: the pale mountain with a red slab sliding into the lake, a big wave over the still-standing dam, a small figure watching from the far ridge. Background family: light/mid.
- **Why it should work:** scale contrast is a real attention driver (a large object captures attention, Proulx 2010 [A]); "safe danger" is why people enjoy fear (Rozin 2013 [A]); it is proven in the niche: Practical Engineering "Why Are Beach Holes So Deadly?" (tiny figure in a huge trench, 7M views, 0kQXOTcEB_E) and in cartoon channels (Zenn "Why Hasn't Anyone Raised the Titanic?", 706K, IlCq6a0sDCk) [B]. "THE MOUNTAIN" completes the title instead of repeating it.
- **Layout:** structure at least 60% of the frame; figure 18–22% of frame height (figures under about 12% read only by posture, not by face); figure on a ridge or ledge, never below the harm; words top-left.
- **Watch out:** never place the figure where the victims were. The figure is the decider or observer.
- **Prompt:** *A tall concrete dam standing intact while a huge wave of dark green water arches over its top; on the left a pale tan mountain slope with a jagged red slab sliding into the reservoir and a white splash; a small stick figure stands on a green ridge on the far right looking at the scene with a worried face. Sky blue background with two clouds. The upper left is calm and empty.* + master block.
- **Also fits:** Banqiao, Sleipner, any dam or slope failure, Quebec Bridge, Titanic-type stories.

### Style 2 — The Moment Before
*The calm, ordinary scene just before the failure, with one wrong detail and a worried figure who has noticed it.*

- **Example:** Challenger, 1986. Draft title: *Why did a rubber ring destroy a space shuttle?* Words: **COLDEST LAUNCH**. Image: shuttle stack on a frosty pad, icicles on the tower, a small figure holding a thermometer, breathing a cold puff. Background family: light.
- **Why it should work:** this is the niche gap: nearly every disaster thumbnail shows the intact object, the fire or the wreckage; only two of the roughly 105 thumbnails inspected by eye came close to showing a cause or decision (Storified "26 PEOPLE", 613K, 0QXvhtPaKoY; Infographics Show's decisions video, 957K, vRAsU_ov84Q) [B]. Curiosity is strongest at a medium gap (Kang 2009; Le Quéré & Matias 2025 [A]); threat feels larger the nearer it is (Mobbs 2007 [A]). It is also your unique angle drawn as a picture.
- **Layout:** the whole intact structure plus one detail that is off (icicles, a tilted deck, a gauge in the red); figure 12–18% of frame height, looking at the detail; words in the empty sky.
- **Watch out:** the "wrong detail" must be visible at 168 px, and everything shown must be in the video by second 15.
- **Prompt:** *A space shuttle stack standing on a launch pad at dawn, frost on the ground, long icicles hanging from the brown service tower; in the foreground a small stick figure with a worried face looks up at the tower and holds a small thermometer with a red column; a tiny white cloud of breath in front of the mouth. Sky blue background, cream frosty ground.* + master block.
- **Also fits:** Tacoma (the deck starting to lift), Quebec (a bending chord), Hyatt, Vasa at the quay.

### Style 3 — The Impossible Scene
*A scene that looks absurd but is true, at human scale, with no words needed.*

- **Example:** de Havilland Comet, 1954. Draft title: *Why did engineers put a jet airliner in a water tank?* Words: **none** (a two-word option, **TANK TEST**, is documented but not needed). Image: an entire airliner with rounded windows and a red tail fin inside a large water tank, two calm engineers on the rim. Background family: mid (brown hall).
- **Why it should work:** the most extreme "zero-text anomaly" pattern: Veritasium "Why Are 96,000,000 Black Balls on This Reservoir?" (112M, uxPdPpi5W4o) and Mark Rober's jello pool (223M) show the image *is* the hook [B]; 1of10's best-performing text setup is no text [B]. Muller's "legitbait": the image hints at the real content [B, secondary]. The Comet agent's own ranking put this story first for thumbnail strength (no graphic risk, unique picture, busts the "square windows" myth).
- **Layout:** the bright water window is the focal point in a mid-tone frame; hero 60% of frame width; figures small and calm.
- **Watch out:** only use it when the true image exists; never invent an odd picture. Draw **rounded** windows: the "square windows" explanation is a myth (the failure began at a bolt hole near a roof antenna cut-out).
- **Prompt:** *A large rectangular water tank in a brown workshop hall, inside it a complete white jet airliner with a row of small rounded windows and a red tail fin, underwater with a few bubbles; two calm stick figures stand on the tank rim, one holds a clipboard. Sky blue water, tan tank walls, brown wall, three small windows high on the wall.* + master block.
- **Also fits:** Vasa raised from the seabed, Sleipner, "nothing broke but it failed" cases.

### Style 4 — Object on Trial
*One small part, drawn enormous, alone on a dark background. The part is the only red.*

- **Example:** Hyatt Regency walkways, 1981. Draft title: *Why did one small change bring down two hotel walkways?* Words: **LOAD DOUBLED**. Image: a giant nut and washer under a steel box beam with cracks starting, a rod above and below. Background family: dark (ink).
- **Why it should work:** one dominant subject (Pieters & Wedel 2004 [A]; Netflix win rates drop as scenes get more complex [B]); the niche's "lone object on a plain field" formula does well (Brick Immortar "El Faro", 4.8M, -BNDub3h2_I) [B]. It fits a channel about small decisions with huge consequences.
- **Layout:** hero 30–40% of the frame, off-center; words top-left in white on ink (maximum contrast).
- **Watch out:** **dark thumbnails underperform in 1of10's data** [B], so this is the riskiest color choice: test it against a light-tier style. The drawing is generic; check the connection detail against the NBS report before final art. The dark mockup will fade into a dark-mode feed without the edge band.
- **Prompt:** *A giant red hexagonal nut with a white round washer pressed against the underside of a cream steel box beam, thin red cracks starting at the washer edges, a tan steel rod passing through from above and continuing below, plain ink-black background.* + master block.
- **Also fits:** Challenger's O-ring, Flixborough's bellows, Comet's bolt hole, Big Dig's bolt.

### Style 5 — The Cutaway
*A see-through cross-section of the part no camera ever recorded.*

- **Example:** Big Dig ceiling, 2006. Draft title: *Why did a Boston tunnel ceiling fall after glue let go?* Words: **26 TONS**. Image: a cutaway of the roof slab with an epoxy-filled hole, the red bolt sliding out, a heavy panel hanging from it, a small worried figure below. Background family: mid (brown earth over dark tunnel).
- **Why it should work:** cutaways are common among the best-performing engineering videos (Jared Owen "What's inside the Titanic?", 22M, HLrBUwNSEo0; Sabin Civil "Golden Gate", 19M, E6tp8DCAJ-0) [B], and a cartoon precedent exists (Ink Explainer's mammoth-carcass cutaway, 756K, dp3jYZXKOos) [B]. It delivers your promise, "what no camera ever recorded", and your brief explicitly allows a see-through cutaway.
- **Layout:** the cutaway is the frame's center band; the red part is 2× larger than feels natural; words on the earth band.
- **Watch out:** this was **the weakest style at phone size** in my test (at 168 px the bolt is small), so it needs the enlarged hero and probably words. It is the hardest style to draw correctly.
- **Prompt:** *A cross-section cutaway of a tan concrete roof slab with speckles, showing a white epoxy-filled hole with a thick red threaded bolt that has slipped down leaving an ink-black gap above it; below, an ink-black tunnel with a large cream ceiling panel hanging from the bolt and a small worried stick figure standing on the road. Brown earth above the slab.* + master block.
- **Also fits:** Comet fatigue crack, Challenger joint, Tacoma cable clamp, Flixborough bellows.

### Style 6 — The Giant Number
*One figure, huge, is the hook. The number is in the words layer, not the picture.*

- **Example:** Tacoma Narrows, 1940. Draft title: *Why did a four-month-old bridge twist itself apart?* Words: **42 MPH** (cap height about 300 px, unit line about 130 px). Image: the undulating deck with red center line and a red windsock blowing flat, a small figure on the shore. Background family: light/mid.
- **Why it should work:** it survived every phone-size test (light, dark, grayscale, blur) with the number still legible at 168 px. Numbers as the hook are common in the niche (Dark Records "1,500 TONS OF TNT", 4.8M, NgQ7jh9mrWs; Sabin Civil "27000!", 19M; Banqiao "62 DAMS GONE", 358K, CFnh54FeNo0) [B] and in cartoon channels (Explain In Paint "-58°F?", 398K, Q3_htAFS7wg) [B]. 1of10 found that numbers in **titles** cost about 11% of views [B]: keep the number in the thumbnail and out of the title (the title and the picture then complement each other).
- **Layout:** the number takes the left 40%, cap height 300 px; picture on the right; nothing in the bottom-right zone.
- **Watch out:** pick a number that is surprising and **not** a death toll. Casualty counts as hooks ("161 PEOPLE") exist in the niche but conflict with your "state casualties factually and move on". "42 mph" is a gale, not a hurricane: never write "light wind".
- **Prompt:** *A suspension bridge with two tall brown towers, thin cables and vertical hangers, the roadway rippling in a wave with a thin red center line, a red pennant on a tower blowing sideways; green hills, dark green water, a small worried stick figure with hands on head on the near shore. Sky blue background with two clouds; the left 40% of the frame is calm and empty.* + master block.
- **Also fits:** Blackout ("50 MILLION"), Challenger ("36°F"), Banqiao, Kaprun-type stories (with a non-casualty number).

### Style 7 — The Diptych (small cause, big effect)
*Two single-idea images side by side: the tiny thing, then what it did. The tiny thing is red.*

- **Example:** Quebec Bridge, 1907. Draft title: *Why did they keep building a bridge that was bending?* Words: **none**. Left: the red bowed steel chord with a small inspector. Right: the collapsed span in the river, pale. Background family: light (needs the divider).
- **Why it should work:** split panels are among the top cartoon formulas (JarToon, 7.7M, L698u3f92eE; ClipperFlipper Titanic vs iceberg, 4.6M, tMvpB6cBjYk; Infographics Show "Small Thing, Big Outcome", 957K, vRAsU_ov84Q) [B], and it is the closest visual translation of "a chain of small decisions".
- **Layout:** 50/50 with a 20 px ink divider; the left panel carries the red; nothing in the bottom-right corner.
- **Watch out:** **needs your approval**. The brief bans "collage" and "multiple panels" in images. I built it as two separate single-panel images composited in your design tool. Its Quebec facts are lower-confidence (secondary sources): check the Royal Commission report before use. Weak at phone size in my first pass; I enlarged the wreck and figure and re-tested.
- **Prompt (left):** *Close-up of a thick steel column bowed into a curve, painted red with tan lacing plates, a small worried stick figure inspector pointing at it from the ground, sky blue background, green ground.* **(right):** *A steel bridge span broken into a river, a standing brown pier on the bank, pale tan trusses collapsed into dark green water with white splashes, sky blue background.* + master block.
- **Also fits:** Hyatt (one rod vs two rods), Challenger (a rubber ring vs the whole stack), Piper Alpha.

### Style 8 — Nobody Notices
*The viewer sees the flaw that the calm crowd does not.*

- **Example:** Vasa, 1628. Draft title: *Why did a brand-new warship sink in front of its own crowd?* Words: **LIGHT BREEZE**. Image: the big ship heeling, lowest gunports open (red), three calm figures waving on the shore. Background family: mid/light.
- **Why it should work:** dramatic irony is the brief's core promise ("the viewer sees how they would have made the same call"). Storified's bus-heading-to-a-broken-bridge thumbnail is a close cousin (613K, 0QXvhtPaKoY) [B]. Three figures respect the Netflix ≤3-people finding.
- **Layout:** the tilted ship is the diagonal; the crowd is small and cheerful (waving arms, flat mouths: no smile unless the picture asks for one); words in the sky.
- **Watch out:** the flaw must be big and obvious (the heel), or the style fails. "Light breeze" comes from secondary sources: check the Vasa Museum before use. The stability failure and the open lower gunports are documented; anything about the rulers is only an inference.
- **Prompt:** *A tall wooden warship with three masts and cream square sails tilting sharply in dark green water, two rows of open gunports on the brown hull with the lowest row red, a curved raised stern; on the left shore three calm stick figures wave their thin arms. Sky blue background, two clouds, small cream waves.* + master block.
- **Also fits:** Tacoma (drivers on the bridge), Hyatt atrium (empty, before), Titanic-type stories.

### Style 9 — Seat of the Decider
*The viewer sits where the decision was made and sees what the figure cannot.*

- **Example:** the 2003 Northeast Blackout. Draft title: *Why did a silent alarm black out 50 million people?* Words: **2:14 PM**. Image: a calm operator at a console with two blank screens and a lamp; through the window a power line (red) touches a tree. Background family: dark (ink) with a brown edge band and one amber lamp.
- **Why it should work:** it is the brief's speech pattern #1 (second person, the viewer in the seat) as a picture. None of the roughly 105 disaster-niche thumbnails inspected by eye showed a decision room. Cartoon channels use a dark scene with one figure and props (StickFigure Explains, 4.5M, Yh_7y2PYH1o; easy, actually, 9.7M, C5OJJD3Eytk) [B].
- **Layout:** the figure calm, looking at the screens; the cause visible only through the window; words top-left.
- **Watch out:** the character sheet has no side or back view: approve it. Dark tier, so the 1of10 brightness caution applies. The blank monitors should be replaced by something readable in final art (a frozen bar, an unlit lamp). The "phone ringing" in the brief's own example is not documented for this event: do not draw it.
- **Prompt:** *A dark control room seen from the side: a calm stick figure sits at a brown console desk in front of two large blank sky-blue monitors, a small amber desk lamp; on the right a window showing a green tree at dusk with a power line drooping onto it, the line in red. Ink-black room, thin brown border.* + master block.
- **Also fits:** Challenger's teleconference, Piper Alpha's control room, Big Dig's inspection office.

### Style 10 — Close-Up Gaze
*A huge worried face looks sideways at the hazard. The hazard is red.*

- **Example:** Flixborough, 1974. Draft title: *Why did a temporary pipe blow up a whole chemical plant?* Words: **NO DRAWING**. Image: a head filling the left of the frame, eyes shifted toward two tan reactors joined by a red dog-leg bypass. Background family: light/mid.
- **Why it should work:** it passed every phone-size test, including blur. The nearest real precedent: The Hydraulic Record puts the same worried presenter looking toward the hazard on every thumbnail (25K subscribers, 2M and 1M views on two recent videos; the Oroville example, mwwdnfaNKxk, has 132K) [B, causation unverified]. Netflix: complex emotion beats stoic [B]. A figure looking at the object shifts viewers' attention and recall to it (Sajjacholapunt & Ball 2014 [A]). Schematic faces still read emotion (Kendall 2016 [A]); only about 5% of vidIQ's breakout videos used an exaggerated expression [B], so use **worried, not a scream**.
- **Layout:** head at least 25% of the frame height (mockup: about 55%); eyes shifted 20% toward the hazard; brows angled up in the middle; hazard on the right third; words in the sky.
- **Watch out:** two-dot eyes with no eye whites are **untested** for fear signals (Whalen 2004 concerns real eye whites [A]); test a subtle version against an open-mouth one. Flixborough's cause is contested (HSE says the bypass failure "may have been caused by" a nearby pipe fire): the video must say so; "NO DRAWING" is the documented part.
- **Prompt:** *A single huge round white stick-figure head filling the left third of the frame with a worried face, two black dot eyes shifted to the right, eyebrows angled up in the middle, small downturned mouth; on the right two tan chemical reactors joined by a thick red zig-zag pipe with cream flexible joints; green ground, sky blue background.* + master block.
- **Also fits:** any story with one visible defect: Quebec's bowed chord, Big Dig's bolt, Tacoma's cable.

---

## 6. Comparison and phone-size results

`thumbnails/qa-phone-sizes.png` shows each style at 360 px and 168 px on the light feed, 168 px on the dark feed, in grayscale and blurred. My reading (a visual check, not a human study):

| # | Style | Background | Words | Phone-size result | Fit to any story | Risk |
|---|---|---|---|---|---|---|
| 1 | Tiny Under the Giant | light/mid | 2 | good; the red slope and words read | high | medium (figure size) |
| 2 | The Moment Before | light | 2 | good | **high** | low |
| 3 | The Impossible Scene | mid | 0 | readable; small at 168 px | low (needs a true odd image) | low if true |
| 4 | Object on Trial | dark | 2 | good | medium | **dark-tier caution** |
| 5 | The Cutaway | mid | 1 | **weakest**; enlarged, still needs words | medium | drawing difficulty |
| 6 | The Giant Number | light/mid | 1 | **strongest**; the number survives the squint test | medium (needs a good number) | low |
| 7 | The Diptych | light | 0 | improved after enlargement; weakest without words | medium | **needs your approval** |
| 8 | Nobody Notices | mid/light | 2 | good | low-medium (needs a visible flaw) | medium |
| 9 | Seat of the Decider | dark | 1 | good | medium | dark tier, needs a side view |
| 10 | Close-Up Gaze | light/mid | 2 | **strongest**; survives blur | **high** | dot-eye fear untested |

**Suggested test trios** (never two styles from the same row of variables in one test): one *human* style (10 or 9), one *mechanism* style (4 or 5) and one *scale/scene* style (1 or 2). Alternate light-, mid- and dark-tier styles across consecutive videos.

**Style × story type** (my judgment, not tested):

| Story type | Best | Also good |
|---|---|---|
| Dam, flood, slope | 1 | 2, 6, 10 |
| Bridge (collapse, flutter) | 6, 2 | 1, 7, 10 |
| Building, walkway | 4, 7 | 2, 5 |
| Aircraft | 3, 5 | 10, 4 |
| Rocket, spacecraft | 2, 4 | 7, 9 |
| Plant, offshore, industrial | 10, 4 | 5, 9 |
| Tunnel, mine | 5, 2 | 10, 1 |
| Control system, software, blackout | 9, 6 | 2, 10 |
| Failed product, invention | 4, 10 | 7, 3 |
| "Nothing broke but it failed" | 8, 3 | 2, 7 |

---

## 7. Testing playbook

- **Use Test & Compare** on every long-form video: up to 3 variants, desktop Studio, winner by watch-time share, up to 2 weeks. Upload your preferred variant **first**: if the result is inconclusive, the first upload stays. Outcomes are Winner, Performed Same and Inconclusive, and "Performed Same" is common. Editing the title or thumbnail during a test stops it. Do **not** swap thumbnails by hand and compare: early viewers are your fans and the traffic-source mix distorts CTR.
- **Test concepts, not tweaks.** Sample size per variant for 80% power at 5% significance, CTR only (my arithmetic with the standard two-proportion formula; the real tool uses watch-time share, so treat as indicative): 4% → 8%: about 550; 4% → 6%: about 1,860; 4% → 5%: about 6,700; 4% → 4.8%: about 10,300. Three variants triple the total.
- **Cadence.** Run a test at publish (core audience), read it at 48–72 hours, and re-test older videos with a new concept if the topic is evergreen. Retesting at 72+ hours matches official guidance [A].
- **Log every video:** style, overlay words, CTR by traffic source, average view duration, test outcome. After 8–10 videos look for patterns across videos: single tests will rarely reach significance at small volumes.
- **Never judge CTR alone.** YouTube says clickbait shows as high CTR with low average view duration. If CTR rises and average view duration falls, the thumbnail over-promised.
- **Decision rules (my heuristics [C], not from a source):** do not touch anything for 48 hours; "Winner" means adopt it; "Performed Same" means keep your favorite and log it; "Inconclusive" means accept the default; consider a manual swap only if after about 5,000 impressions CTR is under 70% of your own same-source baseline and average view duration is healthy, and then change the whole concept.
- **Title–thumbnail pairing** (Galloway, Ritchie, the MrBeast memo, YouTube staff [B]): plan the title and thumbnail before recording. The thumbnail must add what the title does not, must not repeat its first ~40 characters, and everything it promises must be visible or explained by second 15 (your outcome-first opening already enforces this). Keep your question titles, but make them concrete (a named object or a number) so they do not read as vague; the evidence on questions is mixed and comes from headlines.
- **Per-thumbnail QA** (run `tools/thumb_preview.py`): 1) squint (blur): accent, main word and silhouette survive; 2) phone size: main word cap height at least 90 px on the master; 3) grayscale: word vs background lightness gap at least 50, figure vs background at least 25; 4) light and dark feed: image edges do not dissolve; 5) color-blind: red never on green or brown; 6) badge zone empty; 7) zoom to 100% and look for stray letters or numbers on signs, gauges and clocks, and for hands, shoes or thick limbs; 8) 3 words or fewer; 9) export sRGB, 16:9, under 2 MB.

---

## 8. Registry of facts used in the examples

Every fact shown in a mockup or title, with its source and the confidence of that source. The channel rule is "nothing invented": **re-verify each against the primary report before publishing.** Detailed quotes are in `research/story-visuals.md`.

| Story | Fact used | Primary source read? | Confidence |
|---|---|---|---|
| Vajont, 1963 | 1,917 dead (Italian Civil Protection), other counts 1,919–2,056, so "about 1,900"; the 262 m dam stayed standing; the slope slid, not the dam; the slide was about 260 million m³ (sources say 200–300 million) | secondary (ASDSO, Fondazione Vajont, Civil Protection) | [B] |
| Challenger, 1986 | Air temperature 36°F at launch, 15°F colder than any earlier launch; Thiokol engineers advised against launching below 53°F; foot-long icicles on the pad; the O-ring joint failed | **Rogers Commission Vol. 1 read** | [A] |
| Comet, 1954 | Whole fuselage tested in a water tank; failure at a bolt hole near a roof antenna cut-out, **not** the passenger windows (rounded rectangles); the Cohen inquiry report, 1 Feb 1955 | Withey 1997 paper and Aerossurance; official CAP 127 PDF not opened | [B/C] |
| Hyatt Regency, 1981 | Two sets of rods replaced one continuous rod, which "essentially doubled" the load on the fourth-floor connection; 113 dead | **NBS report read** | [A] |
| Big Dig, 2006 | About 26 tons fell on 10 July 2006 at 11:01 pm; cause: epoxy with poor creep resistance (anchor slowly let go) | **NTSB HAR-07/02 read** | [A] |
| Tacoma Narrows, 1940 | Opened 1 July, collapsed 7 Nov: four months; wind 42 mph; the exact cause of the flutter is still argued ("resonance" is a myth as the textbook explanation) | **WSDOT history read** | [A] |
| Quebec Bridge, 1907 | Bent lower chords were noticed for weeks before the collapse; no numbers used | Wikipedia-level; Royal Commission report not read | [C] |
| Vasa, 1628 | Heeled and sank on the maiden voyage after about 1,300 m; lower gunports open; wind described as a light breeze/gust | secondary; the museum page returned 404 | [C] |
| 2003 Blackout | About 50 million people; the utility's alarm system failed after 14:14 and stayed dead; operators "remained unaware"; overgrown trees tripped lines from 15:05 | **Task Force final report read** | [A] |
| Flixborough, 1974 | Temporary 20-inch bypass; HSE: no drawing, no calculations for the dog-leg or bellows, no pressure test; cause of failure contested | **HSE page read** | [A] |

**Dropped by the legal filter (searched 2026-09-30):** Morandi Bridge (verdict 16 July 2026, appeal announced), Boeing 737 MAX (civil trials continue), Grenfell (charging decisions pending, trials 2029 or later). Lac-Mégantic is borderline (sources conflict on the year of the Supreme Court decision): not used. Not verified this pass: Chernobyl, Three Mile Island, Apollo 13, Columbia, Mars Climate Orbiter, Millennium Bridge, St. Francis Dam, Sleipner, Ronan Point, Kaprun, Sampoong, Therac-25, and the Titan submersible and Baltimore Key Bridge (recent, with legal matters).

**Myths to avoid when drawing:** Comet's "square windows"; Tacoma's "resonance"; "a light wind" at Tacoma; the Vasa "king added a deck" story (no evidence); Quebec's "Iron Rings from the wreckage" (no support found); Piper Alpha blamed on the two workers named by the court.

---

## 9. Decisions I need from you

1. **Text on thumbnails.** The brief bans text inside images, but every high-view thumbnail in the niche (median 3–4 words, maximum 7) and in Ink Explainer's top videos carries 2–3 words. I assumed the words are a separate overlay layer in Figma, Canva or Photopea, never in the generated image; the `art-only/` files show the generated layer. Confirm, or tell me to make all ten wordless.
2. **The Diptych (Style 7).** Allowed to composite two single-panel images, given the "no collage or multiple panels" rule?
3. **The character sheet.** There is none in the brief. Ink Explainer's figures have circle eyes with lids; yours have dot eyes. Approve dot eyes with a *shift toward the hazard* for gaze, a *side view* for Style 9, and a *very large head* for Style 10.
4. **Numbers on thumbnails.** I used only non-casualty numbers (mph, tons, people affected by a blackout). Should a death toll ever appear as a hook, given "state casualties factually and move on"? I recommend no.

---

## 10. Shorts

- The Shorts feed plays the video without showing a thumbnail; covers appear on the channel page, in search and on the homepage [A/B]. A custom cover can only be set on a computer in Studio, is rolling out (Partner Program creators first; the Help page says "verified account": check which applies to your channel), and there is **no A/B testing for Shorts** [A].
- Covers are 9:16 (2160×3840). Keep everything important inside a central 2:3 crop [B]; the safe zone is what remains after cropping the top and bottom of the frame.
- The first-frame equivalent of a thumbnail is **frame 0 to 1 s**: the outcome image plus a 3–6 word line (matches the brief's "outcome within the first 3 seconds"). Styles that translate best to vertical: 6 (Giant Number), 10 (Close-Up Gaze), 4 (Object on Trial).
- "99.9% of Shorts views come from the feed" is a creator remark, misattributed online: do not rely on it.

---

## 11. Caveats

- No CTR or impression data exists outside your own Studio, so every "should work" is an inference from view counts, lab attention studies and headline experiments. Views depend on video age, topic and channel size: I compared only within a channel and only as patterns.
- Several sources could not be opened (YouTube watch pages and transcripts, vidIQ's study page, ScienceDirect, Springer, ACM). Those findings rest on abstracts or secondary reports and are marked as such in `research/`.
- Beaupré's and Ritchie's statements come through Search Engine Journal and ppc.land, not the original videos.
- The MrBeast production memo is unauthenticated.
- The saliency and OCR checks in the design report are proxies, not human studies. The duration-badge geometry is approximate. The mockups are vector art, not generated images: real generated images will differ, and you must check every one for stray letters and numbers.
- About 300 of the 405 niche thumbnails were measured programmatically but not visually inspected.

## 12. Files

- `thumbnail-lookbook.html`: all ten mockups, the phone-size test, and the comparison in one page.
- `thumbnails/`: the ten composites, `art-only/` layers, editable `svg/`, and `qa-phone-sizes.png`.
- `tools/thumb_preview.py`: feed preview rig (light and dark feed, several sizes, badge, grayscale, blur, safe zones). Usage: `python3 thumb_preview.py image.png --title "..." --duration 10:24 --safezone` (needs Pillow).
- `research/*.md`: the eight research agents' notes with URLs, quotes and evidence grades: `platform`, `ctr-evidence`, `psychology`, `niche-audit`, `cartoon-audit`, `design-system`, `packaging`, `story-visuals`.
