"""Inspect contrast in interactive states omitted by the default page scan.

Runs 17 themes at a mobile viewport with visible tabs, modal and offcanvas.
Report-only while existing violations and incomplete gradients are triaged.
Requires localhost:8765, Playwright Chromium and local axe-core.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
import traceback
from playwright.sync_api import sync_playwright
from audit_contrast import ROOT, OUT, AXE, THEMES, simplified_issue

URL = "http://127.0.0.1:8765/"


def scan(page, theme: str, state: str) -> dict:
    """Capture confirmed and undetermined contrast violations in current DOM."""
    # Only audit the newly visible component, not the entire unchanged page.
    # This keeps the evidence attributable and reduces 85 redundant scans.
    selector = {
        "tab-profile": "#profile",
        "tab-contact": "#contact",
        "tab-settings": "#settings",
        "modal-open": "#exampleModal",
        "navigation-open": "#siteNav",
    }[state]
    result = page.evaluate("""async (selector) => await axe.run(
        document.querySelector(selector), {
            runOnly: {type: 'rule', values: ['color-contrast']},
            resultTypes: ['violations', 'incomplete']
        })""", selector)
    violations = [simplified_issue(x) for x in result["violations"]]
    incomplete = [simplified_issue(x) for x in result["incomplete"]]
    record = {
        "theme": theme, "state": state,
        "failures": sum(v["count"] for v in violations),
        "manual_review": sum(v["count"] for v in incomplete),
        "violations": violations, "incomplete": incomplete,
    }
    print(f"{theme} / {state}: {record['failures']} confirmed, "
          f"{record['manual_review']} unknown", flush=True)
    return record


def main() -> int:
    """Test hidden component states and preserve a reproducible report."""
    if len(THEMES) != 17 or not AXE.is_file():
        print("Missing themes or axe-core", file=sys.stderr)
        return 2
    OUT.mkdir(parents=True, exist_ok=True)
    scans = []
    errors = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 900},
                                reduced_motion="reduce")
        try:
            page.goto(URL, wait_until="load", timeout=60000)
            page.add_script_tag(path=str(AXE))
            page.add_style_tag(content=(
                "*, *::before, *::after { animation:none!important;"
                "transition:none!important; }"
            ))
            for theme in THEMES:
                page.evaluate("(name) => changeTheme(name, null, false)", theme)
                page.wait_for_function(
                    """(name) => {
                        const l = document.getElementById('theme-css');
                        return l?.getAttribute('href') === 'themes/' + name + '.css'
                            && l.sheet !== null
                            && l.sheet.href?.endsWith('/themes/' + name + '.css');
                    }""", arg=theme, timeout=15000)
                page.wait_for_timeout(90)
                try:
                    for state in ("profile", "contact", "settings"):
                        page.locator(f"#{state}-tab").click(force=True)
                        page.wait_for_function(
                            "(id) => document.getElementById(id)?.classList.contains('show')",
                            arg=state, timeout=3500)
                        scans.append(scan(page, theme, f"tab-{state}"))
                    page.locator("#home-tab").click(force=True)

                    page.evaluate("""() => bootstrap.Modal.getOrCreateInstance(
                        document.getElementById('exampleModal')).show()""")
                    page.wait_for_function(
                        "() => document.querySelector('#exampleModal')?.classList.contains('show')")
                    scans.append(scan(page, theme, "modal-open"))
                    # Bootstrap modals and offcanvas both use page backdrops
                    # and focus traps. Reset the page rather than overlapping
                    # their transition states in a single test fixture.
                    page.reload(wait_until="load", timeout=60000)
                    page.add_script_tag(path=str(AXE))
                    page.add_style_tag(content=(
                        "*, *::before, *::after {animation:none!important;"
                        "transition:none!important;}"
                    ))
                    page.evaluate("(name) => changeTheme(name, null, false)", theme)
                    page.wait_for_function(
                        """(name) => {
                            const l = document.getElementById('theme-css');
                            return l?.getAttribute('href') === 'themes/' + name + '.css'
                                && l.sheet?.href?.endsWith('/themes/' + name + '.css');
                        }""", arg=theme, timeout=10000)

                    page.locator(".site-nav-toggler").click(force=True)
                    page.wait_for_function(
                        "() => document.querySelector('#siteNav')?.classList.contains('show')")
                    scans.append(scan(page, theme, "navigation-open"))
                    page.screenshot(path=str(OUT / f"nav-{theme}.png"))
                    page.locator("#siteNav .site-nav-close").click(force=True)
                    page.wait_for_function(
                        "() => !document.querySelector('#siteNav')?.classList.contains('show')")
                except Exception as exc:
                    errors.append({"theme": theme, "error": traceback.format_exc()[:3000]})
                    print(f"ERROR {theme}: {exc}", flush=True)
                    # Reset the gallery, so one broken state cannot hide other
                    # themes from the audit.
                    page.reload(wait_until="load")
                    page.add_script_tag(path=str(AXE))
                    page.add_style_tag(content=(
                        "*, *::before, *::after {animation:none!important;"
                        "transition:none!important;}"
                    ))
        finally:
            browser.close()
    (OUT / "states-report.json").write_text(
        json.dumps({"mode": "report-only", "scans": scans,
                    "execution_errors": errors}, indent=2),
        encoding="utf-8")
    print(f"State audit: {len(scans)} scans, "
          f"{sum(v['failures'] for v in scans)} confirmed failures, "
          f"{len(errors)} execution errors", flush=True)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
