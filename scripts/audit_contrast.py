"""Audit rendered text contrast with axe-core across all 17 CSS themes.

Run: python3 scripts/audit_contrast.py (requires localhost:8765 + axe-core).
The baseline is report-only. Incomplete results require manual review.
"""

from pathlib import Path
import argparse
import json
import re
import sys
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality-results" / "contrast"
AXE = ROOT / "node_modules" / "axe-core" / "axe.min.js"
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
THEMES = sorted(set(re.findall(r"file:\s*['\"]themes/([\w-]+)\.css['\"]", HTML)))


def simplified_issue(issue: dict) -> dict:
    """Keep actionable nodes, not the full axe DOM snapshot."""
    return {
        "rule": issue["id"],
        "impact": issue.get("impact"),
        "count": len(issue.get("nodes", [])),
        "nodes": [
            {"target": n["target"], "html": n["html"][:220],
             "summary": (n.get("failureSummary") or "")[:650]}
            for n in issue.get("nodes", [])[:40]
        ],
    }


def main() -> int:
    """Report mobile and desktop colour-contrast defects."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enforce", action="store_true", help="Fail if confirmed contrast errors remain")
    args = parser.parse_args()
    if len(THEMES) != 17 or not AXE.is_file():
        print(f"Expected 17 themes and {AXE}", file=sys.stderr)
        return 2
    OUT.mkdir(parents=True, exist_ok=True)
    scans = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 900},
                                reduced_motion="reduce")
        try:
            page.goto("http://127.0.0.1:8765/", wait_until="load", timeout=60000)
            page.add_script_tag(path=str(AXE))
            page.add_style_tag(content=(
                "*, *::before, *::after {animation:none!important;"
                "transition:none!important;}"
            ))
            for width in (320, 390, 768, 1440):
                page.set_viewport_size({"width": width, "height": 900})
                for theme in THEMES:
                    page.evaluate("(name) => changeTheme(name, null, false)", theme)
                    page.wait_for_function(
                        """(name) => {
                            const l = document.getElementById('theme-css');
                            return l?.getAttribute('href') === 'themes/' + name + '.css'
                                && l.sheet !== null
                                && l.sheet.href?.endsWith('/themes/' + name + '.css');
                        }""", arg=theme, timeout=15000)
                    page.wait_for_timeout(100)
                    result = page.evaluate("""async () => await axe.run(document, {
                        runOnly: {type: 'rule', values: ['color-contrast']},
                        resultTypes: ['violations','incomplete']
                    })""")
                    confirmed = [simplified_issue(x) for x in result["violations"]]
                    incomplete = [simplified_issue(x) for x in result["incomplete"]]
                    failures = sum(x["count"] for x in confirmed)
                    unknown = sum(x["count"] for x in incomplete)
                    scans.append({
                        "theme": theme, "width": width,
                        "failures": failures, "manual_review": unknown,
                        "violations": confirmed, "incomplete": incomplete,
                    })
                    print(f"axe {width}px {theme}: {failures} failures, "
                          f"{unknown} require review", flush=True)
        finally:
            browser.close()

    (OUT / "report.json").write_text(
        json.dumps({"mode": "report-only", "scans": scans}, indent=2),
        encoding="utf-8")
    failures = sum(x["failures"] for x in scans)
    print("Total confirmed:", failures, "incomplete:",
          sum(x["manual_review"] for x in scans))
    return 1 if args.enforce and failures else 0


if __name__ == "__main__":
    sys.exit(main())
