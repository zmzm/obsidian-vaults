---
type: twir-item
issue: 256
item: 4
item_type: item
date: 2025-10-29
source: https://appwrite.io/blog/post/why-developers-leaving-nextjs-tanstack-start
tags:
  - "Nextjs"
  - "TanStack"
status: auto
quality: keep
---

[[2025-10-29-TWIR-256|Index]]

# Item 4: Why developers are leaving Next.js for TanStack Start, and loving it

Source: [https://appwrite.io/blog/post/why-developers-leaving-nextjs-tanstack-start](https://appwrite.io/blog/post/why-developers-leaving-nextjs-tanstack-start)

Summary:
This post explores why some developers are migrating from Next.js to TanStack Start, highlighting frustrations with Next.js's growing complexity and perceived Vercel lock-in. TanStack Start is praised for its simplicity, explicitness, type-safe routing, and server functions, offering a developer experience closer to "plain React." The article shares real-world use cases and emphasizes TanStack Start's flexibility, transparency, and rapid adoption among developers seeking more control and less abstraction.

Key takeaways:
- Developers cite Next.js complexity, breaking changes, and Vercel coupling as pain points.
- TanStack Start offers type-safe routing, explicit server functions, and a lighter, more transparent stack.
- The framework is suitable for production apps and scales well from small to large projects.
- The shift reflects a broader desire for simplicity, control, and alignment with React's core principles.

Recommendation:
Summary sufficient

Content:
# Why developers are leaving Next.js for TanStack Start, and loving it

The React world is full of opinions, and every few years a new framework changes how we think about building apps. Next.js has been the default choice for a long time. It offered a clear path to production and made React easier to manage. But recently, more developers have been moving toward **TanStack Start**, a newer full-stack framework built by the same team behind TanStack Query and TanStack Router.

They're not leaving because Next.js is broken. They're leaving because **TanStack feels lighter, clearer, and closer to plain React,** and it gives them back control over how things actually work.

Many developers used to love Next.js for its simplicity. But as it grew, so did its complexity. The shift to the App Router, the introduction of React Server Components, and constant new patterns have made the framework harder to follow.

In community discussions, one developer summed it up: *"Next.js lost me with the constant changes and complexity. The benefits don't justify the cognitive overload."* Others mentioned how debugging has become confusing and how new features often break old patterns.

Another recurring concern is that **Next.js feels tied to Vercel**. Many devs appreciate Vercel as a company, but they feel the framework has become more about the platform than the developer. As one user said, *"It's tough to separate Next.js from Vercel. Most advantages people list are actually Vercel features."*

TanStack didn't appear out of nowhere. It grew from the success of **TanStack Query** (formerly React Query), a library that completely changed how developers handled state and server data. It replaced complex Redux setups with something that "just made sense."

That same idea of **simplicity without shortcuts** is what's driving interest in TanStack Start. Developers already trust the TanStack team because their tools consistently solve real problems without hiding what's going on behind the scenes.

As one developer put it, *"They did for routing and server logic what they already did for state management â made it simple, predictable, and type-safe."*

TanStack Start is a **full-stack React framework** that builds on TanStack Router, powered by **Vite** for fast builds and **Vite Env APIs**, which supports Nitro among other deployment plugins. It combines client-side interactivity with server-side rendering, all while keeping things explicit and type-safe.

Key features developers like:

- **Type-safe routing:** Everything is validated at compile time. If a route or parameter changes, you'll know immediately.
- **Server functions:** You can write backend logic (like database queries or API calls) in the same codebase and call it safely from the client.
- **Client-first rendering:** You get SSR for performance, but navigation feels like a single-page app.
- **Simple deployment:** Works on Netlify, Cloudflare, Vercel, or your own Node server with minimal setup.

It's not trying to reinvent React. It's giving React a modern backbone that's easy to understand.

Developers in the community consistently mention a few themes:

1. **Less magic, more control.**

   Frameworks like Next.js and Remix rely on "magic" conventions which is behaviors that happen automatically. TanStack Start avoids that. You choose how data loads, where it runs, and what gets rendered.
2. **Feels closer to React.**

   Many devs say that once they start using TanStack Start, they forget they're even in a framework. It feels like normal React with some helpful extras.
3. **A smoother developer experience.**

4. **Flexible hosting and tooling.**

   Using Vite and Nitro means you can build and deploy anywhere. You're not locked into one company's stack or runtime.

The developers experimenting with TanStack Start aren't just building toy projects. They're using it for **production apps**, internal dashboards, and even company websites.

A few examples mentioned in community threads:

- A **real-time quiz app** built for an event, where switching from React Router 7 to TanStack Start fixed hydration issues right before launch.
- A **multi-language analytics dashboard** powered by Laravel on the backend and TanStack Start on the frontend, praised for its easy SSR setup.
- **Startups and indie projects** migrating from Next.js because they wanted more predictable code and simpler local hosting options.

Many devs say TanStack Start lets them **scale from side projects to production** without losing control or adding complexity.

This shift isn't just about replacing one framework with another. It reflects a broader change in what developers value.

For years, frameworks have chased automation and abstractions and trying to do more for the developer. But that often came with confusion, slower builds, and less transparency. TanStack's approach goes the other way. It gives developers clarity, type safety, and freedom to understand and shape their stack.

As one developer wrote, *"TanStack brings back sanity. It's a framework that 99% of devs actually want to use."*

TanStack Start is still young, but it's already making an impact. Its community is growing quickly, its documentation is improving fast, and it's backed by a team with a proven record of building tools developers trust.

Next.js isn't going anywhere, but developers are looking for something that feels simpler and more honest. TanStack Start gives them that: a framework that's powerful without being heavy, modern without being controlling, and familiar without being boring.

If you've ever wished React felt like React again, you'll probably understand why developers are leaving Next.js for TanStack Start, and loving it.
