# Google Ads Dashboard

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

View specification.

## Metrics and behavior

Spend, clicks, impressions, CTR, CPC, search impression share/lost share, calls, forms, qualified leads, scheduled estimates, wins, revenue, gross profit, CPQL, CAC; search-term quality and geography/device/day-hour/campaign/ad-group cuts. Platform delivery fields require current Google Ads export/API validation; CRM/finance joins require IDs and offline reconciliation. Never imply unavailable fields exist.

## Controls

Shared date/source/campaign/service/geography/segment/owner filters where applicable; show source freshness, missingness, synthetic badge in prototype, and export only filtered non-PII demonstration rows.

## Decision use

Record Scale/Fix/Hold/Stop with evidence. Default to Hold when coverage, volume, reconciliation, or capacity is inadequate.
