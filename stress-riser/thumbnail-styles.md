# Stress Riser — 10 thumbnail styles

Research date: 2026-09-30. Eight research agents read official YouTube documentation, peer-reviewed studies and creator data, and looked at real thumbnails (about 105 in the engineering-disaster niche and about 300 in cartoon channels were inspected by eye, out of 860+ downloaded). Their full notes, with every URL, are in `research/`. The first draft of this report and the mockups were then reviewed by two independent reviewers (one checked every claim against sources, one checked the brief, the palette and the design); this is the corrected version. A third reviewer later checked the master file built from this report (`STRESS-RISER-MASTER.html`); the corrections that touch this report are applied here too. Ten vector mockups are in `thumbnails/` (open `thumbnail-lookbook.html` to see them side by side).

**Read this first: what the evidence can and cannot tell you.**
The research found no controlled study of what makes YouTube thumbnails get clicked, and YouTube's own A/B tool optimizes watch-time share, not click-through rate (CTR). Almost every "rule" online rests on samples of videos that already went viral: it shows what winners look like, not what caused the clicks. Related lab and headline experiments exist, but none tests cartoon or stick-figure thumbnails on YouTube. So the ten styles below are **hypotheses built on the best evidence available, designed to be tested against each other**, not guaranteed winners. Each claim carries an evidence grade: **[A]** official documentation, peer-reviewed, or a large dataset; **[B]** first-hand data from a creator or company, or a correlational dataset; **[C]** opinion, vendor blog, or my own inference.

---

## 1. The short version

