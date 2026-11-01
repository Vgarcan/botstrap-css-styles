"""Automated browser smoke tests of the live theme gallery at key viewports.

Run against the local server:
    python3 -m http.server 8765 --bind 127.0.0.1 &
    python3 scripts/test_responsive.py

Requires the optional development dependency: pip install playwright,
followed by python -m playwright install chromium.
"""

from pathlib import Path
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
THEMES = sorted(set(re.findall(r"file:\s*['\"]themes/([\w-]+\.css)['\"]", INDEX)))
WIDTHS = (320, 375, 390, 430, 768, 1024, 1280, 1440)
BASE_URL = "http://127.0.0.1:8765/"
EVIDENCE = ROOT / "responsive-results"


def measure(page):
    """Return viewport size, document overflow and misplaced core components."""
    return page.evaluate("""() => {
      const view = document.documentElement.clientWidth;
      const width = Math.max(document.documentElement.scrollWidth, document.body.scrollWidth);
      const selectors = '.container, .container-fluid, .card, .table-responsive, .form-control, .navbar-brand, .btn';
      const offscreen = Array.from(document.querySelectorAll(selectors)).filter(el => {
        // A table's action buttons are intentionally scrollable within its own
        // container; they must never count as full-page viewport overflow.
        if (el.closest('.modal, .offcanvas, .toast-container, .theme-selector, .carousel')
            || (el.closest('.table-responsive') && !el.matches('.table-responsive'))) return false;
        const s = getComputedStyle(el), rect = el.getBoundingClientRect();
        if (s.display === 'none' || s.visibility !== 'visible' || rect.width < 1) return false;
        return rect.right > view + 4 || rect.left < -4;
      }).slice(0, 5).map(el => ({
        selector: el.tagName.toLowerCase() + '.' + [...el.classList].slice(0, 3).join('.'),
        left: Math.round(el.getBoundingClientRect().left),
        right: Math.round(el.getBoundingClientRect().right)
      }));
      const spill = Array.from(document.querySelectorAll('body *'))
        .filter(el => {
          if (el.closest('.table-responsive, .theme-selector, .modal, .offcanvas, .carousel')) return false;
          const r = el.getBoundingClientRect(), s = getComputedStyle(el);
          return s.display !== 'none' && r.width > 0 && (r.right > view + 3 || r.left < -3);
        })
        .sort((a,b) => b.getBoundingClientRect().right - a.getBoundingClientRect().right)
        .slice(0, 5)
        .map(el => ({
          element: el.tagName.toLowerCase() + '.' + [...el.classList].slice(0,3).join('.'),
          left: Math.round(el.getBoundingClientRect().left),
          right: Math.round(el.getBoundingClientRect().right)
        }));
      return {view, width, excess: width - view, scrollX: window.scrollX,
              offscreen, spill: width - view > 2 ? spill : []};
    }""")


def main() -> int:
    """Run across each theme and viewport; fail CI on structural regressions."""
    if len(THEMES) != 17:
        print(f"ERROR: expected 17 selectable themes; got {len(THEMES)}")
        return 1

    EVIDENCE.mkdir(exist_ok=True)
    failures: list[str] = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
        try:
            page.goto(BASE_URL, wait_until="load", timeout=60000)
            page.wait_for_function("() => typeof changeTheme === 'function'", timeout=10000)

            for width in WIDTHS:
                page.set_viewport_size({"width": width, "height": 900})
                for theme in THEMES:
                    page.evaluate("(name) => changeTheme(name.replace('.css', ''), null, false)", theme)
                    try:
                        page.wait_for_function(
                            """(name) => {
                              const link = document.getElementById('theme-css');
                              return link && link.getAttribute('href') === 'themes/' + name
                                && link.sheet !== null;
                            }""",
                            arg=theme,
                            timeout=18000,
                        )
                    except Exception as exc:
                        failures.append(f"{width}px / {theme}: stylesheet did not load ({exc})")
                        continue

                    # Remove retained horizontal scroll from previous themes and
                    # allow reduced-motion animations to reach their final frame.
                    page.evaluate("() => window.scrollTo(0, 0)")
                    page.wait_for_timeout(70)
                    result = measure(page)
                    if result["excess"] > 2 or result["offscreen"]:
                        message = (f"{width}px / {theme}: excess={result['excess']}px; "
                                   f"scrollX={result['scrollX']}; "
                                   f"misplaced={result['offscreen']}; spill={result['spill']}")
                        failures.append(message)
                        if len(failures) <= 10:
                            page.screenshot(path=str(EVIDENCE / f"{width}-{theme[:-4]}.png"))
                    if theme == "minimalist-clean.css" and width in (390, 768, 1440):
                        page.screenshot(path=str(EVIDENCE / f"sample-{width}.png"))

                # The theme chooser is navigation, not part of the theme being audited.
                button = page.locator(".toggle-selector")
                button.click(force=True)
                selector = page.locator("#themeSelector")
                if not selector.is_visible():
                    failures.append(f"{width}px: theme selector could not be opened")
                else:
                    bounds = selector.bounding_box()
                    if bounds and (bounds["x"] < -2 or bounds["x"] + bounds["width"] > width + 2):
                        failures.append(f"{width}px: theme selector extends off-screen")
                    if width <= 430:
                        first = page.locator(".theme-option").first.bounding_box()
                        if first and first["height"] < 44:
                            failures.append(f"{width}px: theme option touch target too small")
                page.keyboard.press("Escape")
                if selector.is_visible():
                    failures.append(f"{width}px: Escape did not close theme selector")

        finally:
            browser.close()

    if failures:
        for failure in failures:
            print("FAIL:", failure, flush=True)
        print(f"FAILED: {len(failures)} responsive checks across 17 themes", flush=True)
        return 1

    print(f"OK: {len(THEMES)} themes at {len(WIDTHS)} viewport widths", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
