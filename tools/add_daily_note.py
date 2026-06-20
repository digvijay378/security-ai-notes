#!/usr/bin/env python3
"""
Simple helper to add a daily note and commit it.

Usage:
  python tools/add_daily_note.py "Today I improved the risk scoring logic and added 8 tests."

This makes it easy to keep a consistent public record of work.
"""

import sys
from datetime import date
from pathlib import Path
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/add_daily_note.py \"your note here\"")
        sys.exit(1)

    note = " ".join(sys.argv[1:])
    today = date.today().isoformat()
    filename = f"{today}-update.md"
    path = Path("notes") / filename
    path.parent.mkdir(exist_ok=True)

    content = f"# {today} — Quick Update\n\n{note}\n"
    path.write_text(content)

    subprocess.run(["git", "add", str(path)], check=True)
    subprocess.run(["git", "commit", "-m", f"docs: daily note for {today}"], check=True)
    print(f"Added and committed {filename}")

if __name__ == "__main__":
    main()
