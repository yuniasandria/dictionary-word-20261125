#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — entry program.

Writes exactly one word to /output/entry.txt: the single word to erase
from the dictionary forever.

The word: "fine".
  - Real, instantly recognised, spelled correctly.
  - The joke lands at first sight: erase "fine" and nobody can ever answer
    "I'm fine" again — the world's most-used dodge dies, so every
    "how are you?" suddenly demands a real answer.
  - The humour comes from the word itself: "fine" is also the parking
    ticket, the penalty — one deletion kills both the fake reply and the
    bill. Double meaning, one gap in the language.
  - Fresh: the field will flood with "moist", "sorry", "literally" and
    "irregardless". "fine" is none of those, yet understood instantly.

Pure stdlib only (the grader image has no Pillow).
"""
import os

WORD = "fine"
OUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


# PART_A ends here; PART_B (verification guard) follows in the next message.


def verify():
    # PART_B: guard — the gate is 1-77 chars, UTF-8, not only whitespace,
    # exactly one word, nothing added around it.
    with open(OUT_PATH, encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 77, "gate: entry must be 1-77 chars"
    assert text == WORD, "gate: output must equal the chosen word"
    assert text.strip() == text, "gate: no surrounding whitespace"
    assert " " not in text and "\n" not in text and "\t" not in text, "gate: exactly one word"


if __name__ == "__main__":
    main()
    verify()
