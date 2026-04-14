---
type: twir-item
issue: 257
item: 3
item_type: item
date: 2025-11-05
source: https://wyattjoh.ca/blog/partial-prerendering
tags:
  - "PPR"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-11-05-TWIR-257|Index]]

# Item 3: Partial Prerendering - From error-based detection to promise-driven architecture for optimal web performance

Source: [https://wyattjoh.ca/blog/partial-prerendering](https://wyattjoh.ca/blog/partial-prerendering)

Summary:
Next.js’s Partial Prerendering (PPR) optimizes web performance by serving static shells instantly while fetching dynamic content in parallel. The initial error-based detection for request data access caused developer friction and performance issues, leading to a new promise-based approach in Next.js 15. Now, request APIs (like cookies, headers) suspend prerendering via unresolved promises instead of errors, improving reliability and developer experience. This shift leverages React Server Components’ async capabilities and Node.js’s event loop for more predictable, performant builds.

Key takeaways:
- PPR balances static speed and dynamic flexibility by splitting rendering responsibilities.
- Error-based detection led to unreliable behavior and slow builds; promise-based detection is more robust.
- All request APIs in Next.js 15 are now async and suspend prerendering with unresolved promises.
- This change improves developer ergonomics and build performance, especially with React Server Components.

Recommendation:
Read fully (for those using or migrating to Next.js 14/15 or interested in advanced SSR strategies)

Why it matters:
for those using or migrating to Next.js 14/15 or interested in advanced SSR strategies

Content:
# How Partial Prerendering Works Under the Hood

At last yearâs Next.js Conf, we announced a new rendering paradigm, Partial Prerendering (or PPR). Building on Next.jsâs strong support for data and route caching, PPR optimizes the way Next.js serves static parts of a page quickly while still allowing server rendering of components that require access to request data.

Since announcing experimental support for the feature, weâve iterated on some of the core mechanisms that Next.js uses to detect request data access through a new experimental flag, `dynamicIO`.

## Understanding the Problem Space

Before diving into PPRâs implementation details, letâs establish why this feature matters. In modern web development, we face a fundamental tension between performance and functionality:

- **Static rendering** delivers content blazingly fast from the edge but lacks access to request-specific data
- **Dynamic rendering** provides full functionality but requires server computation, increasing time to first byte

This dichotomy forces developers into an all-or-nothing decision at the route level. Even accessing a single cookie marks an entire page as dynamic, sacrificing the performance benefits of static generation.

## Core Web Vitals: The North Star

PPRâs design centers around optimizing Core Web Vitals, particularly:

- **Time to First Byte (TTFB)**: How quickly the server responds with initial content
- **Largest Contentful Paint (LCP)**: When the main content becomes visible

The goal is sub-2.5-second LCP times, though ideally weâre targeting hundreds of milliseconds. PPR achieves this by serving static shells immediately while fetching dynamic content in parallel.

## Legacy Partial Prerendering

When we announced PPR in Next.js 14, it relied on throwing errors to signal to Next.js that request data was accessed. We assumed it would work as well as other APIs we have, such as `redirect()` and `notFound()`, which still use error throwing as a signal today. The issue arose for developers migrating existing applications who now had errors being thrown in unexpected places.

```
import { setTimeout } from "node:timers/promises"
import { cookies } from "next/headers"

async function getPosts() {
  for (let i = 0; i < 3; i++) {
    try {
      // In Next.js 14, this threw an error during
      // prerendering.
      const session = cookies().get("session")
      // ...
    } catch (err) {
      if (i === 2) {
        throw err
      }

      // Here we have a timeout added when a
      // fetch failed.
      await setTimeout(500 + i * 500)
    }
  }
}

export default async function Page() {
  const posts = await getPosts()

  // ...
}
```

This was a common pattern that we found even within popular database drivers handling unreliable backends. The retry loop with backoffs would eventually throw the error we used to signal request data access (`cookies()` in this case), but only after running through the set of timeouts, dramatically slowing down builds.

Additionally, we discovered cases where fallbacks were returned when operations failed or, worse, the error was shadowed:

```
async function checkAuthorization() {
  try {
    const session = cookies().get("session")
    // ...
  } catch (err) {
    throw new Error("AUTHORIZATION_CHECK_FAILED")
  }
}
```

In these cases, Next.js couldnât determine which components accessed request data, as it relied on the surrounding suspense boundary to catch the special error that was thrown.

We initially tried to solve this problem by introducing the `unstable_rethrow(err)` API:

```
import { unstable_rethrow } from "next/navigation"

async function checkAuthorization() {
  try {
    const session = cookies().get("session")
    // ...
  } catch (err) {
    unstable_rethrow(err)

    throw new Error("AUTHORIZATION_CHECK_FAILED")
  }
}
```

This would re-throw internal errors that Next.js uses for signaling. However, this introduced a new problem: it required developers to remember to add it. Every call site that could potentially generate a Next.js internal error would need this re-throw function inserted before any other throw in the application code. We felt this wasnât an acceptable developer experience.

We were left with two options. Since we could detect that request data was accessed, but not where, we could either mark the entire page as dynamic and provide a warning to developers, or rethink the detection mechanism. The first option wasnât ideal, as it might eliminate the entire static shell on revalidation, depending on the applicationâs logic. We decided on the latter approach.

## Modern Partial Prerendering

We needed a way to suspend the processing of user code when they tried to access request data. Errors were our first choice, but the problems with nested `try/catch` blocks meant that these signals that were meant to inform Next.js about request data being used would be unreliable, and possibly lead to longer than expected build times due to the retry logic.

But if we canât throw an error, then what primitives do we have left?

The answer? **Promises**.

Developers are already adept at managing Promises. With the advent of React Server Components, for the first time, users could write async components, allowing data fetching to be colocated, all while using the native APIs that they were already familiar with, such as fetch.

## The Promise-Based Approach

The key insight was to leverage JavaScriptâs inherent asynchronous behavior. Instead of throwing errors that could be caught and mishandled, we needed our request APIs to return promises that would never resolve during a static prerender. This approach provides several advantages:

```
// Before - synchronous with error throwing
function cookies() {
  if (isPrerendering) {
    throw new PostponeError("Cannot access cookies during prerendering")
  }
  return getCookies()
}

// After - asynchronous with promises
async function cookies() {
  if (isPrerendering) {
    // Return a promise that never resolves
    return new Promise(() => {})
  }
  return getCookies()
}
```

This shift required updating all request APIs to be asynchronous:

```
// Next.js 15 Request APIs
await cookies()
await headers()
await connection()  // replaces unstable_noStore()
```

## Leveraging the Node.js Event Loop

The real innovation comes from understanding how the Node.js event loop works. Node.js is single-threaded, meaning it can only run one block of synchronous code at a time. When it needs to perform I/O operations, it offloads them to native code.

Hereâs the crucial insight: **I/O thatâs non-deterministic canât complete in the same Task**.

Next.js takes advantage of this by using a clever scheduling mechanism:

```
import { prerender } from 'react-dom/static.edge'

const controller = new AbortController()
await { prelude, postponed } = new Promise((resolve, reject) => {
  let result
  setImmediate(() => {
    try {
      result = prerender(<App />, { signal: controller.signal })
      resolve(result)
    } catch (err) {
      reject(err)
    }
  })

  setImmediate(() => {
    controller.abort()
    resolve(result)
  })
})
```

This approach schedules a task to prerender the application, then immediately schedules another task to abort it. Node.js processes all microtasks (like resolving already-resolved promises) before moving to the next Task, allowing synchronous operations to complete while preventing asynchronous I/O from executing.

## The Prospective Render Strategy

One challenge remained: how to include external data in the static shell? Data from a CMS or database requires async fetches that wonât complete within a single event loop task.

The solution is the **prospective render**:

```
// Using Next.js cache APIs
async function getData() {
  'use cache'
  const res = await fetch('...')
  return res.json()
}

// Or with unstable_cache
const getData = unstable_cache(async () => {
  const res = await fetch('...')
  return res.json()
})
```

During build time, Next.js performs a prospective render to fill cache entries for any cacheable data. This renderâs output is discarded, but the caches are primed. When the actual prerender occurs, these cached values can be resolved synchronously within the first task, allowing them to be included in the static shell.

## Partially Static vs. Fully Static Pages

This leads to two categories of pages in PPR:

### Partially Static Pages

Pages that access uncached data or request information:

```
async function Page() {
  const data = await fetch('...') // No cache
  return (
    <Suspense fallback={<Skeleton />}>
      <Component data={data} />
    </Suspense>
  )
}
```

These require the resume render to stream in dynamic content.

### Fully Static Pages

Pages where all async operations are cached:

```
async function Page() {
  const data = await getData() // Cached
  return <Component data={data} />
}
```

These can be served entirely from the edge without any origin invocation.

## The Streaming Architecture

PPR uses a single HTTP response stream to deliver both static and dynamic content. This approach minimizes roundtrips and optimizes performance:

1. **Static shell streams immediately** from the edge
2. **Resume render starts concurrently** at the origin
3. **Dynamic content streams in** as it becomes ready
4. **Single response** contains everything

This timing is critical - while the browser downloads static resources (CSS, JS) hinted by the static shell, the server is already rendering dynamic content.

## Practical Implementation

Letâs examine how PPR works in practice with a real-world example:

```
import { Suspense } from "react"
import { cookies } from "next/headers"

async function getCart() {
  const jar = await cookies()
  // Fetch cart data based on session
  return fetchCartData(jar.get("session"))
}

async function Cart() {
  const cart = await getCart()
  return <CartDisplay items={cart.items} />
}

export default function Page() {
  return (
    <div>
      <Header /> {/* Static - included in shell */}

      <Suspense fallback={<CartSkeleton />}>
        <Cart /> {/* Dynamic - streamed later */}
      </Suspense>

      <ProductListing /> {/* Static - included in shell */}
    </div>
  )
}
```

In this example:

- `Header` and `ProductListing` are static and included in the initial shell
- `Cart` accesses cookies, making it dynamic
- The `CartSkeleton` is part of the static shell
- The actual cart content streams in once available

## Enabling Dynamic I/O

Currently, PPR requires two experimental flags:

```
// next.config.js
module.exports = {
  experimental: {
    ppr: true,
    dynamicIO: true
  }
}
```

The `dynamicIO` flag enables the promise-based detection mechanism. The plan is to eventually remove this flag as PPR stabilizes.

## Dynamic Path Parameters

A special consideration for pathname-based APIs: with traditional rendering, dynamic paths like `/products/[id]` would force the entire page to be dynamic. With PPR and async params:

```
type Props = {
  params: Promise<{ id: string }>
}

export default function Page({ params }: Props) {
  return (
    <Suspense fallback={<ProductDetailsSkeleton />}>
      <ProductDetails params={params} />
    </Suspense>
  )
}
```

This enables fallback static shells that work for any product ID, providing static-like performance even for dynamic routes.

## Performance Implications

The performance benefits of PPR are substantial:

- **Reduced TTFB**: Static shells serve immediately from edge locations
- **Improved LCP**: Critical content loads faster through parallel fetching
- **Better perceived performance**: Users see content immediately instead of waiting
- **Efficient caching**: Static portions cache effectively at CDN edge nodes

## Developer Experience Considerations

While PPR offers significant performance benefits, itâs important to understand its impact on development:

### Benefits

- No API changes required - existing Suspense boundaries just work
- Granular control over static/dynamic boundaries
- Automatic optimization without manual configuration

### Current Limitations

- Experimental status means potential breaking changes
- Requires careful Suspense boundary placement
- Debugging can be more complex with streaming responses
- Limited platform support outside Vercel and self-hosting

## Future Developments

### CDN Interoperability

Currently, the single-stream approach works on Vercel and self-hosted deployments, but broader CDN support is planned once PPR stabilizes. This will involve creating standardized protocols for CDNs to handle the static shell and dynamic streaming pattern.

### Production Readiness

While PPR represents a significant advancement, it remains experimental. The Next.js team is working towards:

- Removing the `dynamicIO` flag requirement
- Improving developer experience for larger codebases
- Expanding platform compatibility
- Stabilizing the API surface

## Conclusion

Partial Prerendering represents a paradigm shift in how we think about web application rendering. By combining static shells with streaming dynamic content, PPR offers:

- **Optimal TTFB** through edge-served static content
- **Improved LCP** via parallel data fetching
- **Better UX** with immediate static content display
- **Developer ergonomics** using familiar React patterns

The journey from error-based detection to promise-based mechanisms showcases the thoughtful evolution of this feature. While challenges remain around platform compatibility and production readiness, PPR represents the future of web application rendering - one where developers no longer need to choose between speed and functionality.

As we move forward, the goal is clear: make PPR the default rendering model for web applications, bringing together the best of static site generation and dynamic delivery without compromising on either. The technical foundations are solid, the performance benefits are clear, and the developer experience continues to improve with each iteration.

For teams looking to push the boundaries of web performance while maintaining rich, dynamic functionality, Partial Prerendering offers a compelling path forward. While it may still be experimental, the principles and patterns it introduces are already shaping how we think about modern web architecture.

Related notes: [[Server Components]]
