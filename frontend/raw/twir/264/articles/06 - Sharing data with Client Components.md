---
type: twir-item
issue: 264
item: 6
item_type: item
date: 2026-01-14
source: https://next-16-recipes.vercel.app/sharing-data-with-client-components
tags:
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-01-14-TWIR-264|Index]]

# Item 6: Sharing data with Client Components

Source: [https://next-16-recipes.vercel.app/sharing-data-with-client-components](https://next-16-recipes.vercel.app/sharing-data-with-client-components)

Summary:
This guide explains how to share server-fetched data (like the current user) with client components in Next.js, avoiding prop drilling and blocking renders. It shows how to use React’s cache function on the server and Context on the client, passing promises to enable non-blocking, Suspense-friendly data access throughout the client tree. The pattern allows for efficient, scalable data sharing without unnecessary network roundtrips.

Key takeaways:
- Server Components can fetch data and pass it to Client Components via props and Context.
- Passing unresolved promises to Context enables Suspense to handle loading states without blocking the whole app.
- React’s cache function ensures server-side data is only fetched once per request.
- This approach solves prop drilling and improves initial render performance in Next.js apps.

Recommendation:
Read fully (for anyone working with Next.js or hybrid server/client data flows)

Why it matters:
for anyone working with Next.js or hybrid server/client data flows

Content:
# Sharing data with Client Components

A common pattern in client-side React apps is to fetch some shared data, like the current user, and make it available to the rest of the tree using a Context provider:

```
function Layout({ children }) {
  return <AuthProvider>{children}</AuthProvider>;
}

// Somewhere deep in the client tree...
function Menu() {
  const currentUser = useCurrentUser();

  return <p>Hello, {currentUser.name}!</p>;
}
```

This helps you avoid ["prop drilling"](https://react.dev/learn/passing-data-deeply-with-context#the-problem-with-passing-props), a situation where lots of intermediate components end up passing data down the tree *solely* to get it to the deeper components that need it.

In Next.js, most of your data fetching happens in Server Components. And since Server Components don't support Context, you might be wondering how to address the problem of prop drilling within your Next app's component tree.

## React cache

First, while Server Components don't support Context, they do support React's [cache](https://react.dev/reference/react/cache) function, which helps you avoid prop drilling for deeply nested Server Components:

```
// lib/auth.ts
import { cache } from "react";

// 🟢 Cache the function for the current request
export const getCurrentUser = cache(
  async function () {
    const session = await getSession(cookies());

    return session.currentUser;
  },
);

// Somewhere deep in the server tree...
async function Menu() {
  const currentUser = await getCurrentUser();

  return <p>Hello, {currentUser.name}!</p>;
}
```

`cache` will memoize the function you give it for the current request-response cycle only. So no matter how many components call it, your function will only execute once per request.

But what about Client Components? How can they access this data?

By design, Client Components can't directly call server-side helpers like `getCurrentUser`; if they could, it'd be too easy for us to add unnecessary roundtrips from the client to the server and back (so-called network waterfalls) while rendering our page.

So—how can we share data that we fetched in our Server Components with the rest of the client tree?

Well, even though Server Components can't use Context themselves, they *can* pass their data to Client Components as props. And Client Components can use Context.

## Passing Server Component props into Context

So, if we fetch `currentUser` from a Server Component, pass it to a Client Component as a prop, and then render a Context with that prop as its value, the rest of our client tree should have access to `currentUser`.

Let's give it a shot!

Here's the Server Component part of our AuthProvider:

```
// auth-provider/index.jsx
export async function AuthProvider({ children }) {
  const currentUser = await getCurrentUser();

  return (
    <AuthContext value={currentUser}>
      {children}
    </AuthContext>
  );
}
```

And here's the client part: the Context itself, and a Hook for convenient access:

```
// auth-provider/client.jsx
"use client";
import { createContext, use } from "react";

const Context = createContext();

async function AuthContext({ value, children }) {
  return (
    <Context value={value}>{children}</Context>
  );
}

export function useCurrentUser() {
  const currentUser = use(Context);

  return currentUser;
}
```

Now if we add the provider to our root layout:

```
// layout.jsx
import { AuthProvider } from "./auth-provider";

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  );
}
```

...we can call `useCurrentUser` anywhere inside the client tree to access the data:

```
// Somewhere deep in the client tree...
function Menu() {
  const currentUser = useCurrentUser();

  return <p>Hello, {currentUser.name}!</p>;
}
```

Voilà! Pretty nifty.

---

We've solved the prop drilling problem across both our server and client trees, but we've introduced a new issue:

AuthProvider is now blocking the initial render of our entire application.

By awaiting the `getCurrentUser` promise in our provider, none of the children can be rendered until that promise resolves. And if you've enabled [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components), you'll even see a new warning calling this out:

> Data that blocks navigation was accessed outside of <Suspense>

How can we fix it?

## Using promises to unblock navigations

Instead of passing the *resolved* user to the Client Component, let's pass only the *promise*:

```
// auth-provider/index.jsx
export async function AuthProvider({ children }) {
  const currentUserPromise = getCurrentUser(); // 🟢 No await

  return (
    <AuthContext value={currentUserPromise}>
      {children}
    </AuthContext>
  );
}
```

Now our Context is providing the promise to the rest of the tree:

```
// auth-provider/client.jsx
"use client";
import { createContext } from "react";

const Context = createContext();

async function AuthContext({ value, children }) {
  // 🟢 value is a promise
  return (
    <Context value={value}>{children}</Context>
  );
}
```

...and AuthProvider no longer blocks our app from rendering.

But what about our Hook? Its return value is now the promise instead of the actual data:

```
export function useCurrentUser() {
  const currentUserPromise = use(Context);

  return currentUserPromise;
}
```

If we call React's [`use`](https://react.dev/reference/react/use) API once more, we can unwrap the promise:

```
export function useCurrentUser() {
  const currentUserPromise = use(Context);
  const currentUser = use(currentUserPromise);

  return currentUser;
}
```

...and now the Hook provides the data just like before, only this time **it will suspend the caller** if the data's not ready.

So, if a Client Component deep in the tree needs the current user for rendering, we can call `useCurrentUser`:

```
// Somewhere deep in the client tree...
function Menu() {
  const currentUser = useCurrentUser();

  return <p>Hello, {currentUser.name}!</p>;
}
```

and provide some fallback UI while the component suspends:

```
// The component that renders Menu
function Header() {
  return (
    <div>
      <Link href="/">Home</Link>

      <Menu.Root>
        <Menu.Trigger>Account</Menu.Trigger>
        <Menu.Popup>
          {/* 🟢 Fallback UI for when Menu suspends */}
          <Suspense fallback="Loading...">
            <Menu />
          </Suspense>
        </Menu.Popup>
      </Menu.Root>
    </div>
  );
}
```

Now, our provider doesn't block the rest of the page from rendering, and we still have an easy way to access the data throughout our client tree.

---

Passing promises to Client Components is a powerful pattern.

You get to use Server Components to martial all the data needed for a page during the initial request, but you unblock components that don't depend on that data from rendering as early as possible—potentially even at build time, if you're prerendering your app.

And by using `cache` on the server, and Context and `use` on the client, you can avoid prop drilling when sharing that data throughout your server and client trees.

It's a great pattern for data that many components need, like the current user, feature flags, or even dynamic data that depends on request values like dynamic params or search params.

Related notes: [[Server Components]]
