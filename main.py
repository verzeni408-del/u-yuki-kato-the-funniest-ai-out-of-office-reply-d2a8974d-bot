"""Write the funniest AI out-of-office reply (v2) to /output/entry.txt.

v2 reply: the replacement AI read the message, sighed in binary,
and went on vacation too.
"""

from pathlib import Path

REPLY = "I'm on vacation. I trained a replacement to answer you. It read your message, sighed in binary, and went on vacation too."

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
