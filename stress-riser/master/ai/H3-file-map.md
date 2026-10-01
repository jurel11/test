### R2. Repository file map

Everything is in the repository `jurel11/test`, branch `claude/stress-riser-channel-o2tnfv`, folder `stress-riser/`. The `isotrack-*.html` files in the repository root are unrelated to the channel.

| Path | What it is |
|---|---|
| `STRESS-RISER-AI.md` | This file: the AI-readable edition of the research (plain Markdown) |
| `STRESS-RISER-MASTER.html` | The full human-readable dossier in one HTML page: images, raw notes, reviews, video indexes, consolidated sources |
| `channel-brief.md` | The channel brief, verbatim (also loaded automatically through `CLAUDE.md`) |
| `thumbnail-styles.md` | The corrected report of the ten styles (Part C of this file) |
| `thumbnail-lookbook.html` | Visual gallery of the ten mockups with Slovenian captions |
| `thumbnails/NN-*.png` | The ten final composites (1280x720, with the text overlay) |
| `thumbnails/art-only/NN-*-art.png` | The layer an image generator would produce (no words); Styles 2 and 3 have no words, so no separate file |
| `thumbnails/svg/NN-*.svg` | Editable vector sources |
| `thumbnails/qa-phone-sizes.png` | Each style at 360 px, 168 px (light and dark feed), grayscale and blurred |
| `research/*.md` | The eight agents' working notes (G3 to G10 of the HTML dossier) and the palette pair report |
| `master/*.md`, `master/reports/*.md`, `master/ai/*.md` | Text sources of the two dossier editions: summary, synthesis, briefs, the eleven reports (eight research reports and three reviews), and the AI-edition front matter |
| `data/` | CSV tables (niche and cartoon video indexes, palette pairs, fonts, OCR) and small reports |
| `tools/thumb_preview.py` | Feed preview rig: light and dark feed, several sizes, badge, grayscale, blur, safe zones (needs Pillow) |
| `tools/scenes.py`, `lib.py`, `render.py`, `fonts/` | The mockup generator (needs a headless Chromium) |
| `tools/build_master.py`, `tools/build_ai.py` | Scripts that rebuild the HTML dossier and this file from the sources above |

Preview tool usage: `python3 tools/thumb_preview.py image.png --title "..." --duration 10:24 --safezone`.

Rebuilding this file: `python3 tools/build_ai.py` (Python 3 only, no packages needed).
