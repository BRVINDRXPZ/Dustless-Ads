# Command Center Data Model

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Canonical relationship model; schemas are implementation contracts.

## Conventions

Primary keys are immutable opaque IDs with entity prefix. Foreign keys must exist or be quarantined. Timestamps are ISO 8601 UTC; local business display may use `America/Chicago` with zone shown. Money is decimal USD, never binary float.

## Entities

| Entity | Primary key | Relationships |
|---|---|---|
| Contact | contact_id | Account via account_id; leads and activities |
| Account | account_id | Contacts, opportunities; subtype contractor/commercial/household |
| Lead | lead_id | Contact; source/campaign; opportunity; calls/forms |
| Opportunity | opportunity_id | Lead/account; estimates/proposals/projects |
| Estimate | estimate_id | Opportunity |
| Proposal | proposal_id | Opportunity/estimate |
| Project | project_id | Won opportunity; invoices; costs |
| Invoice | invoice_id | Project |
| Payment | payment_id | Invoice |
| Marketing Source | source_id | Campaign and attribution touch |
| Campaign | campaign_id | Source; ad groups/content/leads/cost |
| Ad Group | ad_group_id | Campaign; keywords/search terms |
| Keyword | keyword_id | Ad group |
| Search Term | search_term_id | Ad group/keyword |
| Landing Page | landing_page_id | Form submissions/touches |
| Call | call_id | Lead/source/touch |
| Form Submission | submission_id | Lead/landing page/touch |
| Review | review_id | Project/contact only with governed internal join |
| Social Content | content_id | Campaign/touches |
| B2B Activity | activity_id | Account/contact/opportunity |
| Experiment | experiment_id | Campaign/content and observations |
| Referral | referral_id | Lead/referrer contact/account |
| Contractor Partner | account_id | Account subtype/view |
| Commercial Account | account_id | Account subtype/view |

## Cardinalities

Account 1→many contacts/opportunities; contact 1→many leads; lead 0→1 primary opportunity and many touches; opportunity 0→many estimates/proposals and 0→1 won project; project 1→many invoices; invoice 1→many payments; campaign 1→many ad groups; sources/campaigns many→many leads through attribution touches.

## Lifecycle integrity

A project with booked revenue requires a Won/Awarded opportunity. Payments cannot exceed adjusted invoice balance without an exception. Gross profit requires approved revenue recognition and actual attributable costs; otherwise status is pending.

## Reuse mapping

`tracking/CRM_FIELD_MAP.csv`, `LEAD_SOURCE_SCHEMA.csv`, and `OFFLINE_CONVERSION_SCHEMA.csv` map capture fields; `b2b/PIPELINE_SCHEMA.csv` maps B2B records. Do not silently rename upstream fields.
