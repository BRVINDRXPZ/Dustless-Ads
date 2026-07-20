# Event Naming Standard

Use lowercase `snake_case`, stable verbs, no spaces, no vendor prefix, and ≤40 characters where a destination requires it. Event name describes the outcome, not the UI label. Never encode customer, phone, email, ZIP, address, company, project description, or file name in event names/parameters.

Required common parameters: `event_id`, `event_version`, `page_type`, `page_path`, `lead_type` where applicable, `service_category`, and `consent_state`. Allowed values are documented enums. Server-side timestamps are ISO 8601 UTC. Money uses numeric value plus ISO 4217 currency. Changes require versioning and dictionary/QA updates; do not silently repurpose an event.
