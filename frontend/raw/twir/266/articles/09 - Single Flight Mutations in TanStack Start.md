---
type: twir-item
issue: 266
item: 9
item_type: item
date: 2026-01-28
source: https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/
tags:
  - "TanStack"
  - "TanStackQuery"
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 9: Single Flight Mutations in TanStack Start

Source: [https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/](https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/)

Summary:
This blog post introduces the concept of "single flight mutations"—updating data and UI with a single network round trip—using TanStack Query, Router, and Start. It explains the inefficiencies of traditional mutation patterns and demonstrates a basic implementation where the server returns all necessary updated data after a mutation, reducing redundant client queries. The post sets the stage for more advanced middleware-based solutions in a follow-up.

Key takeaways:
- Single flight mutations minimize network round trips by returning all updated data in one server response.
- TanStack Query and Start can be leveraged to streamline data fetching and UI updates.
- The approach improves performance and consistency, especially for complex data dependencies.
- Part 1 covers fundamentals and a simple implementation; advanced patterns follow in part 2.

Recommendation:
Read fully (read fully if using TanStack Query/Start or optimizing mutation patterns)

Why it matters:
read fully if using TanStack Query/Start or optimizing mutation patterns

Content:
# Single Flight Mutations in TanStack Start: Part 1

A **“single flight mutation”** is a fancy way of saying: mutate the data *and* update the UI with just *one* round trip to the network.

