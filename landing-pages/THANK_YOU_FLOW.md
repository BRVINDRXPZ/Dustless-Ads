# Thank-You Flow

1. Server validates, rate-limits, scans allowed uploads, creates an idempotent lead, and records consent/attribution.
2. Server returns a non-guessable submission receipt identifier; never expose CRM IDs or personal data in the URL.
3. Browser navigates to `/thank-you/` and emits `thank_you_view` with submission type and event ID only after consent rules permit.
4. Page confirms receipt—not acceptance, availability, price, or response deadline—and offers a placeholder call path for urgent clarification.
5. CRM creates **New**, routes by residential/contractor/commercial, and starts approved handling workflow.
6. Failures retain non-sensitive form state where safe, route to `/form-error/`, and provide retry/contact options; do not fire submission conversion.
7. Submission event is deduplicated using server event/lead ID across browser/server destinations.

The local prototype never performs steps 1–6: it explicitly states that nothing was sent.
