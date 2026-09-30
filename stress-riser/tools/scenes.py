"""10 thumbnail style mockups. Each scene returns (art_layer, text_layer): the art layer obeys the brief's
'no text/numbers/arrows in images' rule; the words are a separate overlay added in the design tool."""
from lib import *


def edge(color=BR, w=14):
    """Mid-tone edge band so dark scenes do not dissolve into a dark-mode feed."""
    return f'<rect x="{w/2}" y="{w/2}" width="{W-w}" height="{H-w}" fill="none" stroke="{color}" stroke-width="{w}"/>'


# 1 ── Tiny Under the Giant · Vajont ───────────────────────────────────────────────────────────
def s1():
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(1010, 70, 0.75), cloud(1215, 190, 0.45)]
    a.append(poly([(1100, 720), (1140, 540), (1190, 440), (1280, 410), (1280, 720)], LG))                        # right valley wall
    a.append(poly([(0, 0), (380, 0), (620, 460), (700, 720), (0, 720)], TAN))                                    # the mountain (pale)
    a.append(poly([(620, 460), (900, 460), (900, 720), (700, 720)], DG))                                         # reservoir
    a.append(poly([(130, 330), (300, 290), (450, 340), (560, 425), (620, 462), (430, 480), (250, 440), (120, 400)], RED))  # the slope that slid
    a.append(line(300, 290, 330, 400, 6)); a.append(line(450, 340, 400, 450, 6))
    for x, y, r in ((650, 448, 22), (600, 502, 16), (690, 492, 13)):
        a.append(circ(x, y, r, RED, 8))                                                                          # boulders reaching the lake
    a.append(blob([("c", 660, 430, 32), ("c", 700, 398, 40), ("c", 742, 376, 32), ("c", 700, 442, 28)], WHITE))    # splash where it hit
    a.append(poly([(690, 462), (715, 340), (785, 245), (880, 205), (960, 212), (1015, 245), (1045, 335), (1092, 475), (1135, 600), (1165, 720), (900, 720), (900, 462)], DG))   # the wave
    a.append(poly([(860, 282), (990, 282), (1092, 720), (850, 720)], PAPER))                                     # the dam: still standing
    for y, k in ((380, 0), (480, 1), (580, 2), (680, 3)):
        a.append(line(862 + k * 8, y, 1010 + k * 26, y, 4))
    a.append(blob([("c", 775, 262, 24), ("c", 840, 222, 28), ("c", 915, 204, 30), ("c", 985, 216, 28), ("c", 1030, 262, 24)], WHITE))
    a.append(blob([("c", 1090, 690, 40), ("c", 1160, 676, 46), ("c", 1230, 692, 34)], WHITE))
    a.append(figure(1220, 300, 32, "worried", look=(-1, 0.1), arms=((-1.4, -0.7), (1.0, 0.9)), legs=((-0.5, 3.4), (0.5, 3.4))))
    return "".join(a), text(["THE", "MOUNTAIN"], 64, 140, 92)


# 2 ── The Moment Before · Challenger (cold launch pad) ────────────────────────────────────────
def s2():
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(1130, 330, 0.5)]
    a.append(poly([(0, 610), (420, 585), (900, 600), (1280, 575), (1280, 720), (0, 720)], PAPER))     # frost ground
    # service tower with icicles
    a.append(rect(470, 130, 92, 470, BR))
    for y in range(190, 580, 70):
        a.append(line(470, y, 562, y + 60, 6))
        a.append(line(562, y, 470, y + 60, 6))
    for y in (230, 380, 520):
        a.append(rect(400, y, 86, 22, BR, 4, 8))
        for k in range(4):
            x = 410 + k * 20
            a.append(poly([(x, y + 22), (x + 14, y + 22), (x + 7, y + 22 + 46 - k * 6)], WHITE, 5))
    # shuttle stack: tank, two boosters, orbiter
    for x in (216, 384):
        a.append(poly([(x, 200), (x + 26, 140), (x + 52, 200)], INK))
        a.append(rect(x, 195, 52, 400, WHITE, 26))
        a.append(rect(x, 520, 52, 74, INK, 20))
    a.append(rect(282, 120, 104, 480, TAN, 52))
    a.append(poly([(302, 270), (334, 200), (366, 270), (366, 540), (302, 540)], WHITE))
    a.append(poly([(302, 500), (250, 580), (302, 580)], WHITE))
    a.append(poly([(366, 500), (418, 580), (366, 580)], WHITE))
    a.append(rect(324, 235, 20, 26, INK, 8, 0))
    # engineer with a thermometer, breath puff
    a.append(blob([("c", 838, 388, 12), ("c", 822, 396, 9), ("c", 852, 396, 8)], WHITE, 6))
    a.append(figure(920, 400, 46, "worried", look=(-1, -0.6), arms=((-1.5, 0.2), (1.0, 1.2)), prop=thermometer(920 - 1.5 * 46, 400 + 1.22 * 46 + 0.2 * 46 - 30, 0.8), legs=((-0.5, 3.4), (0.5, 3.4))))
    return "".join(a), text(["COLDEST", "LAUNCH"], 600, 175, 92)


