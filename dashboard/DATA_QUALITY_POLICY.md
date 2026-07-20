# Data Quality Policy

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Makes missing and unreliable data visible.

## Standards

Required fields per schema; accountable field owner; enum and referential validation; snake_case machine fields; ISO 8601 timestamps; ISO dates; decimal USD; E.164 phones when collected; syntax-check/lowercase emails while preserving raw under restricted access.

## Controls

Exact/fuzzy duplicate flags; normalized source taxonomy; legal stage transition checks; won-to-project integrity; monthly revenue and GP reconciliations; explicit Unknown/Not collected/Not applicable; append-only audit logs.

## Correction workflow

Detect → quarantine/flag → assign owner → compare source evidence → correct without overwriting raw record → record before/after/reason/time/actor → rerun QA → approve.

## Monthly review

Coverage, duplicates, invalid stages/sources, orphan FKs, stale feeds, unreconciled projects, unknown-source rate, correction aging. Never impute business outcomes.

## Ownership

Sales owns qualification/stage; marketing owns source/campaign/cost; operations owns project state; finance owns invoices/payments/revenue/cost/GP; system administrator owns IDs, access and logs.
