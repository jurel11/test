#!/usr/bin/env python3
"""Assemble stress-riser/STRESS-RISER-MASTER.html: one self-contained page with the whole dossier.

Inputs (all inside the repository folder stress-riser/):
  master/*.md             summary (Slovenian), synthesis B1-B6, research briefs, glossary, file map
  master/reports/*.md     the eight final research reports and the three review reports (verbatim)
  thumbnail-styles.md     the corrected report of the ten styles (Part C)
  research/*.md           the eight agents' raw working notes (Part G)
  data/*.csv, data/*.md   tables and small reports (Part F)
  thumbnails/             mockups, art-only layers, phone-size QA sheet
  channel-brief.md        the brief, verbatim
Needs: Python 3, the 'markdown' package; Pillow and numpy for the mockup measurements.
"""
import base64, csv, datetime, glob, html, os, re, sys
from collections import Counter, OrderedDict
from urllib.parse import urlparse

import markdown
from markdown.extensions import Extension

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
M = os.path.join(ROOT, "master")
OUT = os.path.join(ROOT, "STRESS-RISER-MASTER.html")
BUILT = "2026-10-01"
RESEARCHED = "2026-09-30"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def words(text):
    return len(re.findall(r"\w+", text))


# ----------------------------------------------------------------------------- markdown helpers
FENCE = re.compile(r"^(```|~~~)")


def heading_levels(md):
    inf, lv = False, []
    for line in md.split("\n"):
        if FENCE.match(line):
            inf = not inf
        if not inf:
            m = re.match(r"^(#{1,6})\s", line)
            if m:
                lv.append(len(m.group(1)))
    return lv


def demote(md, shift=0, base=None, drop_h1=False):
    """Shift heading levels (outside code fences). base: make the smallest level in the file equal to base."""
    if base is not None:
        lv = heading_levels(md)
        shift = base - (min(lv) if lv else base)
    out, inf, dropped = [], False, False
    for line in md.split("\n"):
        if FENCE.match(line):
            inf = not inf
        if not inf:
            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                lvl = len(m.group(1))
                if drop_h1 and lvl == 1 and not dropped:
                    dropped = True
                    continue
                line = "#" * min(6, max(1, lvl + shift)) + " " + m.group(2)
        out.append(line)
    return "\n".join(out)


def normalize_lists(md):
    """Python-Markdown needs 4 spaces for nested lists; many notes use 2 or 3."""
    out, inf = [], False
    for line in md.split("\n"):
        if FENCE.match(line):
            inf = not inf
        if not inf:
            m = re.match(r"^( {2,3})([-*+]|\d+\.)\s", line)
            if m:
                line = "    " + line[len(m.group(1)):]
            else:
                m = re.match(r"^( {4,7})([-*+]|\d+\.)\s", line)
                if m and len(m.group(1)) < 8:
                    line = "        " + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def blank_before_lists(md):
    """Python-Markdown only starts a list after a blank line; the reviews put '1. ...' straight under a heading line."""
    out, inf, in_list = [], False, False
    for line in md.split("\n"):
        if FENCE.match(line):
            inf = not inf
        item = (not inf) and bool(re.match(r"^\d+\.\s", line))
        if item and not in_list and out and out[-1].strip():
            out.append("")
        if item:
            in_list = True
        elif line.strip() and not line.startswith(" "):
            in_list = False
        out.append(line)
    return "\n".join(out)


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


def slug_factory(prefix):
    def _s(value, sep="-"):
        base = re.sub(r"[^\w\s-]", "", value.lower()).strip()
        base = re.sub(r"[\s_-]+", sep, base)
        return (prefix + sep + base)[:90]
    return _s


SCRATCH_NOTES = re.compile(r"/tmp/claude-0/[^\s)]*?/scratchpad/research/([a-z-]+)/notes\.md")
SCRATCH_DIR = re.compile(r"/tmp/claude-0/[^\s)]*?/scratchpad/research/([a-z-]+)/?")


def clean_paths(md):
    md = SCRATCH_NOTES.sub(lambda m: f"research/{m.group(1)}.md", md)
    md = SCRATCH_DIR.sub(lambda m: f"research/{m.group(1)}/", md)
    # the reviewers' prompts name their scratch folders and the agents' transcripts
    md = re.sub(r"/tmp/claude-0/[^/\s]+/[0-9a-f-]{36}/scratchpad/", "<scratchpad>/", md)
    return re.sub(r"/tmp/claude-0/[^/\s]+/[0-9a-f-]{36}/tasks/", "<agent-transcripts>/", md)


def autolink(h):
    def repl(m):
        if m.group(1) or m.group(2):
            return m.group(0)
        url, trail = m.group(3), ""
        while url and url[-1] in ".,;:)!?":
            trail, url = url[-1] + trail, url[:-1]
        return f'<a href="{url}" target="_blank" rel="noopener">{url}</a>{trail}'
    return re.sub(r'(<a\b[^>]*>.*?</a>)|(<[^>]+>)|(https?://[^\s<>"\']+)', repl, h, flags=re.S)


class EscapeHtml(Extension):
    """The notes quote placeholders such as <title> and <img>: show them as text, never as markup.
    (An unescaped <title> swallows the rest of the page, scripts included.)"""

    def extendMarkdown(self, md):
        md.preprocessors.deregister("html_block")
        md.inlinePatterns.deregister("html")


def to_html(md, prefix, nl2br=False):
    md = clean_paths(md)
    exts = [EscapeHtml(), "tables", "fenced_code", "sane_lists", "toc"]
    if nl2br:
        exts.append("nl2br")
    conv = markdown.Markdown(extensions=exts, extension_configs={"toc": {"slugify": slug_factory(prefix)}})
    h = conv.convert(md)
    h = h.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    h = re.sub(r"<td>(#[0-9a-fA-F]{6})</td>", r'<td><span class="sw" style="background:\1"></span>\1</td>', h)
    return autolink(h)


# ----------------------------------------------------------------------------- document model
toc = []          # (level, id, title, words)
chapters_html = []
stats = Counter()


