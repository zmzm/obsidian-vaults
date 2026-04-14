---
type: twir-item
issue: 275
item: 6
item_type: item
date: 2026-04-01
source: https://tanstack.com/blog/tanstack-router-signal-graph
tags:
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 6: TanStack Router's New Reactive Core: A Signal Graph

Source: [https://tanstack.com/blog/tanstack-router-signal-graph](https://tanstack.com/blog/tanstack-router-signal-graph)

Content:
# TanStack Router's New Reactive Core: A Signal Graph | TanStack Blog

*by Florian Pellet on Mar 31, 2026.*

![veins of emerald as a signal graph embedded in the rock of a tropical island](https://tanstack.com/.netlify/images?url=%2Fblog-assets%2Ftanstack-router-signal-graph%2Fheader.jpg&w=800&q=80)

TanStack Router used to keep all of its reactive state in one large object: router.state. [This refactor](https://github.com/TanStack/router/pull/6704) replaces that with a graph of smaller stores for the pieces of state that change independently. router.state still exists, but it is now derived from those stores instead of serving as the internal source of truth.

This builds on TanStack Store's migration[1](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fn-alien-migration) to [alien-signals](https://github.com/stackblitz/alien-signals), implemented by [@DavidKPiano](https://github.com/davidkpiano). In external benchmarks[2](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fn-alien-bench), alien-signals performed very well. The faster primitive helps, but the bigger change is that this allows the router to track state in smaller pieces instead of routing everything through one broad store.

Concretely, this means:

-   more targeted updates,
-   fewer store updates during navigation,
-   faster client-side navigation in our benchmarks,
-   the Solid adapter now uses native Solid signals internally.

The old model had one main reactive surface: router.state.

That was useful. It made it possible to prototype features quickly and ship a broad API surface without first designing a perfect internal reactive topology. But it also meant many different concerns shared the same reactive entry point.

| Concern | Stored under router.state | Typical consumer |
| --- | --- | --- |
| Location | location, resolvedLocation | useLocation, Link |
| Match lifecycle | matches, pendingMatches, cachedMatches | useMatch, Matches, Outlet |
| Navigation status | status, isLoading, isTransitioning | pending UI, transitions |
| Side effects | redirect, statusCode | navigation and response handling |

Routing state does not change as one unit. During a navigation, one match stays active, another becomes pending, one link changes state, and some cached matches do not change at all.

The old model captured those pieces of state, but all subscriptions still started from the same top-level state object. That mismatch shows up here:

A video showing that on every stateful event in the core of the router, changes are propagated to every subscription across the entire application.

The main change is that the smaller stores are now the source of truth, and router.state is rebuilt from them.

Instead of one broad state object, the router keeps separate stores with narrower responsibilities.

-   **top-level stores** for location, status, loading, transitions, redirects, and similar scalar state
-   **per-match stores** grouped into pools of active matches, pending matches, and cached matches.
-   **derived stores** for specific purposes like "is any match pending"

router.state still exists for public APIs, but it is now rebuilt from the store graph instead of serving as the internal source of truth.

The new picture looks like this:

Note

Active, pending, and cached matches are now modeled separately because they have different lifecycles. This cuts down updates even further.

Before, the smaller pieces of state were derived from router.state. Now, router.state is derived from the smaller stores. That is the core of this refactor.

ts

```
// Before
useRouterState({
  select: (state) => {
    const match = state.matches.find((m) => m.routeId === routeId)
    return /* select from one match */
  }
})

// After
const matchStore = router.stores.getMatchStoreByRouteId(routeId)
useStore(matchStore, (match) => /* select from one match */)
```

```
// Before
useRouterState({
  select: (state) => {
    const match = state.matches.find((m) => m.routeId === routeId)
    return /* select from one match */
  }
})

// After
const matchStore = router.stores.getMatchStoreByRouteId(routeId)
useStore(matchStore, (match) => /* select from one match */)
```

This is an internal implementation detail, not a new public API surface for application code.

Note

The store-update-count graphs below show how many times subscriptions are invoked during various routing scenarios. The last point is this refactor.[4](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fn-store-update-tests)

Important

Vue Router is mentioned throughout this article as a useful reference. However it is still a work in progress. Vue Vapor (3.6) is on the doorstep (beta.9 at the time of writing), so the plan is to do the Vapor refactor and then support that refreshed version.

The refactor also moves the store implementation behind a shared contract.

The router core defines the interface. Each adapter provides the implementation.

ts

```
export interface RouterReadableStore<TValue> {
  readonly state: TValue
}

export interface RouterWritableStore<TValue> {
  readonly state: TValue
  setState: (updater: (prev: TValue) => TValue) => void
}

export type StoreConfig = {
  createMutableStore: MutableStoreFactory
  createReadonlyStore: ReadonlyStoreFactory
  batch: RouterBatchFn
  init?: (stores: RouterStores<AnyRoute>) => void
}
```

```
export interface RouterReadableStore<TValue> {
  readonly state: TValue
}

export interface RouterWritableStore<TValue> {
  readonly state: TValue
  setState: (updater: (prev: TValue) => TValue) => void
}

export type StoreConfig = {
  createMutableStore: MutableStoreFactory
  createReadonlyStore: ReadonlyStoreFactory
  batch: RouterBatchFn
  init?: (stores: RouterStores<AnyRoute>) => void
}
```

| Adapter | Store implementation |
| --- | --- |
| React | TanStack Store |
| Vue | TanStack Store |
| Solid | Solid signals |

This keeps one router core while letting each adapter plug in the store model it wants.

Note

Solid's derived stores are backed by native memos, and the adapter uses a FinalizationRegistry[5](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fn-finalization-registry) to dispose detached roots when those stores are garbage-collected.

No new public API is required here. useMatch, useLocation, and <Link> keep the same surface. The difference is that navigation and preload flows now trigger fewer subscriptions.

Our benchmarks isolate client-side navigation cost on a synthetic rerender-heavy page.[6](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fn-client-nav-bench)

-   React: 7ms -> 4.5ms
-   Solid: 12ms -> 8ms
-   Vue: 7.5ms -> 6ms

There is also a bundle-size tradeoff. In our synthetic bundle-size benchmarks, measuring gzipped sizes:[7](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fn-bundle-size-bench)

-   ↗ React increased by ~1KiB
-   ↗ Vue increased by ~1KiB
-   ↘ Solid decreased by ~1KiB

React and Vue increased in size because representing the router as several stores takes more code than representing it as one state object. Solid decreased in size because it no longer depends on tanstack/store.

This refactor changes how reactivity is structured inside the router.

Before, router.state was the broad reactive surface and smaller pieces of state were derived from it. Now the smaller stores are primary, and router.state is a derived snapshot kept for the existing public API.

In practice, that means route changes update more locally and trigger less work during navigation.

* * *

1.  [TanStack Store PR #265](https://github.com/TanStack/store/pull/265) [↩](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fnref-alien-migration)

2.  [js-reactivity-benchmark](https://github.com/transitive-bullshit/js-reactivity-benchmark) last updated January 2025 [↩](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fnref-alien-bench)

3.  For a great JavaScript-oriented explanation of how LRU caches work, see [Implementing an efficient LRU cache in JavaScript](https://yomguithereal.github.io/posts/lru-cache/). [↩](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fnref-lru-cache)

4.  Methodology and exact scenario assertions live in the adapter test files for [React](https://github.com/TanStack/router/blob/main/packages/react-router/tests/store-updates-during-navigation.test.tsx), [Solid](https://github.com/TanStack/router/blob/main/packages/solid-router/tests/store-updates-during-navigation.test.tsx), and [Vue](https://github.com/TanStack/router/blob/main/packages/vue-router/tests/store-updates-during-navigation.test.tsx). [↩](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fnref-store-update-tests)

5.  A [FinalizationRegistry](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry) allows us to hook into the Garbage Collector to execute arbitrary cleanup functions when an object gets collected. [↩](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fnref-finalization-registry)

7.  These numbers come from the deterministic fixtures in [benchmarks/bundle-size](https://github.com/TanStack/router/tree/main/benchmarks/bundle-size), measured from the initial-load JS graph and tracked primarily as gzip deltas. See the [README](https://github.com/TanStack/router/blob/main/benchmarks/bundle-size/README.md). [↩](https://tanstack.com/blog/tanstack-router-signal-graph#user-content-fnref-bundle-size-bench)

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
