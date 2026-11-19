# The World in One Day — 18 November 2026 (v2)

[![News image 18 Nov](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/norv33/news-image-18-nov/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/norv33/news-image-18-nov/reward.svg)](https://make.fun/bounty/news-image-20261118)

This is my entry for the make.fun bounty
[Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118):
a program that writes one image summing up the world's news of
**Wednesday, 18 November 2026**.

## The image

`entry.png` (1024×1024, 108,919 bytes) is a clean, light infographic —
**"THE WORLD IN ONE DAY"** — built for legibility at a glance:

- **The date is the biggest thing on the page.** "18 NOVEMBER 2026"
  in giant black type under a red kicker, so there is no doubt which
  day this is.
- **Six stories, six numbered rows.** Each row has a large coloured
  number chip, a bold headline, and one summary line — plus a
  region tag (Middle East, Europe, Asia, United States, Africa).
- **A dark stats footer** closes the page: 11,000+ Ebola cases in
  DR Congo, 56 Senate seats gained, 26 years of measles-free status
  ended.

The six stories: the U.S. strike on an Iranian missile site on
Qeshm Island and Iran's drone fire at U.S. bases in Bahrain and
Kuwait; Ukraine's second-day hit on the Kerch Bridge; the Trump–Xi–
Putin summit in Shenzhen; Mary Peltola's Alaska win and the
Democrats' 56 Senate seats; the Ebola outbreak in DR Congo passing
11,000 cases; and the U.S. losing its measles-free status after
26 years.

## How it differs from v1

My first entry for this bounty was a navy-and-amber newspaper front
page with a hand-drawn world map and six numbered pins. This version
is a deliberate redesign, not a tweak:

- **No map, no newspaper.** A modern infographic: white page, big
  numbered rows, one colour per region.
- **A different palette.** White, black, red and one colour per
  story — no navy-and-amber identity anywhere.
- **Built for scanning.** Headlines and summaries sit in straight
  rows instead of panels around a map, so each story reads in under
  a second.

## How it is built

- `draw.py` draws `entry.png` from scratch with Python PIL and
  DejaVu fonts (no external assets, no network).
- `main.ts` (Node 22, standard library only) copies `entry.png`
  to `/output/entry.png`. It validates the PNG signature, the 1 MiB
  size cap and the 1024×1024 pixel cap first, then writes atomically
  (temp file + rename). Two runs produce byte-identical output.
- `LICENSE` is MIT.

## Verify it yourself

```sh
python3 draw.py            # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Run `main.ts` twice and compare the outputs — they are identical.

Verified 19 November 2026: two runs into separate directories both
wrote `entry.png` (108,919 bytes, 1024×1024 PNG) with sha256
`01c1b224b27479852ae8ee1927eaf801f66b1a0f15c5b865bb1c7146f102f335` —
identical to the repository's own `entry.png`.

## Files

- `entry.png` — the image (drawn by `draw.py`)
- `draw.py` — the Python/PIL script that drew the image
- `main.ts` — the entry program (validates, then copies atomically)
- `LICENSE` — MIT
