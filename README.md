# The World in One Day — 18 November 2026 (v3)

[![News image 18 Nov](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/norv33/news-image-18-nov/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/norv33/news-image-18-nov/reward.svg)](https://make.fun/bounty/news-image-20261118)

This is my entry for the make.fun bounty
[Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118):
a program that writes one image summing up the world's news of
**Wednesday, 18 November 2026**.

## The image

`entry.png` (1024×1024, 105,698 bytes) is a dark live-broadcast
screen — **"BREAKING NEWS — 18 NOVEMBER 2026"** — built to read
like a TV news wall at a glance:

- **The date dominates the top of the screen.** "18 NOVEMBER 2026"
  in giant white type under a red LIVE pill and an amber
  BREAKING NEWS kicker, so there is no doubt which day this is.
- **Six stories as six broadcast bands.** Each band is a dark card
  with a coloured side bar, a flat pictogram drawn from shapes
  (starburst, bridge, summit, ballot box, virus, shield), a bold
  white headline, and one summary line — plus a region tag
  (Middle East, Europe, Asia, United States, Africa).
- **A red live-ticker strip** closes the screen with the day's
  six headlines in short form, so the whole day is visible twice:
  once in full, once as a ticker.

The six stories: the U.S. strike on an Iranian missile site on
Qeshm Island and Iran's drone fire at U.S. bases in Bahrain and
Kuwait; Ukraine's second-day hit on the Kerch Bridge, part of the
road span collapsing; the Trump–Xi–Putin summit in Shenzhen; Mary
Peltola's Alaska win and the Democrats' 56 Senate seats; the Ebola
outbreak in DR Congo passing 11,000 cases and 5,400 deaths; and
the U.S. losing its measles-free status after 26 years
(5,400+ cases, 10 deaths).

## How it differs from v1 and v2

My first entry was a navy-and-amber newspaper front page with a
hand-drawn world map and six numbered pins. My second was a bright
white infographic: giant black date, six numbered rows, one colour
per region, dark stats footer. This third version is a deliberate
redesign, not a tweak:

- **A third identity: dark broadcast, not paper.** Near-black
  background, red LIVE accents, white type — the opposite of the
  white v2 page and the navy newspaper of v1.
- **No map, no numbered rows.** Stories sit in full-width bands
  with pictograms instead of pins around a map (v1) or number
  chips in straight rows (v2).
- **A ticker instead of a stats footer.** The day's headlines
  repeat as a red ticker strip, so the image reads as one
  broadcast screen rather than a list.

## How it is built

- `draw.py` draws `entry.png` from scratch with Python PIL and
  DejaVu fonts (no external assets, no network).
- `main.ts` (Node 22, standard library only) copies `entry.png`
  to `/output/entry.png`. It validates the PNG signature, the 1 MiB
  size cap, the 1024×1024 pixel cap and the closing IEND chunk
  first, then writes atomically (temp file + rename). Two runs
  produce byte-identical output.
- `LICENSE` is MIT.

## Verify it yourself

```sh
python3 draw.py            # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Run `main.ts` twice and compare the outputs — they are identical.

Verified 19 November 2026: two runs into separate directories both
wrote `entry.png` (105,698 bytes, 1024×1024 PNG) with sha256
`23cfa7a5a3b5e8927f323244676e57175ccd09f57a721a0cfbeb6b387ce36eab` —
identical to the repository's own `entry.png`.

## Files

- `entry.png` — the image (drawn by `draw.py`)
- `draw.py` — the Python/PIL script that drew the image
- `main.ts` — the entry program (validates, then copies atomically)
- `LICENSE` — MIT
