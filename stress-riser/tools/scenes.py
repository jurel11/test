"""10 thumbnail style mockups (v2, after review). Each scene returns (art_layer, text_layer).
The art layer obeys the brief's 'no text / numbers / arrows / empty flat background' rules;
the words are a separate overlay added in the design tool. Every scene is lit (no black voids),
figures stand on light surfaces so their single-line limbs stay visible, and the red accent marks the culprit."""
import math
from lib import *


def edge(color=BR, w=14):
    return f'<rect x="{w/2}" y="{w/2}" width="{W-w}" height="{H-w}" fill="none" stroke="{color}" stroke-width="{w}"/>'


# 1 ── Tiny Under the Giant · Vajont ───────────────────────────────────────────────────────────
def s1():
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(1040, 70, 0.7), cloud(1210, 175, 0.42)]
    a.append(poly([(1120, 720), (1150, 470), (1210, 395), (1280, 375), (1280, 720)], BR))                        # far valley wall
    a.append(poly([(0, 0), (380, 0), (640, 470), (720, 720), (0, 720)], TAN))                                    # the mountain (pale)
    a.append(poly([(640, 470), (940, 470), (940, 720), (720, 720)], DG))                                         # reservoir
    a.append(poly([(130, 330), (300, 292), (450, 342), (560, 425), (622, 464), (430, 482), (250, 442), (120, 402)], RED))   # the slope that slid
    a.append(line(300, 292, 330, 402, 6)); a.append(line(450, 342, 400, 452, 6))
    for x, y, r in ((652, 450, 22), (600, 504, 16), (692, 494, 13)):
        a.append(circ(x, y, r, RED, 8))
    a.append(blob([("c", 664, 432, 32), ("c", 706, 400, 40), ("c", 748, 378, 32), ("c", 704, 444, 28)], WHITE))    # splash where it hit
    a.append(poly([(800, 470), (825, 350), (890, 262), (975, 222), (1050, 226), (1100, 262), (1125, 345), (1140, 470), (1112, 590), (1086, 700), (960, 700), (945, 470)], DG))   # the wave
    a.append(poly([(935, 306), (995, 306), (1052, 720), (915, 720)], PAPER))                                     # the dam: thin, tall, still standing
    a.append(blob([("c", 850, 300, 24), ("c", 915, 250, 28), ("c", 985, 226, 30), ("c", 1060, 240, 28), ("c", 1105, 290, 24)], WHITE))
    a.append(blob([("c", 985, 690, 34), ("c", 1035, 676, 40)], WHITE))
    a.append(figure(1215, 284, 32, "worried", look=(-1, 0.1), arms=((-1.4, -0.7), (1.0, 0.9)), legs=((-0.5, 3.4), (0.5, 3.4))))
    return "".join(a), title(["THE", "MOUNTAIN"], 90)


# 2 ── The Moment Before · Quebec Bridge, half built ───────────────────────────────────────────
def s2():
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(900, 100, 0.85), cloud(1170, 200, 0.5)]
    a.append(rect(0, 610, W, 110, DG, 0, 0))                                               # river
    for x, y, s in ((520, 650, 1), (840, 675, 1.1)):
        a.append(blob([("c", x, y, 22 * s), ("c", x + 40 * s, y - 6, 26 * s), ("c", x + 84 * s, y, 20 * s), ("r", x - 22 * s, y, 126 * s, 22 * s, 11)], PAPER, 8))
    a.append(poly([(0, 640), (430, 618), (430, 720), (0, 720)], LG))                       # bank
    a.append(rect(60, 300, 130, 340, BR, 6))                                                # anchor pier
    a.append(rect(40, 285, 170, 34, TAN, 6))
    top = "M 190 330 L 1150 300"                                                            # half-built cantilever truss stopping mid-air
    for k in range(0, 9):
        x = 190 + k * 120
        yt = 330 - (x - 190) * 30 / 960
        yb = 440 + 55 * math.sin(math.pi * (x - 190) / 960)
        a.append(line(x, yt, x, yb, 10))
        if k < 8:
            x2 = x + 120
            yt2 = 330 - (x2 - 190) * 30 / 960
            yb2 = 440 + 55 * math.sin(math.pi * (x2 - 190) / 960)
            a.append(line(x, yt, x2, yb2, 8))
    a.append(path(top, "none", 44)); a.append(path(top, "none", 22, TAN))
    bow = "M 190 440 Q 670 550 1150 440"
    a.append(path(bow, "none", 46)); a.append(path(bow, "none", 26, RED))                  # the bowed lower chord (accent)
    a.append(poly([(1150, 296), (1178, 288), (1178, 452), (1150, 448)], TAN))
    a.append(figure(330, 528, 34, "worried", look=(0.8, -0.9), arms=((-1.3, 0.9), (1.4, -1.0)), legs=((-0.5, 3.4), (0.5, 3.4))))
    return "".join(a), ""


