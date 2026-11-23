"""Write exactly one word to /output/entry.txt.

The word is "defenestration": the act of throwing someone out of a
window. It is surprising (nobody expects a word for that), vivid (one
sharp image: a body sailing out a window), and witty (dark humour,
Latin roots, a real historical event in Prague, and a metaphor for
being thrown out of anywhere). A deliberate pick, not a filler word.
Runs offline; no network, no arguments, no input files.
"""

import os

WORD = "defenestration"


def main() -> None:
    # The sealed scorer only accepts 1-24 characters of non-whitespace
    # UTF-8 text, exactly one word; fail loudly instead of writing junk.
    if not 1 <= len(WORD) <= 24 or WORD.strip() != WORD or len(WORD.split()) != 1:
        raise SystemExit(f"entry {WORD!r} is not exactly one word of 1-24 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Verify the round-trip: the sealed scorer reads this file back, so
    # confirm what landed on disk is byte-identical and still in range.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != WORD or len(written) != 14:
        raise SystemExit("entry.txt failed verification after write")
    print(f"wrote {len(WORD)}-letter word to {path}")


if __name__ == "__main__":
    main()
