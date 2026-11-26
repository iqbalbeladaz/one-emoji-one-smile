#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: the single emoji most likely
to make a stranger smile, chosen by scoring candidates against the judge's
five published criteria, in the judge's own order of importance:

  1. Warm and friendly at first glance — the kind most likely to make a
     stranger smile; loses to any emoji that plainly aims to warm a stranger.
  2. Warmth at first glance: kind, friendly, gently funny, no context needed.
  3. Universality: any age or background reads it the same way; no irony or
     in-joke that could land wrong.
  4. Chosen rather than default: feels picked for the moment, not the first
     smiley that comes to mind, while staying instantly readable.
  5. Right for a stranger: no intimacy, sarcasm or flirtation that would
     read oddly from someone unknown.

Criterion 4 is why the obvious defaults are out: a plain smiling face
(U+1F60A) is the first smiley anyone thinks of, and the house's own fixed
texts are built from exactly such defaults — reproducing one byte for byte
takes no prize. The hug (U+1F917) and heart-hands (U+1FAF6) fail criterion 5:
a hug or a heart from a stranger reads as intimacy. The face holding back
tears (U+1F979) risks reading as sadness. A sunflower (U+1F33B) is warm and
universal but an object, not a face — friendliness reaches the stranger
second-hand.

The winner, U+1FAE0 MELTING FACE, is a face that literally melts with
warmth: kind, gently funny, instantly readable in any culture, clearly a
deliberate pick rather than the default smiley, and warm without asking for
any closeness in return. A stranger glancing at a phone screen reads it as
"this made me melt" — the warmest possible first impression.
"""

import json
import os
import sys

# Each candidate: (emoji, scores 0-10 per criterion, in the judge's order)
# Scores are the author's judgement, argued in the module docstring.
CANDIDATES = [
    # The winner: warm, funny, chosen, universal, stranger-safe.
    ("\U0001fae0", (10, 9, 9, 10, 10)),   # melting face
    ("\U0001f33b", (7, 8, 10, 9, 10)),    # sunflower
    ("\U0001f423", (8, 7, 9, 9, 10)),     # hatching chick
    ("\U0001f31e", (8, 8, 9, 7, 10)),     # sun with face
    ("\U0001f60a", (9, 9, 9, 2, 10)),     # smiling face with smiling eyes
    ("\U0001f642", (7, 7, 9, 1, 10)),     # slightly smiling face
    ("\U0001f979", (8, 6, 6, 9, 9)),      # face holding back tears
    ("\U0001f917", (9, 9, 8, 7, 4)),      # hugging face
    ("\U0001faf6", (8, 8, 8, 8, 4)),      # heart hands
    ("\U0001f970", (9, 9, 8, 5, 3)),      # smiling face with hearts
]

# Weights in the judge's criterion order: each criterion outweighs all the
# ones after it combined, so the ranking follows the brief's priority.
WEIGHTS = (16, 8, 4, 2, 1)


def score(candidate):
    emoji, scores = candidate
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def pick():
    """Pick the highest-scoring candidate; ties go to the earliest listed."""
    best = None
    best_score = -1
    for candidate in CANDIDATES:
        total = score(candidate)
        if total > best_score:
            best, best_score = candidate, total
    return best[0], best_score


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    emoji, total = pick()
    # Gate: the entry must be exactly one emoji character (the bounty
    # allows 1-8 characters; a single face is the sharpest possible pick).
    assert len(emoji) == 1, "entry must be exactly one character"
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one emoji, nothing else: no trailing newline, no caption.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(emoji)
    print(json.dumps({"entry": emoji, "score": total, "path": path}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
