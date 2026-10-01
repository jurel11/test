#!/usr/bin/env python3
"""Check Stress Riser titles against the channel brief (stdlib only).

Rules come from channel-brief.md ("Never" list and the title rule) and from title-research.md.
FAIL = breaks a brief rule. WARN = a judgment call or a soft limit. Facts, tone and honesty still need
a human: this tool cannot know whether a number is in the source.

Usage:
  python3 tools/title_check.py "Why did 1,900 people die under a dam that never broke?" "..."
  python3 tools/title_check.py --bank data/title-bank.csv        (checks the `title` column; `short_title` as Shorts)
  python3 tools/title_check.py --short "Why did a dam that held kill 1,900?"   (Shorts limit: 40 characters)
Exit code 1 if any FAIL.
"""
import csv
import re
import sys

OPENERS = {"why", "how", "what", "when", "where", "which", "who", "did", "is", "are", "do", "does", "can",
           "could", "would", "should", "was", "were", "will", "has", "have", "if"}
YESNO = {"did", "is", "are", "do", "does", "can", "could", "would", "should", "was", "were", "will", "has", "have"}
LOUD = {"shocking", "insane", "terrifying", "horrifying", "unbelievable", "crazy", "brutal", "horrific",
        "nightmare", "disturbing", "jaw-dropping", "mind-blowing", "epic", "secret", "secrets", "forbidden", "banned"}
CLICKBAIT_PHRASES = ["you won't believe", "you wont believe", "nobody tells you", "this changes everything",
                     "what happened next", "in this video", "let's dive", "lets dive", "will blow your mind",
                     "doctors hate", "gone wrong", "must watch", "watch till the end"]
BLAME = re.compile(r"\b(blame\w*|fault|idiots?|fools?|negligen\w*|reckless\w*|careless\w*|incompeten\w*|"
                   r"murder\w*|killers?|criminals?|guilty|scapegoat\w*)\b", re.I)
GORE = re.compile(r"\b(blood\w*|bodies|corpses?|gore|gory|mutilat\w*|dismember\w*|decapitat\w*|burn(ed|t)? alive|"
                  r"crushed|charred)\b", re.I)
BRITISH = {"metre": "meter", "metres": "meters", "kilometre": "kilometer", "kilometres": "kilometers",
           "colour": "color", "centre": "center", "defence": "defense", "harbour": "harbor", "labour": "labor",
           "storey": "story", "storeys": "stories", "tyre": "tire", "tyres": "tires", "aluminium": "aluminum",
           "programme": "program", "whilst": "while", "analyse": "analyze", "behaviour": "behavior",
           "favour": "favor", "neighbour": "neighbor", "grey": "gray", "litre": "liter", "litres": "liters"}
VAGUE = {"this", "thing", "things", "something", "everything", "stuff"}
ACRONYMS = {"USA", "UK", "NASA", "FAA", "NTSB", "AI", "TV", "USS", "RMS", "DC", "NYC", "LNG", "UFO", "WWII",
            "CIA", "FBI", "USSR", "GPS", "CEO", "EU", "UN", "LED", "DNA", "MIT", "BBC", "HMS", "SS", "II", "III"}


def check(title, short=False):
    t = title.strip()
    res = []  # (level, rule, message)
    words = re.findall(r"[A-Za-z0-9'’]+", t)
    low = [w.lower() for w in words]
    first = low[0] if low else ""
    limit_soft, limit_hard = (40, 60) if short else (60, 70)

    if not t.endswith("?") or t.count("?") != 1:
        res.append(("FAIL", "question", "must be one question ending in a single '?' (brief: no statements)"))
    if re.search(r":| - | – | — |\|", t):
        res.append(("FAIL", "separator", "no colon, dash or pipe (brief: no colon; keep series tags out of the title)"))
    if first not in OPENERS:
        res.append(("FAIL", "opener", f"starts with '{words[0] if words else ''}', not a question word "
                                      "(brief: no case name first, no statement)"))
    elif first == "who":
        res.append(("FAIL", "blame", "'Who ...' invites blaming a person (brief: the failure is the villain)"))
    elif first in YESNO:
        res.append(("WARN", "yes/no", "yes/no question: weaker in our title data (n small); fine for a decision-seat test"))
    n = len(t)
    if n > limit_hard:
        res.append(("FAIL", "length", f"{n} characters; limit {limit_hard}" + (" for a Short" if short else "")))
    elif n > limit_soft:
        res.append(("WARN", "length", f"{n} characters; soft limit {limit_soft}" + (" for a Short" if short else "")))
    if n > 100:
        res.append(("FAIL", "length", "over YouTube's 100-character hard limit"))
    if not short and n > 40:
        res.append(("INFO", "visible", f"first 40 characters: '{t[:40]}' | hidden on small screens: '{t[40:]}'"))
    if "!" in t:
        res.append(("FAIL", "loud", "exclamation mark (YouTube lists it under 'loud'; brief tone is calm)"))
    caps = [w for w in re.findall(r"\b[A-Z]{3,}\b", t) if w not in ACRONYMS]
    if caps:
        res.append(("FAIL", "loud", f"ALL-CAPS word {caps} (YouTube: limit ALL CAPS)"))
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", t):
        res.append(("FAIL", "loud", "emoji (YouTube: limit emoji)"))
    hits = [w for w in low if w in LOUD]
    if hits:
        res.append(("FAIL", "clickbait", f"loud/clickbait word {hits}"))
    for p in CLICKBAIT_PHRASES:
        if p in t.lower():
            res.append(("FAIL", "clickbait", f"phrase '{p}'"))
    m = BLAME.search(t)
    if m:
        res.append(("FAIL", "blame", f"'{m.group(0)}': blames a person (brief: blame systems, incentives, assumptions)"))
    m = GORE.search(t)
    if m:
        res.append(("FAIL", "gore", f"'{m.group(0)}': no graphic injury or death wording (brief)"))
    for w in low:
        if w in BRITISH:
            res.append(("WARN", "spelling", f"British '{w}' -> American '{BRITISH[w]}' (brief: American spelling)"))
    nums = re.findall(r"\d[\d,.]*", t)
    if len(nums) >= 2:
        res.append(("WARN", "numbers", f"{len(nums)} numbers {nums}: the brief wants one number the viewer can feel"))
    v = [w for w in low if w in VAGUE]
    if v:
        res.append(("WARN", "vague", f"vague word {v}: name the object or the number instead"))
    if re.search(r"\((19|20)\d\d\)|\b(19|20)\d\d\)?\s*$", t):
        res.append(("WARN", "year-tag", "year tag at the end; keep the date in the description unless it is the hook"))
    return res


def verdict(res):
    if any(r[0] == "FAIL" for r in res):
        return "FAIL"
    if any(r[0] == "WARN" for r in res):
        return "WARN"
    return "PASS"


def show(title, short=False):
    res = check(title, short)
    v = verdict(res)
    print(f"[{v}] ({len(title)}) {title}")
    for level, rule, msg in res:
        if level != "INFO" or v != "PASS":
            print(f"      {level:4} {rule}: {msg}")
    return v


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    bad = 0
    if argv[0] == "--bank":
        for r in csv.DictReader(open(argv[1], encoding="utf-8")):
            print(f"\n## {r['story']} / {r['slot']} ({r['pattern']})")
            bad += show(r["title"]) == "FAIL"
            if r.get("short_title"):
                bad += show(r["short_title"], short=True) == "FAIL"
        return 1 if bad else 0
    short = False
    if argv[0] == "--short":
        short, argv = True, argv[1:]
    for t in argv:
        bad += show(t, short) == "FAIL"
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
