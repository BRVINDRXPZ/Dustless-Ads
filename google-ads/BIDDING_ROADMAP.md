# Bidding Roadmap

## Staged path

| Stage | Entry condition | Recommended approach | Exit condition |
|---|---|---|---|
| 1. Launch/data validation | Primary tracking QA passed; little reliable data | Exact/phrase; conservative Maximize Clicks with CPC ceiling **or** Manual CPC only if still available and operationally manageable | Search terms clean; primary conversions deduplicated; lead quality captured |
| 2. Early conversion | Enough recent, correctly attributed primary conversions for the platform to learn; no fixed universal count asserted | Controlled Maximize Conversions experiment against prior method | Stable qualified-lead mix and sufficient data across conversion lag |
| 3. Qualified-lead optimization | Qualified outcomes imported reliably | Maximize Conversions, then tCPA only when observed CPA distribution supports a non-choking target | Consistent qualified CPL and estimate progression |
| 4. Offline-value optimization | Won revenue/gross profit imported with stable values and identifiers | Maximize Conversion Value; consider tROAS only after value completeness and lag are understood | Value coverage, reconciliation, and sufficient volume pass thresholds |
| 5. Scale | Profitable cohorts and capacity confirmed | Increase budgets gradually; broaden terms/geos one isolated test at a time | Stop scaling when marginal qualified CAC, capacity, or quality breaches guardrails |

## Tool rules

- **Maximize Clicks:** useful only to obtain controlled query data; cap bids where available and never treat clicks as success.
- **Manual CPC:** use only if present in the current account/editor and the operator can manage it; availability is provisional and must be checked.
- **Maximize Conversions:** do not feed form starts, page engagement, or raw click-to-call as primary goals.
- **tCPA:** derive from actual qualified economics; do not set from platform suggestions alone or tighten abruptly.
- **Maximize Conversion Value / tROAS:** require trustworthy offline values, adjustment/cancellation handling, value lag, and gross-profit policy.
- **Broad match:** later-stage, isolated campaign/ad-group test only with Smart Bidding, robust negatives, sufficient qualified conversions, and daily query review.
- **Smart Bidding:** valuable only when conversion definitions and data are valuable. Platform recommendations are inputs, not authorization.

## Change discipline

Avoid simultaneous budget, bid, match-type, ad, geo, and conversion-goal changes. Record the hypothesis and allow for conversion lag. Emergency pauses are allowed for tracking failure, policy risk, wrong geography, runaway spend, or capacity shutdown.
