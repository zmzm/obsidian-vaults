---
type: twir-item
issue: 230
item: 4
item_type: item
date: 2025-04-16
source: https://github.com/facebook/react/pull/32819
tags:
  - "PR"
status: auto
quality: keep
---

[[2025-04-16-TWIR-230|Index]]

# Item 4: React Core PR - Add Suspensey Images behind a flag

Source: [https://github.com/facebook/react/pull/32819](https://github.com/facebook/react/pull/32819)

Summary:
This PR adds a feature to React that allows images to suspend rendering until they are decoded, up to a 500ms timeout, similar to how Suspense works for fonts. The feature only applies during transitions, retries, and gesture transitions (behind a flag), not for synchronous updates. There are opt-outs for images with `loading="lazy"` or a custom `onLoad` handler, and future plans for opt-in longer blocking and integration with View Transitions.

Key takeaways:
- Images can now suspend rendering in transitions, improving perceived loading and preventing layout shifts.
- Default timeout is 500ms; opt-outs exist for lazy or manually handled images.
- Intended for major release rollout, with possible minor release integration via View Transitions.
- Optimization avoids unnecessary fallback if the image is already decoded.

Recommendation:
Summary sufficient (read the PR for edge cases or if you implement custom image loading strategies)

Why it matters:
read the PR for edge cases or if you implement custom image loading strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