# 3 ── The Impossible Scene · Comet fuselage in a water tank (plan view, wings out through seals) ─
def s3():
    a = [rect(0, 0, W, H, TAN, 0, 0), rect(0, 0, W, 100, BR, 0, 0)]
    a.append(line(0, 100, W, 100, SW))
    for x in (130, 480, 830):
        a.append(rect(x, 22, 300, 52, SKY, 6, 8))
    a.append(rect(150, 240, 980, 300, PAPER, 18))                                            # tank walls
    a.append(rect(172, 262, 936, 256, SKY, 10))                                              # water
    a.append(poly([(590, 362), (700, 362), (906, 150), (842, 150)], WHITE))                  # wings out through seals
    a.append(poly([(590, 420), (700, 420), (906, 632), (842, 632)], WHITE))
    a.append(rect(733, 224, 66, 56, BR, 6, 8)); a.append(rect(740, 502, 66, 56, BR, 6, 8))
    a.append(rect(846, 120, 62, 26, INK, 4, 0)); a.append(rect(846, 636, 62, 26, INK, 4, 0))  # jacks at the wing tips
    a.append(rect(226, 362, 840, 58, WHITE, 29))                                             # fuselage
    a.append(poly([(978, 362), (1044, 362), (1082, 296), (1040, 296)], WHITE))               # tailplane
    a.append(poly([(978, 420), (1044, 420), (1082, 486), (1040, 486)], WHITE))
    a.append(f'<ellipse cx="640" cy="336" rx="44" ry="15" fill="{PAPER}" stroke="{INK}" stroke-width="8"/>')
    a.append(f'<ellipse cx="640" cy="446" rx="44" ry="15" fill="{PAPER}" stroke="{INK}" stroke-width="8"/>')
    a.append(circ(400, 391, 27, "none", 20)); a.append(f'<circle cx="400" cy="391" r="27" fill="none" stroke="{RED}" stroke-width="10"/>')   # where a crack began (accent)
    for bx, by, br_ in ((210, 300, 9), (240, 480, 7), (1070, 500, 9), (300, 330, 6)):
        a.append(circ(bx, by, br_, WHITE, 5))
    a.append(figure(250, 596, 30, "calm", look=(0.9, -0.5), arms=((-1.0, 0.7), (1.0, 0.7)), prop=clipboard(250 - 30, 596 + 1.22 * 30 + 0.7 * 30, 0.8, -8), legs=((-0.4, 3.5), (0.4, 3.5))))
    a.append(figure(980, 596, 30, "calm", look=(-0.9, -0.5), arms=((-1.0, 0.7), (1.0, 0.7)), legs=((-0.4, 3.5), (0.4, 3.5))))
    return "".join(a), ""


# 4 ── Exhibit A · Hyatt connection on a plain paper card ─────────────────────────────────────
def s4():
    a = [rect(0, 0, W, H, PAPER, 0, 0)]
    a.append(rect(380, 300, 940, 150, TAN, 14))                                              # steel box beam (two channels)
    a.append(line(380, 375, 1290, 375, 6))
    a.append(rect(770, 368, 220, 16, INK, 0, 0))                                             # welded seam split open
    a.append(rect(846, 20, 76, 280, BR, 10))                                                 # upper rod (from the roof)
    a.append(rect(902, 460, 76, 250, BR, 10))                                                # lower rod (a separate rod, offset)
    a.append(f'<ellipse cx="880" cy="458" rx="160" ry="34" fill="{WHITE}" stroke="{INK}" stroke-width="{SW}"/>')    # washer pulled through
    a.append(poly([(750, 555), (815, 480), (945, 480), (1010, 555), (945, 630), (815, 630)], RED))                  # the nut (accent)
    a.append(edge(INK, 24))
    return "".join(a), title(["LOAD", "DOUBLED"], 96)


