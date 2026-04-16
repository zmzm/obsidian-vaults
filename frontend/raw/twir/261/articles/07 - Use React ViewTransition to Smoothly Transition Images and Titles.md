---
type: twir-item
issue: 261
item: 7
item_type: item
date: 2025-12-03
source: https://www.epicreact.dev/use-react-view-transition-to-smoothly-transition-images-and-titles-lu6ks
tags:
  - "ViewTransition"
status: auto
quality: keep
---

[[2025-12-03-TWIR-261|Index]]

# Item 7: Use React <ViewTransition /> to Smoothly Transition Images and Titles

Source: [https://www.epicreact.dev/use-react-view-transition-to-smoothly-transition-images-and-titles-lu6ks](https://www.epicreact.dev/use-react-view-transition-to-smoothly-transition-images-and-titles-lu6ks)

Summary:
React 19’s <ViewTransition> component leverages the platform View Transition API to create smooth, animated transitions between pages or components. By wrapping elements with the same name prop, React automatically animates transitions, supporting multiple elements and custom CSS animations.

Key takeaways:
- <ViewTransition> enables seamless, cross-fade (or custom) transitions for elements across navigation.
- Requires unique name props and proper placement in the DOM.
- Works with routers and startTransition for navigation.
- Supports CSS customization for advanced animation effects.

Recommendation:
Read fully (read fully if implementing animated transitions or evaluating React 19 features)

Why it matters:
read fully if implementing animated transitions or evaluating React 19 features

Content:
# Use React <ViewTransition /> to Smoothly Transition Images and Titles

React 19's ViewTransition component makes it easy to create smooth, animated
transitions between pages. Wrap elements with the same name on different pages
and React handles the rest.

Remember when clicking between pages meant an abrupt jump? Users expect smooth
transitions now, especially after years of polished mobile apps. React's new
`<ViewTransition />` component (available in React 19 Canary) makes it easy to
create those smooth, animated transitions between pages.

## What is ViewTransition?

`<ViewTransition />` is React's componentized way to use the platform's View
Transition API. It lets you animate elements as they move from one page to
another, creating that polished, app-like feel users expect.

The concept is simple: wrap elements you want to transition with
`<ViewTransition />` and give them the same `name` prop. When React navigates
between pages, it automatically animates elements with matching names.

## A Practical Example

Let's say you have a movie catalog. When users click a movie card, they navigate
to the details page. Wouldn't it be nice if the poster image smoothly
transitioned from the card to the details page? That's exactly what
ViewTransition does.

Here's the movie card component:

`` <ViewTransition name={`movie-poster-${movie.id}`}>

alt={`${movie.title} poster`}

className="mb-4 h-64 w-full rounded-lg object-cover" ``

And here's the same element on the details page:

`` <ViewTransition name={`movie-poster-${movie.id}`}>

alt={`${movie.title} poster`}

className="h-96 w-full rounded-lg object-cover" ``

Notice both use the same `name` prop: `movie-poster-${movie.id}`. This tells
React these are the same element transitioning between pages. When you navigate,
React automatically creates a smooth fade transition between them.

## Multiple Elements

You can transition multiple elements at once. Let's also transition the title:

`` <ViewTransition name={`movie-title-${movie.id}`}>

<h3 className="rr-heading text-lg font-semibold">{movie.title}</h3> ``

And on the details page:

`` <ViewTransition name={`movie-title-${movie.id}`}>

<h1 className="rr-heading mb-4 text-3xl font-bold">{movie.title}</h1> ``

Now both the poster and title smoothly transition when navigating between pages.
The browser handles the animation automatically with a default cross-fade, but
you can customize it with CSS if you want.

## Important Details

**Unique names are required**: Each `<ViewTransition />` with the same `name`
must be unique across your entire app. That's why we use
`movie-poster-${movie.id}` instead of just `"movie-poster"`. If two components
with the same name are mounted simultaneously, React will throw an error.

**Works with Transitions**: ViewTransition only activates when wrapped in a
`startTransition` call. Most routers (like React Router) handle this
automatically, but if you're managing navigation manually, make sure to use
`startTransition`.

**Placement matters**: The `<ViewTransition />` component must wrap DOM nodes
directly. It can't be placed after other DOM elements in the same parent.

## Customization

By default, ViewTransition uses a smooth cross-fade animation. But you can
customize it with CSS using view transition pseudo-elements:

`::view-transition-old(movie-poster-1) {

animation-duration: 500ms;

::view-transition-new(movie-poster-1) {

animation-duration: 500ms;`

You can create slide animations, scale effects, or any other CSS animation you
can imagine. The platform's View Transition API is powerful, and React's
component makes it accessible.

## Learn More

ViewTransition is a great example of React making platform APIs more ergonomic.
To dive deeper:

Give ViewTransition a try in your next project. Your users will notice the
difference!
