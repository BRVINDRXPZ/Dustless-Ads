# Spam and Duplicate Policy

## Spam controls

Layer server-side validation, honeypot, minimum-completion timing as a signal (not sole rejection), CSRF, origin checks, per-IP/device-safe rate limits, reputation/risk scoring, upload scanning, payload/length allowlists, and monitored quarantine. CAPTCHA is escalation-only after accessibility/privacy review. Never disclose exact detection thresholds publicly.

## Classification

`Spam` is demonstrably abusive/automated/irrelevant; `Duplicate` is an additional record for the same opportunity; neither equals a low-quality but genuine lead. A reviewer can reverse classifications. Preserve audit reason, reviewer, timestamp and linked canonical lead.

## Dedupe

Use server idempotency key first. Then match normalized phone/email plus project ZIP/service and a provisional 30-day window. Calls use provider call ID and linked opportunity. Offline uploads use immutable stage event/order IDs. Merge attribution history; do not overwrite first touch or delete activity. Report gross and deduplicated leads.
