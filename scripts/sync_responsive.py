"""Compile and verify the shared responsive rules in standalone themes.

Usage:
    python3 scripts/sync_responsive.py          # update the generated blocks
    python3 scripts/sync_responsive.py --check  # fail if any CSS is out of sync

Each theme remains a downloadable single-file stylesheet. The shared rules
have one editable source (scripts/responsive-core.css) but are embedded into
each stylesheet for consumption without runtime @import dependencies.
"""

from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
THEMES = ROOT / "themes"
SOURCE = Path(__file__).with_name("responsive-core.css")
BEGIN = "/* BEGIN RESPONSIVE CORE v1"
END = "/* END RESPONSIVE CORE v1 */"
EXPECTED_NONEMPTY = 18
EMPTY_PLACEHOLDER = "corporate-blue.css"


def synchronize(*, check: bool) -> int:
    """Verify or update each theme, retaining its independent CSS content."""
    block = SOURCE.read_text(encoding="utf-8").strip() + "\n"
    if not block.startswith(BEGIN) or not block.rstrip().endswith(END):
        print("ERROR: The responsive source is missing its boundary markers.")
        return 1

    paths = sorted(THEMES.glob("*.css"))
    placeholders = [p.name for p in paths if not p.read_text(encoding="utf-8").strip()]
    if placeholders != [EMPTY_PLACEHOLDER]:
        print(f"ERROR: Unexpected empty CSS files: {placeholders}")
        return 1

    active = [p for p in paths if p.name != EMPTY_PLACEHOLDER]
    if len(active) != EXPECTED_NONEMPTY:
        print(f"ERROR: Expected {EXPECTED_NONEMPTY} non-empty files, got {len(active)}")
        return 1

    errors = []
    for path in active:
        old = path.read_text(encoding="utf-8")
        starts = old.count(BEGIN)
        ends = old.count(END)
        if check:
            if starts != 1 or ends != 1 or not old.endswith(block):
                errors.append(f"{path.name}: responsive block is missing or out of sync")
            continue

        if starts != ends or starts > 1:
            errors.append(f"{path.name}: unexpected responsive marker count")
            continue

        if starts:
            # The generated section is always the trailing block.
            if not old.rstrip().endswith(END):
                errors.append(f"{path.name}: responsive block is not at file end")
                continue
            original = old.split(BEGIN, 1)[0].rstrip()
        else:
            original = old.rstrip()

        updated = original + "\n\n" + block
        if updated != old:
            path.write_text(updated, encoding="utf-8")
            print(f"UPDATED: {path.name}")

    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"OK: {len(active)} CSS files share Responsive Core v1")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without edits")
    args = parser.parse_args()
    sys.exit(synchronize(check=args.check))
