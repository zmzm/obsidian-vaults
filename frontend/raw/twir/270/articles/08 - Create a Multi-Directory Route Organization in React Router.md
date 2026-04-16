---
type: twir-item
issue: 270
item: 8
item_type: item
date: 2026-02-25
source: https://sergiodxa.com/tutorials/create-a-multi-directory-route-organization-in-react-router
tags:
  - "ReactRouter"
  - "Multi-Directory"
status: auto
quality: keep
---

[[2026-02-25-TWIR-270|Index]]

# Item 8: Create a Multi-Directory Route Organization in React Router

Source: [https://sergiodxa.com/tutorials/create-a-multi-directory-route-organization-in-react-router](https://sergiodxa.com/tutorials/create-a-multi-directory-route-organization-in-react-router)

Summary:
This tutorial explains how to organize large React Router codebases by splitting routes into multiple directories (e.g., public, app, api, actions), each following the flat routes convention. It covers combining route configs, applying shared layouts or middleware, and handling cross-directory dependencies, enabling scalable and maintainable routing structures for teams.

Key takeaways:
- Use multiple directories with flatRoutes() to keep route organization manageable.
- Shared layouts and middleware can be applied per section or across sections.
- Cross-directory dependencies are handled via absolute paths.
- Supports scaling route organization to team or feature boundaries.

Recommendation:
Summary sufficient

Content:
# How to Create a Multi-Directory Route Organization in React Router by sergiodxa

As your application grows, a single `routes/` folder can become overwhelming. You might have public marketing pages, authenticated app routes, API endpoints, and [action routes](/tutorials/use-action-routes-in-react-router) all mixed together. Splitting routes into logical directories helps teams work independently and makes the codebase easier to navigate, while the flat routes convention remains desirable for its simplicity and predictability within each directory.

You can call `flatRoutes()` multiple times, once per directory, and combine the results. Each directory maintains the flat routes convention internally for simplicity and predictability, while the overall structure stays organized by feature or team. For even more control over route organization, see [how to split your routes config](/tutorials/split-routes-config-in-react-router).

## Set Up the Directory Structure

```
app/
├── routes/
│   ├── public/
│   │   ├── _index.tsx
│   │   ├── about.tsx
│   │   └── pricing.tsx
│   ├── app/
│   │   ├── _.tsx
│   │   ├── _.dashboard.tsx
│   │   └── _.settings.tsx
│   ├── api/
│   │   ├── users.ts
│   │   └── posts.ts
│   └── actions/
│       ├── user-update.ts
│       └── post-create.ts
└── routes.ts
```

Each sub-folder contains routes using the flat routes convention. The `public/` folder handles marketing pages, `app/` contains authenticated routes with a shared layout, `api/` exposes REST endpoints, and `actions/` centralizes form handlers.

## Configure Multiple Route Sources

```
import type { RouteConfig } from "@react-router/dev/routes";
import { prefix } from "@react-router/dev/routes";
import { flatRoutes } from "@react-router/fs-routes";

let [publicRoutes, appRoutes, apiRoutes, actionRoutes] = await Promise.all([
	flatRoutes({ rootDirectory: "./routes/public" }),
	flatRoutes({ rootDirectory: "./routes/app" }),
	flatRoutes({ rootDirectory: "./routes/api" }),
	flatRoutes({ rootDirectory: "./routes/actions" }),
]);

export default [
	...publicRoutes,
	...prefix("/app", appRoutes),
	...prefix("/api", apiRoutes),
	...prefix("/actions", actionRoutes),
] satisfies RouteConfig;
```

The `flatRoutes()` function scans each directory independently, so `_.dashboard.tsx` in the `app/` folder becomes `/app/dashboard` after the prefix is applied. Public routes have no prefix since they live at the root.

Using `Promise.all()` loads all directories in parallel, keeping build time fast even with many route folders.

## Add Shared Layouts per Section

```
import { Outlet } from "react-router";

export default function AppLayout() {
	return (
		<div className="flex min-h-screen">
			<aside className="w-64 border-r">
				<nav>{}</nav>
			</aside>
			<main className="flex-1 p-8">
				<Outlet />
			</main>
		</div>
	);
}
```

The `_.tsx` file creates a layout route with no path segment. Routes prefixed with `_.` become children of this layout, so `_.dashboard.tsx` renders at `/app/dashboard` inside the `AppLayout`. Using `_.` as the prefix keeps filenames short while making the nesting relationship clear. This allows you to share navigation, styles, or any other UI across all routes in that section without repeating code.

This also works to apply middleware to a section. Export the auth middleware from `_.tsx` and every route nested inside it will require authentication. If you're new to middleware, start with [the middleware basics](/tutorials/use-middleware-in-react-router).

## Add Shared Layout between Sections

If you want to share a layout, or middleware, between multiple sections (e.g. both app and public routes), you can create a separate file for that:

```
import { Outlet } from "react-router";

export default function SharedLayout() {
	return (
		<div>
			<header>{}</header>
			<main>
				<Outlet />
			</main>
			<footer>{}</footer>
		</div>
	);
}
```

Then wrap the relevant route groups in `routes.ts`:

```
import type { RouteConfig } from "@react-router/dev/routes";
import { layout, prefix } from "@react-router/dev/routes";
import { flatRoutes } from "@react-router/fs-routes";

let [publicRoutes, appRoutes, apiRoutes, actionRoutes] = await Promise.all([
	flatRoutes({ rootDirectory: "./routes/public" }),
	flatRoutes({ rootDirectory: "./routes/app" }),
	flatRoutes({ rootDirectory: "./routes/api" }),
	flatRoutes({ rootDirectory: "./routes/actions" }),
]);

export default [
	layout("./layouts/shared.tsx", [...publicRoutes, ...prefix("/app", appRoutes)]),
	...prefix("/api", apiRoutes),
	...prefix("/actions", actionRoutes),
] satisfies RouteConfig;
```

## Handle Cross-Directory Dependencies

```
import type { Route } from "./+types/_.posts";
import { useFetcher } from "react-router";

export default function Posts({ loaderData }: Route.ComponentProps) {
	let fetcher = useFetcher();

	return (
		<div>
			<h1>Posts</h1>
			<fetcher.Form method="post" action="/actions/post-create">
				<input name="title" placeholder="Post title" />
				<button type="submit">Create Post</button>
			</fetcher.Form>
		</div>
	);
}
```

Routes in one directory can reference routes in another using absolute paths. The form submits to `/actions/post-create`, which lives in the `actions/` directory. This keeps the action logic centralized while allowing any route to trigger it.

## Scale to Team Boundaries

For larger teams, you might organize by feature or team ownership:

```
app/
├── routes/
│   ├── marketing/      # Marketing team
│   ├── dashboard/      # Product team
│   ├── admin/          # Platform team
│   ├── api/            # API team
│   └── actions/        # Shared actions
└── routes.ts
```

Each team owns their directory and can add routes without merge conflicts. The `routes.ts` file acts as the central registry, making it clear which prefixes map to which directories.

This pattern scales well because adding a new section means adding one `flatRoutes()` call and one spread in the export, no restructuring of existing routes required.
