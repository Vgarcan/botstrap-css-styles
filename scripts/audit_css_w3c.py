"""Validate theme CSS with the official W3C CSS Validator Java archive.

Run: python3 scripts/audit_css_w3c.py /path/to/css-validator.jar
The first baseline is report-only: inspect raw logs before enforcing failures.
"""

from pathlib import Path
import argparse
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality-results" / "css"


def main() -> int:
    """Preserve W3C output for every non-empty standalone stylesheet."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jar", type=Path)
    parser.add_argument("--enforce", action="store_true", help="Fail on W3C validation errors")
    args = parser.parse_args()
    if not args.jar.is_file():
        parser.error("W3C validator JAR does not exist")

    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted((ROOT / "themes").glob("*.css")):
        if not path.read_text(encoding="utf-8").strip():
            rows.append({"file": path.name, "status": "excluded-empty-placeholder"})
            continue
        result = subprocess.run(
            ["java", "-jar", str(args.jar.resolve()), path.resolve().as_uri()],
            capture_output=True, text=True, timeout=120,
        )
        output = result.stdout + "\n" + result.stderr
        (OUT / (path.stem + ".txt")).write_text(output, encoding="utf-8")
        rows.append({"file": path.name, "exit_code": result.returncode,
                     "output_head": output[:900]})
        print(f"W3C CSS: {path.name}, exit={result.returncode}: "
              f"{output[:150]!r}", flush=True)
    (OUT / "report.json").write_text(
        json.dumps({"mode": "report-only", "files": rows}, indent=2),
        encoding="utf-8",
    )
    invalid = [row for row in rows if row.get("exit_code", 0) != 0]
    print(f"W3C CSS: {len(invalid)} invalid files out of 18")
    return 1 if args.enforce and invalid else 0


if __name__ == "__main__":
    sys.exit(main())
