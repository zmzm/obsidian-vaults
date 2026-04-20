---
type: twir-item
issue: 238
item: 6
item_type: item
date: 2025-06-11
source: https://bikeshedd.ing/posts/use_state_should_require_a_dependency_array/
tags:
status: auto
quality: keep
---

[[2025-06-11-TWIR-238|Index]]

# Item 6: useState should require a dependency array

Source: [https://bikeshedd.ing/posts/use_state_should_require_a_dependency_array/](https://bikeshedd.ing/posts/use_state_should_require_a_dependency_array/)

Summary:
The article argues that React's useState should require a dependency array to prevent common bugs related to derived state from props or other mutable values. It discusses pitfalls of current patterns, the limitations of using key props and workarounds, and suggests that stricter linting or API changes could help avoid subtle bugs in state synchronization.

Key takeaways:
- Initializing useState from props can lead to stale or unsynchronized state if the prop changes.
- Using key to force remounts solves some issues but can cause unwanted resets of unrelated state.
- React and other frameworks (like SolidJS) could benefit from stricter linting or API changes to prevent these patterns.
- The article provides practical examples and discusses why current workarounds are often insufficient.

Recommendation:
Read fully (for a deep understanding of state synchronization issues and best practices)

Why it matters:
for a deep understanding of state synchronization issues and best practices

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
