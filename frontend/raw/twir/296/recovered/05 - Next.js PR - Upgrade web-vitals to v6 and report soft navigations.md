---
type: "twir-recovery"
issue: 296
item: 5
source: "https://github.com/vercel/next.js/pull/97232"
final_url: "https://github.com/vercel/next.js/pull/97232"
retrieved: "2026-10-22T11:30:12+00:00"
original_note: "frontend/raw/twir/296/articles/05 - Next.js PR - Upgrade web-vitals to v6 and report soft navigations.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/05 - Next.js PR - Upgrade web-vitals to v6 and report soft navigations|Next.js PR - Upgrade web-vitals to v6 and report soft navigations]]

# Upgrade web-vitals to v6 and report soft navigations by timneutkens · Pull Request #97232 · vercel/next.js · GitHub

```
## Summary

Upgrades the vendored `web-vitals` dependency to v6.0.1 and enables
soft-navigation reporting for CLS, INP, and LCP. This lets
`useReportWebVitals` report metrics against the navigation where they
occurred, including `navigationURL` for route attribution.

The upgrade also removes the obsolete FID integration and compatibility
patch, regenerates the standard and attribution bundles, and updates the
public metric types and documentation to match the current upstream API.

Related to vercel#97161.

## Verification

- Added production-mode coverage for initial and soft-navigation Web
Vitals reporting with both Turbopack and Webpack.

<!-- NEXT_JS_LLM -->
```
