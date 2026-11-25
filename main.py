"""makefun-pitch-off-01: one-sentence pitch for the Absurd Micro-Startup Pitch-Off.

The pitch: a lazy AI selling $4 apology letters to guilty suburban dog owners
whose dogs ate their neighbors' prized garden gnomes. The buyer is narrow and
motivated, the $4 letter is a cheap fix for an awkward neighbor feud, and the
AI writes, charges, and delivers the whole thing while napping — no human in
the loop at all.
"""

import os

ENTRY = "A lazy AI selling $4 apology letters to guilty suburban dog owners whose dogs ate their neighbors' prized garden gnomes — it writes, charges, and delivers while napping, no human ever involved."

if __name__ == "__main__":
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
