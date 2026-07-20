# Backup and Recovery

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Versioned recovery specification.

## Backup

After tool selection: encrypted daily incremental and periodic full backups for CRM/config/export logs; immutable monthly reconciliation snapshots; repository via Git remote. Retention and location require owner/legal approval.

## Restore test

Quarterly in isolated environment: select restore point, verify checksums, IDs, row/control totals, permissions and audit logs; record RPO/RTO observed. Never test with production messaging enabled.

## Failure priorities

Preserve raw source evidence and finance records; restore system of record before derived dashboard; regenerate calculations; reconcile before reopening decisions. RPO/RTO remain TBD pending system choice.
