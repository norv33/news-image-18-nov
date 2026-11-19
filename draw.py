#!/usr/bin/env python3
"""Draw entry.png v4: warm magazine-cover data poster, Wed 18 Nov 2026.

Fourth identity for this bounty, unlike v1 (navy-amber newspaper with
a hand-drawn world map and pins), v2 (bright white page, six numbered
rows, giant black date) and v3 (near-black breaking-news broadcast,
red LIVE pill, six dark bands, red ticker): a warm magazine cover.
A sunset illustration panel crowns the page (amber-to-plum sky, sun,
city skyline, a bridge, three leaders at a summit table), a red
banner carries the date in huge white type, and the six stories sit
in a 2x3 grid of cream cards, each with a thick colour bar, a giant
number, a bold headline and a stat chip. 1024x1024, flat shapes,
DejaVu fonts, no external assets, no network.
Run: python3 draw.py -> entry.png (in this directory)."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 238, 221)      # warm cream page
CARD = (255, 253, 247)       # card white
INK = (38, 28, 24)           # near-black warm ink
MUTED = (122, 105, 88)       # warm grey-brown
RULE = (214, 198, 170)       # hairline
RED = (193, 39, 45)          # date banner red
PLUM = (58, 31, 77)          # skyline silhouette
SUN = (255, 214, 120)        # sun disc

FD = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FD + name, size)


F_MAST = font("DejaVuSerif-Bold.ttf", 78)
F_KICK = font("DejaVuSans-Bold.ttf", 23)
F_DATE = font("DejaVuSans-Bold.ttf", 31)
F_NUM = font("DejaVuSans-Bold.ttf", 46)
F_TAG = font("DejaVuSans-Bold.ttf", 13)
F_HEAD = font("DejaVuSans-Bold.ttf", 22)
F_BODY = font("DejaVuSans.ttf", 17)
F_STAT = font("DejaVuSans-Bold.ttf", 15)
F_FOOT = font("DejaVuSans.ttf", 15)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 28
RIGHT = W - M


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# ---- sunset illustration panel -------------------------------------------
PX0, PY0, PX1, PY1 = M, 24, RIGHT, 292
TOP_C = (247, 183, 51)       # amber sky
MID_C = (242, 122, 60)       # orange
BOT_C = (122, 59, 143)       # plum dusk
steps = 60
for i in range(steps):
    t = i / (steps - 1)
    if t < 0.5:
        c = lerp(TOP_C, MID_C, t * 2)
    else:
        c = lerp(MID_C, BOT_C, (t - 0.5) * 2)
    y0 = PY0 + (PY1 - PY0) * i // steps
    y1 = PY0 + (PY1 - PY0) * (i + 1) // steps
    d.rectangle([PX0, y0, PX1, y1], fill=c)

# sun with a soft halo, upper right of the panel
sx, sy, sr = 838, 108, 46
d.ellipse([sx - sr - 16, sy - sr - 16, sx + sr + 16, sy + sr + 16],
          fill=(250, 196, 90))
d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=SUN)

# birds: three small chevrons in the clear sky right of the masthead
for bx, by, s in ((612, 66, 11), (654, 52, 8), (690, 70, 9)):
    d.arc([bx - s, by - s // 2, bx, by + s // 2], start=200, end=340,
          fill=(255, 240, 200), width=3)
    d.arc([bx, by - s // 2, bx + s, by + s // 2], start=200, end=340,
          fill=(255, 240, 200), width=3)

# skyline silhouette along the panel floor
base = PY1
skyline = [(0, 46), (52, 84), (104, 60), (150, 96), (206, 70),
           (258, 110), (312, 78), (368, 100), (420, 64), (470, 92),
           (520, 58), (566, 88), (618, 72), (668, 104), (720, 66),
           (770, 90), (820, 62), (872, 86), (920, 70)]
for i in range(len(skyline) - 1):
    x0, h0 = skyline[i]
    x1, h1 = skyline[i + 1]
    d.rectangle([PX0 + x0, base - h0, PX0 + x1, base], fill=PLUM)
# one tower with a lit spire
d.rectangle([PX0 + 560, base - 132, PX0 + 584, base], fill=PLUM)
d.polygon([(PX0 + 566, base - 132), (PX0 + 578, base - 132),
           (PX0 + 572, base - 158)], fill=PLUM)
# bridge arc on the left of the skyline
d.arc([PX0 + 60, base - 118, PX0 + 300, base + 6], start=180, end=360,
      fill=PLUM, width=8)
for dx in (100, 140, 180, 220, 260):
    d.line([PX0 + dx, base - 52, PX0 + dx, base - 8], fill=PLUM, width=5)
d.line([PX0 + 56, base - 8, PX0 + 304, base - 8], fill=PLUM, width=6)

# three summit figures seated at a table, right side of the panel
for fx in (700, 758, 816):
    d.ellipse([fx - 13, base - 96, fx + 13, base - 70], fill=PLUM)
    d.polygon([(fx - 17, base - 68), (fx + 17, base - 68),
               (fx + 11, base - 34), (fx - 11, base - 34)], fill=PLUM)
d.rectangle([PX0 + 668, base - 34, PX0 + 848, base - 26], fill=PLUM)
d.rectangle([PX0 + 682, base - 26, PX0 + 690, base], fill=PLUM)
d.rectangle([PX0 + 826, base - 26, PX0 + 834, base], fill=PLUM)

# masthead over the sunset, with a plum shadow for legibility
d.text((M + 22, 44), "THE WORLD", font=F_MAST, fill=(40, 18, 52))
d.text((M + 18, 40), "THE WORLD", font=F_MAST, fill=(255, 250, 238))
d.text((M + 20, 138), "IN ONE DAY  ·  SIX STORIES", font=F_KICK,
       fill=(255, 232, 180))

# ---- red date banner ------------------------------------------------------
DY0, DY1 = 300, 346
d.rectangle([M, DY0, RIGHT, DY1], fill=RED)
date = "WEDNESDAY  ·  18 NOVEMBER 2026"
dw = d.textlength(date, font=F_DATE)
d.text(((W - dw) / 2, DY0 + 7), date, font=F_DATE, fill=(255, 255, 255))

# ---- story cards: 2 rows x 3 columns --------------------------------------
STORIES = [
    ((192, 57, 43), "MIDDLE EAST", "U.S. STRIKES IRAN; IRAN FIRES BACK",
     "U.S. bombs a missile site on Qeshm Island; Iran fires drones "
     "at bases in Bahrain, Kuwait.",
     "QESHM ISLAND"),
    ((46, 111, 163), "EUROPE", "KERCH BRIDGE HIT A SECOND DAY",
     "Ukraine strikes the Crimea bridge again; part of the road span "
     "collapses.",
     "ROAD SPAN DOWN"),
    ((217, 142, 0), "ASIA", "TRUMP, XI AND PUTIN MEET",
     "The three leaders hold a summit in Shenzhen on Thursday "
     "19 November.",
     "SHENZHEN"),
    ((108, 74, 176), "UNITED STATES", "DEMOCRATS WIN THE SENATE",
     "Mary Peltola takes Alaska's seat; Democrats gain 56 Senate seats.",
     "56 SEATS"),
    ((224, 93, 31), "AFRICA", "EBOLA OUTBREAK MORE THAN DOUBLES",
     "DR Congo passes 11,000 cases and 5,400 deaths in the outbreak.",
     "11,000+ CASES"),
    ((194, 67, 122), "UNITED STATES", "U.S. LOSES MEASLES-FREE STATUS",
     "After 26 years: 5,400+ cases and 10 deaths.",
     "5,400+ CASES"),
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


GY0, GY1 = 366, 972
GAP = 16
CW = (RIGHT - M - 2 * GAP) // 3
CH = (GY1 - GY0 - GAP) // 2

for i, (color, tag, head, body, stat) in enumerate(STORIES):
    col, row = i % 3, i // 3
    x0 = M + col * (CW + GAP)
    y0 = GY0 + row * (CH + GAP)
    x1, y1 = x0 + CW, y0 + CH
    d.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=CARD,
                        outline=RULE, width=1)
    d.rectangle([x0 + 10, y0, x1 - 10, y0 + 10], fill=color)
    # giant number + region tag
    num = "%02d" % (i + 1)
    d.text((x0 + 18, y0 + 22), num, font=F_NUM, fill=color)
    tw = d.textlength(tag, font=F_TAG)
    d.text((x1 - 18 - tw, y0 + 40), tag, font=F_TAG, fill=color)
    d.line([x0 + 18, y0 + 84, x1 - 18, y0 + 84], fill=RULE, width=1)
    # headline, up to 3 lines
    lines = wrap(head, F_HEAD, CW - 36)[:3]
    for j, ln in enumerate(lines):
        d.text((x0 + 18, y0 + 98 + j * 28), ln, font=F_HEAD, fill=INK)
    # body, up to 3 lines
    blines = wrap(body, F_BODY, CW - 36)[:3]
    by = y0 + 98 + len(lines) * 28 + 8
    for j, ln in enumerate(blines):
        d.text((x0 + 18, by + j * 23), ln, font=F_BODY, fill=MUTED)
    # stat chip pinned to the card bottom
    sw = d.textlength(stat, font=F_STAT) + 24
    sy = y1 - 46
    d.rounded_rectangle([x0 + 18, sy, x0 + 18 + sw, sy + 30], radius=15,
                        fill=color)
    d.text((x0 + 30, sy + 6), stat, font=F_STAT, fill=(255, 255, 255))

# ---- footer ---------------------------------------------------------------
foot = "THE WORLD IN ONE DAY  ·  SIX STORIES FROM FIVE REGIONS"
fw = d.textlength(foot, font=F_FOOT)
d.text(((W - fw) / 2, 988), foot, font=F_FOOT, fill=MUTED)

img.save("entry.png", optimize=True)
print("wrote entry.png")
