#!/usr/bin/env python3
"""
thumb_preview.py - preview a 16:9 YouTube thumbnail the way it appears in the feed.

Renders ONE image at the real CSS-pixel sizes YouTube shows, on the light (#ffffff) and dark (#0f0f0f)
page backgrounds, with rounded corners, the duration badge in the bottom-right corner, an optional
title/channel line, plus a grayscale column and a blur ("squint") column. Output is a contact sheet PNG
at 1:1 pixel scale (open it at 100 %; use --zoom 2 to enlarge with nearest-neighbour for a monitor check).

USAGE
  python3 thumb_preview.py my_thumb.jpg                       # -> my_thumb_preview.png
  python3 thumb_preview.py my_thumb.jpg -o sheet.png --duration 10:24 --title "Why did 1,900 people die under a dam that never broke?"
  python3 thumb_preview.py a.png b.png c.png --sizes small-168 phone-360      # several images side by side rows
  python3 thumb_preview.py --demo                             # builds 4 synthetic palette samples + sheet
  python3 thumb_preview.py my_thumb.jpg --safezone            # also writes my_thumb_safezone.png (1280x720 guide overlay)
  python3 thumb_preview.py my_thumb.jpg --watched 0.4         # add red 'watched' progress bar (bottom edge)

SIZE PRESETS (CSS px, width x height; 16:9)
  phone-360   360x202  narrow Android full-width card (360 css-px wide viewports: 3-5 % of US/UK/CA/AU phones)
  phone-390   390x219  iPhone 12-15 class (390 css-px viewport is 2nd most common in US/UK/CA/AU, StatCounter Aug 2026)
  phone-414   414x233  414 css-px viewport (most common in US/UK/CA/AU, 21-30 %, StatCounter Aug 2026)
  desk-search 360x202  desktop search result (YouTube web requests 360x202 + 720x404)
  desk-home   310x174  min width of a desktop home-feed card (from YouTube home skeleton CSS: flex-basis 310px)
  related-246 246x138  one of the sizes the watch-page sidebar requests (168x94 / 196x110 / 246x138 / 336x188)
  small-168   168x94   smallest common thumbnail: watch-page sidebar 'up next' (168x94 + 336x188 requested)
Default: phone-360 phone-390 desk-home related-246 small-168

NOTES / ASSUMPTIONS (flagged because not all are verified first-hand)
  * Page backgrounds: light #ffffff, dark #0f0f0f  (both read from YouTube's own skeleton CSS, Sept 2026).
  * Corner radius 12 px (8 px below 200 px width) - approximates the current web/app look. UNVERIFIED for native apps.
  * Duration badge: 12 px bold label, 4 px padding, 4 px radius, 80 % black, 4 px from right/bottom edge.
    Width for '10:24' ~ 40 px. Badge geometry is an approximation (UNVERIFIED first-hand); it is drawn slightly
    large on purpose. At 1280 px master width, 1 css px = 3.56 px (360 wide) so the badge keep-out is ~ 230x90 px.
  * The real image is served 1280x720 JPEG 4:2:0 (measured) and the phone has 2-3x pixel density, so real phone
    screens look SHARPER than this 1:1 CSS-pixel simulation. Treat the sheet as the pessimistic case.
  * Downscale uses LANCZOS (close to what browsers/GPU mip-mapping give). --resample box|bilinear|lanczos.
  * Optional --jpeg-q N re-encodes the master through JPEG 4:2:0 at quality N first (YouTube re-encodes uploads).

Requires: Pillow (pip install pillow). Optional: numpy not required.
"""
import argparse, io, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

PRESETS = {
    "phone-360": (360, 202), "phone-390": (390, 219), "phone-414": (414, 233),
    "desk-search": (360, 202), "desk-home": (310, 174), "related-246": (246, 138), "small-168": (168, 94),
}
DEFAULT_SIZES = ["phone-360", "phone-390", "desk-home", "related-246", "small-168"]
BG = {"light": (255, 255, 255), "dark": (15, 15, 15)}
FG_TITLE = {"light": (15, 15, 15), "dark": (241, 241, 241)}
FG_META = {"light": (96, 96, 96), "dark": (170, 170, 170)}
PALETTE = dict(ink="#1a1a1a", white="#ffffff", paper="#f3ead8", sky="#bfe2ea", grn_l="#8fbf5a",
               grn_d="#4f7d3a", brown="#9a6b43", tan="#d2b48c", amber="#e6b23a", red="#d94a38")

