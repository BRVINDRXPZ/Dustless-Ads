> **Internal plan only.** No publishing, pitching, outreach, account connection, schema deployment, or public action is authorized. Current platform/search requirements require dated official validation before implementation.
# Local Schema Plan

## Rule
Schema must describe visible, current, owner-verified content and use the most specific type that remains valid in the current Schema.org vocabulary and eligible under current Google Search documentation. Validate with official validators on staging and after any separately approved deployment.

| Type | Proposed use | Required truth/implementation gate |
|---|---|---|
| `Organization` | canonical identity/logo/social profiles | approved legal/public entity and owned URLs |
| `LocalBusiness` | local business details | approved NAP, eligible address policy, phone, URL, hours; omit unknowns |
| `FlooringContractor` or current subtype | only if current vocabulary supports it and business fits | validate current subtype; otherwise use accurate parent type, never invent |
| `Service` | visible service pages | real service, provider relationship, page content, qualified `areaServed` |
| `WebSite` | site identity | canonical owner-controlled domain |
| `BreadcrumbList` | visible hierarchy | URLs/names match navigation/canonicals |
| `FAQPage` | only where current search eligibility and visible page format qualify | no marketing Q&A disguise; current Google policy validation |
| `Review` / `AggregateRating` | generally hold; only first-party visible, policy-compliant, supported data if eligible | no copied GBP reviews, self-serving/unsupported ratings or fabricated totals |
| `ImageObject` | permissioned visible images | canonical asset URL, rights/caption/license as appropriate; privacy clear |
| `VideoObject` | visible original video | title/description/thumbnail/upload date/content URL as current rules require |
| `Article` | expert-reviewed guides | author/editor/date/headline/image visible and accurate |
| `Place` / `areaServed` | valid geographic relationships | no fake location, hidden home address or ranking-radius stuffing |

## Entity graph
Use stable HTTPS `@id` values: `/#organization`, `/#localbusiness`, `/#website`; connect `publisher`, `provider`, `isPartOf`, `mainEntityOfPage` accurately. Choose one canonical business entity rather than conflicting blocks. `sameAs` only for official profiles.

## QA
Compare rendered page/NAP; JSON parse; Schema.org validator; Google Rich Results Test where applicable; URL Inspection rendered HTML after authorization; no errors/warnings left unexplained; mobile canonical parity; review after template or policy changes. Schema does not guarantee a rich result and is never evidence of rankings.
