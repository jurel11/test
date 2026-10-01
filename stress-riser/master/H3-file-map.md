## H3. File map and tools

Everything is in the repository `jurel11/test` on the branch `claude/stress-riser-channel-o2tnfv`, folder `stress-riser/`. The Isotrack files in the repository root are unrelated.

| Path | What it is |
|---|---|
| `STRESS-RISER-MASTER.html` | This file: the whole dossier in one self-contained page |
| `STRESS-RISER-AI.md` | The same research as one plain-Markdown file for an AI to read: no images, layered from the most to the least important, with a map and line numbers at the top (reports, raw notes and indexes are left out) |
| `channel-brief.md` | The channel brief, verbatim (also loaded automatically through `CLAUDE.md`) |
| `thumbnail-styles.md` | The corrected report of the ten styles (Part C of this file) |
| `thumbnail-lookbook.html` | The visual gallery of the ten mockups, in Slovenian captions |
| `thumbnails/NN-*.png` | The ten final composites (1280×720, with the text overlay) |
| `thumbnails/art-only/NN-*-art.png` | The layer an image generator would produce (no words); Styles 2 and 3 have no words, so no separate file |
| `thumbnails/svg/NN-*.svg` | Editable vector sources |
| `thumbnails/qa-phone-sizes.png` | Each style at 360 px, 168 px (light and dark feed), grayscale and blurred |
| `research/*.md` | The eight agents' working notes (G3–G10) and the palette pair report |
| `master/*.md` | The sources of this file: summary, synthesis, briefs, and `reports/` with the eleven final reports (eight research reports and three reviews) |
| `data/` | CSV tables (niche and cartoon video indexes, palette pairs, fonts, OCR) and small reports |
| `tools/thumb_preview.py` | The feed preview rig: light and dark feed, several sizes, badge, grayscale, blur, safe zones |
| `tools/scenes.py`, `lib.py`, `render.py`, `fonts/` | The mockup generator (needs a headless Chromium) |
| `tools/build_master.py` | The script that assembles this file from the sources above |
| `tools/build_ai.py` | The script that assembles `STRESS-RISER-AI.md` (Python 3 only; its own front matter is in `master/ai/`) |

**Preview tool usage:** `python3 tools/thumb_preview.py image.png --title "…" --duration 10:24 --safezone` (needs Pillow).

**Rebuilding this file:** `python3 tools/build_master.py` (needs the Python package `markdown`; images and data are read from the folders above).

**Commits:** `c9fc437` brief stored; `475dc9c` research, ten styles, gallery, tools; `cfc1310` corrections after the first two independent reviews; `dfcadcd` this master file; the commit after it applies the third review (E3).
