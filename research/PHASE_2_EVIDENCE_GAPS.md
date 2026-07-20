# Phase 2 Evidence Gaps

**Audit date:** 2026-07-20  
**Status:** Phase 2B evidence-readiness audit. No live public evidence was supplied or collected in this task.

## Audit conclusion

Phase 2 produced a useful query universe, 35-company candidate set, capture method, language hypotheses, and strategic hypotheses. It did **not** verify current competitor operation, ownership of candidate URLs, rankings, Maps presence, reviews, ads, social activity, services, service areas, offers, or positioning. All competitor-specific conclusions remain provisional until linked to dated evidence in `EVIDENCE_REGISTER.csv`.

## File-by-file audit

| Phase 2 file | Unsupported or evidence-dependent content found | Required treatment / evidence |
|---|---|---|
| `audit/CURRENT_STATE_AUDIT.md` | Numeric readiness scores are judgments, not measurements; NOLA capabilities and platform performance remain unknown. | Label scores as provisional internal triage; obtain owner records and account baselines. |
| `research/COMPETITOR_MATRIX.csv` | Candidate identity, URL ownership, location, service area, services, positioning, strengths, weaknesses, and opportunities lack dated public captures. Review, Maps, organic, paid, and social fields were already unknown. | Every row remains a provisional lead; validate via queue and link Evidence IDs before analysis. |
| `research/SEARCH_INTENT_MAP.csv` | Demand, volume, priority scores, current rankings, and destination opportunity are hypotheses. | Use Search Console/keyword data plus dated SERPs; priority is planning judgment only. |
| `research/SERP_ANALYSIS.md` | “Strongest” and “growth blocker” lists are provisional archetype rankings; retailer, directory, Northshore, B2B, and service-by-place conclusions depend on missing SERP/Maps evidence. | Capture 25 queries across specified locations/devices twice; then re-rank using an explicit rubric. |
| `research/SOCIAL_GAP_ANALYSIS.md` | No competitor platform presence, posting cadence, follower counts, engagement, content themes, or offers were observed. The proposed gap and cadence are inferences. | Audit a defined recent-post sample per platform; confirm NOLA capacity separately. |
| `research/MARKET_WHITESPACE.md` | Five “weak areas,” all positioning gaps, the opportunity scores/rank, and competitor weakness ratings are hypotheses—not market findings. | Validate websites, SERPs, Maps, social, reviews, and buyer evidence; preserve as hypotheses meanwhile. |
| `research/CUSTOMER_LANGUAGE_BANK.md` | All phrases, concerns, objections, and segment language are constructed hypotheses, not quotes or proven demand. | Validate with permissioned reviews, de-identified call themes, Search Console, and owner interviews. |
| `research/COMPETITIVE_CLAIMS_TO_VERIFY.md` | Claim examples are classes to watch for; no competitor-specific claim was observed. | Record exact URL/date/context and distinguish company-stated claims from independent substantiation. |
| `strategy/INITIAL_DOMINATION_THESIS.md` | Proposed category, promise, audience plays, channel sequence, “required conclusions,” and competitor lists depend partly on missing live evidence and owner proof. | Treat as provisional strategy; do not finalize or publish. Use interim hypotheses file for gated decisions. |

## Gap categories

| Gap | Current status | Evidence needed | Decision blocked |
|---|---|---|---|
| Competitor ranking | Provisional | Dated organic and Maps observations by query/location/device, repeated | Final threat ranking and comparison |
| Reviews | Unverified | Platform URLs, rating/count/date screenshots, recent-review sample | Reputation gap and review priority claims |
| Organic search | Unverified | Top 10 captures for mapped queries | Search opportunity and competitor visibility |
| Google Maps | Unverified | Local pack/Maps positions and profiles by location | Local visibility conclusions |
| Paid search | Unverified; absence not established | Labeled sponsored-result observations | Advertiser presence and landing-page analysis |
| Social | Unverified | Profile identity, latest activity, sample/cadence, visible engagement | Social gap and competitor activity claims |
| Service area | Unverified | Current first-party service-area text plus Maps/contact details | Geographic comparison and Northshore strategy |
| Services/offers | Unverified | Relevant current pages and dated screenshots | Offer and specialization comparisons |
| Historic positioning | Provisional inference | Search/site/social/proof sample plus owner capability evidence | Historic positioning |
| Contractor positioning | Provisional inference | B2B query/site/intake/proof sample plus owner readiness | Contractor positioning |
| Commercial positioning | Provisional inference | Commercial query/site/case evidence plus owner readiness | Commercial positioning |

## Validation rules

1. `Verified` requires a dated source URL/context and matching screenshot or durable export; repository context alone should say `Verified in repository only`.
2. A company claim is verified **as observed wording**, not independently substantiated, unless independent evidence is recorded.
3. A single SERP, Maps, or ad capture proves only that observation. Recurrence needs the planned repeat.
4. `Not found`, `not observed`, and blank never mean absent.
5. Contradictory evidence stays in the register with notes; do not select the favorable version silently.
6. No competitor comparison, final positioning, ad, landing page, spend, outreach, publishing, or live-system change is authorized.

## Exit criteria for Phase 2B validation

- All queue Priority 1 companies have current identity/site, SERP, Maps, reviews, social, and positioning evidence or an explicit unresolved reason.
- All 25 mapped queries have desktop and mobile observations in New Orleans, Metairie, and one owner-approved Northshore location, repeated after seven days.
- Every claim used in a competitor rank or whitespace conclusion links to Evidence IDs.
- Review/ad/social claims state platform, date, and context.
- Owner evidence resolves NOLA service area and historic, commercial, contractor, credential, and proof boundaries.
- Interim hypotheses are confirmed, revised, or rejected; final positioning still requires owner approval.
