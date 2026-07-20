# Accessibility Checklist

Target WCAG 2.2 AA; conduct automated and manual testing.

- [ ] Unique title, one descriptive H1, semantic landmarks, logical heading order.
- [ ] Skip link, keyboard operation, visible focus, no trap, sensible focus order.
- [ ] Text contrast ≥4.5:1; large text ≥3:1; UI boundaries/focus ≥3:1.
- [ ] Reflow at 320 CSS px and 200%/400% zoom; text spacing override causes no loss.
- [ ] Every control has a programmatic label; required state/instructions not color-only.
- [ ] Errors identify field and remedy; summary receives focus; status uses `aria-live`.
- [ ] Images have contextual alt or empty alt when decorative; proof placeholders are text, not images.
- [ ] Link purpose is clear; repeated CTAs have context.
- [ ] Native disclosure/tab behavior is screen-reader tested; tab implementation exposes selected state.
- [ ] Motion respects `prefers-reduced-motion`; no flashing content.
- [ ] Consent copy is adjacent to checkbox and privacy link.
- [ ] Run axe/Lighthouse plus NVDA/VoiceOver and keyboard-only review before release.
