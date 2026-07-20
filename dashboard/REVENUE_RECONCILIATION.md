# Revenue Reconciliation

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Monthly control from lead to finance evidence.

## Chain

Lead → estimate → proposal → won opportunity → project → invoice → payment. Join customer/contact/account and primary/referral source through immutable IDs. Booked, invoiced, recognized and collected revenue are distinct.

## Procedure

Freeze period extract; validate IDs; reconcile won projects to approved proposals/change orders; reconcile invoice totals and adjustments; reconcile payments/refunds/retainage; resolve exceptions; finance signs; lock version; publish coverage.

## Exception controls

| Case | Control |
|---|---|
| Duplicate jobs | Unique project ID; duplicate account/address/scope/date review |
| Partial payments/deposits | Apply to invoice; separate booked, recognized and cash |
| Change orders | Versioned approved amount linked to project |
| Refunds | Negative adjustment linked to original invoice/payment |
| Cancelled jobs | Preserve record; reverse unearned booking under approved policy |
| Shared projects | One project master; participant links; no double count |
| Commercial retainage | Separate receivable/retained amount and release date |
| Multiple sources | One governed primary plus non-additive assists |
| Unknown source | Keep Unknown and assign correction queue |
| Closed outside CRM | Exception import with evidence and retrospective source review |

## Control totals

Project count/amount, invoice amount, adjustments, recognized revenue, cash received, open receivable and unknown-source amount must tie to approved source totals or carry a documented exception.
