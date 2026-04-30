---
type: concept
status: active
updated: 2026-04-21
tags:
  - react
  - activity
  - rendering
  - suspense
---

# React Activity

React Activity is a rendering concept for keeping UI subtrees alive while changing their visibility and execution priority, which makes it useful for state preservation, preloading, and smoother async navigation flows.

## Key Ideas

- Activity is not just "show or hide a subtree"; it changes how hidden work is kept around and resumed.
- It is useful where unmounting would throw away valuable local state, but fully active rendering would waste work.
- The concept becomes especially interesting when combined with Suspenseful data, route transitions, and state restoration across navigation.

## Practical Significance

- This page should become the landing point for Activity as a distinct async-rendering primitive rather than leaving it scattered across release notes and PRs.
- It matters because Activity changes how React apps can model tabs, hidden panes, route back/forward restoration, and speculative UI work.

## Current Signals

- The archive now contains repeated references to Activity in React core, Next.js experiments, and practical Suspense-oriented usage guidance.
- That is enough to treat it as an active concept instead of a release-footnote feature.

## Related Pages

- [[Server Components]]
- [[React use()]]
- [[../topics/React Rendering|React Rendering]]
- [[../tools/Next.js|Next.js]]
- [[../sources/TWIR 230|TWIR 230]]
- [[../sources/TWIR 231|TWIR 231]]
- [[../sources/TWIR 248|TWIR 248]]
- [[../sources/TWIR 250|TWIR 250]]
- [[../sources/TWIR 252|TWIR 252]]
- [[../sources/TWIR 254|TWIR 254]]

## Sources

- [[../../raw/twir/230/articles/03 - Next.js PR - Experimental bfcache - Restore state with Activity|Next.js PR - Experimental bfcache - Restore state with Activity]]
- [[../../raw/twir/248/articles/07 - Using Activity with Suspenseful data|Using Activity with Suspenseful data]]
- [[../../raw/twir/250/2025-09-17-TWIR-250|TWIR #250]]
- [[../../raw/twir/252/articles/01 - React 19.2|React 19.2]]
- [[../../raw/twir/254/2025-10-15-TWIR-254|TWIR #254]]

## Open Questions

- Where Activity should be preferred over simpler conditional rendering plus preserved parent state.
- How much of its long-term value depends on framework integration rather than standalone React usage.