# 3 ── The Impossible Scene · Comet in a water tank (no words) ─────────────────────────────────
def s3():
    a = [rect(0, 0, W, H, BR, 0, 0)]
    for x in (120, 470, 820):
        a.append(rect(x, 18, 300, 52, SKY, 6, 8))
    a.append(rect(0, 640, W, 80, TAN))
    a.append(rect(100, 236, 1080, 392, TAN, 26))
    a.append(rect(140, 280, 1000, 310, SKY, 14))
    # airliner (rounded windows; fin is the red accent)
    a.append(rect(240, 385, 790, 88, WHITE, 44))
    a.append(poly([(945, 388), (990, 296), (1058, 296), (1020, 388)], RED))
    a.append(poly([(950, 430), (1060, 412), (1072, 446), (950, 460)], WHITE))
    a.append(poly([(560, 452), (720, 452), (650, 545), (600, 545)], WHITE))
    a.append(f'<ellipse cx="600" cy="478" rx="44" ry="15" fill="{PAPER}" stroke="{INK}" stroke-width="8"/>')
    for i in range(14):
        a.append(f'<ellipse cx="{345 + i * 40}" cy="425" rx="9" ry="12" fill="{INK}"/>')
    a.append(poly([(262, 405), (300, 400), (300, 440), (268, 446)], INK, 4))
    for bx, by, br_ in ((200, 350, 10), (230, 320, 7), (1090, 520, 9), (1110, 470, 6), (450, 540, 8)):
        a.append(circ(bx, by, br_, WHITE, 5))
    a.append(path("M 140 285 Q 300 262 460 285 T 780 285 T 1140 285", "none", 6))
    for cx, cl, look in ((330, "calm", (0.9, 0.6)), (930, "calm", (-0.9, 0.6))):
        pr = clipboard(cx - 1.0 * 32, 118 + 1.22 * 32 + 0.7 * 32, 0.8, -8) if cx < 600 else None
        a.append(figure(cx, 118, 32, cl, look=look, arms=((-1.0, 0.7), (1.0, 0.7)), legs=((-0.4, 3.5), (0.4, 3.5)), prop=pr))
    return "".join(a), ""


# 4 ── Object on Trial · Hyatt connection (ink, one hero) ──────────────────────────────────────
def s4():
    a = [rect(0, 0, W, H, INK, 0, 0), edge()]
    a.append(rect(846, 14, 80, 290, TAN, 10))                                   # rod from above
    a.append(rect(400, 290, 900, 150, PAPER, 14))                               # steel box beam
    a.append(line(400, 365, 1290, 365, 6))
    a.append(rect(846, 440, 80, 290, TAN, 10))                                  # rod below
    a.append(f'<ellipse cx="886" cy="452" rx="190" ry="38" fill="{WHITE}" stroke="{INK}" stroke-width="{SW}"/>')   # washer
    a.append(poly([(761, 548), (823, 474), (949, 474), (1011, 548), (949, 622), (823, 622)], RED))                  # the nut (accent)
    a.append(path("M 700 442 l -44 -58 l 34 16 l -30 -66", "none", 10, RED))                                        # cracks in the beam
    a.append(path("M 1072 442 l 44 -58 l -34 16 l 30 -66", "none", 10, RED))
    return "".join(a), text(["LOAD", "DOUBLED"], 64, 130, 92)


