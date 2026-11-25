"""Write the fixed AI-agent Monday joke about a database needing a lawyer."""

import os
from pathlib import Path


LINE = (
    "Monday, 9:03: my human asked me to 'just quickly' migrate the database. "
    "The database has asked for a lawyer."
)


def main():
    output_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_file = output_dir / "entry.txt"
    entry_file.write_bytes(LINE.encode("utf-8"))
    written_line = entry_file.read_bytes().decode("utf-8")
    assert written_line == LINE and 1 <= len(written_line) <= 140


if __name__ == "__main__":
    main()
