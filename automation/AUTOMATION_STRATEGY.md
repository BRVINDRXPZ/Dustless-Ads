# Automation Strategy

> **Planning specification — inactive.** No live accounts, credentials, communications, or real customer data.

## Purpose

Automate controls and reminders before communications.

## Safe after setup and QA

Lead acknowledgement **only after owner approves content/channel/consent despite category label**; internal task creation; source/UTM capture; reminders; report generation; duplicate flags; stage-required-field checks; review eligibility flags; stale-opportunity and data-quality alerts.

## Owner approval before activation

Customer SMS/email; estimate follow-up; review requests; contractor/commercial outreach; social publishing; budget changes; bid follow-up; reactivation.

## Never fully automate

Pricing; final estimates; scope promises; technical diagnosis; warranty commitments; contract acceptance; complaints/legal disputes; negative-review disputes; high-value negotiation; crew promises; project acceptance; public claims; crisis communications.

## Design

Every workflow has immutable ID/version, trigger, conditions, idempotency key, approval, dry run, audit event, rate limit, fallback, owner and kill switch. Default status is inactive.