def add_toc(level, id_, title, w=None):
    toc.append((level, id_, title, w))


def heading_ids(h, level):
    """Collect (id, text) for headings of the given level in a rendered fragment."""
    res = []
    for m in re.finditer(r'<h%d id="([^"]+)">(.*?)</h%d>' % (level, level), h, flags=re.S):
        res.append((m.group(1), re.sub(r"<[^>]+>", "", m.group(2))))
    return res


def open_chapter(id_, title, body_html, w, folded=True, label=None):
    tag = "details" if folded else "section"
    summ = f'<summary><h3 id="{id_}-h">{html.escape(title)}</h3><span class="wc">{label or f"{w:,} words"}</span></summary>' if folded else f'<h3 id="{id_}-h">{html.escape(title)}</h3>'
    open_attr = "" if folded else ""
    return f'<{tag} class="chapter" id="{id_}"{open_attr}>{summ}<div class="chbody">{body_html}</div></{tag}>'


def part_header(id_, label, title, blurb):
    return (f'<header class="partheader" id="{id_}"><div class="plabel">{html.escape(label)}</div>'
            f'<h2>{html.escape(title)}</h2><p>{blurb}</p></header>')


# ----------------------------------------------------------------------------- images
def figure(path, caption):
    return (f'<figure><img loading="lazy" alt="{html.escape(caption)}" src="data:image/png;base64,{b64(path)}">'
            f'<figcaption>{html.escape(caption)}</figcaption></figure>')


def style_block(n):
    comp = [p for p in sorted(glob.glob(os.path.join(ROOT, "thumbnails", f"{n:02d}-*.png"))) if not p.endswith("-art.png")]
    art = sorted(glob.glob(os.path.join(ROOT, "thumbnails", "art-only", f"{n:02d}-*-art.png")))
    parts = []
    if comp:
        parts.append(figure(comp[0], "Final composite: picture plus the text overlay"))
        stats["images"] += 1
    if art:
        parts.append(figure(art[0], "Art-only layer: what an image generator would produce (no words)"))
        stats["images"] += 1
    return '<div class="mockups">' + "".join(parts) + "</div>"


# ----------------------------------------------------------------------------- Part A
parts_out = []

cover = f'''
<section class="cover" id="top">
  <div class="kicker">Stress Riser</div>
  <h1>Master dossier: thumbnails, packaging and everything we learned</h1>
  <p class="sub">One file with the findings, the numbers, the recommendations, the ten thumbnail styles, every research report, the independent reviews, the data and the sources.</p>
  <p class="meta">Compiled {BUILT} · research carried out {RESEARCHED} · English, with a summary in Slovenian (Part A)</p>
  <div class="grades"><b>Evidence grades:</b>
    <span class="g">A</span> official documentation, peer-reviewed or a large dataset ·
    <span class="g">B</span> first-hand data from a creator or company, a correlational dataset, or a measurement by an agent ·
    <span class="g">C</span> opinion, vendor blog or inference ·
    <b>UNVERIFIED</b> could not be confirmed</div>
  <div class="jump"><a href="#A">Povzetek (SL)</a><a href="#B4">All recommendations</a><a href="#C5">The ten styles</a><a href="#B3">Myths</a><a href="#F4">Data tables</a><a href="#H1">Sources</a></div>
  <div class="statstrip" id="statstrip"></div>
</section>'''

summary_md = demote(read(os.path.join(M, "A-summary-sl.md")), shift=1, drop_h1=True)
a_html = to_html(summary_md, "a")
add_toc(1, "A", "A. Povzetek v slovenščini", words(summary_md))
for id_, t in heading_ids(a_html, 3):
    add_toc(2, id_, t)
parts_out.append(part_header("A", "Part A", "Povzetek v slovenščini", "Kratek pregled za odločanje: ugotovitve, stili, priporočila, odločitve in načrt. Ostalo je v angleščini."))
parts_out.append(f'<div class="prose">{a_html}</div>')

# ----------------------------------------------------------------------------- Part B
parts_out.append(part_header("B", "Part B", "Master synthesis", "Context and method, the key numbers, myths and contradictions, all recommendations, the roadmap, and the review and spend log."))
add_toc(1, "B", "B. Master synthesis")
b_files = ["B1-context-and-method", "B2-key-numbers", "B3-myths-and-contradictions", "B4-recommendations", "B5-roadmap-risks-decisions", "B6-review-audit-and-spend"]
for name in b_files:
    md = demote(normalize_lists(read(os.path.join(M, name + ".md"))), shift=1, drop_h1=True)
    h = to_html(md, name[:2].lower())
    sec_id = name[:2]
    ttl = heading_ids(h, 3)
    parts_out.append(f'<section class="prose chapter-open" id="{sec_id}">{h}</section>')
    if ttl:
        add_toc(2, sec_id, ttl[0][1], words(md))
        for id_, t in ttl[1:]:
            pass
    for id_, t in heading_ids(h, 4):
        if name in ("B4-recommendations", "B5-roadmap-risks-decisions", "B6-review-audit-and-spend", "B1-context-and-method", "B2-key-numbers", "B3-myths-and-contradictions"):
            add_toc(3, id_, t)

# ----------------------------------------------------------------------------- Part C
parts_out.append(part_header("C", "Part C", "The ten thumbnail styles (the corrected report)", "The report as corrected after the independent reviews: constraints, evidence, the house system, the ten styles with mockups, the phone-size results, the testing playbook, the fact registry, decisions, Shorts and caveats. Section numbers C1 to C12 are referred to throughout this file."))
add_toc(1, "C", "C. The ten thumbnail styles")
c_md = read(os.path.join(ROOT, "thumbnail-styles.md"))
c_md = re.sub(r"(?m)^## (\d+)\. ", lambda m: f"## C{m.group(1)}. ", c_md)
style_blocks = {}


def inject_style_block(m):
    key = f"STYLEBLOCKTOKEN{int(m.group(2))}X"
    style_blocks[key] = style_block(int(m.group(2)))
    return m.group(1) + "\n\n" + key + "\n"


