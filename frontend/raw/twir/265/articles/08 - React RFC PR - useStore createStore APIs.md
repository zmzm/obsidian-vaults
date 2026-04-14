---
type: twir-item
issue: 265
item: 8
item_type: item
date: 2026-01-21
source: https://developer.chrome.com/blog/anchor-positioning-api
tags:
  - "Store"
  - "RFC"
  - "PR"
  - "APIs"
status: auto
---

[[2026-01-21-TWIR-265|Index]]

# Item 8: React RFC PR - useStore/createStore APIs

Source: [https://developer.chrome.com/blog/anchor-positioning-api](https://developer.chrome.com/blog/anchor-positioning-api)

Summary:
This RFC proposes new useStore and createStore APIs for React, enabling efficient observation of external (non-React) state with correct transition semantics and minimal rerenders. The ReactExternalDataSource interface allows libraries to expose state to React components, while useStore and createStore provide ergonomic hooks for consuming and updating such state. The proposal addresses shortcomings of useContext, useReducer, and useSyncExternalStore for shared state management in concurrent React.

Key takeaways:
- Introduces a standard interface (ReactExternalDataSource) for external state sources.
- useStore enables efficient, selective observation of external state with transition support.
- createStore provides a simple, built-in store implementation for common use cases.
- Aims to reduce rerenders, avoid tearing, and support concurrent React semantics.

Recommendation: Read fully (for library authors and advanced state management users)
