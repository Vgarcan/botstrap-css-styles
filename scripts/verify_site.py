"""Basic dependency-free checks for the GitHub Pages theme gallery.

Run locally with: python3 scripts/verify_site.py

The checks protect against publishing a gallery with missing or empty
stylesheets. They do not replace browser, accessibility, or visual testing.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
THEME_DIR = ROOT / "themes"


def main() -> int:
    """Validate the stylesheet references used by the live theme switcher."""
    if not INDEX.is_file():
        print("ERROR: index.html is missing")
        return 1

    html = INDEX.read_text(encoding="utf-8")
    referenced_themes = set(
        re.findall(r"file:\s*['\"]themes/([\w-]+\.css)['\"]", html)
    )

    if len(referenced_themes) != 17:
        print(f"ERROR: Expected 17 selectable themes, got {len(referenced_themes)}")
        return 1

    errors: list[str] = []
    for filename in sorted(referenced_themes):
        css_path = THEME_DIR / filename
        if not css_path.is_file():
            errors.append(f"Missing theme: {css_path.relative_to(ROOT)}")
        elif not css_path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty selectable theme: {css_path.relative_to(ROOT)}")

    if "fetch(selectedTheme.file" not in html:
        errors.append("Download must fetch the actual stylesheet, not mock CSS")

    if errors:
        for problem in errors:
            print(f"ERROR: {problem}")
        return 1

    print(f"OK: {len(referenced_themes)} selectable theme CSS files verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
