---
type: twir-item
issue: 286
item: 7
item_type: item
date: 2026-06-17
source: https://make.wordpress.org/core/2026/06/05/react-19-upgrade-temporarily-reverted-in-gutenberg/
tags:
  - "WordPress"
  - "19"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 7: WordPress - React 19 upgrade temporarily reverted in Gutenberg

Source: [https://make.wordpress.org/core/2026/06/05/react-19-upgrade-temporarily-reverted-in-gutenberg/](https://make.wordpress.org/core/2026/06/05/react-19-upgrade-temporarily-reverted-in-gutenberg/)

Summary:
WordPress and Gutenberg temporarily reverted their React 19 upgrade after discovering widespread plugin incompatibilities, mainly due to differences in the react/jsx-runtime helper and element object shapes between React 18 and 19. The team plans to develop a more incremental upgrade strategy, possibly with feature flags and compatibility layers, before attempting the upgrade again.

Key takeaways:
- React 19 upgrade caused runtime incompatibilities with existing plugins.
- Differences in JSX runtime and element shapes triggered crashes.
- Upgrade reverted to React 18 in Gutenberg 23.3.2 for stability.
- Future upgrades will be more incremental and compatibility-focused.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
