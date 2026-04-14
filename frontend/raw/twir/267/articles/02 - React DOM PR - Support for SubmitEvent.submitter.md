---
type: twir-item
issue: 267
item: 2
item_type: item
date: 2026-02-04
source: https://github.com/facebook/react/pull/35590
tags:
  - "DOM"
  - "PR"
  - "SubmitEventsubmitter"
  - "Bun"
status: auto
---

[[2026-02-04-TWIR-267|Index]]

# Item 2: React DOM PR - Support for SubmitEvent.submitter

Source: [https://github.com/facebook/react/pull/35590](https://github.com/facebook/react/pull/35590)

Summary:
A pull request to React DOM adds support for the SubmitEvent.submitter property, which identifies the element that triggered a form submission. The change assumes broad browser support and includes tests to validate the new interface, with no significant impact on bundle size.

Key takeaways:
- React DOM will now expose the submitter property on submit events, aligning with native browser behavior.
- No polyfill is included for older browsers; assumes modern browser usage.
- The change is tested and has negligible impact on bundle size.

Recommendation: Summary sufficient
