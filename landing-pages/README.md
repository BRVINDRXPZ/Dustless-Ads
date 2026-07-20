# Phase 5: Conversion Landing Pages and Measurement Architecture

**Status:** Complete local prototype and implementation specification; **not approved for publication or live integration**.

This package creates the conversion layer specification required before Phase 4 advertising can launch. It does not modify the live site, connect an account, submit a lead, publish a page, include production identifiers, or authorize spend.

## Repository inspection

Inspection on 2026-07-20 found no website source, web framework, package/lock file, hosting configuration, forms, tracking code, brand image assets, project images, testimonial assets, analytics IDs, or CRM integration in the repository. Existing files were strategy/research/Google Ads documentation and placeholder workspace READMEs. Therefore Phase 5 uses dependency-free HTML, CSS, and minimal JavaScript.

## Preview and test

From the repository root:

```bash
python3 -m http.server 8080 --directory landing-pages/prototype
# Visit http://localhost:8080/
python3 landing-pages/prototype/tools/check_prototype.py
```

Opening `prototype/index.html` directly also works. Forms have no `action`; JavaScript validates locally, never transmits data or reads files, and records demo tracking only in memory at `window.prototypeDataLayer`.

## Deliverable map

- Architecture/components/content: `SITE_ARCHITECTURE.md`, `COMPONENT_SYSTEM.md`, `CONTENT_REQUIREMENTS.md`.
- Claims/assets: `CLAIMS_AND_ASSET_GAPS.md` with page matrix and five-project capture plan.
- Forms/journeys: `FORM_STRATEGY.md`, `FORM_FIELD_DICTIONARY.csv`, `THANK_YOU_FLOW.md`.
- QA: mobile, accessibility, page-speed checklists and automated prototype checker.
- Acquisition/SEO: metadata, URL, CTA CSVs.
- Measurement: complete vendor-neutral specifications under `../tracking/`.

## Ruthless conversion priority

Scores are internal planning judgments on a 1–5 scale (5 = more/stronger), not measured performance. **Claim risk is inverse for readiness: 5 means riskier.** Proof readiness reflects the current absence of registered assets.

| Rank | Page | Ads importance | Intent | Revenue potential | Proof readiness | Form readiness | Tracking readiness | Operational fit | Claim risk | Build priority |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Refinishing | 5 | 5 | 5 | 2 | 4 | 3 | 4 | 2 | 5 |
| 2 | Dust-controlled sanding | 5 | 5 | 4 | 1 | 4 | 3 | 4 | 4 | 5 |
| 3 | Installation | 4 | 5 | 5 | 1 | 4 | 3 | 4 | 3 | 5 |
| 4 | Repair/restoration | 4 | 5 | 3 | 1 | 4 | 3 | 3 | 4 | 4 |
| 5 | Request estimate | 5 | 5 | 5 | 3 | 4 | 3 | 5 | 2 | 5 |
| 6 | Contractor/builder | 3 | 4 | 5 | 1 | 4 | 3 | 2 | 4 | 3 |
| 7 | Commercial | 3 | 4 | 5 | 1 | 4 | 3 | 2 | 5 | 3 |
| 8 | Historic/heart pine | 3 | 4 | 4 | 1 | 4 | 3 | 2 | 5 | 3 |
| 9 | Northshore | 2 | 4 | 3 | 1 | 4 | 3 | 1 | 5 | 2 |

## Exact minimum viable launch set

After—not before—all owner, proof, technical, legal, QA, and written approval gates pass: launch only **Refinishing**, **Dust-Controlled Sanding**, **Installation**, the shared **Request an Estimate**, **Thank-You**, **Form Error**, **Privacy/Consent**, **Service Areas**, and enough approved **Gallery/Proof** modules to substantiate those three services. Start with corresponding tightly matched Phase 4 Search campaigns only. Repair/restoration follows after minimum/fit rules and matching language are approved. Historic, commercial, contractor, and Northshore remain held until their specific proof, capacity, geography, and operating rules exist.

Phase 4 remains paused even if a prototype page is visually complete. The MVP is a recommended sequence, not launch authorization.

### Ready to Preview

All 15 local prototypes: eight service pages, request estimate, gallery, reviews/proof, service areas, thank-you, form error, and privacy/consent. Placeholder content and non-submitting behavior are intentional.

### Ready After Owner Inputs

No page is publish-ready today. Owner input is required for phone, hours, address-display policy, exact service areas, minimums, approved services/methods, offers/CTAs, operating capacity, response process, consent/contact policy, claims, credentials, and permissioned project/review assets. Refinishing, sanding, installation, repair, estimate, gallery/proof, and service-area content can advance after those inputs; historic, commercial, contractor, and Northshore require additional specific proof/readiness decisions.

### Ready After Technical Integration

Every conversion page requires approved hosting/templates, secure server validation and upload handling, consent management, production privacy language, CRM/system-of-record mapping, call/DNI implementation, analytics/ad test configuration, attribution persistence, offline conversion pipeline, security testing, reconciliation, and documented mobile/accessibility/performance QA.

### Do Not Publish

All prototype pages and every placeholder proof/review/credential/service-area/contact section. Historic-specialist implications, commercial/contractor capability claims, Northshore coverage, dust-process specifics, license/insurance language, offers, response promises, reviews, photography, and legal/privacy text are unsafe until evidence, permission, operational approval, and any required legal review are documented. **Do not launch Phase 4 ads or use these pages publicly without explicit written owner approval.**
