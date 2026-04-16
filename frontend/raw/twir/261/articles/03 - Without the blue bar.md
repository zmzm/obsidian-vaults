---
type: twir-item
issue: 261
item: 3
item_type: item
date: 2025-12-03
source: https://wtbb.vercel.app/
tags:
status: auto
quality: keep
---

[[2025-12-03-TWIR-261|Index]]

# Item 3: Without the blue bar

Source: [https://wtbb.vercel.app/](https://wtbb.vercel.app/)

Summary:
Francisco Miranda presents a fully streamed, instant-loading GitHub repository view that eliminates the blue loading bar and preserves native browser search. The project demonstrates how streaming UI can significantly improve perceived performance and user experience over traditional loading indicators.

Key takeaways:
- Implements instant-loading UI for GitHub repo views using streaming.
- Removes traditional loading bars for a smoother experience.
- Maintains native browser search functionality.
- Example and repo available for exploration.

Recommendation:
Read fully (read fully if interested in streaming UIs or performance optimizations)

Why it matters:
read fully if interested in streaming UIs or performance optimizations

Content:
# Without the blue bar

I got nerd-sniped the other day by a [series](https://x.com/jaredpalmer/status/1979204222420664405) of [tweets](https://x.com/jaredpalmer/status/1985385707762802981) from [Jared Palmer](https://x.com/jaredpalmer) asking the community what could be done to improve GitHub.

I love GitHub, but my main concern is how slow it can get sometimes — and based on the replies to those tweets, I’m clearly not alone.

I started to think, as a user, about my non-negotiables for the GitHub experience:

- I want the experience to be fast, whether the content is large or tiny.
- I want to use the browser’s native search, because I rely on it constantly.

The first point is obvious.

The second one is more interesting: many performance techniques rely on virtualizing views, but the caveat is that native browser search only works on content that actually exists in the DOM and is visible (or at least “present”) to the browser. If the thing isn’t really there, Cmd+F won’t find it.

## A quick recap of list virtualization

I’ll use something familiar we all interact with every day: your phone. The concept existed long before, but it wasn’t until the iPhone that I really started paying attention to how it worked and why it felt so smooth.

Painting is expensive in computing — especially when resources are limited. You might have the latest Mac, but your browser still restricts how many resources a single tab gets. So even powerful machines hit limits.

And phones? Much more constrained.

When the first iPhone launched, the hardware constraints were even tighter. To deliver a good experience, Apple couldn’t afford to paint huge UI surfaces all at once. That’s where UITableView came in.

Back to the phone example: imagine you have ten thousand contacts. Painting every single contact would take a while, waste memory, and destroy the user experience. So instead, the system paints a single container that fills the screen, and then creates a limited number of “cells”. For the sake of keeping this simple, let’s say 10 visible cells, plus maybe 3 extra above and below as buffers.
[![virtual list](https://gist.github.com/user-attachments/assets/05baf529-9b27-4209-87df-a841e1e90db7)](https://gist.github.com/user-attachments/assets/05baf529-9b27-4209-87df-a841e1e90db7)

When you scroll down to contact number twelve, that cell is already painted. Contact number one has scrolled off-screen, and there’s no reason to keep rendering it, so the system reuses that now-invisible cell for the next contact that’s about to enter the viewport.

By recycling cells like this, the OS simulates a massive list while actually rendering only ~16 elements.

This pattern is everywhere: timelines, chat apps, feeds — basically anything that wants to feel “infinite” without melting your device. Parts of GitHub work exactly like this too, even if we don’t usually think about it while scrolling through issues or commits.

## GitHub already virtualizes blobs (in a genius way)

GitHub also wants to preserve native browser search while still virtualizing heavy views.

They already do this for large blobs: the visible portion of the file is syntax-highlighted and virtualized, and on top of that they place a full-height transparent `<textarea>` containing the raw code. The browser searches the textarea, the user sees the highlighted code, and both layers stay perfectly in sync.

[![image](https://gist.github.com/user-attachments/assets/dd6c19f1-1360-4ad5-8af5-8a853ed1ed3f)](https://gist.github.com/user-attachments/assets/dd6c19f1-1360-4ad5-8af5-8a853ed1ed3f)

## Why virtualization doesn’t help much in pull requests

When it comes to pull requests, virtualization doesn’t help as much — at least not with what I’ll call **the diff component** (the UI that shows the file patch in one or two columns).

These components rarely render more than ~100 lines at a time, so virtualizing them can actually hurt performance on large PRs instead of helping. The overhead isn’t worth it.

So what realistic options does GitHub have to improve the PR experience?

1. **Render the entire PR diff at once.**  
   (Probably GitHub’s original approach years ago)
2. **Lazy-load and schedule diff components via JavaScript.**  
   (Both the classic UI and the new UI do versions of this)
3. **Render diffs using a fast, non-DOM painting layer.**  
   (Canvas/WebGPU. But this breaks browser search, so GitHub would need to reinvent search, highlighting, and the entire rendering stack.)

Eventually, GitHub will likely need something like option 3. But getting there means outperforming the browser’s native search, implementing syntax highlighting in a custom renderer while keeping code indexable — for SEO and for AI.

That’s a long road.

There’s also the blue progress bar — hence the title of this post.

It’s not really a feature; it’s a symptom. It appears when the router is stalled doing expensive work: fetching data, loading chunks, running logic, painting. The more often you see it, the more your UI is blocking the user unnecessarily.

The goal isn’t to speed up the bar.  
The goal is to remove the need for it at all.

## My approach: a mix of #1 and #2 (but with a twist)

So when I got nerd-sniped, the first idea that came to mind was a mix of options 1 and 2 — but **with a twist**:

1. **Baseline 2024** for CSS and JS
2. **Avoid JavaScript** unless strictly necessary
3. **Stream** everything that can be streamed
4. **Use the fastest framework available**
5. **Protect the browser’s main thread**

You’ll quickly agree with #1 and #2.

By the time you hit #3, you’re already wondering about #4. So let’s address the elephant in the room.

It’s built on one of the fastest — and most battle-tested — UI runtimes out there, the same one GitHub uses internally today: React. You might disagree with “fastest”, and that’s fair, but here’s something harder to argue with: React has the largest ecosystem, the most documentation, and the biggest pool of developers.

There’s a reason Facebook stuck with PHP for so many years — ubiquity is a superpower.

> “But React is used by other frameworks too…”

True. But among all the React-based frameworks, Next.js is the one most aligned with React’s current and future direction. Choosing it immediately checks off items #2 and #3 for me (streaming + server-first mindset).

And by removing those concerns, I can finally address the next elephant in the room.

If I can move most rendering and logic to the server, the user experience improves immediately. You free up the main thread and reserve it for the moments when client-side JavaScript is actually needed.

RSC isn’t everyone’s cup of tea. I’ve used them in production with great results, and most of the backlash I see comes from trying to use them like a traditional SPA — usually with older patterns, older React versions, or libraries that weren’t designed for this model.

It’s a paradigm shift, just like server-side rendering was back in the day (and people still fight about that too).

For some projects, a regular SPA will absolutely perform better. That’s fine. But for this POC, RSC aligns perfectly with what I wanted: streaming, server-driven UI, and a main thread that isn’t suffocating under unnecessary work.

Thinking in terms of server components first forces us — as developers — to really question **when something truly needs to be a client component**.

That alone is a massive win for users, because **every client component is extra work the browser must do**. Most of the time, the honest answer is: “only when the thing cannot be serialized.”

That’s also why porting an existing SPA to RSC feels hard. It’s not PHP or any traditional server-side system, but it’s not a classic SPA either. It’s a hybrid. It takes some of the best ideas from both worlds, adds streaming, and then asks you to think carefully about where JavaScript actually belongs.

Next.js is not perfect, and I’ll address its issues in a separate post, but for this kind of experiment, RSC gave me exactly the foundations I needed.

## 1. Baseline 2024 for CSS and JS

One of the coolest additions in the latest Baseline is the `content-visibility` property. It isn’t virtualization in the strict sense, but it brings some of the same performance benefits **without** requiring a full virtual list implementation.

Going back to the “ten thousand contacts” example: `content-visibility` tells the browser:

> “Don’t bother painting this subtree unless it’s actually visible on screen.”

The element still exists in the DOM, and its layout footprint is preserved, but the browser skips all the heavy rendering work until needed.

It’s not as powerful as a real virtualizer — there’s no element reuse, and everything still exists in memory — but the performance win can be significant. And unlike true virtualization, off-screen content is still **searchable** with the native browser find tool, which is critical for something like GitHub.

[![content-visibility](https://gist.github.com/user-attachments/assets/85b99be8-cceb-4b7c-a381-ebcb91b6aec0)](https://gist.github.com/user-attachments/assets/85b99be8-cceb-4b7c-a381-ebcb91b6aec0)

It’s still not optimal, of course, because all of those contacts still need to exist in the DOM. But thanks to streaming, we can insert them gradually and show a fallback view via React’s `<Suspense>` while that happens.

This keeps the main thread free and avoids the “everything renders at once” bottleneck.

So why not apply `content-visibility` everywhere?

#### 1. It works best in chunks, not per item.

It’s far easier for the browser to decide whether a whole block of content should be painted than to evaluate dozens or hundreds of tiny individual elements one by one. Chunking gives you predictable behavior and better performance.

#### 2. The browser needs a size hint.

If the browser hasn’t painted an element yet, it doesn’t know its dimensions. Applying `content-visibility` blindly can cause unexpected layout jumps (CLS) as the user scrolls and the browser suddenly discovers the element’s true height.

Fortunately, Baseline 2023 introduced `contain-intrinsic-size`, which lets us provide a “fake” height/width up front — essentially telling the browser:

> “Pretend this block is X tall until you actually paint it.”

This eliminates layout shifts while still giving us the rendering savings from `content-visibility`.

## Getting to know GitHub’s front-end

I use GitHub every day, but it wasn’t until now that I really dug into its DOM.

For many years, GitHub relied on jQuery plus server-side templates to render its pages. As the product grew, that approach became harder to scale, and React became the natural way to simplify the UI, enforce consistency, and power a proper design system.

That design system is called **Primer**, split into two major pieces:

- **Primitives** (public and private components used across the interface)
- **Octicons** (the icon library)

Both libraries are beautifully crafted and extremely well documented. But for what I wanted to build, I couldn’t reuse them directly. They were designed with a **client-side mental model**, not a server-component one.

React 19 is smart enough to let you import a client component and serve it through the server where possible, but Primer Primitives make heavy use of hooks — even in places where you’d expect simple DOM elements. That forces them to be compiled as **client components**, which doesn’t align with a server-first architecture.

As GitHub matured its design system, they standardized on **design tokens** and use CSS variables throughout the UI to keep spacing, color, and typography consistent. Naming is famously one of the hardest problems in software, so they also defined clear conventions for how tokens should be referenced in code, making the system easier to scale and maintain.

[![image](https://gist.github.com/user-attachments/assets/f0b1963d-3d4d-42dc-a433-a68eb34f2cb7)](https://gist.github.com/user-attachments/assets/f0b1963d-3d4d-42dc-a433-a68eb34f2cb7)

They chose CSS Modules for Primitives to favor encapsulation and reusability — something I’ll come back to later in this post.

As design systems grow, being fully responsive becomes mandatory, not optional. Sometimes, designers can get a breakpoint wrong and present a totally different layout across sizes; in those cases, the only alternative is to have elements that render only on mobile and others only on desktop.

But that wasn’t often the case with the components I reviewed.

[![image](https://gist.github.com/user-attachments/assets/cfce09b8-8084-4dc7-91ed-740741c9ca63)](https://gist.github.com/user-attachments/assets/cfce09b8-8084-4dc7-91ed-740741c9ca63)

You’d expect full responsiveness to be handled at the CSS level, but some components rely on breakpoint-specific DOM duplication.

[![github resize](https://gist.github.com/user-attachments/assets/6b0ab011-19ff-4fb4-be38-ad57e20eb562)](https://gist.github.com/user-attachments/assets/6b0ab011-19ff-4fb4-be38-ad57e20eb562)

Individually, these shortcuts are small. But reused dozens of times in the same view, they add up — introducing visible lag, especially during resizes.

You can literally feel the UI “pushing back” when you resize the window.

To render what you see on GitHub, the platform relies on a mix of public and private data sources. It has some of the most thoughtfully designed GraphQL endpoints I’ve ever used, paired with a set of REST APIs — again, both public and private — for tasks that GraphQL alone can’t cover.

It’s worth noting that no single API exposes all the data needed to replicate GitHub’s UI. GraphQL is excellent for fetching exactly the fields required for a view, but you still need REST for things like converting Markdown to HTML, or retrieving patch data for pull requests.

In practice, GitHub stitches together multiple APIs behind the scenes to deliver what looks like a unified experience.

One clue that private APIs exist is a small but delightful feature in the web UI called **simplified paths**. If your repository contains deeply nested directories like this:

[![image](https://gist.github.com/user-attachments/assets/41640e9b-621b-4752-80ee-537a8a67468d)](https://gist.github.com/user-attachments/assets/41640e9b-621b-4752-80ee-537a8a67468d)

…the web interface collapses that folder hierarchy so you can jump straight to the files:

[![image](https://gist.github.com/user-attachments/assets/442e91a9-b5b9-4d5f-b1cf-3ab25d4a678e)](https://gist.github.com/user-attachments/assets/442e91a9-b5b9-4d5f-b1cf-3ab25d4a678e)

This relies on serialized metadata embedded directly into the HTML:

[![image](https://gist.github.com/user-attachments/assets/817bd34b-9a6a-4ffd-9816-6f86bb21c491)](https://gist.github.com/user-attachments/assets/817bd34b-9a6a-4ffd-9816-6f86bb21c491)

Unfortunately, this feature doesn’t exist in the GitHub mobile app. There, you need to tap through every layer of the folder tree — likely because the native app relies exclusively on the public GraphQL API, which doesn’t expose the data needed to compute simplified paths.

[![folders](https://gist.github.com/user-attachments/assets/e7adfcad-3f61-471e-9b6e-14fb50bf7f91)](https://gist.github.com/user-attachments/assets/e7adfcad-3f61-471e-9b6e-14fb50bf7f91)

With the framework in place — and after deciding to experiment with **cache components** — I began with the data-fetching layer. I went with GraphQL and chose **Relay** for the job.

When I first adopted RSC three years ago, Relay was the only library that somewhat supported server components. The integration was barely documented, but by digging through GitHub issues I found an approach that worked.

Relay still provides one of the best DX experiences out there: its compiler optimizes queries and fragments, and its IDE extension offers excellent autocomplete. Once you get used to that workflow, it’s hard to go back.

The most helpful tool in this entire POC, though, was **ChatGPT 5.1**. I could paste UI screenshots and ask for the GraphQL queries needed to replicate a view. It felt like pair-programming with someone who memorized the entire GitHub schema.

For styling, I’m using the latest version of **Tailwind**. It’s a personal preference, but it turned out to be a perfect fit for this project. Tailwind v4 is built on CSS variables, which made it easy to reuse GitHub’s existing design tokens.

Another advantage over GitHub’s current CSS-Modules approach is Tailwind’s **atomic nature**: as your component library grows, the final CSS bundle can remain essentially the same size. Combined with GitHub’s consistent spacing scale (multiples of 4), the entire design system can sit comfortably under ~20KB.

If you want even better performance, you can inline it into the root layout and skip CSS downloads altogether.

With the setup ready, I began porting GitHub’s tokens into Tailwind. At first I naively tried to migrate everything, but quickly realized it was better to add tokens incrementally as I needed them. I started with a single theme (dark mode), since additional themes can be layered later just by swapping variable values.

Once the design foundation was stable, the next step was recreating the repository layout in a fully responsive way — rather than relying on the breakpoint-specific show/hide patterns that are common in the original implementation.

[![ezgif-5a6031401fbac4bc](https://gist.github.com/user-attachments/assets/c3fe5277-e1ef-4197-9754-7c466617ef2b)](https://gist.github.com/user-attachments/assets/c3fe5277-e1ef-4197-9754-7c466617ef2b)

Once that was done, I replaced the colored placeholder blocks with the actual UI. I used Sketch with alignment guides to compare my layout against the real GitHub interface and push toward a pixel-perfect Tailwind port.

[![image](https://gist.github.com/user-attachments/assets/4353ab01-b019-4860-bf37-5df451e1e1e2)](https://gist.github.com/user-attachments/assets/4353ab01-b019-4860-bf37-5df451e1e1e2)

As I mentioned earlier, my approach with React Server Components is simple: render everything on the server unless there is a real reason not to. That meant skipping any pieces of the layout that would eventually become client components or, even better, “donut components”.

A good example is the file timestamp: the server can render a `<time>` element with an ISO date, and the client can hydrate only that tiny donut to localize it based on the user’s timezone.

But for this POC, I wanted to move fast, so I avoided almost all client components and kept the entire UI server-rendered — except for the “scroll to top” button in the sticky header for blob and tree views.

I also ported several GitHub interactions that can be done entirely in CSS, without client-side JavaScript:

---

Hiding or revealing the number of visible files on mobile, using only `<input>` + `<label>` tricks.

[![expand](https://gist.github.com/user-attachments/assets/eaae427b-a87a-46d0-bda3-20b6d1b2a9fc)](https://gist.github.com/user-attachments/assets/eaae427b-a87a-46d0-bda3-20b6d1b2a9fc)

---

Toggling commit details with the same pure-CSS technique.

[![expand view](https://gist.github.com/user-attachments/assets/3e6de27e-44da-45ed-abfd-1c8d7dcd2638)](https://gist.github.com/user-attachments/assets/3e6de27e-44da-45ed-abfd-1c8d7dcd2638)

---

Implementing the sticky header behavior — including removing border radius when it “sticks” — using an old-school CSS technique instead of JS.

[![expand](https://gist.github.com/user-attachments/assets/001d0c57-3788-42eb-8744-f740772127db)](https://gist.github.com/user-attachments/assets/001d0c57-3788-42eb-8744-f740772127db)

---

GitHub’s version uses JS and has a visible “jump” when the sticky header activates.

[![expand](https://gist.github.com/user-attachments/assets/0daa62fa-182b-4ba4-bd09-7abc953183e8)](https://gist.github.com/user-attachments/assets/0daa62fa-182b-4ba4-bd09-7abc953183e8)

The next step was building skeletons for the views I already had.

I animated them using simple opacity transitions so they only touch the “[composite](https://motion.dev/blog/web-animation-performance-tier-list)” stage of the rendering pipeline instead of animating `mask-image` the way GitHub does, which forces both paint + composite and is noticeably heavier.

[![skeleton opt](https://gist.github.com/user-attachments/assets/c2a3ae71-e062-4cab-b3cf-5a573ee0f7d9)](https://gist.github.com/user-attachments/assets/c2a3ae71-e062-4cab-b3cf-5a573ee0f7d9)

The goal was simple: keep the perception of motion, remove as much rendering cost as possible.

## Streaming and cache components

With the skeletons in place, it was time to implement streaming.

Next.js 16 introduced **cache components**, which make data dependencies explicit and push more work into the server runtime. When this flag is enabled, Next.js warns you whenever a component reads async data without being wrapped in `<Suspense>`, or when a synchronous boundary would block partial rendering.

This matters because — starting in recent versions — Next.js intentionally treats most runtime data as async to unlock earlier streaming. Without cache components enabled, these issues are swallowed silently; with the feature on, the framework surfaces them so you can structure your tree for maximum parallelism.

In practice, it forces you to design components the way React expects:

- async when they need async data
- streamable where they can defer
- explicit about what is allowed to block

Once everything lines up, you get much better partial rendering and **almost instant route transitions**.

## Simulating virtualization with RSC + content-visibility

Since I’m not virtualizing any views — that’s a client-side technique — I took a different approach to simulate some of its benefits in blob views using a combination of `content-visibility`, `contain-intrinsic-size`, and `<Suspense>`.

GitHub does something similar today for large blobs: they virtualize only the highlighted lines and overlay a transparent textarea to preserve native text selection and browser search. I wanted to keep that spirit, but adapt it to a server-streamed environment.

For this POC, GitHub doesn’t expose a syntax-highlighting API, but it does expose an endpoint to convert Markdown into HTML. So the pipeline looks like this:

1. Fetch raw blob text.
2. Wrap it in backticks with the file extension.
3. Send it to the Markdown API for HTML-highlighted output.
4. Split into lines; wrap each in a `<div>`.
5. Group lines into chunks with `content-visibility: auto`.
6. Give each chunk a deterministic `contain-intrinsic-size` based on the line count so the browser can reserve space before painting.
7. Use `<Suspense>` to show a `<pre>` fallback while chunks stream.

The result is imperceptible in small files — which is exactly what you want — but becomes extremely noticeable in large ones: smooth scrolling, fast search, and significantly reduced main-thread pressure.

[![large file](https://gist.github.com/user-attachments/assets/5488b781-5b91-4dcf-969c-845f4f6d47d1)](https://gist.github.com/user-attachments/assets/5488b781-5b91-4dcf-969c-845f4f6d47d1)

## Caching, activity, and prefetching

Cache components also introduce the `'use cache'` directive, which lets you enable smart, granular caching without wiring everything manually. Combined with React’s newest **Activity** primitives, links can now be prerendered — preserving component state across route transitions and eliminating that subtle “reset” feeling typical of full reloads.

Once I enabled this and added prefetch to many of the links in the interface, the navigation experience became essentially **instant**.

You could argue that this results in “too much prefetching”, but that’s actually desirable:

a) it dramatically improves perceived performance, and  
b) in a real-world GitHub scenario, most of these requests would already be cached globally, and GitHub could easily invalidate them with a hook whenever a file changes.

The result feels closer to a native app than a website — yet it’s still just HTML, CSS, and JS.

I still haven’t built the pull-request functionality — that part is only halfway done.

Hopefully, this repo will also serve as a useful reference for other developers exploring RSC and cache components — or for anyone who’s ever looked at the blue bar and thought:

> “What if this didn’t have to be here at all?”
