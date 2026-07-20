# Component System

## Reusable components

- **Header/navigation:** text wordmark placeholder, skip link, responsive wrapping.
- **Hero:** eyebrow, H1, restrained value proposition, assessment CTA, placeholder call CTA.
- **Trust bar:** process statements only; credentials and ratings excluded until verified.
- **Section shell/cards:** consistent spacing and readable line length.
- **Proof placeholder:** neutral hatched panel explicitly requiring approved real photography and permission.
- **Process steps:** Assess → Define scope → Plan execution → Confirm result/care.
- **Qualification/concerns/FAQ:** candid fit, limitations, and disclosure controls.
- **CTA panel:** route-specific form path plus disabled/non-dialing call placeholder.
- **Form tabs:** keyboard-operable buttons and distinct residential/contractor/commercial forms.
- **Footer/legal:** owner-supplied contact placeholders, consent draft, publication warning.

## Tokens

CSS custom properties define warm plaster, pine, ink, moss, clay, focus blue, borders, radii, shadows, and a 72rem content width. Typography uses a system stack; no font request or dependency.

## Tracking contract

Interactive elements carry `data-track` event names and `data-track-label`. Prototype events are written only to an in-memory `window.prototypeDataLayer`; they are not transmitted. Form fields use stable names aligned to the field dictionary.
