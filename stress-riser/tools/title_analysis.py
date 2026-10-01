#!/usr/bin/env python3
"""Title-pattern analysis of the two video indexes (stdlib only).

Reads data/niche-video-index.csv (disaster / engineering / documentary niche) and
data/cartoon-video-index.csv (cartoon and stick-figure explainers), derives
title features, and compares them in two channel-controlled ways:

  1. share of titles with a feature in the channel's top group vs its weak group
     (mean of per-channel differences, bootstrap CI over channels);
  2. within-channel z-score of log10(views) for titles with vs without the
     feature (pooled over channels, bootstrap CI over channels).

Views are the abbreviated numbers YouTube lists (11M, 172K), so they are coarse,
and they depend on the age of the video. Correlation only; see the report.

Usage:  python3 tools/title_analysis.py      (run from stress-riser/)
Writes: data/title-features.csv, data/title-analysis-report.md
"""
import csv
import math
import random
import re
import statistics as st
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
random.seed(20261001)

Q_OPENERS = ("why", "how", "what", "when", "who", "where", "which", "is", "are", "do", "does",
             "did", "can", "could", "would", "should", "was", "were", "will", "has", "have", "if")
LOUD = {"insane", "terrifying", "horrifying", "disturbing", "shocking", "deadly", "worst", "scary",
        "crazy", "unbelievable", "brutal", "horrific", "nightmare", "terror", "mystery", "secret",
        "secrets", "hidden", "forgotten", "untold", "dark", "darkest", "disturbing", "banned"}
OUTCOME = {"disaster", "collapse", "collapsed", "failure", "failed", "explosion", "exploded",
           "sinking", "sank", "sinks", "meltdown", "crash", "crashed", "fire", "flood", "burst",
           "explode", "explodes", "collapses", "fails", "blast", "catastrophe", "tragedy"}
ACRONYMS = {"USA", "UK", "NASA", "FAA", "NTSB", "AI", "TV", "USS", "RMS", "DC", "NYC", "LNG",
            "UFO", "WWII", "WW2", "CIA", "FBI", "USSR", "GPS", "CEO", "EU", "UN", "LED", "DNA",
            "MIT", "BBC", "SS", "HMS", "II", "III"}


def parse_views(s):
    s = (s or "").strip().lower().replace("views", "").replace(",", "").strip()
    m = re.match(r"^([\d.]+)\s*([kmb]?)$", s)
    if not m:
        return None
    n = float(m.group(1))
    return n * {"": 1, "k": 1e3, "m": 1e6, "b": 1e9}[m.group(2)]


def parse_age_years(s):
    s = (s or "").lower()
    m = re.search(r"(\d+)\s*(y|year|years|mo|month|months|w|week|weeks|d|day|days)\b", s)
    if not m:
        return None
    n, u = int(m.group(1)), m.group(2)
    if u.startswith("y"):
        return float(n)
    if u.startswith("mo"):
        return n / 12
    if u.startswith("w"):
        return n / 52
    return n / 365


def features(title):
    t = title.strip()
    words = re.findall(r"[A-Za-z0-9'’]+", t)
    low = [w.lower() for w in words]
    first = low[0] if low else ""
    caps = [w for w in re.findall(r"\b[A-Z]{3,}\b", t) if w not in ACRONYMS]
    f = {
        "chars": len(t),
        "words": len(words),
        "question": "?" in t,
        "q_opener": first in Q_OPENERS,
        "why": first == "why",
        "how": first == "how",
        "what": first == "what",
        "yesno": first in ("is", "are", "do", "does", "did", "can", "could", "would", "should", "was",
                           "were", "will", "has", "have"),
        "starts_the": first == "the",
        "digit": bool(re.search(r"\d", t)),
        "colon": ":" in t,
        "separator": bool(re.search(r"(:| - | – | — | \| )", t)),
        "allcaps_word": bool(caps),
        "exclaim": "!" in t,
        "you": bool(re.search(r"\byou(r|'re|'ll|'ve)?\b", t.lower())),
        "really_actually": bool(re.search(r"\b(really|actually|truth|real reason)\b", t.lower())),
        "loud_word": any(w in LOUD for w in low),
        "outcome_word": any(w in OUTCOME for w in low),
        "len_le40": len(t) <= 40,
        "len_41_60": 40 < len(t) <= 60,
        "len_gt60": len(t) > 60,
    }
    if f["question"]:
        shape = "Q:" + ("Why" if f["why"] else "How" if f["how"] else "What" if f["what"]
                        else "Yes/no" if f["yesno"] else "other")
    elif f["separator"]:
        shape = "Statement with separator"
    elif f["starts_the"]:
        shape = "Statement: The ..."
    else:
        shape = "Statement: other"
    f["shape"] = shape
    return f


