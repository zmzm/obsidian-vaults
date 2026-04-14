---
type: twir-item
issue: 256
item: 6
item_type: item
date: 2025-10-29
source: https://www.lorenstew.art/blog/10-kanban-boards
tags:
  - "10"
  - "Nextjs"
  - "EAS"
status: auto
quality: keep
---

[[2025-10-29-TWIR-256|Index]]

# Item 6: I Built the Same App 10 Times: Evaluating Frameworks for Mobile Performance

Source: [https://www.lorenstew.art/blog/10-kanban-boards](https://www.lorenstew.art/blog/10-kanban-boards)

Summary:
The author built a Kanban app in ten different frameworks to evaluate mobile web performance, focusing on bundle size and load times for real-world users (e.g., real estate agents in low-connectivity environments). The results show dramatic differences in bundle sizes and performance, with Marko and Qwik City leading in minimal JavaScript delivery and instant interactivity, while Next.js lags with significantly larger bundles. The post argues that framework architectural choices have a direct, measurable impact on user experience, especially on mobile.

Key takeaways:
- Bundle size varies up to 6x between frameworks, directly affecting mobile load times and user experience.
- Marko and Qwik City use resumability to eliminate traditional hydration, achieving the smallest bundles.
- SPA frameworks (e.g., Next.js) have higher baseline JS costs than MPA or resumability-based frameworks.
- Mobile performance is critical for user retention and brand perception, especially in bandwidth-constrained scenarios.

Recommendation:
Read fully (for those making framework decisions or concerned with mobile performance)

Why it matters:
for those making framework decisions or concerned with mobile performance

Content:
# I Built the Same App 10 Times: Evaluating Frameworks for Mobile Performance

## Why I Built This

My team needed to choose a framework for an upcoming app. The requirements were clear: it had to work well on mobile. We’re building tools for real estate agents working in the field. They need to use our apps at open houses, in parking lots, and in areas with spotty cellular signals. When someone’s standing in front of a potential buyer trying to look professional, a slow-loading app makes them look unprofessional.

I started with what seemed like a reasonable comparison: Next.js (our current default when a framework is required) versus SolidStart and SvelteKit (alternatives I’d heard good things about). I thought comparing three frameworks should be straightforward. But when I built the first implementations and measured bundle sizes, I noticed significant differences. Next.js bundles came in at 154 to 176 kB compressed, while SolidStart and SvelteKit delivered 30 to 54 kB compressed. I wondered if these differences were specific to individual framework implementations, or were they systematic across framework families? If React, Angular, and Vue all share similar architectural approaches, would their bundle sizes follow similar patterns? I decided to expand the evaluation to find out.

That question changed the scope. If I was going to make a real recommendation for the team, I needed to test all the major meta-frameworks and understand the full landscape of alternatives. Three frameworks became ten. What started as a practical evaluation for work turned into something bigger: a semi-comprehensive look at what’s actually possible for mobile web performance in 2025.

If you’re interested in the theoretical implications of why framework diversity matters, I wrote about that in [React Won by Default](/blog/react-won-by-default). This post focuses on the data.

This post shares what I discovered after writing kanban app in all ten frameworks. At the extremes are Marko, which delivers 12.4 kB raw (6.8 kB compressed) bundles for the homepage and Next.js which ships 486.1 kB raw (150.9 kB compressed) bundles for the homepage. That’s a 39x difference in raw size for the homepage. For the board page, Marko delivers 88.8 kB raw (28.8 kB compressed) versus Next.js’s 563.7 kB raw (176.1 kB compressed), a 6.11x difference in compressed size. These differences translate to real seconds on cellular networks.

The code can be found [here](https://github.com/lorenseanstewart/kanban-comparison)

---

## Why Mobile Web Performance Matters

For this evaluation, mobile performance was the primary constraint. Our users are real estate agents working in the field. They need our technology to work well at open houses with 30 people hammering the same cell tower, in parking lots between showings, and other places that are not a desk with WiFi. Our agents need tools that work quickly, not “eventually load.”

The company I work for does not have the resources to build a native app. We’re building for the web, which means if it has a URL, people will access it on their phones. And for our users, the app could be used on a phone just as frequently as a desktop.

This reality shaped the evaluation. I couldn’t just pick a framework that “works on mobile.” I needed something that genuinely performs well on cellular connections. The difference between a framework shipping 30 kB versus 170 kB isn’t academic. It’s the difference between an app that feels professional and one that makes our users look bad in front of clients.

**The business cost of slow performance**: Research from [Tammy Everts at SpeedCurve](https://www.speedcurve.com/blog/downtime-vs-slowtime/) reveals something surprising. While site *downtime* causes 9% permanent user abandonment, *slow performance* causes 28% permanent abandonment. That’s over 3x worse. In fact, slowdowns occur 10x more frequently than outages, resulting in roughly 2x total revenue impact despite lower per-hour costs. Beyond the abandonment numbers, slow performance creates a psychological effect where users start perceiving your entire brand negatively. Content seems “boring,” design looks “tacky,” even when those elements haven’t changed. Slowness poisons everything.

**The real-world cost:** A 147 kB difference at 3G speeds (1.6 Mbps, 150ms RTT) translates to roughly 1 second additional download time plus 500ms to 1s for parse and execution on mobile CPUs. Total: 1.5 to 2 seconds slower between frameworks. Even as 3G networks phase out, the real estate agents we’re building for regularly experience 3G-equivalent speeds. Crowded open houses, parking lots between showings, and properties in low-coverage areas (this varies by cellular provider) all create spotty 4G conditions where 10 Mbps degrades to 1 to 2 Mbps. A 147 kB bundle difference still translates to 1+ second delays on congested 4G.

**“But it’s cached!”** This objection misses reality. Cache busting is standard. Every deployment means users download again. First impressions matter. So do second, third, and tenth impressions. Your users remember negative experiences far more than positive ones.

This is why I expanded the evaluation beyond the initial three frameworks. I needed to see the full range of options. When someone pulls up the app in a parking lot between showings, every second counts. Building for mobile performance first means desktop on WiFi is excellent by default. The reverse isn’t true. Optimize for desktop and mobile users suffer.

I discovered the difference between frameworks reflects fundamentally different engineering priorities. Some frameworks prioritize runtime flexibility, shipping extensive abstractions to support wide use cases. Others prioritize runtime size and mobile performance from the ground up. The bundle sizes I measured for the board page varied by up to 6.1x (from 28.8 kB compressed to 176.1 kB compressed), differences that matter enormously on cellular networks.

---

## Key Takeaways (TL;DR)

> **All Tested Frameworks Achieve Instant FCP:** Modern frameworks achieve excellent First Contentful Paint performance in the 35-71ms range, making initial page load feel instant across the board. The real differentiator is bundle size: frameworks range from 28.8 kB (Marko) to 176.1 kB (Next.js) compressed, a 6.1x difference that impacts mobile users through increased data usage, longer parse times, and greater battery drain on every visit.
>
> **Bundle Size Champion: Marko** delivers 88.8 kB raw (28.8 kB compressed) for the board page, 6.11 times smaller than Next.js’s 563.7 kB raw (176.1 kB compressed). This is 31% smaller than the next closest competitor (SolidStart at 41.5 kB compressed), making Marko the clear choice when bundle size is the absolute top priority.
>
> **Resumability Pattern: Marko and Qwik City** both eliminate traditional hydration via resumability. Marko achieves the smallest bundles (28.8 kB compressed) through build-time analysis, while Qwik (58.4 kB compressed) uses lazy resumability with progressive loading. Both deliver instant interactivity without re-executing components on the client.
>
> **Nuxt Proves Established Frameworks Can Compete:** At 224.9 kB raw (74.7 kB compressed) with 38ms FCP, Nuxt demonstrates that established “big three” frameworks can achieve next-gen performance when properly configured. Vue’s architecture allows competitive mobile web performance while maintaining a mature ecosystem. React and Angular show no path to similar results.
>
> **Critical scaling difference**: MPA frameworks (Marko, HTMX) ship minimal JavaScript per page, staying lean as you add features. SPA frameworks ship routing and framework runtime upfront, with higher baselines even using code splitting. Marko delivers around 12.4 to 88.8 kB raw regardless of total routes. SPAs maintain 83.9 to 563.7 kB raw baselines plus route chunks.

The dominant frameworks show dramatically different bundle sizes. **TanStack Start (React)** achieves 373.6 kB raw (118.2 kB compressed) bundles using React 19, only 1.49 times better than Next.js’s 563.7 kB raw (176.1 kB compressed). **Angular** has achieved competitive bundles via Analog at 376.3 kB raw (103.9 kB compressed), positioning it similarly to TanStack Start and ahead of Next.js. **Vue** (via Nuxt) proved even better, achieving 224.9 kB raw (74.7 kB compressed) bundles that matches next-gen frameworks.

Meanwhile, next-gen frameworks like **SolidStart** deliver 128.6 kB raw (41.5 kB compressed) bundles, 4.24 times smaller than Next.js and 2.85 times smaller than TanStack Start with React. The perfect controlled comparison: TanStack Start with React (373.6 kB raw) versus TanStack Start with Solid (182.6 kB raw). Same meta-framework, same patterns, but React bundles are 2x the size of Solid, isolating React’s runtime cost.

**Mobile is the web.** These measurements matter because mobile web is the primary internet for billions of people. If your app is accessible via URL, people will use it on phones with cellular connections. Optimizing for desktop and hoping mobile is good enough is backwards. The web is mobile. Build for that reality.

Each build uses the same database, features, and UI so the comparison stays fair. The differences in bundle size for the board page range from 4.24 to 6.11 times smaller compared to Next.js for modern alternatives. **Important: These measurements represent disciplined baseline implementations with minimal dependencies.** Real production apps typically ship 5 to 10 times more JavaScript from analytics, authentication, feature flags, and third party libraries, meaning the framework differences compound significantly in practice. On mobile devices with cellular connections, this matters enormously.

---

## Bundle Size Reality Check

React (via Next.js) ships 150.9 to 176.1 kB compressed (486.1 to 563.7 kB raw). Angular (via Analog) ships 103.9 kB compressed (376.3 kB raw) for both pages, achieving competitive bundle sizes that position it similarly to TanStack Start and ahead of Next.js, though still heavier than next-gen frameworks. Vue (via Nuxt) stands apart from both. Nuxt ships even more competitive bundle sizes at 74.7 kB compressed (224.9 kB raw), making it the only “big three” meta-framework that competes on mobile web bundle sizes. React requires architectural changes to achieve similar results. Angular (via Analog) has shown improvement but remains heavier than next-gen alternatives. Nuxt proved that with proper optimization, even established frameworks can deliver competitive bundle sizes.

**React’s explicit strategy:** React Native for mobile. The architectural choices that make React heavy on the web are deliberate and solve real problems for desktop development. But for mobile web, React’s position is: use React Native instead. The tradeoff is that React Native pushes developers into app stores where platform holders extract up to 30% of transactions and control distribution.

Other frameworks are designed so that, with discipline, developers can create great mobile experiences. The teams behind Marko, Solid, Svelte, Qwik, and Vue have built solutions that optimize for the web as a first-class platform for mobile.

### Board page bundle sizes (smallest to largest)

![Bundle Sizes](/images/kanban-bundle-size-comparison.svg)

**Performance context**: All frameworks tested achieve excellent Lighthouse scores (100) with similar First Contentful Paint times. Since performance is essentially identical, **bundle size is what differentiates these frameworks** for mobile users. The 6.1x range matters for data usage, parse time, and battery consumption.

**Field data validation**: The [Chrome User Experience Report (CrUX)](https://lookerstudio.google.com/u/0/reporting/55bc8fad-44c2-4280-aa0b-5f3f0cd3d2be/page/M6ZPC?params=%7B%22df44%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580AngularJS%25EE%2580%2580Nuxt.js%25EE%2580%2580Next.js%2520App%2520Router%25EE%2580%2580Astro%25EE%2580%2580SvelteKit%25EE%2580%2580Qwik%25EE%2580%2580SolidStart%22,%22df46%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580mobile%22%7D) provides real-world Core Web Vitals data from millions of actual websites using these frameworks on mobile devices. This field data complements the controlled measurements in this post. Important caveat: CrUX data reflects how these frameworks are used in production by average developers, not optimal implementations. If a framework shows poorly in CrUX but well in these tests, it demonstrates what’s possible with proper configuration, performance tuning, and dependency discipline. The gap between field data and optimized implementations reveals opportunity for improvement in real-world usage patterns.

The difference between Marko’s 88.8 kB raw (28.8 kB compressed) and Next.js’s 563.7 kB raw (176.1 kB compressed) translates to roughly 1.5 seconds on cellular. These seconds are the baseline. Time waiting to load increases with every feature and every dependency added.

**Important context on HTMX**: Astro + HTMX achieves its small footprint with the simplest codebase by trading client-side reactivity for server-driven interactions. For apps requiring rich client-side state, Marko, Solid, and Svelte deliver full reactivity while staying lean.

---

> Before diving in, a reminder from my [Progressive Complexity Manifesto](/blog/progressive-complexity-manifesto): The frameworks compared here represent Level 5 complexity. They are powerful tools for when you need unified client-side state, a lot of reactivity, and/or client-side navigation. But most applications thrive at lower levels. For instance, Level 3 (server-rendered HTML enhanced with HTMX and vanilla JavaScript, as demonstrated in the kanban-htmx app in this repo) can handle complex interactive applications with minimal JavaScript. Level 4 adds occasional Web Components using Lit for reusable elements. These simpler approaches often deliver even smaller bundles and much simpler codebases. This post focuses on Level 5 options for cases that demand them, while remembering simpler paths often suffice.

## The Experiment Setup

I built a Kanban board application ten times, once in each of these frameworks: [**Next.js 16**](https://nextjs.org/) (React 19 with built-in compiler) representing React’s Virtual DOM approach with automatic optimization, [**TanStack Start**](https://tanstack.com/start/latest/docs/framework/react/overview) (also React 19) for a leaner React meta-framework without App Router overhead, [**TanStack Start + Solid**](https://tanstack.com/start/latest/docs/framework/solid/overview) (SolidJS 1.9) using the same meta-framework with fine-grained reactivity, [**Nuxt 4**](https://nuxt.com/) (Vue 3) for Vue’s reactive refs with SSR-first developer experience, [**Analog**](https://analogjs.org/) (Angular 20) using Angular’s modern signals API with meta-framework tooling, [**Marko**](https://markojs.com/docs/marko-run/getting-started) (@marko/run) for streaming SSR with fine-grained reactivity, [**SolidStart**](https://docs.solidjs.com/solid-start/) (SolidJS 1.9) for native Solid integration with fine-grained reactivity through signals, [**SvelteKit**](https://svelte.dev/docs/kit/introduction) (Svelte 5) for fine-grained reactivity with runes, [**Qwik City**](https://qwik.dev/docs/qwikcity/) for resumability instead of hydration, and **[Astro](https://astro.build/) + [HTMX](https://htmx.org/)** for a traditional MPA approach.

Each implementation includes the exact same features: board creation and listing pages, four fixed lists per board (Todo, In Progress, QA, Done), full CRUD operations for cards, drag-and-drop card reordering within lists and movement between lists, assignee assignment from a static user list, tag management, comments on cards with authorship tracking, completion status toggles, optimistic UI updates for drag-and-drop and chart changes (HTMX lacks this though), and server-side form validation using [Valibot](https://valibot.dev/).

All ten apps share the same foundation. The database is SQLite with [Drizzle ORM](https://orm.drizzle.team/) using an identical schema across all implementations. Styling comes from [Tailwind CSS](https://tailwindcss.com/) plus [DaisyUI](https://daisyui.com/) to keep the UI consistent. Each framework implementation contains roughly 17 components. Most importantly, every app performs real database queries against relational data (boards → lists → cards → tags/comments/users) rather than working with hardcoded arrays.

You can check out the code [here](https://github.com/lorenseanstewart/kanban-comparison).

**A critical choice about dependencies**: These apps intentionally minimize dependencies compared to what many developers typically reach for. For mobile web applications, every dependency represents a choice to ship additional kilobytes to users. I used necessary UI libraries like drag-and-drop packages (which vary by ecosystem), but deliberately avoided data fetching libraries, state management helpers, and other utilities that frameworks already handle natively. Each ecosystem has popular packages that add convenience but increase bundle size (React developers often reach for tanstack-query for data fetching, state management libraries, or form helpers). To illustrate the trade-off: tanstack-query alone weighs approximately 13 kB gzipped. That single dependency is already larger than Marko’s entire homepage bundle at 6.8 kB. By avoiding these “nice to have” dependencies and using each framework’s built-in capabilities instead, the bundle differences you’ll see reflect framework architectural choices, not different amounts of functionality or third-party helpers.

**Measurement Methodology**: All bundle sizes represent production build artifacts measured using Chrome Lighthouse. I report both raw (uncompressed) JavaScript sizes and compressed transfer sizes. The raw size reflects actual code volume generated by each framework and is more consistent for comparison since it doesn’t vary by server compression settings. The compressed size shows what users actually download over the network. All implementations use identical functionality, database, and UI framework to ensure fair comparison. See the complete [measurement methodology](https://github.com/lorenseanstewart/kanban-comparison/blob/main/METHODOLOGY.md) for details.

---

### React’s Ceiling in Practice (TanStack vs Next)

**TanStack Start achieves 98.3 to 118.2 kB compressed bundles (309.4 to 373.6 kB raw) while Next.js ships 150.9 to 176.1 kB compressed (486.1 to 563.7 kB raw).** Both use React 19. That’s only a 33 to 35% improvement, primarily reflecting App Router + RSC overhead.

Next.js ships the full React Server Components runtime plus serialization layers, component boundary management, caching infrastructure, App Router with all its routing features, progressive enhancement for Server Actions, image optimization, and middleware. TanStack Start strips most of that out: traditional SSR without RSC, leaner routing, and simple RPC-style server functions.

Both use server-side rendering, but Next.js’s RSC model adds substantial overhead. Server Components render on the server only, Client Components get marked with the `"use client"` directive, the server serializes everything to a special format, and the client needs runtime code to deserialize and coordinate those boundaries. TanStack Start uses the simpler traditional SSR approach: render on server, ship HTML, hydrate everything on the client. No serialization, no boundary coordination.

In this measurement, Next.js’s App Router + RSC adds roughly 53 to 58 kB compressed. The remaining 98.3 to 118.2 kB compressed (309.4 to 373.6 kB raw) is React’s core runtime costs associated with reconciliation, event system, and hydration.

**TanStack Start with Solid proves the point:** using the same meta-framework with Solid instead of React delivers 182.6 kB raw (60.4 kB compressed), 49% smaller than TanStack Start with React. That’s 42% larger than SolidStart’s 128.6 kB raw (41.5 kB compressed) due to TanStack Router having more features, but still far better than any React option.

Compare React’s baseline to other frameworks. **Marko** delivers 6.8 to 28.8 kB compressed (12.4 to 88.8 kB raw), **4.1x smaller than TanStack Start** with React. **SolidStart** delivers 29.8 to 41.5 kB compressed (83.9 to 128.6 kB raw) using JSX, 2.85x to 3.30x smaller. **SvelteKit** achieves 47.8 to 54.1 kB compressed (103.4 to 125.2 kB raw), 2.06x to 2.18x smaller. **Qwik** delivers 42.5 to 58.4 kB compressed (86.5 to 114.8 kB raw), 2.02x to 2.31x smaller.

**React’s architecture (not just the Virtual DOM, but also synthetic events, platform patching, and sheer feature complexity) creates unavoidable costs that no meta-framework optimization can eliminate.** Virtual DOM implementations can be small (see Preact at 4 kB). React’s size reflects deliberate choices to circumvent platform constraints and provide extensive features. To escape this ceiling and achieve 3 to 4 times smaller bundles, you need a fundamentally different architectural approach. Frameworks that lean into the platform instead of circumventing it can deliver significant size reductions. The React team chose to accept these costs to solve other problems (Server Components, unified patterns). That’s a legitimate choice. But it’s not negotiable within React.

## Addressing Common Critiques

I know what some of you are thinking. “Aren’t you comparing MPAs to SPAs unfairly?” And “Is this app complex enough?”

**App Complexity Defense**: This isn’t some toy todo list. It’s a solid mid-complexity app with real database persistence using SQLite plus Drizzle ORM, relational queries across boards to lists to cards to tags and comments, drag-and-drop reordering, (some) optimistic updates, modals, and server validation. It matches the kind of internal tools or MVPs teams crank out every day. The bundle differences come straight from framework overhead, not the features themselves, and those gaps only get bigger at scale with more routes and dependencies. If your production app throws in auth or real-time features, framework baselines would just balloon even more, not shrink.

**MPA vs SPA Nuances**: The routing pattern debate misses the point, reactivity models matter way more. With features like [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) and the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API), MPAs like Marko or HTMX feel just as snappy as SPAs for navigation. The real split is in scaling. MPAs ship minimal JS per page, for example Marko sticks to 6.8 to 28.8 kB, while SPAs lug around upfront runtime from 83.9 to 563.7 kB baselines plus chunks.

**A Note on Ecosystems**: the “small ecosystem” concern is often overstated. For mobile-first applications, we should be extremely selective about every dependency we add. Each package increases bundle size and maintenance burden. Modern AI tools like Claude, ChatGPT, and Cursor excel at generating focused code for your specific use case. Instead of importing a 50 kB library for 3 features, AI can help you write exactly what you need in 2 kB. This approach yields smaller bundles, code you actually understand, and [fewer supply chain risks](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/). Large ecosystems are sometimes advantageous, but they’re also a liability when every import costs your mobile users.

## The Verdict: What I’m Recommending

With ten implementations complete (see acknowledgements below for a list of the kind people who helped improve my code) and all measurements gathered, the data gives clear direction for our mobile-first requirements:

**All frameworks deliver instant initial load.** The meaningful difference is bundle size. Bundles have a 6.1x gap at the extremes (28.8 kB to 176.1 kB compressed) that affects mobile users through data costs, parse time, and battery drain. Choose based on bundle size priorities and developer experience.

That said, context matters. Not every project can or should switch frameworks.

**When Next.js still makes sense:** For large existing React codebases, migration costs may outweigh performance benefits. If you’re stuck with React and can’t migrate, consider TanStack Start over Next.js for a 33-35% bundle reduction without App Router complexity. For greenfield projects, though, there’s no legacy to maintain, no migration costs to weigh. Choosing to build on a foundation that costs users 2x to 3x more JavaScript on every visit means voluntarily accepting worse performance when better options cost nothing extra. “We only know React” isn’t a technical constraint, it’s a learning investment decision. And “organizational politics” is real, but it’s not a technical justification. It’s an admission that better options exist but can’t be chosen.

**Reality check on common objections:**

**“But hiring!”** Competent developers learn frameworks. These alternatives are actually easier to learn than React: no rules of hooks, no dependency arrays, no manual memoization dance. The real difficulty isn’t learning curve, it’s creating a engineering culture that acknowledges constraints and makes intentional decisions with these constraints in mind.

**“But ecosystem!”** React’s ecosystem is both advantage and liability. Large libraries ship code for scenarios you’ll never encounter. That date picker with every locale? You need 3 features, you’re shipping 300. For mobile-first projects where every kilobyte matters, this becomes a problem. Modern AI tools make building exactly what you need feasible: generate the function instead of importing 50kB for 3 features. Smaller bundles, code you understand.

**“But it’s risky!”** Shipping 3x larger bundles to mobile users on cellular is the actual risk. Slow loads damage your brand and cost conversions. The “safe choice” has measurable costs.

**“But my users are desktop-only!”** Let’s be honest, “desktop-only” is usually an excuse to skip performance discipline entirely. And it’s rarely true for long. Six months later someone asks “can I check this on my phone?” and suddenly you’re stuck. Better to build it right from the start. Desktop users still benefit from faster parsing and execution. Even on WiFi, 29.8 kB compressed loads noticeably faster than 176.1 kB compressed. More importantly, why would you voluntarily accept 3x worse performance when the better option costs nothing extra? Performance is a feature regardless of screen size. Building with constraints makes you a better engineer. “Desktop-only” shouldn’t mean “no discipline.”

**Why you should seriously consider the alternatives**: With these next-gen frameworks, performance comes by default. They have 2x to 6x smaller bundles and require much less optimization work. You’ll write less code, ship less JavaScript, and debug fewer framework quirks. Most importantly, greenfield projects deserve choices made on merit rather than defaults.

**These alternatives are especially compelling** for mobile-first applications where bundle size directly impacts user experience. Mobile professionals like real estate agents, field service workers, healthcare staff, delivery drivers, and sales reps working on cellular connections benefit most. Building one performant web app instead of separate web, iOS, and Android codebases means smaller teams, substantially lower development costs, and faster iteration cycles.

### Choosing among the alternatives (organized by primary use case):

**Smallest Bundles: Choose Marko** for the absolute best bundle sizes (6.8 to 28.8 kB compressed). Marko is the clear winner when bundle size is your top priority. The MPA architecture ships minimal JavaScript per page, staying lean as you add routes. The developer experience is excellent once you embrace its streaming model. If you prefer an html-first approach, Marko is the only option here (although SvelteKit comes close). Note: Marko 6 is currently in beta (tagged as `next` on npm) and expected to leave beta by end of year, with no expected API changes but ongoing bug fixes and optimizations.

**JSX Familiarity: Choose SolidStart** if you want the easiest migration path from React. SolidStart uses JSX syntax with automatic dependency tracking that eliminates manual memoization, while feeling immediately familiar to React developers. The mental model is actually simpler than React because signals are more straightforward than hooks.

**Best All-Around Developer Experience: Choose SvelteKit** for approachable syntax and excellent defaults. At 125.2 kB raw (54.1 kB compressed), SvelteKit delivers 3.26x smaller bundles than Next.js with progressive enhancement by default and minimal framework overhead. The compiler-based approach means less runtime code and cleaner component logic. With its focus on authoring in plain JS, CSS, and HTML, SvelteKit is best for developers from any background seeking readable code with few framework quirks.

**Resumability Pattern: Choose Marko or Qwik City** if you want to eliminate traditional hydration overhead. Both avoid re-executing components on the client, but with different approaches. **Marko** (6.8 to 28.8 kB compressed) achieves the smallest bundles through build-time analysis, bundling exactly the code needed for events and effects with no lazy loading. **Qwik City** (42.5 to 58.4 kB compressed) uses lazy resumability, progressively loading JavaScript based on actual interactions. Choose Marko for absolute smallest bundles, Qwik for applications with significant client-side functionality that benefit from progressive loading.

**Established Ecosystem: Choose Nuxt** if you want Vue’s mature ecosystem with competitive mobile web performance. At 224.9 kB raw (74.7 kB compressed), Nuxt proves that established “big three” 

... (content truncated)
