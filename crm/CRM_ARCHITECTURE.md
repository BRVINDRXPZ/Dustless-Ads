# CRM Architecture

> **Planning specification — inactive.** No live accounts, credentials, communications, or real customer data.

## Purpose

One relationship model from contact through project economics.

## Model

Contacts belong to accounts and may create leads. Qualified leads create opportunities. Won opportunities create projects. Activities attach to contact/account/lead/opportunity. Attribution touches retain first, primary, last and assists.

## Supported types

Contacts: homeowner, contractor, designer, architect, realtor, property_manager, commercial_contact, supplier, referral_partner, past_customer. Accounts: household, contractor_company, builder, design_firm, architecture_firm, property_management_company, hotel_group, restaurant_group, church_or_institution, commercial_company, supplier. Leads: residential, contractor, commercial, referral, past_customer, partner. Opportunities: residential_estimate, contractor_project, commercial_bid, repeat_account_project, referral_opportunity. Projects: won, active, completed, lost, cancelled.

## Source of truth

CRM owns lifecycle; finance owns invoices/payments/revenue/cost/GP; project operations owns delivery. IDs, not names/emails, join systems. Unknown is valid and visible.

## Minimum viable setup

Controlled tables for contacts/accounts/leads/opportunities/projects/activities/attribution. Required-field and stage-transition checks precede dashboards or automation.
