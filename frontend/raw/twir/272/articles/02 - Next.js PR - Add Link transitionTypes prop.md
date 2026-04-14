---
type: twir-item
issue: 272
item: 2
item_type: item
date: 2026-03-11
source: https://github.com/vercel/next.js/pull/90701
tags:
  - "Nextjs"
  - "PR"
  - "Navigation"
status: auto
---

[[2026-03-11-TWIR-272|Index]]

# Item 2: Next.js PR - Add Link transitionTypes prop

Source: [https://github.com/vercel/next.js/pull/90701](https://github.com/vercel/next.js/pull/90701)

Summary:
A new transitionTypes prop is added to Next.js's <Link> component, enabling developers to specify transition animations for navigations in the App Router. The prop is reactive and integrates with React's addTransitionType API, allowing dynamic transitions based on React state. A bug fix ensures transitionTypes is not leaked onto DOM elements, and the feature is only supported in the App Router (not Pages Router). This aligns Next.js navigation with React's upcoming view transitions capabilities.

Key takeaways:
- transitionTypes enables animated transitions for navigation in Next.js App Router.
- The prop is reactive and can be controlled via component state.
- Proper prop handling prevents React warnings and invalid DOM attributes.
- Only available in App Router; ignored in Pages Router.

Recommendation: Summary sufficient (read PR for implementation details or if you build custom navigation components)
