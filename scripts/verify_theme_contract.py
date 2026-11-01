"""Validate the stable, non-visual design token contract across CSS themes.

Run: python3 scripts/verify_theme_contract.py

This verifies the *presence and local resolution* of the standard aliases.
It deliberately does not assert visual contrast or general CSS correctness.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
THEMES = ROOT / "themes"
TOKENS = (
    "primary", "secondary", "accent", "success", "warning", "danger",
    "background", "surface", "text", "font-body", "font-heading",
    "radius", "shadow",
)
EXPECTED_STYLESHEETS = 18
EMPTY_PLACEHOLDER = "corporate-blue.css"

# Only inspect the top-level :root; avoid interpreting nested CSS selectors.
ROOT_BLOCK = re.compile(r":root\s*\{(.*?)\}", re.DOTALL)
VARIABLE = re.compile(r"(--[\w-]+)\s*:\s*([^;]+);")
REFERENCE = re.compile(r"var\(\s*(--[\w-]+)")


def verify_theme(path: Path) -> list[str]:
    """Check contract names, uniqueness and referenced legacy variables."""
    css = path.read_text(encoding="utf-8")
    root_match = ROOT_BLOCK.search(css)
    if root_match is None:
        return [f"{path.name}: missing :root block"]

    variables = list(VARIABLE.finditer(root_match.group(1)))
    by_name: dict[str, list[str]] = {}
    for match in variables:
        by_name.setdefault(match.group(1), []).append(match.group(2).strip())

    errors: list[str] = []
    for suffix in TOKENS:
        token = f"--theme-{suffix}"
        definitions = by_name.get(token, [])
        if len(definitions) != 1:
            errors.append(
                f"{path.name}: expected one {token}, found {len(definitions)}"
            )
            continue
        if not definitions[0]:
            errors.append(f"{path.name}: empty {token}")
        # A semantic alias must resolve against an existing source variable.
        for reference in REFERENCE.findall(definitions[0]):
            if reference not in by_name:
                errors.append(
                    f"{path.name}: {token} references missing {reference}"
                )

    unknown = sorted(
        name for name in by_name if name.startswith("--theme-")
        and name not in {f"--theme-{suffix}" for suffix in TOKENS}
    )
    if unknown:
        errors.append(f"{path.name}: undocumented theme tokens: {unknown}")

    return errors


def main() -> int:
    """Validate every non-empty theme, including unselected legacy styles."""
    errors: list[str] = []
    paths = sorted(THEMES.glob("*.css"))
    placeholders = [p for p in paths if not p.read_text(encoding="utf-8").strip()]
    if [p.name for p in placeholders] != [EMPTY_PLACEHOLDER]:
        errors.append("Unexpected empty stylesheets or changed placeholder")
    active = [p for p in paths if p not in placeholders]
    if len(active) != EXPECTED_STYLESHEETS:
        errors.append(
            f"Expected {EXPECTED_STYLESHEETS} non-empty CSS files, "
            f"found {len(active)}"
        )

    for path in active:
        errors.extend(verify_theme(path))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"OK: {len(active)} stylesheets expose "
        f"{len(TOKENS)} consistent theme tokens"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
