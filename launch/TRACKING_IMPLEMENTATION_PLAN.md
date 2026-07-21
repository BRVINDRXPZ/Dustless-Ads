# Tracking Implementation Plan

**Status:** Internal implementation draft. Owner completion, validated access, evidence, testing, and written approval are required. This document authorizes no live change, connection, publication, outreach, or spend.

## Exact sequence
1. Confirm data owner, privacy/consent rules and production domains. 2. Inventory/create owner-controlled GTM and GA4 only with approval. 3. Define test mode and lead ID generation. 4. Persist first/last UTMs plus GCLID, GBRAID and WBRAID where lawfully available. 5. Map hidden form fields to CRM. 6. Implement validated form success/failure events only after server confirmation. 7. Configure click-to-call diagnostics and qualified call handling via approved call tracking. 8. Create Google Ads conversions: qualified form/call as primary only after human criteria; raw submits/clicks diagnostic. 9. Apply duplicate/spam/test rules. 10. Test consent states. 11. Run synthetic test leads end-to-end. 12. Prepare offline import schema; do not upload. 13. Reconcile won revenue and GP under approved definitions. 14. QA and obtain launch approval. 15. Verify first live leads daily without exposing PII.

## Pass/fail
| Check | Pass criterion | Result | Evidence |
|---|---|---|---|
| Container/property ownership | Correct owner/admin/MFA recorded | TBD | TBD |
| Consent | Nonessential tags honor reviewed behavior | TBD | TBD |
| IDs/UTMs | Lead ID + available UTM/click IDs persist to record | TBD | TBD |
| Form | One server-confirmed event and one CRM record per test | TBD | TBD |
| Calls | Correct routing; qualified-call rule can be reviewed | TBD | TBD |
| Deduplication | Repeat does not inflate primary conversions | TBD | TBD |
| Test/spam | Marked and excluded from business reporting | TBD | TBD |
| Ads goals | Only approved outcomes primary | TBD | TBD |
| Offline file | Schema validates; no upload before approval | TBD | TBD |
| Revenue/GP | Won record ties to approved finance source | TBD | TBD |
| Debug leakage | No PII in URLs/data layer/analytics | TBD | TBD |
| Launch verification | Test matrix signed; rollback rehearsed | TBD | TBD |

Any failed row affecting capture, routing, consent, primary conversion or CRM is automatic NO-GO.
