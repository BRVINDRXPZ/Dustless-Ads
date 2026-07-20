# Measurement Plan

**Status:** Design only. No analytics, ads, call platform, CRM, or live site is connected.

## Business questions

Measure which consented sources produce qualified calls/inquiries, scheduled and completed estimates, proposals, wins, revenue, and gross profit—not merely clicks. Raw leads are an early optimization signal; business outcomes are the decision standard.

## Funnel and ownership

1. Ad click stores permitted click IDs and UTMs.
2. Validated lead receives server event/lead UUID and enters **New**.
3. Owner classifies qualified/disqualified with a reason.
4. Estimate/site walkthrough scheduled and timestamped.
5. Estimate completed.
6. Proposal sent with value where appropriate.
7. Won/lost recorded.
8. Revenue booked in the approved financial/system-of-record definition.
9. Gross profit booked only from approved cost/accounting logic.
10. Eligible consented outcomes upload using click ID or privacy-approved enhanced-conversion identifier, event name/time/value/currency, order/event ID; results reconcile to CRM.

## Governance

CRM is the proposed outcome system of record; exact product is undecided. Browser events are diagnostic. Server acceptance creates form conversions. Qualified calls require review/classification. Offline events use immutable event IDs and original lead attribution. Secondary events must not become primary Smart Bidding goals after mature qualified/offline data exists.

## Reporting cuts

Audience, service, broad geography, campaign/ad group, landing page, lead type, qualification reason, lifecycle stage, and time-to-stage. Suppress small/privacy-sensitive segments and never send names, phones, emails, street addresses, descriptions, or upload data to analytics.

## Launch criteria

Approved definitions, consent/legal review, test properties/actions, CRM ownership, dedupe, call qualification, form backend, end-to-end QA, reconciliation, mobile validation, proof/claim approval, and written owner launch approval. Phase 4 remains paused.
