#!/usr/bin/env python3
"""Draw entry.png v3: dark breaking-news broadcast, Wed 18 Nov 2026.

Third identity for this bounty, unlike v1 (navy-amber newspaper with a
hand-drawn world map) and v2 (bright white page, numbered rows, dark
stats footer): a near-black live-broadcast screen. Red LIVE pill and
amber kicker over a giant white date, then six full-width dark bands,
each with a coloured side bar, a flat pictogram and a bold headline
plus one summary, closed by a red live-ticker strip. 1024x1024,
flat colours, DejaVu fonts.
Run: python3 draw.py -> entry.png (in this directory)."""

import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (11, 13, 17)
CARD = (24, 29, 37)
CARD_EDGE = (48, 55, 66)
WHITE = (245, 246, 248)
MUTED = (168, 175, 186)
BODY_GREY = (198, 203, 212)
RED = (214, 40, 40)
AMBER = (255, 176, 32)
TICKER = (178, 28, 28)

FD = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FD + name, size)


F_LIVE = font("DejaVuSans-Bold.ttf", 20)
F_KICK = font("DejaVuSans-Bold.ttf", 22)
F_DATE = font("DejaVuSans-Bold.ttf", 68)
F_SUB = font("DejaVuSans.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 27)
F_BODY = font("DejaVuSans.ttf", 20)
F_TAG = font("DejaVuSans-Bold.ttf", 15)
F_TICK = font("DejaVuSans-Bold.ttf", 21)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
M = 32
RIGHT = W - M

# ---- broadcast header ---------------------------------------------------
d.rounded_rectangle([M, 28, M + 118, 28 + 36], radius=18, fill=RED)
d.ellipse([M + 20, 28 + 12, M + 32, 28 + 24], fill=WHITE)
d.text((M + 42, 28 + 7), "LIVE", font=F_LIVE, fill=WHITE)
d.text((M + 136, 28 + 8), "BREAKING NEWS", font=F_KICK, fill=AMBER)
_w = d.textlength("THE WORLD", font=F_KICK)
d.text((RIGHT - _w, 28 + 8), "THE WORLD", font=F_KICK, fill=MUTED)

d.text((M, 76), "18 NOVEMBER 2026", font=F_DATE, fill=WHITE)
d.text((M, 152), "WEDNESDAY  ·  SIX STORIES FROM AROUND THE WORLD",
       font=F_SUB, fill=MUTED)
d.rectangle([M, 184, RIGHT, 188], fill=RED)

# ---- pictograms (flat, drawn from primitives) ---------------------------
def starburst(cx, cy, color):
    r = 34
    pts = []
    for i in range(16):
        ang = math.pi * i / 8 - math.pi / 2
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=color)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=BG)


def bridge(cx, cy, color):
    d.arc([cx - 40, cy - 26, cx + 40, cy + 46], start=180, end=360,
          fill=color, width=6)
    for dx in (-26, 0, 26):
        d.line([cx + dx, cy - 8, cx + dx, cy + 22], fill=color, width=5)
    d.line([cx - 44, cy + 22, cx + 44, cy + 22], fill=color, width=7)


def summit(cx, cy, color):
    for dx in (-30, 0, 30):
        d.ellipse([cx + dx - 11, cy - 22, cx + dx + 11, cy],
                  fill=color)
    d.line([cx - 42, cy + 16, cx + 42, cy + 16], fill=color, width=6)


def ballot(cx, cy, color):
    d.rectangle([cx - 26, cy - 6, cx + 26, cy + 30], outline=color, width=5)
    d.line([cx - 18, cy + 12, cx - 5, cy + 24, cx + 20, cy - 12],
           fill=color, width=6)