# 5 ── The Cutaway · Big Dig anchors pulling out of the roof slab ─────────────────────────────
def s5():
    import random
    random.seed(11)
    a = [rect(0, 0, W, H, BR, 0, 0)]
    a.append(rect(0, 175, W, 200, TAN, 0, SW))                                               # roof slab
    for _ in range(46):
        x, y = random.randint(20, 1260), random.randint(195, 360)
        if any(hx - 70 < x < hx + 70 for hx in (300, 640, 980)):
            continue
        a.append(circ(x, y, random.randint(3, 6), INK, 0))
    a.append(rect(0, 375, W, 289, PAPER, 0, 0))                                              # lit tunnel
    a.append(line(0, 375, W, 375, SW))
    a.append(rect(0, 664, W, 56, INK, 0, 0))                                                 # road surface
    for hx, gap in ((300, 60), (640, 46), (980, 8)):                                         # how far each anchor has slid
        a.append(rect(hx - 62, 228, 124, 147, WHITE, 6))                                      # epoxy-filled hole (cutaway)
        a.append(rect(hx - 46, 228, 92, 30 + gap, INK, 0, 0))                                # gap above the anchor
        a.append(rect(hx - 17, 228 + 30 + gap, 34, 330 - gap, RED, 5, 8))                    # anchor (accent)
    a.append('<g transform="rotate(-5 640 590)">' + rect(230, 560, 820, 96, WHITE, 14) + "</g>")   # heavy hung ceiling panel
    a.append(figure(120, 550, 38, "worried", look=(1, -0.9), arms=((-1.2, 0.8), (1.2, 0.8)), legs=((-0.5, 3.3), (0.5, 3.3))))
    return "".join(a), title(["26 TONS"], 96)


# 6 ── The Giant Number · Tacoma Narrows ───────────────────────────────────────────────────────
def s6():
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(900, 70, 0.75), cloud(1150, 150, 0.5)]
    a.append(poly([(560, 585), (700, 440), (860, 495), (1010, 420), (1160, 490), (1280, 440), (1280, 640), (560, 640)], LG))
    a.append(rect(0, 585, W, 135, DG, 0, 0))
    a.append(poly([(780, 720), (830, 640), (1010, 630), (1045, 720)], LG))
    for x in (735, 1150):
        a.append(rect(x, 175, 40, 410, BR))
        a.append(line(x, 290, x + 40, 340, 6)); a.append(line(x + 40, 290, x, 340, 6))
    yc = lambda x: 410 + 16 * math.sin((x - 580) / 80)
    ycab = lambda x: 175 + 190 * (1 - ((x - 955) / 195) ** 2)
    for x in range(790, 1130, 40):
        a.append(line(x, ycab(x), x, yc(x), 5))
    cable = "M 580 470 L 755 175 " + " ".join(f"L {x} {ycab(x):.1f}" for x in range(760, 1150, 10)) + " L 1170 175 L 1280 430"
    a.append(path(cable, "none", 8))
    x0, x1, step = 580, 1280, 10
    wfun = lambda x: 26 + 130 * abs(math.sin((x - x0) / 62)) * math.sin(math.pi * (x - x0) / (x1 - x0))
    segs = []
    for x in range(x0, x1, step):
        xa = x + step + 1
        col = RED if math.sin((x - x0) / 62) >= 0 else BR
        segs.append(f'<polygon points="{x},{yc(x) - wfun(x) / 2:.1f} {xa},{yc(xa) - wfun(xa) / 2:.1f} {xa},{yc(xa) + wfun(xa) / 2:.1f} {x},{yc(x) + wfun(x) / 2:.1f}" fill="{col}" stroke="{col}" stroke-width="1"/>')
    a.append("".join(segs))
    a.append(path("M " + " L ".join(f"{x} {yc(x) - wfun(x) / 2:.1f}" for x in range(x0, x1, 8)), "none", 8))
    a.append(path("M " + " L ".join(f"{x} {yc(x) + wfun(x) / 2:.1f}" for x in range(x0, x1, 8)), "none", 8))
    a.append(figure(900, 532, 30, "worried", look=(-0.3, -1.0), arms=((-0.9, -0.8), (0.9, -0.8)), legs=((-0.5, 3.3), (0.5, 3.3))))
    return "".join(a), title(["42"], 250, x=94, y=330) + title(["MPH"], 110, x=80, y=500)


