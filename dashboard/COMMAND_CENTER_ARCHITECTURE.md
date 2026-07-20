# Command Center Architecture

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Defines the smallest safe, auditable central operating system.

## Operating principle

A single governed lead register is the spine. Stable IDs join source → lead → opportunity → project → invoice/payment → recognized revenue and actual gross profit. Channel data diagnoses demand; it never overrides verified business outcomes. Unknown and missing remain visible.

## System layers

**Capture:** local forms/calls/manual intake and UTM fields. **System of record:** owner-selected CRM or controlled sheet during Phase A. **Finance evidence:** approved invoice, payment and job-cost exports. **Reporting:** versioned local extracts transformed into normalized tables. **Action:** human-reviewed queue. Every sync logs run ID, source, row counts, errors, freshness, and approver.

## Source-of-truth precedence

Finance system for invoices/payments; approved job-cost record for actual cost; CRM for lifecycle; call/form logs for interactions; channel platforms for delivery/cost. Conflicts are exceptions, not silently overwritten.

## Decision framework

**Scale:** sufficient reconciled wins and gross profit, capacity available, stable quality. **Fix:** demand exists but tracking, response, funnel, or margin fails. **Hold:** sample too small, stale/missing data, approval/capacity constraint. **Stop:** owner-approved action after verified persistent negative economics, policy risk, or no operational fit. No numeric threshold is invented.

## Views and filters

Executive scorecard; lead funnel/source economics; Ads; local SEO; social; B2B; operations; experiments; owner queue. Shared filters: date, source, campaign, service, geography, segment (residential/contractor/commercial/referral partner), and lead owner.

## Data flow and refresh

Manual versioned CSV import first. Validate → quarantine invalid rows → normalize → reconcile → calculate → publish local report → human sign-off. Daily operational, weekly funnel, monthly economics, quarterly strategy. Freshness is displayed per source.

## Controls

Least privilege; no secrets in repo; synthetic prototype only; immutable raw extracts; audit trail; approval gates; reversible imports; visible unknowns; denominator and eligibility definitions beside metrics.

## Implement First

Use one controlled lead register plus opportunity/project and monthly cost/job-cost tabs. Require lead ID, received time, normalized source, segment, qualification, lifecycle stage, estimate/proposal dates, won/lost status, project ID, booked revenue, actual direct cost, and gross profit. Reconcile weekly to invoices/payments. This is the smallest reliable system.

## Implement Next

After core accuracy: approved form and call capture, CRM migration, finance export, Google Ads/Analytics/GBP/Search Console/social read-only imports, B2B activity joins, governed dashboards, internal reminders, data-quality reports, and reviewed offline conversion files.

## Hold Until Data Is Clean

Hold multi-touch fractional attribution, Smart Bidding/offline value imports, forecasts, customer lifetime value, capacity forecasts, automated budget changes, and broad customer-facing workflows until IDs, stages, sources, revenue, costs, consent, and reconciliation pass QA.

## Never Automate Blindly

Reject automatic ad-budget increases; customer-facing promises; estimate creation; project acceptance; negative-review replies; contractor spam; commercial bids; public publishing; deletion of business records; automation without audit logs; dashboards that hide missing data; and forecasts based on invented assumptions.