def virus(cx, cy, color):
    for i in range(10):
        ang = math.pi * 2 * i / 10
        x1 = cx + 16 * math.cos(ang)
        y1 = cy + 16 * math.sin(ang)
        x2 = cx + 34 * math.cos(ang)
        y2 = cy + 34 * math.sin(ang)
        d.line([x1, y1, x2, y2], fill=color, width=5)
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=color)
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=BG)


def shield(cx, cy, color):
    pts = [(cx, cy - 32), (cx + 26, cy - 22), (cx + 26, cy + 4),
           (cx, cy + 32), (cx - 26, cy + 4), (cx - 26, cy - 22)]
    d.polygon(pts, outline=color, width=5)
    d.line([cx, cy - 12, cx, cy + 12], fill=color, width=5)
    d.line([cx - 10, cy, cx + 10, cy], fill=color, width=5)


ICONS = [starburst, bridge, summit, ballot, virus, shield]

# ---- six story bands ----------------------------------------------------
STORIES = [
    ((255, 70, 70), "MIDDLE EAST",
     "U.S. STRIKES IRAN — IRAN FIRES BACK",
     "U.S. bombs a missile site on Qeshm Island; Iran launches drones "
     "at U.S. bases in Bahrain and Kuwait."),
    ((86, 170, 255), "EUROPE",
     "KERCH BRIDGE HIT FOR A SECOND DAY",
     "Ukraine strikes the Crimea bridge again; part of the road span "
     "collapses."),
    ((255, 176, 32), "ASIA",
     "TRUMP, XI AND PUTIN MEET IN SHENZHEN",
     "The three leaders hold a summit in Shenzhen on Thursday "
     "19 November."),
    ((178, 132, 255), "UNITED STATES",
     "DEMOCRATS WIN THE SENATE",
     "Mary Peltola takes Alaska's seat; Democrats gain 56 Senate seats."),
    ((255, 122, 26), "AFRICA",
     "EBOLA OUTBREAK MORE THAN DOUBLES",
     "DR Congo passes 11,000 cases and 5,400 deaths in the outbreak."),
    ((255, 92, 168), "UNITED STATES",
     "U.S. LOSES MEASLES-FREE STATUS",
     "After 26 years: 5,400+ cases and 10 deaths across the country."),
]


def wrap(text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


BAND_Y = 204
BAND_H = 112
GAP = 10
TX = 170
TW = RIGHT - TX - 8

for i, (color, tag, head, body) in enumerate(STORIES):
    y = BAND_Y + i * (BAND_H + GAP)
    d.rounded_rectangle([M, y, RIGHT, y + BAND_H], radius=12,
                        fill=CARD, outline=CARD_EDGE, width=1)
    d.rectangle([M, y + 10, M + 7, y + BAND_H - 10], fill=color)
    ICONS[i](104, y + BAND_H // 2, color)
    d.text((TX, y + 14), head, font=F_HEAD, fill=WHITE)
    tw = d.textlength(tag, font=F_TAG)
    d.text((RIGHT - 16 - tw, y + 18), tag, font=F_TAG, fill=color)
    lines = wrap(body, F_BODY, TW)[:2]
    for j, ln in enumerate(lines):
        d.text((TX, y + 54 + j * 26), ln, font=F_BODY, fill=BODY_GREY)

# ---- live ticker strip ----------------------------------------------------
TY = BAND_Y + 6 * BAND_H + 5 * GAP + 8   # 934
d.rectangle([0, TY, W, H], fill=TICKER)
tick1 = "QESHM ISLAND STRUCK   ·   KERCH BRIDGE DOWN   ·   SHENZHEN SUMMIT"
tick2 = "SENATE FLIPS   ·   EBOLA 11,000+   ·   MEASLES-FREE STATUS LOST"
for j, tick in enumerate((tick1, tick2)):
    tw = d.textlength(tick, font=F_TICK)
    d.text(((W - tw) / 2, TY + 12 + j * 34), tick, font=F_TICK, fill=WHITE)

img.save("entry.png", optimize=True)
print("wrote entry.png")
