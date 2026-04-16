---
type: twir-item
issue: 273
item: 7
item_type: item
date: 2026-03-18
source: https://tanstack.com/blog/tanstack-start-5x-ssr-throughput
tags:
  - "TanStack"
  - "SSR"
  - "5x"
  - "Ease"
status: auto
quality: keep
---

[[2026-03-18-TWIR-273|Index]]

# Item 7: TanStack Start - 5x SSR Throughput after profiling SSR Hot Paths

Source: [https://tanstack.com/blog/tanstack-start-5x-ssr-throughput](https://tanstack.com/blog/tanstack-start-5x-ssr-throughput)

Summary:
TanStack Start achieved a 5.5x increase in SSR throughput and significant latency reductions by profiling and optimizing server hot paths. Improvements include avoiding unnecessary URL parsing, skipping client-side reactivity during SSR, and introducing server-only fast paths. The process involved targeted benchmarks, flamegraph analysis, and iterative PRs, resulting in more efficient SSR for high-traffic deployments.

Key takeaways:
- Throughput improved from 427 req/s to 2,357 req/s; latency and error rates dropped sharply.
- Major optimizations: fast-path checks for URLs, bypassing reactivity on the server, and code path simplifications.
- Profiling and feature-focused benchmarks were critical to identifying bottlenecks.
- These patterns are transferable to other SSR frameworks for similar gains.

Recommendation:
Read fully (for SSR framework maintainers or teams optimizing SSR performance)

Why it matters:
for SSR framework maintainers or teams optimizing SSR performance

Content:
# 5x SSR Throughput: Profiling SSR Hot Paths in TanStack Start

*by Manuel Schiller and Florian Pellet on Mar 17, 2026.*

![A flamegraph island in the tanstack universe](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Fheader.png&w=800&q=80)

We improved TanStack Start's SSR performance dramatically. Under sustained load (using our links-100 stress benchmark with 100 concurrent connections, 30 seconds):

- **Throughput**: 427 req/s → 2357 req/s (**5.5x**)
- **Average latency**: 424ms → 43ms (**9.9x faster**)
- **p99 latency**: 6558ms → 928ms (**7.1x faster**)
- **Success rate**: 99.96% → 100% (the server stopped failing under load)

For SSR-heavy deployments, this translates directly to lower hosting costs, the ability to handle traffic spikes without scaling, and eliminating user-facing errors.

This work started after v1.154.4 and targets server-side rendering performance. The goal was to increase throughput and reduce server CPU time per request.

We did it with a repeatable process, not a single clever trick:

- **Measure under load**, not in microbenchmarks.
- Use **CPU profiling** to find the highest-impact work.
- Remove **entire categories of cost** from the server hot path.

We highlight the highest-impact patterns below:

- avoid URL construction/parsing when it is not required
- avoid reactivity work during SSR (subscriptions, structural sharing, batching)
- add server-only fast paths behind a build-time isServer flag
- avoid delete in performance-sensitive code

We are not claiming that any single line of code is "the" reason. This work spanned over [20 PRs](https://github.com/TanStack/router/compare/v1.154.4...v1.157.18), with still more to come. Every change was validated by:

- a stable load test (same endpoint, same load)
- a before/after comparison on the same benchmark endpoint
- a CPU profile (flamegraph) that explains the delta

We did not benchmark "a representative app page". We used endpoints that exaggerate a feature so the profile is unambiguous:

- **links-100**: renders ~100 links to stress link rendering and location building.
- **layouts-26-with-params**: deep nesting + params to stress matching and path/param work.
- **empty**: minimal route to establish a baseline for framework overhead.

This is transferable: isolate the subsystem you want to improve, and benchmark that.

To capture a CPU profile of the server under load, we start the built server with [@platformatic/flame](https://github.com/platformatic/flame):

```
flame run ./dist/server.mjs
```

```
flame run ./dist/server.mjs
```

This produces:

- a CPU flamegraph
- a heap flamegraph
- and markdown summaries of the captured profile data

While @platformatic/flame is running in one terminal, we used [autocannon](https://github.com/mcollina/autocannon) in another terminal to generate a 30s sustained load. We tracked:

- requests per second (req/s)
- latency distribution (average, p95, p99)

Example command (adjust concurrency and route):

```
autocannon -d 30 -c 100 --warmup [ -d 2 -c 20 ] http://localhost:3000/bench/links-100
```

```
autocannon -d 30 -c 100 --warmup [ -d 2 -c 20 ] http://localhost:3000/bench/links-100
```

To improve SSR performance, we repeated the same loop:

- Focus on **self time** first. That is where the CPU is actually spent.
- Fix one hotspot, re-run the benchmark, and re-profile.
- Prefer changes that remove work in the steady state.

Our benchmarks were stable enough to produce very similar results on a range of setups. However, here are the exact environment details we used to run most of the benchmarks:

- Node.js: v24.12.0
- Hardware: MacBook Pro (M3 Max)
- OS: macOS 15.7

The exact benchmark code is available in [our repository](https://github.com/TanStack/router/tree/main/e2e/react-start/flamegraph-bench).

In our SSR profiles, URL construction/parsing showed up as significant self-time in the hot path on link-heavy endpoints. The cost comes from doing real work (parsing/normalization) and allocating objects. When you do it once, it does not matter. When you do it per link, per request, it dominates.

Use cheap predicates first, then fall back to heavyweight parsing only when needed.

- If a value is clearly internal (e.g. starts with / but not //, or starts with .), don't try to parse it as an absolute URL.
- If a feature is only needed in edge cases (e.g. rewrite logic), keep it off the default path.

```
// Before: always parse
const url = new URL(to, base)

// After: check first, parse only if needed
if (isSafeInternal(to)) {
  // fast path: internal navigation, no parsing needed
} else {
  const url = new URL(to, base)
  // ...external URL handling
}
```

```
// Before: always parse
const url = new URL(to, base)

// After: check first, parse only if needed
if (isSafeInternal(to)) {
  // fast path: internal navigation, no parsing needed
} else {
  const url = new URL(to, base)
  // ...external URL handling
}
```

The isSafeInternal check can be orders of magnitude cheaper than constructing a URL object[1](#user-content-fn-url-cost). It's meant to be a cheap predicate, so it is okay if some URLs that *would* be internal are classified as external and go through the slower path.

See: [#6442](https://github.com/TanStack/router/pull/6442), [#6447](https://github.com/TanStack/router/pull/6447), [#6516](https://github.com/TanStack/router/pull/6516)

Like every PR in this series, this change was validated by profiling the impacted method before and after. For example we can see in the example below that the buildLocation method went from being one of the major bottlenecks of a navigation to being a very small part of the overall cost:

![CPU profiling of buildLocation before the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Fbuild-location-before.png&w=800&q=80)

**Before:** The RouterCore.buildLocation (red arrow) method was creating a new URL every time (purple blocks), and then updating its search which re-triggers an expensive parsing step.

![CPU profiling of buildLocation after the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Fbuild-location-after.png&w=800&q=80)

**After:** The isSafeInternal check is able to fully skip the URL. RouterCore.buildLocation becomes an almost insignificant part of the overall cost.

SSR renders once per request.[2](#user-content-fn-ssr-streaming) There is no ongoing UI to reactively update, so on the server:

- store subscriptions add overhead but provide no benefit
- structural sharing[3](#user-content-fn-structural-sharing) reduces re-renders, but SSR does not re-render

If your code supports both client reactivity and SSR, gate the reactive machinery so the server can skip it entirely:

- on the server: return state directly, no subscriptions, reduce immutability overhead

This is the difference between "server = a function" and "client = a reactive system".

```
// Before: same code path for client and server
function useRouterState() {
  return useStore(router, { ... }) // unnecessary subscription on the server
}

// After: server gets a simple snapshot
function useRouterState() {
  if (isServer) return router.store // no subscriptions on the server
  return useStore(router, { ... }) // regular behavior on the client
}
```

```
// Before: same code path for client and server
function useRouterState() {
  return useStore(router, { ... }) // unnecessary subscription on the server
}

// After: server gets a simple snapshot
function useRouterState() {
  if (isServer) return router.store // no subscriptions on the server
  return useStore(router, { ... }) // regular behavior on the client
}
```

See: [#6497](https://github.com/TanStack/router/pull/6497), [#6482](https://github.com/TanStack/router/pull/6482)

isServer is a build-time constant. This means that the above code is not violating the rules of hooks in React. At runtime, the code will always execute the same branch.

Taking the example of the useRouterState hook, we can see that most of the client-only work was removed from the SSR pass, leading to a ~2x improvement in the total CPU time of this hook.

![CPU profiling of useRouterState before the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Frouter-state-before.png&w=800&q=80)

**Before:** The useRouterState hook was subscribing to the router store, which triggers many sync and memoization calls before calling the select callback.

![CPU profiling of useRouterState after the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Frouter-state-after.png&w=800&q=80)

**After:** The isServer check is able to skip directly to the select callback.

As a general rule, client code cares about bundle size, while server code cares about CPU time per request. Those constraints are different.

If you can guard a branch with a **build-time constant** like isServer, you can:

- add server-only fast paths for common cases
- keep the general algorithm for correctness and edge cases
- allow bundlers to delete the server-only branch from client builds

In TanStack Start, isServer is provided via build-time resolution of export conditions[4](#user-content-fn-export-conditions) (client: false, server: true, dev/test: undefined with fallback). Modern bundlers like Vite, Rollup, and esbuild perform dead code elimination (DCE)[5](#user-content-fn-dce), removing unreachable branches when the condition is a compile-time constant.

Write two implementations:

- **fast path** for the common case
- **general path** for correctness

And gate them behind a build-time constant so you don't inflate the bundle size for clients.

```
// isServer is resolved at build time:
// - Vite/bundler replaces it with `true` (server) or `false` (client)
// - Dead code elimination removes the unused branch

if (isServer) {
  // server-only fast path (removed from client bundle)
  if (isCommonCase(input)) {
    return fastServerPath(input)
  }
}
// general algorithm that handles all cases
return generalPath(input)
```

```
// isServer is resolved at build time:
// - Vite/bundler replaces it with `true` (server) or `false` (client)
// - Dead code elimination removes the unused branch

if (isServer) {
  // server-only fast path (removed from client bundle)
  if (isCommonCase(input)) {
    return fastServerPath(input)
  }
}
// general algorithm that handles all cases
return generalPath(input)
```

See: [#4648](https://github.com/TanStack/router/pull/4648), [#6505](https://github.com/TanStack/router/pull/6505), [#6506](https://github.com/TanStack/router/pull/6506)

Taking the example of the matchRoutesInternal method, we can see that its children's total CPU time was reduced by ~25%.

![CPU profiling of interpolatePath before the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Finterpolate-before.png&w=800&q=80)

**Before:** The interpolatePath function spends >1s using the generic parseSegment function.

![CPU profiling of interpolatePath after the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Finterpolate-after.png&w=800&q=80)

**After:** The interpolatePath function now uses the server-only fast path, skipping parseSegment entirely.

Modern engines optimize property access using object "shapes" (e.g. V8 HiddenClasses[6](#user-content-fn-v8-fast-properties) / JSC Structures[7](#user-content-fn-webkit-delete-ic)) and inline caches. delete changes an object's shape and can force a slower internal representation (e.g. dictionary/slow properties), which can disable or degrade those optimizations and deopt optimized code.

Avoid delete in hot paths. Prefer patterns that don't mutate object shapes in-place:

- set a property to undefined (when semantics allow)
- create a new object without the key (object rest destructuring) when you need a "key removed" shape

```
// Before: mutates shape
delete this.shouldViewTransition

// After: set to undefined
this.shouldViewTransition = undefined
```

```
// Before: mutates shape
delete this.shouldViewTransition

// After: set to undefined
this.shouldViewTransition = undefined
```

See: [#6456](https://github.com/TanStack/router/pull/6456), [#6515](https://github.com/TanStack/router/pull/6515)

Taking the example of the startViewTransition method, we can see that the total CPU time of this method was reduced by >50%.

![CPU profiling of startViewTransition before the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Fdelete-before.png&w=800&q=80)

**Before:** The startViewTransition function (red arrow) has ~400ms of self-time in the hot path (i.e. not including the time spent in its children).

![CPU profiling of startViewTransition after the changes](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Fdelete-after.png&w=800&q=80)

**After:** Removing the delete statement almost completely removes the self-time of this function.

Matteo Collina independently benchmarked Start's SSR performance as part of his [article investigating SSR performance across React meta-frameworks](https://blog.platformatic.dev/react-ssr-framework-benchmark-tanstack-start-react-router-nextjs) and observed significant improvements after our optimizations. The following table summarizes the before/after results under sustained load:

| Metric | Before | After | Improvement |
| --- | --- | --- | --- |
| Success rate | 75.52% | 100% | does not fail under load |
| Throughput | 477 req/s | 1041 req/s | +118% (2.2x) |
| Average latency | 3,171ms | 13.7ms | 231x faster |
| p90 latency | 10,001ms | 23.0ms | 435x faster |
| p95 latency | 10,001ms | 28.1ms | 370x faster |

The "before" numbers show a server under severe stress: 25% of requests failed (likely timeouts), and p90/p95 hit the 10s timeout ceiling. After the optimizations, the server handles the same load comfortably with sub-30ms tail latency and zero failures.

To be clear: TanStack Start was not broken before these changes. Under normal traffic, SSR worked fine. These numbers reflect behavior under *sustained heavy load* (the kind you see during traffic spikes or load testing). The optimizations increase headroom. At this same load, the server no longer drops requests, and it only starts failing at substantially higher load than before.

The following graphs show event-loop utilization[8](#user-content-fn-elu) against throughput for each feature-focused endpoint, before and after the optimizations. Lower utilization at the same req/s means more headroom; higher req/s at the same utilization means more capacity.

For reference, the machine on which these were measured reaches 100% event-loop utilization at 100k req/s on an empty Node HTTP server[9](#user-content-fn-empty-node-http-server).

#### 100 links per page[#](#100-links-per-page)

![Event-loop utilization vs throughput for links-100, before and after](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Felu-links.png&w=800&q=80)

![Event-loop utilization vs throughput for nested routes, before and after](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Felu-nested.png&w=800&q=80)

![Event-loop utilization vs throughput for minimal route, before and after](/.netlify/images?url=%2Fblog-assets%2Ftanstack-start-5x-ssr-throughput%2Felu-empty.png&w=800&q=80)

The biggest gains came from removing whole categories of work from the server hot path. Throughput improves when you eliminate repeated work, allocations, and unnecessary generality in the steady state.

There were many other improvements (client and server) not covered here. SSR performance work is ongoing.
