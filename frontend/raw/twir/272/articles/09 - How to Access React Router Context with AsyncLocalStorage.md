---
type: twir-item
issue: 272
item: 9
item_type: item
date: 2026-03-11
source: https://sergiodxa.com/tutorials/access-react-router-context-with-asynclocalstorage
tags:
  - "AsyncLocalStorage"
  - "Nodejs"
status: auto
quality: keep
---

[[2026-03-11-TWIR-272|Index]]

# Item 9: How to Access React Router Context with AsyncLocalStorage

Source: [https://sergiodxa.com/tutorials/access-react-router-context-with-asynclocalstorage](https://sergiodxa.com/tutorials/access-react-router-context-with-asynclocalstorage)

Summary:
This tutorial explains how to use Node.js’s AsyncLocalStorage to make React Router’s context and request objects accessible throughout an application without explicit parameter passing. By wrapping the request lifecycle with AsyncLocalStorage (or using Remix Utils’ helper), developers can access context, request, session, or database instances from any function, simplifying loader and service code. The middleware order and helper function patterns are detailed for robust integration.

Key takeaways:
- AsyncLocalStorage enables per-request context propagation without manual parameter threading.
- Middleware setup ensures context and request are available throughout the request lifecycle.
- Helper functions can access session, database, or user data from anywhere in the codebase.
- This pattern simplifies code and improves maintainability in complex React Router/Remix applications.

Recommendation:
Read fully (read fully for implementation details or if integrating per-request context in Node.js/React Router apps)

Why it matters:
read fully for implementation details or if integrating per-request context in Node.js/React Router apps

Content:
# How to Access React Router Context with AsyncLocalStorage by sergiodxa

React Router's `context` object is available in loaders and actions, and [middleware can populate it](/tutorials/use-middleware-in-react-router) with databases, sessions, and other per-request resources. The problem is that you need to pass this context through every function that needs access to these resources: from loaders to services, from services to repositories, and so on.

AsyncLocalStorage solves this by storing the React Router context in a request-scoped storage. Any function can retrieve it during that request's lifecycle without requiring it as a parameter. You set it up once with middleware and access it from anywhere in your application.

## Understand How AsyncLocalStorage Works

Node.js provides `AsyncLocalStorage` as a way to store data that follows the execution flow of asynchronous operations. You create a storage instance, run code within it using `run()`, and any function called during that execution can retrieve the stored value using `getStore()`:

```
import { AsyncLocalStorage } from "node:async_hooks";
import type { MiddlewareFunction, RouterContextProvider } from "react-router";

interface Store {
	context: RouterContextProvider;
	request: Request;
}

let storage = new AsyncLocalStorage<Store>();

export const contextStorageMiddleware: MiddlewareFunction<Response> = (
	{ context, request },
	next,
) => {
	return storage.run({ context, request }, next);
};

export function getContext() {
	let store = storage.getStore();
	if (!store) throw new Error("Context storage not initialized");
	return store.context;
}

export function getRequest() {
	let store = storage.getStore();
	if (!store) throw new Error("Context storage not initialized");
	return store.request;
}
```

The middleware wraps the entire request lifecycle with `storage.run()`, making the context and request available to any function called during that request.

## Use the Remix Utils Implementation

The implementation above works, but [Remix Utils](https://github.com/sergiodxa/remix-utils) provides a `createContextStorageMiddleware` function that handles this for you with proper TypeScript types:

```
import { createContextStorageMiddleware } from "remix-utils/middleware/context-storage";

export const [contextStorageMiddleware, getContext, getRequest] = createContextStorageMiddleware();
```

This returns a tuple with the middleware and two getter functions. The `contextStorageMiddleware` stores the `context` and `request` in AsyncLocalStorage when a request comes in, and `getContext` and `getRequest` retrieve them from anywhere in your code during that request.

## Add the Middleware to Your Root Route

Add the context storage middleware to your root route. It should be one of the first middlewares in the chain so other middlewares can use the getter functions:

```
import { contextStorageMiddleware } from "~/middleware/context-storage";
import { loggerMiddleware } from "~/middleware/logger";
import { sessionMiddleware } from "~/middleware/session";
import { databaseMiddleware } from "~/middleware/database";

export const middleware = [
	contextStorageMiddleware,
	loggerMiddleware,
	sessionMiddleware,
	databaseMiddleware,
];
```

The order matters: `contextStorageMiddleware` must run before any middleware that calls `getContext()` or `getRequest()`.

## Create Helper Functions That Use the Context

Now you can create helper functions that access the context without requiring it as a parameter. If you followed [how to create a per-request database instance with middleware](/tutorials/create-a-per-request-database-instance-with-middleware), you can wrap the database access like this:

```
import { databaseContext } from "~/context/database";
import { getContext } from "~/middleware/context-storage";

export function getDB() {
	let context = getContext();
	return context.get(databaseContext);
}
```

The `getDB()` function retrieves the context internally and returns the database instance. Callers don't need to know about the context at all.

## Access the Request from Anywhere

You can also access the current request from anywhere using `getRequest()`. This is useful for building URLs or reading headers:

```
import { getRequest } from "~/middleware/context-storage";

export function buildAbsoluteUrl(path: string) {
	let request = getRequest();
	return new URL(path, request.url).toString();
}
```

This pattern is particularly useful in query functions or services that need request information but shouldn't require it as a parameter.

## Access Session Data from Anywhere

The same pattern works for session data. If you have a session context set up by middleware, wrap it with a helper function:

```
import { sessionContext } from "~/context/session";
import { getContext } from "~/middleware/context-storage";

export function getSession() {
	let context = getContext();
	return context.get(sessionContext);
}

export function getUser() {
	let session = getSession();
	return session.get("user");
}
```

Now any part of your application can call `getUser()` without passing context through multiple layers.

## Use in Loaders and Actions

With this setup, your loaders and actions become much cleaner:

```
import type { Route } from "./+types/posts";
import { getDB } from "~/middleware/database";
import { getUser } from "~/middleware/session";

export async function loader({}: Route.LoaderArgs) {
	let user = getUser();
	let db = getDB();

	let posts = await db.query.posts.findMany({
		where: (posts, { eq }) => eq(posts.authorId, user?.id),
	});

	return { posts };
}
```

No need to destructure `context` or pass it around. The helper functions handle everything internally.

## Trade-Offs to Consider

This pattern creates implicit dependencies: functions call `getDB()` or `getUser()` without declaring them as parameters. This makes the code cleaner but harder to test in isolation since you need the AsyncLocalStorage context to be set up.

For an alternative approach that keeps dependencies explicit, see [dependency injection in loaders and actions](/articles/dependency-injection-in-remix-loaders-and-actions).
