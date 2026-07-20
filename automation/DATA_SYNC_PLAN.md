# Data Sync Plan

> **Planning specification — inactive.** No live accounts, credentials, communications, or real customer data.

## Purpose

Begin with versioned manual CSV: land immutable raw → validate schema/hash/row counts → quarantine → normalize IDs/enums → upsert idempotently → reconcile control totals → publish derived tables. Future read-only connectors require owner/security approval. Finance never overwritten by channel data.

## Status

Specification only. No workflow, message, notification, upload, publishing, budget change, or live connection has been activated.
