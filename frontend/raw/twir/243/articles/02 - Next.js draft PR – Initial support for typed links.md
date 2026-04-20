---
type: twir-item
issue: 243
item: 2
item_type: item
date: 2025-07-16
source: https://github.com/vercel/next.js/pull/81528
tags:
  - "Nextjs"
  - "PR"
status: auto
quality: keep
---

[[2025-07-16-TWIR-243|Index]]

# Item 2: Next.js draft PR – Initial support for typed links

Source: [https://github.com/vercel/next.js/pull/81528](https://github.com/vercel/next.js/pull/81528)

Summary:
This draft PR introduces a new implementation of typed links for Next.js, replacing the previous experimental.typedRoutes. The new approach is compatible with both Turbopack and Webpack, focusing on bringing typed links to Turbopack users quickly. Some planned Link component prop changes (path, params, searchParams) were removed from this PR and will be addressed separately. The PR is part of a stack of related changes to improve type safety and developer experience around routing.

Key takeaways:
- Typed links are being re-implemented for compatibility with both Turbopack and Webpack.
- Immediate focus is on Turbopack support; further Link API enhancements are deferred.
- The PR is part of a broader effort to improve type safety in routing.
- Tests have passed, and the work is ongoing with related dependent PRs.

Recommendation:
Summary sufficient (read the PR if you need typed links or are following Next.js type safety improvements closely)

Why it matters:
read the PR if you need typed links or are following Next.js type safety improvements closely

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
