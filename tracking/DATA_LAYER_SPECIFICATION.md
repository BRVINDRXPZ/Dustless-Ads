# Data Layer Specification

Production proposal: `window.dataLayer = window.dataLayer || []` only after approved implementation; the prototype instead uses `window.prototypeDataLayer` and sends nothing.

```json
{"event":"form_start","event_id":"UUID","event_version":"1.0","page_type":"service","page_path":"/refinishing/","lead_type":"residential","service_category":"refinishing","form_id":"residential_estimate","consent_state":"granted|denied|unknown"}
```

## Event payload rules

- Interaction: `element_type`, approved `element_label`, `form_id`, `form_step`, `error_code` (never entered value).
- Upload: type category and success flag only; never filename/content/URL.
- Submission: server-issued event/lead ID, form/lead type; browser receipt event must share ID for dedupe.
- Offline: original immutable lead ID, stage event ID/time, click identifier type when eligible, value/currency only at approved stages.
- Calls: provider call ID, classification, duration bucket, source class; recording/transcript data never enters analytics.

Validate schema, enum, consent and prohibited-PII rules before dispatch. Retention and access follow the approved privacy policy.
