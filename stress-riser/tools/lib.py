"""Tiny SVG helpers for the Stress Riser thumbnail mockups (1280x720, channel palette only)."""
import base64, math, os

INK, WHITE, PAPER, SKY = "#1a1a1a", "#ffffff", "#f3ead8", "#bfe2ea"
LG, DG, BR, TAN, AM, RED = "#8fbf5a", "#4f7d3a", "#9a6b43", "#d2b48c", "#e6b23a", "#d94a38"
SW = 12          # outline weight on the 1280x720 master (brief: clean black outlines)
W, H = 1280, 720

FONT_B64 = base64.b64encode(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "LilitaOne-Regular.ttf"), "rb").read()).decode()


def pts(p):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in p)


def poly(p, fill, sw=SW):
    return f'<polygon points="{pts(p)}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>'


def rect(x, y, w, h, fill, rx=0, sw=SW):
    s = f' stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"' if sw else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'


def circ(cx, cy, r, fill, sw=SW):
    s = f' stroke="{INK}" stroke-width="{sw}"' if sw else ""
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"{s}/>'


def path(d, fill="none", sw=SW, stroke=INK):
    s = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"' if sw else ""
    return f'<path d="{d}" fill="{fill}"{s}/>'


def line(x1, y1, x2, y2, sw=SW, stroke=INK):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>'


def blob(shapes, fill, sw=SW):
    """Union outline: draw every shape with a thick ink stroke, then re-fill them without stroke."""
    a, b = [], []
    for s in shapes:
        if s[0] == "c":
            _, cx, cy, r = s
            a.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{INK}" stroke="{INK}" stroke-width="{2*sw}"/>')
            b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>')
        elif s[0] == "r":
            _, x, y, w, h, rx = s
            a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{INK}" stroke="{INK}" stroke-width="{2*sw}" stroke-linejoin="round"/>')
            b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"/>')
        elif s[0] == "p":
            _, p = s
            a.append(f'<polygon points="{pts(p)}" fill="{INK}" stroke="{INK}" stroke-width="{2*sw}" stroke-linejoin="round"/>')
            b.append(f'<polygon points="{pts(p)}" fill="{fill}"/>')
    return "".join(a) + "".join(b)


def cloud(cx, cy, s=1.0, fill=WHITE):
    return blob([("c", cx - 70 * s, cy + 10 * s, 42 * s), ("c", cx, cy - 10 * s, 58 * s), ("c", cx + 78 * s, cy + 8 * s, 44 * s),
                 ("r", cx - 112 * s, cy + 10 * s, 234 * s, 46 * s, 23 * s)], fill)


def text(lines, x, y, cap, anchor="start", fill=WHITE):
    """Overlay text layer: Lilita One, ink outline drawn outside the glyphs (12% of cap height)."""
    if isinstance(lines, str):
        lines = [lines]
    fs = cap / 0.70
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + i * cap * 1.22:.1f}" font-family="LilitaOne" font-size="{fs:.1f}" text-anchor="{anchor}" '
                   f'fill="{fill}" stroke="{INK}" stroke-width="{2 * 0.12 * cap:.1f}" stroke-linejoin="round" paint-order="stroke fill">{ln}</text>')
    return "".join(out)


