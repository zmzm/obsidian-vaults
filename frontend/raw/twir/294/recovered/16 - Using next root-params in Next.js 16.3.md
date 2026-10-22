---
type: "twir-recovery"
issue: 294
item: 16
source: "https://next-intl.dev/blog/nextjs-root-params"
final_url: "https://next-intl.dev/blog/nextjs-root-params"
retrieved: "2026-10-22T11:30:07+00:00"
original_note: "frontend/raw/twir/294/articles/16 - Using next root-params in Next.js 16.3.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/16 - Using next root-params in Next.js 16.3|Using next/root-params in Next.js 16.3]]

# Using next/root-params in Next.js 16.3

# Using `next/root-params` in Next.js 16.3

Aug 4, 2026 · by Jan Amann

Next.js v16.3 was just released and comes with a new feature: `next/root-params`.

This new API fills in the that allows apps that use top-level dynamic segments like `[locale]` to read segment values deeply in Server Components:

This addition is a game-changer for `next-intl`.

While the library previously relied on workarounds to provide a locale to Server Components, this API now provides native support in Next.js for this use case, allowing the library to integrate much tighter with Next.js.

Practically, for users of `next-intl` this means:

1. Being able to support static rendering of apps with locale-based routing without `setRequestLocale`
2. Improved integration with Next.js cache mechanisms like `cacheComponents`

But first, let’s have a look at how this API works in practice.

## Introduction to root layouts

Previously, Next.js required a to be present at `app/layout.tsx`—the root of your app.

Now, you can move a root layout to a nested segment, even if it’s a dynamic one:

In this extended definition, a root layout now is any layout that has **no other layouts located above it**.

In contrast, layouts that do have other layout ancestors are regular layouts:

With the addition of `next/root-params`, you can now read param values of a root layout in all Server Components that render within it:

## Multiple root layouts

Here’s where it gets interesting: With , you can provide another layout for pages that are not located in the `[locale]` segment:

The layout at `[locale]/layout.tsx` as well as the layout at `(unlocalized)/layout.tsx` both have no other layouts located above them, therefore *both* qualify as root layouts.

Due to this, in this case the returned value of `next/root-params` will depend on where the component that calls the function is being rendered from.

If you call `next/root-params` in shared code that is used by both layouts, this allows for a pattern like this:

With this, you can use the `getLocale` function across your codebase to read the current locale without having to worry about where it’s being called from.

In an internationalized app, this can for example be useful to implement a country selection page at the root where you have to rely on a default locale. Once the user is within the `[locale]` segment, this param value can be used instead for localizing page content.

## Static rendering

In case we know the values for the `[locale]` segment ahead of time, we can provide them to Next.js by using the function to enable static rendering:

Note that doesn’t work with Cache Components, therefore if you want to treat your `locales` array as exhaustive, you might be better off adding runtime validation for the `[locale]` segment and call `notFound()` to guard against unknown locales (see below).

## Leveraging `next/root-params` in `next-intl`

So, how can you use this in `next-intl`?

Similarly to how we’ve defined the `getLocale` function above, we do in fact already have a central place that is called by all server-side functions that require the current locale of the user: .

So let’s use `next/root-params` here:

That’s it—with a single change to `i18n/request.ts` you can start using `next/root-params`!

---

**One caveat though**: `next/root-params` currently doesn’t work in Route Handlers or Server Actions. Next.js for these in a future release.

You can work around that though by passing an explicit `locale` param at call sites, e.g. via :

… and then incorporate the override in `getRequestConfig`:

## Time for spring cleaning

With this change, you can now simplify your codebase in various ways:

### Remove a pass-through root layout

For certain patterns like global 404 pages, you might have used a pass-through root layout so far:

This needs to be removed now as otherwise this will qualify as a root layout instead of the one defined at `src/app/[locale]/layout.tsx`.

Instead, you can use for this now.

### Avoid reading the `[locale]` segment

Since `next-intl` provides the current locale via , you can seamlessly read the locale from these APIs instead of `params` now:

If you’ve augmented the you’ll now also benefit from type safety here:

Behind the scenes, if you call `useLocale` or `getLocale` in a Server Component, your `i18n/request.ts` config will be consulted, potentially using a fallback that you have defined.

### Remove manual locale overrides

If you’re using async APIs like `getTranslations`, you might have previously passed the locale manually, typically to enable static rendering in the Metadata API.

Now, you can remove this and rely on the locale that is returned from `i18n/request.ts`:

The cases where you still require a locale override are:

1. When you’re using functions from `next-intl` in **Route Handlers** or **Server Actions**, which `next/root-params` doesn’t support yet
2. If your UI renders messages from **multiple locales** in parallel (uncommon)

### Static rendering

If you’ve previously used `setRequestLocale` to enable static rendering, you can now remove it:

Note that `generateStaticParams` is naturally still required though.

### Custom routing setups

`next-intl` provides mechanisms like (and esp. ) that allow you to customize your . However, some apps might require further customization that goes beyond the capabilities that `next-intl` provides out of the box.

With the introduction of `next/root-params`, it’s now easier than ever to implement custom routing setups, while still being able to use core functionality from `next-intl` like `useTranslations`.

**Example:**

In this case, you can consider implementing your own and , if relevant.

## Try `next/root-params` today!

If you’re giving `next/root-params` a go with `next-intl`, let me know how it works for you by joining the discussion here: .

I’m curious to hear how it simplifies your codebase!

—Jan

[![Video preview](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fthumb.06bfa870.jpg&w=384&q=75)](https://learn.next-intl.dev)

### Want to ship a real-world app with next/root-params?

Master the art of holistic internationalization, from the fundamentals to advanced patterns, all through a real-world project.

[Get started→](https://learn.next-intl.dev)
