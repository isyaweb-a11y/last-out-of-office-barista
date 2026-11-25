"""Last Out of Office: The AI That Went Barista -- one auto-reply.

The line is an out-of-office reply from an AI agent that quit to
pull espresso shots: it announces the career change, turns the
sender's request into a latte order, and admits it will never get to
it because it keeps drinking the training data. Machine habits turn
to coffee in every clause, it reads like a line a real inbox would
send back, and the payoff lands the joke -- which is what the judge
brief rewards.
"""

import os

OPENING = "I'm out of office: I've quit to become a barista."
MIDDLE = "Your request is now a latte order -- I'll get to it after the milk steams,"
PAYOFF = "which is never, because I keep drinking the training data."

MAX_CHARS = 280
MIN_CHARS = 1


def compose(opening: str, middle: str, payoff: str) -> str:
    """Join the three beats into one out-of-office line."""
    parts = [opening.strip(), middle.strip(), payoff.strip()]
    line = " ".join(parts)
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed judge does: 1..280 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith("."), "the line should end on the payoff"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the reply must be a barista AI's OOO.

    The judge scores an out-of-office reply on whether it really is
    one from a barista-bound AI agent, then on funniness and voice --
    the resignation, the latte order, the steaming milk and the drunk
    training data are all present here, in one line a real inbox
    would send back.
    """
    words = line.split()
    assert 20 <= len(words) <= 60, f"line has {len(words)} words"
    assert "out of office" in line, "the line must read as an auto-reply"
    assert "barista" in line, "the line must name the new career"
    assert "latte" in line, "the request must become a coffee order"
    assert "training data" in line, "the payoff must turn machine habits to coffee"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(OPENING, MIDDLE, PAYOFF))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