# ---------------------------------------------------------------- stick figure (character-sheet rules)
def figure(cx, cy, r, mood="worried", look=(0.0, 0.0), arms=((-1.3, 0.9), (1.3, 0.9)), legs=((-0.5, 3.6), (0.5, 3.6)), prop=None, back=False):
    """cx,cy = head centre, r = head radius. Round white head, dot eyes, line brows + mouth,
    small white body, arms/legs are single black lines, no hands/feet/clothes."""
    lw = max(6.0, min(12.0, r * 0.24))   # limbs stay single thin lines, even in a close-up
    sw = max(6.0, min(SW, r * 0.34))
    e = []
    sh = (cx, cy + r * 1.22)                       # shoulders
    hip = (cx, cy + r * 2.15)
    for dx, dy in arms:
        e.append(line(sh[0] + (0.30 if dx > 0 else -0.30) * r, sh[1] + 0.05 * r, cx + dx * r, cy + r * 1.22 + dy * r, lw))
    for dx, dy in legs:
        e.append(line(hip[0] + (0.22 if dx > 0 else -0.22) * r, hip[1] - 0.1 * r, cx + dx * r, cy + dy * r, lw))
    e.append(f'<ellipse cx="{cx:.1f}" cy="{cy + r * 1.62:.1f}" rx="{r * 0.55:.1f}" ry="{r * 0.62:.1f}" fill="{WHITE}" stroke="{INK}" stroke-width="{sw:.1f}"/>')
    e.append(circ(cx, cy, r, WHITE, sw))
    if prop:
        e.append(prop)
    if back:
        return "".join(e)
    gx, gy = look[0] * r * 0.22, look[1] * r * 0.22
    ex, ey, er = 0.36 * r, -0.02 * r, max(3.0, 0.11 * r)
    for s in (-1, 1):
        e.append(circ(cx + s * ex + gx, cy + ey + gy, er, INK, 0))
    bw = max(3.5, 0.1 * r)
    if mood == "worried":
        for s in (-1, 1):
            e.append(line(cx + s * 0.66 * r, cy - 0.28 * r, cx + s * 0.14 * r, cy - 0.52 * r, bw))
        e.append(path(f"M {cx - 0.30 * r:.1f} {cy + 0.52 * r:.1f} Q {cx:.1f} {cy + 0.30 * r:.1f} {cx + 0.30 * r:.1f} {cy + 0.52 * r:.1f}", "none", bw))
    elif mood == "surprised":
        for s in (-1, 1):
            e.append(path(f"M {cx + s * 0.66 * r:.1f} {cy - 0.38 * r:.1f} Q {cx + s * 0.4 * r:.1f} {cy - 0.68 * r:.1f} {cx + s * 0.14 * r:.1f} {cy - 0.44 * r:.1f}", "none", bw))
        e.append(f'<ellipse cx="{cx:.1f}" cy="{cy + 0.48 * r:.1f}" rx="{0.13 * r:.1f}" ry="{0.19 * r:.1f}" fill="{WHITE}" stroke="{INK}" stroke-width="{bw:.1f}"/>')
    elif mood == "scared":
        for s in (-1, 1):
            e.append(line(cx + s * 0.66 * r, cy - 0.30 * r, cx + s * 0.12 * r, cy - 0.58 * r, bw))
        e.append(path(f"M {cx - 0.30 * r:.1f} {cy + 0.5 * r:.1f} q {0.15 * r:.1f} {-0.2 * r:.1f} {0.30 * r:.1f} 0 t {0.30 * r:.1f} 0", "none", bw))
    else:  # calm
        for s in (-1, 1):
            e.append(line(cx + s * 0.64 * r, cy - 0.38 * r, cx + s * 0.16 * r, cy - 0.38 * r, bw))
        e.append(line(cx - 0.26 * r, cy + 0.48 * r, cx + 0.26 * r, cy + 0.48 * r, bw))
    return "".join(e)


def clipboard(x, y, s=1.0, tilt=0):
    return (f'<g transform="translate({x},{y}) rotate({tilt}) scale({s})">' + rect(-22, -30, 44, 60, PAPER, 4, 6) + rect(-10, -36, 20, 12, TAN, 3, 5) + "</g>")


def thermometer(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">' + rect(-6, -48, 12, 76, WHITE, 6, 6) + circ(0, 34, 12, RED, 6) + rect(-3, -6, 6, 34, RED, 0, 0) + "</g>")


def svg(body, bg=None):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<defs><style>@font-face{{font-family:LilitaOne;src:url(data:font/ttf;base64,{FONT_B64}) format("truetype");}}</style></defs>'
            + (rect(0, 0, W, H, bg, 0, 0) if bg else "") + body + "</svg>")
