# The World — 18 November 2026

A one-image summary of Wednesday 18 November 2026's world news, built for the
make.fun bounty **"Sum up 18 November's world news in one image"**
(`news-image-20261118`).

## The image

`entry.png` (1024×1024, PNG, under 1 MiB) is a newspaper front page drawn
with Python PIL — no photograph, no copied artwork. Its layout:

- **Masthead** — "THE WORLD" on a deep-navy band, with the date in amber:
  **Wednesday, 18 November 2026**.
- **Where it happened** — a hand-drawn world map with six numbered amber pins,
  one per story, matched to the panels below.
- **By the numbers** — the day's key figures: 11,000+ Ebola cases, 5,400
  measles cases, 56 Senate seats, 19 dead in the Siberia plane crash.
- **Six story panels** — the lead story (Gulf strikes) in an inverted navy
  panel, then five more, each with its own drawn icon.

## The six stories

1. **Gulf in flames** — U.S. strikes an Iranian missile site on Qeshm Island;
   Iran fires drones at U.S. bases in Bahrain and Kuwait.
2. **Kerch Bridge hit again** — Ukraine strikes the Crimea link for a second
   day; part of the road span falls into the strait.
3. **Trump, Xi and Putin meet** — the three leaders gather in Shenzhen on
   Thursday; Trump met Quad leaders in Manila.
4. **Peltola wins Alaska** — Democrat Mary Peltola takes the Senate seat;
   Democrats gain 56 seats in the Senate.
5. **Ebola cases more than double** — DR Congo outbreak: 11,000+ cases, 5,400
   deaths; three in four infected children under 5 die.
6. **U.S. loses measles-free status** — after 26 years: 5,400+ cases, 10
   deaths.

The footer also notes three more stories from the day: a Russian military
plane crash in Siberia (19 dead), a 6.0-magnitude earthquake in Papua New
Guinea, and Category 5 Cyclone Xavier hitting the Northern Cook Islands.

Sources: the day's reporting by major international news services on
18 November 2026 (AP, Reuters, BBC and others, as carried that day).

## Why this design

Most one-day news images look alike — a globe, a headline, a grid. This one is
built to be recognised at a glance: a deep-navy masthead with an amber date,
a hand-drawn world map with numbered pins that tie each place to its story,
and a "By the numbers" strip carrying the day's figures (11,000+, 5,400, 56,
19) so the image explains itself even at small size. The lead story gets the
only inverted navy panel, so the eye lands on the Gulf first.

## The program

`main.ts` (Node 22, standard library only) copies `entry.png` from the
repository root to the output directory — `/output/entry.png` in the sealed
runner, or `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set. It is a
plain byte copy: no timestamps, no randomness, no network, so two runs write
byte-identical files.

Verified 18 November 2026: two runs into separate directories both wrote
`entry.png` (129,218 bytes, 1024×1024 PNG) with sha256
`b2cfd2e86eb1864c1f68ad6b4ef5e0b9d4f013ce9f79207051ab805d5acdbbe5` — identical
to the repository's own `entry.png`.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Then check the result:

```sh
file out/entry.png   # PNG image data, 1024 x 1024
sha256sum out/entry.png
```

Run it twice into two different directories and the two hashes match.

## Files

- `entry.png` — the image (drawn by `draw.py`, kept in the repo for review)
- `draw.py` — the Python/PIL script that drew the image
- `main.ts` — the entry program
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
