---
type: twir-item
issue: 211
item: 2
item_type: item
date: 2024-11-27
source: https://github.com/facebook/react/pull/31596
tags:
  - "PR"
status: auto
quality: keep
---

[[2024-11-27-TWIR-211|Index]]

# Item 2: React Core PR - Add moveBefore Experiment

Source: [https://github.com/facebook/react/pull/31596](https://github.com/facebook/react/pull/31596)

Summary:
A longstanding React issue is that reordering stateful nodes can cause state loss. The new moveBefore() proposal, now at intent-to-ship stage, aims to allow DOM node reordering while preserving state, similar to insertBefore but stateful. The feature is currently behind a Chrome flag and not yet available in experimental React builds due to a semantic breaking change when moving disconnected nodes.

Key takeaways:
- moveBefore() preserves state when reordering DOM nodes, addressing a common React pain point.
- Still experimental and requires a custom build; not enabled even in React experimental channels yet.
- There is an unresolved issue when both nodes are disconnected, which must be addressed before wider rollout.
- Demo and further discussion are available for those interested in the technical details.

Recommendation:
Summary sufficient (read the PR if you need deep technical or implementation details)

Why it matters:
read the PR if you need deep technical or implementation details

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