# 7 ── The Odd True Detail · Challenger hearing, a rubber ring in ice water ──────────────────
def s7():
    a = [rect(0, 0, W, H, TAN, 0, 0), rect(0, 520, W, 200, BR, 0, 0), line(0, 520, W, 520, SW)]
    a.append(rect(900, 90, 280, 250, SKY, 12))                                                 # window
    a.append(line(1040, 90, 1040, 340, 8))
    for x, mood, look in ((620, "calm", (-0.6, 0.6)), (830, "worried", (-0.9, 0.7)), (1040, "calm", (-0.9, 0.5))):
        a.append(figure(x, 262, 48, mood, look=look, arms=((-1.5, 0.9), (1.5, 0.9)), legs=((-0.4, 3.0), (0.4, 3.0))))
    a.append(rect(90, 440, 1100, 46, PAPER, 8))                                                # long table
    a.append(rect(120, 486, 1040, 190, DG, 6))
    a.append(rect(160, 300, 150, 146, WHITE, 16, SW))                                          # glass of ice water
    a.append(rect(172, 340, 126, 94, SKY, 8, 0))
    for cx, cy in ((205, 370), (255, 392), (220, 416)):
        a.append(rect(cx - 20, cy - 20, 40, 40, WHITE, 8, 6))
    a.append(f'<circle cx="470" cy="405" r="34" fill="none" stroke="{INK}" stroke-width="34"/><circle cx="470" cy="405" r="34" fill="none" stroke="{RED}" stroke-width="18"/>')   # the rubber ring (accent)
    a.append(rect(420, 370, 100, 20, INK, 6, 0)); a.append(rect(420, 420, 100, 20, INK, 6, 0))
    a.append(rect(510, 384, 60, 42, TAN, 8, 6))
    return "".join(a), title(["ICE", "WATER"], 96)


# 8 ── The Crowd on the Shore · Vasa ───────────────────────────────────────────────────────────
def s8():
    a = [rect(0, 0, W, H, SKY, 0, 0), cloud(1060, 80, 0.8), cloud(1220, 190, 0.42)]
    a.append(poly([(0, 470), (200, 440), (420, 462), (420, 480), (0, 480)], LG))
    for x, w_, h_ in ((60, 46, 40), (140, 60, 34), (300, 50, 44)):
        a.append(rect(x, 436 - h_, w_, h_, BR, 4, 6))
    a.append(rect(0, 480, W, 240, DG, 0, 0))                                                 # sea
    ship = []
    for x, top in ((760, 110), (940, 70), (1100, 130)):
        ship.append(line(x, 380, x, top - 20, 12))
    ship.append(poly([(700, 150), (820, 150), (836, 250), (684, 250)], PAPER))
    ship.append(poly([(884, 100), (1004, 100), (1020, 210), (868, 210)], PAPER))
    ship.append(poly([(1050, 160), (1150, 160), (1164, 250), (1036, 250)], PAPER))
    ship.append(poly([(470, 420), (1130, 400), (1170, 260), (1230, 230), (1262, 246), (1258, 360), (1200, 480), (1040, 560), (800, 580), (580, 560), (500, 500)], BR))
    ship.append(poly([(470, 420), (1130, 400), (1134, 426), (476, 446)], TAN))
    for x in range(590, 1090, 90):
        ship.append(rect(x, 452, 34, 30, INK, 4, 0))
    for x in range(620, 1080, 90):
        ship.append(rect(x, 512, 40, 36, RED, 4, 6))                                        # the lower gunports, open (accent)
    a.append("".join(ship))
    for x, y, s in ((470, 600, 1), (760, 570, 1.1), (1060, 585, 0.9)):
        a.append(blob([("c", x, y, 22 * s), ("c", x + 40 * s, y - 6, 26 * s), ("c", x + 84 * s, y, 20 * s), ("r", x - 22 * s, y, 126 * s, 22 * s, 11)], PAPER, 8))
    a.append(poly([(0, 560), (250, 545), (410, 610), (410, 720), (0, 720)], TAN))           # shore
    for x in (70, 170, 270):
        a.append(figure(x, 450, 26, "calm", look=(1, -0.3), arms=((-1.0, 0.8), (1.0, 0.8)), legs=((-0.5, 3.4), (0.5, 3.4))))
    return "".join(a), title(["CALM", "DAY"], 96)


