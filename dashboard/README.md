# Phase 9 Marketing Command Center

> **Planning specification — not connected or activated.** No live accounts, credentials, customer data, or invented business performance. Any prototype values are synthetic demonstration data.

## Purpose

Index and operating instructions for a decision system anchored to qualified leads, won revenue, and gross profit.

## Start here

1. Resolve `OWNER_DECISION_QUEUE.md`. 2. Implement Phase A in `IMPLEMENTATION_ROADMAP.md`. 3. Use `DATA_MODEL.md`, dictionaries, and CRM schemas as contracts. 4. Run the prototype and QA locally. 5. Never treat synthetic values as a baseline.

## Repository reuse

Extends `tracking/` source, UTM, conversion, offline-conversion and CRM field specifications; `b2b/` account/opportunity registers; Google Ads import templates; local SEO registers; social scorecard; landing-page prototype. These remain source-specific inputs; this folder is the governed reporting layer, not a duplicate live system.

## Prototype

From the repository root run `python3 -m http.server 8000`, open `http://localhost:8000/dashboard/prototype/`, and run `python3 dashboard/prototype/tests/check_dashboard.py`. No dependencies or network calls are used.

## Deliverable map

Architecture and governance: architecture, model, dictionaries, KPI hierarchy, wireframes, cadence, alerts, data quality, security, backup, QA. Economics: attribution and revenue/gross-profit reconciliation. Views: executive, response, Ads, SEO, social, B2B, operations, experiments. Execution: owner decisions and roadmap.
