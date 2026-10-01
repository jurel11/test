# Design system, colour math, workflow: final report (2026-09-30)

Folder: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/design-system
Full notes with URLs: notes.md. All 45 pairs: palette_report.md and palette_pairs.csv.
**Preview script: /tmp/claude-0/-home-user-test/6d0dc7ad-48d3-54ee-b7fe-493bfcf23c29/scratchpad/research/design-system/tools/thumb_preview.py**
Usage: `python3 thumb_preview.py img.png --title "..." --duration 10:24 --safezone`, or `--demo`. Pillow is installed here; the other scripts also need numpy, fonttools, scipy and rapidocr-onnxruntime.

Grades: [A] official or peer-reviewed, or a measurement I made myself. [B] company or creator data. [C] opinion or SEO blog.

## 1. Palette maths (my computations, checked against published reference values) [A]
The palette has only three lightness tiers.
- LIGHT: white L*100, paper 93, sky 88, amber 75, tan 75, light green 72.
- MID: red 52, brown 49, dark green 48.
- DARK: ink 9.
- Colours inside one tier cannot be told apart by lightness in grayscale, blur or colour-blind vision. Only hue separates them.

Thresholds I used:
- WCAG text needs 4.5:1, and non-text needs 3:1.
- Material's own code comment says an L* gap of 40 guarantees at least 3:1 and a gap of 50 guarantees at least 4.5:1.
- APCA Lc levels: 90 preferred body, 75 minimum body, 60 minimum fluent text, 45 minimum large text, 30 any text, 15 invisible.

My rule: a gap of 50 or more is text-safe, 40–50 suits big bold text, 25–40 suits big flat shapes only (add an outline), and under 25 is luminance-invisible.

| pair | WCAG | dL* | dE2000 | APCA Lc | worst colour-blind dE2000 | use |
|---|---|---|---|---|---|---|
| ink/white | 17.4 | 90.7 | 86 | 104 | 86 | text and outline |
| ink/paper | 14.6 | 83.7 | 84 | 92 | 83 | text |
| ink/sky | 12.7 | 78.4 | 79 | 84 | 77 | text |
| ink/amber | 8.95 | 66.2 | 66 | 65 | 62 | text; amber's best pairing |
| ink/light green | 8.1 | 62.9 | 61 | 60 | 57 | text |
| white/dark green | 4.85 | 52.2 | 45 | -79 | 42 | white text |
| white/brown | 4.6 | 50.8 | 42 | -77 | 40 | white text |
| white/red | 4.2 | 48.2 | 44 | -73 | 38 | white text |
| ink/red | 4.1 | 42.5 | 43 | 34 | 31 | outline yes, ink text no |
| paper/red | 3.5 | 41.2 | 41 | -60 | 31 | big text |
| red/sky | 3.1 | 35.9 | 52 | -51 | 40 | best red accent background |
| sky/paper | 1.15 | 5.3 | 18 | -8 | 14 | FAIL |
| white/paper | 1.2 | 7.0 | 9 | -11 | 8 | FAIL |
| white/sky | 1.37 | 12.3 | 14 | -21 | 9 | FAIL |
| tan/amber | 1.01 | 0.5 | 14 | 0 | 7.7 | FAIL |
| dark green/red | 1.15 | 4.0 | 54 | 0 | 5.5 | FAIL for colour-blind viewers |
| brown/red | 1.09 | 2.5 | 19 | 0 | 2.9 | FAIL |
| dark green/brown | 1.05 | 1.4 | 31 | 0 | 3.7 | FAIL |
| light green/amber | 1.11 | 3.3 | 26 | 0 | 4.3 | FAIL |
| light green/tan | 1.09 | 2.9 | 24 | 0 | 7.8 | FAIL |
| light green/red | 1.96 | 20.4 | 59 | -26 | 13 | weak |

