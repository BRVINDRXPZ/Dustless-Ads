# Campaign Architecture

**Status:** launch-ready offline specification, not launch authorization. All campaigns remain paused until owner, evidence, landing-page, measurement, operations, current-platform, and budget gates pass. Phase 2 competitor observations are not used as verified facts.

## System rules

Launch exact and phrase match only. A later broad-match test requires qualified offline signals, Smart Bidding, isolated budget, daily query review, and a rollback. Account negatives cover unmistakably irrelevant intent; campaign negatives prevent audience/service/geo leakage. Offers are value-based assessment/planning concepts from Phase 3 and remain owner-gated. Placeholder URLs must be replaced and QA’d.

## Campaign specifications

### 1. Search | Core | Brand | All

- **Objective/audience/service/geography:** capture navigational demand for the business; all valid audiences; brand navigation; all owner-approved core territory.
- **Budget priority/conversion/bidding:** protective low fixed share; qualified call/form or audience-specific inquiry; Stage 1 Maximize Clicks with cap or Manual CPC if available.
- **Ad groups:** NOLA Dustless; NOLA Dustless Hardwood Floors. Misspellings/owner-name variants are later tests only after actual query evidence and name approval.
- **Keywords/negatives:** exact + phrase brand strings; negatives for jobs, DIY, tools, products and wrong businesses, applied cautiously.
- **Page/offer/qualification:** verified home/contact page; request a floor assessment; valid service, geography, scope, and contact intent.
- **Risks:** organic cannibalization, competitor/customer-support queries, trademark/name ambiguity.
- **Scale/kill:** scale only for lost eligible brand coverage and qualified incremental demand; reduce if no incrementality or query ambiguity dominates.

### 2. Search | Core | Refinishing | Residential

- **Objective/audience/service/geography:** capture high-intent homeowner refinishing/restoration demand in approved New Orleans/Metairie core.
- **Budget priority/conversion/bidding:** highest; qualified call/form and estimate scheduled; Stage 1 controlled clicks then Maximize Conversions on qualified signals.
- **Ad groups:** Hardwood Floor Refinishing; Wood Floor Refinishing; Sanding & Refinishing; Refinish Near Me; Restore Hardwood Floors.
- **Keywords/negatives:** tightly matched exact/phrase; cross-negative repair-only, install-only, and B2B when routing is clear; shared irrelevant list.
- **Page/offer/qualification:** `/hardwood-floor-refinishing/` placeholder; professional floor assessment; hardwood/likely wood, approved area, viable project size/timing/access.
- **Risks:** DIY/product traffic, small spot jobs, unknown material, dust claims, price-only leads.
- **Scale/kill:** scale on qualified CPL/CAC, estimate capacity, and profitable wins; kill/rebuild if wrong-material/scope dominates or economics exceed ceiling after fixes.

### 3. Search | Core | Dust Controlled Sanding | Residential

- **Objective/audience/service/geography:** capture homeowners explicitly concerned with sanding dust/disruption; approved core.
- **Budget priority/conversion/bidding:** high but capped against Refinishing overlap; qualified call/form; Stage 1 controlled clicks.
- **Ad groups:** Dustless Floor Sanding; Dust-Controlled Sanding; Cleaner Refinishing; Sanding With Containment.
- **Keywords/negatives:** exact/phrase; campaign negatives for rentals/machines/bags/vacuums; route generic sanding carefully.
- **Page/offer/qualification:** `/dust-controlled-floor-sanding/` placeholder; floor/process assessment; viable hardwood refinishing scope and owner-approved expectations.
- **Risks:** company name vs process confusion, “dust-free” expectation, equipment shoppers, overlap with Refinishing.
- **Scale/kill:** scale when incremental qualified demand and approved dust language are proven; hold immediately if process wording/evidence is not approved.

### 4. Search | Core | Installation | Residential

- **Objective/audience/service/geography:** acquire homeowners seeking approved hardwood installation methods in core territory.
- **Budget priority/conversion/bidding:** high; qualified call/form and installation review scheduled; Stage 1 then qualified-conversion bidding.
- **Ad groups:** Hardwood Installation; Solid Hardwood Installation; Nail-Down Installation; Hardwood Installer; Match Existing Hardwood.
- **Keywords/negatives:** exact/phrase; exclude material-only shopping, wholesale, floating/LVP/laminate, DIY; do not block legitimate material-plus-install intent blindly.
- **Page/offer/qualification:** `/hardwood-floor-installation/` placeholder; whole-home flooring plan; method/material/subfloor/timeline/size/serviceability review.
- **Risks:** retail-only shoppers, unsupported methods, small rooms, substrate surprises, matching guarantees.
- **Scale/kill:** scale on qualified project value and installed capacity; kill ad groups for persistently unoffered methods or poor economics.