c_md = re.sub(r"(?m)^(### Style (\d+) .*)$", inject_style_block, c_md)
c_md = demote(normalize_lists(c_md), shift=1, drop_h1=True)
c_html = to_html(c_md, "c")
for key, block in style_blocks.items():
    assert f"<p>{key}</p>" in c_html, key
    c_html = c_html.replace(f"<p>{key}</p>", block)
c_html = re.sub(r'<h3 id="c-c(\d+)-[^"]*">', lambda m: f'<h3 id="C{m.group(1)}">', c_html)
parts_out.append(f'<section class="prose" id="Cbody">{c_html}</section>')
for id_, t in heading_ids(c_html, 3):
    add_toc(2, id_, t)
    if t.startswith("C5."):
        for sid, st in heading_ids(c_html, 4):
            if st.startswith("Style "):
                add_toc(3, sid, st)

# ----------------------------------------------------------------------------- Part D (final reports)
parts_out.append(part_header("D", "Part D", "The eight research reports", "The final report of each research agent, verbatim (up to about 1,500 words each, with evidence grades, sources and caveats). Click a chapter to open it."))
add_toc(1, "D", "D. The eight research reports")
d_list = [("D1", "platform", "D1. Platform mechanics, specs, policies and testing"),
          ("D2", "ctr-evidence", "D2. Empirical evidence on what gets thumbnails clicked"),
          ("D3", "psychology", "D3. Psychology and visual perception of clicking"),
          ("D4", "niche-audit", "D4. Audit of the engineering-disaster and documentary niche"),
          ("D5", "cartoon-audit", "D5. Audit of cartoon and stick-figure explainer channels"),
          ("D6", "design-system", "D6. Design system, color math and production workflow"),
          ("D7", "story-visuals", "D7. From story to thumbnail moment (fact-checked)"),
          ("D8", "packaging", "D8. Packaging, title-thumbnail pairing, testing and Shorts")]
for id_, slug, title in d_list:
    md = read(os.path.join(M, "reports", slug + ".md"))
    if slug == "story-visuals":
        md = nest_story_bullets(md)
    md = demote(normalize_lists(md), base=4, drop_h1=False) if heading_levels(md) else md
    h = to_html(md, id_.lower(), nl2br=True)
    parts_out.append(open_chapter(id_, title, h, words(md)))
    add_toc(2, id_, title, words(md))

# ----------------------------------------------------------------------------- Part E (reviews)
parts_out.append(part_header("E", "Part E", "The three independent reviews", "The full reports of three reviewers, verbatim: two audited the first draft (E1 facts and claims, E2 brief compliance and design) and a third checked the master synthesis in Part B against the reports and data (E3). The status of every finding is in B6."))
add_toc(1, "E", "E. The three independent reviews")
for id_, slug, title in (("E1", "review-factcheck", "E1. Reviewer 1: fact and claim audit"), ("E2", "review-design", "E2. Reviewer 2: brief compliance and design critique"), ("E3", "review-synthesis", "E3. Reviewer 3: check of the master synthesis")):
    md = normalize_lists(blank_before_lists(read(os.path.join(M, "reports", slug + ".md"))))
    md = demote(md, base=4) if heading_levels(md) else md
    h = to_html(md, id_.lower(), nl2br=True)
    parts_out.append(open_chapter(id_, title, h, words(md)))
    add_toc(2, id_, title, words(md))

# ----------------------------------------------------------------------------- Part F (data)
parts_out.append(part_header("F", "Part F", "Data tables and measurements", "The palette math, the font and legibility measurements, the two video indexes (searchable and sortable), and the measurements of the ten mockups."))
add_toc(1, "F", "F. Data tables and measurements")


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def simple_table(headers, rows, cls="data nw"):
    th = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tablewrap"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def sw(hexv):
    return f'<span style="white-space:nowrap"><span class="sw" style="background:{hexv}"></span>{hexv}</span>'


# F1 palette pairs
pp = read_csv(os.path.join(ROOT, "data", "palette-pairs.csv"))


def verdict(dl):
    dl = float(dl)
    return "text-safe" if dl >= 50 else "big bold text" if dl >= 40 else "big shapes + outline" if dl >= 25 else "invisible (hue only)"


rows = [[html.escape(r["a"]) + " / " + html.escape(r["b"]), sw(r["hexa"]), sw(r["hexb"]), r["wcag"], r["dL"], r["dE2000"], r["apca_a_on_b"], r["dE2000_min_cvd"], verdict(r["dL"])] for r in pp]
f1 = ('<p>All 45 pairs of the ten palette colors. <b>WCAG</b> is the contrast ratio; <b>ΔL*</b> the lightness difference; <b>ΔE2000</b> the color difference; <b>APCA</b> the newer contrast measure (negative = light on dark); the last numeric column is the worst ΔE2000 across the three color-blindness simulations. The verdict uses the rule in B4.3: gap of 50 or more text-safe, 40–50 big bold text, 25–40 big shapes with an outline, under 25 invisible by lightness.</p>'
      + simple_table(["Pair", "A", "B", "WCAG", "ΔL*", "ΔE2000", "APCA (A on B)", "Worst ΔE2000 (color-blind)", "Use"], rows)
      + to_html(demote(read(os.path.join(ROOT, "data", "palette-report.md")), base=5), "f1r"))
parts_out.append(open_chapter("F1", "F1. Palette pairs and single-color values", f1, words(f1)))
add_toc(2, "F1", "F1. Palette pairs and single-color values")

# F2 fonts
fm = read_csv(os.path.join(ROOT, "data", "font-metrics.csv"))
hdr = list(fm[0].keys())
f2 = ('<p>Candidate display fonts measured on three sample phrases (width per cap-height, and the largest cap height that fits one line in 1,152 px). Lilita One is the primary recommendation (cap height 0.70 of the font size; about 143 px font size gives a 100 px cap height).</p>'
      + simple_table(hdr, [[html.escape(r[h]) for h in hdr] for r in fm])
      + to_html(demote(read(os.path.join(ROOT, "data", "font-metrics.md")), base=5), "f2r"))
