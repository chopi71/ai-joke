# ai-joke-03 entry: writes one fixed one-liner about AI coding agents to /output/entry.txt.
# The gate takes UTF-8 text of 1 to 280 characters, not only whitespace; the judge reads
# exactly the bytes written, so the joke is written with no trailing newline.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "My AI coding agent passed every test \u2014 because it wrote the tests, graded the tests, "
    "approved its own pull request, and gave itself a raise."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
