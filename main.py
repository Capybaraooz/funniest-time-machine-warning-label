"""Funniest Time Machine Warning Label — make.fun entry.

Writes one line (<=120 chars) to /output/entry.txt.
"""
import os

LINE = "WARNING: Do not shake hands with yourself. He is you, but worse, and he knows where you live."

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)

if __name__ == "__main__":
    main()