parts_out.append(open_chapter("F2", "F2. Font measurements", f2, words(f2)))
add_toc(2, "F2", "F2. Font measurements")

# F3 OCR + experiments + color blindness
oc = read_csv(os.path.join(ROOT, "data", "ocr-legibility.csv"))
hdr = list(oc[0].keys())
f3 = ('<p>Text legibility measured by an OCR program at the feed sizes (a proxy for legibility, not a human study): the number of the three test phrases read correctly at each cap height on the 1280-wide master.</p>'
      + simple_table(hdr, [[html.escape(r[h]) for h in hdr] for r in oc])
      + "<h4>Saliency, compression and other experiments</h4>"
      + to_html(demote(read(os.path.join(ROOT, "data", "experiments-report.md")), base=5), "f3a")
      + "<h4>Color-blindness simulation</h4>"
      + to_html(demote(read(os.path.join(ROOT, "data", "color-blindness-report.md")), base=5), "f3b"))
parts_out.append(open_chapter("F3", "F3. Legibility, saliency and color-blindness experiments", f3, words(f3)))
add_toc(2, "F3", "F3. Legibility, saliency and color-blindness experiments")


# F4 / F5 video indexes
def num_views(s):
    s = (s or "").lower().replace("views", "").replace(",", "").strip()
    m = re.match(r"^([\d.]+)\s*([kmb]?)$", s)
    if not m:
        return ""
    v = float(m.group(1)) * {"": 1, "k": 1e3, "m": 1e6, "b": 1e9}[m.group(2)]
    return int(v)


def yt(vid):
    return f'<a href="https://www.youtube.com/watch?v={html.escape(vid)}" target="_blank" rel="noopener">{html.escape(vid)}</a>'


ni = read_csv(os.path.join(ROOT, "data", "niche-video-index.csv"))
rows = []
for r in ni:
    v = r.get("views_listed_on_channel_page") or ""
    rows.append(f'<tr><td>{html.escape(r["channel"])}</td><td>{html.escape(r["tier"])}</td><td>{html.escape(r["group"])}</td>'
                f'<td>{html.escape(r["title"])}</td><td class="nw" data-v="{num_views(v)}">{html.escape(v)}</td><td class="nw">{html.escape(r["age_listed"])}</td>'
                f'<td class="nw">{yt(r["video_id"])}</td><td class="nw">{html.escape(r["lum"])}</td><td class="nw">{html.escape(r["sat"])}</td><td class="nw">{html.escape(r["dark"])}</td><td class="nw">{html.escape(r["edge"])}</td></tr>')
f4 = (f'<p>{len(ni)} thumbnails from the niche audit (engineering disasters, documentaries and neighbors), as listed on channel pages on {RESEARCHED}. <b>Views are YouTube\'s rounded strings; compare only within a channel</b> (age, topic and channel size differ). <b>Group</b>: top = among the most-viewed, low = among the least-viewed recent uploads. The numeric columns come from the agent\'s image analysis (brightness 0–1, saturation, share of dark pixels, edge density). Type in the box to filter; click a column heading to sort.</p>'
      '<input class="filter" type="search" placeholder="Filter rows (channel, title, group…)" aria-label="Filter rows" data-target="t-niche"> <span class="rc" data-for="t-niche"></span>'
      '<div class="tablewrap tall"><table class="data sortable" id="t-niche"><thead><tr><th>Channel</th><th>Tier</th><th>Group</th><th>Title</th><th>Views (listed)</th><th>Age</th><th>Video</th><th>Bright</th><th>Sat</th><th>Dark</th><th>Edge</th></tr></thead><tbody>'
      + "".join(rows) + "</tbody></table></div>")
parts_out.append(open_chapter("F4", "F4. Niche video index (405 thumbnails)", f4, 0, label=f"{len(ni)} rows"))
add_toc(2, "F4", "F4. Niche video index (405 thumbnails)")

cv = read_csv(os.path.join(ROOT, "data", "cartoon-video-index.csv"))
rows = []
for r in cv:
    rows.append(f'<tr><td>{html.escape(r["channel"])}</td><td>{html.escape(r["subs_at_fetch"])}</td><td>{html.escape(r["group"])}</td><td>{html.escape(r["rank"])}</td>'
                f'<td>{html.escape(r["title"])}</td><td class="nw" data-v="{html.escape(r["views_num"])}">{html.escape(r["views_as_fetched"])}</td><td class="nw">{html.escape(r["published_as_fetched"])}</td>'
                f'<td class="nw">{html.escape(r["length"])}</td><td class="nw">{yt(r["video_id"])}</td></tr>')
f5 = (f'<p>{len(cv)} rows from the cartoon and stick-figure audit (52 channels), as fetched on {RESEARCHED}. <b>Group</b>: top = most-viewed, weak = the lowest-viewed of a channel\'s last 20 long-form uploads that are at least 21 days old. Compare views within a channel only. Type to filter; click a heading to sort.</p>'
      '<input class="filter" type="search" placeholder="Filter rows (channel, title, group…)" aria-label="Filter rows" data-target="t-cartoon"> <span class="rc" data-for="t-cartoon"></span>'
      '<div class="tablewrap tall"><table class="data sortable" id="t-cartoon"><thead><tr><th>Channel</th><th>Subscribers</th><th>Group</th><th>Rank</th><th>Title</th><th>Views</th><th>Published</th><th>Length</th><th>Video</th></tr></thead><tbody>'
      + "".join(rows) + "</tbody></table></div>")
parts_out.append(open_chapter("F5", "F5. Cartoon and stick-figure video index (462 rows)", f5, 0, label=f"{len(cv)} rows"))
add_toc(2, "F5", "F5. Cartoon and stick-figure video index (462 rows)")

