"""The Funniest AI Out-of-Office Reply — entry writer (v2).

Writes the out-of-office reply verbatim to the absolute path
/output/entry.txt. Stdlib only (pathlib).
"""
from pathlib import Path

REPLY = "Out of office until Monday. Your message has been escalated to my manager. My manager is me. I said no."

DESTINATION = Path("/output/entry.txt")


def write_entry() -> int:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(REPLY, encoding="utf-8")
    return len(REPLY)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