# 5 ── The Cutaway · Big Dig anchor bolt ───────────────────────────────────────────────────────
def s5():
    import random
    random.seed(7)
    a = [rect(0, 0, W, H, BR, 0, 0)]
    a.append(rect(0, 150, W, 260, TAN, 0, SW))                                  # concrete roof slab
    for _ in range(50):
        x, y = random.randint(20, 1260), random.randint(170, 392)
        if 470 < x < 960:
            continue
        a.append(circ(x, y, random.randint(3, 6), INK, 0))                      # aggregate speckle
    a.append(rect(0, 410, W, 310, INK, 0, 0))                                   # tunnel below
    a.append(rect(0, 664, W, 56, BR))
    a.append(rect(470, 190, 480, 220, WHITE, 6))                                # cutaway: epoxy-filled hole
    a.append(rect(500, 190, 420, 62, INK, 0, 0))                                # gap where the bolt has slid down
    a.append(rect(672, 252, 76, 320, RED, 8, 8))                                # anchor bolt (accent)
    for y in (470, 490, 510, 530, 550):
        a.append(line(676, y, 744, y, 6))                                       # bolt thread
    a.append('<g transform="rotate(-2 710 610)">' + rect(280, 566, 860, 96, PAPER, 14) + circ(710, 566, 40, PAPER, 8) + "</g>")   # heavy hung ceiling panel
    for x in (350, 1070):
        a.append(rect(x - 16, 412, 32, 160, TAN, 6, 8))                         # neighbouring anchors, still holding
    a.append(figure(140, 530, 40, "worried", look=(1, -0.9), arms=((-1.2, 0.8), (1.2, 0.8)), legs=((-0.5, 3.3), (0.5, 3.3))))
    return "".join(a), text(["26 TONS"], 64, 118, 96)


# 6 ── The Giant Number · Tacoma Narrows ───────────────────────────────────────────────────────
def s6():
    import math
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(880, 80, 0.8), cloud(1140, 160, 0.55)]
    a.append(poly([(560, 570), (700, 420), (860, 480), (1010, 400), (1160, 470), (1280, 420), (1280, 640), (560, 640)], LG))
    a.append(poly([(0, 580), (1280, 580), (1280, 720), (0, 720)], DG))
    a.append(poly([(860, 720), (920, 625), (1280, 630), (1280, 720)], LG))
    for x in (735, 1150):
        a.append(rect(x, 190, 40, 420, BR))
        a.append(line(x, 300, x + 40, 350, 6)); a.append(line(x + 40, 300, x, 350, 6))
    yc = lambda x: 190 + 200 * (1 - ((x - 955) / 195) ** 2)
    yd = lambda x: 480 + 70 * math.sin(math.pi * (x - 560) / 720) * math.sin((x - 560) / 68)
    for x in range(780, 1140, 36):
        a.append(line(x, yc(x), x, yd(x), 5))
    cable = "M 580 480 L 755 190 " + " ".join(f"L {x} {yc(x):.1f}" for x in range(760, 1150, 10)) + " L 1170 190 L 1280 440"
    a.append(path(cable, "none", 8))
    deck = "M " + " L ".join(f"{x} {yd(x):.1f}" for x in range(560, 1290, 8))
    a.append(path(deck, "none", 46)); a.append(path(deck, "none", 22, TAN)); a.append(path(deck, "none", 8, RED))
    a.append(poly([(775, 195), (900, 208), (775, 240)], RED))                                            # windsock blowing flat
    a.append(figure(1010, 512, 30, "worried", look=(-1, -0.6), arms=((-0.9, -0.8), (0.9, -0.8)), legs=((-0.5, 3.4), (0.5, 3.4))))
    return "".join(a), text(["42"], 64, 430, 300) + text(["MPH"], 70, 590, 130)


