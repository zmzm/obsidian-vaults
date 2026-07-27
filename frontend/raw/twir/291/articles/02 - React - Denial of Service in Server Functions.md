---
type: twir-item
issue: 291
item: 2
item_type: item
date: 2026-07-22
source: https://github.com/react/react/security/advisories/GHSA-wx67-qw84-cm4g
tags:
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-07-22-TWIR-291|Index]]

# Item 2: React - Denial of Service in Server Functions

Source: [https://github.com/react/react/security/advisories/GHSA-wx67-qw84-cm4g](https://github.com/react/react/security/advisories/GHSA-wx67-qw84-cm4g)

Summary:
A denial of service (DoS) vulnerability was identified in React server function packages, where specially crafted HTTP requests could exhaust server resources. The issue affects specific versions of react-server-dom-webpack, react-server-dom-parcel, and react-server-dom-turbopack, but only if your app uses React Server Components. The vulnerability has been patched in newer versions, and immediate upgrades are recommended.

Key takeaways:
- Affected versions: 19.0.0–19.0.7, 19.1.0–19.1.8, 19.2.0–19.2.7; fixed in 19.0.8, 19.1.9, 19.2.8.
- Only apps using React Server Components are impacted; traditional client-only apps are unaffected.
- Upgrade to the patched versions immediately to mitigate risk.

Recommendation:
Summary sufficient (read advisory if you use React Server Components)

Why it matters:
read advisory if you use React Server Components

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
