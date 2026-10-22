---
type: twir-item
issue: 294
item: 5
item_type: item
date: 2026-08-19
source: https://github.com/react/react/pull/37290
tags:
  - "PR"
status: auto
quality: keep
---

[[2026-08-19-TWIR-294|Index]]

# Item 5: React PR – Enable Parallel Transitions Flag Everywhere

Source: [https://github.com/react/react/pull/37290](https://github.com/react/react/pull/37290)

Summary:
A React pull request flips the enableParallelTransitions feature flag on by default in the open-source and canary builds, as well as all hardcoded forks (including React Native). The flag has been in production at Meta, and the team plans to deploy it to Vercel apps for broader testing ahead of React 19.3. The change leaves the flag in the repo for now but makes parallel transitions the default behavior.

Key takeaways:
- enableParallelTransitions is now enabled by default across all React forks.
- The feature has been tested in production at Meta, indicating stability.
- The team aims to include this in React 19.3 and will monitor for regressions.
- No significant production bundle size changes reported.

Recommendation:
Read fully (read fully if you need migration or feature flag details)

Why it matters:
read fully if you need migration or feature flag details

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
