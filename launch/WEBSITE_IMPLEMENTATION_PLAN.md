# Website Implementation Plan

**Status:** Internal implementation draft. Owner completion, validated access, evidence, testing, and written approval are required. This document authorizes no live change, connection, publication, outreach, or spend.

## Recommendation and assumptions
**Recommended:** integrate only the approved Refinishing, Dust-Controlled Sanding, Installation, Estimate, Thank-you and Privacy/Consent pages into the current site **if** the owner confirms the stack, staging, rollback and implementer. Rebuild only these selected pages. If the current stack cannot support secure forms/tracking/performance on schedule, use a same-brand, owner-controlled campaign host as a fallback. The static prototype is preview/reference-only and must never receive production traffic: it has no backend or production identifiers. The live stack, host, canonical behavior and access remain unknown.

| Order | Item | Minimum production work | Acceptance | Risk/rollback |
|---:|---|---|---|---|
| 1 | Stack/staging | Inventory CMS, host, templates, DNS/canonical, backups; clone to staging | Owner/implementer can deploy and restore | Stop; restore backup |
| 2 | Shared shell | Approved logo/NAP, call CTA, navigation, footer, consent link | Mobile keyboard/screen-reader checks | Revert template |
| 3 | Refinishing page | Migrate only approved factual copy and permissioned proof | Message/page/CTA QA | Unpublish route |
| 4 | Sanding page | Narrow verified process wording; never “dust-free” | Claim evidence linked | Hold page/campaign |
| 5 | Installation page | Approved eligible methods/geography/proof | Scope verified | Hold page/campaign |
| 6 | Estimate page/form | Minimum fields, server validation, spam control, secure upload only if required | Test submission/routing/CRM | Disable form; retain phone only if routing works |
| 7 | Thank-you/error | No fabricated promise; next-step and fallback | Direct access and event test | Revert |
| 8 | Privacy/consent | Reviewed notice and consent behavior | Legal/technical signoff | Disable nonessential tags/form |
| 9 | Metadata | Unique title/description/canonical/index rules | Crawl/render check | Restore metadata |
| 10 | QA | Mobile, accessibility, speed, browser, analytics and failure tests | All P0/P1 defects closed | NO-GO |

Separate-host risks: fragmented analytics, DNS/cookie/consent complexity, brand distrust, maintenance duplication and SEO/canonical mistakes. Current-site risks: unknown template constraints and deployment ownership. Decide after a read-only technical audit, not preference.
