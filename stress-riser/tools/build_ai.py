#!/usr/bin/env python3
"""Assemble stress-riser/STRESS-RISER-AI.md: the research as ONE plain-Markdown file that an AI reads easily.

Same research as the HTML dossier (tools/build_master.py), but: no images, no HTML, no scripts; layered from the
most important content to the least important; a map with line numbers at the top; rules repeated at the end.
Python 3 only (no packages).

Inputs (all inside the repository folder stress-riser/):
  master/ai/*.md          new front matter: read-first, core card, compact review status, final reminders, file map
  thumbnail-styles.md     the corrected report of the ten styles (Part C)
  master/B1..B5*.md       the synthesis (Part B)
  master/reports/*.md     the eight final research reports (Part D)
  data/*.md, data/*.csv   palette, font and experiment tables (Part F)
  channel-brief.md        the brief, verbatim (Part R1)
  master/H4-glossary.md   glossary (Part R3)
Output: STRESS-RISER-AI.md
Left out on purpose (see 0.4 in the output): reviewers' reports, raw notes, agent prompts, the two 400-row video
indexes, the consolidated source list, images.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
M = os.path.join(ROOT, "master")
AI = os.path.join(M, "ai")
OUT = os.path.join(ROOT, "STRESS-RISER-AI.md")

FENCE = re.compile(r"^\s*(```|~~~)")
HEAD = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


def read(*p):
    return open(os.path.join(*p), encoding="utf-8").read()


def words(md):
    return len(re.findall(r"\S+", md))


# ----------------------------------------------------------------------------- markdown helpers
def each_line(md, fn):
    """fn(line, in_fence) -> replacement line or None (drop). Fence lines are kept untouched."""
    out, inf = [], False
    for line in md.split("\n"):
        if FENCE.match(line):
            inf = not inf
            out.append(line)
            continue
        new = fn(line, inf)
        if new is not None:
            out.append(new)
    return "\n".join(out)


def shift(md, delta):
    def f(line, inf):
        m = HEAD.match(line)
        if inf or not m:
            return line
        return "#" * min(6, max(1, len(m.group(1)) + delta)) + " " + m.group(2)
    return each_line(md, f)


def drop_h1(md):
    lines, inf = md.split("\n"), False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            inf = not inf
        m = HEAD.match(line)
        if not inf and m and len(m.group(1)) == 1:
            del lines[i]
            if i < len(lines) and not lines[i].strip():
                del lines[i]
            break
    return "\n".join(lines)


def drop_rules(md):
    """Horizontal rules (---) are visual noise in a plain-text knowledge file."""
    return each_line(md, lambda line, inf: None if (not inf and line.strip() == "---") else line)


SCRATCH_NOTES = re.compile(r"/tmp/claude-0/[^\s)]*?/scratchpad/research/([a-z-]+)/notes\.md")
SCRATCH_DIR = re.compile(r"/tmp/claude-0/[^\s)]*?/scratchpad/research/([a-z-]+)/?")


def clean(md):
    md = SCRATCH_NOTES.sub(lambda m: f"research/{m.group(1)}.md", md)
    md = SCRATCH_DIR.sub(lambda m: f"research/{m.group(1)}/", md)
    return md.replace("\r", "")


def nest_story_bullets(md):
    """The story report uses '1. TITLE' followed by '- fact' lines at column 0: indent the bullets under the item."""
    out, in_item = [], False
    for line in md.split("\n"):
        if re.match(r"^\d+\.\s+[A-Z]", line):
            in_item = True
            out.append(line)
            continue
        if in_item and line.startswith("- "):
            out.append("    " + line)
            continue
        if in_item and line.strip() == "":
            out.append(line)
            continue
        if in_item and not line.startswith(" "):
            in_item = False
        out.append(line)
    return "\n".join(out)


def sub_once(text, old, new, what):
    if text.count(old) != 1:
        sys.exit(f"build_ai: expected exactly one match for {what!r}, found {text.count(old)}")
    return text.replace(old, new)


# ----------------------------------------------------------------------------- the parts
def part_a():
    return "## A. Core card: read this even if you read nothing else\n\n" + read(AI, "A-core-card.md").strip() + "\n"


def part_c():
    md = read(ROOT, "thumbnail-styles.md")
    md = drop_h1(md)
    md = re.sub(r"(?m)^## (\d+)\. ", lambda m: f"## C{m.group(1)}. ", md)
    md = shift(drop_rules(clean(md)), 1)
    return ("## C. The ten thumbnail styles: house system, evidence, testing playbook, fact registry (C1 to C12)\n\n"
            + md.strip() + "\n")


def part_b():
    b1 = drop_h1(read(M, "B1-context-and-method.md"))
    b1 = sub_once(b1, "parts D to G are the underlying reports and data.",
                  "Part D holds the underlying reports and Part F the data tables (raw notes, reviews and indexes are not in this edition: see 0.4).",
                  "B1 intro sentence")
    chunks = [shift(clean(b1), 1)]
    for n in ("B2-key-numbers", "B3-myths-and-contradictions", "B4-recommendations", "B5-roadmap-risks-decisions"):
        chunks.append(shift(clean(read(M, n + ".md")), 1))
    chunks.append(read(AI, "B6-status.md"))
    return ("## B. Synthesis: key numbers, myths, contradictions, recommendations, roadmap, risks\n\n"
            + "\n\n".join(c.strip() for c in chunks) + "\n")


D_LIST = [("D1", "platform", "Platform mechanics, specs, policies and testing"),
          ("D2", "ctr-evidence", "Empirical evidence on what gets thumbnails clicked"),
          ("D3", "psychology", "Psychology and visual perception of clicking"),
          ("D4", "niche-audit", "Audit of the engineering-disaster and documentary niche"),
          ("D5", "cartoon-audit", "Audit of cartoon and stick-figure explainer channels"),
          ("D6", "design-system", "Design system, color math and production workflow"),
          ("D7", "story-visuals", "From story to thumbnail moment (fact-checked)"),
          ("D8", "packaging", "Packaging, title-thumbnail pairing, testing and Shorts")]


def part_d():
    out = ["## D. The eight research reports (verbatim source layer)\n\n"
           "These are the final reports of the eight research agents, unedited except that long scratch-folder paths were shortened. "
           "They were written before the reviews. Where they disagree with Parts A, B, C or F, those parts win (known conflicts: B3.2). "
           "Read them for detail, quotations and the source list at the end of each report."]
    for id_, slug, title in D_LIST:
        md = read(M, "reports", slug + ".md")
        if slug == "story-visuals":
            md = nest_story_bullets(md)
        md = shift(drop_rules(clean(drop_h1(md))), 2)
        out.append(f"### {id_}. {title}\n\n" + md.strip())
    return "\n\n".join(out) + "\n"


def verdict(dl):
    dl = float(dl)
    return "text-safe" if dl >= 50 else "big bold text" if dl >= 40 else "big shapes + outline" if dl >= 25 else "invisible (hue only)"


def palette_with_use(md):
    """Add a 'use' column (the lightness-gap rule of B4.3) to the 45-pair table."""
    out, in_pairs = [], False
    for line in md.split("\n"):
        if line.startswith("| pair |"):
            in_pairs = True
            out.append(line + " use |")
            continue
        if in_pairs and line.startswith("|---"):
            out.append(line + "---|")
            continue
        if in_pairs and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append(line + f" {verdict(cells[2])} |")
            continue
        if in_pairs and not line.startswith("|"):
            in_pairs = False
        out.append(line)
    return "\n".join(out)


def part_f():
    d = os.path.join(ROOT, "data")
    pal = palette_with_use(read(d, "palette-report.md"))
    pal = shift(pal, 2)
    fonts = read(d, "font-metrics.md").strip()
    n_fonts = sum(1 for l in fonts.split("\n") if l.startswith("|")) - 2
    exp = shift(read(d, "experiments-report.md"), 2)
    cvd = shift(read(d, "color-blindness-report.md"), 2)
    with open(os.path.join(d, "ocr-legibility.csv"), encoding="utf-8") as fh:
        ocr = fh.read().strip()
    parts = ["## F. Data tables: palette math, fonts, legibility experiments (F1 to F3)\n\n"
             "F4 and F5 (the two video indexes) and F6 (phone-size QA sheet) are not in this edition (see 0.4).",
             "### F1. Palette pairs and single-color values\n\n"
             "Color names: grn_l = light green #8fbf5a, grn_d = dark green #4f7d3a. WCAG = contrast ratio; dL* = lightness difference (CIELAB); "
             "dE2000 = color difference; Lc = APCA contrast (a/b: a is the text, b the background; negative = light on dark); "
             "protan, deutan, tritan = dE2000 as seen with that color-vision deficiency. "
             "The 'use' column applies the rule of B4.3: a lightness gap of 50 or more is text-safe, 40 to 50 suits big bold text, 25 to 40 big flat shapes with an outline, under 25 is invisible by lightness.\n\n"
             + pal.strip(),
             f"### F2. Font measurements\n\nMetrics of {n_fonts} display fonts measured by the design agent (source: `data/font-metrics.csv`). "
             "'max cap px' is the largest cap height at which the line WHY DID IT FAIL? fits on one line in 1152 px (the 1280 master minus the 64 px margins). Lilita One is the recommended font (B4.4).\n\n" + fonts,
             "### F3. Legibility, saliency and color-blindness experiments\n\n" + exp.strip() + "\n\n" + cvd.strip()
             + "\n\n#### D. OCR legibility proxy (data/ocr-legibility.csv)\n\n"
             "A machine proxy, not a human study: RapidOCR was run on a thumbnail with white text and a 12% ink outline, downscaled to the target size (168x94, 246x138, 360x202). "
             "Six test words (WHY, FELL, BROKE, WHO?, CRACK, SNAP) were scored; 5 is the practical maximum because 'WHO?' is usually misread. "
             "Columns capNN are the cap height in px on the 1280 master.\n\n```csv\n" + ocr + "\n```"]
    return "\n\n".join(parts) + "\n"


def part_r():
    brief = shift(drop_rules(drop_h1(read(ROOT, "channel-brief.md"))), 2)
    file_map = read(AI, "H3-file-map.md").strip()
    gloss = sub_once(read(M, "H4-glossary.md"), "## H4. Glossary", "## R3. Glossary", "glossary heading")
    gloss = shift(gloss, 1)
    return ("## R. Reference: the channel brief (verbatim), file map, glossary (R1 to R3)\n\n"
            "### R1. The channel brief (verbatim; it overrides everything else)\n\n" + brief.strip() + "\n\n"
            + file_map + "\n\n" + gloss.strip() + "\n")


def part_z():
    return "## Z. Final reminders\n\n" + read(AI, "Z-final-reminders.md").strip() + "\n"


# ----------------------------------------------------------------------------- map and checks
def headings(text):
    out, inf = [], False
    for n, line in enumerate(text.split("\n"), 1):
        if FENCE.match(line):
            inf = not inf
        m = HEAD.match(line)
        if m and not inf:
            out.append((n, len(m.group(1)), m.group(2)))
    return out


def make_map(text):
    hs = headings(text)
    rows = []
    for i, (n, lvl, title) in enumerate(hs):
        if lvl not in (2, 3) or title.startswith("0.") or title.startswith("0 "):
            continue
        end = len(text.split("\n"))
        for n2, lvl2, _ in hs[i + 1:]:
            if lvl2 <= lvl:
                end = n2 - 1
                break
        w = words("\n".join(text.split("\n")[n - 1:end]))
        rows.append(f"L{n:<6d}{'  ' if lvl == 3 else ''}{'#' * lvl} {title} ({w:,} words)")
    return "```text\n" + "\n".join(rows) + "\n```"


def main():
    front = read(AI, "0-read-first.md").strip()
    # the brief comes right after the core card because it overrides everything else
    body = "\n\n".join([part_a(), part_r(), part_c(), part_b(), part_d(), part_f(), part_z()])
    text = front + "\n\n" + body
    text = re.sub(r"\n{3,}", "\n\n", text)
    # two passes: the map has the same number of lines whatever the numbers are
    text1 = text.replace("{{MAP}}", make_map(text.replace("{{MAP}}", "")))
    text2 = text.replace("{{MAP}}", make_map(text1))
    final = text.replace("{{MAP}}", make_map(text2))
    # the map must describe the final file: verify the fixed point
    if make_map(final) != make_map(text2):
        sys.exit("build_ai: map did not converge")
    open(OUT, "w", encoding="utf-8").write(final.rstrip("\n") + "\n")
    w, c = words(final), len(final)
    print(f"wrote {OUT}  {c/1e3:,.0f} KB  words={w:,}  lines={final.count(chr(10)):,}  approx tokens={int(c/3.9):,}")


if __name__ == "__main__":
    main()