# 9 ── Seat of the Decider · Blackout control room ─────────────────────────────────────────────
def s9():
    a = [rect(0, 0, W, H, TAN, 0, 0), rect(0, 560, W, 160, BR, 0, 0), line(0, 560, W, 560, SW)]
    a.append(rect(870, 110, 320, 320, SKY, 14))                                              # window: the cause he cannot see yet
    a.append(poly([(870, 380), (1190, 380), (1190, 430), (870, 430)], LG, 0))
    a.append(blob([("c", 1110, 360, 48), ("c", 1152, 336, 38), ("c", 1070, 350, 34)], DG))
    a.append(rect(1102, 384, 22, 46, BR, 4, 6))
    a.append(path("M 880 210 Q 960 275 1040 210", "none", 10))                              # power line, still clear of the tree
    a.append(line(1040, 210, 1040, 140, 10))
    a.append(rect(870, 110, 320, 320, "none", 14, 14))
    a.append(rect(0, 490, 850, 70, PAPER, 8))                                                # console desk
    a.append(rect(0, 560, 850, 160, INK, 0, 0))
    a.append(rect(50, 290, 240, 190, INK, 12)); a.append(rect(66, 306, 208, 158, SKY, 6, 0))
    for y, wd in ((330, 150), (370, 110), (410, 170)):
        a.append(rect(84, y, wd, 22, WHITE, 6, 0))
    a.append(rect(330, 290, 240, 190, RED, 12)); a.append(rect(346, 306, 208, 158, PAPER, 6, 0))    # the frozen screen (accent frame)
    a.append(figure(690, 372, 82, "calm", look=(-1, 0.15), arms=((-1.3, 0.1), (-1.8, 0.14)), legs=((-0.4, 2.0), (0.4, 2.0))))
    return "".join(a), title(["LAST ALARM", "2:14 PM"], 90)


# 10 ── Close-Up Gaze · Flixborough bypass ──────────────────────────────────────────────────────
def s10():
    a = [rect(0, 0, W, H, SKY, 0, 0), rect(0, 600, W, 120, DG, 0, 0)]
    for x in (630, 1010):
        a.append(rect(x + 50, 322, 60, 56, PAPER, 10))
        a.append(rect(x, 360, 160, 240, TAN, 44))                                            # the two reactors still in place
    a.append(rect(830, 540, 130, 60, TAN, 8))                                                # the empty stand where reactor 5 was
    for x in (846, 926):
        a.append(rect(x, 560, 16, 40, BR, 4, 0))
    pipe = "M 790 480 L 850 480 L 850 550 L 940 430 L 940 480 L 1010 480"
    a.append(path(pipe, "none", 56)); a.append(path(pipe, "none", 32, RED))                # the bypass, dog-leg (accent)
    for x in (764, 986):
        a.append(rect(x, 452, 50, 56, PAPER, 6, 8))
        for k in range(1, 4):
            a.append(line(x + k * 12.5, 456, x + k * 12.5, 504, 4))
    a.append(figure(290, 405, 200, "worried", look=(1.0, 0.25), arms=((-1.5, 1.0), (1.5, 1.0)), legs=((-0.5, 3.8), (0.5, 3.8))))
    return "".join(a), title(["NO", "DRAWING"], 90, x=600)


SCENES = [
    ("01-tiny-under-the-giant", "Tiny Under the Giant", "Vajont", s1),
    ("02-the-moment-before", "The Moment Before", "Quebec Bridge", s2),
    ("03-the-impossible-scene", "The Impossible Scene", "Comet", s3),
    ("04-exhibit-a", "Exhibit A", "Hyatt Regency", s4),
    ("05-the-cutaway", "The Cutaway", "Big Dig", s5),
    ("06-the-giant-number", "The Giant Number", "Tacoma Narrows", s6),
    ("07-the-odd-true-detail", "The Odd True Detail", "Challenger", s7),
    ("08-the-crowd-on-the-shore", "The Crowd on the Shore", "Vasa", s8),
    ("09-seat-of-the-decider", "Seat of the Decider", "2003 Blackout", s9),
    ("10-close-up-gaze", "Close-Up Gaze", "Flixborough", s10),
]
