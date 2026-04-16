---
type: twir-item
issue: 274
item: 7
item_type: item
date: 2026-03-25
source: https://saschb2b.com/blog/use-hook-react
tags:
  - "useEffect"
status: auto
quality: keep
---

[[2026-03-25-TWIR-274|Index]]

# Item 7: use(): The Hook That Breaks the Rules (On Purpose)

Source: [https://saschb2b.com/blog/use-hook-react](https://saschb2b.com/blog/use-hook-react)

Summary:
React's new `use()` hook allows reading promises and context at render time, integrating directly with Suspense and error boundaries. It eliminates common useEffect anti-patterns for data fetching, enabling simpler, declarative components that focus on the "happy path." The hook can be called inside conditionals and loops, but requires Suspense boundaries to handle loading states.

Key takeaways:
- `use()` suspends components on unresolved promises, handled by Suspense.
- Simplifies data fetching logic—no more manual loading/error state management.
- Can be used inside conditionals and loops, breaking traditional hook rules.
- Requires careful boundary placement for correct error/loading handling.

Recommendation:
Read fully (read fully if you are adopting React 19 or want to modernize data fetching patterns)

Why it matters:
read fully if you are adopting React 19 or want to modernize data fetching patterns

Content:
# use(): The Hook That Breaks the Rules (On Purpose)

#### use(): The Hook That Breaks the Rules (On Purpose)

Every React developer has written this code:

```
```
const [data, setData] = useState<User | null>(null);

const [isLoading, setIsLoading] = useState(true);

const [error, setError] = useState<Error | null>(null);

useEffect(() => {

let cancelled = false;

setIsLoading(true);

fetchUser(id)

.then((user) => {

if (!cancelled) setData(user);

})

.catch((err) => {

if (!cancelled) setError(err);

})

.finally(() => {

if (!cancelled) setIsLoading(false);

});

return () => {

cancelled = true;

};

}, [id]);
```
```

Three state variables. A cleanup flag. A dependency array. A race condition you have to think about every single time. And this is the *correct* version: most codebases skip the `cancelled` flag and the error handling entirely.

This pattern is not wrong. It works. But it is boilerplate that exists because React had no built-in way to say "wait for this promise, then render." Every component that fetches data had to reinvent the same loading/error/data state machine from scratch.

React 19 introduced `use()` to fix this. It is the first hook that can be called inside conditionals and loops, it integrates directly with Suspense, and it turns the fetch-then-setState pattern into a single line.

`use()` reads a value from a resource at render time. The resource can be a **Promise** or a **Context**.

```
```
import { use } from "react";

const user = use(userPromise);

const theme = use(ThemeContext);
```
```

That is the entire API. One function, two use cases.

When you pass a Promise, `use()` integrates with the nearest `<Suspense>` boundary. While the promise is pending, the component *suspends*. React shows the Suspense fallback. When it resolves, React re-renders with the resolved value. When it rejects, the nearest Error Boundary catches the error.

No `useState`. No `useEffect`. No `isLoading`. No `setData`. React handles all of it.

Wrap the snippet from above into a component and add the obligatory loading/error guards:

```
```
function UserProfile({ userId }: { userId: string }) {

const [user, setUser] = useState<User | null>(null);

const [isLoading, setIsLoading] = useState(true);

const [error, setError] = useState<Error | null>(null);

useEffect(() => {

}, [userId]);

if (isLoading) return <Skeleton />;

if (error) return <ErrorMessage error={error} />;

if (!user) return null;

return <ProfileCard user={user} />;

}
```
```

Three state declarations, one effect, three conditional returns: all before you reach the actual UI. Every component that fetches data repeats this structure.

Here is the same component with `use()`:

```
```
"use client";

import { use } from "react";

function UserProfile({ userPromise }: { userPromise: Promise<User> }) {

const user = use(userPromise);

return <ProfileCard user={user} />;

}
```
```

```
```
import { Suspense } from "react";

import { ErrorBoundary } from "react-error-boundary";

export default function UserPage({ params }: { params: { id: string } }) {

const userPromise = fetchUser(params.id);

return (

<ErrorBoundary fallback={<ErrorMessage />}>

<Suspense fallback={<Skeleton />}>

<UserProfile userPromise={userPromise} />

</Suspense>

</ErrorBoundary>

);

}
```
```

The loading state is handled by `<Suspense>`. The error state is handled by `<ErrorBoundary>` (from the [`react-error-boundary`](https://www.npmjs.com/package/react-error-boundary) package). The component itself only contains the happy path - the code that runs when data is available. The state machine has been moved from your code into React's runtime.

Because `UserPage` is a Server Component, it does not re-render. The promise reference is created once and passed down as a stable prop, no caching gymnastics needed.

Notice how the component that *uses* the data (`UserProfile`) is separated
from the component that *initiates* the fetch and *defines* the loading/error
UI (`UserPage`). This is intentional. The consumer doesn't know where the
promise came from or what to show while waiting.

`use()` does not work in isolation. It is one piece of a three-part architecture:

1. **`use(promise)`**: suspends the component while the promise is pending.
2. **`<Suspense fallback={...}>`**: catches the suspension and shows a fallback UI.
3. **`<ErrorBoundary fallback={...}>`**: catches rejected promises and shows an error UI.

Without a Suspense boundary above it, a component that calls `use()` with a pending promise will crash. The boundary is not optional.

```
```
<ErrorBoundary fallback={<p>Something went wrong.</p>}>

<Suspense fallback={<p>Loading...</p>}>

<UserProfile userPromise={userPromise} />

</Suspense>

</ErrorBoundary>
```
```

You can nest Suspense boundaries to create staged loading sequences:

```
```
<Suspense fallback={<PageSkeleton />}>

<Header userPromise={userPromise} />

<Suspense fallback={<FeedSkeleton />}>

<Feed postsPromise={postsPromise} />

</Suspense>

</Suspense>
```
```

If `Header` resolves before `Feed`, the header appears immediately while the feed still shows its skeleton. Each boundary controls a different loading zone. This is declarative loading orchestration, you describe the structure, not the timing.

##### Revealing Content Together

All children inside a single Suspense boundary are treated as a unit. If any child suspends, the *entire* boundary shows its fallback. This is useful when you want multiple pieces of data to appear at the same time:

```
```
<Suspense fallback={<DashboardSkeleton />}>

<Stats statsPromise={statsPromise} />

<Chart chartPromise={chartPromise} />

<RecentActivity activityPromise={activityPromise} />

</Suspense>
```
```

All three components will "pop in" together once every promise has resolved. No partial states, no layout shift.

This is where most tutorials stop. But if you try to use `use()` with a promise created *inside* a Client Component, you will hit a subtle and frustrating bug.

```
```
function UserProfile({ userId }: { userId: string }) {

const user = use(fetchUser(userId));

return <ProfileCard user={user} />;

}
```
```

`fetchUser(userId)` returns a *new* Promise object on every render. React sees a new promise, suspends again, the component re-renders, creates another new promise, suspends again, infinite loop.

use() does not fetch data. It reads a promise. The promise must have a
**stable identity** across renders. If you create a new promise on every
render, you get an infinite suspension loop.

##### How to Stabilize the Promise

There are several approaches, each suited to a different architecture:

**1. Create the promise in a parent component or Server Component**

This is the recommended pattern. The parent creates the promise once and passes it down as a prop:

```
```
export default function UserPage({ params }: { params: { id: string } }) {

const userPromise = fetchUser(params.id);

return (

<Suspense fallback={<Skeleton />}>

<UserProfile userPromise={userPromise} />

</Suspense>

);

}
```
```

No `async`/`await` needed, the promise is passed down *unresolved*. The Client Component unwraps it with `use()`. Server Components don't re-render, so the promise reference is inherently stable.

**2. Use a module-level cache**

For Client Components that need to initiate fetches, cache the promise so the same reference is returned on subsequent calls:

```
```
const cache = new Map<string, Promise<User>>();

function fetchUserCached(id: string): Promise<User> {

if (!cache.has(id)) {

cache.set(id, fetchUser(id));

}

return cache.get(id)!;

}

function UserProfile({ userId }: { userId: string }) {

const user = use(fetchUserCached(userId));

return <ProfileCard user={user} />;

}
```
```

Same arguments produce the same promise reference. No infinite loop.

Avoid async in Cache Wrappers

Do not mark your cache function as `async`. The `async` keyword *always*
creates a new promise, even if you return a cached value. Use a synchronous
function that stores and returns the original promise object.

**3. Use a data fetching library**

Libraries like [TanStack Query](https://tanstack.com/query/latest) or [SWR](https://swr.vercel.app/) handle caching, deduplication, and revalidation out of the box. They predate `use()` and solve a much broader problem - but they also add ~13kB gzipped and a provider wrapper. For a simple "fetch once, display result" pattern, `use()` with a 5-line cache function (option 2 above) does the job without the extra dependency. The library earns its keep when your UI has **long-lived client state that needs to stay fresh**: think dashboards that refetch on tab focus, lists with pagination, or mutations that should optimistically update related queries.

**4. Use React's `cache()` in Server Components**

React provides a built-in [`cache()`](https://react.dev/reference/react/cache) function for Server Components. It memoizes a function's return value for the lifetime of a single server request:

```
```
import { cache } from "react";

const getUser = cache(async (id: string): Promise<User> => {

const res = await fetch(`/api/users/${id}`);

return res.json();

});
```
```

Multiple components calling `getUser("123")` during the same server render will share one fetch. The cache is scoped to the request, it resets on every new page load.

Both memoize. But `cache()` works across components in a server render
(deduplication), while `useMemo` works within a single component across
re-renders. `cache()` is for data fetching. `useMemo` is for computations.
Different tools, different jobs.

`use()` can also read Context, and this is where it breaks a rule that every other hook follows.

Every React hook must be called at the top level of a component, never inside conditions, loops, or early returns. `use()` is the exception. It can be called conditionally:

```
```
function Greeting({ showFormal }: { showFormal: boolean }) {

if (showFormal) {

const { locale } = use(I18nContext);

return <p>{locale === "de" ? "Guten Tag" : "Good day"}</p>;

}

return <p>Hey!</p>;

}
```
```

With `useContext`, this code would violate the rules of hooks. With `use()`, it is valid. React's linter knows about this exception.

The landscape of data fetching in React has more options than ever. Here is when each one is the right choice:

| Scenario | Approach |
| --- | --- |
| Server Component fetching data | `async`/`await` directly in the component |
| Passing async data from Server to Client Component | Create promise on server, `use()` on client with Suspense |
| Simple client-side fetch (popup, dialog, one-off display) | `use()` with a cached promise + Suspense |
| Complex client state (auto-refetch, pagination, mutations) | [TanStack Query](https://tanstack.com/query/latest) or [SWR](https://swr.vercel.app/) |
| Computed/derived state from props or other state | `useMemo` or direct calculation during render |
| Reading context conditionally | `use(SomeContext)` |
| Reading context unconditionally | `useContext(SomeContext)`: simpler, more familiar |
| Subscribing to an external store (Redux, Zustand, browser API) | `useSyncExternalStore` |
| DOM measurements, event listeners, timers | `useEffect`: this is what it's actually for |

The Litmus Test for useEffect

If your `useEffect` is fetching data and calling `setState` with the result,
it is almost certainly doing work that belongs in a Server Component, a data
library, or `use()` + Suspense. If your `useEffect` is adding an event
listener, starting a timer, or measuring the DOM, that is an actual side
effect, and `useEffect` is the right tool.

#### Migrating Away from useEffect + setState

If you have an existing codebase full of the useEffect-fetch-setState pattern, you don't need to rewrite everything at once. Here is a practical migration path:

Before changing the data fetching mechanism, encapsulate the existing pattern:

```
```
function useUser(id: string) {

const [user, setUser] = useState<User | null>(null);

const [isLoading, setIsLoading] = useState(true);

const [error, setError] = useState<Error | null>(null);

useEffect(() => {

let cancelled = false;

setIsLoading(true);

fetchUser(id)

.then((data) => {

if (!cancelled) setUser(data);

})

.catch((err) => {

if (!cancelled) setError(err);

})

.finally(() => {

if (!cancelled) setIsLoading(false);

});

return () => {

cancelled = true;

};

}, [id]);

return { user, isLoading, error };

}
```
```

This doesn't change the mechanism, but it gives you a single place to swap the implementation later.

##### Step 2: Add Suspense Boundaries

Wrap the consuming components in Suspense and Error Boundaries. This is safe even before switching to `use()`: the boundaries just don't trigger yet:

```
```
<ErrorBoundary fallback={<ErrorMessage />}>

<Suspense fallback={<Skeleton />}>

<UserProfile userId={userId} />

</Suspense>

</ErrorBoundary>
```
```

##### Step 3: Swap the Internals

Now change the custom hook (or the component) to accept a promise and use `use()`. The consuming components don't change, they already have Suspense boundaries:

```
```
function UserProfile({ userPromise }: { userPromise: Promise<User> }) {

const user = use(userPromise);

return <ProfileCard user={user} />;

}
```
```

The old `useUser` hook can be deleted. The three state variables, the effect, and the cleanup flag are gone. The boundary handles loading and errors.

##### Step 4: Move the Fetch Up

Push promise creation to Server Components or to a caching layer. This is the real architectural shift, data initiation moves from the component that needs it to the component (or server) that can create a stable reference.

##### use() Can Be Called Conditionally

Unlike every other hook, `use()` works inside `if`, `for`, and after early returns. React's linter is aware of this exception.

##### use() Cannot Be Called in try-catch

Rejected promises are caught by Error Boundaries, not by try-catch blocks. If you wrap `use()` in a try-catch, React throws a "Suspense Exception" error.

```
```
try {

const data = use(promise);

} catch (e) {

}
```
```

If you need to provide a fallback value for a rejected promise, use `.catch()` on the promise itself:

```
```
const safePromise = riskyFetch().catch(() => defaultValue);

const data = use(safePromise);
```
```

##### Resolved Values Must Be Serializable (Server to Client)

When passing a promise from a Server Component to a Client Component, the resolved value must be serializable, no functions, no class instances, no symbols. Primitives, plain objects, and arrays are fine.

##### Don't Mix Patterns for the Same Data

If you read a promise with `use()`, don't also fetch the same data in a `useEffect`. Pick one source of truth for each piece of data.

Here is a realistic example, a dashboard that loads a user profile and their recent orders in parallel, with staged loading:

```
```
import { Suspense } from "react";

import { ErrorBoundary } from "react-error-boundary";

import { fetchUser, fetchOrders } from "@/lib/api";

import { Dashboard } from "./Dashboard";

export default function DashboardPage({ params }: { params: { id: string } }) {

const userPromise = fetchUser(params.id);

const ordersPromise = fetchOrders(params.id);

return (

<ErrorBoundary fallback={<p>Something went wrong.</p>}>

<Suspense fallback={<HeaderSkeleton />}>

<Dashboard userPromise={userPromise} ordersPromise={ordersPromise} />

</Suspense>

</ErrorBoundary>

);

}
```
```

```
```
"use client";

import { use, Suspense } from "react";

export function Dashboard({

userPromise,

ordersPromise,

}: {

userPromise: Promise<User>;

ordersPromise: Promise<Order[]>;

}) {

const user = use(userPromise);

return (

<div>

<h1>Welcome back, {user.name}</h1>

<Suspense fallback={<OrdersSkeleton />}>

<OrderList ordersPromise={ordersPromise} />

</Suspense>

</div>

);

}

function OrderList({ ordersPromise }: { ordersPromise: Promise<Order[]> }) {

const orders = use(ordersPromise);

if (orders.length === 0) return <p>No recent orders.</p>;

return (

<ul>

{orders.map((order) => (

<li key={order.id}>

{order.item} – {order.status}

</li>

))}

</ul>

);

}
```
```

The flow below shows the exact sequence, what renders when, and what the user sees at each stage:

The key takeaway: `use()` never returns an undefined or pending value. By the time `user.name` executes, the promise has resolved. While it's pending, the component simply doesn't render, the nearest Suspense boundary shows its fallback instead.

#### What About Client-Side Fetching?

All examples so far start the fetch in a Server Component and pass the promise down. But what if you're already deep inside a client component, say a button opens a popup that needs fresh data?

You can't render a Server Component inside a Client Component. But `use()` + Suspense still works, you just have to manage promise identity yourself.

##### Start the Fetch in the Event Handler

The most straightforward approach: create the promise in the click handler, store it in state, and let `use()` read it.

```
```
"use client";

function DetailPopup({ dataPromise }: { dataPromise: Promise<ItemDetail> }) {

const detail = use(dataPromise);

return <div>{detail.description}</div>;

}

function ItemCard({ itemId }: { itemId: string }) {

const [promise, setPromise] = useState<Promise<ItemDetail> | null>(null);

const handleOpen = () => {

setPromise(fetchItemDetail(itemId));

};

return (

<>

<button onClick={handleOpen}>Show Details</button>

{promise && (

<Suspense fallback={<Skeleton />}>

<DetailPopup dataPromise={promise} />

</Suspense>

)}

</>

);

}
```
```

This is responsive, the fetch fires the instant the user clicks, not after React schedules a render. Each click creates a new promise, so you always get fresh data.

##### Use a Module-Level Cache for Repeated Access

If the same popup might be opened multiple times with the same ID, a cache avoids redundant requests:

```
```
const cache = new Map<string, Promise<ItemDetail>>();

export function getItemDetail(id: string) {

if (!cache.has(id)) {

cache.set(

id,

fetch(`/api/items/${id}`).then((r) => r.json()),

);

}

return cache.get(id)!;

}
```
```

```
```
const handleOpen = () => {

setPromise(getItemDetail(itemId));

};
```
```

This is exactly the same caching pattern from the section above, it works
identically whether the promise is created in a Server Component or a click
handler. What matters is that `use()` always receives the **same** promise
object for the same request.

##### When Is `use()` Enough, and When Do You Need More?

For the popup scenario above, user clicks, data loads, popup displays it. `use()` with a simple cache function is all you need. No extra dependency, no provider, no configuration. The 5-line `Map` cache from above handles deduplication just fine.

Consider TanStack Query or SWR when the data has a **lifecycle beyond a single display**:

- The same data is shown in multiple places and a mutation in one place should update all of them
- Data goes stale and should silently refetch when the user returns to the tab
- You need paginated or infinite-scroll lists with cursor tracking
- You want optimistic UI that rolls back on server error

If none of those apply, `use()` + a cache function is the simpler choice. You can always add a library later when the caching requirements grow, the mental model (promise in, data out, Suspense handles the wait) stays the same.

- [use: React Reference

  The official React documentation for the use() hook. API reference, rules, caveats, and examples with both Promises and Context.](https://react.dev/reference/react/use)
- [Suspense: React Reference

  How Suspense boundaries work, nested boundaries, staged loading, and integration with streaming server rendering.](https://react.dev/reference/react/Suspense)
- [You Might Not Need an Effect: React Docs

  React's official guide on avoiding unnecessary useEffect calls, essential reading for understanding when use() or useMemo is the better choice.](https://react.dev/learn/you-might-not-need-an-effect)
- [cache: React Reference

  React's built-in cache() function for deduplicating data fetches across Server Components within a single request.](https://react.dev/reference/react/cache)
- [TanStack Query

  The most popular client-side data fetching library for React, handles caching, background refetching, pagination, and optimistic updates.](https://tanstack.com/query/latest)
- [React Has Changed, Your Hooks Should Too: Matt Smith

  A practical overview of how React 18/19 changes the way developers should think about hooks, effects, and data fetching architecture.](https://allthingssmitty.com/2025/12/01/react-has-changed-your-hooks-should-too/)