- **Why this set should stand out (untested).** The engineering-disaster niche is photographic, dark and text-heavy: across 268 direct-niche thumbnails the average brightness was 0.43 on a 0–1 scale (the figure for eight cartoon-style channels was 0.52). Among the channels checked, almost nobody in the disaster niche uses flat hand-drawn illustration (the closest are the Infographics Show's flat vector and Storified's stylized 3D). And almost nobody shows the moment *before* the failure, which is your whole angle. Whether standing out lifts CTR is unknown.
- **What the evidence supports.** One dominant subject; at most three people (Netflix's artwork tests); a readable emotion; few or no words; a promise the video keeps by second 15.
- **What is contested or unsupported.** *Faces always win*: contested (faces and no faces perform about the same in the largest dataset). *Shocked, open-mouth faces*: contested (only about 5% of vidIQ's breakout videos use an exaggerated expression, but that figure has no base rate; YouTube's own tips page recommends "a shocked face"). *Exact word counts*: convention, no study. *Red wins*: 1of10 found cyan, green and yellow/orange ahead. *Bright and saturated*: 1of10 supports it (winners only), but both of our audits found that brightness, saturation and clutter did **not** separate top from weak videos within a channel (coin-flip tallies: 12–19 of 32 channels, and 17–29 of 44). Treat brightness as a hypothesis.
- **The test rule.** Small tweaks cannot be detected on a small channel: 4% → 5% CTR needs about 6,700 impressions per variant, while 4% → 8% needs about 550. So test **radically different concepts** (these ten styles), never font or color tweaks.
- **What fits almost any story.** Styles 2 (Moment Before), 10 (Close-Up Gaze) and 1 (Tiny Under the Giant). Styles 3, 6, 7 and 8 need a special true image, number, odd detail or contrast in the story.
- **Four decisions I need from you** are in section 9. The biggest: the brief bans text inside images, yet about 70% of the thumbnails inspected in the niche (75 of about 105; median 3–4 words, maximum 7) carry words. I assume the words are a separate overlay added in your design tool, never inside the generated image.

---

## 2. Hard constraints (every thumbnail must pass)

From YouTube's own documentation [A] unless marked. Sources in `research/platform.md` and `research/design-system.md`.

1. **Format.** 16:9, JPG or PNG. Official recommendation 3840×2160, minimum width 640 px (the old "1280×720" advice is out of date on the official page). YouTube serves thumbnails at 1280×720 (measured on YouTube's own responses, 2026-09-30). Upload limit: 2 MB from a phone, 50 MB from desktop (announced Oct 2025 [B]). My mockups are 1280×720 PNG-24 at about 100 KB each.
2. **Testing.** Every variant must be at least 1280×720, or **all** variants are downscaled to 480p. Up to 3 variants; long-form only; desktop Studio only. The winner is chosen by **watch-time share**, not CTR.
3. **Where things sit.** The duration badge is bottom-right and watched videos show a red progress bar along the bottom edge. I keep **230×90 px free at bottom-right** and about **110×110 px free at top-right** of the 1280×720 master (neither box is official geometry: the badge box comes from a [C] source and the top-right size is unverified). Margins: 64 px on the sides, 36 px on top and bottom (outline included). YouTube is running an experiment that may crop thumbnails on mobile Home (Team YouTube post, 2026-04-29; the page is script-rendered, so a reviewer could not re-open it), so keep everything important central.
4. **Impressions count** only when the thumbnail is on screen for more than 1 second with at least 50% visible, and not on the mobile website, embeds or email.
5. **Policy.** Never a thumbnail that "misleads viewers to think they're about to view something that's not in the video" (strike risk). No "violent imagery that intends to shock or disgust", no blood or gore. Advertiser-friendly rules apply to the thumbnail too: disaster footage with visible harm to people gets limited ads; content that "profits from or exploits" a sensitive event gets none. YouTube treats clearly animated depictions differently from live action. Your rules (no injuries, no victims, no mockery) already fit. YouTube's performance FAQ also lists "Loud: ALL CAPS or !!!!!" among things to avoid: keep to one to three words, never use exclamation marks, and consider testing sentence case against caps.
6. **AI disclosure.** Not required for clearly non-realistic animation; YouTube's rules list "generative AI tools to create or improve a … thumbnail" among uses that do not need disclosure. A realistic depiction of an event that did not happen would need it, so stay flat and cartoonish.
7. **Originality.** YouTube's monetization policy lists "AI-generated content made with generic or unoriginal templates" among content that is not monetizable, and reviewers look at thumbnails. Its language about repetitive content is about "giving the impression of mass production without adding the creator's original, authentic insights or perspective". My reading, not YouTube's words: a house style is fine as long as each thumbnail is specific to its story.

---

## 3. What the research found (condensed)

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

---

## 4. The house system: what never changes and what varies

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

---

## 5. The ten styles

Mockups are vector drawings that show composition, color and text placement. They are **not final art**, and details are simplified (see each style's watch-out). Each example lists the story, a draft question title, and the overlay words. **All facts in the examples are in the registry in section 8.** Draft titles are questions with no colon, at most 60 characters, and the thumbnail words add something the title does not say. Phones truncate long titles (real limits vary by device [C]).

Files: `thumbnails/NN-*.png` (final composite), `thumbnails/art-only/NN-*-art.png` (the layer an image generator would produce: no words; styles 2 and 3 have no words so they have no separate file), `thumbnails/svg/` (editable).

**Master prompt block** (append to every image-generation prompt below). It is written in positive terms because image models often ignore "no text" instructions, so also check every output at 100% for stray letters and numbers:

> Hand-drawn flat cartoon illustration in the style of a modern animated explainer: clean black outlines of even weight, soft flat colors with gentle cel shading, warm natural light, 16:9 landscape, one dominant subject, simple bold shapes, a lit scene. Use only these colors: ink black #1a1a1a, white #ffffff, paper cream #f3ead8, sky blue #bfe2ea, light green #8fbf5a, dark green #4f7d3a, brown #9a6b43, tan #d2b48c, amber #e6b23a, red #d94a38. Any person is a stick figure exactly as on the attached character sheet: round white head with black outline, two dot eyes, simple line eyebrows and mouth, small white body, arms and legs as single thin black lines, no hands, feet or clothes. Every sign, gauge, screen and panel is blank and unmarked. A calm, quiet area is left free for a title.

---

### Style 1 — Tiny Under the Giant
*A huge structure or force fills the frame; one small figure watches. The culprit is the only red.*

- **Example:** Vajont Dam, 1963. Draft title: *Why did 1,900 people die under a dam that never broke?* Words: **THE MOUNTAIN**. Image: a pale mountain with a red slab sliding into the reservoir, a big wave over the still-standing thin dam, a small figure watching from the far ridge.
- **Why it should work:** scale contrast is a real attention driver (a large object captures attention, Proulx 2010 [A]); "safe danger" is why people enjoy fear (Rozin 2013 [A]). Similar images are seen among high-view videos: Practical Engineering "Why Are Beach Holes So Deadly?" (tiny figure in a huge trench, 7M views, 0kQXOTcEB_E) and Zenn "Why Hasn't Anyone Raised the Titanic?" (706K, IlCq6a0sDCk) [B; a correlation, with no CTR data]. "THE MOUNTAIN" completes the title instead of repeating it.
- **Layout:** the structure and wave take most of the frame; the figure is about 18–22% of the frame height (figures under about 12% read only by posture, not by face); the figure stands on a ridge, never below the harm; words top-left.
- **Watch out:** never place the figure where victims were. The dam in the mockup is drawn thin and tall (Vajont is an arch dam); check the profile against a reliable drawing before final art.
- **Prompt:** *A tall thin concrete dam standing intact while a huge wave of dark green water arches over its top; on the left a pale tan mountain slope with a jagged red slab sliding into the reservoir and a white splash; a small stick figure stands on a brown ridge on the far right looking at the scene with a worried face. Sky blue background with two clouds. The upper left is calm and empty.* + master block.
- **Also fits:** Banqiao, Sleipner, any dam or slope failure, Titanic-type stories.

### Style 2 — The Moment Before
*The calm scene just before the failure, with one wrong thing in the middle of the frame and a worried figure who has noticed.*

- **Example:** Quebec Bridge, 1907. Draft title: *Why did engineers keep building a bending bridge?* Words: **none**. Image: a half-built cantilever truss stopping in mid-air, its red lower chord visibly bowed, a small inspector pointing up from the bank. The Quebec facts are low-confidence: see the registry.
- **Why it should work:** this is the niche gap: only two of the roughly 105 thumbnails inspected by eye came close to showing a cause or decision (Storified "26 PEOPLE", 613K, 0QXvhtPaKoY; Infographics Show's decisions video, 957K, vRAsU_ov84Q) [B]. Curiosity is strongest at a medium gap (Kang 2009; Le Quéré & Matias 2025 [A]). Mobbs 2007 (threat feels larger when nearer) is a maze-task mechanism, not evidence about thumbnails [A, untested here]. It is also your unique angle drawn as a picture.
- **Layout:** the whole intact structure plus the wrong detail **in the center of the frame, where the eye already lands** (anomalies away from fixation are often missed: Vö & Henderson 2009, 2011 [A]); figure 15–20% of frame height, looking at the detail.
- **Watch out:** the wrong detail must be visible at 168 px (here the red chord is), and everything shown must be in the video by second 15. Add 1–2 words only if they add a fact the title lacks.
- **Prompt:** *A half-built steel cantilever bridge reaching out from a brown stone pier and stopping in mid-air, a long red lower beam clearly bowed downward, a straight tan upper beam and thin crossing braces; a small stick figure with a worried face stands on a green bank pointing up at the red beam; dark green river, sky blue background with clouds.* + master block.
- **Also fits:** Challenger at the cold pad, Tacoma's bouncing deck, Hyatt's empty atrium, Vasa at the quay.

### Style 3 — The Impossible Scene
*A scene that looks absurd but is true, with no words needed.*

- **Example:** de Havilland Comet, 1954. Draft title: *Why did a jet airliner end up in a water tank?* Words: **none**. Image, in plan view: a whole airliner fuselage in a water tank, wings protruding out through seals in the tank walls, a red ring on the roof near the front where a fatigue crack began, two calm engineers on the floor.
- **Why it should work:** the most extreme "zero-text anomaly" pattern: Veritasium "Why Are 96,000,000 Black Balls on This Reservoir?" (112M, uxPdPpi5W4o) and Mark Rober's jello pool (223M, DPZzrlFCD_I) show the image *is* the hook (both are 7-year cumulative totals) [B]; 1of10's best text setup is none, or under 10 characters [B]. Muller's "legitbait" idea: the picture hints at the real content [B, secondary].
- **Layout:** the bright water rectangle is the focal point on a warm floor; hero 65% of frame width; figures small and calm.
- **Watch out:** only use it when the true image exists; never invent an odd picture. The tank test is documented (Withey 1997); windows are not visible in plan view, so the "square windows" myth is neither drawn nor claimed. The red ring marks where a fatigue crack began (the tank-test crack started near the forward escape hatch; the Elba crack near the roof antenna cut-out): say which in the video.
- **Prompt:** *A plan view from above of a large rectangular water tank in a brown-walled hall: a complete white jet airliner fuselage lies in the light blue water with its swept wings passing out through two brown seals in the tank walls, small tailplane inside the tank, a thin red ring painted on the roof near the nose; two calm stick figures stand on the tan floor in front, one with a clipboard.* + master block.
- **Also fits:** Vasa raised from the seabed, Sleipner, "nothing broke but it failed" cases.

### Style 4 — Exhibit A
*One small part, drawn enormous, alone on a plain paper card with a thick ink frame. The part is red.*

- **Example:** Hyatt Regency walkways, 1981. Draft title: *Why did one small change help bring down two hotel walkways?* Words: **LOAD DOUBLED**. Image: a giant red nut and washer pulling through a split steel box beam, two separate rods (one above, one below).
- **Why it should work:** one dominant subject is the best-supported composition principle (Netflix win rates fall as scenes get more complex [B]; visual complexity has an inverted-U relationship with popularity [A]). A lone object on a plain field appears among high-view niche videos (Brick Immortar "El Faro", 4.8M, -BNDub3h2_I; Beyond Sky's clean object-on-light thumbnails, 1.6M and 1.2M) [B, correlational]. The brief explicitly allows beat drawings and text cards on plain flat paper, so this is the one style with a plain background by design.
- **Layout:** hero about 30–40% of the frame, off-center; words top-left; an ink frame keeps the pale card from dissolving on the white feed.
- **Watch out:** the geometry is generic and the rods are offset only to signal "two rods": check the connection detail against NBS report NBSIR 82-2465 before final art. The full story is two causes (the original detail would not have met code, and the change "essentially doubled" the load): the words "LOAD DOUBLED" are only half; the video must tell both.
- **Prompt:** *A plain cream paper card with a thick black frame; in the center a giant red hexagonal nut and a round white washer pulled up into a tan steel box beam whose welded seam has split open, a brown rod entering the beam from above and a second brown rod hanging below and slightly to the right.* + master block.
- **Also fits:** Challenger's rubber ring, Flixborough's bellows, Comet's bolt hole, Big Dig's anchor.

### Style 5 — The Cutaway
*A see-through cross-section of the part no camera ever recorded.*

- **Example:** Big Dig ceiling, 2006. Draft title: *Why did a Boston tunnel ceiling fall after glue let go?* Words: **26 TONS**. Image: the roof slab cut open, three red anchors sliding out of their epoxy-filled holes with dark gaps above, a heavy panel hanging tilted below, a small worried figure standing clear of it.
- **Why it should work:** cutaways are common among high-view engineering videos (Jared Owen "What's inside the Titanic?", 22M, HLrBUwNSEo0; Sabin Civil "Golden Gate", 19M, E6tp8DCAJ-0) [B, correlational], and a cartoon precedent exists (Ink Explainer's mammoth-carcass cutaway, 756K, dp3jYZXKOos) [B]. It delivers your promise, "what no camera ever recorded", and the brief explicitly allows a see-through cutaway.
- **Layout:** the cutaway is the central band; the red parts are oversized; words on the earth band; nothing important in the bottom-right corner.
- **Watch out:** the hardest style to draw correctly. Cause: epoxy with poor creep resistance (NTSB HAR-07/02); the mockup shows three anchors as an illustration, so check the count and details against the NTSB report. One person died in a car under the ceiling: keep every vehicle and person out from under the panel.
- **Prompt:** *A cross-section cutaway of a tan speckled concrete roof slab under brown earth: three white epoxy-filled holes each with a thick red anchor bolt that has slid down leaving a dark gap above it, the anchors holding a large white ceiling panel that hangs tilted in a bright cream tunnel; a small worried stick figure stands far to the left on a dark road.* + master block.
- **Also fits:** Comet's fatigue crack, Challenger's joint, Tacoma's cable band, Flixborough's bellows.

### Style 6 — The Giant Number
*One figure, huge, is the hook. The number is in the words layer, not the picture.*

- **Example:** Tacoma Narrows, 1940. Draft title: *Why did a four-month-old bridge twist itself apart?* Words: **42 MPH** (number cap height 250 px, unit 110 px). Image: a suspension bridge with the roadway drawn as a red-and-brown twisting ribbon, a small worried figure on a mound.
- **Why it should work:** it survived every phone-size test with the number still readable at 168 px. Numbers as the hook are common among high-view niche videos (Dark Records "1,500 TONS OF TNT", 4.8M, NgQ7jh9mrWs; Sabin Civil "27000!", 19M; Banqiao "62 DAMS GONE", 358K, CFnh54FeNo0) and in cartoon channels (Explain In Paint "-58°F?", 398K, Q3_htAFS7wg) [B, correlational]. 1of10 found titles with numbers got about 11% fewer views [B, correlational, viral videos only]; that is not a reason to avoid numbers, but putting the number in the thumbnail and not the title keeps the two complementary. Test it.
- **Layout:** the number takes the left 40%; picture on the right; nothing in the bottom-right zone.
- **Watch out:** this style deliberately breaks 1of10's "text under 10 characters and under 7% of the image" pattern: the words cover about a fifth of the frame. That is why it must be tested against a smaller-number variant. Pick a surprising number that is **not** a death toll. WSDOT measured 42 mph at 9:30 a.m.; the twisting began about 10:03: "42 mph" is a gale, so never write "light wind". The exact cause is still debated (torsional flutter is the usual explanation).
- **Prompt:** *A suspension bridge with two tall brown towers, thin cables and vertical hangers; the roadway is a ribbon twisting in the air, its face red and its underside brown; green hills, dark green water, a small worried stick figure with hands on head on a light green mound. Sky blue background with two clouds; the left 40% of the frame is calm and empty.* + master block.
- **Also fits:** Blackout ("50 MILLION"), Challenger ("36°F"), Banqiao, any story with a good non-casualty number.

### Style 7 — The Odd True Detail
*Two or three figures doing something odd that is documented, in a lit scene, with a two-word tease. This is Ink Explainer's format.*

- **Example:** Challenger, 1986 (the televised demonstration). Draft title: *Why did a rubber ring destroy a space shuttle?* Words: **ICE WATER**. Image: a hearing-room table with a glass of ice water and a clamped red rubber ring, three anonymous figures behind it.
- **Why it should work:** Ink Explainer's six top thumbnails all share this recipe: a full scene, one to three stick figures, and two or three words that tease the answer without repeating the title (e.g. "NO JOBS", 9.7M, 49_Ph2q6uIM; 106K subscribers) [B]. The same template gave very different results on clone channels, so the *idea* carries it, not the template. Three figures respect the Netflix limit.
- **Layout:** figures behind a long table; the two hero props (glass, ring) at the left, clear of the words; window at the right for light.
- **Watch out:** the demonstration was on 11 Feb 1986 (Rogers Commission Vol. 4 transcript; the quote was seen through a search summary): keep the figures anonymous and do not name or caricature the real people. The glass and ring are small at 168 px: the words carry the style there.
- **Prompt:** *A hearing room with a tan wall and a window: a long cream table with a dark green front; on the table a large glass of ice water with three white ice cubes and, beside it, a red rubber ring held in a small black clamp; behind the table three stick figures, two calm and one worried, looking at the ring.* + master block.
- **Also fits:** Tacoma's lemon-chewing workmen (documented by WSDOT), Vasa's stability test, Piper Alpha's permit boxes.

### Style 8 — The Crowd on the Shore
*The viewer sees the flaw while the calm crowd watches. The flaw is red.*

- **Example:** Vasa, 1628. Draft title: *Why did a brand-new warship sink in front of its own crowd?* Words: **CALM DAY**. Image: the grand ship upright with its lower gunports open (red) just above the waves, three calm figures on the shore.
- **Why it should work:** dramatic irony is the brief's core promise ("the viewer sees how they would have made the same call"). Storified's bus-heading-to-a-broken-bridge thumbnail is a cousin (613K, 0QXvhtPaKoY) [B]. Three figures respect the Netflix limit.
- **Layout:** the ship is the horizontal mass on the right; the crowd sits small on the left; words in the sky.
- **Watch out:** do not claim "nobody noticed": a stability test was stopped shortly before, so someone did. The style is about the *spectators'* view. The sources for the day and the wind are secondary: one says a calm day with a light breeze, then a gust, then a stronger gust; check the Vasa Museum. The red ports are small at 168 px, so the words carry the style there.
- **Prompt:** *A tall wooden warship with three masts and cream square sails floating in dark green water, a high curved stern, a row of black gunports on the brown hull and a lower row of open red gunports just above small cream waves; on the left a tan shore with three calm stick figures and a few small brown buildings behind them. Sky blue background, two clouds.* + master block.
- **Also fits:** Tacoma's drivers, Titanic-type stories, the Hyatt atrium before the collapse (empty).

### Style 9 — Seat of the Decider
*The viewer sits in the control room and sees what the operator does not.*

- **Example:** the 2003 Northeast Blackout. Draft title: *Why did a dead alarm help black out 50 million people?* Words: **LAST ALARM / 2:14 PM**. Image: a calm operator (front view, eyes toward the screens) at a console, one working screen and one frozen screen with a red frame; through the window a power line still clear of a tree.
- **Why it should work:** it is the brief's speech pattern #1 (second person, the viewer in the seat) as a picture; none of the roughly 105 disaster-niche thumbnails inspected by eye showed a decision room; cartoon channels use a single figure with props in a room (StickFigure Explains, 4.5M, Yh_7y2PYH1o; easy, actually, 9.7M, C5OJJD3Eytk) [B].
- **Layout:** the figure calm, the frozen screen red-framed, the window at the right; words top-left, clear of the window.
- **Watch out:** the timeline must stay separate: the Task Force report says the alarm software failed "shortly after 14:14 EDT" (the last valid alarm), while lines touched trees from about 15:05, so the picture shows the line still clear of the tree. The four cause groups in the report include much more than the alarm, and the title says "help black out". Do not draw a ringing phone: it is not documented. The figure is a front view with a gaze shift (no side view needed).
- **Prompt:** *A bright control room with a tan wall and brown floor: a calm stick figure sits behind a cream console desk, looking to the left at two monitors, one with a blue screen and white bars, the other with a blank cream screen in a thick red frame; on the right a window showing a green tree under a power line that droops but does not touch it.* + master block.
- **Also fits:** Challenger's teleconference, Piper Alpha's control room, Big Dig's inspection office.

### Style 10 — Close-Up Gaze
*A huge worried face looks sideways at the hazard. The hazard is red.*

- **Example:** Flixborough, 1974. Draft title: *Why did one bypass pipe blow up a whole chemical plant?* Words: **NO DRAWING**. Image: a head filling the left of the frame, eyes shifted toward two tan reactors joined by a red dog-legged bypass over the empty stand where a third reactor had been.
- **Why it should work:** it passed every phone-size test, including blur. The nearest real precedent: The Hydraulic Record puts the same worried presenter looking toward the hazard on the six of its thumbnails that were viewed (25K subscribers; 2M and 1M views on two recent videos; the Oroville example, mwwdnfaNKxk, has 132K) [B, causation unverified]. Netflix: complex emotion beats stoic [B]. A figure looking at the object shifts attention and recall to it (Sajjacholapunt & Ball 2014; real faces on banner ads [A]). Schematic faces still read emotion (Kendall 2016 [A]). MrBeast's team reported a small benefit from a closed mouth [B].
- **Layout:** head at least 25% of the frame height (mockup: about 55%); eyes shifted 20% toward the hazard; brows angled up in the middle; hazard in the right third; words in the sky.
- **Watch out:** two-dot eyes with no eye whites are **untested** for fear signals (Whalen 2004 concerns real eye whites [A]); test a subtle "worried" version against an open-mouth one. HSE's page says "bypass" (not "temporary"); it says no drawing and no calculations existed for the dog-leg or the bellows. Its statement that the bypass failure "may have been caused by" a fire on a nearby 8-inch pipe means the cause is contested: the red pipe marks the *modification*, not a proven cause, and the video must say so.
- **Prompt:** *A single huge round white stick-figure head filling the left third of the frame with a worried face, two black dot eyes shifted to the right, eyebrows angled up in the middle, small downturned mouth; on the right two tan chemical reactors with an empty tan stand between them, joined by a thick red zig-zag pipe with cream accordion joints; green ground, sky blue background.* + master block.
- **Also fits:** any story with one visible defect: Quebec's bowed chord, Big Dig's anchor, Tacoma's cable band.

---

## 6. Comparison and phone-size results

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

---

## 7. Testing playbook

- **Use Test & Compare** on every long-form video: up to 3 variants, desktop Studio, winner by watch-time share, up to 2 weeks. Upload your preferred variant **first**: if the result is inconclusive, the first upload stays. Outcomes are Winner, Performed Same and Inconclusive; YouTube says it is normal not to get a winner. Editing the title or thumbnail during a test stops it. Do **not** swap thumbnails by hand and compare: early viewers are your fans and the traffic-source mix distorts CTR.
- **Test concepts, not tweaks.** Sample size per variant for 80% power at 5% significance, CTR only (my arithmetic with the standard two-proportion formula; the real tool uses watch-time share, so treat as indicative): 4% → 8%: about 550; 4% → 6%: about 1,860; 4% → 5%: about 6,700 (6,745 exactly); 4% → 4.8%: about 10,300. Three variants triple the total.
- **Cadence.** Run a test at publish (core audience), read it at 48–72 hours, and re-test older videos with a new concept if the topic is evergreen. Re-testing after 72+ hours matches official guidance [A].
- **Log every video:** style, overlay words, CTR by traffic source, average view duration, test outcome. After 8–10 videos look for patterns across videos: single tests will rarely reach significance at small volumes.
- **Never judge CTR alone.** YouTube says clickbait shows as high CTR with low average view duration. If CTR rises and average view duration falls, the thumbnail over-promised.
- **Decision rules (my heuristics [C], not from a source):** do not touch anything for 48 hours; "Winner" means adopt it; "Performed Same" means keep your favorite and log it; "Inconclusive" means accept the default; consider a manual swap only if after about 5,000 impressions CTR is under 70% of your own same-source baseline and average view duration is healthy, and then change the whole concept.
- **Title–thumbnail pairing** (Galloway, Ritchie, the MrBeast memo, YouTube staff [B]): plan the title and thumbnail before recording. The thumbnail must add what the title does not, must not repeat its first ~40 characters, and everything it promises must be visible or explained by second 15 (your outcome-first opening already enforces this). Keep your question titles, but make them concrete (a named object or a number) so they do not read as vague; the evidence on questions is mixed and comes from headlines. Note that several draft titles here have their key idea after character 40 (for example titles 3, 6 and 9): shorten them before publishing if you want the hook to survive truncation.
- **Per-thumbnail QA** (run `tools/thumb_preview.py`): 1) squint (blur): the accent, main word and silhouette survive; 2) phone size: main word cap height at least 90 px on the master; 3) grayscale: word vs background lightness gap at least 50 (the ink outline carries white words on pale colors), figure vs background at least 25; 4) light and dark feed: image edges do not dissolve; 5) color-blind: red never on green or brown; 6) badge zone free of anything important; 7) zoom to 100% and look for stray letters or numbers on signs, gauges and clocks, and for hands, shoes or thick limbs; 8) 3 words or fewer; 9) export sRGB, 16:9, under 2 MB.

