# UTM Standard

Required for controlled non-Google-autotagged links: lowercase ASCII, hyphen-separated values, no personal data.

- `utm_source`: platform/publisher (`google`, `instagram`, `partner-name`).
- `utm_medium`: controlled channel (`cpc`, `paid-social`, `organic-social`, `email`, `referral`).
- `utm_campaign`: durable initiative (`search_refinishing_gno_2026q3`).
- `utm_content`: creative/placement variant.
- `utm_term`: keyword token only where appropriate.

Prefer Google Ads auto-tagging for GCLID/GBRAID/WBRAID and preserve it through redirects; UTMs are complementary. Store first-touch and latest-touch values separately with capture timestamps and original landing page. Never overwrite first touch. Lowercase/trim, allowlist lengths, reject scripts, and exclude UTMs from canonical URLs. A campaign naming register and owner approval are required before activation.
