/**
 * Optional progressive enhancement for glassmorphism-pro.css.
 *
 * One directional, pointer-responsive highlight per card. No global mouse
 * tracking, no perpetual animation loops, no DOM injection and no effects on
 * touch or reduced-motion devices. The CSS supplies the complete appearance.
 */
export function mount({ root, signal, reducedMotion }) {
  const cards = Array.from(root.querySelectorAll(".card"));
  const decorated = [];
  let frame = 0;
  let pending = null;

  function flush() {
    frame = 0;
    if (!pending || signal.aborted) return;
    const { card, x, y } = pending;
    card.style.setProperty("--glass-light-x", x + "%");
    card.style.setProperty("--glass-light-y", y + "%");
    pending = null;
  }

  for (const card of cards) {
    card.classList.add("glass-interactive");
    decorated.push(card);

    card.addEventListener("pointermove", event => {
      // A mouse or trackpad can enhance the effect; gestures and reduced
      // motion must not continuously update a decorative spotlight.
      if (signal.aborted || reducedMotion.matches ||
          event.pointerType === "touch") return;

      const rect = card.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      const x = Math.max(0, Math.min(100,
        Math.round(100 * (event.clientX - rect.left) / rect.width)));
      const y = Math.max(0, Math.min(100,
        Math.round(100 * (event.clientY - rect.top) / rect.height)));
      pending = { card, x, y };
      if (!frame) frame = window.requestAnimationFrame(flush);
    }, { signal, passive: true });
  }

  return function cleanup() {
    if (frame) window.cancelAnimationFrame(frame);
    frame = 0;
    pending = null;
    for (const card of decorated) {
      card.classList.remove("glass-interactive");
      card.style.removeProperty("--glass-light-x");
      card.style.removeProperty("--glass-light-y");
    }
  };
}
