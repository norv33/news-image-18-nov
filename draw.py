#!/usr/bin/env python3
"""Draw entry.png v2: clean light infographic, Wed 18 Nov 2026.

Design (deliberately unlike v1's navy-amber newspaper + hand-drawn map):
white page, giant black date, six numbered rows, each with its own
region colour chip, bold headline + one summary line, and a dark
stats footer. 1024x1024, flat colours, DejaVu fonts.
Run: python3 draw.py -> entry.png (in this directory)."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
WHITE = (255, 255, 255)
PAGE = (250, 249, 246)
INK = (17, 17, 17)
GREY = (102, 102, 102)
HAIR = (222, 220, 214)
RED = (200, 38, 38)
FOOT = (28, 30, 34)
FOOT_LBL = (168, 172, 180)

FD = "/usr/share/fonts/truetype/dejavu/"

def font(name, size):
    return ImageFont.truetype(FD + name, size)

KICK = font("DejaVuSans-Bold.ttf", 22)
DATE = font("DejaVuSans-Bold.ttf", 74)
SUB = font("DejaVuSans.ttf", 20)
NUM = font("DejaVuSans-Bold.ttf", 40)
HEAD = font("DejaVuSans-Bold.ttf", 30)
BODY = font("DejaVuSans.ttf", 21)
TAG = font("DejaVuSans-Bold.ttf", 15)
STAT_N = font("DejaVuSans-Bold.ttf", 34)
STAT_L = font("DejaVuSans.ttf", 14)

img = Image.new("RGB", (W, H), PAGE)
d = ImageDraw.Draw(img)
M = 36
RIGHT = W - M

# ---- header -------------------------------------------------------------
d.text((M, 30), "THE WORLD IN ONE DAY", font=KICK, fill=RED)
d.text((M, 58), "18 NOVEMBER 2026", font=DATE, fill=INK)
d.text((M, 142), "WEDNESDAY  ·  SIX STORIES FROM AROUND THE GLOBE",
       font=SUB, fill=GREY)
d.rectangle([M, 170, RIGHT, 174], fill=RED)

# ---- six stories --------------------------------------------------------
ROWS = [
    ("01", (200, 38, 38), "MIDDLE EAST",
     "U.S. STRIKES IRAN, IRAN HITS BACK",
     "U.S. bombs a missile site on Qeshm Island; Iran fires drones "
     "at U.S. bases in Bahrain and Kuwait."),
    ("02", (37, 99, 235), "EUROPE",
     "KERCH BRIDGE HIT AGAIN",
     "Ukraine strikes the Crimea bridge a second day; part of the "
     "road span collapses."),
    ("03", (14, 124, 102), "ASIA",
     "TRUMP, XI AND PUTIN MEET",
     "The three leaders hold a summit in Shenzhen on Thursday 19 November."),
    ("04", (109, 40, 217), "UNITED STATES",
     "DEMOCRATS TAKE THE SENATE",
     "Mary Peltola wins Alaska's seat; Democrats gain 56 Senate seats."),
    ("05", (234, 88, 12), "AFRICA",
     "EBOLA CASES MORE THAN DOUBLE",
     "The outbreak in DR Congo passes 11,000 cases and 5,400 deaths."),
    ("06", (190, 24, 93), "UNITED STATES",
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

ROW_Y = 174
ROW_H = 128
TX = 140                      # text column x
TW = RIGHT - TX               # text column width

for i, (num, color, tag, head, body) in enumerate(ROWS):
    y = ROW_Y + i * ROW_H
    # number chip
    d.rounded_rectangle([M, y + 22, M + 84, y + 106], radius=14, fill=color)
    nw = d.textlength(num, font=NUM)
    d.text((M + (84 - nw) / 2, y + 40), num, font=NUM, fill=WHITE)
    # tag, right aligned
    tw = d.textlength(tag, font=TAG)
    d.text((RIGHT - tw, y + 26), tag, font=TAG, fill=color)
    # headline
    d.text((TX, y + 22), head, font=HEAD, fill=INK)
    # summary, up to two lines
    lines = wrap(body, BODY, TW)[:2]
    for j, ln in enumerate(lines):
        d.text((TX, y + 62 + j * 27), ln, font=BODY, fill=GREY)
    # hairline between rows
    if i < len(ROWS) - 1:
        d.line([M, y + ROW_H, RIGHT, y + ROW_H], fill=HAIR, width=2)

# ---- dark stats footer --------------------------------------------------
FY = ROW_Y + 6 * ROW_H        # 942
d.rectangle([0, FY, W, H], fill=FOOT)
STATS = [
    ("11,000+", "EBOLA CASES IN DR CONGO"),
    ("56", "SENATE SEATS GAINED"),
    ("26 YEARS", "MEASLES-FREE, ENDED"),
]
SEG = W // 3
for i, (n, lbl) in enumerate(STATS):
    cx = i * SEG + SEG // 2
    nw = d.textlength(n, font=STAT_N)
    d.text((cx - nw / 2, FY + 12), n, font=STAT_N, fill=WHITE)
    lw = d.textlength(lbl, font=STAT_L)
    d.text((cx - lw / 2, FY + 52), lbl, font=STAT_L, fill=FOOT_LBL)

img.save("entry.png", optimize=True)
print("wrote entry.png")
