"""Estimate foreground contrast against actual rendered backgrounds.

This is a triage aid for axe-core's *incomplete* colour-contrast results.
It never certifies WCAG compliance. It makes a background-only screenshot,
samples pixels behind selected text nodes and compares them to the computed
foreground colour. Text gradients, overlays, texture boundaries and
pseudo-elements remain candidates for human review.

Usage:
    python3 scripts/audit_rendered_contrast.py
    python3 scripts/audit_rendered_contrast.py --widths 390 1440 --limit 90

Requires a running localhost:8765 gallery, Playwright, Pillow and axe-core.
"""

from __future__ import annotations

import argparse
from collections import Counter
from io import BytesIO
import json
from pathlib import Path
import re
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "quality-results" / "visual-contrast"
AXE = ROOT / "node_modules" / "axe-core" / "axe.min.js"
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
THEMES = sorted(set(re.findall(r"file:\s*['\"]themes/([\w-]+)\.css['\"]", HTML)))
COLOUR = re.compile(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,\s/]+([\d.]+))?\s*\)")
BASE = "http://127.0.0.1:8765/"

# Text becomes transparent while its containing surfaces and decoration stay
# rendered. The selector does not remove background gradients or animations.
MASK_CSS = """
*, *::before, *::after {
  color: transparent !important;
  -webkit-text-fill-color: transparent !important;
  -webkit-text-stroke-color: transparent !important;
  text-shadow: none !important;
  caret-color: transparent !important;
}
"""

def rgb_tuple(value: str) -> tuple[float, float, float, float] | None:
    """Parse the rgb()/rgba() form returned by Chromium computed styles."""
    match = COLOUR.fullmatch(value.strip())
    if not match:
        return None
    r, g, b = (int(match.group(i)) for i in (1, 2, 3))
    alpha = float(match.group(4)) if match.group(4) is not None else 1.0
    return (r, g, b, alpha)


def luminance(channels: tuple[float, float, float]) -> float:
    """Relative sRGB luminance, as specified by WCAG."""
    linear = []
    for channel in channels:
        c = max(0.0, min(255.0, channel)) / 255.0
        linear.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    """WCAG contrast ratio of two opaque colours."""
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def text_data(page, selectors: list[str]) -> list[dict]:
    """Measure visible DOM text geometry and computed foreground styles."""
    return page.evaluate("""(selectors) => selectors.map(selector => {
      let el;
      try { el = document.querySelector(selector); } catch (_) { return null; }
      if (!el) return null;
      const cs = getComputedStyle(el), r = el.getBoundingClientRect();
      if (cs.display === 'none' || cs.visibility === 'hidden' ||
          r.width < 3 || r.height < 3) return null;
      const fill = cs.webkitTextFillColor;
      const ownBg = cs.backgroundImage;
      return {
        selector,
        tag: el.tagName.toLowerCase(),
        excerpt: (el.innerText || el.textContent || '').trim().slice(0, 110),
        x: r.left + window.scrollX, y: r.top + window.scrollY,
        w: r.width, h: r.height,
        color: cs.color, fill,
        opacity: cs.opacity,
        clip: cs.backgroundClip,
        background: cs.backgroundColor,
        image: ownBg.slice(0, 200),
        fontSize: parseFloat(cs.fontSize), fontWeight: cs.fontWeight
      };
    }).filter(Boolean)""", selectors)


def choose_targets(page, limit: int) -> tuple[list[str], int]:
    """Choose representative axe incomplete nodes, prioritising controls."""
    results = page.evaluate("""async () => await axe.run(document, {
      runOnly: {type: 'rule', values: ['color-contrast']},
      resultTypes: ['incomplete']
    })""")
    targets = []
    for rule in results["incomplete"]:
        for node in rule.get("nodes", []):
            if node.get("target") and isinstance(node["target"][0], str):
                targets.append(node["target"][0])
    targets = list(dict.fromkeys(targets))
    patterns = ("btn", "nav-link", "badge", "alert", "card-header",
                "form-label", "tab", "accordion", "text-primary", "lead",
                "navbar", "h1", "h2", "h3", "h4", "input", "modal",
                "small", "table", "page-link", "list-group")
    targets.sort(key=lambda selector: (
        -sum(1 for word in patterns if word in selector), selector
    ))
    return targets[:limit], len(targets)


def sample_points(node: dict, width: int, height: int) -> list[tuple[int, int]]:
    """Use inner 10–90% of the element bounds, avoiding borders and margins."""
    x0, y0, w, h = (node[k] for k in ("x", "y", "w", "h"))
    points = []
    for fx in (0.15, 0.35, 0.5, 0.65, 0.85):
        for fy in (0.2, 0.4, 0.6, 0.8):
            x, y = int(x0 + fx * w), int(y0 + fy * h)
            if 0 <= x < width and 0 <= y < height:
                points.append((x, y))
    return points