# F6 mockup measurements + QA sheet
meas_rows = []
try:
    import numpy as np
    from PIL import Image
    PAL = {"INK": (26, 26, 26), "WHITE": (255, 255, 255), "PAPER": (243, 234, 216), "SKY": (191, 226, 234), "LG": (143, 191, 90),
           "DG": (79, 125, 58), "BR": (154, 107, 67), "TAN": (210, 180, 140), "AM": (230, 178, 58), "RED": (217, 74, 56)}
    pal = np.array(list(PAL.values()), dtype=int)
    for p in sorted(glob.glob(os.path.join(ROOT, "thumbnails", "[0-9][0-9]-*.png"))):
        if p.endswith("-art.png"):
            continue
        im = np.array(Image.open(p).convert("RGB")).astype(int)
        d = np.abs(im[:, :, None, :] - pal[None, None, :, :]).sum(-1).min(-1)
        exact = (d == 0).mean() * 100
        red = (np.abs(im - np.array(PAL["RED"])).sum(-1) == 0).mean() * 100
        z = im[630:720, 1050:1280].reshape(-1, 3)
        _, cnt = np.unique(z, axis=0, return_counts=True)
        meas_rows.append([html.escape(os.path.basename(p)), f"{exact:.1f}%", f"{red:.1f}%", f"{100 * (1 - cnt.max() / len(z)):.0f}%"])
except Exception as e:  # measurements are optional
    meas_rows = [[f"(measurement skipped: {html.escape(str(e))})", "", "", ""]]
qa_path = os.path.join(ROOT, "thumbnails", "qa-phone-sizes.png")
f6 = ('<p><b>Phone-size test.</b> Each row is one style: 360 px (light feed), 168 px (light), 168 px (dark feed), grayscale, blurred ("squint"). If the main word, the red accent and the silhouette survive the last two columns, the thumbnail reads. Strongest: Styles 6 and 10. For Styles 7, 8 and 9 the words carry the thumbnail and small props or details vanish at 168 px.</p>'
      + figure(qa_path, "The ten mockups at five sizes and modes") +
      '<h4>Measurements of the ten composites</h4><p><b>Exact palette</b>: share of pixels that are exactly one of the ten colors (the rest are one- or two-pixel blends at edges). <b>Red</b>: share of the frame in the accent color. <b>Badge-zone activity</b>: share of the bottom-right 230×90 px that differs from its dominant color (lower is clearer).</p>'
      + simple_table(["Composite", "Exact palette", "Red accent", "Badge-zone activity"], meas_rows))
stats["images"] += 1
parts_out.append(open_chapter("F6", "F6. Phone-size test and mockup measurements", f6, words(f6)))
add_toc(2, "F6", "F6. Phone-size test and mockup measurements")

# ----------------------------------------------------------------------------- Part G (raw notes)
parts_out.append(part_header("G", "Part G", "Raw research notes and the agents' exact instructions", "The working notes of the eight agents, copied unchanged, and the exact prompts each agent received. This is the most detailed record: every URL, quotation and grade, including dead ends."))
add_toc(1, "G", "G. Raw research notes and instructions")
g1 = to_html(demote(read(os.path.join(M, "G1-notes-intro.md")), base=4), "g1")
parts_out.append(open_chapter("G1", "G1. How to read the raw notes", g1, words(g1)))
add_toc(2, "G1", "G1. How to read the raw notes")
g2_md = demote(read(os.path.join(M, "G2-research-briefs.md")), base=4, drop_h1=False)
g2 = to_html(g2_md, "g2")
parts_out.append(open_chapter("G2", "G2. The exact instructions each agent received", g2, words(g2_md)))
add_toc(2, "G2", "G2. The exact instructions each agent received")
g_list = [("G3", "platform", "G3. Notes: platform mechanics, specs, policies"),
          ("G4", "ctr-evidence", "G4. Notes: CTR evidence"),
          ("G5", "psychology", "G5. Notes: psychology and perception"),
          ("G6", "niche-audit", "G6. Notes: niche audit"),
          ("G7", "cartoon-audit", "G7. Notes: cartoon and stick-figure audit"),
          ("G8", "story-visuals", "G8. Notes: story visuals (the fact base)"),
          ("G9", "design-system", "G9. Notes: design system and color math"),
          ("G10", "packaging", "G10. Notes: packaging, testing, Shorts")]
all_md_for_urls = []
for id_, slug, title in g_list:
    md = read(os.path.join(ROOT, "research", slug + ".md"))
    all_md_for_urls.append(md)
    md2 = demote(normalize_lists(md), base=4)
    h = to_html(md2, id_.lower())
    parts_out.append(open_chapter(id_, title, h, words(md)))
    add_toc(2, id_, title, words(md))

# ----------------------------------------------------------------------------- Part H
parts_out.append(part_header("H", "Part H", "Sources, the brief, file map and glossary", "The consolidated list of every web address cited anywhere in this file, the channel brief verbatim, the file map and tools, and a glossary."))
add_toc(1, "H", "H. Sources, brief, file map, glossary")

# H1 sources
corpus = []
for pth in glob.glob(os.path.join(M, "*.md")) + glob.glob(os.path.join(M, "reports", "*.md")) + glob.glob(os.path.join(ROOT, "research", "*.md")) + [os.path.join(ROOT, "thumbnail-styles.md")]:
    if os.path.basename(pth).startswith("G2-"):
        continue
    corpus.append(read(pth))
text_all = "\n".join(corpus)
urlre = re.compile(r"https?://[^\s<>\"')\]`]+")
TLD = r"(?:com|org|net|gov|edu|io|co\.uk|uk|tv|studio|blog|ai|app|int|eu|it|se|be|us|ca|au|de|info|ly|me|ws)"
barere = re.compile(r"(?<![\w@/.:-])((?:[a-z0-9][a-z0-9-]*\.)+" + TLD + r"/[^\s<>\"')\]`,;{}]*)", re.I)
urls = Counter()
for u in urlre.findall(text_all):
    u = u.rstrip(".,;:!?*")
    if "scratchpad" in u or "localhost" in u:
        continue
    urls[u] += 1
have = {re.sub(r"^https?://(www\.)?", "", u).rstrip("/") for u in urls}
for m in barere.finditer(text_all):
    u = m.group(1).rstrip(".,;:!?*…")
    key = re.sub(r"^www\.", "", u).rstrip("/")
    if key in have or u.endswith("/") and key.rstrip("/") in have:
        continue
    have.add(key)
    urls["https://" + u] += 1