def load(path, kind):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    out = []
    seen = set()
    for r in rows:
        if not r["title"].strip() or r["video_id"] in seen:
            continue
        seen.add(r["video_id"])
        if kind == "niche":
            v = parse_views(r["views_exact_at_fetch"]) or parse_views(r["views_listed_on_channel_page"])
            age = parse_age_years(r["age_listed"])
            grp = {"top": "top", "low": "weak", "extra": "extra"}[r["group"]]
        else:
            v = float(r["views_num"]) if r["views_num"] else parse_views(r["views_as_fetched"])
            age = parse_age_years(r["published_as_fetched"])
            grp = {"top": "top", "weak_recent": "weak"}[r["group"]]
        if not v or v <= 0:
            continue
        d = {"set": kind, "channel": r["channel"].strip(), "group": grp, "video_id": r["video_id"],
             "title": r["title"].strip(), "views": v, "age_years": age}
        d.update(features(r["title"]))
        out.append(d)
    return out


def boot_ci(per_channel_values, n=3000):
    """Bootstrap the mean over channels. per_channel_values: list of numbers."""
    k = len(per_channel_values)
    if k < 3:
        return None
    means = []
    for _ in range(n):
        s = [per_channel_values[random.randrange(k)] for _ in range(k)]
        means.append(sum(s) / k)
    means.sort()
    return means[int(0.025 * n)], means[int(0.975 * n)]


def share_diff(rows, feat):
    """Per channel: share(feature | top) - share(feature | weak); only channels with both groups."""
    by = defaultdict(lambda: {"top": [], "weak": []})
    for r in rows:
        if r["group"] in ("top", "weak"):
            by[r["channel"]][r["group"]].append(1 if r[feat] else 0)
    diffs = []
    for ch, g in by.items():
        if g["top"] and g["weak"]:
            diffs.append(sum(g["top"]) / len(g["top"]) - sum(g["weak"]) / len(g["weak"]))
    if not diffs:
        return None
    ci = boot_ci(diffs)
    return sum(diffs) / len(diffs), ci, len(diffs)


def add_z(rows):
    by = defaultdict(list)
    for r in rows:
        by[r["channel"]].append(math.log10(r["views"]))
    stats = {c: (st.mean(v), st.pstdev(v)) for c, v in by.items() if len(v) >= 4}
    for r in rows:
        m = stats.get(r["channel"])
        r["z"] = (math.log10(r["views"]) - m[0]) / m[1] if m and m[1] > 0 else None


def z_diff(rows, feat):
    """Pooled within-channel z: mean z(feature) - mean z(no feature); bootstrap over channels."""
    rs = [r for r in rows if r["z"] is not None]
    by = defaultdict(list)
    for r in rs:
        by[r["channel"]].append(r)
    chans = list(by)

    def diff(sample):
        a = [r["z"] for c in sample for r in by[c] if r[feat]]
        b = [r["z"] for c in sample for r in by[c] if not r[feat]]
        if len(a) < 5 or len(b) < 5:
            return None
        return st.mean(a) - st.mean(b)

    d = diff(chans)
    if d is None:
        return None
    n_with = sum(1 for r in rs if r[feat])
    boots = []
    for _ in range(1500):
        s = [chans[random.randrange(len(chans))] for _ in chans]
        x = diff(s)
        if x is not None:
            boots.append(x)
    boots.sort()
    lo, hi = boots[int(0.025 * len(boots))], boots[int(0.975 * len(boots))]
    return d, (lo, hi), n_with, len(rs)