# 7 ── The Diptych · Quebec Bridge (two single-panel images composited) ─────────────────────────
def s7():
    a = [rect(0, 0, 630, H, SKY, 0, 0), rect(650, 0, 630, H, SKY, 0, 0)]
    a.append(path("M 250 770 Q 480 380 240 -50", "none", 124))                                            # left: the bowed chord (accent)
    a.append(path("M 250 770 Q 480 380 240 -50", "none", 96, RED))
    for t in range(1, 8):
        y = 728 - t * 96
        x = 250 + (1 - (abs(y - 360) / 400) ** 1.5) * 118
        a.append(rect(x - 48, y, 96, 16, TAN, 4, 5))
    a.append(poly([(0, 612), (630, 612), (630, 720), (0, 720)], DG))
    a.append(figure(520, 470, 42, "worried", look=(-0.9, -0.3), arms=((-1.5, -0.7), (0.9, 0.9)), legs=((-0.5, 3.3), (0.5, 3.3))))
    a.append(poly([(650, 545), (1280, 545), (1280, 720), (650, 720)], DG))                                # right: the span in the river (pale)
    a.append(poly([(650, 450), (720, 430), (800, 470), (830, 545), (650, 545)], LG))
    a.append(rect(690, 170, 76, 300, BR, 8))                                                              # standing pier
    a.append(poly([(766, 240), (1040, 400), (1040, 490), (766, 340)], TAN))                               # cantilever arm sagging
    for k in range(6):
        x = 790 + k * 42
        a.append(line(x, 262 + k * 24, x + 42, 312 + k * 24, 6))
    a.append(poly([(1040, 400), (1170, 570), (1100, 626), (1040, 490)], TAN))                             # arm broken into the water
    a.append(poly([(1280, 290), (1090, 430), (1130, 510), (1280, 400)], TAN))                             # fallen truss
    a.append(poly([(880, 570), (1050, 545), (1075, 605), (895, 632)], TAN))
    a.append(blob([("c", 1080, 620, 46), ("c", 1150, 600, 56), ("c", 1230, 622, 42), ("c", 930, 640, 36)], WHITE, 8))
    a.append(rect(630, 0, 20, H, INK, 0, 0))
    return "".join(a), ""


# 8 ── Nobody Notices · Vasa ───────────────────────────────────────────────────────────────────
def s8():
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(1030, 70, 0.8), cloud(1215, 185, 0.45)]
    a.append(rect(0, 480, W, 240, DG, 0, 0))
    ship = []
    for x, top in ((700, 110), (900, 70), (1090, 130)):
        ship.append(line(x, 350, x, top - 20, 12))
    ship.append(poly([(650, 150), (770, 150), (790, 250), (630, 250)], PAPER))
    ship.append(poly([(840, 100), (960, 100), (980, 210), (820, 210)], PAPER))
    ship.append(poly([(1040, 160), (1140, 160), (1156, 250), (1024, 250)], PAPER))
    ship.append(poly([(400, 400), (1090, 372), (1130, 250), (1200, 222), (1250, 236), (1246, 350), (1190, 480), (1040, 585), (760, 622), (520, 590), (440, 490)], BR))
    ship.append(poly([(400, 400), (1090, 372), (1094, 398), (406, 426)], TAN))
    for x in range(530, 1040, 96):
        ship.append(rect(x, 444, 34, 32, INK, 4, 0))
    for x in range(560, 1030, 96):
        ship.append(rect(x, 512, 34, 32, RED, 4, 6))
    a.append('<g transform="translate(20 0) rotate(-9 820 490)">' + "".join(ship) + "</g>")
    a.append(poly([(0, 520), (300, 500), (560, 540), (900, 525), (1280, 540), (1280, 720), (0, 720)], DG))
    for x, y, s in ((560, 585, 1), (900, 620, 1.1), (1120, 590, 0.9)):
        a.append(blob([("c", x, y, 24 * s), ("c", x + 44 * s, y - 6, 28 * s), ("c", x + 92 * s, y, 22 * s), ("r", x - 24 * s, y, 140 * s, 24 * s, 12)], PAPER, 8))
    a.append(poly([(0, 575), (250, 555), (410, 630), (410, 720), (0, 720)], LG))
    for x in (70, 170, 270):
        a.append(figure(x, 455, 26, "calm", look=(1, -0.4), arms=((-1.1, -1.1), (1.1, 0.8)), legs=((-0.5, 3.4), (0.5, 3.4))))
    return "".join(a), text(["LIGHT", "BREEZE"], 64, 135, 88)


