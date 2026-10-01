#!/usr/bin/env python3
"""Collect YouTube search-box suggestions for the candidate stories (stdlib + curl).

For each story it asks the public suggest endpoint (client=firefox, ds=yt) with
several question-shaped prefixes, so the report can show how viewers phrase their
questions about each disaster. Writes data/title-autocomplete.json and
data/title-autocomplete.md. Needs outbound HTTPS (curl).

Usage:  python3 tools/title_autocomplete.py      (run from stress-riser/)
"""
import json
import subprocess
import time
import urllib.parse
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# story label -> short search name
STORIES = {
    "Comet airliner 1954": "de havilland comet",
    "Tacoma Narrows 1940": "tacoma narrows bridge",
    "Vajont 1963": "vajont dam",
    "Vasa 1628": "vasa ship",
    "Challenger 1986": "challenger shuttle",
    "Northeast blackout 2003": "2003 northeast blackout",
    "Galaxy Note 7 2016": "galaxy note 7",
    "Quebec Bridge 1907": "quebec bridge",
    "Big Dig ceiling 2006": "big dig ceiling collapse",
    "Hyatt Regency 1981": "hyatt regency walkway",
    "Piper Alpha 1988": "piper alpha",
    "Flixborough 1974": "flixborough",
}
PREFIXES = ["why did {s}", "why was {s}", "how did {s}", "what happened {s}", "what caused {s}",
            "what went wrong {s}", "{s} explained", "{s} documentary", "{s} engineering", "{s} animation",
            "{s} what if", "{s} did you know"]


def suggest(q):
    url = "https://suggestqueries.google.com/complete/search?" + urllib.parse.urlencode(
        {"client": "firefox", "ds": "yt", "hl": "en", "gl": "us", "q": q})
    out = subprocess.run(["curl", "-sS", "-m", "20", url], capture_output=True, text=True)
    try:
        return json.loads(out.stdout)[1]
    except Exception:
        return []


def main():
    res = {}
    for label, s in STORIES.items():
        res[label] = {}
        for p in PREFIXES:
            q = p.format(s=s)
            res[label][q] = suggest(q)
            time.sleep(0.15)
    (DATA / "title-autocomplete.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    md = ["# YouTube search-box suggestions per candidate story (generated)\n",
          "Collected with `tools/title_autocomplete.py` from the public suggest endpoint (client=firefox, ds=yt, "
          "hl=en, gl=us) on the run date. Suggestions depend on region, time and personalization; they show how "
          "people phrase searches, not how many search.\n"]
    for label, qs in res.items():
        md.append(f"## {label}\n")
        for q, sug in qs.items():
            md.append(f"- `{q}` -> " + (" / ".join(sug) if sug else "(no suggestions)"))
        md.append("")
    (DATA / "title-autocomplete.md").write_text("\n".join(md), encoding="utf-8")
    print("done", sum(len(v) for v in res.values()), "queries")


if __name__ == "__main__":
    main()