FEATS = [
    ("question", "Contains a question mark"),
    ("why", "Starts with Why"),
    ("how", "Starts with How"),
    ("what", "Starts with What"),
    ("yesno", "Starts with Is/Are/Do/Did/Can/Could/..."),
    ("starts_the", "Starts with The (label-style statement)"),
    ("digit", "Contains a digit"),
    ("colon", "Has a colon (the brief bans it)"),
    ("separator", "Has a colon, dash or pipe separator"),
    ("allcaps_word", "Has an ALL-CAPS word (not an acronym)"),
    ("exclaim", "Has an exclamation mark"),
    ("you", "Uses you/your"),
    ("really_actually", "Says really/actually/truth/real reason"),
    ("loud_word", "Has a loud word (insane, terrifying, deadly, secret ...)"),
    ("outcome_word", "Names the outcome (disaster, collapse, explosion ...)"),
    ("len_le40", "40 characters or fewer"),
    ("len_41_60", "41 to 60 characters"),
    ("len_gt60", "More than 60 characters"),
]


def pct(x):
    return f"{100 * x:+.0f} pp"


def report(name, rows):
    L = []
    add_z(rows)
    n_ch = len({r["channel"] for r in rows})
    n_top = sum(1 for r in rows if r["group"] == "top")
    n_weak = sum(1 for r in rows if r["group"] == "weak")
    L.append(f"### {name}\n")
    L.append(f"{len(rows)} titles from {n_ch} channels ({n_top} in the top group, {n_weak} in the weak group, "
             f"{len(rows) - n_top - n_weak} extra).\n")
    L.append("**Share of titles with the feature**\n")
    L.append("| Feature | All | Top group | Weak group | Top minus weak, per channel (95% CI over channels) | Channels | z-score gap in log views (95% CI) | n with feature |")
    L.append("|---|---|---|---|---|---|---|---|")
    for key, label in FEATS:
        tot = sum(1 for r in rows if r[key]) / len(rows)
        top = [r for r in rows if r["group"] == "top"]
        weak = [r for r in rows if r["group"] == "weak"]
        st_ = sum(1 for r in top if r[key]) / len(top) if top else float("nan")
        sw_ = sum(1 for r in weak if r[key]) / len(weak) if weak else float("nan")
        sd = share_diff(rows, key)
        zd = z_diff(rows, key)
        sd_txt = (f"{pct(sd[0])} ({pct(sd[1][0])} to {pct(sd[1][1])})" if sd and sd[1] else "n/a")
        ch_txt = str(sd[2]) if sd else "0"
        zd_txt = (f"{zd[0]:+.2f} ({zd[1][0]:+.2f} to {zd[1][1]:+.2f})" if zd else "n/a")
        n_txt = str(zd[2]) if zd else "-"
        L.append(f"| {label} | {100 * tot:.0f}% | {100 * st_:.0f}% | {100 * sw_:.0f}% | {sd_txt} | {ch_txt} | {zd_txt} | {n_txt} |")
    L.append("")
    L.append("**Title shape**\n")
    L.append("| Shape | Titles | Share of all | Share of top group | Share of weak group | Median views | Mean within-channel z |")
    L.append("|---|---|---|---|---|---|---|")
    shapes = defaultdict(list)
    for r in rows:
        shapes[r["shape"]].append(r)
    top_n = max(1, sum(1 for r in rows if r["group"] == "top"))
    weak_n = max(1, sum(1 for r in rows if r["group"] == "weak"))
    for s, rs in sorted(shapes.items(), key=lambda kv: -len(kv[1])):
        zs = [r["z"] for r in rs if r["z"] is not None]
        L.append(f"| {s} | {len(rs)} | {100 * len(rs) / len(rows):.0f}% | "
                 f"{100 * sum(1 for r in rs if r['group'] == 'top') / top_n:.0f}% | "
                 f"{100 * sum(1 for r in rs if r['group'] == 'weak') / weak_n:.0f}% | "
                 f"{st.median(r['views'] for r in rs) / 1e6:.2f}M | {st.mean(zs):+.2f} |" if zs else
                 f"| {s} | {len(rs)} | - | - | - | - | - |")
    L.append("")
    tops = [r for r in rows if r["group"] == "top"]
    weaks = [r for r in rows if r["group"] == "weak"]
    L.append("**Length**: median characters, top group "
             f"{st.median(r['chars'] for r in tops):.0f}, weak group {st.median(r['chars'] for r in weaks):.0f}; "
             f"median words {st.median(r['words'] for r in tops):.0f} vs {st.median(r['words'] for r in weaks):.0f}.\n")
    return "\n".join(L)


