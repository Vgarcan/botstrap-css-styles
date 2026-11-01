"""Reject references to undefined local CSS custom properties in themes.

This is a structural guard, not a CSS syntax or contrast validator.
Bootstrap's --bs-* variables belong to the upstream framework and are external.
Other variable references must be declared somewhere in that same standalone CSS.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DECL = re.compile(r"(--[a-zA-Z0-9_-]+)\s*:")
REF = re.compile(r"var\(\s*(--[a-zA-Z0-9_-]+)")

def strip_comments(css: str) -> str:
    """Ignore commented-out declarations while checking actual code."""
    return re.sub(r"/\*[\s\S]*?\*/", "", css)


def main() -> int:
    """Validate all populated CSS assets, preserving standalone imports."""
    errors = []
    checked = 0
    for path in sorted((ROOT / "themes").glob("*.css")):
        css = strip_comments(path.read_text(encoding="utf-8"))
        if not css.strip():
            continue
        checked += 1
        declared = set(DECL.findall(css))
        referenced = set(REF.findall(css))
        missing = sorted(
            item for item in referenced
            if item not in declared and not item.startswith("--bs-")
        )
        for item in missing:
            errors.append(f"{path.name}: unresolved local var({item})")
    for error in errors:
        print("ERROR:", error)
    if errors:
        return 1
    print(f"OK: no undefined local CSS variables in {checked} themes")
    return 0

if __name__ == "__main__":
    sys.exit(main())
