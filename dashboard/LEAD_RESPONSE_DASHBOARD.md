# Lead Response Dashboard

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

View specification.

## Metrics and behavior

New leads, first response, contact attempts, median and percentile response time, business-hours response, uncontacted aging, missed calls, owner workload. Inputs: CRM activity and approved call logs; unavailable until integrated. Filters: date/source/segment/owner/geography. Flag clock anomalies and automated acknowledgements separately from human response.

## Controls

Shared date/source/campaign/service/geography/segment/owner filters where applicable; show source freshness, missingness, synthetic badge in prototype, and export only filtered non-PII demonstration rows.

## Decision use

Record Scale/Fix/Hold/Stop with evidence. Default to Hold when coverage, volume, reconciliation, or capacity is inadequate.