def _font(size, bold=True, name=None):
    cands = ([name] if name else []) + [
        "/usr/share/fonts/truetype/liberation/LiberationSans-%s.ttf" % ("Bold" if bold else "Regular"),
        "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""),
        "Arial Bold.ttf" if bold else "Arial.ttf"]
    for c in cands:
        try: return ImageFont.truetype(c, size)
        except Exception: pass
    return ImageFont.load_default()

RESAMPLE = {"lanczos": Image.LANCZOS, "box": Image.BOX, "bilinear": Image.BILINEAR}

def jpeg_roundtrip(im, q):
    b = io.BytesIO(); im.convert("RGB").save(b, "JPEG", quality=q, subsampling=2); b.seek(0)
    return Image.open(b).convert("RGB")

def rounded(im, r):
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.size[0]-1, im.size[1]-1], r, fill=255)
    out = Image.new("RGBA", im.size); out.paste(im.convert("RGB"), (0, 0)); out.putalpha(m); return out

def add_badge(im, text, w):
    s = 1.0 if w >= 300 else (0.9 if w >= 200 else 0.85)
    f = _font(int(round(12*s)), True)
    d = ImageDraw.Draw(im, "RGBA")
    tw = d.textlength(text, font=f); pad = int(round(4*s)); h = int(round(18*s))
    x1 = im.size[0] - 4; y1 = im.size[1] - 4; x0 = int(x1 - tw - 2*pad); y0 = y1 - h
    d.rounded_rectangle([x0, y0, x1, y1], 4, fill=(0, 0, 0, 204))
    d.text((x0+pad, y0 + (h - f.size)//2 - 1), text, font=f, fill=(255, 255, 255, 255))
    return (x0, y0, x1, y1)

def add_progress(im, frac):
    d = ImageDraw.Draw(im, "RGBA"); H = im.size[1]
    d.rectangle([0, H-3, im.size[0], H], fill=(255, 255, 255, 90))
    d.rectangle([0, H-3, int(im.size[0]*frac), H], fill=(255, 0, 0, 255))

def wrap(d, text, font, maxw, lines=2):
    words, out, cur = text.split(), [], ""
    for w in words:
        t = (cur+" "+w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: out.append(cur); cur = w
    out.append(cur)
    if len(out) > lines:
        out = out[:lines]; out[-1] = out[-1].rstrip(".,") + "..."
    return out

def card(master, size, mode, args, variant="normal"):
    w, h = size
    img = master.convert("RGB")
    if args.jpeg_q: img = jpeg_roundtrip(img, args.jpeg_q)
    th = img.resize((w, h), RESAMPLE[args.resample])
    if variant == "gray": th = ImageOps.grayscale(th).convert("RGB")
    if variant == "blur":  th = th.filter(ImageFilter.GaussianBlur(radius=max(2.0, w/60)))
    th = th.convert("RGBA")
    badge = add_badge(th, args.duration, w)
    if args.watched: add_progress(th, args.watched)
    th = rounded(th, 12 if w >= 200 else 8)
    pad = 12
    lines = []
    tf = _font(14 if w >= 300 else 12, True); mf = _font(12 if w >= 300 else 11, False)
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    if args.title: lines = wrap(tmp, args.title, tf, w, 2)
    text_h = (len(lines)*(tf.size+4) + (mf.size+6)) if args.title else 0
    cv = Image.new("RGB", (w + 2*pad, h + 2*pad + text_h), BG[mode])
    cv.paste(th, (pad, pad), th)
    if args.title:
        d = ImageDraw.Draw(cv); y = pad + h + 6
        for ln in lines: d.text((pad, y), ln, font=tf, fill=FG_TITLE[mode]); y += tf.size + 4
        d.text((pad, y), "Stress Riser  -  12K views  -  2 days ago", font=mf, fill=FG_META[mode])
    return cv

def sheet(master, name, args):
    sizes = args.sizes or DEFAULT_SIZES
    cols = [("light", "normal"), ("dark", "normal"), ("light", "gray"), ("dark", "blur")]
    if args.no_extra: cols = cols[:2]
    rows = []
    for s in sizes:
        rows.append([card(master, PRESETS[s], m, args, v) for (m, v) in cols])
    lab = _font(13, True)
    colw = [max(r[i].size[0] for r in rows) for i in range(len(cols))]
    rowh = [max(c.size[1] for c in r) for r in rows]
    G = 14; top = 34; left = 128
    W = left + sum(colw) + G*(len(cols)+1); H = top + sum(rowh) + G*(len(rows)+1)
    sh = Image.new("RGB", (W, H), (128, 128, 128))
    d = ImageDraw.Draw(sh)
    d.text((8, 8), name, font=lab, fill=(255, 255, 255))
    heads = {"normal": "", "gray": " grayscale", "blur": " blur (squint)"}
    x = left + G
    for i, (m, v) in enumerate(cols):
        d.text((x, 8+14), f"{m}{heads[v]}", font=_font(12, False), fill=(255, 255, 255)); x += colw[i] + G
    y = top + G
    for ri, s in enumerate(sizes):
        d.text((8, y+4), s, font=lab, fill=(255, 255, 255))
        d.text((8, y+22), "%dx%d px" % PRESETS[s], font=_font(11, False), fill=(230, 230, 230))
        x = left + G
        for ci, c in enumerate(rows[ri]):
            sh.paste(c, (x, y)); x += colw[ci] + G
        y += rowh[ri] + G
    if args.zoom != 1:
        sh = sh.resize((sh.size[0]*args.zoom, sh.size[1]*args.zoom), Image.NEAREST)
    return sh

def safezone(master, path):
    """Annotate the 1280x720 master with keep-out zones: bottom-right badge zone, 5 % edge margin, phone-crop hint."""
    im = master.convert("RGB").resize((1280, 720), Image.LANCZOS).convert("RGBA")
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.rectangle([1280-230, 720-90, 1280, 720], fill=(217, 74, 56, 110), outline=(217, 74, 56, 255), width=3)  # badge + progress bar zone
    d.rectangle([0, 0, 1280, 720], outline=(0, 0, 0, 0))
    for (x0, y0, x1, y1) in [(0, 0, 1280, 36), (0, 684, 1280, 720), (0, 0, 64, 720), (1216, 0, 1280, 720)]:
        d.rectangle([x0, y0, x1, y1], fill=(26, 26, 26, 70))       # outer 5 % margins (rounded corners, crops)
    d.rectangle([1280-110, 0, 1280, 110], outline=(230, 178, 58, 255), width=3, fill=(230, 178, 58, 60))  # desktop hover buttons (watch later / queue)
    f = _font(20, True)
    d.text((1280-226, 720-84), "badge zone", font=f, fill=(255, 255, 255, 255))
    d.text((1280-106, 6), "hover", font=f, fill=(26, 26, 26, 255))
    Image.alpha_composite(im, ov).convert("RGB").save(path)

# ---------------------------------------------------------------- demo/synthetic samples
def _stick(d, x, y, s, prop=None):
    ink = PALETTE["ink"]; w = max(3, int(s*0.05))
    d.ellipse([x-s*0.5, y-s*1.0, x+s*0.5, y], fill="#ffffff", outline=ink, width=w)
    d.ellipse([x-s*0.22, y-s*0.62, x-s*0.14, y-s*0.54], fill=ink); d.ellipse([x+s*0.14, y-s*0.62, x+s*0.22, y-s*0.54], fill=ink)
    d.line([x-s*0.25, y-s*0.25, x+s*0.25, y-s*0.20], fill=ink, width=w)
    d.line([x-s*0.28, y-s*0.78, x-s*0.10, y-s*0.72], fill=ink, width=w); d.line([x+s*0.28, y-s*0.78, x+s*0.10, y-s*0.72], fill=ink, width=w)
    body = [x, y, x, y+s*1.1]; d.line(body, fill=ink, width=w)
    d.line([x, y+s*0.3, x-s*0.7, y+s*0.75], fill=ink, width=w); d.line([x, y+s*0.3, x+s*0.7, y+s*0.15], fill=ink, width=w)
    d.line([x, y+s*1.1, x-s*0.45, y+s*1.9], fill=ink, width=w); d.line([x, y+s*1.1, x+s*0.45, y+s*1.9], fill=ink, width=w)

def _text(d, xy, text, fontfile, size, fill, outline=None, sw=0, anchor="lm"):
    try: f = ImageFont.truetype(fontfile, size)
    except Exception: f = _font(size, True)
    d.text(xy, text, font=f, fill=fill, stroke_width=sw, stroke_fill=outline, anchor=anchor)

def demo_images(outdir):
    P = PALETTE; here = os.path.dirname(os.path.abspath(__file__))
    ff = os.path.join(here, "..", "fonts", "LilitaOne-Regular.ttf")
    os.makedirs(outdir, exist_ok=True); paths = []
    # 1) sky + green hills + dam + red accent figure prop, big text top-left in white/ink
    for k, (bg_top, bg_bot, accent, txt, txtcol) in enumerate([
        (P["sky"], P["grn_l"], P["red"], "WHY IT FELL", "#ffffff"),
        (P["paper"], P["tan"], P["red"], "WHO SIGNED?", P["ink"]),
        (P["amber"], P["brown"], P["ink"], "ONE BOLT", "#ffffff"),
        (P["grn_d"], P["ink"], P["amber"], "THE CRACK", "#ffffff")]):
        im = Image.new("RGB", (1280, 720), bg_top); d = ImageDraw.Draw(im)
        d.rectangle([0, 470, 1280, 720], fill=bg_bot)
        if k == 0:
            d.polygon([(500, 470), (1280, 250), (1280, 470)], fill=P["tan"], outline=P["ink"])          # dam wall
            d.rectangle([760, 300, 1280, 470], fill=P["paper"], outline=P["ink"], width=8)
        if k == 1: d.rectangle([700, 180, 1150, 520], fill="#ffffff", outline=P["ink"], width=8)
        if k == 2:
            d.rectangle([690, 250, 1180, 560], fill=P["tan"], outline=P["ink"], width=10)
        if k == 3: d.polygon([(640, 500), (1280, 100), (1280, 500)], fill=P["brown"], outline=P["ink"])
        _stick(d, 930, 300, 150)
        d.ellipse([1010, 280, 1090, 360], fill=accent, outline=P["ink"], width=8)                        # the single accent object
        _text(d, (70, 150), txt.split()[0], ff, 200, txtcol, P["ink"], 14)
        _text(d, (70, 330), " ".join(txt.split()[1:]) or "", ff, 200, txtcol, P["ink"], 14)
        p = os.path.join(outdir, f"demo_{k+1}.png"); im.save(p); paths.append(p)
    return paths

def main():
    ap = argparse.ArgumentParser(description="YouTube feed thumbnail preview contact sheet")
    ap.add_argument("images", nargs="*"); ap.add_argument("-o", "--out")
    ap.add_argument("--sizes", nargs="+", choices=list(PRESETS)); ap.add_argument("--duration", default="10:24")
    ap.add_argument("--title"); ap.add_argument("--watched", type=float, default=0.0)
    ap.add_argument("--zoom", type=int, default=1); ap.add_argument("--resample", default="lanczos", choices=list(RESAMPLE))
    ap.add_argument("--jpeg-q", type=int, default=0, help="pre-compress master as JPEG 4:2:0 at this quality (YouTube re-encodes)")
    ap.add_argument("--no-extra", action="store_true", help="only light+dark columns")
    ap.add_argument("--safezone", action="store_true"); ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()
    imgs = a.images
    if a.demo:
        imgs = demo_images(os.path.join(os.getcwd(), "demo_samples"))
        a.title = a.title or "Why did 1,900 people die under a dam that never broke?"
    if not imgs: ap.error("give an image path or --demo")
    parts = [sheet(Image.open(p).convert("RGB"), os.path.basename(p), a) for p in imgs]
    for p, s in zip(imgs, parts):
        if a.safezone: safezone(Image.open(p), os.path.splitext(p)[0] + "_safezone.png")
    if len(parts) == 1:
        out = a.out or os.path.splitext(imgs[0])[0] + "_preview.png"; parts[0].save(out)
    else:  # stack images vertically
        W = max(p.size[0] for p in parts); H = sum(p.size[1] for p in parts)
        big = Image.new("RGB", (W, H), (128, 128, 128)); y = 0
        for p in parts: big.paste(p, (0, y)); y += p.size[1]
        out = a.out or os.path.join(os.path.dirname(imgs[0]) or ".", "contact_sheet.png"); big.save(out)
    print("wrote", out)

if __name__ == "__main__":
    main()
