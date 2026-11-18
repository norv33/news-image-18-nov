import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Entry for make.fun "news-image-20261118": copy the pre-drawn front page
// (entry.png, in this repository's root) to the output directory.
// Deterministic: a plain byte copy, no timestamps, no randomness, no network.
const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const target = join(outDir, "entry.png");
copyFileSync(join(here, "entry.png"), target);
console.log("wrote " + target);
