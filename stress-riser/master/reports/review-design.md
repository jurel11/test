VERDICT: Not ready to hand to an image generator. The palette is clean. But the set breaks the brief in 3 places (Style 7 panels, flat black scenes in 4 and 9, invisible limbs in 5 and 9), misdepicts documented facts in 3, 4, 8 and 9, and 6 of 10 mockups fail the report's own red-accent and phone-size claims.

MEASURED, no action needed: palette. 97.5–99.7% of pixels per file are exact palette colors. The rest are 1–2 px blends of two palette colors. Off-palette flat fills: none. Pixels farther than 6 RGB units from any two-color blend: 0–46 per file (worst is 02, 40 px at #9c625b, a three-color edge). SVGs use only the 10 fills and strokes, with no gradient, opacity, filter, dash or marker. Off-palette color used on purpose: none. OCR (rapidocr) on art-only files found no text. The only hits are shapes: 01 "o000", 08 "中宁中", 10 "ri", 03 "P", 07 "1O". The composite 01 reads "MOUNTAIN.OOQ".

MUST-FIX
1. Style 7 (whole file). Two panels joined by an ink divider is "collage/multiple panels" from the brief's Never list. The report only says it "needs approval". Near/mid/far layers are also missing. The geometry is invented. A vertical banana-shaped column bows about 230 px over 700 px. The documented member is a lower chord, which is near-horizontal, and the size of the bend is "check the Commission". Fix: one 1280x720 frame.
   - Brown stone pier at x80–200, y300–650.
   - Half-built truss reaching to about x1150 and stopping in mid-air.
   - Lower chord horizontal at y420–470, red, bowed about 40 px.
   - Inspector at (330,560), head r=34, one arm pointing up.
   - Delete the divider, the wreck and the splash blobs.
2. Styles 4 and 9. The prompts say "plain ink-black background", which is "empty flat background" and not a "whole, richly illustrated place". Evidence also runs against dark scenes: Ink Explainer's dark-cave "I WILL DIE" is one of its lowest 3, and 1of10 found dark thumbnails underperform. Fix: put both on lit scenes. For 09, paper wall #f3ead8 at x0–800.
3. Style 3 (Comet) misdepicts the fact. research/story-visuals.md says the whole fuselage sat in the tank with the wings out through seals.
   - The mockup shows the entire airliner submerged, tail included, with one under-wing pod. The Comet had four buried engines.
   - The red tail fin marks a part that did not fail. That breaks the report's own rule 4.
   - The windows are ellipses (rx9, ry12). That is the post-fix oval shape, not the Comet 1's rounded rectangles the report says to draw.
   - Fix: wings poke through the tank walls (x≈100 and 1180). Tail outside the tank. Windows about 22x30 with rx7. Fin paper-colored. A small red ring (about 30 px) at the roof cut-out, since the failure began at a bolt hole near the roof antenna cut-out.
4. Style 9 timeline is wrong. "2:14 PM" is paired with a red line touching a tree. Documented: the alarm failed shortly after 14:14. Lines contacted trees after 15:05. The picture merges two events and never shows the dead alarm, which is the title's subject. Fix: leave a gap of at least 40 px between line and tree (line end (1104,342) to tree top (1060,340)). Make the screens the visible problem.
5. Style 4 (Hyatt) has a diagram symbol and invented geometry.
   - The red lightning cracks (x650–700 and 1070–1120, y330–445) read as arrows and are invented. NBS says the welded seam of the box beam opened and the washer pulled through.
   - One rod through beam and nut is the original single-rod design. As drawn, it cannot show "LOAD DOUBLED".
   - Fix: delete the bolts. Open the centerline seam (y=365) about 20 px under the washer. Draw two separate rods, and check the detail against NBSIR 82-2465.
6. Style 5 (Big Dig).
   - The red bar plus the cream circle beneath it (x672–748, y252–608) reads as a red "!". The five thread lines read as a ruler.
   - One bolt carries the panel. NTSB says several anchors pulled free.
   - Fix: three red anchors, each 110 px wide. Delete the circle and thread lines. Black void above the bolt 62 → 110 px (y190–300).
   - Text fill top is at y=21, below the 36 px margin. Baseline 118 → 136.
7. Limbs are invisible on ink in 05 and 09. Single black lines on #1a1a1a leave a floating head and body. This breaks the "arms and legs are single black lines" rule. Fix: put the figure on a light surface. For 05, a paper rect at x60–260, y420–664 and r 40 → 55. For 09, the paper wall from finding 2.

SHOULD-FIX
8. Red accent 3–8% of the frame, measured. Pass: 01 5.1%, 04 3.0%, 07 5.1%. Fail: 02 0.0%, 03 0.5%, 05 1.9%, 06 0.7%, 08 0.1%, 09 0.4%, 10 0.8%.
   - Red sits on non-culprits: the 02 thermometer, the 03 fin, the 06 pennant.
   - 02: make a red band on both boosters at y≈470–500, and make the thermometer column ink.
   - 08: the foreground polygon hides the red ports. Raise the ship about 60 px and enlarge the ports to 50x46.
9. Style 8 (Vasa).
   - The ship pitches bow-down. It does not heel. Sea and land are both #4f7d3a, so it reads as a hull stranded on a hill.
   - "Nobody notices" is undocumented. It contradicts the stopped stability test, where someone did notice.
   - "LIGHT BREEZE" rests on a [C] source, and the research also notes a second, stronger gust.
   - Fix: sea sky-blue. Ship seen bow-on and heeled about 20°. Crowd expectant, not waving.
10. Style 1 (Vajont).
   - The dam reads as a cream staircase on a hill. Wave, reservoir and hill are all #4f7d3a. The horizontal lines look like ladder rungs.
   - The foam circles read as "OOOO" beside the word. They sit about 15 px from the N at x735.
   - Vajont is a thin arch dam, not a trapezoid.
   - Fix: reservoir light green. Narrow tall arch. Delete the lines. Foam at least 60 px from the text.
11. Arrow and diagram-like shapes.
   - The 06 pennant (x780–905, y195–240) is a right-pointing wedge next to "42". Its flag is undocumented, so delete it.
   - The 10 red Z pipe (x840–1040, y425–545) reads as a lightning bolt between two jars. Fix: thicken to 50 px and add cream accordion bellows.
12. Style 2 (Challenger).
   - The figure floats about 40 px above the ground (feet y≈556, ground y≈598). Lower it by 44 px.
   - The icicles are about 45 px and vanish at 168 px. Enlarge to 90–130 px.
   - The breath puff sits on the thermometer top and reads as steam. Move it to the mouth, about (905,430).
13. Safe zones and text rules, measured.
   - Fill top margin under 36 px: 05 (21) and 10 (27).
   - Cap height under 90 px: 08 (88) and 10 (86).
   - 06 outline reaches x=32.
   - Text bounding box is about 30% of the frame in 06. The report's own evidence is "under 7%".
   - Left fill margins are 65–71 px, fine.
   - QA rule 3 needs word-to-background L* gap of 50 or more. White on sky is 12 (02, 06, 08, 10). White on tan is 25 (01). Only the outlines carry these.
   - Badge zone (x1050–1280, y630–720): 01 has the dam base, wave and foam there, 07 has the splash, and 05 has the panel corner.
14. Style 9 is not a side view. It is a front head with a gaze shift. The report and Decision 3 ask approval for something that was not drawn. The amber lamp is a sliver, 0.04% of the frame, behind the body. The screens are the same sky blue as the window. The thin vertical stroke at x=830 reads as a stray "I".
15. Style 10. The red bypass asserts a contested cause. HSE says an 8-inch pipe fire may have caused it. The reactor-5 gap is missing. Word the title around the modification: "no drawing".
16. Style 6. The picture shows vertical waves. The title says "twist", and the documented image is a deck tilted 28 ft or 45° with solid green girder walls. Red on the pennant makes wind the culprit. The deck touches the figure's head (about (1010,503) vs a head at 512).
17. If overlay text is refused (Decision 1), 06 has no hook and 4, 5 and 9 lose theirs.

NIT
- 03: the wavy waterline reads as a sagging cable. The wing trapezoid reads as a funnel.
- 08: crowd arms are hidden as bumps behind the heads. The three figures are identical and in a row.
- Big Dig: keep the figure out from under the panel. One person died, in a car.

PHONE SIZE (qa-phone-sizes.png)
I disagree with report section 6 on these:
- 09 "good": no. Blank rectangles, a limbless figure, and the concept unreadable.
- 08 "good": no. The ports are invisible, and it reads as a boat on a hill.
- 07 "improved": no. It is the worst: a red arc plus beams.
- 02 "good": the words read, but the "wrong detail" and the figure do not.
- 04: the cracks read as red arrows.
Fail the 168 px squint: 1, 2, 5, 7, 8, 9. Pass: 3, 6, 10, and 4 (words and nut only). A stranger gets the subject at a glance from 3 (airliner in a tank), 6 (bridge plus "42 MPH"), and 2 and 8 only from their silhouettes and words.

DISTINCTNESS
- 4 and 5 are the same layout: vertical rod through a horizontal slab, a red part, dark ground, words top-left. Merge them.
- 2, 8 and 9 are one idea (a calm figure unaware of the hazard).
- 1, 2, 6, 8 and 10 share one template: sky, two words, object, tiny figure. 2 and 8 look alike at 168 px.
- 7 is 1 split in two.
- Story-locked: 3 (needs a true odd image), 9, 6, 7.
- Missing: Ink Explainer's format. The evidence (cartoon-audit item 1) is a full saturated scene, 1–3 figures doing an odd documented thing, and a 2–3 word teaser. Example from story-visuals: Tacoma's "Galloping Gertie" as a tourist attraction, with the lemon-chewing workmen. Replace 7 with it.
- Style 7 has no evidence beyond three videos and is banned by the brief.

FIXES FOR THE THREE WEAKEST (7, 5, 9)
- 7: see finding 1.
- 5: see findings 6 and 7. Also recolor the tunnel from #1a1a1a to #4f7d3a or brown so the limbs read, and use r=55.
- 9:
  - Paper wall x0–800, y100–545.
  - Amber lamp at (620,470) in front of the body.
  - Screens paper-cream with a 12 px ink frame.
  - Line clear of the tree.
  - Figure r 74 → 90 at (640,360), arms and legs on paper.
  - Words: keep "2:14 PM" only if the tree contact is removed.

RANKED, strongest to weakest concept for this channel
1. 10 Close-Up Gaze: reads at any size, emotion, works for any story.
2. 2 Moment Before: it is the channel's angle drawn as a picture. It needs a visible detail.
3. 1 Tiny Under the Giant: a proven scale format. It needs a redraw.
4. 6 Giant Number: the only sure squint pass. It is number-only and text-heavy.
5. 9 Seat of the Decider: speech pattern #1 as a picture. Execution is weak.
6. 3 Impossible Scene: honest and memorable, but story-locked and currently wrong.
7. 8 Nobody Notices: the crowd's unawareness is undocumented, and there is a mockery risk.
8. 4 Object on Trial: dark, flat, and a duplicate of 5.
9. 5 Cutaway: fails the squint.
10. 7 Diptych: banned by the brief and unreadable.