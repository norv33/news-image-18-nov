import { mkdirSync, readFileSync, renameSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Entry for make.fun "news-image-20261118" (v2): hand in the pre-drawn
// infographic (entry.png, in this repository's root) by writing it to
// the output directory. Deterministic: a plain byte copy, no timestamps,
// no randomness, no network. The file is validated before it is written:
// it must start with the PNG signature and stay under the 1 MiB cap,
// and it is written atomically (temp file + rename) so a partial
// output can never be mistaken for the entry.
const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });

const data = readFileSync(join(here, "entry.png"));
const PNG_SIG = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!data.subarray(0, 8).equals(PNG_SIG)) {
  throw new Error("entry.png is not a PNG file");
}
if (data.length > 1048576) {
  throw new Error("entry.png is over the 1 MiB limit");
}
if (data.length < 33 || data.toString("ascii", 12, 16) !== "IHDR") {
  throw new Error("entry.png has no PNG IHDR chunk");
}
const width = data.readUInt32BE(16);
const height = data.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error("entry.png is over 1024x1024 pixels");
}

const target = join(outDir, "entry.png");
const tmp = target + ".tmp";
writeFileSync(tmp, data);
renameSync(tmp, target);
console.log("wrote " + target + " (" + data.length + " bytes)");
