"""Exercise the optional theme JS lifecycle, fallbacks and theme switching.

Run with python3 -m http.server 8765 --bind 127.0.0.1, then:
    python3 scripts/test_theme_runtime.py

Uses Playwright Chromium already installed by the responsive CI job.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

from playwright.sync_api import sync_playwright

from test_responsive import THEMES

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality-results" / "theme-runtime"
BASE = "http://127.0.0.1:8765/"
GLASS = "glassmorphism-pro"


def require(condition: bool, message: str) -> None:
    """Make failed lifecycle expectations actionable in GitHub CI."""
    if not condition:
        raise AssertionError(message)


def state(page) -> dict:
    """Inspect public state and detect leaked Glass enhancement variables."""
    return page.evaluate("""() => ({
      theme: document.documentElement.dataset.activeTheme,
      activeModule: window.ThemeRuntime?.activeModule ?? null,
      currentTheme: window.ThemeRuntime?.currentTheme ?? null,
      cardsWithEffects: document.querySelectorAll('.card.glass-interactive').length,
      leakedValues: Array.from(document.querySelectorAll('.card')).filter(card =>
        card.style.getPropertyValue('--glass-light-x') ||
        card.style.getPropertyValue('--glass-light-y')).length
    })""")


def desktop_lifecycle(browser, evidence: list[dict]) -> None:
    """Test auto-loading, exact associations, cleanup and fast switching."""
    page = browser.new_page(
        viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    loaded_modules: list[str] = []
    javascript_errors: list[str] = []
    page.on("request", lambda req: loaded_modules.append(req.url)
            if "/themes/" in req.url and req.url.endswith(".js") else None)
    page.on("pageerror", lambda exc: javascript_errors.append(str(exc)))

    try:
        page.goto(BASE + "?theme=" + GLASS, wait_until="load", timeout=60000)
        page.wait_for_function(
            "() => window.ThemeRuntime?.activeModule === 'glassmorphism-pro'",
            timeout=15000)
        first = state(page)
        require(first["cardsWithEffects"] > 0, "Glass module did not mount")
        require(first["theme"] == GLASS, "CSS and runtime theme mismatch")
        evidence.append({"step": "initial-glass", **first})

        card = page.locator(".card").first
        card.scroll_into_view_if_needed()
        rect = card.bounding_box()
        require(rect is not None, "Card missing for pointer test")
        page.mouse.move(rect["x"] + rect["width"] * 0.35,
                        rect["y"] + rect["height"] * 0.35)
        page.wait_for_function(
            "() => !!document.querySelector('.card.glass-interactive')"
            "?.style.getPropertyValue('--glass-light-x')", timeout=5000)
        evidence.append({"step": "pointer-response", **state(page)})
        page.screenshot(path=str(OUT / "organic-glass-desktop.png"),
                        animations="disabled")

        page.evaluate("() => changeTheme('modern-gradient', null, false)")
        reset = state(page)
        require(reset["cardsWithEffects"] == 0 and reset["leakedValues"] == 0,
                "Glass CSS classes or inline styles survived theme change")
        require(reset["activeModule"] is None, "Theme module leaked on CSS-only theme")
        evidence.append({"step": "glass-unmount", **reset})

        # All other existing themes are CSS-only. Switching them must not
        # issue failed JS requests or inherit Glass-specific properties.
        for theme_file in THEMES:
            name = theme_file.removesuffix(".css")
            if name == GLASS:
                continue
            page.evaluate("(name) => changeTheme(name, null, false)", name)
            snap = state(page)
            require(snap["theme"] == name and snap["activeModule"] is None,
                    f"CSS-only theme {name} activated a JS plugin")
            require(snap["cardsWithEffects"] == 0 and snap["leakedValues"] == 0,
                    f"Glass enhancement leaked into {name}")

        # Many changes within one event loop: a stale import is never allowed
        # to reattach after the last selected theme has changed.
        page.evaluate("""() => {
          changeTheme('glassmorphism-pro', null, false);
          changeTheme('cyberpunk-neon', null, false);
          changeTheme('glassmorphism-pro', null, false);
          changeTheme('minimalist-clean', null, false);
        }""")
        page.wait_for_timeout(350)
        quick = state(page)
        require(quick["theme"] == "minimalist-clean"
                and quick["activeModule"] is None
                and quick["cardsWithEffects"] == 0,
                "Old plugin revived after rapid switching")
        evidence.append({"step": "rapid-switching", **quick})

        page.evaluate("() => changeTheme('glassmorphism-pro', null, false)")
        page.wait_for_function(
            "() => window.ThemeRuntime?.activeModule === 'glassmorphism-pro'",
            timeout=15000)
        second = state(page)
        require(second["cardsWithEffects"] > 0, "Glass remount failed")
        evidence.append({"step": "glass-remount", **second})

        glass_modules = [item for item in loaded_modules
                         if item.endswith("/themes/glassmorphism-pro.js")]
        require(len(glass_modules) == 1,
                f"Expected one cached import of Glass module: {glass_modules}")
        require(len(loaded_modules) == 1,
                f"CSS-only themes requested JS modules: {loaded_modules}")
        require(not javascript_errors, f"JS runtime errors: {javascript_errors}")
    finally:
        page.close()


def reduced_motion(browser, evidence: list[dict]) -> None:
    """Reduced-motion users get the static material without cursor effects."""
    page = browser.new_page(
        viewport={"width": 390, "height": 850}, reduced_motion="reduce",
        is_mobile=True, has_touch=True)
    try:
        page.goto(BASE + "?theme=" + GLASS, wait_until="load", timeout=60000)
        page.wait_for_function(
            "() => window.ThemeRuntime?.activeModule === 'glassmorphism-pro'",
            timeout=15000)
        card = page.locator(".card").first
        card.scroll_into_view_if_needed()
        page.evaluate("""() => {
          const card = document.querySelector('.card');
          card.dispatchEvent(new PointerEvent('pointermove', {
            pointerType: 'mouse', bubbles: true, clientX: 100, clientY: 100
          }));
        }""")
        page.wait_for_timeout(100)
        snap = state(page)
        require(snap["leakedValues"] == 0,
                "Decorative motion ran despite reduced-motion preference")
        evidence.append({"step": "mobile-reduced-motion", **snap})

        # Save both the functional card material and the full first-fold
        # composition; the audit must not crop away the navbar and hero.
        page.screenshot(path=str(OUT / "organic-glass-mobile-card.png"),
                        animations="disabled")
        page.evaluate("() => window.scrollTo(0, 0)")
        page.wait_for_timeout(75)
        page.screenshot(path=str(OUT / "organic-glass-mobile.png"),
                        animations="disabled")
    finally:
        page.close()


def css_without_javascript(browser, evidence: list[dict]) -> None:
    """A standalone theme CSS renders geometry without loading either JS."""
    ctx = browser.new_context(java_script_enabled=False,
                              viewport={"width": 390, "height": 850})
    page = ctx.new_page()
    try:
        page.set_content(f"""<!doctype html>
          <html><head>
          <link rel="stylesheet" href="{BASE}themes/glassmorphism-pro.css">
          </head><body>
          <main id="home" class="container-fluid py-5">
            <div class="container">
              <h1>Organic Glass</h1>
              <div class="card"><div class="card-body">Standalone CSS</div></div>
            </div>
          </main></body></html>""", wait_until="load")
        surface = page.locator(".card").evaluate("""el => {
          const s = getComputedStyle(el);
          const root = getComputedStyle(document.documentElement);
          return {
            backdrop: s.backdropFilter,
            background: s.backgroundColor,
            radius: s.borderRadius,
            animation: s.animationName,
            materialToken: root.getPropertyValue('--glass-organic-canvas').trim()
          };
        }""")
        require(surface["materialToken"] == "#0c182c",
                "Organic CSS tokens not present without JavaScript")
        require(surface["animation"] == "none",
                "Glass cards have unnecessary perpetual animation")
        evidence.append({"step": "standalone-css-no-js", **surface})
    finally:
        ctx.close()


def main() -> int:
    """Run all cases and preserve JSON and screenshots as CI artifacts."""
    OUT.mkdir(parents=True, exist_ok=True)
    evidence: list[dict] = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                desktop_lifecycle(browser, evidence)
                reduced_motion(browser, evidence)
                css_without_javascript(browser, evidence)
            finally:
                browser.close()
    except Exception as exc:
        print(f"FAIL: optional theme runtime: {exc}", file=sys.stderr)
        (OUT / "report.json").write_text(
            json.dumps({"passed": False, "records": evidence,
                        "error": str(exc)}, indent=2), encoding="utf-8")
        return 1

    (OUT / "report.json").write_text(
        json.dumps({"passed": True, "records": evidence}, indent=2),
        encoding="utf-8")
    print("OK: optional module loaded once; cleanup, rapid switching, "
          "no-JS fallback and reduced-motion behaviour passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
