# Measurement QA Checklist

- [ ] Test-only properties/actions and synthetic records clearly marked.
- [ ] Consent states tested: unknown, denied, granted, changed/revoked.
- [ ] Every dictionary event fires once at correct trigger; no conversion on validation/client-only success.
- [ ] Parameters validate; no PII, address, descriptions, filenames, call content or secrets.
- [ ] GCLID, GBRAID, WBRAID, UTMs, first/latest touch, landing path and timestamps survive approved flow.
- [ ] Redirects preserve permitted IDs; canonicals exclude parameters.
- [ ] Forms: errors, retries, back/refresh, duplicate, spam, rate limit, upload spoof/size/malware, server outage.
- [ ] Calls: ad/web/DNI fallback, hours/after-hours, missed/repeat, classifications and qualified review.
- [ ] CRM stages/reasons and stage timestamps map exactly; won/lost and values reconcile.
- [ ] Offline upload uses correct timezone, currency, identifiers, dedupe, adjustment/retraction process.
- [ ] Browser, server, CRM and ad counts reconcile within documented timing/logic differences.
- [ ] Secondary events excluded from mature Smart Bidding primary goals.
- [ ] Mobile, accessibility, browser and tag-performance QA pass.
- [ ] Owner signs claims/assets, legal/consent, operations, numbers/hours/areas and launch authorization.
