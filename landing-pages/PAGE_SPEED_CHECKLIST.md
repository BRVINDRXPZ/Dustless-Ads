# Page Speed Checklist

- [ ] Measure mobile Lighthouse and real-device performance on production-like hosting.
- [ ] Set budgets: initial HTML ≤50 KB, CSS ≤50 KB, JS ≤40 KB compressed; exceptions documented.
- [ ] Target LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 at the 75th percentile once field data exists.
- [ ] Use correctly sized AVIF/WebP with width/height; preload only the true hero.
- [ ] Lazy-load below-fold media; never lazy-load the LCP image.
- [ ] Self-host/subset fonts or retain system stack; avoid render-blocking third parties.
- [ ] Minify/cache versioned static assets; Brotli/Gzip; sensible immutable caching.
- [ ] Defer consented measurement; limit tags and audit tag cost.
- [ ] Keep form validation small; no framework required for current prototype.
- [ ] Test cold/warm cache, slow 4G, error pages, and disabled JavaScript.
