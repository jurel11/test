# Stress Riser

This repository is the workspace for **Stress Riser**, a YouTube channel of documentary-style engineering-disaster stories: English voiceover, hand-drawn stick-figure animation. Whenever a task concerns the channel — a script, title, description, thumbnail, scene list, image prompt or video idea — follow the full channel brief below.

Talk to the user in the language they write in (so far Slovenian). Everything that goes into the channel itself — voiceover, titles, descriptions — is always English.

@stress-riser/channel-brief.md

For thumbnails (styles, text overlay rules, testing, image-generation prompts, evidence) read `stress-riser/thumbnail-styles.md` first; mockups are in `stress-riser/thumbnails/` and viewable in `stress-riser/thumbnail-lookbook.html`. Research notes with sources are in `stress-riser/research/`.

For titles (evidence, the eight title formulas, the 36-title bank for the twelve candidate stories, Shorts titles, testing) read `stress-riser/title-research.md` first; `python3 stress-riser/tools/title_check.py "Why did ...?"` checks a title against the brief's rules. Its data is in `stress-riser/data/title-*`.

The whole thumbnail research (all findings, numbers, recommendations, the ten styles, every agent report and review, data tables and sources) is gathered in `stress-riser/STRESS-RISER-MASTER.html`. It is large (about 3 MB with embedded images): do not read it into context; its text sources are in `stress-riser/master/`, `stress-riser/research/` and `stress-riser/thumbnail-styles.md`, and `stress-riser/tools/build_master.py` rebuilds it.

For an AI to read, use the plain-Markdown edition `stress-riser/STRESS-RISER-AI.md` (about 50,000 words, no images, layered from the most to the least important, with a map with line numbers at the top): read the sections you need, not necessarily the whole file. `stress-riser/tools/build_ai.py` rebuilds it.

The `isotrack-*.html` files in this repository are unrelated to the channel; the brief does not apply to them.
