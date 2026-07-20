# Google Ads Account Structure

**Status:** offline production package; owner approval, platform validation, tracking QA, landing pages, and budget approval are required before upload. No live account was accessed.

## Naming and hierarchy

Use `Search | {Market} | {Service} | {Audience}` for campaigns, `{Intent theme} | {Geo}` for ad groups, and labels `P4`, `launch`, `hold`, `later-test`, audience, service, and geography. Keep one Search campaign per distinct budget, geography, conversion goal, or business constraint. Do not fragment merely to place keywords in names.

| Layer | Design |
|---|---|
| Account | One owner-controlled business account; billing and administrator ownership verified before work |
| Shared library | Account negative list, approved conversion goals, brand safety exclusions, asset library |
| Campaigns | Brand; Refinishing; Dust-Controlled Sanding; Installation; Repair/Restoration; Historic/Heart Pine; Commercial; Contractor/Builder; Northshore |
| Ad groups | One service/intent family; exact and phrase together when copy and landing intent match |
| Ads | Two materially different RSAs per launch ad group; no unsupported proof |
| Keywords | Exact and phrase at launch; broad only in isolated later tests after qualified conversion signals |
| Assets | Account-level safe assets plus campaign-specific sitelinks/snippets; calls only during answered hours |

## Settings blueprint

- Search Network only at launch. Disable Display expansion and Search Partners initially; test Partners later with segmented quality reporting.
- Final URLs, tracking templates, auto-tagging, consent behavior, and UTMs must pass QA.
- Use campaign-specific goals, not an unreviewed account-default bundle.
- Set language to English initially; language targeting is not a translation substitute. Add other languages only with approved pages, ads, and handling capacity.
- Use presence-based geography and exclude unserved regions. See `LOCATION_STRATEGY.md`.
- Keep all campaigns and ads **paused** in import files. “Eligible to launch” means structurally recommended, not authorized.

## Governance and access

Owner must confirm account ownership, least-privilege roles, billing, advertiser verification, business identity, legal entity, phone, domain, and change approvers. Never store credentials here. Maintain a change log containing date, operator, reason, before/after state, approval, and rollback plan.

## Import contract

The CSVs are a normalized production specification, **not a claimed one-click Google Ads Editor schema**. Google Ads Editor headers and accepted operations must be revalidated in the installed current version before import. Map columns in a duplicate/offline draft, inspect the preview, resolve errors, and keep everything paused. `Launch status` is the business gate; `Campaign status`/`Ad status` remain paused.

## Platform-validation note

Public-web verification was attempted on 2026-07-20 but the browsing service returned HTTP 401. Therefore platform limits, eligibility, asset availability, bidding availability, and Editor mapping in this package are explicitly **provisional current-best-practice assumptions** and appear in the launch validation checklist.
