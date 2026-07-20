# Form Strategy

## Paths and friction

Residential begins with contact, ZIP, service, area/timeline, occupancy/use, description, preference, and consent; address and photos are optional. Contractor and commercial forms expose organization and project-specific fields. Long fields are grouped but kept on one page in the prototype to avoid false progress. Only name, email or phone (production rule), location, scope basics, and consent should block submission.

## Prototype behavior

There is **no endpoint**. JavaScript validates required fields, email/phone patterns, consent, honeypot, and selected file metadata. A valid demo submission is intercepted, a local-only event is recorded in memory, and a clear “not sent” message appears. Files are never uploaded or read.

## Production requirements

- Validate and normalize again server-side; reject unknown fields and unsafe lengths.
- CSRF protection, same-origin controls, honeypot, privacy-safe risk scoring, and IP/account rate limits.
- Permit PDF/JPG/JPEG/PNG only after MIME, extension, signature and malware checks; provisional maximum 10 MB each and 25 MB/request, pending owner/security approval.
- Store outside the public web root with randomized object names, encryption/access controls, retention/deletion rules, and short-lived authorized access. Never execute or serve active content inline.
- Generate server-side UUID lead/event IDs. Do not trust client timestamps, attribution, consent, or hidden fields without validation.
- Detect duplicates on normalized contact + project ZIP/service within a provisional 30-day window; preserve attribution history and link records rather than silently deleting.
- Return accessible field and form errors without disclosing security logic. Use idempotency keys to prevent retry duplicates.
- Capture first/last UTM, GCLID/GBRAID/WBRAID when present, landing path, referrer domain (minimized), timestamps, consent version/time, and derived device category only when permitted.
- Never put customer details, addresses, uploads, or raw identifiers in analytics events.

Legal/privacy counsel and the owner must approve consent, retention, call recording, and contact practices before production.
