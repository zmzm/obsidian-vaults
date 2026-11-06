---
type: twir-item
issue: 303
item: 5
item_type: item
date: 2026-10-28
source: https://sarthakmishra.com/blog/optimizing-tanstack-start
tags:
  - "TanStack"
status: auto
quality: keep
---

[[2026-10-28-TWIR-303|Index]]

# Item 5: Optimizing the sh*t out of TanStack Start

Source: [https://sarthakmishra.com/blog/optimizing-tanstack-start](https://sarthakmishra.com/blog/optimizing-tanstack-start)

Summary:
This post details a comprehensive performance optimization journey for a TanStack Start site, focusing on reducing JavaScript, optimizing font and image loading, and improving critical rendering paths. The author emphasizes measuring before optimizing, lazy-loading non-critical assets, and using code splitting and font subsetting. The process led to significant improvements in PageSpeed Insights scores and user-perceived performance.

Key takeaways:
- Audit and measure before making optimizations; focus on largest contentful paint (LCP).
- Major wins come from not loading unnecessary assets (images, fonts, JS).
- Use lazy loading, code splitting, and font subsetting to minimize initial payload.
- Continuous monitoring and size budgets help prevent regressions.

Recommendation:
Read fully (practical, step-by-step insights for any React or SSR app)

Why it matters:
practical, step-by-step insights for any React or SSR app

Content:
# Optimizing the sh*t out of TanStack Start

A few days after I [moved this site to TanStack Start](/blog/astro-to-tanstack-start), PageSpeed Insights scored the home page 73 on mobile. The largest contentful element was a paragraph, and it took **5.2 seconds** to appear. The page was prerendered. The words were already in the HTML. The browser still took five seconds to show them.

The fastest request is the one the browser never makes. Most of this post is some version of that idea, ordered from the cheapest fixes to the ones Iâm still not sure were worth it. It covers how to find that work in your own TanStack Start app and what to do about it.

I worked through it with Claude Code and Codex, and [the section near the end](#how-i-used-claude-code-and-codex) covers how that went.

**In short:**

- Audit a production build, repeat the runs, and identify the LCP element before changing anything.
- The biggest wins I could measure and attribute came from not loading things: a site-wide image manifest, closed dialogs, hidden navigation images, and font files the page didnât need.
- Fonts need two fixes: smaller files, then a fallback with matched metrics so the faster swap doesnât move the page.
- Critical CSS extraction and delayed app startup reduced blocking work, but I canât credit the final score to either. Try them after the basics, and budget for the upkeep.
- Add size budgets and browser tests, or the next feature adds the bytes back.

## The results

| Mobile home-page metric | [October 24, before the fixes](https://pagespeed.web.dev/analysis/https-sarthakmishra-com/adninyd8c2?form_factor=mobile) | [October 26](https://pagespeed.web.dev/analysis/https-sarthakmishra-com/3sjxsf8ck0?form_factor=mobile) |
| --- | --- | --- |
| Performance | 73 | 100 |
| First Contentful Paint | 2.3 s | 1.2 s |
| Largest Contentful Paint | 5.2 s | 1.7 s |
| Total Blocking Time | 160 ms | 0 ms |
| Cumulative Layout Shift | 0.002 | 0.001 |
| Speed Index | 4.5 s | 1.2 s |

These are individual PageSpeed Insights lab runs on the live home page, with several changes between them.

## Measuring TanStack Start performance: what to audit first

Audit a production build, either on a preview server or at a deployed URL.

Development mode includes work your visitors never receive. Run Lighthouse several times with the same settings and compare medians, then confirm on the deployed site with PageSpeed Insights.

On October 25, the same home-page build scored 91, 95, and 92 within a few minutes on PageSpeed Insights. Any single run inside that range tells you very little about one change. PageSpeed Insights can also serve a cached audit under a new report link, so check the capture time before counting a repeat.

Check compression on a local preview too. My local Lighthouse runs scored 94 to 95 because the preview served 165 KiB of uncompressed HTML. Serving the same build with Brotli brought the document down to about 28 KiB and the score up to 99, which matched the live site more closely.

The [Performance score](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring) comes from measured timings, so start with the slow metric and look for its cause:

| What you see | Where Iâd look first |
| --- | --- |
| The document itself arrives late | Server response time, route loaders, sequential data requests, caching |
| First Contentful Paint (FCP) is late | Render-blocking CSS, font loading, work before the first frame |
| Largest Contentful Paint (LCP) is much later than FCP | The LCP element, when its resource is discovered, and what delays its display |
| Total Blocking Time (TBT) is high | Long JavaScript tasks, hydration, third-party scripts, animation loops |
| Cumulative Layout Shift (CLS) is high | Font swaps, missing media dimensions, content inserted above existing content |
| Speed Index is high | Filmstrip frames, late visible sections, animation during the initial load |

Before changing anything, identify the LCP element. Mine was a paragraph that needed no image download or client-side data fetch, so compressing the hero image wouldnât have helped.

No

Yes

Image

Text

LCP element

In the HTML response?

Route loaders, prerendering, server reads

Image or text?

Discovery, priority, sizes

Fonts and render-blocking CSS

JavaScript and hidden downloads competing for bandwidth

Check the document response first. If the content is there but appears late, the cause is in the browser.

The DevTools screenshots and clip below show the live home page on October 27, with a mobile viewport, cache disabled, and no CPU or network throttling. Their timings belong to those inspection sessions, not to the Lighthouse runs above.

## Server rendering in TanStack Start: put content in the first HTML response

Open the document request in the Network panel and search its Response tab for your heading and main text. Inspecting the DOM after hydration doesnât tell you what the server sent.

If the content is missing, fetch it in a route loader rather than a client Effect. In Startâs [execution model](https://tanstack.com/start/latest/docs/framework/react/guide/execution-model), a loader can run on the server and in the browser, so keep server-only code behind a server boundary. Putting an import inside a loader doesnât make it server-only.

Public content that can be generated at build time suits [static prerendering](https://tanstack.com/start/latest/docs/framework/react/guide/static-prerendering). These options in your `tanstackStart` plugin configuration prerender two routes:

```
tanstackStart({
  prerender: {
    enabled: true,
    autoStaticPathsDiscovery: false,
    crawlLinks: false,
  },
  pages: [
    { path: '/', prerender: { enabled: true } },
    { path: '/about', prerender: { enabled: true } },
  ],
});
```

Keep request-time rendering for personalized pages. On the deployed site, confirm the [`Content-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Encoding) and [`Cache-Control`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) headers. Content-hashed assets can be cached for a long time; HTML depends on how often the page changes.

My HTML was fine. The document arrived in about 110 ms and already contained the paragraph. The delay came from everything that loaded around it, and most of that was JavaScript Iâd never meant to send.

## Code splitting in TanStack Start: stop shipping the rest of the site

Filter the Network panel to JS, sort by size, and follow the imports behind the larger files. Compare a simple route with a complex one. If both load much of the same code, look at the root route, shared layouts, and modules imported by both.

Generated data is easy to miss here. On my site, an import in a card component made every page load the full image manifest, with metadata for 117 images, about 35 KiB compressed, even when the page displayed a handful. Every page downloaded image descriptions and rendition URLs as JavaScript, on top of the images themselves.

Each route now collects the image data it renders, and navigation imports data for newly needed images. I also removed tooling-only excerpts and unused recommendation scores from the shared content index. The home pageâs module-preloaded JavaScript fell from roughly 234 to 196 KiB. Its HTML grew from about 42 to 49 KiB because it now carried the selected image data, but every page stopped receiving the unrelated catalog.

Returning a smaller object from a loader only helps if the full dataset also stays out of the modules the browser loads at startup. Inspect both the serialized response and the emitted bundles.

### Lazy-load dialogs and closed features

TanStack Routerâs [route code splitting](https://tanstack.com/router/latest/docs/framework/react/guide/code-splitting) separates routes. You still decide whether everything inside the current route needs to load immediately. Search, the mobile menu, image enlargement, a portrait viewer, and a leave-form confirmation had all pulled code into my initial load.

Declare the lazy component at module scope:

```
import { lazy } from 'react';

const SearchDialog = lazy(() => import('./SearchDialog'));
```

`SearchDialog` is a default export here. [React loads the module when you first attempt to render it](https://react.dev/reference/react/lazy), so rendering the dialog immediately with `open={false}` can start the download before anyone opens it. Keep it out of the tree until needed, use `Suspense` and an error boundary for loading and failure, and let closing behavior and focus return finish before unmounting it.

I kept the triggers available and mounted each dialog on first open. The browser fetches the chunks after the page loads, so the first interaction doesnât always wait for a download:

| Page | Before, KiB gzip | After, KiB gzip |
| --- | --- | --- |
| Home | 196.1 | 174.4 |
| A long post | 213.0 | 190.8 |

Verify the split in the browser. A new chunk filename doesnât prove anything if the initial page still preloads it.

In a recorded Network log, choose Font, then JS. Click Size until the largest
downloads appear first. This short clip has no audio.

## Font loading: subset, trim preloads, and match fallback metrics

Filter the Network panel to Font and check which families, styles, weights, and character ranges the page downloads. Then trace the imports and preload hints that caused them.

Use WOFF2 subsets that cover your content and remove unused styles and axes. My original normal Inter file was about 342 KiB. Fontsourceâs subsets let the browser fetch only the character ranges a page uses. Removing the optical-size axis then took the normal Latin file from 71.2 to 47.1 KiB, a cut of about a third. I kept small symbol supplements so the reduction didnât remove characters the interface uses.

Preload a font only if the initial view needs it and youâve measured late discovery. I cut three font preloads down to the normal Latin Instrument Serif face used by the heading; the other faces load when text needs them. Check the preloadâs URL, `type`, and `crossorigin` mode, or the browser downloads the font twice. [Googleâs font-loading guide](https://web.dev/articles/optimize-webfont-loading) explains how discovery and subset selection work.

Test the swap, too. Faster fonts made my text appear sooner, and I could see it move. During those changes, Newsletter Issue 1 recorded CLS around 0.21. The web font changed the headingâs dimensions and pushed the content below it.

A fallback with adjusted metrics fixes that. This is the Instrument Serif fallback from my site:

```
@font-face {
  font-family: 'Instrument Serif Fallback';
  src:
    local('Times New Roman'), local('TimesNewRomanPSMT'),
    local('Liberation Serif'), local('Noto Serif');
  size-adjust: 83.75%;
  ascent-override: 118.2%;
  descent-override: 37.01%;
  line-gap-override: 0%;
}
```

Place it after the web font in the `font-family` stack. The percentages belong to this pairing, so measure your own. Googleâs [CLS guidance](https://web.dev/articles/optimize-cls) covers the overrides. Record a cold load with the filmstrip visible and check that text appears early and stays put.

Images had a version of the same problem: some of what downloaded was never going to be seen.

## Image loading: prioritize the LCP image, keep hidden images out

The LCP image needs the opposite treatment. It should be discoverable in the initial HTML, eager, and eligible for high fetch priority. [Googleâs LCP guidance](https://web.dev/articles/optimize-lcp) splits LCP into discovery, transfer, and render delay, and the Performance panelâs breakdown tells you which part youâre fixing.

For an image filling a container capped at 960 pixels, with 16-pixel gutters on smaller screens:

```
<img
  src="/images/article-1280.webp"
  srcSet="/images/article-640.webp 640w, /images/article-960.webp 960w, /images/article-1280.webp 1280w"
  sizes="(max-width: 992px) calc(100vw - 32px), 960px"
  width={1280}
  height={720}
  alt="An editor displaying a published article"
  loading="eager"
  fetchPriority="high"
/>
```

Those paths assume generated 16:9 renditions. The `sizes` value must describe the layout, not the source file. On my site, whose renditions differ from this example, correcting that hint let a phone choose a 640-pixel file where it had previously chosen a 1080-pixel one.

Lazy-load everything further down and reserve its space. Hiding an image with CSS doesnât prevent its download. My desktop navigation was hidden on phones, but its eager images still landed in the preload list. That was nine requests for navigation the visitor couldnât see. Marking them lazy removed the preloads. The desktop sidebar now waits for hydration and a desktop-sized viewport before decoding its images, so phones never request them. On desktop, the navigation now appears slightly later, and I accepted that.

Video posters need the same care. I had deferred the enhanced player with an `IntersectionObserver` but left its poster eager, so the page still downloaded posters for videos nobody had scrolled to. Defer both.

## Deferring non-critical JavaScript after page load

Decide what triggers each deferred import, download, or animation:

| Work | A useful starting policy |
| --- | --- |
| Main text, initial styles, LCP resource | Available for the first render |
| A video player or heavy embed further down | Prepare as it approaches the viewport |
| Search, an editor, or a dialog | Load on intent or first use |
| Decorative animation | Start after load, then pause when idle or out of view |
| Third-party scripts | Load when the feature needs them, accounting for measurement |

For decorative work, this helper waits for `load` and an idle slot, and also handles being called after `load` has already fired:

```
export function afterPageLoad(callback: () => void) {
  let idle = 0;
  let timer = 0;

  const schedule = () => {
    if (typeof requestIdleCallback === 'function') {
      idle = requestIdleCallback(callback, { timeout: 2000 });
    } else {
      timer = window.setTimeout(callback, 200);
    }
  };

  if (document.readyState === 'complete') schedule();
  else window.addEventListener('load', schedule, { once: true });

  return () => {
    window.removeEventListener('load', schedule);
    if (idle) cancelIdleCallback(idle);
    window.clearTimeout(timer);
  };
}
```

Call it from client-side setup and cancel the pending callback during cleanup. Any loop or subscription the callback starts needs its own cleanup. Postponing work doesnât reduce it, either. I found an idle animation on my home page updating SVG geometry about 30 times a second. Its loop needed to stop at rest.

Deferral has costs. My analytics now loads on first interaction or a few seconds after load, so it can miss a very short visit. The form verification script loads when someone focuses the form, which gives it time to start before the first submit. Test these features as someone who acts the moment the page appears.

## React Compiler and bundle size

I had adopted the [native React Compiler](https://oxc.rs/blog/2026-08-18-react-compiler-support.html#vite) before this work. In five alternating baseline and compiled pairs on three routes, timings stayed roughly unchanged while compressed JavaScript grew by 9.5 to 14.1 KiB per route.

I kept it because it replaced hand-written memoization, a maintenance benefit I wanted at a measured byte cost. It never decided whether a closed dialog or an image catalog belonged in the first load. Test compiler changes separately from loading changes, or one will hide the other.

By this point, the obvious waste was gone. What remained was the stylesheet, where each improvement cost more to build and maintain.

## Does critical CSS help in TanStack Start?

Start with the stylesheet imports. Keep shared tokens and base styles global, and put feature styles with their route or component. Start tracks side-effect CSS imports and CSS modules in its route manifest; an explicit `?url` link returned from `head().links` sits outside it. The [CSS styling guide](https://tanstack.com/start/latest/docs/framework/react/guide/css-styling) covers both.

After trimming the imports, choose a delivery strategy:

| Strategy | Benefit | Cost to measure |
| --- | --- | --- |
| External route CSS | Reusable browser cache | A blocking request on a cold visit |
| Inline route CSS | Removes that stylesheet request | More HTML on every document load |
| Extracted critical CSS plus deferred stylesheets | Fewer rules needed before paint | Extraction complexity and more states to verify |

Start has an experimental, production-only option for inlining route CSS from its manifest:

```
tanstackStart({
  server: {
    build: { inlineCss: true },
  },
});
```

I tried all three. Inlining repeated my full route stylesheet in every HTML document, including feature styles that had accumulated in the global CSS. I moved those styles to their owners and returned to external files, which roughly halved the home pageâs HTML. PageSpeed Insights couldnât tell the two choices apart. The inlined build scored 91 to 95 across three mobile runs, and the first two runs after the switch scored [92](https://pagespeed.web.dev/analysis/https-sarthakmishra-com/ilmnkrz1n9?form_factor=mobile) and 97.

The third attempt used [Beasties](https://github.com/danielroe/beasties) to extract the rules matching each prerendered document. I inlined those and deferred the complete stylesheets with the [`media="print"` and `onload` pattern](https://web.dev/articles/defer-non-critical-css), plus a `<noscript>` fallback. Beasties matches selectors against the document rather than measuring a viewport, so its output can include content below the fold.

The extracted pages then exposed assumptions the static HTML didnât show:

- Dark mode wasnât represented in the build-time HTML.
- Font families selected through CSS variables lost their declarations.
- Selectors for selected form controls were dropped.
- Preload headers would have promoted the deferred stylesheets back to high priority.

I compared all 71 prerendered pages with critical CSS alone against full styles, at phone and desktop widths, in light and dark themes, and tested navigation and the no-JavaScript fallback. Render-blocking CSS went from between 20.6 and 29.7 KiB per page to between 7.0 and 14.9 KiB. Pages rendered at request time kept their normal blocking stylesheets. My Cloudflare Early Hints now carry only the heading font.

The reduction is real, and I canât show what it did to the score. It also left me maintaining a selector allowlist, font handling, and a set of states to recheck whenever the site changes. Iâd want a clear stylesheet bottleneck in the trace before taking that on in another app.

Then I did the same thing with JavaScript.

## Should you defer hydration in TanStack Start?

If JavaScript still blocks startup, check which server-rendered sections must become interactive immediately. Related articles can wait. A checkout form canât.

Start documents an experimental [`Hydrate` boundary](https://tanstack.com/start/latest/docs/framework/react/guide/deferred-hydration) that keeps the server HTML while delaying a sectionâs hydration, and by default splits its code into a separate chunk:

```
import { Hydrate } from '@tanstack/react-start';
import { visible } from '@tanstack/react-start/hydration';
import { Reviews } from './Reviews';

export function DeferredReviews() {
  return (
    <Hydrate when={visible({ rootMargin: '600px' })}>
      <Reviews />
    </Hydrate>
  );
}
```

Check support in your installed Start version. The boundary controls initial hydration only. Later client-side mounts behave differently, and updates can trigger hydration early. The server HTML still needs its CSS before hydration.

I went further than that on my site. A build step rewrites Startâs emitted preload links and entry script so the whole application starts after the browser paints the prerendered HTML. It fails the build if Start emits markup the transform doesnât recognize.

Test what happens before hydration finishes: scroll, follow a link, focus a control. When a reader scrolled early, my router took over and sent them from 2,000 pixels down the page back to the top. An existing video test caught it, and I had to preserve that early scroll while keeping normal restoration for later navigation.

The score was inconclusive. A preview copy of the critical-CSS build scored 100 with 0.9-second FCP and LCP, and that copy didnât delay startup at all. Production with the delayed startup still returned 92. The October 26 run that scored 100 came from a later deploy containing both techniques and some unrelated work, the same day both techniques had scored 92 on production. Lighthouseâs [simulated throttling](https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md) models slower conditions from an observed load, so small differences in what it observes can move the result. I canât credit the production score to the delayed startup, and I canât rule it out either.

For another app, Iâd try a `Hydrate` boundary around the sections that can wait before delaying every React-controlled interaction.

## How I used Claude Code and Codex

I split this work between Claude Code and Codex, often handing oneâs result to the other. They made changes and measured them; I decided what to keep.

Claude Code did the first round on October 24. I gave it the 73 report and asked why mobile was slow. It read the report, found that the HTML arrived in about 110 ms, and identified the paragraph LCP and the downloads competing with it. Over that evening it trimmed font preloads, delayed the home pageâs animations, moved analytics after load, raised the post heroesâ fetch priority, and found the 117-image manifest that every page was loading. It also ran Unlighthouse across 17 representative pages, so I wasnât optimizing the home page alone.

Codex took the CSS work on October 25. It moved feature styles out of the global stylesheet, measured HTML size with and without inlining, switched to external CSS, and added CSS and font Early Hints. When I asked for real PageSpeed Insights results instead of local Lighthouse CLI runs, it collected before-and-after batches and caught PageSpeed reusing cached audits under new report links.

The two tools also disagreed. On October 24, Claude Code advised against critical CSS because Lighthouse estimated no FCP or LCP savings from the single blocking stylesheet. When the score dipped again, I asked it to build the pipeline anyway, with a requirement to test it rigorously and remove it if it didnât hold up. It built the Beasties step and the delayed startup, compared all 71 pages across themes and widths, deployed preview variants to Cloudflare, and found the scroll-restoration bug. When production stayed at 92, I had it save the work on a branch and roll production back.

Codex later reworked both transforms as Vite plugins and redeployed them. It also built the delayed sidebar reveal and worked out that my local mobile score of 95 came mostly from an uncompressed preview server.

With the agents, a preview variant, a 71-page comparison, or a rollback took minutes. Deciding whether a 92 and a 97 meant anything stayed my job. So did choosing between a smaller stylesheet and a build step Iâd have to maintain.

## Keeping TanStack Start fast: budgets and browser tests

Once a page performs well, record its asset sizes and fail the build when they grow. Set limits from your measured routes with room for planned additions. These are my portfolioâs limits:

| Measure | Budget |
| --- | --- |
| Render-blocking CSS | 17,500 bytes gzip |
| All linked stylesheets | 34,000 bytes gzip |
| Initial JavaScript | 250,000 bytes gzip |
| Module preloads | 40 |
| Shared content-index chunk | 15,000 bytes gzip |

Count deferred downloads too. My JavaScript budget includes the entry and preloads that startup defers, and deferred stylesheets count toward the total CSS limit. Otherwise moving a tag would look like removing bytes.

Add browser tests for the behaviors this kind of work puts at risk: main content present before hydration, fonts settling without reflow, hidden assets staying unloaded, dialogs returning focus, and hydration preserving an early scroll.

Check pages beyond the home page as well. On October 26, the [Blog listing](https://pagespeed.web.dev/analysis/https-sarthakmishra-com-blog/rw0qk89bxu?form_factor=mobile) scored 100 and [Newsletter Issue 1](https://pagespeed.web.dev/analysis/https-sarthakmishra-com-newsletter-issue-1/fzfp00vdsl?form_factor=mobile) scored 99. The image-heavy posts on [fixing exams](https://pagespeed.web.dev/analysis/https-sarthakmishra-com-blog-stop-fixing-exams/gh12w1kooy?form_factor=mobile) and [building the interactive SVG avatar](https://pagespeed.web.dev/analysis/https-sarthakmishra-com-blog-building-interactive-svg-avatar/xip0px5rg0?form_factor=mobile) were still at 89 and 88, both with 3.5-second LCP and zero blocking time.

So for your own Start app, Iâd begin with the catalog, the closed features, the fonts, and the hidden requests, which the browser can skip entirely. For mine, the next round goes to the LCP images on those two posts.
