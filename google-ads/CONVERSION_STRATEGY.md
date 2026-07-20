# Conversion Strategy

## Goal hierarchy

| Action | Category | Initial bidding role | Qualification/value rule |
|---|---|---|---|
| Qualified phone call | Primary | Primary after call-duration/content qualification is defined | Service + geography + decision authority + viable scope; duration alone is not quality |
| Qualified estimate form | Primary | Primary | Server/CRM-confirmed unique submission meeting approved rules |
| Estimate scheduled | Primary offline | Primary when import QA passes | Unique accepted appointment, not calendar click |
| Commercial inquiry | Primary | Campaign-specific primary | Valid organization/project, geography, scope, authority |
| Contractor inquiry | Primary | Campaign-specific primary | Valid trade/project fit and bid readiness |
| Site walkthrough scheduled | Primary offline | Primary for commercial | Accepted scheduled walkthrough |
| Proposal sent | Down-funnel primary | Observation, then value input | CRM stage and proposal identifier |
| Job won | Down-funnel primary | Value optimization candidate | Signed/accepted under owner definition |
| Revenue booked | Value outcome | Value optimization after reconciliation | Owner-approved booked-revenue definition |
| Gross profit booked | Value outcome | Preferred economic value only when reliable | Consistent cost policy; never fabricate |
| Click-to-call, form start, photo upload, email click, gallery engagement, directions, service-page engagement | Secondary | Observation only | Diagnose friction; do not bid to these once primary data is viable |

## Implementation specification

1. Create a durable lead ID and capture GCLID/GBRAID/WBRAID where consent and platform rules permit.
2. Deduplicate web submissions on server/CRM success, exclude spam/test records, and test reloads/back-button behavior.
3. Use dynamic number insertion with a fallback number and call recording/consent only if legally and operationally approved.
4. Define phone qualification by disposition, not only duration. Set a provisional duration threshold only after historical call review.
5. Import milestones with event time, currency/value policy, identifiers, and correction/retraction process.
6. Separate campaign-specific goal sets so consumer campaigns do not optimize toward B2B actions or weak micro-events.
7. Reconcile Ads, analytics, call tracking, forms, CRM, estimates, wins, revenue, and gross profit weekly.

## Consent and privacy

Owner/legal review must approve consent mode, privacy notice, call recording, enhanced-conversion use, retention, photo uploads, and data access. Send only data permitted by policy and law; never upload sensitive free-text or floor photos as customer data.

## QA acceptance

Each action fires once, carries the correct timestamp/source, survives cross-device/consent cases as designed, appears in the right goal category, imports test records without bidding contamination, and can be reversed. Use test campaigns/data or mark test records; do not create live spend.