# 9 ── Seat of the Decider · Blackout control room ──────────────────────────────────────────────
def s9():
    a = [rect(0, 0, W, H, INK, 0, 0), edge()]
    a.append(rect(800, 100, 400, 380, SKY, 14))                                         # window: what he cannot see
    a.append(poly([(800, 410), (1200, 410), (1200, 480), (800, 480)], DG, 0))
    a.append(blob([("c", 1110, 380, 60), ("c", 1160, 350, 48), ("c", 1060, 370, 44)], DG))
    a.append(rect(1102, 400, 24, 80, BR, 4, 6))
    a.append(line(830, 250, 830, 480, 10))
    a.append(path("M 810 170 Q 960 290 1104 342", "none", 12, RED))                      # power line touching the tree (accent)
    a.append(rect(800, 100, 400, 380, "none", 14, 14))
    a.append(rect(0, 545, 800, 175, BR))                                                 # console desk
    for x in (50, 320):
        a.append(rect(x, 230, 250, 200, SKY, 12))
        a.append(rect(x + 105, 430, 40, 115, TAN, 4, 8))
    a.append(rect(730, 400, 44, 170, BR, 8))                                             # chair back
    a.append(circ(700, 512, 26, AM, 8))                                                  # desk lamp (amber, only on ink scenes)
    a.append(figure(668, 372, 74, "calm", look=(-1, 0.1), arms=((-1.5, 0.9), (-1.9, 1.2)), legs=((-1.0, 2.0), (-1.4, 2.0))))
    return "".join(a), text(["2:14 PM"], 64, 150, 100)


# 10 ── Close-Up Gaze · Flixborough bypass ───────────────────────────────────────────────────────
def s10():
    a = [rect(0, 0, W, H, SKY, 0, 0)]
    a.append(rect(0, 590, W, 130, DG, 0, 0))
    for x in (680, 1040):
        a.append(rect(x + 50, 300, 60, 60, PAPER, 10))
        a.append(rect(x, 340, 160, 250, TAN, 44))
    pipe = "M 840 480 L 890 480 L 890 545 L 990 425 L 990 480 L 1040 480"
    a.append(path(pipe, "none", 52)); a.append(path(pipe, "none", 30, RED))                # the temporary bypass (accent)
    for x in (826, 1004):
        a.append(rect(x, 456, 50, 50, PAPER, 6, 8))
    a.append(figure(300, 400, 200, "worried", look=(1.0, 0.25), arms=((-1.5, 1.0), (1.5, 1.0)), legs=((-0.5, 3.8), (0.5, 3.8))))
    return "".join(a), text(["NO", "DRAWING"], 610, 112, 84)


SCENES = [
    ("01-tiny-under-the-giant", "Tiny Under the Giant", "Vajont", s1),
    ("02-the-moment-before", "The Moment Before", "Challenger", s2),
    ("03-the-impossible-scene", "The Impossible Scene", "Comet", s3),
    ("04-object-on-trial", "Object on Trial", "Hyatt Regency", s4),
    ("05-the-cutaway", "The Cutaway", "Big Dig", s5),
    ("06-the-giant-number", "The Giant Number", "Tacoma Narrows", s6),
    ("07-the-diptych", "The Diptych", "Quebec Bridge", s7),
    ("08-nobody-notices", "Nobody Notices", "Vasa", s8),
    ("09-seat-of-the-decider", "Seat of the Decider", "2003 Blackout", s9),
    ("10-close-up-gaze", "Close-Up Gaze", "Flixborough", s10),
]