The beautiful thing about implementing this with TanStack is that we can leverage the tools we already know, and love: [TanStack Query](https://tanstack.com/query/latest) (formerly react-query), [TanStack Router](https://tanstack.com/router/latest), and [TanStack Start](https://tanstack.com/start/latest).

If you’re not familiar with these tools, TanStack Router is a client-only SPA framework (see my [three-part introduction series](https://frontendmasters.com/blog/introducing-tanstack-router/)). TanStack Start is a server layer for Router that enables things like SSR, API routes, and server functions (see my [introduction for it](https://frontendmasters.com/blog/introducing-tanstack-start/) and [a post on its middleware feature](https://frontendmasters.com/blog/introducing-tanstack-start-middleware/)).

I’ve never written about TanStack Query, but it’s one of the most widely used React libraries, and there are tons of resources about it. One of the best would be [TkDodo’s blog](https://tkdodo.eu/blog/all). He’s the lead maintainer of TanStack Query, and his blog is superb.

In this first post, we’ll cover some fundamentals and then implement the simplest imaginable single flight mutation with a TanStack Start Server Function. In the next part, we’ll dive deep into middleware and implement a more serious solution, while having some fun with TypeScript in the process.

## Laying the Groundwork

In my [post on TanStack Start](https://frontendmasters.com/blog/introducing-tanstack-start/), I included this image, which is how client-driven single-page applications (SPAs) almost always behave.

The initial request for whatever URL you’re viewing returns an empty skeleton of a page. From there, more networks requests happen to fetch scripts and styles, and most likely some data, which eventually results in your actual content page being rendered.

The network round trips will almost always be the single most expensive thing your web application will do. To look at it another way, there are few things you can do to improve performance as much as *removing* network roundtrips. And this is why server-side rendering can be so beneficial: it allows us to display content to our users *immediately*, after the initial request is responded to.

I expressed this in the Start post with this image.

Those scripts and styles still have to load for your page to be interactive, but that initial response from the server can immediately display content for the user.

## Why Single Flight Mutations

Let’s think about how you’d normally update a piece of data in a web application.

You probably make a network request to some sort of `/update` endpoint, along with a post packet for whatever you’re trying to change. The endpoint will probably return a success flag, possibly with the actual piece of data you just updated. Your UI will usually then request updated data. You might think that returning the updated piece of data you just changed is all you’d need in order to update the UI, but frequently that’s not the case.

Imagine you’re looking at a list of TODO tasks, and you just edited one of them. Just updating the item on the screen isn’t good enough; maybe the edit causes this TODO to no longer even be in this list, depending on your filters. Or perhaps your edit causes this TODO to move to a different page in your results, based on your sort order. Or maybe you just *created* a *brand new* todo. In that case, who knows where, or even *if* this todo will show up in your list, again based on your filters and sorts.

So we re-fetch whatever query produces our list. It usually looks like this

This works, and if we’re honest with ourselves, it’s usually good enough. But can we do better? We wouldn’t be good engineers if we didn’t at least *try*. Conceptually we’d like to get something like this

We’ll implement a dead simple solution to this here in part 1, and then part 2 will discuss increasingly flexible ways of accomplishing it with middleware.

## Our App

As with prior posts about TanStack Start and Router, this post will use our cheap, simple, and frankly ugly Jira clone. [Here’s a repo for it](https://github.com/arackaf/tanstack-start-single-flight-mutations-blog-post). It’s a trivial app that runs on an SQLite database. The epics page looks like this:

As you can see, zero effort was put into the design. But there’s a few sources of data on the screen, which will help us implement single flight mutations: the main list of epics; the count of all epics (12) just above the list; and above that we have a summary list of epics, with the numbers of tasks therein.

This is the page we’ll be focusing on for this post. If you’re following along at home, you can run the app with `npm run dev` and then visit <http://localhost:3000/app/epics>.

Our queries for our list of epics and our summary data are driven by react-query. I’ve put the query options into helper utilities, like so.

```
export const epicsQueryOptions = (page: number) => {
  return queryOptions({
    queryKey: ["epics", "list", page],
    queryFn: async () => {
      const result = await getEpicsList({ data: page });
      return result;
    },
    staleTime: 1000 * 60 * 5,
    gcTime: 1000 * 60 * 5,
  });
};Code language: TypeScript (typescript)
```

This allows me to query data using the normal `useQuery` or `useSuspenseQuery` hook.

```
const { data: epicsData } = useSuspenseQuery(epicsQueryOptions(deferredPage));Code language: TypeScript (typescript)
```

And also prefetch these queries in TanStack loaders, without duplicating code.

```
  async loader({ context, deps }) {
    const queryClient = context.queryClient;

    queryClient.ensureQueryData(epicsQueryOptions(deps.page));
    queryClient.ensureQueryData(epicsCountQueryOptions());
  },Code language: TypeScript (typescript)
```

As you can see, this query (and all our other queries) are just straight calls to a single server function (`getEpicsList` in this case), with the result passed through. This is a key detail that will come in handy in part 2.

## Simplest Possible Single Flight Mutation

Let’s implement a dirt simple single flight mutation, and then iterate on it, to make it more and more scalable. Our main epics page has an edit button, which allows for inline editing.

When we hit save, let’s just refetch the list of epics, as well as the epics summary data inside the edit epic server function, and send those new data down to the client, so the client can update the UI.

Here’s the entire server function:

```
export const updateWithSimpleRefetch = createServerFn({ method: "POST" })
  .inputValidator((obj: { id: number; name: string }) => obj)
  .handler(async ({ data }) => {
    await new Promise(resolve => setTimeout(resolve, 1000 * Math.random()));
    await db.update(epicsTable).set({ name: data.name }).where(eq(epicsTable.id, data.id));

    const [epicsList, epicsSummaryData] = await Promise.all([getEpicsList({ data: 1 }), getEpicsSummary()]);

    return { epicsList, epicsSummaryData };
  });Code language: TypeScript (typescript)
```

We save our epic, and then fetch the updated data from the `getEpicsList`, and `getEpicsSummary` server functions, which we call in parallel with `Promise.all`. Note that a production-ready application would likely have some error handling.

Now when we call our server function, the data for those queries will be attached to the result. In fact, since we’re using server functions, these things will even be statically typed!

![Code snippet displaying a loop over result.epicsList with properties of each epic highlighted, showing 'id' and 'name' attributes.](https://i0.wp.com/frontendmasters.com/blog/wp-content/uploads/2026/01/img7.png?resize=1024%2C150&ssl=1)

## Updating the UI

With updated data for our queries coming back after the save, we can now insert it back into the UI. TanStack Query makes this simple. We need a reference to the QueryClient:

```
const queryClient = useQueryClient();Code language: TypeScript (typescript)
```

Then we can update the query payload for a given query with the `setQueryData` method. It takes the query key and the data.

```
const handleSaveSimple = async () => {
  const newValue = inputRef.current?.value || "";
  const result = await runSaveSimple({
    data: {
      id: epic.id,
      name: newValue,
    },
  });

  queryClient.setQueryData(["epics", "list", 1], result.epicsList);
  queryClient.setQueryData(["epics", "list", "summary"], result.epicsSummaryData);

  setIsEditing(false);
};Code language: TypeScript (typescript)
```

If hard-coding those query keys feels gross to you, don’t forget about those helper utilities we added before.

```
queryClient.setQueryData(epicsQueryOptions(1).queryKey, result.epicsList, { updatedAt: Date.now() });
queryClient.setQueryData(epicsSummaryQueryOptions().queryKey, result.epicsSummaryData, { updatedAt: Date.now() });Code language: TypeScript (typescript)
```

## Iterating

Our solution works, but it’s fragile. Our server function hard codes which data to fetch. What if our update function were to be called from different parts of the UI, which each needed different slices of data to be refetched? We certainly don’t want to redefine our server function N times, for each place it needs to be called.

Fortunately, TanStack has the perfect feature to help reduce this coupling: Middleware. We can remove the refetching from the server function, and move it to a reusable middleware which can be attached to server functions.

Related notes: [[TanStack Query]]
