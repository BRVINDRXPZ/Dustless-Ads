# Command Center QA Checklist

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Pre-release and recurring quality gate.

## Checklist

- [ ] Every screen/file discloses synthetic data where sample values exist.
- [ ] Duplicate IDs, required fields, stages, sources and dates pass.
- [ ] Currency is nonnegative where required; refunds use adjustment rules.
- [ ] No revenue exists without Won/Awarded project linkage.
- [ ] Gross profit does not exceed revenue without approved exception.
- [ ] Links and schema headers pass automated checks.
- [ ] No credentials, remote APIs, trackers or PII.
- [ ] Filters, reset, export, keyboard use and mobile layout work.
- [ ] Source freshness, Unknown and unavailable fields remain visible.
- [ ] Revenue and GP reconciliations have finance sign-off before decisions.
- [ ] Automations are inactive and approval gates documented.

## Commands

`python3 dashboard/prototype/tests/check_dashboard.py` and `python3 -m http.server 8000` followed by local browser review. No deployment command is authorized.