### 5. Search | Core | Repair Restoration | Residential

- **Objective/audience/service/geography:** capture repair, damage, board replacement, and save-versus-replace decisions in core territory.
- **Budget priority/conversion/bidding:** medium-high with strict qualification; qualified form/call and assessment scheduled; Stage 1.
- **Ad groups:** Hardwood Floor Repair; Board Replacement; Water Damage; Pet Damage; Original Floor Restoration; Repair Old Wood Floors.
- **Keywords/negatives:** exact/phrase; exclude furniture repair, kits, cleaners, insurance/legal-only intent; preserve legitimate repair queries.
- **Page/offer/qualification:** `/hardwood-floor-repair-restoration/` placeholder; photo-based initial review or assessment, both pending workflow approval; material, extent, source condition, minimum, area.
- **Risks:** tiny uneconomic fixes, emergency remediation/mold, impossible matches, diagnosis from photos.
- **Scale/kill:** scale by qualified scope and profitable downstream restoration; kill/reroute subthemes that consistently seek services not offered.

### 6. Search | Core | Historic Heart Pine | Residential

- **Objective/audience/service/geography:** reach owners seeking careful historic/heart-pine/antique-pine work; core historic-property demand.
- **Budget priority/conversion/bidding:** strategic hold; feasibility-assessment request; launch only after case/species/process proof and page readiness.
- **Ad groups:** Historic Floor Restoration; Heart-Pine Restoration; Antique Pine Repair; Old New Orleans Floors; Historic-Home Hardwood.
- **Keywords/negatives:** exact/phrase only; exclude reclaimed-lumber/material shopping and furniture; avoid “specialist/leader” terms in copy unless approved.
- **Page/offer/qualification:** `/historic-hardwood-restoration/` placeholder; historic-floor feasibility assessment; evidence access, viable scope, expectations, property constraints.
- **Risks:** unsupported expertise/species, irreversible-work expectations, perfect-match demands, low volume.
- **Scale/kill:** scale after permissioned cases and qualified values; do not launch without evidence or if service delivery cannot support careful assessment.

### 7. Search | Core | Commercial | B2B

- **Objective/audience/service/geography:** generate valid commercial/hospitality/institutional opportunities; approved metro.
- **Budget priority/conversion/bidding:** strategic hold/controlled separate budget; commercial inquiry, walkthrough, proposal; data collection then offline optimization.
- **Ad groups:** Commercial Hardwood Contractor; Hotel Refinishing; Restaurant Flooring; Church Restoration; Commercial Installation; Property Management.
- **Keywords/negatives:** exact/phrase; exclude residential/DIY/product where unambiguous; add bid/job confusion negatives carefully.
- **Page/offer/qualification:** `/commercial-hardwood-flooring/` placeholder; commercial site walkthrough/bid intake; entity, authority, scope, schedule, procurement, capacity, terms.
- **Risks:** proof/capacity/vendor-document gaps, long cycle, residential crossover, “commercial” product shopping.
- **Scale/kill:** scale on qualified pipeline and gross profit through full lag; hold if bid/no-bid process, documents, references, or capacity are absent.

### 8. Search | Core | Contractor Builder | B2B

- **Objective/audience/service/geography:** attract GCs/builders seeking a hardwood subcontractor; approved metro.
- **Budget priority/conversion/bidding:** strategic hold/low controlled budget; contractor inquiry, plan package, proposal; Stage 1 then offline outcomes.
- **Ad groups:** Hardwood Subcontractor; Flooring Subcontractor New Orleans; Builder Hardwood Installer; Contractor Flooring Partner; Commercial Flooring Bid; Hardwood Plan Review.
- **Keywords/negatives:** exact/phrase; strong jobs/careers/training negatives; distinguish subcontract opportunity from consumer work and material suppliers.
- **Page/offer/qualification:** `/contractor-partnerships/` placeholder; contractor plan review; complete scope, authority, schedule, terms, geography, documents, capacity fit.
- **Risks:** employment searches, bid portals, weak operational proof, adverse terms, sparse demand.
- **Scale/kill:** scale on valid bid packages/wins/repeat value; do not launch before vendor readiness and intake workflow.

### 9. Search | Northshore | Hardwood Services | Residential

