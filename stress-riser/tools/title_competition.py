#!/usr/bin/env python3
"""Who already owns the search results for each candidate story? (stdlib + curl)

For each story it fetches the YouTube results page for two search phrases (a question-shaped one
that the search box suggests, and the plain event name), parses the first videos out of the page
data, and writes data/title-competition.csv and data/title-competition.md: title, channel, exact
view count as listed, age, and whether the title is a question.

Needs outbound HTTPS. Results depend on region, time and personalization (this run: logged out,
English, US consent cookie). Be gentle: one request every 3 seconds.

Usage:  python3 tools/title_competition.py      (run from stress-riser/)
"""
import csv
import json
import re
import subprocess
import time
import urllib.parse
from datetime import date
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

STORIES = {
    "Comet airliner 1954": ["de havilland comet disaster", "why did the comet airliner crash"],
    "Tacoma Narrows 1940": ["why did the tacoma narrows bridge collapse", "tacoma narrows bridge collapse"],
    "Vajont 1963": ["vajont dam disaster", "why did the vajont dam fail"],
    "Vasa 1628": ["why did the vasa sink", "vasa ship"],
    "Challenger 1986": ["why did challenger explode", "challenger disaster explained"],
    "Northeast blackout 2003": ["what caused the 2003 blackout", "2003 northeast blackout"],
    "Galaxy Note 7 2016": ["why did the galaxy note 7 explode", "galaxy note 7"],
    "Quebec Bridge 1907": ["quebec bridge collapse", "why did the quebec bridge collapse"],
    "Big Dig ceiling 2006": ["big dig ceiling collapse", "why did the big dig ceiling collapse"],
    "Hyatt Regency 1981": ["hyatt regency walkway collapse", "why did the hyatt regency walkway collapse"],
    "Piper Alpha 1988": ["what caused the piper alpha disaster", "piper alpha disaster"],
    "Flixborough 1974": ["flixborough disaster", "why did flixborough explode"],
}


def fetch(query):
    url = "https://www.youtube.com/results?" + urllib.parse.urlencode({"search_query": query})
    out = subprocess.run(
        ["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
         "-b", "CONSENT=YES+1; SOCS=CAI", url], capture_output=True, text=True)
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", out.stdout, re.S)
    if not m:
        return []
    data = json.loads(m.group(1))
    found = []

    def walk(o):
        if isinstance(o, dict):
            v = o.get("videoRenderer")
            if v:
                title = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
                views = v.get("viewCountText", {}).get("simpleText", "")
                n = re.sub(r"[^\d]", "", views) if "view" in views else ""
                found.append({
                    "video_id": v.get("videoId", ""),
                    "title": title,
                    "channel": (v.get("ownerText", {}).get("runs") or [{}])[0].get("text", ""),
                    "views": int(n) if n else "",
                    "published": v.get("publishedTimeText", {}).get("simpleText", ""),
                    "length": v.get("lengthText", {}).get("simpleText", ""),
                })
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)

    walk(data)
    return found


def main():
    rows = []
    for story, queries in STORIES.items():
        for q in queries:
            for rank, v in enumerate(fetch(q)[:10], 1):
                rows.append({"story": story, "query": q, "rank": rank, **v,
                             "is_question": "?" in v["title"], "fetched": date.today().isoformat()})
            time.sleep(3)
    with open(DATA / "title-competition.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    md = ["# Existing YouTube results for each candidate story (generated)\n",
          "Collected with `tools/title_competition.py` on " + date.today().isoformat() +
          " (logged out, English, US). Top 10 results per phrase, exact view counts as listed on the results page. "
          "Results change by region, time and personalization. This shows how existing videos are titled and "
          "how large they are, not what ranks for you.\n"]
    for story in STORIES:
        sr = [r for r in rows if r["story"] == story]
        uniq = {}
        for r in sr:
            uniq.setdefault(r["video_id"], r)
        vids = list(uniq.values())
        nq = sum(1 for r in vids if r["is_question"])
        big = [r for r in vids if isinstance(r["views"], int) and r["views"] >= 1_000_000]
        md.append(f"## {story}\n")
        md.append(f"{len(vids)} distinct videos; {nq} with a question mark in the title; {len(big)} with 1M views or more.\n")
        md.append("| Views | Channel | Title | Age |")
        md.append("|---|---|---|---|")
        for r in sorted(vids, key=lambda r: -(r["views"] if isinstance(r["views"], int) else 0))[:8]:
            v = f"{r['views']:,}" if isinstance(r["views"], int) else "n/a"
            md.append(f"| {v} | {r['channel']} | {r['title']} | {r['published']} |")
        md.append("")
    (DATA / "title-competition.md").write_text("\n".join(md), encoding="utf-8")
    print("wrote", len(rows), "rows")


if __name__ == "__main__":
    main()
