---
type: "twir-recovery"
issue: 294
item: 13
source: "https://tanstack.com/blog/tanstack-router-navigation-lanes"
final_url: "https://tanstack.com/blog/tanstack-router-navigation-lanes"
retrieved: "2026-10-22T11:30:06+00:00"
original_note: "frontend/raw/twir/294/articles/13 - Inside a TanStack Router Navigation.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/13 - Inside a TanStack Router Navigation|Inside a TanStack Router Navigation]]

# Inside a TanStack Router Navigation

![A meandering river flows, its tributaries joining and separating](https://tanstack.com/cdn-cgi/image/width=1200,quality=80,format=auto/blog-assets/tanstack-router-navigation-lanes/header.png)

From application code, a navigation looks almost too simple:

```
await router.navigate({ to: '/account' })
```

That simplicity gets deceptive as soon as a few things overlap.

[](/blog-assets/tanstack-router-navigation-lanes/tanstack-router-navigation-demo.mp4)

1. Hovering /account starts preloading it.
2. Clicking /account reuses the loading work that the hover started.
3. Before it finishes, the user clicks /settings, whose route loaders run in parallel.
4. One /settings loader errors while another redirects to /login.
5. The earlier /account work finishes and is cached, even though the user is no longer going there.
6. The router publishes /login, but its content suspends.
7. The framework eventually renders /login.

This is what the scenario looks like on a timeline. Don't worry about the labels yet, we'll unpack them as we go.

![A timeline where an account preload is joined by a navigation, a later settings navigation starts layout and index loaders, the index loader redirects to login, account data also enters the cache, and the framework acknowledges login after publication](/blog-assets/tanstack-router-navigation-lanes/nav-orchestra_simple-scenario.svg)

Account loading, the redirect to login, caching, and rendering proceed on different schedules.

Why can /account keep loading after the user moves on, but no longer update the page? Why does the /settings error never appear? And why isn't publishing /login the end of the navigation?

**A navigation looks like one asynchronous operation, but the router must decide four things independently: which loading work should continue, which navigation may publish, what the route attempt decided, and whether the framework rendered it.**

That distinction came out of [rewriting TanStack Router's loading system](https://github.com/TanStack/router/pull/7805). We had dozens of bugs across preloading, redirects, caching, pending UI, SSR, and more. They looked unrelated, but many had the same root cause: the router compressed too many facts into too few variables. Cancellation, supersession, publication, and rendering were allowed to stand in for each other.[1](#user-content-fn-lifetime-bugs)

Application code still gets one navigate() call. Inside the router, separate lifetimes keep track of those four answers.[2](#user-content-fn-architecture)

Before we return to all that overlap, it helps to focus on one ordinary navigation. There is no second click, no error, and no redirect here. The route simply loads slowly enough to show pending UI, then succeeds.

Each row follows a different part of the navigation, and the arrows between them are handoffs. Loaders can run while a pending timer races them. The framework can render pending UI while the private route branch keeps loading. We'll decode the internal labels just below.

![A single navigation moving through route matching, transaction acquisition, context building, parallel loader flights, pending UI publication, outcome selection, final match publication, and framework render acknowledgements](/blog-assets/tanstack-router-navigation-lanes/nav-orchestra_single-orchestration.svg)

One successful navigation still moves along several schedules: loaders run, pending UI may appear, final matches publish, and the framework handles each publication in its own time.

The **lane** in the middle is a private, unpublished draft of the matched route branch. Following it across the diagram:

1. **Route matching** turns the destination URL into an ordered branch of route matches.
2. The navigation becomes the **current transaction**. This is what grants it permission to publish if it is still current when the work finishes.[3](#user-content-fn-planning)
3. The private lane builds route context and runs beforeLoad from parent to child. Each child needs its parent's completed context, so this part is intentionally serial.
4. Eligible route loaders can then run in parallel. Each actual loader invocation is a **loader flight**.
5. If the loaders take longer than pendingMs, the router can publish pending UI. The framework handles that publication while the lane keeps working toward the final result.
6. Once the loader outcomes are ready, the lane selects the successful result.
7. This navigation is still current, so it publishes the final matches. The framework acknowledges that publication, and the navigation can finish.

Note

The diagram's release flight label marks where the lane releases its temporary claim. That does not necessarily end ownership of settled data. The loader-flight section below explains why.

Nothing goes wrong in this version. The transaction is never replaced, the loaders do not error or redirect, and both publications render successfully. Now change one assumption at a time:

Usually, all four answers arrive within a few milliseconds of each other, preserving the illusion of one asynchronous task, but it is also plenty of time for another event to change what should happen next.

The opening scenario puts all four complications back together. Here is the whole thing at once, and then one section per complication.

Unlike the other diagrams, this one reads from **top to bottom**. Each column follows one owner: the current transaction, a private lane, a loader flight, or the framework render. The horizontal arrows pass work or results between them. This is only one possible interleaving; independent events, such as caching /account and publishing /login, could happen in either order.

In the opening scenario, /account keeps loading after the user clicks away. Both the hover preload and the navigation need /account's data, but the loader should still run only once.

The preload and navigation still do their own matching, build their own context, and run their own beforeLoad. They share only the loader invocation and its outcome.

To decide when that shared invocation can be aborted, the router wraps it in a **flight**: a promise, an abort controller, and a lease count. Every consumer that needs the flight takes a **lease**.[4](#user-content-fn-flights)

![One loader flight shared across three overlapping lease lifetimes, with its lease count rising from one to three and falling back to zero](/blog-assets/tanstack-router-navigation-lanes/nav-orchestra_mini-lease-explainer.svg)

Consumers acquire and release their own claims on one loader invocation. The flight remains owned until the final lease ends.

For /account, clicking /settings ends the navigation's claim. The preload still holds its own lease, so the count never reaches zero. The flight continues, settles, and its result enters the cache.

Losing permission to publish /account does not prove that its loader is useless. The transaction enforces whether /account may publish, and the flight's leases track whether the loader is still needed.

Note

Preload and navigation lanes, published routes, and cache entries can all hold leases. A lease can also outlive the promise it covers: the lease represents ownership of the resource, not a promise lifecycle.

Keeping a loader alive is separate from deciding whether its navigation may reach the page. In the simple example, one transaction stays current all the way through publication. In the complex scenario, /settings starts while the /account lane is still pending.

The **current transaction** is a single slot that holds which navigation is allowed to publish. When /settings takes the slot, /account loses that right. It does not matter whether some of /account's work is still useful; the lane can no longer update the page.

![The /account lane moves through matching, beforeLoad and loaders, checking that it still holds the transaction between stages; /settings then takes the slot, so any /account continuation fails its next check and cannot publish](/blog-assets/tanstack-router-navigation-lanes/nav-orchestra_mini-tx-explainer.svg)

At each async boundary, the lane compares its transaction with the current slot. The first few checks pass, but when `/settings` takes the slot, the next check fails. The `/account` lane loses publication authority, and the dotted segment can never publish.

Discarding the navigation also releases its leases. Any pending flight with no other consumers may now abort. Our /account flight has the preload consumer, though, so it carries on.

Note

The implementation check is deliberately small. At an asynchronous boundary, a lane that no longer holds the slot cleans up and returns instead of publishing:

```
if (router._tx !== tx) {
  finishPending(tx)
  discardLane(result)
  return
}
```

In the successful navigation, every loader contributes to one successful result. The diagram below shows three outcomes: the root route succeeds, the parent layout loader rejects, and the child index loader throws redirect('/login').

Each settlement tells us what happened to one loader, but not yet what the whole route attempt should do. The outcomes go back to the private lane, which **reduces** them into one result.[5](#user-content-fn-reduction)

![Three loaders return a success, an error, and a redirect to one private lane, which reduces them to a single outcome](/blog-assets/tanstack-router-navigation-lanes/nav-orchestra_mini-reduce-explainer.svg)

Loader outcomes return to the lane. One settled error cannot decide the route result while another started loader could still redirect.

The error does not become the lane's result just because it settles first. Before choosing an ordinary failure, the lane waits for already-started loaders that could still redirect. It eventually chooses one result for the whole branch:

- A redirect starts a new navigation.
- A failure selects the error or not-found boundary that will render it.
- A success makes the complete lane eligible to publish.

It is tempting to say that the redirect "beats" the error, but that is not quite what happens. A redirect is *control flow* and not really a piece of UI. It discards the /settings lane and starts a new navigation to /login. Since that lane never publishes its final matches, the error never reaches the page.

Note

The lane's TypeScript type changes with each phase: matched, contextualized, reduced, then projected. These labels help ensure that the lane goes through each stage in the correct order without adding runtime states.[6](#user-content-fn-lane-phases)

*This section depends on the UI framework (React / Solid / Vue). We will use React for this explanation.*

Both scenarios represent the end of a successful lane as two separate events: publish and acknowledge. *Publishing* means handing a route branch to the framework. It is a request to render, not proof that the framework committed that branch.[7](#user-content-fn-publication-events)

React may still be busy with the previous tree. The new one can suspend on promises of its own (useSuspenseQuery, use(promise), lazy(() => import(...)), etc.), leaving the committed UI on screen. If another navigation publishes in the meantime, the earlier publication may never commit at all.

The diagram below shows that generic race.

![Two route publications race to render. The first is replaced before it commits and receives a false acknowledgement; the second commits and receives a true acknowledgement](/blog-assets/tanstack-router-navigation-lanes/nav-orchestra_mini-ack-explainer.svg)

The second publication replaces the first before it commits, then commits successfully itself.

To tell these cases apart, the router keeps a single **receipt** slot. A new publication acknowledges (ack) the previous receipt with false before installing its own. If React commits the new publication, the adapter acknowledges that receipt with true.[8](#user-content-fn-framework-ack)

ack:false does not mean the navigation failed. It means that exact publication was replaced before it committed. Either answer settles the receipt, but only ack:true proves that the framework rendered the publication.

Note

The receipt belongs to one exact publication. Either answer releases the internal render wait, but what happens next depends on the value:

|  | ack:true | ack:false |
| --- | --- | --- |
| The navigation resolves | ✅ | 🤷 |
| onResolved, if the transaction is still current | ✅ | ✅ |
| onRendered, if the transaction is still current | ✅ | ❌ |
| A pending fallback starts its pendingMinMs[9](#user-content-fn-pending) | ✅ | ❌ |

A superseded public navigate() can remain chained to the navigation that replaced it, so ack:false does not guarantee that the navigation resolves.

*Rendered* here means that React committed the tree and ran its layout effects. It does not necessarily mean that the browser painted it.

In the opening scenario, the user lands on /login, but four separate decisions produce that result. The /account loader continues because its preload still holds a lease. That same /account lane can no longer publish, because /settings took the transaction. The /settings lane sees an error, but its redirect starts a new /login navigation instead of producing UI. The framework then reports when /login actually commits.

navigate() can remain one promise because the router keeps these lifetimes separate. A lease says whether loader work is still needed. The current transaction says which navigation may publish. A private lane decides what one route attempt did. A receipt reports whether the framework rendered a publication.

```
await router.navigate({ to: '/account' })
```

---

Note

We have seen how the 4 main owners of a navigation work: transaction, lane, flight, render receipt. But the system has more complexity if you want to investigate further:

- The implementation also separates preflight planning, pending UI presentation, preload and cache entries, hydration handoff, development HMR rollback, server request cleanup, and stream ownership.
- During a background refresh of active routes, the router keeps the existing successful data visible while replacement data loads privately. It publishes the replacement only if the reload is still current and the committed route state it started from has not changed.
- Other features attach to those owners instead of creating new ones: lazy component readiness feeds into lane reduction, scroll restoration consumes rendered events, and view transitions wrap publication.

Those details are not needed to follow the client navigation above.[10](#user-content-fn-other-lifetimes)

---
