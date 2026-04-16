---
type: twir-item
issue: 261
item: 2
item_type: item
date: 2025-12-03
source: https://github.com/reduxjs/react-redux/issues/2264
tags:
  - "React-Redux"
  - "Bun"
status: auto
quality: keep
---

[[2025-12-03-TWIR-261|Index]]

# Item 2: React-Redux issue - Mark connect as deprecated

Source: [https://github.com/reduxjs/react-redux/issues/2264](https://github.com/reduxjs/react-redux/issues/2264)

Summary:
The React-Redux team proposes officially deprecating the connect API, aligning with their long-standing recommendation to use useSelector instead. Connect will not be removed soon, but will be marked as @deprecated in upcoming releases, and documentation will be updated accordingly. The move is motivated by connect's larger bundle size, complex TypeScript usage, and lack of compatibility with upcoming concurrent features.

Key takeaways:
- connect will be marked as deprecated but not removed in the near future.
- useSelector is the recommended alternative for new codebases.
- Deprecation aligns with React’s direction towards concurrent-compatible APIs.
- Documentation and tutorials referencing connect will be updated or removed.

Recommendation:
Summary sufficient (read issue if you rely on connect or maintain large Redux codebases)

Why it matters:
read issue if you rely on connect or maintain large Redux codebases

Content:
# Mark `connect` as deprecated · Issue #2264 · reduxjs/react-redux · GitHub

### What is the new or updated feature that you are suggesting?

We're doing early collaboration with the React team on the design and behavior of the upcoming "concurrent stores" API. Loosely put, it's meant to be a concurrent compatible replacement for `useSyncExternalStore`.

This would likely ship as React-Redux v10, and also require a newer minimum version of React (unless they ship a polyfill for backwards compat with older versions).

Per discussion in [#2263 (comment)](https://github.com/reduxjs/react-redux/pull/2263#issuecomment-3566978744) , I don't intend to spend any time upgrading `connect` to use the new API, which means that it would still be using `useSyncExternalStore` and have its limitations with concurrent behavior like transitions.

We've said for years that `useSelector` ought to be the default, and that while we're not *removing* `connect`, we also recommend against using it.

Given that, we ought to do the [same thing we did for `createStore`](https://github.com/reduxjs/redux/releases/tag/v4.2.0), and officially mark `connect` as `@deprecated`. As with `createStore`, we still have no plans to remove `connect`, but we really don't think anyone should be writing new code that uses it directly.

As with `createStore`, I'd probably ship an aliased version that doesn't have the deprecation, for folks who *reallly* don't want those deprecated strikethroughs in their codebase (or get flagged by enterprise linting requirements).

Once again, to be very clear: **I do not intend to remove `connect` any time in the near future!** It's possible we might remove it *someday*, but I have no plans to actually do so, and *if* we ever do it'd be a few years / major versions down the road.

Given that `connect` has a bigger bundle size, much more complex TS usage, worse re-rendering performance due to the tiered update cascading in the commit phase, and presumably won't have upcoming concurrent compat like `useSelector`, there's no good reason for people to still use it. Even the auto-wrapping-with-`React.memo` behavior is irrelevant now that the React Compiler exists.

I'll probably ship this deprecation in a new minor release in the next few weeks when I have time to do the work, and update the docs to cover this. (I might even rip out the ancient `connect`-based tutorial page while I'm at it.)

### Why should this feature be included?

Because `connect` is obsolete :)

### What docs changes are needed to explain this?

Release notes, removing some `connect` references, etc.