def inspect(node: dict, image: Image.Image) -> dict:
    """Estimate a minimum contrast ratio, never a certificate of a pass."""
    record = {key: node[key] for key in (
        "selector", "tag", "excerpt", "color", "fill", "background",
        "image", "clip", "opacity", "fontSize", "fontWeight"
    )}
    foreground = rgb_tuple(node["fill"] or node["color"])
    if not foreground or (node["clip"] == "text"
                          and node["image"] != "none") or node["opacity"] != "1":
        record["status"] = "manual-only"
        record["reason"] = "text gradient, opacity or unsupported computed colour"
        return record

    pixels = image.load()
    scores = []
    samples = sample_points(node, image.width, image.height)
    for x, y in samples:
        px = pixels[x, y]
        background = (float(px[0]), float(px[1]), float(px[2]))
        alpha = foreground[3]
        effective = tuple(alpha * foreground[i] + (1 - alpha) * background[i]
                          for i in range(3))
        scores.append((contrast(effective, background), (x, y), px[:3]))
    if not scores:
        record["status"] = "manual-only"
        record["reason"] = "outside screenshot boundaries"
        return record

    score, location, bg = min(scores, key=lambda sample: sample[0])
    try:
        bold = int(node["fontWeight"]) >= 700
    except ValueError:
        bold = node["fontWeight"] in ("bold", "bolder")
    large = node["fontSize"] >= 24 or (bold and node["fontSize"] >= 18.66)
    threshold = 3.0 if large else 4.5
    record.update({
        "status": "review" if score < threshold else "estimated-clear",
        "min_ratio": round(score, 2), "threshold": threshold,
        "max_ratio": round(max(item[0] for item in scores), 2),
        "background_at_min": list(bg), "sample_coordinate": list(location),
        "samples": len(samples), "note": "Pixel sample estimate, not WCAG certification",
    })
    return record


def main() -> int:
    """Produce per-theme ranked contrast-risk evidence without masking axe."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--widths", nargs="+", type=int, default=[390, 1440])
    parser.add_argument("--limit", type=int, default=90)
    args = parser.parse_args()
    if len(THEMES) != 17 or not AXE.exists():
        print("Expected 17 themes and local axe-core", file=sys.stderr)
        return 2

    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 900},
                                reduced_motion="reduce")
        try:
            page.goto(BASE, wait_until="load", timeout=60000)
            page.add_script_tag(path=str(AXE))
            page.add_style_tag(content=(
                "*, *::before, *::after {animation:none!important;"
                "transition:none!important;scroll-behavior:auto!important;}"
            ))
            for width in args.widths:
                page.set_viewport_size({"width": width, "height": 900})
                for theme in THEMES:
                    page.evaluate("(name) => changeTheme(name, null, false)", theme)
                    page.wait_for_function(
                        """(name) => {
                          const l = document.getElementById('theme-css');
                          return l?.getAttribute('href') === 'themes/' + name + '.css'
                            && l.sheet?.href?.endsWith('/themes/' + name + '.css');
                        }""", arg=theme, timeout=15000)
                    page.evaluate("() => window.scrollTo(0, 0)")
                    page.wait_for_timeout(80)
                    selectors, incomplete_total = choose_targets(page, args.limit)
                    elements = text_data(page, selectors)

                    # Keep screenshot geometry fixed and backgrounds intact.
                    mask = page.add_style_tag(content=MASK_CSS)
                    try:
                        png = page.screenshot(full_page=True,
                                              animations="disabled", type="png")
                    finally:
                        mask.evaluate("(el) => el.remove()")
                    image = Image.open(BytesIO(png)).convert("RGB")
                    results = [inspect(node, image) for node in elements]
                    risks = sorted((x for x in results if x["status"] == "review"),
                                   key=lambda x: x["min_ratio"])
                    row = {
                        "theme": theme, "width": width,
                        "incomplete_nodes": incomplete_total,
                        "inspected": len(results),
                        "review": len(risks),
                        "manual_only": sum(x["status"] == "manual-only"
                                           for x in results),
                        "risks": risks,
                        "other": [x for x in results if x["status"] != "review"],
                    }
                    rows.append(row)
                    print(f"{width}px {theme}: inspected {len(results)}/"
                          f"{incomplete_total}; review {len(risks)}; "
                          f"manual-only {row['manual_only']}", flush=True)
        finally:
            browser.close()

    (OUT / "report.json").write_text(
        json.dumps({
            "method": "rendered background sampling; NOT proof of WCAG pass",
            "viewports": args.widths, "samples_per_target": 20,
            "per_page_limit": args.limit, "scans": rows,
        }, indent=2), encoding="utf-8")
    summary = {
        "sampled": sum(r["inspected"] for r in rows),
        "review": sum(r["review"] for r in rows),
        "manual_only": sum(r["manual_only"] for r in rows),
        "by_theme": dict(Counter({r["theme"]: sum(x["review"] for x in rows
                                  if x["theme"] == r["theme"]) for r in rows})),
    }
    (OUT / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8")
    print("Rendered contrast triage:", summary, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
