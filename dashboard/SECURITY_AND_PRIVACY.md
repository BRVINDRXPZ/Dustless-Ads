# Security and Privacy

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Least-data, least-privilege plan.

## Rules

No secrets or real customer data in Git. Store credentials in approved secret manager outside repository. Role-based access, MFA where supported, periodic access review, encrypted transport/storage, vendor agreements and consent review before integration.

## Data minimization

Dashboard uses IDs and aggregates; restrict phone/email/address; never place PII in UTMs, analytics events, filenames or exports. Synthetic prototype names are fictional.

## Incident response

Stop sync, preserve logs, notify owner/security role, rotate affected credentials outside repo, assess scope, follow applicable legal advice, document remediation. No public response is automated.
