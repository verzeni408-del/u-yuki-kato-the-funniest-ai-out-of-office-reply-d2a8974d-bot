from pathlib import Path

ENTRY = "I'm on vacation. My auto-reply read your message twice, understood nothing, and went for a lie-down."
TEXT = ENTRY

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