- **Objective/audience/service/geography:** validate profitable service demand in owner-approved Mandeville/Covington/Madisonville/Slidell scope.
- **Budget priority/conversion/bidding:** hold, then separate capped budget; qualified call/form; Stage 1.
- **Ad groups:** Refinishing Mandeville; Refinishing Covington; Installation Northshore; Repair Slidell; Hardwood Services Northshore.
- **Keywords/negatives:** geo-explicit exact/phrase; exclude metro campaigns reciprocally and unapproved towns.
- **Page/offer/qualification:** `/northshore-hardwood-services/` placeholder; photo-based initial review; town, travel minimum, scope, timing.
- **Risks:** coverage claims, thin volume, travel cost, generic page, lack of local proof.
- **Scale/kill:** scale on travel-adjusted gross profit and operational cadence; do not launch until towns/minimums/page are approved.

### Stairs evaluation

Do **not** include a separate stairs campaign at launch. Stair/tread refinishing is preliminary, owner economics and minimums are unknown, intent can mix refinishing with parts/materials/DIY, and a dedicated page/measurement path is absent. Preserve exact/phrase stair service keywords as a later-test set only after scope, search planning data, margins, negatives, page, and capacity are approved. It may become an ad group before a campaign if volume cannot support independent control.

## Ruthless priority scores

Scores are internal strategic judgments, not market facts. `Claim risk` 10 = highest risk; other columns 10 = strongest. Competitive opportunity is provisional because live competitor evidence is unavailable.

| Campaign | Revenue | Intent | Lead quality | Competitive opportunity | Operational fit | Evidence | Page ready | Measurement ready | Claim risk | Launch priority |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Brand Defense | 6 | 10 | 8 | 5 | 8 | 8 | 5 | 4 | 2 | 9 |
| Refinishing | 9 | 9 | 8 | 7 | 8 | 6 | 3 | 3 | 4 | 10 |
| Dust-Controlled Sanding | 8 | 9 | 8 | 7 | 7 | 3 | 3 | 3 | 7 | 8 |
| Installation | 9 | 9 | 8 | 6 | 7 | 4 | 3 | 3 | 4 | 8 |
| Repair/Restoration | 7 | 8 | 6 | 7 | 5 | 4 | 3 | 3 | 5 | 7 |
| Historic/Heart Pine | 8 | 8 | 8 | 8 | 4 | 2 | 2 | 3 | 8 | 4 |
| Commercial | 9 | 7 | 8 | 7 | 3 | 2 | 2 | 2 | 7 | 4 |
| Contractor/Builder | 9 | 7 | 8 | 7 | 3 | 2 | 2 | 2 | 6 | 4 |
| Northshore | 7 | 8 | 6 | 6 | 3 | 2 | 2 | 2 | 6 | 3 |
| Stairs | 5 | 6 | 4 | 5 | 3 | 2 | 1 | 2 | 4 | 2 |

## Launch First

After all checklist gates and explicit approval, launch exactly:

1. **Brand Defense:** NOLA Dustless; NOLA Dustless Hardwood Floors.
2. **Hardwood Floor Refinishing:** Hardwood Floor Refinishing; Wood Floor Refinishing; Sanding & Refinishing; Refinish Near Me; Restore Hardwood Floors.
3. **Dust-Controlled Floor Sanding:** Dustless Floor Sanding; Dust-Controlled Sanding; Cleaner Refinishing; Sanding With Containment—**only after dust-process wording is approved**.
4. **Hardwood Floor Installation:** Hardwood Installation; Solid Hardwood Installation; Nail-Down Installation; Hardwood Installer; Match Existing Hardwood—only for confirmed methods.
5. **Repair and Restoration:** Hardwood Floor Repair; Board Replacement; Original Floor Restoration; Repair Old Wood Floors. Hold water/pet damage until service/remediation boundaries and economics are approved.

## Hold Until Ready

- Historic and Heart-Pine Restoration: all ad groups pending substantiated cases, species/process proof, and page.
- Commercial Hardwood Flooring: all ad groups pending capabilities, references, vendor readiness, capacity, landing page, and offline stages.
- Contractor and Builder Partnerships: all ad groups pending bid/no-bid, documents, intake, response, proof, and page.
- Northshore Hardwood Services: all ad groups pending towns, travel minimums, cadence, page, and measurement.
- Water Damage and Pet Damage ad groups; brand misspellings/owner-name variants; Search Partners; broad match; lead-form assets; image assets; Performance Max.

## Do Not Launch

- Stairs as a separate campaign now; generic “flooring” or home-improvement campaigns; competitor conquesting without legal/economic review; Display expansion; primary-launch Performance Max; unapproved Mississippi targeting; DIY/product/material/rental campaigns; discount/free-product campaigns; “dust-free,” “best,” “#1,” “authority,” guaranteed match/save, unverified credential, project, review, speed, warranty, or leadership claims.