---

## 8. Registry of facts used in the examples

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

---

## 9. Decisions I need from you

1. **Text on thumbnails.** The brief bans text inside images, but about 70% of the thumbnails inspected in the niche (75 of about 105; median 3–4 words, max 7) and all of Ink Explainer's top videos carry two or three words. I assumed the words are a separate overlay layer in Figma, Canva or Photopea, never in the generated image; the `art-only/` files show the generated layer. Confirm, or tell me to make all ten wordless.
2. **Plain paper (Style 4).** The brief bans an "empty flat background" but allows beat drawings and text cards on plain flat paper. Style 4 is a plain paper card with an ink frame. Confirm it counts as a beat drawing.
3. **The character sheet.** There is none in the brief. Ink Explainer's figures have circle eyes with lids; yours have dot eyes. Approve dot eyes with a *gaze shift* toward the hazard, and a *very large head* for Style 10.
4. **Numbers on thumbnails.** I used only non-casualty numbers (mph, tons, a time of day). Should a death toll ever appear as a hook, given "state casualties factually and move on"? I recommend no.

---

## 10. Shorts

- The Shorts feed plays the video without showing a thumbnail; covers appear on the channel page, in search and on the homepage [B/C: search is our own JSON check; the rest is secondary]. A custom cover can only be set on a computer in Studio, is rolling out (Partner Program creators first; the Help page says "verified account": check which applies to your channel), and there is **no A/B testing for Shorts** [A].
- Covers are 9:16 (2160×3840). Keep everything important inside a central 2:3 crop [B].
- The first-frame equivalent of a thumbnail is **frame 0 to 1 s**: the outcome image plus a 3–6 word line (matches the brief's "outcome within the first 3 seconds"). Styles that translate best to vertical: 6 (Giant Number), 10 (Close-Up Gaze), 4 (Exhibit A).
- "99.9% of Shorts views come from the feed" is a creator remark, misattributed online: do not rely on it.

---

## 11. Caveats

- No CTR or impression data exists outside your own Studio, so every "should work" is an inference from view counts, lab attention studies and headline experiments. Views depend on video age, topic and channel size: I compared only within a channel and only as patterns. Several cited view counts are cumulative over many years.
- Several sources could not be opened (YouTube watch pages and transcripts, vidIQ's study page, ScienceDirect, Springer, ACM). Those findings rest on abstracts or secondary reports and are marked as such in `research/`.
- Beaupré's and Ritchie's statements come through Search Engine Journal and ppc.land, not the original videos. The MrBeast production memo is unauthenticated.
- The saliency and OCR checks in the design report are proxies, not human studies. The duration-badge geometry is approximate.
- The mockups are vector art, not generated images: real generated images will differ, and you must check every one for stray letters and numbers. Several drawings simplify the real objects (see each style's watch-out).
- About 300 of the 405 niche thumbnails were measured programmatically but not visually inspected. The counts "about 105 inspected by eye", "75 with text" and "about 300 cartoon thumbnails inspected" come from the agents' reports, not from their saved notes.

## 12. Files

- `thumbnail-lookbook.html`: all ten mockups, the phone-size test, and the comparison in one page (Slovenian captions).
- `thumbnails/`: the ten composites, `art-only/` layers, editable `svg/`, and `qa-phone-sizes.png`.
- `tools/`: `thumb_preview.py` (feed preview rig: light and dark feed, several sizes, badge, grayscale, blur, safe zones; usage `python3 thumb_preview.py image.png --title "..." --duration 10:24 --safezone`, needs Pillow) and the mockup generator (`scenes.py`, `lib.py`, `render.py`, `fonts/`; rendering needs a headless Chromium).
- `research/*.md`: the eight research agents' notes with URLs, quotes and evidence grades: `platform`, `ctr-evidence`, `psychology`, `niche-audit`, `cartoon-audit`, `design-system` (and `design-system-palette-pairs`), `packaging`, `story-visuals`.
