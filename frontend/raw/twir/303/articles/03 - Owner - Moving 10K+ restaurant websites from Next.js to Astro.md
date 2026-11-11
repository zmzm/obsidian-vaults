---
type: twir-item
issue: 303
item: 3
item_type: item
date: 2026-10-28
source: https://building.owner.com/project-speed
tags:
  - "Nextjs"
  - "10K"
status: auto
quality: keep
---

[[2026-10-28-TWIR-303|Index]]

# Item 3: Owner - Moving 10K+ restaurant websites from Next.js to Astro

Source: [https://building.owner.com/project-speed](https://building.owner.com/project-speed)

Summary:
Owner migrated over 10,000 restaurant websites from a Next.js stack to Astro, achieving a 4% revenue increase per restaurant and dramatic performance improvements (e.g., LCP reduced from 5.4s to 0.7s). The new architecture leverages Astro’s server-rendered markup and React “islands” for interactivity, with aggressive caching and edge delivery via Cloudflare Workers. The migration addressed issues with over-fetching, slow cache invalidation, and third-party script overhead, and introduced a layered cache and edge-optimized asset handling.

Key takeaways:
- Astro enables markup-first rendering with opt-in React interactivity, reducing client JS.
- Edge caching and Cloudflare Workers significantly improve time-to-first-byte and scalability.
- Careful asset inlining and cache strategies are critical for performance at scale.
- Migration required architectural changes but resulted in measurable business and technical gains.

Recommendation:
Read fully (valuable for those considering SSR/SSG frameworks, edge delivery, or large-scale migrations)

Why it matters:
valuable for those considering SSR/SSG frameworks, edge delivery, or large-scale migrations

Content:
# Project Speed Â· Building @Owner

Big restaurant chains invest millions into fast, high-converting websites. That is one reason your local pizzeria struggles to compete against Dominoâs. Now that Owner has scaled to 10K+ restaurant websites, we have enough traffic to test changes and measure their effect on conversion and sales, then ship the successful variants to every business. Project Speed was one of those changes. We rebuilt our website infrastructure for speed, and it raised per-restaurant revenue by more than 4% across the network.

We replaced our Next.js rendering stack, codenamed Mercury, with an Astro stack we call Apollo. Apollo serves cached pages from the edge and only uses React where needed. As one measure, largest contentful paint on menu pages went from 5.4 seconds to 0.7 seconds at the 75th percentile.

In July 2025, I was inspired by [McMaster-Carr](https://www.mcmaster.com/) (Iâm a frequent customer) and thought it would be cool if Owner websites were that fast. Two months later Jack joined the team and we were off to the races. By late January 2026, Apollo served 100% of our traffic.

## Why Mercury was slow

When Mercury needed to render a page, it fetched data from our backend, Olympus, then rendered the page and sent the response to the user. That round trip is slow. So we cached. Then we cached the caches. That somewhat worked, and most of the time the websites looked reasonably fast. But pages had unpredictable delays, website changes took a while to publish, and every time we redeployed it cleared the cache.

Mercury also loaded more data than most pages needed, due to inherent design choices when the largest customer we served had one menu and two locations. We loaded every location for a brand and every menu, including items, categories, and modifiers. Our platform lead Dmitry winced every time we saw massively oversized assets, slow loading times, and request amplification issues at the backend.

Third-party scripts added more overhead. Google Tag Manager and the Facebook pixel loaded on every page. We couldnât remove them without breaking customersâ analytics, and they affected our lab scores. Our baseline and targets:

| Metric (p75) | Before | Target |
| --- | --- | --- |
| Largest contentful paint | 5 to 6s | under 1s |
| Time to first byte | 600ms+ | under 200ms |
| Interaction to next paint | ~200ms | under 100ms |
| JavaScript bundle | ~1,500KB | under 100KB marketing, under 250KB dynamic |
| Google PageSpeed (out of 100) | ~45 | 90+ |

## Why we chose Astro

We wanted a framework that defaulted to markup-only components and let us choose where to add client-side JavaScript. Most of our website content didnât need React running in the browser. We also considered Remix, TanStack Start, and Gatsby. We chose Astro for 4 reasons:

1. It renders components to markup by default; client-side framework JavaScript is opt-in.
2. It supports islands: self-contained components with their own hydration boundaries, using React or another supported framework.
3. It supports prerendered and on-demand pages in the same app, with client-side interactivity where needed.
4. It integrates deeply with Cloudflare, a platform we wanted to bet on.

## Architecture

Apollo renders pages to markup and caches the output. Cache hits serve that markup. We refresh the affected pages in the background when restaurant info changes.

The interactive parts are React islands. Astro renders the whole page to markup on the server, then hydrates the islands only, each on its own schedule. The rest of the page doesn't need any client-side React.

Marketing pages (careers, FAQ, location, about) donât need much JavaScript. The menu page puts the ordering flow in a single React island, keeping the ordering experience inside one hydration boundary. Over time, we'll make more of the menu experience static to drive performance gains further without sacrificing UX.

Client directives control when Astro loads and hydrates an island:

- `client:load` loads and hydrates on page load. We use this for the menu and cart because a user might tap âadd to orderâ immediately.
- `client:visible` loads and hydrates when the component enters the viewport.
- `client:idle` defers loading and hydration until after the initial page load, using the browserâs idle callback where supported.

We didn't want to rebuild the whole online ordering flow at first. All we needed to get that experience working in Astro was roughly:

```
---
const brand = await fetchBrand(Astro, brandId)
const initialPage = await fetchPage(Astro, brandId, '/menu')
const pageData = await transformPageData(initialPage, brand)
---

<BrandLayout brand={brand}>
  <MenuIsland
    client:load
    brandId={brandId}
    pageData={pageData}
  />
</BrandLayout>
```

The code above the template runs on the server to prepare the page data. Astro renders `<MenuIsland>` to markup. The `client:load` directive tells Astro to load the islandâs JavaScript and hydrate it on page load. That island contains the entire ordering experience.

We also configured the build to reduce asset requests:

```
export default defineConfig({
  output: 'server',
  integrations: [react()],
  prefetch: { prefetchAll: true },
  build: {
    inlineStylesheets: 'always', // no render-blocking CSS requests
    assetsInlineLimit: 150000,    // inline anything under 150KB
  },
})
```

Inlining project CSS removes separate stylesheet requests. Inlining eligible assets removes requests for those files too. We also enable prefetching for links. Some of these settings are unorthodox; we tweaked them with a lot of data to prove this is the best for our app.

Our old setup ran on AWS in `us-east-1` only. Requests that reached that server traveled there and back, even when it returned cached markup. Apollo runs on Cloudflare Workers across Cloudflareâs edge network. Workers execute our code in Cloudflareâs data centers, letting us render and serve pages near the user. We use Cloudflare's `workerd` runtime in local development too.

We even moved the brand lookup (figuring out which restaurant a domain belongs to) into the edge worker. That one change shaved about 50ms off time to first byte. Images have their own edge treatment through a service we call Pluto, which resizes and re-encodes photos at the edge.

## Cache layer

Mercury slowed down after every deploy while its caches rebuilt. Apollo needed to avoid that slowdown and limit requests to Olympus. To fix it we built a custom cache, layered like this:

1. Every request first goes through a gateway Worker, which checks feature flags, selects the route type, and determines which markup to serve.
2. The gateway then forwards the request through [Cloudflareâs Workers Cache](https://blog.cloudflare.com/workers-cache/), placing a tiered cache between the gateway and the rest of our stack.
3. On a cache miss, we fall back to R2, Cloudflareâs object storage, where HTML is stored alongside metadata such as the version that rendered it and when it was generated. We serve the stored HTML and use that metadata to decide whether to trigger a background refresh of both R2 and the tiered cache.
4. If no HTML exists in R2, we fall back to the Astro renderer, which generates the page, stores it in R2 with its metadata, and populates the cache.

**Stale while revalidate.** When we can serve a stale cached page, we return it and refresh it in the background - those requests donât wait for a re-render.

**Tracing requests.** We tag every response with a header (`x-owner-source`) that says whether it came from the edge cache or a fresh render, and we emit `Server-Timing` headers for each hop (R2 read, Astro render, R2 write). These headers show where the response came from and how long each measured operation took.

**Push, donât poll.** Olympus calls Apolloâs revalidation endpoint when a restaurantâs data changes, and then Apollo re-renders the affected pages in the background. This reduces repeated fetches from Olympus.

Small table of route types:

| Route type | Browser cache | CDN cache |
| --- | --- | --- |
| Static assets | 30 days (immutable) | 30 days |
| Marketing pages | 60s | 600s |
| Menu | 60s | 120s |

Cache keys include the brand and a hash of the active feature flags, keeping cached markup separate for each experiment variant. Any page tied to a specific logged-in user (checkout, order status, login) doesnât go through the shared cache.

By the time we rolled Apollo out to all customers, our markup store had grown to 5TB.

## Speed bumps

Experiment variants. Each independent binary feature flag doubles the number of cached variants. Many flags could explode into thousands of stored copies and prevent us from properly prerendering and caching. So we bucket groups of customers together at random and run experiments across different segments.

Duplicate React copies. Node loaded 2 copies of React during server rendering. Astroâs deduplication settings didnât cover that module-loading path. We used a filesystem symlink so Apollo and the root project resolved React to the same copy.

Early Hints. We enabled HTTP 103 Early Hints so the browser could start fetching the hero image before the markup response. Some pages reached a largest contentful paint of about 600ms with Early Hints enabled.

We found so many other performance and optimization wins as we went along. We're still finding them: agents make the pursuit of performance excellence a game we don't know that we'll ever stop playing (and enjoying!).

## Shipping it without anyone noticing

We ran Apollo and Mercury side by side as a 50/50 experiment measured in PostHog. Some brands stayed on Mercury, others went fully to Apollo, and for the rest, we split their traffic down the middle to compare the stacks on the same kinds of sites.

Jack did such a good job making the new sites pixel perfect to the old, I couldn't tell them apart. We added a little animated Owner logo in the footer (this was pre our redesign).

For testing we shipped a small browser extension Sphinx that let an engineer force their own browser onto Apollo or Mercury on any site. Today it powers our feature flag system.

We staged the rollout in steps: 8 brands, then 800, then 4,800, then all. At each step we watched the field data, and we had a kill switch in case we needed to drop back to 50/50 or turn Apollo off entirely.

Timeline:

- July 2025: Ryan is asked what a big moonshot would be, writes a short doc called "Project Speed"
- Oct 2025: Validated Cloudflare Workers
- Nov 13, 2025: First real end-to-end order in Apollo
- Dec 2025: First brands go live. Scaled to ~4,800 by Christmas.
- Jan 2, 2026: All brands enter 50/50 test
- Jan 26, 2026: Apollo serves 100% of traffic
- Feb 9, 2026: Public launch

## Results

- p75 largest-contentful-paint on the menu page (field RUM): **5.4s** before â **0.7s** after. About 87% faster. We score mobile against a 5-year-old $200 Android phone. Some sites with a fast hero image hit a 0.6-second paint.
- **+23%** click-through from homepage to menu item
- **+4%** per-restaurant revenue
- **$8,000 to $10,000 per month** infrastructure savings
- Mobile Lighthouse: 90 to 99 (previously 44)
- Desktop Lighthouse: 98 to 100
- Page load, lab: <1s
- In the database, Apollo carts converted about 10% better from "add item" to checkout. One restaurant, El Vaquero, converted 33% better on the new stack (they have a large menu, so the optimizations benefitted them even more).

![PageSpeed Insights mobile report for ashleys.cafe: Performance 96, Accessibility 100, Best Practices 100, SEO 100](/images/posts/project-speed-psi-mobile.webp)

PageSpeed Insights, mobile: ashleys.cafe

![PageSpeed Insights desktop report for ashleys.cafe: Performance 100, Accessibility 100, Best Practices 100, SEO 100](/images/posts/project-speed-psi-desktop.webp)

PageSpeed Insights, desktop: ashleys.cafe

Apollo is how we build our websites now. Since the end of Project Speed, weâve rebuilt our Restaurant Grader and other frontends in a similar way, following all the lessons we learned.

Owner wants to help local businesses succeed. This is just the start of the work we're doing, and AI is accelerating the pace we can improve our platform for our customers. If you're excited about local restaurants and this sounds like something you want to work on, [reach out to us](https://www.owner.com/careers#roles).