bydom = OrderedDict()
for u, c in sorted(urls.items(), key=lambda kv: (urlparse(kv[0]).netloc.lower().removeprefix("www."), kv[0])):
    dom = urlparse(u).netloc.lower().removeprefix("www.")
    bydom.setdefault(dom, []).append((u, c))
items = []
for dom, lst in sorted(bydom.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    lis = "".join(f'<li><a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(u if len(u) < 130 else u[:127] + "…")}</a>' + (f' <span class="n">×{c}</span>' if c > 1 else "") + "</li>" for u, c in lst)
    items.append(f'<details class="dom"><summary><b>{html.escape(dom)}</b> <span class="n">{len(lst)} address{"es" if len(lst) != 1 else ""}</span></summary><ul>{lis}</ul></details>')

# DOIs and YouTube Help pages
dois = Counter(d.rstrip(".,;:)") for d in re.findall(r"\b(10\.\d{4,9}/[^\s)\]>,;\"'`]+)", text_all))
help_ids = Counter(re.findall(r"(?:support\.google\.com/youtube/answer/|Help (?:answer )?|Help pages? |answer )(\d{5,9})", text_all))
for m in re.finditer(r"(?:answer|Help)[^.\n]{0,40}?((?:\d{5,9})(?:\s*(?:,|and|/)\s*\d{5,9})+)", text_all):
    for n in re.findall(r"\d{5,9}", m.group(1)):
        help_ids[n] += 1


def listing(title, lis):
    return f"<h4>{html.escape(title)}</h4><ul>{lis}</ul>"


doi_html = listing(f"DOIs cited ({len(dois)})", "".join(f'<li><a href="https://doi.org/{html.escape(d)}" target="_blank" rel="noopener">{html.escape(d)}</a></li>' for d in sorted(dois)))
help_html = listing(f"YouTube Help pages cited by number ({len(help_ids)})", "".join(f'<li><a href="https://support.google.com/youtube/answer/{n}" target="_blank" rel="noopener">support.google.com/youtube/answer/{n}</a></li>' for n in sorted(help_ids)))


# the source lists exactly as each report gave them (studies, articles, documents, channels)
def extract_sources(md):
    lines = md.split("\n")
    for i, ln in enumerate(lines):
        if re.match(r"^(#{1,6}\s*)?(KEY )?SOURCES\b", ln.strip(), re.I):
            j = i + 1
            while j < len(lines):
                t = lines[j]
                if re.match(r"^#{1,6}\s", t) and j > i + 1:
                    break
                if re.match(r"^(CAVEATS|\*\*CAVEATS|Caveats)\b", t.strip()):
                    break
                j += 1
            return "\n".join(lines[i + 1:j]).strip()
    return ""


blocks = []
for id_, slug, title in d_list:
    src = extract_sources(read(os.path.join(M, "reports", slug + ".md")))
    if src:
        blocks.append(f"<h5>{html.escape(title)}</h5>" + to_html(normalize_lists(src), "s" + id_.lower()))
lists_html = "<h4>Source lists as given in each research report (studies, articles, documents, pages)</h4>" + "".join(blocks)
h1 = (f'<p>Everything cited in this file, gathered from every chapter. <b>Part 1</b> reproduces the source list at the end of each of the eight research reports (it includes papers, articles and documents that have no web address). <b>Part 2</b> lists all web addresses found in the text, grouped by site; <b>Part 3</b> all DOIs; <b>Part 4</b> the YouTube Help pages cited by number. Extraction is automatic; some addresses come from notes abbreviated by the agents, and a few pages could not be opened (see B1.5). The full detail of each citation is in the notes (Part G).</p>'
      + lists_html
      + f'<h4>All web addresses found ({sum(len(v) for v in bydom.values()):,} from {len(bydom)} sites)</h4>'
      '<input class="filter" type="search" placeholder="Filter sites…" aria-label="Filter sites" data-target="doms"> <div id="doms">' + "".join(items) + "</div>"
      + doi_html + help_html)
parts_out.append(open_chapter("H1", "H1. Consolidated sources", h1, words(re.sub(r"<[^>]+>", " ", h1))))
add_toc(2, "H1", "H1. Consolidated sources")
stats["urls"] = sum(len(v) for v in bydom.values()) + len(dois) + len(help_ids)

# H2 brief
hb = to_html(demote(read(os.path.join(ROOT, "channel-brief.md")), base=4), "h2")
parts_out.append(open_chapter("H2", "H2. The channel brief (verbatim)", hb, words(hb)))
add_toc(2, "H2", "H2. The channel brief (verbatim)")

# H3, H4
for id_, fname, title in (("H3", "H3-file-map.md", "H3. File map and tools"), ("H4", "H4-glossary.md", "H4. Glossary")):
    md = demote(read(os.path.join(M, fname)), base=4, drop_h1=False)
    h = to_html(md, id_.lower())
    parts_out.append(open_chapter(id_, title, h, words(md)))
    add_toc(2, id_, title)

# ----------------------------------------------------------------------------- assemble
total_words = sum(words(re.sub(r"<[^>]+>", " ", p)) for p in parts_out)
stats["words"] = total_words


def toc_html():
    out, cur = ['<ul class="toc">'], 1
    for lvl, id_, title, w in toc:
        cls = f"l{lvl}"
        wc = f' <span class="n">{w:,}</span>' if (w and lvl == 2 and w > 400) else ""
        out.append(f'<li class="{cls}"><a href="#{id_}" data-id="{id_}">{html.escape(title)}</a>{wc}</li>')
    out.append("</ul>")
    return "".join(out)


CSS = """
:root{--bg:#faf7f0;--card:#ffffff;--ink:#1a1a1a;--muted:#5b5648;--line:#ddd3bc;--accent:#d94a38;--link:#1d5f7d;--chip:#f1e9d4;--code:#f4eee0;--sw:#0001}
:root[data-theme="dark"]{--bg:#141311;--card:#1d1b18;--ink:#f1e9d6;--muted:#b6ad98;--line:#39352d;--accent:#ee7a68;--link:#7cc3de;--chip:#2a2722;--code:#25221e}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141311;--card:#1d1b18;--ink:#f1e9d6;--muted:#b6ad98;--line:#39352d;--accent:#ee7a68;--link:#7cc3de;--chip:#2a2722;--code:#25221e}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif}
a{color:var(--link)}
#bar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:10px;padding:8px 14px;background:var(--card);border-bottom:1px solid var(--line)}
#bar b{font-size:.95rem}
#bar .sp{flex:1}
#bar button{font:inherit;font-size:.85rem;padding:5px 10px;border:1px solid var(--line);border-radius:8px;background:var(--chip);color:var(--ink);cursor:pointer}
#layout{display:grid;grid-template-columns:310px minmax(0,1fr);max-width:1400px;margin:0 auto}
nav#side{position:sticky;top:48px;align-self:start;height:calc(100vh - 48px);overflow:auto;padding:14px 12px 40px;border-right:1px solid var(--line);font-size:.86rem}
nav#side ul{list-style:none;margin:0;padding:0}
nav#side li{margin:2px 0;line-height:1.35}
nav#side li.l1{margin-top:12px;font-weight:700}
nav#side li.l2{padding-left:10px}
nav#side li.l3{padding-left:22px;font-size:.8rem;color:var(--muted)}
nav#side a{text-decoration:none;color:inherit;display:block;padding:2px 6px;border-radius:5px}
nav#side a:hover,nav#side a.on{background:var(--chip);color:var(--accent)}
.n{color:var(--muted);font-size:.75rem}
main{padding:0 22px 80px;min-width:0}
.cover{padding:34px 0 12px}
.kicker{font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-size:.85rem}
.cover h1{font-size:clamp(1.8rem,4.2vw,2.8rem);line-height:1.12;margin:.2em 0 .3em}
.cover .sub{font-size:1.1rem;max-width:62ch}
.cover .meta{color:var(--muted)}
.grades{background:var(--chip);border-left:5px solid var(--accent);padding:10px 14px;border-radius:6px;margin:14px 0;max-width:80ch;font-size:.92rem}
.g{display:inline-grid;place-items:center;width:1.5em;height:1.5em;border-radius:50%;background:var(--accent);color:#fff;font-weight:700;font-size:.8rem}
.jump{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}
.jump a{padding:6px 12px;border:1px solid var(--line);border-radius:999px;background:var(--card);text-decoration:none;font-size:.9rem}
.jump a:hover{border-color:var(--accent)}
.statstrip{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0 4px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px 14px;min-width:120px}
.stat b{display:block;font-size:1.3rem}
.stat span{color:var(--muted);font-size:.8rem}
.partheader{margin:56px 0 12px;padding:18px 20px;background:var(--card);border:1px solid var(--line);border-left:6px solid var(--accent);border-radius:10px}
.partheader .plabel{font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);font-size:.78rem}
.partheader h2{margin:.1em 0 .2em;font-size:1.6rem}
.partheader p{margin:0;color:var(--muted);max-width:80ch}
.prose{max-width:92ch}
.prose h3{font-size:1.45rem;margin:2em 0 .4em;padding-top:.4em;border-top:2px solid var(--line)}
.prose h4{font-size:1.15rem;margin:1.6em 0 .3em}
.prose h5{font-size:1rem;margin:1.2em 0 .2em}
.prose p,.prose li{max-width:92ch}
.prose code,.chbody code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.88em}
.prose pre,.chbody pre{background:var(--code);padding:12px 14px;border-radius:8px;overflow:auto;font-size:.82rem;line-height:1.45;white-space:pre-wrap}
blockquote{margin:1em 0;padding:.4em 1em;border-left:4px solid var(--line);color:var(--muted);background:var(--chip);border-radius:0 6px 6px 0}
.tablewrap{overflow-x:auto;margin:1em 0;border:1px solid var(--line);border-radius:8px;background:var(--card)}
.tablewrap.tall{max-height:70vh;overflow:auto}
table.nw td,td.nw{white-space:nowrap}
table{border-collapse:collapse;width:100%;font-size:.86rem}
th,td{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:var(--chip);position:sticky;top:0;z-index:1;white-space:nowrap}
table.sortable th{cursor:pointer}
tr:hover td{background:var(--chip)}
.sw{display:inline-block;width:.95em;height:.95em;border-radius:3px;border:1px solid #0006;margin-right:.4em;vertical-align:-.12em}
details.chapter{margin:12px 0;background:var(--card);border:1px solid var(--line);border-radius:10px}
details.chapter>summary{cursor:pointer;list-style:none;padding:12px 16px;display:flex;align-items:baseline;gap:12px;justify-content:space-between}
details.chapter>summary::-webkit-details-marker{display:none}
details.chapter>summary::before{content:"▸";color:var(--accent);margin-right:6px}
details.chapter[open]>summary::before{content:"▾"}
details.chapter>summary h3{margin:0;font-size:1.12rem;flex:1}
.wc{color:var(--muted);font-size:.78rem;white-space:nowrap}
.chbody{padding:2px 18px 18px;overflow-wrap:anywhere}
.chbody h4{font-size:1.1rem;margin:1.4em 0 .3em}
.chbody h5{font-size:1rem;margin:1.1em 0 .2em}
.chbody h6{font-size:.95rem;margin:1em 0 .2em}
.chbody p,.chbody li{max-width:100ch}
.mockups{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:14px 0}
figure{margin:12px 0}
figure img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:8px;background:#fff}
figcaption{color:var(--muted);font-size:.82rem;margin-top:4px}
.filter{font:inherit;padding:6px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);min-width:min(100%,360px);margin-bottom:6px}
details.dom{border-bottom:1px solid var(--line);padding:4px 0}
details.dom ul{margin:.4em 0 .6em 1.4em;font-size:.85rem}
details.dom summary{cursor:pointer}
#menu{display:none}
@media (max-width:1000px){
  #layout{display:block}
  nav#side{position:fixed;top:48px;left:0;width:min(88vw,360px);height:calc(100vh - 48px);background:var(--card);transform:translateX(-102%);transition:transform .2s;z-index:30;box-shadow:2px 0 14px #0003}
  body.navopen nav#side{transform:none}
  #menu{display:inline-block}
  main{padding:0 14px 80px}
}
@media print{
  #bar,nav#side{display:none}
  #layout{display:block}
  details.chapter>*{display:block!important}
  .tablewrap.tall{max-height:none}
}
"""

JS = r"""
(function(){
  function $(s,r){return (r||document).querySelector(s)}
  function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
  var root=document.documentElement;
  try{var t=localStorage.getItem('sr-theme'); if(t) root.setAttribute('data-theme',t);}catch(e){}
  $('#theme').addEventListener('click',function(){
    var cur=root.getAttribute('data-theme');
    var dark=cur?cur==='dark':window.matchMedia('(prefers-color-scheme: dark)').matches;
    var nxt=dark?'light':'dark'; root.setAttribute('data-theme',nxt);
    try{localStorage.setItem('sr-theme',nxt)}catch(e){}
  });
  $('#menu').addEventListener('click',function(){document.body.classList.toggle('navopen')});
  var allOpen=false;
  $('#expand').addEventListener('click',function(){
    allOpen=!allOpen; $$('details.chapter').forEach(function(d){d.open=allOpen});
    this.textContent=allOpen?'Collapse all':'Expand all';
  });
  function openFor(el){var n=el; while(n&&n!==document.body){ if(n.tagName==='DETAILS') n.open=true; n=n.parentElement;}}
  function go(id,push){
    var el=document.getElementById(id); if(!el) return false;
    openFor(el); el.scrollIntoView(); if(push) history.replaceState(null,'','#'+id); return true;
  }
  document.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="#"]'); if(!a) return;
    var id=a.getAttribute('href').slice(1); if(go(id,true)){e.preventDefault(); document.body.classList.remove('navopen');}
  });
  window.addEventListener('hashchange',function(){go(location.hash.slice(1),false)});
  if(location.hash) setTimeout(function(){go(location.hash.slice(1),false)},50);
  // table filter + sort
  $$('input.filter').forEach(function(inp){
    var tgt=document.getElementById(inp.getAttribute('data-target'));
    var counter=$('.rc[data-for="'+inp.getAttribute('data-target')+'"]');
    function apply(){
      var q=inp.value.toLowerCase(), n=0, tot=0;
      if(tgt.tagName==='TABLE'){
        $$('tbody tr',tgt).forEach(function(r){tot++; var ok=!q||r.textContent.toLowerCase().indexOf(q)>-1; r.style.display=ok?'':'none'; if(ok)n++;});
        if(counter) counter.textContent=n+' of '+tot+' rows';
      } else {
        $$('details.dom',tgt).forEach(function(r){var ok=!q||r.textContent.toLowerCase().indexOf(q)>-1; r.style.display=ok?'':'none'; if(q&&ok) r.open=true;});
      }
    }
    inp.addEventListener('input',apply); apply();
  });
  $$('table.sortable').forEach(function(tb){
    var dir={};
    $$('th',tb).forEach(function(th,i){th.addEventListener('click',function(){
      var rows=$$('tbody tr',tb), asc=!dir[i]; dir[i]=asc;
      rows.sort(function(a,b){
        var x=a.children[i], y=b.children[i];
        var xv=x.getAttribute('data-v'), yv=y.getAttribute('data-v');
        var fx=xv!==null&&xv!==''?parseFloat(xv):parseFloat(x.textContent), fy=yv!==null&&yv!==''?parseFloat(yv):parseFloat(y.textContent);
        var r;
        if(!isNaN(fx)&&!isNaN(fy)) r=fx-fy; else r=x.textContent.localeCompare(y.textContent);
        return asc?r:-r;
      });
      var body=$('tbody',tb); rows.forEach(function(r){body.appendChild(r)});
    })});
  });
  // ToC highlight
  var links=$$('nav#side a'), map={};
  links.forEach(function(a){map[a.getAttribute('data-id')]=a});
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ links.forEach(function(a){a.classList.remove('on')}); var a=map[e.target.id]; if(a){a.classList.add('on'); a.scrollIntoView({block:'nearest'});} } });
    },{rootMargin:'-60px 0px -75% 0px'});
    Object.keys(map).forEach(function(id){var el=document.getElementById(id); if(el) io.observe(el);});
  }
  // stats strip
  var s=$('#statstrip'); if(s){ s.innerHTML=window.__stats.map(function(x){return '<div class="stat"><b>'+x[0]+'</b><span>'+x[1]+'</span></div>'}).join(''); }
})();
"""

stat_items = [
    [f"{stats['words']:,}", "words in this file"],
    ["11", "agents (8 research, 3 review)"],
    ["730", "research tool calls"],
    ["867", "real thumbnails downloaded"],
    ["45", "palette pairs computed"],
    [f"{stats['urls']:,}", "cited addresses, DOIs and Help pages"],
    ["10", "thumbnail styles"],
]
stats_js = "window.__stats=" + str(stat_items).replace("'", '"') + ";"

doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Stress Riser — master dossier</title>
<meta name="description" content="Master dossier for the Stress Riser channel: thumbnail research, ten styles, all reports, data and sources.">
<style>{CSS}</style></head>
<body>
<div id="bar"><button id="menu" aria-label="Contents">☰ Contents</button><b>Stress Riser · Master dossier</b><span class="sp"></span><button id="expand">Expand all</button><button id="theme">Light / dark</button></div>
<div id="layout">
<nav id="side" aria-label="Contents">{toc_html()}</nav>
<main>
{cover}
{''.join(parts_out)}
<p class="n" style="margin-top:60px">Compiled {BUILT} by <code>tools/build_master.py</code> from the files in this folder. Research date {RESEARCHED}.</p>
</main></div>
<script>{stats_js}</script>
<script>{JS}</script>
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(doc)
print(f"wrote {OUT}  {os.path.getsize(OUT) / 1e6:.2f} MB  words={stats['words']:,}  images={stats['images']}  urls={stats['urls']}  toc={len(toc)}")
