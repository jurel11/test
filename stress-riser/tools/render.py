import os, subprocess, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
import importlib, lib, scenes
importlib.reload(lib); importlib.reload(scenes)
from scenes import SCENES
from lib import svg

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
only = sys.argv[1:]


def shot(svg_str, png):
    html = OUT + "/_tmp.html"
    open(html, "w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;padding:0;background:#fff;overflow:hidden}}svg{{display:block}}</style></head><body>{svg_str}</body></html>')
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=3000", "--window-size=1280,1000", f"--screenshot={png}", "file://" + html],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    from PIL import Image
    im = Image.open(png).convert("RGB")
    assert im.size[0] == 1280, im.size
    im.crop((0, 0, 1280, 720)).save(png)


for slug, name, story, fn in SCENES:
    if only and not any(o in slug for o in only):
        continue
    art, txt = fn()
    open(f"{OUT}/{slug}.svg", "w").write(svg(art + txt))
    shot(svg(art + txt), f"{OUT}/{slug}.png")
    if txt:
        shot(svg(art), f"{OUT}/{slug}-art.png")
    print("ok", slug)
