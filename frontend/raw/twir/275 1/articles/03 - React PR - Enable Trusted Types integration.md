---
type: twir-item
issue: 275
item: 3
item_type: item
date: 2026-04-01
source: https://github.com/facebook/react/pull/35816
tags:
  - "TrustedTypes"
  - "PR"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 3: React PR - Enable Trusted Types integration

Source: [https://github.com/facebook/react/pull/35816](https://github.com/facebook/react/pull/35816)

Summary:
React now supports the browser Trusted Types API, a security feature that helps prevent DOM-based XSS by requiring typed objects for DOM injection sinks. Previously, React coerced all values to strings, breaking Trusted Types enforcement. With this change, React passes Trusted Types objects (e.g., TrustedHTML) directly to the DOM, ensuring compatibility and security for apps using Trusted Types, while remaining a no-op for apps that do not.

Key takeaways:
- Trusted Types objects are now preserved and passed directly to DOM APIs, fixing compatibility with strict CSP policies.
- Applies to dangerouslySetInnerHTML, all HTML/SVG attributes, and URL attributes.
- No breaking changes for apps not using Trusted Types; behavior is unchanged for them.
- Enhances security posture for React apps adopting Trusted Types.

Recommendation: Summary sufficient
