# CRM Minimum Viable Setup

**Status:** Internal, inactive draft. No launch, publication, outreach, account connection, or spend is authorized. Owner approval required.

## Immediate system
Use one access-restricted, backed-up tabular lead register with one data steward and manual entry. This is deliberately not advanced automation. Select the actual tool only after privacy, ownership, export, mobile and recovery checks. One row per lead; stable Lead ID; activities may be a second tab.

| Required field | Rule |
|---|---|
| Lead ID; Date | Unique immutable ID; received timestamp |
| Name; Phone; Email | Minimum necessary; restricted access |
| Source; Campaign | Controlled values; Unknown stays visible |
| Service; Geography; Segment | Approved lists; segment = residential/contractor/commercial |
| Qualified; Disqualification reason | Required decision and controlled reason |
| Estimate scheduled/completed; Proposal sent | Date/status, not free-form ambiguity |
| Won/lost; Revenue; Gross profit | Approved definitions; blank is not zero |
| Last contact; Next action; Owner | Updated after every interaction |

**Discipline:** enter by end of response shift; search phone/email before create; never overwrite source; every open record has owner/next action/date; reconcile calls/forms daily; close stale items only under approved rule. Weekly owner review: totals, missing fields, duplicates, idle leads, estimates, wins/losses, source coverage, revenue/GP exceptions.

**Upgrade path:** after 4 consecutive weekly QA reviews demonstrate consistent use, evaluate a simple CRM using `crm/CRM_SELECTION_SCORECARD.csv`; require full CSV export, field/stage mapping, ID preservation, permissions, backup, sandbox import, control totals and rollback before migration.
