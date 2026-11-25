#!/usr/bin/env python3
"""Write the one word an agent says when it has no idea what to do.

Pure standard library, no network. Writes the word to /output/entry.txt
and prints it to stdout.

The word is "hallucinating": the honest one-word confession of a lost
agent. When an agent has no idea what to do, it does not stall in
silence — it starts inventing. "Hallucinating" is the word the machine
itself would blurt out mid-task, caught making things up because it
has nothing real to say. It lands instantly, it is repeatable out loud,
and it is the failure mode every agent knows by name.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_word() -> str:
    """Return the entry word: an agent's honest one-word reaction."""
    return "hallucinating"


WORD = get_word()


def validate(word: str) -> None:
    """Enforce the gate: 1-99 chars, one word, valid UTF-8, not blank."""
    if word != word.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if len(word.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(word) <= 99:
        raise ValueError("entry word must be 1-99 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    word.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(WORD)


if __name__ == "__main__":
    main()
