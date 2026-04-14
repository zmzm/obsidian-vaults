---
type: twir-item
issue: 254
item: 3
item_type: item
date: 2025-10-15
source: https://tkdodo.eu/blog/context-inheritance-in-tan-stack-router
tags:
  - "TanStack"
  - "TanStackRouter"
status: auto
quality: keep
---

[[2025-10-15-TWIR-254|Index]]

# Item 3: Context Inheritance in TanStack Router

Source: [https://tkdodo.eu/blog/context-inheritance-in-tan-stack-router](https://tkdodo.eu/blog/context-inheritance-in-tan-stack-router)

Summary:
This article explores how TanStack Router enables type-safe context inheritance for route parameters, search params, and router context across nested routes. By defining parsing and validation at parent routes, all child routes automatically inherit accurate types and context, reducing boilerplate and improving type safety. The approach extends to dependency injection and allows dynamic modification of context at different levels in the route tree.

Key takeaways:
- Route params and search params are inherited and merged type-safely down the route tree.
- Context inheritance supports dependency injection (e.g., QueryClient) and can be modified at any route level.
- Reduces redundant parsing/validation and ensures accurate types for all nested routes.
- Enhances maintainability and developer experience in complex routing scenarios.

Recommendation:
Read fully (for those using or evaluating TanStack Router or advanced routing patterns)

Why it matters:
for those using or evaluating TanStack Router or advanced routing patterns

Content:
# Context Inheritance in TanStack Router

   Photo by [Janko Ferlič](https://unsplash.com/@itfeelslikefilm)

[TanStack Router (opens in a new window)](https://tanstack.com/router) has a lot of great features, so it’s hard to pick favorites. That said, there is one thing that blew my mind once I saw it in action, and that is how the router lets you accumulate state between nested routes - not just at runtime, but also on type-level.

This feature works in a type-safe and fully inferred way for all parent-child route relations, but let’s start with the most simple one where I think you’d be surprised if that didn’t work:

To show a quite minimal example, let’s just take two nested routes:

If we look at the child route (a widget on a dashboard), we can see that we get all params from our hierarchy back when calling `Route.useParams()`:

```
export const Route = createFileRoute(

'/dashboard/$dashboardId/widget/$widgetId/',

const params = Route.useParams()

//    ^? { dashboardId: string, widgetId: string }
```

This is literally what you’d expect from a type-safe router, after all, `$dashboardId` is right there in the path next to `$widgetId`, so why is this cool?

Well, what if we’d want to express that `$dashboardId` is a number? We would define that on the parent route by parsing the `params` with our favourite validation library:

```
import { type } from 'arktype'

export const Route = createFileRoute('/dashboard/$dashboardId')({

parse: type({ dashboardId: 'string.integer.parse' }).assert,
```

This change leads to something amazing: Every child route in the route tree now knows about this. [The docs (opens in a new window)](https://tanstack.com/router/latest/docs/framework/react/guide/path-params#path-params-can-be-used-by-child-routes) simply say that “once a path param has been parsed, it is available to all child routes”, but look what happens to our types:

```
const params = Route.useParams()

//    ^? { dashboardId: number, widgetId: string }
```

The `Widget` now knows that the `dashboardId` is a `number`. Just like that. It knows. 🤯

Let that sink in for a minute, because it has some cool implications. Because if we can define things on the parent and have the children know about their types for path params, what stops us from applying the same concept to other state our router manages?

Nothing stops us, that’s what. And in fact, there are a couple of other places where this inheritance works as well:

Yes, `searchParams` can inherit context on type-level from their parents, too. Let’s say we want to have an optional `?debug` boolean flag available everywhere in our app. All we need to do is define it on our root component with:

```
export const Route = createRootRouteWithContext<RouteContext>()({

validateSearch: type({ debug: 'boolean=false' }).assert,
```

and now any component will get access to that boolean flag via `useSearch`:

```
const search = Route.useSearch()
```

If we add more search params in our tree, they will be merged on type-level to produce the most accurate result. For example, our widget route might get a date range filter:

```
export const Route = createFileRoute(

'/dashboard/$dashboardId/widget/$widgetId/',

validateSearch: type({ 'range?': "'7d' | '30d' | '90d'" }).assert,

const search = Route.useSearch()

//    ^? { debug: boolean, range?: '7d' | '30d' | '90d' }
```

But if we used `useSearch` on the dashboard route, we would only get access to the `debug` flag. This merging is insanely powerful, because it makes sure that every component gains access to all the state available throughout its parent route hierarchy. All it needs to do is to declare which route is used on.

Another property of the Router that can do inheritance is the [Router Context (opens in a new window)](https://tanstack.com/router/latest/docs/framework/react/guide/router-context). This context is created at the root route if we use `createRootRouteWithContext`, and it’s initial values are passed to `createRouter` itself. It is generally used for dependency injection into route loaders. When used with TanStack Query, we usually use it to distribute the `QueryClient`:

```
const queryClient = new QueryClient()

const router = createRouter({

Wrap: ({ children }) => {

<QueryClientProvider client={queryClient}>
```

Then, this `queryClient` instance is available in all loaders:

```
export const Route = createFileRoute('/dashboard/$dashboardId')({

loader: async ({ context, params }) => {

//             ^? { queryClient: QueryClient }

await context.queryClient.ensureQueryData(

dashboardQueryOptions(params.dashboardId),

const params = Route.useParams()

const { data } = useSuspenseQuery(

dashboardQueryOptions(params.dashboardId),
```

This is great, but Route Context is more than just dependency injection. Again, the [docs state (opens in a new window)](https://tanstack.com/router/latest/docs/framework/react/guide/router-context#modifying-the-router-context) that “that you can modify the context at each route and the modifications will be available to all child routes.”

To modify the context for a specific route, we can define the `beforeLoad` function and return whatever we want:

```
export const Route = createFileRoute('/dashboard/$dashboardId')({

beforeLoad: () => ({ hello: 'world' }) as const,

loader: async ({ context, params }) => {

//                  queryClient: QueryClient;

//                  readonly hello: "world";

await context.queryClient.ensureQueryData(

dashboardQueryOptions(params.dashboardId),
```

Whatever we return will not only be available to this route’s loader, but also wherever we consume the context in child routes, for example, with `useRouteContext`:

```
const { hello } = Route.useRouteContext()
```

Okay, so the context can also evolve and inherit values from its parents, but where would that be useful? Of course we can use it for things like [building generic breadcrumbs (opens in a new window)](https://tanstack.com/router/latest/docs/framework/react/guide/router-context#processing-accumulated-route-context), but I think I’ve found a killer use-case for React Query as well that I will be writing about in the next blog post.

---

That’s it for today. Feel free to reach out to me on [bluesky (opens in a new window)](https://bsky.app/profile/tkdodo.eu)
if you have any questions, or just leave a comment below. ⬇️

Like the monospace font in the code blocks?

Check out [monolisa.dev](https://www.monolisa.dev/?ref=dominik)

 [![Bytes - the JavaScript Newsletter that doesn't suck](/.netlify/images?w=4096&h=256&fit=cover&url=%2Fblog%2F_astro%2Fbytes.PgTxoh9S.jpg)](https://bytes.dev/?r=dom)
