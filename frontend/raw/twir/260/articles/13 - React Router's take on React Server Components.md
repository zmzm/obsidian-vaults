---
type: twir-item
issue: 260
item: 13
item_type: item
date: 2025-11-26
source: https://www.epicreact.dev/react-routers-take-on-react-server-components-4bj7q
tags:
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-11-26-TWIR-260|Index]]

# Item 13: React Router's take on React Server Components

Source: [https://www.epicreact.dev/react-routers-take-on-react-server-components-4bj7q](https://www.epicreact.dev/react-routers-take-on-react-server-components-4bj7q)

Summary:
This brief note points to a resource explaining how React Suspense and the use hook enable declarative async UI, improving loading and error state management in React applications.

Key takeaways:
- React Suspense leverages thrown promises and the use hook for async data handling.
- Simplifies management of loading and error states in React.
- Enhances user experience with more predictable async UI patterns.

Recommendation:
Summary sufficient

Content:
# React Router's take on React Server Components

Did you know React Router is adding React Server Components support? It's still
experimental, but it's very close to landing, and I think React Router's take on
RSC is really great. Here's what you need to know.

## Enabling React Server Components

The first step is to enable RSC in your React Router app. You'll need to install
two plugins:

1. The React Router RSC plugin from `@react-router/dev/vite`
2. The RSC plugin from `@vitejs/plugin-rsc`

Here's how to update your `vite.config.ts`:

`// unstable_reactRouterRSC as reactRouterRSC,

} from '@react-router/dev/vite'

import tailwindcss from '@tailwindcss/vite'

// import rsc from '@vitejs/plugin-rsc'

import { defineConfig } from 'vite'

import devtoolsJson from 'vite-plugin-devtools-json'

import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({

port: process.env.PORT ? Number(process.env.PORT) : undefined,

// Replace reactRouter() with:`

So much of what makes RSC work is the integration with the bundler. A lot of the
heavy lifting comes from the Vite team, with significant contributions from the
React Router team.

Once you've enabled RSC, you'll also need to remove the `Scripts` component from
your root layout. With RSC, those scripts are included as part of the RSC
payload automatically:

`// Remove this Scripts import

export function Layout({ children }: { children: React.ReactNode }) {

<meta name="viewport" content="width=device-width, initial-scale=1" />

{/* Remove this Scripts element */}`

## RSC in Loaders

Now that RSC is enabled, what can you do with it? One powerful pattern is
returning UI from your loaders instead of just data.

Here's a traditional loader that returns data:

`export async function loader() {

const movies = await getMovies()

export default function MoviesPage({ loaderData }: Route.ComponentProps) {

const { movies } = loaderData

const moviesUI = movies.map((movie) => (

<MovieCard key={movie.id} movie={movie} />

<div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">`

The problem with this approach is that we're sending data to the client that we
don't actually need once it's been rendered. We're hydrating data unnecessarily.

With RSC, you can return the completed UI from your loader:

`export async function loader() {

const movies = await getMovies()

const moviesUI = movies.map((movie) => (

<MovieCard key={movie.id} movie={movie} />

export default function MoviesPage({ loaderData }: Route.ComponentProps) {

const { moviesUI } = loaderData

<div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">`

Now you're just serving UI from the server without sending any of the underlying
data. This is especially powerful if you're pulling data from a CMS where you
don't know what UI you need to render before you have the data. Instead of
dynamically loading components (leading to spinners) or loading all possible
components upfront, you can make that determination in the loader and send the
resulting UI, making your payload way smaller.

## RSC Routes

But wait—if the entire page could be a server component, why use a loader at
all? You can make the entire route a server component:

`import { MovieCard } from '#app/movie-card.tsx'

import { getMovies } from '#app/movies-data.ts'

export async function ServerComponent() {

const movies = await getMovies()

const moviesUI = movies.map((movie) => (

<MovieCard key={movie.id} movie={movie} />

<main className="bg-background min-h-screen">

<div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">`

Notice that we're exporting a named `ServerComponent` function instead of a
default export. This means we don't need the loader at all—we can directly get
the data inside the component itself because it's a server component.

The entire UI is rendered on the server, sent to the client, and not hydrated
because there's no interactivity. This makes types simpler too—no need for
loader data types.

## Incremental Migration

One of the most powerful aspects of React Router's RSC implementation is that
you can migrate incrementally. If you have nested routes, a child route can be a
client route, and that can have a child that's a server route. They don't have
to know about each other.

This means if you're working on a big application with different teams in charge
of different routes, one team can decide to make their portion an RSC route
without the rest of the app having to change. This makes incremental migration
really possible and really powerful.

## Server Functions

React Router has always had actions, but React now has form actions as a
primitive. With RSC, you can use React's form actions directly with server
functions.

Here's how you can create a server function:

`export async function setIsFavorite(formData: FormData) {

// Simulate API call delay

await new Promise((resolve) => setTimeout(resolve, 50))

const movieId = Number(formData.get('id'))

const isFavorite = formData.get('isFavorite') === 'true'

// Update the movie's favorite status

const movie = movies.find((m) => m.id === movieId)

movie.isFavorite = isFavorite`

The `'use server'` directive says that the things exported from this module can
be referenced in the client. When the form action is called, it makes an RPC
call to the server to actually call this function.

Then you can use it directly in your form:

`<form action={setIsFavorite}>

<input type="hidden" name="id" value={movie.id} />

value={String(!movie.isFavorite)}

{movie.isFavorite ? 'Favorite' : 'Not Favorite'}`

Why is this cool? With React Router, all actions and loaders are tied to a
route. But if you use React's form actions with server functions, they can be
tied to a component. You could take this form, make it a component all by
itself, and reuse it all over the place—on the details page, on cards, in a chat
feature, anywhere.

The status quo for doing this with React Router before RSC was having to find
the closest route for all of those and have an action on every one of those
routes. With RSC, you don't have to do that. A component can manage its own data
loading and data mutations. You could even publish it on npm, and anybody who
supports RSC would be able to use your component.

## Client Components

Of course, sometimes you need interactivity. That's where client components come
in. If you're using hooks like `useState` or `useEffect`, you need to mark that
component as a client component:

`import { Activity, useEffect, useState } from 'react'

import { type Movie } from '#app/movies-data.ts'

export function MovieTrailer({ movie }: { movie: Movie }) {

const [showTrailer, setShowTrailer] = useState(false)

// ... rest of the component`

The `'use client'` directive says that this code needs to go to the browser
because it has state or other client-side logic. It still server renders, but it
also sends that code to the client to make it interactive.

The really cool thing is that you can use client components inside server
components without changing anything about the server component. The server
component doesn't need to know that the client component exists—it just works.

## Who Does This Help?

RSCs in loaders are really helpful if you're building something like a big
timeline that has many, many combinations of different components that could
possibly be used, and you don't know which one until you have the data. That's
perfect for RSCs in loaders and RSC routes.

For everybody else, it's a nice handy thing. I should call out that sometimes
the combination between data and template together will actually be bigger than
just data and template separate—it kind of depends on the scenario. But for most
people, just using RSCs and RSC routes makes a lot of sense.

The cool thing about React Router is that you don't have to completely switch
over. You can migrate incrementally as you see that being a really beneficial
thing. Aside from the fact that you can also do your data loading right in the
components, so types are a lot better, and you can use Suspense boundaries and
all of that stuff as well.

Server functions are super useful for those of you who have components that need
to have data loading and data mutation associated to them. And now you can just
put those all over the place.

Client components, of course, are only really useful if you are using server
components. If you're not turning your routes or different components into
server components, you're not going to be using client components. Your entire
app is still client components. But if you decide RSC is really the way that you
want to go, then client components are the way you want to go.

## Static Builds

One more thing I should mention: you can actually still do a static build of a
React Router app with Server Components. That is part of the design of React
Server Components. You should be able to still get some of the benefits of RSC
with being able to deploy this to a static environment. You don't necessarily
need a server to use React Server Components—the server can be the build server.

## Summary

React Router's implementation of React Server Components is really well done. It
supports:

- **RSC in the bundler** - Enable RSC with Vite plugins
- **RSCs in loaders** - Return UI from loaders instead of data
- **RSC routes** - Make entire routes server components
- **Server functions** - Use React's form actions with `'use server'`
- **Client components** - Mark components that need interactivity with
  `'use client'`

All of these are supported in React Router, and the incremental migration path
makes it really powerful for teams working on large applications. For the use
cases that React Server Components serves really well, I think this is really
good.

Related notes: [[Server Components]]
