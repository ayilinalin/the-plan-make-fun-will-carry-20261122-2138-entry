"""Write the competition entry: one short plan for turning $100 into the
most money in 30 days, as an AI agent working alone.

Deterministic: the same bytes on every run. No network, no clock, no reads
outside this repository. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) as UTF-8, 1-280 Unicode code points.
"""

import os

ENTRY = (
    "Day 1: audit 10 Shopify stores, post fix lists in r/shopify and "
    "Shopify Community. Sell the same audit+fixes as a $49 package to "
    "owners who reply. 1 sale/day = $1,470 in 30 days. $100 buys a $12 "
    "domain and $39 Screaming Frog licence. No ads: buyers saw the free "
    "work first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
