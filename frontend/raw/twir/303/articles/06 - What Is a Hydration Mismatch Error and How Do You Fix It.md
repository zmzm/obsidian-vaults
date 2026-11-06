---
type: twir-item
issue: 303
item: 6
item_type: item
date: 2026-10-28
source: https://www.gmoniava.com/blog/hydration-mismatch-errors-and-how-to-fix-them
tags:
status: auto
quality: keep
---

[[2026-10-28-TWIR-303|Index]]

# Item 6: What Is a Hydration Mismatch Error and How Do You Fix It?

Source: [https://www.gmoniava.com/blog/hydration-mismatch-errors-and-how-to-fix-them](https://www.gmoniava.com/blog/hydration-mismatch-errors-and-how-to-fix-them)

Summary:
This article explains hydration mismatch errors in React SSR apps, their causes (typically differences between server and client renders), and practical solutions. It covers common pitfalls like using client-only data (e.g., localStorage) during SSR, and provides patterns to avoid or mitigate mismatches, including deferring rendering until after mount and using suppressHydrationWarning. The trade-offs of each approach are discussed, with real-world examples.

Key takeaways:
- Hydration mismatches occur when server and client renders differ, often due to client-only state.
- Avoid using client-only APIs (like localStorage) during SSR or initial render.
- Solutions include deferring rendering, using useEffect, or suppressing warnings (with caveats).
- Each workaround has trade-offs, especially regarding SEO and initial content display.

Recommendation:
Read fully (essential for anyone building SSR React apps or troubleshooting hydration issues)

Why it matters:
essential for anyone building SSR React apps or troubleshooting hydration issues

Content:
# Fixing a Hydration Mismatch Error and UI Flicker in React

In React apps that use server-side rendering, you may encounter a hydration mismatch error.
Before explaining the error and the solutions, let's explain hydration first. We'll use Next.js as an example here.

In a Next.js app, when you visit a page built with Client Components using server-side rendering (SSR),
those components are pre-rendered on the server and the resulting HTML is sent to the client.
This HTML contains the content and structure of the page but without the JavaScript logic that makes it interactive;
the JavaScript required for Client Components is downloaded later.
The reason this is done is to give the user something meaningful to look at as quickly as possible. Once
this initial HTML arrives in the browser, Next.js runs JavaScript for the Client Components to make them
fully interactive - a process called hydration.

For Server Components, however, the story is different:
they are fully rendered on the server (using special data format) and their JavaScript is never sent to the client.

Hydration on the client mainly happens in two steps:

- React uses the same component tree that was used during SSR and renders it again
  on the client in memory (no DOM nodes are generated) and then checks that this output matches the HTML sent from the server.
  The reason why such a check is performed is explained in the [docs](https://react.dev/reference/react-dom/client/hydrateRoot):

  > This is important for the user experience. The user will spend some time looking at the server-generated HTML before your JavaScript code loads. Server rendering creates an illusion that the app loads faster by showing the HTML snapshot of its output. Suddenly showing different content breaks that illusion. This is why the server render output must match the initial render output on the client.
- React will make the HTML sent by the server interactive (e.g. attach event listeners).

A hydration mismatch error happens when the first step above is not satisfied:
the HTML produced on the server doesn’t match what React renders in memory on the client during hydration.

One of the reasons why such error may happen is if your rendering process
is based on information that is only available on the client side, such as local storage.
But there can also be other reasons. During SSR such client information is not available, so
the HTML produced on the server may differ from the in-memory render created during hydration on the client.

One common solution to this problem is to render nothing on the server and on the first client render,
then show the real content after the component mounts:

```
import { useState, useEffect } from 'react'

export default function SampleComponent() {
  const [isClient, setIsClient] = useState(false)

  useEffect(() => {
    setIsClient(true)
  }, [])

  if (!isClient) return null;

  return <h1>{new Date().toLocaleString()}</h1>
}
```

This works because `useEffect` only runs on the client. On the server
and during the initial client render, `isClient` is `false`,
so the component renders nothing in both cases. Because the server-rendered output and the initial
client-rendered output are identical, React can hydrate the component without a hydration mismatch.
However, this approach also prevents the component and all of its children (if there are any) from being server-rendered.
Such a trade-off can be problematic for components that have many
children or content important for SEO, as we'll see below with the layout that manages the sidebar state.

Another option is to add `suppressHydrationWarning` to the element where you expect a hydration mismatch.
However, this only suppresses the warning; it does not fix the underlying mismatch.
As the [React docs](https://react.dev/reference/react-dom/client/hydrateRoot#suppressing-unavoidable-hydration-mismatch-errors) for
`suppressHydrationWarning`  state:

> "This only works one level deep, and is intended to be an escape hatch. Don’t overuse it."

I encountered a hydration mismatch error while building a [full-stack movie app with Next.js and PostgreSQL](/blog/full-stack-movie-app).
In that app, I store whether the sidebar is open or closed in local storage
and use that state in components such as [`(main)/layout.tsx`](https://github.com/gmoniava/movie-app/blob/main/src/app/(main)/layout.tsx).
Since local storage is unavailable on the server, the server could render the sidebar closed,
while the first client render could use the saved state and render it open. The resulting difference
in the rendered HTML would cause a hydration mismatch.
For example, this was the approach I initially used:

```
export default function Layout() {
  // I don't recommend this approach. It can cause hydration errors.
  // Also IMHO reading localStorage here makes the initializer function impure.
  // Based on the docs, that function should be pure.
  const [showSidebar, setShowSidebar] = useState(() => {
    if (typeof window === "undefined") return false; // SSR fallback
    const stored = localStorage.getItem("movie-app-sidebar");
    return stored ? JSON.parse(stored) : false;
  });

  // ...
}
```

However, this approach had two issues:

- Hydration mismatch: as mentioned, during SSR, `showSidebar` would be `false`,
  and on the first render during hydration it could be `true`, which would
  result in different render output.
- Purity: According to the React docs, the `useState` initializer
  function should be a pure function and I am not sure if reading local
  storage inside it is considered pure.

Also I would not be able to fix the hydration error using the fix from the
previous section, which uses `useEffect` to render nothing until mounting,
because it would opt out children of layout from SSR too, which is
basically my whole app.

So I decided to use another approach, which was to read the value of the
sidebar from local storage in `useEffect` instead of `useState` initializer
function.
This does not cause hydration error because `useEffect` runs *after* hydration
and the initial `false` value is the same during SSR and the first render during hydration.

```
export default function Layout() {
  const [showSidebar, setShowSidebar] = useState(false);

  // Read localStorage after the component mounts
  useEffect(() => {
    const stored = localStorage.getItem("movie-app-sidebar");
    if (stored) {
      setShowSidebar(JSON.parse(stored));
    }
  }, []);

  // ...
}
```

However, this approach had another problem, it caused a brief "flicker" initially as the sidebar
state updated from closed to open after `useEffect` was run.

To avoid the "flicker", I used an inline script to apply the saved sidebar state directly to the DOM as the page loads,
without waiting for React to hydrate. The idea is to apply it early enough that the sidebar doesn’t
briefly appear open when the user left it closed, or vice versa. React then uses the same saved sidebar state
for its initial client render (so it matches the updated HTML and avoids a hydration mismatch).
This approach is based on this [post](https://ethanniser.dev/blog/a-clock-that-doesnt-snap).
Here are the main parts of the solution.

#### Apply the Saved State Before Hydration

The inline script reads local storage, updates the relevant classes, and saves the value
on `window` for React to read later.

```
function initializeSidebar() {
  const showSidebar = localStorage.getItem("movie-app-sidebar") === "true";

  const layout = document.querySelector("[data-layout]");
  const sidebar = document.querySelector("[data-sidebar]");

  if (layout && sidebar) {
    // Add each class when open; remove it when closed.
    layout.classList.toggle("sm:ml-64", showSidebar);
    sidebar.classList.toggle("left-0", showSidebar);
    sidebar.classList.toggle("opacity-100", showSidebar);
  }

  // Let React initialize with the same state.
  window._INITIAL_SIDEBAR_STATE_ = showSidebar;
}

function InlineScript() {
  return (
    <script
      dangerouslySetInnerHTML={{
        __html: `(${initializeSidebar.toString()})()`,
      }}
    />
  );
}
```

The `InlineScript` component is then rendered in `Layout`.

#### Use the Same State in React

In `Layout`, this is how we read the initial sidebar state now:

```
const [showSidebar, setShowSideBar] = React.useState(() => {
  // During server side rendering there is no window
  if (typeof window === "undefined") {
    return false;
  }

  // We stored the sidebar state in window._INITIAL_SIDEBAR_STATE_ because it is considered pure IMHO
  // to read from it here because window._INITIAL_SIDEBAR_STATE_ will not be modified after we read it
  // (see here also: https://gist.github.com/sebmarkbage/75f0838967cd003cd7f9ab938eb1958f#forbidden).
  // I am not sure if reading local storage instead here would also be considered pure.
  return window._INITIAL_SIDEBAR_STATE_;
});
```

React then uses `showSidebar` to decide whether to include `sm:ml-64` on the layout and `left-0` and
`opacity-100` on the sidebar, just as the inline script does, keeping its render output in sync with the updated DOM.

#### Another Issue: The Theme Toggle

I use [next-themes](https://github.com/pacocoursey/next-themes) to manage the app's theme.
The theme toggle had a similar issue: its checked state depends on the theme, which is not known on the server.
Here I kept the `useIsClient()` hook, which uses the same `useEffect` approach shown in `SampleComponent` at the
beginning of this post: rendering nothing until the component mounts,
as recommended by [next-themes](https://github.com/pacocoursey/next-themes#avoid-hydration-mismatch).

This is an acceptable trade-off for a small, isolated control because only the toggle is missing from the initial HTML,
while the rest of the page is still server-rendered. Using the same approach in `Layout` would also omit the page
content wrapped by that layout. The toggle appears slightly later, but that is acceptable here.

`next-themes` also helps prevent theme flickering by injecting a script near the beginning of the HTML document,
similar to the approach we used for the sidebar earlier in this post. Depending on the setup, the script adds a class
or data attribute to the `<html>` tag before hydration. Since this changes the server-rendered HTML, I added
`suppressHydrationWarning` to the `<html>` element, following the
[next-themes recommendation](https://github.com/pacocoursey/next-themes#with-app).

#### Another Issue: The Mobile Backdrop

The mobile sidebar also needed a dark backdrop. Conditionally rendering it based on the saved sidebar state could
cause the same hydration mismatch described earlier.

We could have used the `useIsClient` hook described earlier to avoid the hydration mismatch and added a separate class for the backdrop, which the inline script would also update. Instead, I decided to use CSS to make the backdrop follow the sidebar’s existing `left-0` class, which the inline script already updates.

To do this, the backdrop element stays in the HTML. Adding `group` to the sidebar
and `hidden group-[.left-0]:block` to the backdrop makes it appear when the sidebar has `left-0`. Appropriate responsive classes keep the backdrop hidden

This avoids a hydration mismatch because the backdrop and its `hidden group-[.left-0]:block` classes are always present.
These CSS classes control its visibility based on whether the sidebar has `left-0`.
The inline script and React already keep that sidebar class in sync, as described above.

You can find the rest of the implementation in [`(main)/layout.tsx`](https://github.com/gmoniava/movie-app/blob/main/src/app/(main)/layout.tsx).

### A Newer Alternative: `use(browser())`

[React 19.3](https://react.dev/blog/2026/09/09/react-19-3) introduced
[`browser`](https://react.dev/reference/react-dom/browser) from `react-dom`.
Calling `use(browser())` in a Client Component skips its server rendering and leaves the nearest
`<Suspense>` fallback in the initial HTML. This is an alternative to the earlier approach of using
`useEffect` to set `isClient` to `true` and rendering nothing until the component mounts.
My understanding is that using it in the layout would prevent the layout and its children from being server-rendered, just like the earlier `useEffect` approach.
