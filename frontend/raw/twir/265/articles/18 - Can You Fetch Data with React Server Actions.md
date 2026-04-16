---
type: twir-item
issue: 265
item: 18
item_type: item
date: 2026-01-21
source: https://wtbb.vercel.app/i-love-dogs
tags:
status: auto
quality: keep
---

[[2026-01-21-TWIR-265|Index]]

# Item 18: Can You Fetch Data with React Server Actions?

Source: [https://wtbb.vercel.app/i-love-dogs](https://wtbb.vercel.app/i-love-dogs)

Summary:
This article examines whether React Server Actions (Server Functions) should be used for data fetching from client components. It explains how Server Actions work, their underlying POST request mechanism, and the pros (type safety, simplicity) and cons (lack of HTTP caching, no fetch memoization) of using them for data fetching. The author concludes that while technically possible, developers should weigh trade-offs, especially regarding caching and intended use.

Key takeaways:
- React Server Actions can be used for client-initiated data fetching, but are POST-based and lack HTTP caching.
- They offer strong type safety and a simple API, but may not be optimal for all data-fetching scenarios.
- The decision depends on project requirements and trade-offs between convenience and caching.
- Developers should understand the underlying mechanics and limitations before adopting this pattern.

Recommendation:
Read fully (for those considering Server Actions for client-side data fetching)

Why it matters:
for those considering Server Actions for client-side data fetching

Content:
# I Love Dogs

I really do, and I owe them more than I can explain. They’re part of my family — and in many ways, they’re the reason I have one. I met my wife and her dog while walking mine in the park.

Whenever I get stuck on a problem, my dog wagging her tail and asking to go outside forces a pause. And that pause often gives me a new perspective.

I try to be a responsible owner. I don’t anthropomorphize my dogs, and I’ve spent time training them. If my dog ever bites someone, that’s on me — I’m accountable.

And everything I just said applies to AI, too.

Following a classic three-act structure — adapted to software development — we can roughly split the workflow into three parts.

The **introduction** is where work is conceived. Tasks are created, issues are triaged, and ideas take shape. This is where companies like [Linear](https://linear.app) already outperform GitHub: AI helps categorize, prioritize, and even automate large parts of this phase with very little friction.

The **central development** is rapidly shifting toward AI as well. Tools like [Cursor](https://cursor.com) are leading the way, but they’re not alone. Everyone is fighting for this space — whether it’s an agent running in your terminal or a fully AI-powered platform like [V0](https://v0.app).

The **conclusion** is the part that interests me the most — and it should interest GitHub too. This is where code gets reviewed, approved, and shipped. This part of the workflow should be deeply user-centered, giving developers the right tools to understand changes and move confidently, the way tools like [Graphite](https://graphite.com) do.

AI will almost certainly dominate the introduction and much of the central development. But the conclusion feels different.  
AI won’t rant on social media if an MCP call takes too long. Humans will complain if reviewing a pull request is slow.

**GitHub has a unique opportunity.**

It’s the only platform that spans the entire development lifecycle — from planning and coding to reviewing and shipping. Like many companies, GitHub has felt pressure to integrate AI, often in the form of chatbots or RAG-based assistants.

That’s fine. But the real opportunity isn’t another chatbot.

It’s using AI in a way that quietly supports developers across the workflow — especially in the part where humans are most involved: reviewing pull requests.

That’s what this post focuses on, and it’s also what nerd-sniped me in the first place. The conclusion of the workflow — reviewing, understanding, and approving code — should be centered on the human experience. AI can help, but the baseline must be a fast, calm, and predictable review experience. Everything starts with speed.

## Classic vs. New: two experiences, different trade-offs

Today, GitHub offers two pull request experiences: the classic view and the new one. It’s clear the new experience is the future, and GitHub is actively iterating on it — but both come with limitations.

For small PRs, the new experience feels noticeably faster than the classic one.  
For larger PRs, things get more complicated.

At first glance, the most visible change is the sidebar — and that’s not a small detail. GitHub now groups files by folders and then sorts them alphabetically, mirroring how repositories themselves are browsed.

[![new sidebar](https://gist.github.com/user-attachments/assets/d1e409df-6054-4e9b-baa3-69599ab4bb50)](https://gist.github.com/user-attachments/assets/d1e409df-6054-4e9b-baa3-69599ab4bb50)

[![old sidebar](https://gist.github.com/user-attachments/assets/4579e607-06ce-453b-a5db-85db56494e5a)](https://gist.github.com/user-attachments/assets/4579e607-06ce-453b-a5db-85db56494e5a)

The classic view feels cluttered and noisy in comparison. The new one feels natural.

This small change has a big impact: reviewers can focus on a specific folder or package first — especially in monorepos — instead of being forced to start with something arbitrary like a modified `package.json`.

That’s a huge win for users.

It’s also bad news for anyone trying to replicate it, including this POC — and likely for GitHub’s own API consumers — since the API still returns files in the old order. Extra logic was required here to match the new behavior.

The icons are also simpler and clearer.

[![old file](https://gist.github.com/user-attachments/assets/892ab1db-dd65-4e85-8f97-b50cf455dc46)](https://gist.github.com/user-attachments/assets/892ab1db-dd65-4e85-8f97-b50cf455dc46)

Instead of separate glyphs for file type and change type, both are merged into a single symbol. Less noise, more signal.

[![new file](https://gist.github.com/user-attachments/assets/ace9b7ab-ad26-4594-b947-3fbfdfccfe12)](https://gist.github.com/user-attachments/assets/ace9b7ab-ad26-4594-b947-3fbfdfccfe12)

## Sidebar performance

Performance-wise, the new sidebar is buttery smooth. GitHub uses `content-visibility` effectively to limit painting work.

The classic experience, by contrast, now feels visually saturated — at least after spending time with the new one. In large PRs, you can even perceive small delays when hovering over entries.

[![hover gif](https://gist.github.com/user-attachments/assets/92769c10-0096-45d3-821e-14059efe8ee3)](https://gist.github.com/user-attachments/assets/92769c10-0096-45d3-821e-14059efe8ee3)

Diff entries also received subtle but meaningful improvements.

The five blocks representing changes were moved to the right, and additions and deletions are now easier to read. In the classic view, something like this felt like reading a binary clock.

[![image](https://gist.github.com/user-attachments/assets/e1ed796b-ef27-4b91-a54a-b051e251cc25)](https://gist.github.com/user-attachments/assets/e1ed796b-ef27-4b91-a54a-b051e251cc25)

The new experience makes this explicit and readable.

[![Screenshot 2025-12-23 at 7 01 44 p m](https://gist.github.com/user-attachments/assets/ed44bd99-57d2-44ab-b422-614f745cb5d7)](https://gist.github.com/user-attachments/assets/ed44bd99-57d2-44ab-b422-614f745cb5d7)

File names are also clearer, and long paths now truncate from the left instead of the right — preserving the most meaningful part of the name.

[![image](https://gist.github.com/user-attachments/assets/494dcfe2-b6c2-432a-ae35-caf0f0853488)](https://gist.github.com/user-attachments/assets/494dcfe2-b6c2-432a-ae35-caf0f0853488)

## Where the new experience breaks down

Despite these improvements, the new experience has important limitations.

The classic view technically doesn’t limit how many files can be shown — but it only renders the first 100 diff entries, collapsing the rest into placeholders.

[![Screenshot 2025-12-23 at 7 18 24 p m](https://gist.github.com/user-attachments/assets/b1383e80-aa4e-47f3-bd50-3b8af99d16d5)](https://gist.github.com/user-attachments/assets/b1383e80-aa4e-47f3-bd50-3b8af99d16d5)

The new experience uses a different heuristic. Depending on the number of changed lines, it may render only a single file — as in [this PR](https://github.com/facebook/react/pull/34269/changes).

For very large PRs, GitHub eventually recommends switching back to the classic view.

The new experience is clearly optimized for small PRs. When it works, it eagerly renders most diff entries without lazy loading.

## The real problem: sequential loading

- Only 4 diff entries are rendered initially
- Skeletons are assigned a fixed height (in multiples of 50)
- Entries are then loaded **sequentially**, in chunks of 4

Crucially, entries are **not loaded based on what the user is looking at**, but based on what comes next in order.

A PR like [this one](https://github.com/facebook/react/pull/33146/changes) loads **42 entries in a waterfall**. If you scroll quickly to the middle, you may need to wait several seconds before the file you want even exists in the DOM.

Everything is painted on the client, so while you’re waiting for chunks to load, the main thread is also busy parsing and rendering.

If neither streaming nor server-side rendering is currently an option, React 19 opens new doors.

RSC payloads could ship serialized content instead of forcing the client to parse and paint everything. React 19 also introduced [Activity](https://react.dev/reference/react/Activity), allowing parts of the UI to be marked as low priority to keep the main thread responsive.

There’s a great deep dive on this [here](https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization).

Combined with smarter intersection-based loading, this could significantly improve the experience of large PRs without sacrificing responsiveness.

My approach followed the same principles as the first part: keep client components minimal, render as much as possible on the server, and let the browser do less work upfront.

The goal was simple: keep the DOM small, avoid unnecessary client-side painting, and rely on techniques like `content-visibility` so the UI only does work when it actually needs to.

To explore this space, I built a [small playground](https://github.com/cuquo/fast-github-poc/blob/main/src/app/size/page.tsx) that mimics the structure of a pull request layout. This allowed me to experiment with different rendering strategies, DOM sizes, and layout constraints before committing to a full implementation.

In parallel, I needed real-world stress cases. I asked ChatGPT to help me put together a [simple script](https://github.com/cuquo/fast-github-poc/blob/main/bigpr.ts) to collect some of the [largest pull requests](https://github.com/cuquo/fast-github-poc/blob/main/big-prs-results.json) from the React repository, and used those PRs as test inputs throughout the process.

Those PRs became the baseline for validating ideas, breaking assumptions, and measuring whether changes actually improved the experience or just felt clever.

DOM size matters more than it looks.

- Every extra DOM node has a cost. Even elements that aren’t painted still participate in layout and style calculations, and that cost becomes very noticeable during window resizes.
- Rendering a very large number of elements upfront directly impacts First Contentful Paint. In extreme cases, the browser can appear frozen while the DOM is being constructed.
- Gradually inserting elements into the DOM wasn’t an optimization — it was required to keep the experience usable.
- In practice, anything below ~300 files kept the interface consistently smooth, even during resizes.
- For larger PRs, `content-visibility` is non-negotiable. Without it, performance degrades fast. With it, scrolling stays fluid even when the DOM grows significantly.
- Exact height measurement for diff entries isn’t realistic in pull requests. Blob views are predictable, but diffs break the assumption: long lines wrap, context changes, and a single line can become two or three.
- Perfect measurement isn’t necessary. Approximate heights work surprisingly well. I validated this by navigating rapidly between files using the sidebar: layout shifts didn’t push the selected file out of view, and the experience remained stable.

## Sidebar

The new GitHub experience sorts files by folders first and then root files. To match that behavior, I had to load *all* sidebar pages via GraphQL before the first paint. That decision immediately cascaded into the diff entries logic, but it was the right starting point if I wanted to faithfully adopt the new visual model.

Improving the sidebar was surprisingly constrained. GitHub already uses `content-visibility` and `contain-intrinsic-size`, and those two account for most of the performance gains. That meant the biggest remaining lever was DOM size.

I focused on reducing the number of elements while preserving the same visual output. The sidebar went from 11 elements per entry down to 8. That doesn’t sound dramatic, but on a pull request with 3,000 files, that reduction alone is roughly equivalent to the initial DOM size of the New York Times homepage.

I did add one extra element: an `<input>`. That technically increases the DOM count for folders by one, but it allowed me to handle folder collapsing entirely in CSS instead of JavaScript. The trade-off was worth it — simpler logic and fewer runtime costs.

There’s an interesting CSS property called `overflow-anchor`, supported in all modern browsers except Safari, that helps prevent scroll position jumps by adjusting the scroll anchor automatically. It’s enabled by default (`auto`).

[![image](https://gist.github.com/user-attachments/assets/f6d3d499-1f28-4278-bad9-3eacc5e4cb64)](https://gist.github.com/user-attachments/assets/f6d3d499-1f28-4278-bad9-3eacc5e4cb64)

Because every sidebar entry has a fixed height, disabling `overflow-anchor` in supported browsers gave me small but measurable gains, helping the UI consistently hit the maximum frame rate during fast scrolling.

Another subtle improvement came from paint optimization. Transparency isn’t a problem in most interfaces, but in a UI that scales to thousands of rows, alpha blending adds up. By removing unnecessary transparency and avoiding alpha layers, painting became slightly faster and more predictable.

To keep the comparison fair, I avoided adding new features. The only exception was scroll markers for pull requests with 100 files or fewer. I experimented with enabling them for larger PRs, but the scroll experience degraded quickly, so I limited their use to smaller cases.

[![scroll-markers](https://gist.github.com/user-attachments/assets/4cc1903e-626b-4b1f-a121-89aa74b74b09)](https://gist.github.com/user-attachments/assets/4cc1903e-626b-4b1f-a121-89aa74b74b09)

After finishing the work on diff entries, I came back to the sidebar with fresh context.

At that point, it no longer made sense to keep using GraphQL there. I switched the sidebar data source to REST instead, allowing both the sidebar and diff entries to reuse the same endpoint and benefit from the same caching and deduplication logic.

That change simplified the data flow, reduced duplicate fetches, and made the overall system easier to reason about — especially under load.

This was the hardest part of the project — and it kept getting harder the deeper I went. Diff entries look deceptively simple, but there’s a lot happening under the hood.

My initial plan was straightforward:

- Fetch patches
- Parse them
- Calculate an approximate height on the server (for `contain-intrinsic-size`)
- Use `content-visibility` to limit rendering
- Add syntax highlighting

## Fetching and first rendering

This is where the GraphQL road ends. Patches are only available via REST, the rate limits are tighter than GraphQL’s, and the new file-sorting logic made things more complex.

I used Octokit to fetch patches. That part was mostly painless, except for one important tweak: disabling throttling. The default behavior interfered with streaming and introduced unnecessary delays.

Once fetching was in place, I moved on to parsing patches into something renderable. ChatGPT handled that surprisingly well — within a couple of hours I had diff entries rendering correctly, without obvious visual issues.

Calculating approximate heights on the server and adding `content-visibility` took minutes.

At that point, I had a working POC in a single day — everything except syntax highlighting. I tested it on small PRs first, then larger ones, and finally on very large PRs.

That’s when things started to fall apart. Performance wasn’t great — in some cases it was worse than GitHub’s. I also saw random crashes and freezes that I initially dismissed as local issues. But after reproducing the same behavior with Next.js, Turbopack, and Rspack, it became clear this wasn’t just a local issue.

My first fetch strategy was split in two steps:

1. Load the first 100 patches, split into root and non-root files
2. Fetch the rest, merge everything, then sort

It worked functionally — and for small PRs, it behaved just fine. Fetching and painting a few hundred files in one go stayed within reasonable limits, and the UI remained responsive.

The issue only became real as PRs grew larger. The same approach turned a single render pass into thousands of DOM nodes competing for layout, style, and memory at once.

Fetching wasn’t the real issue — it was the amount of global, sequential work that had to complete before any meaningful UI could appear.

[![Initial fetch strategy: global merge and reorder before processing and paint](https://gist.github.com/user-attachments/assets/8ee966e6-9fd7-437a-b17d-bacc99ddc0c1)](https://gist.github.com/user-attachments/assets/8ee966e6-9fd7-437a-b17d-bacc99ddc0c1)

## Syntax highlighting: the first wrong turn

Next on the list was syntax highlighting. I tried the same approach I had used for blobs: calling GitHub’s markup REST endpoint.

That worked — briefly. On large PRs, I hit API rate limits almost immediately.

So I tried a different approach: render everything on the server *without* syntax highlighting, then apply highlighting on the client using Intersection Observers.

It was usable, but not good. Scrolling felt uneven, and rate limits were still a problem.

That’s when I switched to server-side highlighting with [Shiki](https://shiki.style). The tradeoff was clear: unlike GitHub’s API, Shiki can’t infer language automatically — I had to add logic to determine it explicitly. Fortunately, that was manageable.

Around this time, I changed the fetch pattern again. I introduced multiple queries and additional Suspense boundaries to avoid blocking the main thread while painting.

The goal was to give the browser some “air” to render.

[![Second fetch strategy: incremental fetch and stitching with additional Suspense boundaries](https://gist.github.com/user-attachments/assets/6750606e-1677-405b-84d3-e63df554db25)](https://gist.github.com/user-attachments/assets/6750606e-1677-405b-84d3-e63df554db25)

On paper, it made sense.

In practice, it was worse.

## Suspense waterfalls and streaming pain

The problem wasn’t just fetching anymore. React Suspense blocks not only on data fetching, but on *any* async work inside a boundary — including parsing, transforming, and rendering Shiki output.

In practice, it became a massive waterfall

[![image](https://gist.github.com/user-attachments/assets/7555359f-f035-4098-8705-e5ca488506b4)](https://gist.github.com/user-attachments/assets/7555359f-f035-4098-8705-e5ca488506b4)

Performance per frame improved, but total streaming time exploded. Large PRs could take a minute or more before becoming usable.

At first, I suspected Octokit throttling or cache issues. After measuring cache hit rates both locally and on Vercel, it was clear that wasn’t the culprit.

So I changed the strategy again.

## Streaming cadence and adaptive chunking

Cached requests were effectively free — milliseconds locally and in production. So I returned to a two-phase approach:

- Fetch the first set of files eagerly
- Fetch the remaining files in a second pass

This time, instead of fixed chunks, I split diff entries into chunks of ~30 files, each wrapped in its own Suspense boundary, with small delays between them.

Scrolling was always smooth (thanks to `content-visibility`), but the overall experience still didn’t feel *snappy*.

That’s when I added performance markers and brought in Gemini for a second opinion. I profiled different PR sizes, varied chunk sizes and delays, and fed those traces back into Gemini to compare outcomes quickly.

Eventually, instead of hardcoding chunk sizes, I made them dynamic — based on the approximate number of lines derived from patch metadata. That allowed chunk sizes to adapt to PR size and complexity.

The experience improved noticeably.

But the bugs kept coming.

## Diff algorithms: when memory becomes the bottleneck

The biggest remaining issue turned out to be the diff algorithm itself.

To render side-by-side diffs, I needed to transform patches into “old lines” and “new lines”. My initial LCS implementation — generated by ChatGPT 5.2 — used classic dynamic programming.

It worked beautifully on small files.

It did *not* work well at scale.

With many async tasks running, large files, and a serverless environment, the algorithm consumed too much memory and pushed the garbage collector hard. ChatGPT had already warned me this might happen and suggested Myers’ algorithm as a more memory-efficient alternative.

So I asked Gemini.

Gemini suggested a clever optimization: use a single `Int32Array` instead of nested arrays to reduce memory pressure. I searched for an existing JavaScript diff library using Myers with these constraints and found nothing suitable.

So I asked Gemini to write one.

It generated the code fast — very fast — and labeled it “production ready”. I wasn’t convinced, so I asked ChatGPT to review it.

> “LGTM on approach, NACK on implementation. Needs rewrite with array-based Myers + strict invariants.”

With that feedback, Gemini rewrote the implementation. I kept ChatGPT as a reviewer and Gemini as the primary coder until both models agreed the code was solid.

What followed was about half an hour of copy-pasting between ChatGPT and Gemini — a ridiculous sycophancy battle where both models kept praising each other — until they declared the final version *“beyond gold master, this is dynamite.”*

Ridiculous phrasing aside, the result was a Myers diff implementation with predictable memory usage and no GC spikes.

At this point, I stopped trusting intuition and started measuring.

Both models also collaborated on the benchmarks themselves.  
The tests were reviewed and adjusted multiple times to ensure we were **comparing apples to apples**.

[![20k lines performance rev2](https://gist.github.com/user-attachments/assets/6879efd8-f6c6-4361-a05f-dfea8d795406)](https://gist.github.com/user-attachments/assets/6879efd8-f6c6-4361-a05f-dfea8d795406)
[![20k lines memory rev2](https://gist.github.com/user-attachments/assets/89d277d3-b4b7-496a-9006-056cdbb04fa6)](https://gist.github.com/user-attachments/assets/89d277d3-b4b7-496a-9006-056cdbb04fa6)
[![jquery performance rev2](https://gist.github.com/user-attachments/assets/0e5b76ff-b00e-46a7-b22a-05a28ef10100)](https://gist.github.com/user-attachments/assets/0e5b76ff-b00e-46a7-b22a-05a28ef10100)
[![jquery memory rev2](https://gist.github.com/user-attachments/assets/5d2e12ea-0b84-4a83-b226-c2adebbbc720)](https://gist.github.com/user-attachments/assets/5d2e12ea-0b84-4a83-b226-c2adebbbc720)

The custom implementation (`custom-diff`) was benchmarked against:

In all cases I measured **performance** and **memory usage** under two different scenarios:

1. **20k lines with random changes** (worst-case stress test)
2. **jQuery source code with random changes** (real-world diff)

All benchmarks were run using `hyperfine` with warmup runs and repeated measurements.[1](#fn-1)

---

### Test 1: 20k lines (worst case)

| Algorithm | Mean time |
| --- | --- |
| **custom-diff** | **~29 ms** |
| jsdiff | ~32 ms |
| fast-diff | ~35 ms |

Even in this synthetic worst-case scenario, the custom implementation performs slightly better:

- ~**1.2× faster than fast-diff**
- ~**1.1× faster than jsdiff**

Performance differences here are modest, as all three algorithms operate in similar theoretical bounds. Memory behavior is where things diverge sharply.

#### Memory (retained outputs)

| Algorithm | Total retained heap (20 runs) | Avg retained per run |
| --- | --- | --- |
| **custom-diff** | **~0 MB** | **~0 MB** |
| fast-diff (line tokens) | ~17 MB | ~0.87 MB |
| fast-diff (char-level) | ~61 MB | ~3.08 MB |
| jsdiff | **~110 MB** | **~5.5 MB** |

The difference is stark:

- **custom-diff** retains virtually no memory across runs
- **fast-diff** retains moderate memory depending on usage
- **jsdiff** allocates and retains a large amount of heap memory

In serverless or concurrent environments, this kind of retained memory quickly translates into GC pressure and unpredictable latency.

---

### Test 2: jQuery (real-world diff)

| Algorithm | Mean time |
| --- | --- |
| **custom-diff** | **~44 ms** |
| fast-diff | ~300 ms |
| jsdiff | ~1.0 s |

On a realistic codebase, the gap widens dramatically:

- **custom-diff is ~6.7× faster than fast-diff**
- **~24× faster than jsdiff**

Here, object-heavy representations and extra preprocessing costs dominate runtime for the existing libraries.

| Algorithm | Peak heap |
| --- | --- |
| **custom-diff** | **~8 MB** |
| fast-diff | ~40–47 MB |
| jsdiff | **~126 MB** |

Again, the custom implementation keeps memory flat and predictable, while `jsdiff` in particular drives heap usage high enough to cause long GC cycles.

While raw performance improvements on synthetic tests are incremental, **memory behavior is the real differentiator**.

The custom Myers implementation uses flat `Int32Array` structures and avoids object-heavy allocations, resulting in:

- Predictable memory usage
- No retained heap growth
- No GC spikes under load

In realistic scenarios, this translates into **significantly faster diffs** and **far lower memory pressure**.

For serverless, streaming, or highly concurrent systems, this tradeoff matters far more than theoretical algorithmic complexity — and this is where the custom implementation clearly wins.

## Caching: necessary, painful, unavoidable

The next class of bugs was caching.

Caching is deeply underrated — and incredibly hard to get right at scale.

Next.js [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) aren’t perfect, but they’re clearly moving in the right direction. They give developers fine-grained control over what gets cached, for how long, and whether we’re caching fetch responses or the full RSC payload of expensive computations.

That said, cache keys are derived from input parameters. In practice, this meant I couldn’t pass raw diff content or Shiki output directly without exploding the cache key space.

Instead, I had to cache by reference: page index, file index, and identifiers tied back to already-cached queries. In Redis, this would have been trivial — keying directly by file SHA — but that wasn’t an option here.

On top of that, aggressive caching combined with fully async execution introduced another problem: connection limits. Locally, the cache lives in an in-memory LRU. In production, it’s backed by Vercel’s cache or Redis, both with hard limits on concurrent connections.

To avoid thundering herds, I introduced batching and in-flight deduplication across several helpers — while still keeping everything async.

The last bug wasn’t in my code.

I added `scroll-target-group` to the sidebar to improve navigation. Unfortunately, Chrome continuously measures scroll targets while content is still streaming.

Because diff entries were still being added over time, Chrome entered an infinite measurement loop and eventually crashed.

[![crash](https://gist.github.com/user-attachments/assets/1fe78d51-5ab6-4eba-9c61-9d92d8d44698)](https://gist.github.com/user-attachments/assets/1fe78d51-5ab6-4eba-9c61-9d92d8d44698)

The fix was pragmatic: a small client component that waits until the last item of the final chunk loads, then enables `scroll-target-group` via a class toggle.

Not every performance win comes from optimizing algorithms.

Sometimes the right move is to stop optimizing the process and start using small, almost silly tricks. Like magic: once you know how it works, it sounds obvious — but the first time you see it, it genuinely surprises you.

The repository view has one of those tricks. Thanks to the GitHub API, we know a file’s size ahead of time. That lets me fully prefetch small files (≤ 20 KB), while larger files render skeletons first. Navigation feels instant, bandwidth is preserved, and the browser avoids loading content that could otherwise push it toward memory pressure.

[![prefetch blob](https://gist.github.com/user-attachments/assets/a9a2de4d-3e7d-43ca-b536-d9c275ed7bdb)](https://gist.github.com/user-attachments/assets/a9a2de4d-3e7d-43ca-b536-d9c275ed7bdb)

The same idea applies to pull requests.

If a PR has [`DIFFS_PER_PAGE`](https://github.com/cuquo/fast-github-poc/blob/main/src/constants/options.ts#L8) files or fewer, I can fetch that number up front and fully preload the PR. Small PRs open instantly, without special cases or loading states.

[![prefetch pr](https://gist.github.com/user-attachments/assets/462d5423-9292-487b-ba22-1715999428aa)](https://gist.github.com/user-attachments/assets/462d5423-9292-487b-ba22-1715999428aa)

Syntax highlighting needed a similar trick.

Shiki performs well locally, but in production it’s more expensive. The solution was [`INITIAL_SYNTAX_HIGHLIGHT_DIFF`](https://github.com/cuquo/fast-github-poc/blob/main/src/constants/options.ts#L11) cache a small number of highlighted diffs as HTML directly in the initial payload.

No matter how large the PR is, the first 20 entries (`DIFFS_PER_PAGE`) load immediately, and 5 of those are highlighted synchronously on page load. As the user scrolls, the remaining batches continue processing in the background — without ever blocking interaction or making scrolling feel heavy.

I really enjoyed working on this project.

These are the kinds of challenges that originally pulled me into programming — slowing down, questioning assumptions, and caring about how things *feel* to use.

After a long time away from that mindset, this reminded me that curiosity doesn’t disappear. You just have to give it room to come back. Turns out, old dogs can still learn new tricks.

Reviewing code is a human activity. Performance isn’t just about speed — it’s about calm, focus, and staying in flow while trying to understand someone else’s work.

If any of this resonates with you, try it out, explore the repo, and take whatever is useful. I’ll be more than happy if it sparks ideas, conversations, or better implementations.

1. *Numbers are rounded from the hyperfine mean.* [↩](#fnref-1)
