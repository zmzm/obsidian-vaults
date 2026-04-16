---
type: twir-item
issue: 274
item: 9
item_type: item
date: 2026-03-25
source: https://raphaelbronsveld.com/blog/type-safety-in-react-router
tags:
  - "ReactRouter"
  - "Navigation"
status: auto
quality: keep
---

[[2026-03-25-TWIR-274|Index]]

# Item 9: Type Safety in React Router

Source: [https://raphaelbronsveld.com/blog/type-safety-in-react-router](https://raphaelbronsveld.com/blog/type-safety-in-react-router)

Summary:
React Router has improved type safety with generated types for routes, loader data, and actions, reducing the need for manual type hints. The new `useRoute` hook (unstable) provides type-safe access to route data, and the `href` utility ensures compile-time safety for links. These features are available in framework mode and help prevent runtime errors and broken links.

Key takeaways:
- Generated types provide type-safe params and data throughout the route tree.
- `useRoute` hook offers type-safe access to loader and action data.
- `href` utility ensures links are valid at compile time, reducing navigation bugs.
- Type safety improvements are specific to framework mode.

Recommendation:
Read fully (read fully if you use React Router and want to leverage type safety features)

Why it matters:
read fully if you use React Router and want to leverage type safety features

Content:
# Type Safety in React Router

Scrolling through discussions online and reading about "Which React Framework should I use?" I always feel like React Router doesn't get enough credit. React Router is obviously mentioned but often overshadowed by the new shiny thing, TanStack Start. One of the main talking points in these discussions is type-safety. If you need a fully type-safe experience from the ground up, TanStack won't do you wrong.

Type safety isn't something that's entirely new in React Router, but it definitely got improved! If you're already in the React Router ecosystem and want to improve reliability and reduce the amount of runtime errors, this post is for you.

## Route Modules

Before diving in, make sure you have setup React Router to generate types. You can go to [this link](https://reactrouter.com/how-to/route-module-type-safety) to learn more.

Now you're able to use the generated types in, for example, your root route module.

```
// root.tsx
import type { Route } from "./+types/root";
 
// type-safe params from route definition
export const loader = ({ params }: Route.LoaderArgs) => {};
 
// type-safe "data" from loader
export const meta: MetaFunction = ({ data }: Route.MetaArgs) => {};
```

Copy

Previously, you'd have to hint the type manually. `useLoaderData()` returns `unknown`, so you would use a `typeof` cast:

```
const data = useLoaderData<typeof loader>();
```

Copy

With the new generated types, that's no longer needed. Your component receives `loaderData` directly via `Route.ComponentProps`, fully type-safe with return values from your loader's function.

```
// loaderData = type-safe yes!
export default HomeComponent({ loaderData }: Route.ComponentProps) {}
```

Copy

Nice, but still fairly straight-forward. This works fine in the Route module itself but still means you'd have to pass on the generated types to lower-level components. Ideally we'd have something that handles this for us.

## useRoute

This one flew under the radar for me since it's also still marked as *unstable*. The new introduced `useRoute` hook is also aware of your application routes. It takes a route ID, which matches the path of the route you defined in your routes.ts. The return value of `useRoute` contains `loaderData` and `actionData`.

> useRoute is marked as unstable but I don't expect this api to change a whole lot, I'd consider this "fairly safe" to use.

```
import { unstable_useRoute as useRoute } from "react-router";
 
// passing no argument returns the current route
const current = useRoute();
 
// Argument = type-safe
const products = useRoute("routes/products");
 
// Both loaderData + actionData are type-safe
const { loaderData, actionData } = products;
 
// returns undefined if you're not on the checkout page.
const checkout = useRoute("routes/checkout");
if (!checkout) {
	throw new Error(`Checkout accessed with useRoute on non-checkout page"`);
}
```

Copy

For more information I'd suggest taking a look in the [documentation](https://reactrouter.com/changelog#useroute-unstable).

## href

Wouldn't it be nice to also have a way to link to pages you know exist? Let me introduce you to `href()`.

```
import { href } from "react-router";
 
const link = href("/product/:slug", { slug: "awesome-product" })
// -> /product/awesome-product
 
<Link to={href("/user/:username", { username: "raphaelisthebest" })} />
// -> <a href="/user/raphaelisthebest">
```

Copy

> If you relied heavily on `navigate` before, you might be able to refactor those to use `href` instead.

If you rename or remove a route, Typescript will flag every broken `href` call. Neat!

---

One thing worth noting: all of the above is specific to framework mode. If you're using React Router in library mode, type generation won't be done.

I'd suggest going through the documentation on how to migrate to framework mode with React Router's vite plugin.

These might seem like small additions, but they add up: no more manual type-hinting, fewer runtime surprises, and links that actually break at compile time. Hope it was useful!

## You might also like.

[Go back to blog](/blog)
