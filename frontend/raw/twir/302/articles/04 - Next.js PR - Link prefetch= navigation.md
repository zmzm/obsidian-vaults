---
type: twir-item
issue: 302
item: 4
item_type: item
date: 2026-10-21
source: https://github.com/vercel/next.js/pull/99871
tags:
  - "Nextjs"
  - "Navigation"
  - "PR"
status: auto
quality: keep
---

[[2026-10-21-TWIR-302|Index]]

# Item 4: Next.js PR - <Link prefetch="navigation">

Source: [https://github.com/vercel/next.js/pull/99871](https://github.com/vercel/next.js/pull/99871)

Summary:
This Next.js pull request introduces new options for the <Link> component's prefetch prop: "shell", "prefetch", and "navigation". The "navigation" option allows developers to prefetch content up to the navigation stage, enabling more complete prefetching for links likely to be clicked. The changes align with the partial prefetching model introduced in Next.js 16.4, providing finer control over what is prefetched and when.

Key takeaways:
- Adds "shell", "prefetch", and "navigation" options to <Link prefetch>.
- "navigation" enables full prefetching up to the navigation stage for high-confidence links.
- Matches conceptual stages of Next.js navigation and prefetch APIs.
- Improves cache utilization and user experience for anticipated navigations.

Recommendation:
Read fully (if you use Next.js and want to optimize navigation/prefetching)

Why it matters:
if you use Next.js and want to optimize navigation/prefetching

Content:
# Add <Link prefetch="navigation"> by acdlite · Pull Request #99871 · vercel/next.js · GitHub

```
The server ignored cookie and header reads that happen after navigation(),
because a runtime prefetch of the prefetch stage wouldn't include that
content either. But a link that needs the navigation stage would, and the
client couldn't tell it needed one. The server now counts those reads, and
marks where the prefetch stage ends so the client can check that stage on
its own. A static prefetch that's complete through the prefetch stage, but
not past it, is recorded that way: links that only need the prefetch stage
still stop there, and links that need the navigation stage send a runtime
request.
```

```
The values of the next-router-prefetch header were string literals at every
site that sends or reads them, so nothing tied a '2' on the client to the
'2' on the server. They're now named constants, and the server reads a
runtime prefetch's requested stage as one value instead of a flag per kind.
```

```
A link could ask to be prefetched up to the shell (the default) or up to
where prefetch() resolves (prefetch={true}). There was no way to ask for
everything a navigation would render, up to where navigation() resolves.
That's useful for links that are very likely to be clicked, where it's worth
paying for a more complete prefetch.

prefetch="navigation" asks for that stage, and prefetch="prefetch" is a
spelling of prefetch={true} that matches it. router.prefetch can ask for it
too. With Partial Prefetching, the router fills the cache until it's complete
up to the navigation stage, using a new runtime prefetch request that renders
that far. Without Partial Prefetching, it does what prefetch={true} does.

unstable_dynamicOnHover already asked for the navigation stage on hover, so
on Partial Prefetching routes it now gets this prefetch too.
```

```
trackRuntimeDataAccessed cast the current render stage to one of the three
static stages, trusting that a static prerender never reaches the
validation-only stages. It now checks the stage instead, and reports an
unexpected one the same way it already did for the Before stage and the
runtime stages.

The scheduler's check for whether a shell entry is worth a static request
always looked at the prefetch stage's hint, even on a walk to the navigation
stage. It now looks at the walk's own stage, like every other static-request
check. This doesn't change which requests are sent today, because a walk whose
stage can't be prefetched statically switches to a runtime request before it
gets that far.
```
