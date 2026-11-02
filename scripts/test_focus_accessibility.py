"""Check keyboard focus visibility on every theme at three viewport widths.

This is an interactive browser smoke test for WCAG 2.2 2.4.7, 2.4.11 and
1.4.11; it does *not* prove conformance on all gradients or real devices.

Run a local server on port 8765, then:
    python3 scripts/test_focus_accessibility.py

Uses the same Playwright/Chromium installation as the existing CI audit.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
import traceback

from playwright.sync_api import sync_playwright

from audit_contrast import THEMES

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality-results" / "focus"
BASE = "http://127.0.0.1:8765/"
WIDTHS = (390, 768, 1440)

# Representative links, buttons, icon controls, tabs, forms, and an accordion.
CORE_CONTROLS = (
    ".site-brand",
    ".toggle-selector",
    "#home-tab",
    "button[data-bs-target='#exampleModal']",
    ".accordion-button",
)
SETTINGS_CONTROLS = (
    "#settings select.form-control",
    "#notifications",
)


def inspect_focus(page, theme: str, width: int, selector: str) -> dict:
    """Focus an element through keyboard modality, then inspect the ring."""
    target = page.locator(selector).first
    if not target.is_visible():
        raise RuntimeError(f"Expected visible interactive element: {selector}")
    target.scroll_into_view_if_needed(timeout=6000)
    page.keyboard.press("Tab")
    target.focus()
    result = target.evaluate("""el => {
      const cs = getComputedStyle(el), r = el.getBoundingClientRect();
      const x = Math.max(0, Math.min(window.innerWidth - 1, r.left + r.width / 2));
      const y = Math.max(0, Math.min(window.innerHeight - 1, r.top + r.height / 2));
      const top = document.elementFromPoint(x, y);
      return {
        active: document.activeElement === el,
        focusVisible: el.matches(':focus-visible'),
        outlineWidth: cs.outlineWidth,
        outlineStyle: cs.outlineStyle,
        outlineColor: cs.outlineColor,
        outlineOffset: cs.outlineOffset,
        halo: cs.boxShadow,
        inViewport: r.width > 0 && r.height > 0 &&
          r.right > 0 && r.left < window.innerWidth &&
          r.bottom > 0 && r.top < window.innerHeight,
        obscuredAtCentre: !!top && !(top === el || el.contains(top) || top.contains(el))
      };
    }""")
    # White and very dark layers are 17.5:1 against each other, providing
    # two possible visible edges depending on the adjacent background.
    passed = all((
        result["active"],
        result["focusVisible"],
        result["outlineWidth"] == "3px",
        result["outlineStyle"] == "solid",
        result["outlineColor"] == "rgb(16, 24, 39)",
        result["outlineOffset"] == "3px",
        "rgb(255, 255, 255)" in result["halo"],
        result["inViewport"],
        not result["obscuredAtCentre"],
    ))
    return {
        "theme": theme, "viewport": width, "selector": selector,
        "status": "pass" if passed else "fail", **result,
    }


def audit_drawer(page, theme: str) -> list[dict]:
    """Inspect offcanvas controls in their actual opened state."""
    page.evaluate("() => window.scrollTo(0, 0)")
    page.locator(".site-nav-toggler").click()
    page.wait_for_function(
        "() => document.querySelector('#siteNav')?.classList.contains('show')",
        timeout=5000,
    )
    rows = []
    try:
        for selector in (".site-nav-close", "#siteNav .site-nav-link"):
            rows.append(inspect_focus(page, theme, 390, selector))
    finally:
        page.keyboard.press("Escape")
        page.wait_for_function(
            "() => !document.querySelector('#siteNav')?.classList.contains('show')",
            timeout=5000,
        )
    return rows


def main() -> int:
    """Exercise real focus and preserve a concise, per-control JSON report."""
    if len(THEMES) != 17:
        print("ERROR: 17 selectable themes expected", file=sys.stderr)
        return 2
    OUT.mkdir(parents=True, exist_ok=True)
    rows, exceptions = [], []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 390, "height": 900}, reduced_motion="reduce")
        try:
            page.goto(BASE, wait_until="load", timeout=60000)
            page.add_style_tag(content=(
                "*, *::before, *::after {animation:none!important;"
                "transition:none!important;scroll-behavior:auto!important;}"
            ))
            for width in WIDTHS:
                page.set_viewport_size({"width": width, "height": 900})
                for theme in THEMES:
                    try:
                        page.evaluate("(name) => changeTheme(name, null, false)", theme)
                        page.wait_for_function(
                            """name => {
                              const l = document.getElementById('theme-css');
                              return l?.getAttribute('href') === 'themes/' + name + '.css'
                                && l.sheet?.href?.endsWith('/themes/' + name + '.css');
                            }""", arg=theme, timeout=15000,
                        )
                        for selector in CORE_CONTROLS:
                            rows.append(inspect_focus(page, theme, width, selector))

                        # Inputs in Settings start in a hidden Bootstrap tab.
                        page.locator("#settings-tab").click(force=True)
                        page.wait_for_function(
                            "() => document.querySelector('#settings')?.classList.contains('show')",
                            timeout=5000,
                        )
                        for selector in SETTINGS_CONTROLS:
                            rows.append(inspect_focus(page, theme, width, selector))
                        page.locator("#home-tab").click(force=True)

                        if width == 390:
                            rows.extend(audit_drawer(page, theme))
                        if theme in ("cyberpunk-neon", "kids-friendly") and width == 390:
                            page.locator("#home-tab").focus()
                            page.screenshot(path=str(OUT / f"{theme}-keyboard.png"))
                    except Exception as exc:
                        exceptions.append({
                            "theme": theme, "width": width,
                            "error": str(exc), "trace": traceback.format_exc()[:1300],
                        })
                        print(f"ERROR: {width}px {theme}: {exc}", flush=True)
                        page.reload(wait_until="load")
            failures = [r for r in rows if r["status"] == "fail"]
            (OUT / "report.json").write_text(json.dumps({
                "test": "Computed two-tone focus ring and non-obscured centre",
                "widths": WIDTHS, "scans": rows, "errors": exceptions,
                "failure_count": len(failures),
            }, indent=2), encoding="utf-8")
            for entry in failures[:30]:
                print("FAIL:", entry, flush=True)
            print(f"Keyboard focus checks: {len(rows)} controls, "
                  f"{len(failures)} failures, {len(exceptions)} errors", flush=True)
            return 1 if failures or exceptions else 0
        finally:
            browser.close()


if __name__ == "__main__":
    sys.exit(main())
