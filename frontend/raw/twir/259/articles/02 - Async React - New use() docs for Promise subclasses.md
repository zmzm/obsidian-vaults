---
type: twir-item
issue: 259
item: 2
item_type: item
date: 2025-11-19
source: https://github.com/reactwg/async-react/discussions/3
tags:
  - "Promisesubclasses"
status: auto
quality: keep
---

[[2025-11-19-TWIR-259|Index]]

# Item 2: Async React - New use() docs for Promise subclasses

Source: [https://github.com/reactwg/async-react/discussions/3](https://github.com/reactwg/async-react/discussions/3)

Summary:
A new documentation PR clarifies how to correctly create and use Promises with React’s experimental use() hook for Suspense-enabled data fetching. The discussion highlights pitfalls of conditional use() calls, the importance of promise instrumentation for caching/preloading, and practical patterns for subclassing or augmenting Promises to work seamlessly with React. The post also touches on SSR and DevTools implications.

Key takeaways:
- Avoid conditionally calling use() based on data presence to prevent data corruption and hydration issues.
- For cached/preloaded data, ensure Promises are instrumented so use() can resolve them synchronously.
- Subclassing or augmenting Promises (or using thenable-like objects) is recommended for advanced caching scenarios.
- React plans to warn about incorrect use() patterns in the future.

Recommendation:
Read fully

Content:
# New `use()` docs for Promise subclasses · reactwg/async-react · Discussion #3 · GitHub

👍
1
  reacted with thumbs up emoji

 👎
1
  reacted with thumbs down emoji

 😄
1
  reacted with laugh emoji

 🎉
1
  reacted with hooray emoji

 😕
1
  reacted with confused emoji

 ❤️
1
  reacted with heart emoji

 🚀
1
  reacted with rocket emoji

 👀
1
  reacted with eyes emoji

You can’t perform that action at this time.
