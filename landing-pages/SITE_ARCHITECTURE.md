# Site Architecture

**Status:** Local prototype; no publishing authorization.

## Routing model

The prototype uses one semantic page shell and `assets/app.js` page data. Each service route is a small HTML entry point carrying a `data-page` key. This keeps structure reusable and migration-friendly without a framework.

| Layer | Routes | Purpose |
|---|---|---|
| Service | refinishing, dust-controlled-sanding, installation, repair-restoration, historic-heart-pine, commercial, contractor-builder, northshore | Intent-matched acquisition |
| Conversion | request-estimate | Residential, contractor, and commercial paths |
| Proof | gallery, reviews-proof | Permission-gated shared frameworks |
| Geography | service-areas | One substantive coverage page; no thin town clones |
| State/legal | thank-you, form-error, privacy-consent | Safe outcomes and draft disclosures |

## Journey

Search/ad → matching service page → qualification and proof → estimate path/call → validated lead → thank-you → CRM qualification → offline outcome. All production transitions remain blocked.

## Internal linking

Every service page links to estimate, gallery, proof, areas, privacy, and at least two relevant services. Header/footer provide stable navigation. Canonicals are proposed production-relative paths and must be replaced with the approved domain implementation.
