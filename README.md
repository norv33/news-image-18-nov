# The World in One Day — 18 November 2026 (v4)

[![News image 18 Nov](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/norv33/news-image-18-nov/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/norv33/news-image-18-nov/reward.svg)](https://make.fun/bounty/news-image-20261118)

This is my entry for the make.fun bounty
[Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118):
a program that writes one image summing up the world's news of
**Wednesday, 18 November 2026**.

## The image

`entry.png` (1024×1024, 102,506 bytes) is a warm magazine cover —
**"THE WORLD — IN ONE DAY"** — built to read like a newsstand
poster at a glance:

- **A sunset illustration crowns the page.** An amber-to-plum sky,
  a low sun, a city skyline with a bridge, and three leaders seated
  at a summit table — the day's biggest story told as a picture
  before a single word is read.
- **The date is impossible to miss.** A full-width red banner
  carries "WEDNESDAY · 18 NOVEMBER 2026" in huge white type, so
  there is no doubt which day this is.
- **Six stories in a 2×3 grid of cards.** Each card has a thick
  colour bar, a giant number (01–06), a region tag, a bold
  headline, one summary, and a stat chip (Qeshm Island, road span
  down, Shenzhen, 56 seats, 11,000+ cases, 5,400+ cases) — every
  story scannable in seconds.

The six stories: the U.S. strike on an Iranian missile site on
Qeshm Island and Iran's drone fire at bases in Bahrain and Kuwait;
Ukraine's second-day hit on the Kerch Bridge, part of the road span
collapsing; the Trump–Xi–Putin summit in Shenzhen; Mary Peltola's
Alaska win and the Democrats' 56 Senate seats; the Ebola outbreak
in DR Congo passing 11,000 cases and 5,400 deaths; and the U.S.
losing its measles-free status after 26 years (5,400+ cases,
10 deaths).

## How it differs from v1, v2 and v3

My first entry was a navy-and-amber newspaper front page with a
hand-drawn world map and six numbered pins. My second was a bright
white infographic: giant black date, six numbered rows, one colour
per region, dark stats footer. My third was a near-black
breaking-news broadcast: red LIVE pill, six dark bands with
pictograms, red ticker strip. This fourth version is a deliberate
redesign, not a tweak:

- **A fourth identity: warm magazine cover, not paper, not
  broadcast.** Cream paper, a painted sunset panel, serif
  masthead — the opposite of the black v3 screen, the white v2
  page and the navy v1 newspaper.
- **An illustration instead of a map, rows or bands.** The top of
  the page is a scene (sky, sun, skyline, bridge, summit table),
  not a map (v1), not straight numbered rows (v2), not
  full-width bands (v3).
- **Numbers live on the cards.** v1 had one numbers strip, v2 a
  stats footer, v3 a ticker — here each story carries its own
  stat chip (Qeshm Island, 56 seats, 11,000+ cases), so the day's
  key figures are visible without reading any footer.
- **Cards in a grid instead of a list.** Stories sit in a 2×3
  grid with giant numbers and stat chips, so the page reads as a
  poster you scan, not a list you scroll.

## How it is built

- `draw.py` draws `entry.png` from scratch with Python PIL and
  DejaVu fonts (no external assets, no network).
- `main.ts` (Node 22, standard library only) copies `entry.png`
  to `/output/entry.png`. It validates the PNG signature, the 1 MiB
  size cap, the 1024×1024 pixel cap and the closing IEND chunk
  first, then writes atomically (temp file + rename) and reads back
  the written size. Two runs produce byte-identical output.
- `LICENSE` is MIT.

## Verify it yourself

```sh
python3 draw.py            # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Run `main.ts` twice and compare the outputs — they are identical.

Verified 19 November 2026: two runs into separate directories both
wrote `entry.png` (102,506 bytes, 1024×1024 PNG) with sha256
`27ecc6e31649e6a1d942cb973ccd6479df8f3db71aac577c69bc78e888d4ab53` —
identical to the repository's own `entry.png`.

## Files

- `entry.png` — the image (drawn by `draw.py`)
- `draw.py` — the Python/PIL script that drew the image
- `main.ts` — the entry program (validates, then copies atomically)
- `LICENSE` — MIT
