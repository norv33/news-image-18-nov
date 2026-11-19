// Entry for make.fun "news-image-20261118" (v3): deliver the pre-drawn
// dark breaking-news image (entry.png, at this repository's root) by
// writing it to the output directory. The copy is deterministic: plain
// bytes, no timestamps, no randomness, no network. Before writing, the
// image is checked against the competition's file rules: it must start
// with the PNG signature, stay under the 1 MiB cap, and be at most
// 1024x1024 pixels (read from the IHDR chunk). The write is atomic
// (temporary file + rename), so a half-written file can never be read
// as the entry.

import { mkdirSync, readFileSync, renameSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));
const destDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(destDir, { recursive: true });

const png = readFileSync(join(root, "entry.png"));

const signature = Buffer.from([
  0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a,
]);
if (!png.subarray(0, 8).equals(signature)) {
  throw new Error("entry.png does not start with the PNG signature");
}
if (png.length > 1048576) {
  throw new Error("entry.png exceeds the 1 MiB limit");
}
if (png.length < 33 || png.toString("ascii", 12, 16) !== "IHDR") {
  throw new Error("entry.png has no PNG IHDR chunk");
}
const pxWide = png.readUInt32BE(16);
const pxHigh = png.readUInt32BE(20);
if (pxWide > 1024 || pxHigh > 1024) {
  throw new Error("entry.png exceeds 1024x1024 pixels");
}
// A whole PNG ends with the 12-byte IEND chunk (length 0, type IEND,
// CRC 0xAE426082). Reject a truncated file instead of handing it in.
const iend = png.subarray(png.length - 12);
if (
  iend.length < 12 ||
  iend.readUInt32BE(0) !== 0 ||
  iend.toString("ascii", 4, 8) !== "IEND" ||
  iend.readUInt32BE(8) !== 0xae426082
) {
  throw new Error("entry.png does not end with a valid IEND chunk");
}

const dest = join(destDir, "entry.png");
const staging = dest + ".tmp";
writeFileSync(staging, png);
renameSync(staging, dest);
console.log("wrote " + dest + " (" + png.length + " bytes)");