Other findings:
- **(a) Text.** White or paper fill with an ink outline works on every palette colour. Ink text needs a light background. Never use red, brown or green as a text fill.
- **(b) Subject against background.** The white head pops on dark green, brown, red and ink (dL* 48–91). It relies on its outline on sky or paper.
- **(c) Outlines.** Ink is at least 3:1 against every palette colour (the minimum is ink/dark green at 3.59). It is the universal outline.
- **Accent.** Red is the default. Saliency proxy on 168x94 cluttered scenes (Achanta frequency-tuned saliency, 40 scenes per cell): the accent disc was the most salient point in 95% of scenes for red and 69% for amber.
  - Amber fails on light green (2%) and brown (8%).
  - Amber on ink is the only strong amber pairing (dL* 66).
  - Red is weaker on brown and ink.
  - The proxy overrates chroma, so it wrongly favours amber on tan. Treat amber/tan and red/brown as failures. This is a model, so [C].
  - The two accents must never touch: amber/red has dL* 23.7 and a colour-blind dE2000 of 17.7.
- **Colour-blind viewers.** NEI: about 8% of men and 0.5% of women of Northern European descent have red-green deficiency. In simulation (Machado 2009) red becomes olive (#726835 protan, #968733 deutan), the same as dark green. Red on green or brown scenes loses its accent for them.
- **Pale colours on the light feed.** Sky and paper against the white page score 1.37 and 1.15, so the card edge dissolves (see tools/out/demo1_sheet.png). Keep a mid or dark band or an ink border along the image edges.

## 2. Feed sizes: first-hand measurements [A]
I requested YouTube's own JSON on 2026-09-30.
- Desktop search asks for 360x202 and 720x404.
- The watch-page sidebar asks for 168x94 and 336x188, and sometimes 196x110 and 246x138.
- Mobile web asks for up to 686x386, which is 2 x 343 CSS px.
- The desktop home card is 310–500 px wide. This comes from YouTube's skeleton CSS.
- Page background is #ffffff in light mode and #0f0f0f in dark mode, also read from YouTube's CSS.
- Phone widths (StatCounter, Aug 2026): 414 is the most common in the US, UK, CA and AU (21–30%), then 390 (12–14%), then 393/402/375/360. A full-width card is therefore about 360–414 px wide.
- Native app card sizes: UNVERIFIED, because the iOS and Android client APIs refused my requests.
- YouTube serves every thumbnail as a 1280x720, 4:2:0 JPEG of roughly quality 90 (72–367 KB in 20 samples).

Official upload spec (support.google.com/youtube/answer/72431) [A]: 3840x2160 recommended, minimum width 640, JPG or PNG, 16:9, 2 MB limit from mobile and 50 MB from desktop.
- Test & Compare allows up to 3 variants and picks the winner by watch-time share, not click-through rate.
- If any test thumbnail is under 720p, all are downscaled to 480p.

Myths:
- "1280x720, under 2 MB" is outdated.
- "168x94 on the phone feed" is wrong. It is the desktop sidebar size.
- SEO size lists such as "246x138 search" and "156x88 mobile" match nothing I measured [C].
- "38% higher click-through rate from consistency" and "70/30 rule" have no method behind them [C].

Device share:
- TV passed mobile for US watch time in December 2024 (YouTube CEO letter, Feb 2025) [B].
- Chartbeat: 69% of views are on mobile, but TV gives 42% of minutes [B].
- Phones dominate impressions, but thumbnails must also survive big screens.
- Dark-mode share numbers are unsourced: UNVERIFIED.

The rig renders light, dark, grayscale and blur columns at 360, 390, 310 (desktop home minimum), 246 and 168 px, with rounded corners, the badge, an optional title, a watch bar and a safe-zone overlay. The badge geometry is my approximation. The rig is pessimistic, because real phones are 2–3x sharper.

## 3. Text overlay (1280x720 canvas)
Needed cap height on the master is the displayed cap height times 1280 divided by the displayed width.
- Comfortable is 12 px displayed (about 19 arc-min at 36 cm). That is 91 px on the master for a 168-wide thumbnail, 62 px at 246 wide, and 43 px at 360 wide.
- Sources for 12 px: Ohnishi & Oda 2020 (legibility plateaus at about 12 pixels per letter height) [A], ISO 9241-303 (16 arc-min minimum, 20–22 preferred) [B], and Bababekova 2011 (phone viewing distance 36.2 cm for texting, 32.2 cm for web) [A].
- My OCR proxy [C]: the floor is about 5–7 px displayed, or 40–50 px on the master at 168 wide. Fredoka, Baloo 2 and Rubik read at 40 px. Lilita One, Titan One, Paytone One and Luckiest Guy need 50 px. Anton needs 70 px and Passion One Black never stabilised.

Recommendation:
- **Main word.** Cap height 100–140 px, minimum 90 px. Secondary text at least 60 px.
- **Outline.** Ink #1a1a1a, drawn outside the letters with round joins, at 12% of cap height (12–16 px). Use about 8% for condensed fonts, or their counters fill in. Optional hard 6–8 px offset shadow. No blurred shadows, which vanish at small sizes.
- **Words.** 1–3 words (the brief allows 4), caps, no more than about 16 characters per line, at most 2 lines.
- **Font.** Lilita One is the primary: font size about 143 px for a cap height of 100 px, and it fits about 16 characters across 1152 px. Titan One (wide), Paytone One and Fredoka 700 or Baloo 2 800 are alternates.
  - Luckiest Guy and Bangers are comic alternatives, but Bangers is thin at 168 px.
  - Anton or League Gothic suit numbers only.
  - Handwriting faces (Patrick Hand, Kalam, Comic Neue) are too thin.
  - All are free, under OFL or Apache-2.0.
- **Placement.** Margins of 64 px left and right and 36 px top and bottom, because the corner radius is about 43–61 px on the master. Keep 230x90 px free at bottom-right (badge and watch bar). Keep roughly 110x110 px free at top-right (desktop hover icons, size UNVERIFIED). Put the text block top-left or in the left third.
- **Text on mid-tone colours.** Ink text fails on red, brown and dark green (Lc 29–34). Use white fill with a thick outline, or a paper caption box with an ink outline.

## 4. Series consistency
- **Recognition.** Distinctive-brand-asset research (Romaniuk 2018, Ehrenberg-Bass) says recognisable, unique assets (characters, colours, shapes) need consistent repetition [B, via summaries]. A 2026 International Journal of Advertising paper reportedly finds shape assets strongest, but I saw only the snippet, so UNVERIFIED. If true, the stick-figure silhouette is the best anchor.
- **Banner blindness.** NN/g [A] shows people ignore things that look like ads (position, animation, fancy formatting). It is not evidence against consistent templates. The real risks are an ad-like banner or ribbon look and habituation.
- **Pop-out.** Pop-out needs feature contrast against a calmer surround (Nothdurft 1993, Wolfe & Horowitz 2017) [A]. Use one accent per image.

**Fixed anchors**
1. The 10-colour palette only.
2. An ink outline of 12–16 px on every shape.
3. The stick figure exactly as on the character sheet, with a head of at least 150 px if the face carries the emotion.
4. One accent object of 3–8% of frame area, red (amber only on ink scenes), never both.
5. One typeface (Lilita One), white or paper fill, ink outside stroke, 1–3 caps words.
6. Flat colour with gentle cel shading and no gradients.
7. The safe zones above.

**Variables:** composition, hero object, dominant background family (light, mid or dark tier), emotion, text position within the safe zone, word count, camera distance, cutaway or not.

Make consecutive thumbnails differ in background tier so the feed alternates. Keep about 5 anchors fixed and vary about 4 axes per video.

## 5. Production workflow
Documentation [A]:
- **OpenAI.** Prompt order is scene, subject, details, constraints. The edit endpoint takes multiple references and an alpha mask. Text placement, recurring-character consistency and precise placement are documented weak points.
- **Google.** Use the formula Subject + Action + Location + Composition + Style. It accepts up to 14 reference images and does text-based mask edits. It also says "use positive framing" (describe what you want).
- **Midjourney.** V7 uses `--oref`, with `--ow` from 1 to 1000 and a default of 100 (docs page blocked, so secondary sources only).
- **FLUX Kontext.** Iterative edits that preserve the character.

A research finding matters here: image models often ignore negation (arXiv FineGRAIN and NeIn). So back the "no text" rule with positive wording ("blank plain board", "gauge with a needle and no marks"), and inspect or inpaint afterwards.

Workflow:
1. Make one character sheet (front, side, three expressions, prop) on flat paper and attach it to every generation.
2. Generate at 16:9 with one big hero shape, the figure large in the lower third, and a calm empty third for the text.
3. Fix stray glyphs with a masked edit ("change only X, keep everything else identical"), or paint flat colour over them.
4. Add the text as a live-text layer in Figma, Canva, Photopea, GIMP or Affinity (free since Oct 2025 with a Canva account).

Export, measured on a flat cartoon at 1280x720: PNG-24 was 33 KB, PNG-8 14.5 KB, JPEG q90 4:2:0 63 KB, and q95 4:4:4 94 KB. So use sRGB PNG-24 without alpha, under 2 MB. Use JPEG q92 4:4:4 only if a grainy image pushes it over. A master of 1920x1080 or 3840x2160 is fine if it stays under 2 MB, but YouTube delivers 1280x720 anyway. 4:2:0 chroma subsampling softens edges by 2 px (mean dE76 1.4–3.1 at a hard edge), which matters only where there is no ink outline.

**QA checklist** (run the rig on every thumbnail):
1. Squint (blur column): accent, main word and figure silhouette all survive.
2. Phone size: read the 360 and 168 rows at 100% zoom with the main cap at least 90 px.
3. Grayscale: word/background dL* at least 50, figure/background at least 25.
4. Light and dark rows: image edges must not dissolve on white.
5. Colour-blind: accent never red-on-green/brown, amber never on tan or light green.
6. Badge zone empty.
7. AI-glyph check at 100% (letters or numbers on signs, gauges, clocks; fingers, shoes, thick limbs).
8. Three words or fewer.
9. Export: 16:9, sRGB, under 2 MB.
10. After publishing, run Test & Compare with up to 3 variants.

## Sources
- support.google.com/youtube/answer/72431
- support.google.com/youtube/answer/16391400
- gs.statcounter.com/screen-resolution-stats/mobile/{united-states-of-america, united-kingdom, canada, australia, worldwide}
- YouTube web/API responses, YouTube CSS (saved in raw/)
- github.com/material-foundation/material-color-utilities (hct.ts)
- github.com/Myndex/SAPC-APCA (minimum_compliance.md)
- w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- doi.org/10.1109/tvcg.2009.113 (Machado 2009)
- pmc.ncbi.nlm.nih.gov/articles/PMC7768324 (Ohnishi & Oda 2020)
- Bababekova 2011, Optom Vis Sci 88:795 (journals.lww.com)
- ISO 9241-303 / HFES 100 (via search summaries)
- nngroup.com/articles/banner-blindness-old-and-new-findings
- nature.com/articles/s41562-017-0058
- tvtechnology.com (Mohan letter, Feb 2025)
- advanced-television.com (Chartbeat, Jun 2025)
- developers.openai.com/api/docs/guides/image-generation
- developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- docs.bfl.ml/kontext
- arxiv.org/abs/2512.02161 and 2409.06481
- github.com/google/fonts (font licences)
- cgchannel.com and macrumors.com (Affinity free, Oct 2025)
- National Eye Institute colour-blindness figures (via secondary pages)

## Caveats
- I could not read the duration-badge CSS or the native app card sizes. The 230x90 keep-out box is derived from a [C] source.
- The OCR and saliency results are proxies, not human studies.
- The Ohnishi & Oda figures and the Midjourney docs came through summaries, because the raw pages were blocked.
- I could not open the 2026 shape-asset paper.
- Dark-mode share is UNVERIFIED, and so is whether YouTube honours an embedded ICC profile.
- The phone pixel-size figure (about 0.166 mm per CSS px) is derived from a device spec I did not fetch.
- The rig is a 1:1 CSS-pixel simulation, so real phones look sharper than it does.