def question_openers(rows):
    """First two words of question titles, with counts and median views."""
    by = defaultdict(list)
    for r in rows:
        if r["question"]:
            w = re.findall(r"[A-Za-z']+", r["title"])
            key = " ".join(x.capitalize() for x in w[:2]) if r["q_opener"] else "(other: question mark mid-title or after a label)"
            by[key].append(r)
    L = ["| Opening two words | Titles | Median views | Channels |", "|---|---|---|---|"]
    for k, rs in sorted(by.items(), key=lambda kv: -len(kv[1]))[:14]:
        L.append(f"| {k} | {len(rs)} | {st.median(r['views'] for r in rs) / 1e6:.2f}M | {len({r['channel'] for r in rs})} |")
    return "\n".join(L)


def top_titles(rows, n=30, only_question=False):
    rs = sorted(rows, key=lambda r: -r["views"])
    if only_question:
        rs = [r for r in rs if r["question"]]
    L = ["| Views | Channel | Title | Chars |", "|---|---|---|---|"]
    for r in rs[:n]:
        L.append(f"| {r['views'] / 1e6:.1f}M | {r['channel']} | {r['title']} | {r['chars']} |")
    return "\n".join(L)


def main():
    niche = load(DATA / "niche-video-index.csv", "niche")
    cartoon = load(DATA / "cartoon-video-index.csv", "cartoon")
    allrows = niche + cartoon

    with open(DATA / "title-features.csv", "w", newline="", encoding="utf-8") as fh:
        keys = ["set", "channel", "group", "video_id", "title", "views", "age_years", "chars", "words", "shape"] + \
               [k for k, _ in FEATS]
        w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        for r in allrows:
            w.writerow(r)

    out = ["# Title analysis of the two video indexes (generated)\n",
           "Generated by `tools/title_analysis.py` from `data/niche-video-index.csv` and "
           "`data/cartoon-video-index.csv` (fetched 2026-09-30). Views are the abbreviated figures YouTube lists "
           "(for example 11M, 172K), so they are coarse; they also depend on age. The two groups are not random "
           "samples: the top group is each channel's most-viewed list, the weak group its weakest recent uploads. "
           "Everything below is correlation inside that sample, not proof that a title feature causes views. "
           "The z-score gap is the difference in mean within-channel z of log10(views) between titles with and "
           "without the feature (0.5 is half a standard deviation of that channel's own spread); only channels "
           "with at least four titles enter it.\n"]
    out.append(report("Disaster / engineering / documentary niche", niche))
    out.append(report("Cartoon and stick-figure explainers", cartoon))
    out.append(report("Both sets together", allrows))
    out.append("### Question openers (both sets)\n")
    out.append(question_openers(allrows))
    out.append("\n### Question openers inside the top group of the niche set\n")
    out.append(question_openers([r for r in niche if r["group"] == "top"]))
    out.append("\n### The 30 most-viewed titles in the niche set\n")
    out.append(top_titles(niche, 30))
    out.append("\n### The 25 most-viewed question titles (both sets)\n")
    out.append(top_titles(allrows, 25, only_question=True))
    out.append("\n### Question-title share by channel (niche set, channels with 5 or more titles)\n")
    by = defaultdict(list)
    for r in niche:
        by[r["channel"]].append(r)
    out.append("| Channel | Titles | Question titles | Median views |")
    out.append("|---|---|---|---|")
    for c, rs in sorted(by.items(), key=lambda kv: -sum(1 for r in kv[1] if r["question"]) / len(kv[1])):
        if len(rs) >= 5:
            q = sum(1 for r in rs if r["question"])
            out.append(f"| {c} | {len(rs)} | {q} ({100 * q / len(rs):.0f}%) | {st.median(r['views'] for r in rs) / 1e6:.2f}M |")
    (DATA / "title-analysis-report.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote", DATA / "title-analysis-report.md", "and title-features.csv;", len(allrows), "rows")


if __name__ == "__main__":
    main()
