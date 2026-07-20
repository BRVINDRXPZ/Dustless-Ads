# Budget Scenarios

**All dollar inputs are planning placeholders—not recommendations, current CPCs, forecasts, or guarantees.** Owner must supply budget and economics. Daily budget uses `monthly budget / 30.4`; Google may spend unevenly subject to current billing rules, which require verification.

## Economics model

Let `B` = monthly spend, `CPC` = average cost/click, `CLR` = click-to-lead rate, `QLR` = qualified-lead rate, `EBR` = estimate-booked rate from qualified leads, `CR` = close rate from booked estimates, `APV` = average project value, `GM` = gross-margin rate, and `MTCAC` = maximum tolerable customer acquisition cost.

- clicks = `B / CPC`
- raw leads = `clicks × CLR`
- qualified leads = `raw leads × QLR`
- booked estimates = `qualified leads × EBR`
- wins = `booked estimates × CR`
- modeled gross profit = `wins × APV × GM`
- CAC = `B / wins`; qualified CPL = `B / qualified leads`; raw CPL = `B / raw leads`
- economic ceiling per win = `min(MTCAC, APV × GM × owner-approved acquisition share)`
- break-even booked-estimate CPL = `economic ceiling per win × CR`
- break-even qualified CPL = `economic ceiling per win × EBR × CR`
- break-even raw CPL = `economic ceiling per win × QLR × EBR × CR`

Never divide by zero; present ranges and sensitivity tables only after owner inputs and real Keyword Planner/account data are available.

## Scenario A — Controlled Entry

| Field | Plan |
|---|---|
| Monthly / daily | `$TBD-A` / `$TBD-A ÷ 30.4` |
| Allocation | Brand 5%; Refinishing 40%; Dust-Controlled 25%; Installation 15%; Repair 15%; all others 0% |
| Learning limit | May not generate enough primary outcomes for automated bidding or granular ad conclusions |
| Operations | One accountable responder; daily search-term review; lead disposition within one business day |
| Response | Phone only during answered hours; form acknowledgement and owner-approved response SLA |
| Scale trigger | Tracking reconciles; qualified CPL below ceiling across conversion lag; capacity available |
| Cutback | Tracking failure, material wrong-service/geo spend, response backlog, or qualified economics breach |

## Scenario B — Aggressive Growth

| Field | Plan |
|---|---|
| Monthly / daily | `$TBD-B` / `$TBD-B ÷ 30.4` |
| Allocation | Brand 4%; Refinishing 28%; Dust-Controlled 17%; Installation 20%; Repair 15%; Historic 6%; Northshore 10% |
| Learning limit | B2B/commercial intent may remain sparse; attribution lag can obscure short-term results |
| Operations | Coverage across business hours, scheduled estimate capacity, weekly CRM reconciliation, creative/page owner |
| Response | Route residential vs B2B; same-business-day disposition; missed-call recovery workflow |
| Scale trigger | Cohort-level qualified CAC and gross profit acceptable; impression share lost to budget is economically useful |
| Cutback | Marginal spend worsens qualified mix; backlog; geographic leakage; offline imports incomplete |

Historic and Northshore allocations remain **gated**; if gates are not met, reallocate only to proven launch campaigns—not automatically.

## Scenario C — Market Domination

| Field | Plan |
|---|---|
| Monthly / daily | `$TBD-C` / `$TBD-C ÷ 30.4` |
| Allocation | Brand 3%; Refinishing 20%; Dust-Controlled 12%; Installation 17%; Repair 13%; Historic 8%; Commercial 10%; Contractor 7%; Northshore 10% |
| Learning limit | High spend cannot manufacture demand; B2B lag and sparse value data require long evaluation windows |
| Operations | Dedicated lead coverage, capacity forecasting, CRM enforcement, offline value imports, proof production, landing-page testing |
| Response | Defined SLA by segment, after-hours policy, call QA, weekly sales/marketing review |
| Scale trigger | Incremental qualified gross profit supports marginal CAC; capacity and impression-share opportunity confirmed |
| Cutback | Contribution margin or capacity guardrail fails; channel incrementality weak; lead-quality deterioration |

Remarketing, video, and Performance Max are **not funded automatically**; add only after their readiness gates and separate approval.

## Missing owner inputs

Monthly cash ceiling, service-level budget floors, CPC planning ranges from current Keyword Planner, service-specific CLR/QLR/EBR/CR, APV, GM, MTCAC, cancellation rate, conversion lag, minimum job, capacity, response hours, seasonality, Northshore travel economics, and B2B payment/close cycles.
