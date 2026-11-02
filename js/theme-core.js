/**
 * Theme Core v1 — opt-in lifecycle for standalone Bootstrap themes.
 *
 * The CSS is always sufficient on its own. A matching theme module may add
 * progressive enhancement; it must return a synchronous cleanup function.
 * Only explicitly registered modules are requested, avoiding 404s for the
 * other themes. No framework or bundler is required.
 */
(function (global) {
  "use strict";

  // Include a theme here when themes/<name>.js exists and exports mount().
  // This is intentionally an allowlist, not a failed network request per CSS.
  const enhancedThemes = new Set(["glassmorphism-pro"]);
  const baseUrl = new URL("../", document.currentScript.src);
  const motionPreference = global.matchMedia("(prefers-reduced-motion: reduce)");

  let generation = 0;
  let activeTheme = null;
  let controller = null;
  let dispose = null;
  let activeModule = null;

  function unmount() {
    // Abort removes event handlers added with { signal }, then release DOM
    // classes and inline variables. Switching themes must leave no residue.
    if (controller) {
      controller.abort();
      controller = null;
    }
    if (typeof dispose === "function") {
      try {
        dispose();
      } catch (error) {
        console.error("Theme cleanup failed:", error);
      }
    }
    dispose = null;
    activeModule = null;
  }

  async function activate(name) {
    if (typeof name !== "string" || !/^[a-z0-9-]+$/.test(name)) {
      return false;
    }

    const requestId = ++generation;
    unmount();
    activeTheme = name;
    document.documentElement.dataset.activeTheme = name;

    if (!enhancedThemes.has(name)) {
      return true;
    }

    // The module is resolved relative to theme-core.js. It therefore works
    // in GitHub Pages subpaths and Django's /static/ folder alike.
    const moduleUrl = new URL("themes/" + name + ".js", baseUrl);
    try {
      const module = await import(moduleUrl.href);
      if (requestId !== generation) return false;

      if (typeof module.mount !== "function") {
        throw new TypeError(name + ".js must export mount(context)");
      }

      const nextController = new AbortController();
      controller = nextController;
      const release = module.mount({
        root: document,
        signal: nextController.signal,
        reducedMotion: motionPreference,
        name
      });
      dispose = typeof release === "function" ? release : null;
      activeModule = name;
      return true;
    } catch (error) {
      if (requestId === generation) {
        unmount();
        // Optional effects must never prevent selecting a CSS theme.
        console.warn("Optional theme enhancement unavailable:", name, error);
      }
      return false;
    }
  }

  global.ThemeRuntime = Object.freeze({
    activate,
    get currentTheme() { return activeTheme; },
    get activeModule() { return activeModule; }
  });
})(window);
