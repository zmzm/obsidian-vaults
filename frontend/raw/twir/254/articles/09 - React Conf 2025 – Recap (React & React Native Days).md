---
type: twir-item
issue: 254
item: 9
item_type: item
date: 2025-10-15
source: https://blog.swmansion.com/react-conf-2025-recap-922c50d97318
tags:
  - "2025"
  - "Compiler"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2025-10-15-TWIR-254|Index]]

# Item 9: React Conf 2025 – Recap (React & React Native Days)

Source: [https://blog.swmansion.com/react-conf-2025-recap-922c50d97318](https://blog.swmansion.com/react-conf-2025-recap-922c50d97318)

Summary:
This recap summarizes major announcements from React Conf 2025, including new features like captureOwnerStack, Activity, mode="hidden"/"visible", useEffectEvent, partial pre-rendering, and React Performance tracks. Other highlights include the declarative <ViewTransition> component, fragment refs, React Compiler 1.0, and the formation of the React Foundation. The summary also covers React Native updates, app highlights, and community statistics.

Key takeaways:
- React 19.1/19.2 introduce new debugging, performance, and animation features.
- Activity and mode="hidden"/"visible" enable advanced UI state management.
- React Compiler 1.0 offers automatic memoization and improved performance.
- The React Foundation formalizes community stewardship with major industry partners.

Recommendation:
Read fully (for a comprehensive overview of React’s latest features and ecosystem direction)

Why it matters:
for a comprehensive overview of React’s latest features and ecosystem direction

Content:
# React Conf 2025 - Recap

**Now that the dust has settled, let’s summarize the most important announcements from both days of** [**React Conf 2025**](https://conf.react.dev/) **so you don’t miss a thing!**

## Day 1 (React keynote)

### Intro

- [Joe Savona](https://x.com/en_js) announced that React has surpassed **6,000,000,000+ total downloads** on npm.
- **React Server Components became mainstream**; widespread support in Expo, Next, Parcel, Router, Redwood, TanStack, Vite, Waku.
- **React 19.1:** `captureOwnerStack` — dev-only feature more precise information about the source of an error (not a component stack).
- New features, e.g. **Sibling pre-warming** — schedule a pre-warm of remaining siblings to fetch their data too, show fallbacks earlier while continuing prefetching data early.
- **Docs improvements —** e.g. [Build a React app from Scratch](https://react.dev/learn/build-a-react-app-from-scratch)
- LLMs and agents have dramatically improved. What makes React great for humans makes React great for AI. But **AI is just a tool** like linters, autocomplete or devtools.
- The current goal for React is to raise the bar for **responsive user experiences** and **lower the barrier to entry.**

### <Activity>

[Mofei Zhang](https://x.com/zmofei) announced **a new component that lets you hide and restore the UI while keeping the internal state** of the children (like uncontrolled text input content or scroll offset). It’s way more than just about setting the visibility in DOM as it also integrates with other React features.

- `mode="hidden"` — visually hide components; low priority and interruptible updates; **state and DOM nodes persist**; effects left unmounted; not server rendered or hydrated.
- `mode="visible"` — visually reveal components; default priority updates.

### useEffectEvent

A more advanced hook that lets you extract non-reactive logic from your Effects into a **reusable** function called an [Effect Event](https://react.dev/learn/separating-events-from-effects#declaring-an-effect-event). It gives you more fine-grained control over effects.

### Partial pre-rendering

It’s a new server feature that lets you render the static parts of your app and serve it from CDN and then resume the shell to fill it with dynamic content on client side. SSR can use cache resources to let the user see a shell much faster.

### React Performance tracks

A new profiling tool that lives in the Performance panel in the DevTools. It lets you see a timeline of all work done in React. There are 4 subtracks in the **Scheduler** **track** representing a specific priority:

- **Blocking** — synchronous updates which could have been initiated by user interactions.
- **Transition** — any background work under the hood, usually initiated via `startTransition`; can’t stop browser from painting.
- **Suspense** — revealing the content or displaying the fallbacks of `Suspense` component.
- **Idle** — lowest priority work that executes only if there are no tasks with higher priority; used by `Activity`.

![](https://strapi-production-5f3f.up.railway.app/uploads/react_conf_2025_recap_922c50d97318_inline_1_a74a9ceb2d.png)

You‘ll also find the **Components track** which visualizes the durations of React component using a framegraph. [React Performance tracks](https://react.dev/reference/dev-tools/react-performance-tracks) are enabled by default in development builds. For profiling builds, enabled for subtrees wrapped in `<Profiler>` component or for the whole app if you have React DevTools attached. Available in React 19.2.

![](https://strapi-production-5f3f.up.railway.app/uploads/react_conf_2025_recap_922c50d97318_inline_2_3425891d46.png)

### <ViewTransition>

[Jack Pope](https://x.com/__jackpope) introduced a new component that wraps [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) in a declarative way. It lets you avoid common pitfalls like timing or scoping issues when using the View Transitions API directly and manages the view transitions names automatically. It also uses a set of heuristics to determine what and when to animate. By default, the browser-default view transition is used (crossfade), but you can use CSS pseudo-elements to customize the effect further. Available in the canary release.

- **Update animations (default)** — triggered by `startTransition()`, `useDeferredValue()` and `Suspense`.
- **Enter animations** — when component with `ViewTransition` at the top level is mounted, revealed from `Suspense` or revealed from `Activity`.
- **Exit animations** — when component with `ViewTransition` at the top level is unmounted, hidden from `Suspense` or hidden with `Activity`.
- **Share animations** — “magic move”-like effect for a pair of `ViewTransition` components with matching names when one is hidden and the other one appears in the same update.

### Fragment Refs

It’s a new composition model to compose platform behavior without requiring additional element wrappers or even having control over child components. Fragment refs can be integrated at the framework, library or design system levels and used throughout the product code to significantly **lower the complexity** of the product code. `FragmentInstance` objects expose methods for interacting with the DOM nodes wrapped by the fragment like `addEventListener`/`removeEventListener`, `getClientRects`, `focus`/`blur` and [many more](https://react.dev/reference/react/Fragment#fragmentinstance).

### React Compiler

Lauren Tan announced that **React Compiler 1.0 is now available**! The compiler itself is a Babel plugin that provides automatic memoization across all platforms, doesn’t require any code rewrites, it’s compatible with React 17, 18 and 19 and can be [adopted incrementally](https://react.dev/learn/react-compiler/incremental-adoption). It also comes with an ESLint plugin that **enforces rules of hooks** and **prohibits bad patterns** (like setting state in `useEffect` or inside render function, setting state that comes from a parent component, or reading React refs during render). With the compiler enabled, the apps in Meta Quest Store saw up to **2.5x faster interactions**, up to **12% faster initial load and navigation** and overall **neutral impact on memory usage**. For more details, check out [React Compiler docs](https://react.dev/learn/react-compiler).

### React Foundation

## Day 2 (React Native keynote)

### Intro

[Jorge Cohen](https://x.com/jorgewritescode) (Engineering Manager in React team at Meta) reminded us why developers choose and love React Native:

- With React Native, you get the efficiency of React development combined with the native looks of iOS and Android apps.
- Basically Same React as for web but with the power and **performance of native** **mobile applications**.
- You can also build powerful **native modules** and **extensions**, including widgets and [live activities](https://github.com/software-mansion-labs/expo-live-activity).
- [React Conf app](https://github.com/expo/react-conf-app) is built from single codebase yet each version adapts seamlessly to the **unique design language** and **conventions of the respective platforms**.

### State of React Native

[Nicola Corti](https://github.com/cortinico) (Software Engineer in React team at Meta) shared some interesting numbers:

- **4M downloads a week** in 2025 (compared to 2M in 2024, 100% growth)
- **120M total downloads in 2025** so far, expected **160M until the end of year** (compared to 117M in 2024)
- Shipping 6 releases per year (more frequently than in 2024) — that’s a new minor version every 2 months!
- [React Native 0.82](https://reactnative.dev/blog/2025/10/08/react-native-0.82) released on npm
- React Native 0.83 coming in December 2025
- **2000+ libraries** listed in [React Native directory](https://reactnative.directory/)
- **2700+ unique contributors**

### App highlights

- [**Rise**](https://www.risescience.com/) (sleep tracking app) — elegant UI, smooth animations, stunning charts made with `react-native-skia`.
- [**Runna**](https://www.runna.com/) (running coach app) — deep integration with native platforms, real-time background guidance during workouts, wellness tracking, uses `react-native-skia` for recaps.
- [**Partiful**](https://partiful.com/) (social-event planning app) — **Google Play Best App 2024**, app clip and live activities.
- [**Shopify**](https://www.shopify.com/pl/mobile) — Shopify mobile and Point of Sale apps migrated to New Architecture and achieved **10% faster launch time on Android and 3% faster on iOS** as well as **reduced unnecessary re-renders**: [Migrating to React Native’s New Architecture](https://shopify.engineering/react-native-new-architecture#).
- [**Starlink**](https://www.starlink.com/app) (satellite connectivity app) — uses `react-native-vision-camera` to power FOV screen, truly native experience.
- [**Zalando**](https://www.zalando.pl/) (Europe’s leading online fashion platform) — incrementally migrating their mobile app to RN, modernizing their stack without disrupting user experience at all, use of React Strict DOM to share code between web and native platform: [Accelerating Mobile App development at Zalando with Rendering Engine and React Native](https://engineering.zalando.com/posts/2025/10/accelerating-mobile-app-development-at-zalando-with-rendering-engine-and-react-native.html).
- [**HelloFresh**](https://www.hellofresh.com/) (global leader in meal kit delivery) — actively migrating all of their mobile apps to React Native: [HelloFresh’s Brownfield Leap: One App to Feed Them All!](https://engineering.hellofresh.com/hellofreshs-brownfield-leap-one-app-to-feed-them-all-56244a22ceeb)
- [**Mistral Le Chat**](https://mistral.ai/products/le-chat)(conversational with audio interface) — built entirely with React Native, single codebase.
- [**Replit**](https://replit.com/) — collaborate on code; also entirely built with React Native, all from single codebase.
- [**Vercel v0**](https://v0.app/)— also built with React Native, now available in public beta.
- [**Microsoft Copilot for Office**](https://copilot.microsoft.com/) — copilot integration for Word built entirely with React Native, blends in with the rest of the desktop app.

### Building for future platforms

- **Amazon Vega OS** — first React Native operating system, integrating RN at OS level, elegant TV experiences, running smoothly even on low-end devices: [Announcing Vega OS](https://developer.amazon.com/apps-and-games/blogs/2025/09/announcing-vega-os).
- **Facebook and Instagram VR apps** announced at Meta Connect last year, both built entirely with React Native, showcasing how far the framework has come.
- **New specific features** for VR devices, e.g. parallax effect for images; immersive and dynamic experience.
- [**Expo Go**](https://www.meta.com/pl-pl/experiences/expo-go/25322546364000780/)[**app**](https://www.meta.com/pl-pl/experiences/expo-go/25322546364000780/) is now available on the Meta Horizon Store — huge milestone for React Native and Expo, preview and test your project directly inside headset, hot reload now in VR.

### React Native tooling

- [Expo SDK 54](https://expo.dev/changelog/sdk-54) latest release — support for React Native 0.81, Liquid Glass, precompiled binaries for iOS.
- [Expo App Awards](https://expo.dev/awards) initiative to spotlight beautiful and innovative Expo apps, Expo Launch — ship apps to stores faster than ever before.
- [React Native DevTools](https://reactnative.dev/docs/react-native-devtools) — complete rebuild of debugger architecture, closely integrating with React Native and Hermes, built on standardized web debugging protocols.
- [Radon IDE](https://ide.swmansion.com/) — practical features like inline breakpoints; manage, set and hit breakpoints right where you write the code.

### New capabilities

[Rubén Norte](https://github.com/rubennorte) highlighted several community libraries, announced new features and shared some insights regarding the web alignment efforts.

### Libraries

- [Reanimated v4](https://swmansion.com/blog/reanimated-4-stable-release-the-future-of-react-native-animations-ba68210c3713) — full rewrite of the library built specifically for the new architecture, brings CSS animations and transitions.
- [FlashList v2](https://shopify.engineering/flashlist-v2) & [Legend List 2.0](https://legendapp.com/open-source/list/api/version-2/) — most popular list libraries, rewritten from scratch to leverage the New Architecture; synchronous layout access, cross-platform implementation written exclusively using JavaScript.
- `react-native-enriched` — new library that provides fully native rich text editor, created targeting New Architecture from day one.

### <VirtualView>

A new React Native component aware of its position in the viewport (`hidden`, `prerender`, `visible`) that can be used as a building block for list components.

### Web convergence

- A shift in how we saw cross-platform development from “inspired by web” to “aligned with web”.
- [React Strict DOM](https://facebook.github.io/react-strict-dom/) — stand-alone library polyfilling a subset of web stack like HTML elements and CSS.
- DOM APIs — first time they added imperative API ([Element nodes](https://reactnative.dev/docs/element-nodes)) that integrates directly with React Native renderer, allowing to access the DOM representation of any native component in the application.
- `𝚐getBoundingClientRect` — element size, position on screen, margins.
- `childNodes`, `parentNode` — traverse the tree, including text nodes.
- `ownerDocument` — root of the tree that exposes `getElementById`method.
- Implemented **50+ new properties and methods across 10 web interfaces**. More code can be shared between React Native and web, e.g. using `react-strict-dom`.
- Visual Completion Tracker (first paint, progressive paint, visually complete) — what percentage of the pixels rendered in mutations made it to the final UI. Thanks to web convergence efforts they were able to bring that feature to React apps, reusing most of its code.

### Web performance APIs

[Alex Hunt](https://x.com/huntie) presented the recently added performance features:

- **Event Timings** — visibility inside the runtime from start of user interaction, through the rendering pipeline, to paint.
- **Long Tasks** —tasks in the event loop that block and interrupt rendering across multiple frames which can indicate degraded performance.
- **User Timing** — custom performance events with labels, `performance.mark`, `performance.measure`; like logs but better, high-precision, rendered graphically in the performance timeline, used by libraries and React itself.
- [**PerformanceObserver**](https://reactnative.dev/docs/next/global-PerformanceObserver) — measure performance in production, report telemetry.

### React Native DevTools

- **Performance Panel** coming to RNDT (React Native DevTools).
- **JavaScript Samples** — what code is taking time in Hermes and what has been scheduled on the event loop with visual framegraph reflecting the call stack.
- **User Timings** — custom performance events in the timeline.
- **React Performance tracks** — phases of the scheduler.
- Cascading update — when new update was scheduled during render, common pattern in performance issues.
- Investing in performance: optimized performance builds in open source, more performance features, integrating MCP; working with the Chrome team to build trace events format and in other areas.
- **Network Panel** — native implementation of network inspection in modern debugger stack; `fetch()`, `XMLHttpRequest` (XHR) and `<Image>` component supported out-of-the-box and recorded automatically. Allows you to inspect URLs, metadata, timings and response payloads, rich response preview for both text and image data.
- **Request Initiator** — symbolicated JS call site — which piece of code fired the request.
- **Network track** available in Performance panel.
- Third-party integrator API for frameworks and specialist libraries to hook into the native reporting layer.
- **Desktop app** **for React Native DevTools** — no browser requirement, one window per app, QoL improvements, auto-raise on breakpoint, saved window arrangements across launches.

### New Architecture

[Riccardo Cipolleschi](https://x.com/cipolleschir) talked about the current state of the New Architecture and announced the removal of the Legacy Arch.

- In React Native 0.76, the New Architecture became the default.
- Later on, in May 2025, the Legacy Arch was frozen meaning that pull requests against it were no longer accepted.
- **Starting from 0.82, the New Architecture is the only architecture, or simply “The Architecture”.**
- Benefits of single architecture: **bundle size reduction** (Android ~1 MB, iOS ~0.5 MB), **build time reduction** (from 300 s to 140 s without prebuilts), **simpler mental model**, **faster feature development.**
- **No opt-out from the New Architecture** — `newArchEnabled=false` and `RCT_NEW_ARCH_ENABLED=0` will be ignored!
- **How to migrate** if you’re on older version: first migrate to 0.81 (last version with support for both architectures), then enable the New Architecture, see how the app performs, then update to 0.82 (latest release) — it will be much easier to update next few versions that are going to be released in the future.
- **Interop layers** are here to stay for the foreseeable future — removal of the opt-out is a transparent change; libraries won’t be affected.
- Future plans: complete **removal of Legacy Arch from the codebase.**
- The New Architecture is the **present** of React Native: foundation for smaller app bundle, faster builds and new features such as DOM API, new evolution of the libraries; new libraries to be developed.
- If you’re **not** on the New Architecture, you’re missing out everything that was described today and everything released in the past few version of React Native!

### Hermes V1

- Next evolution of the JS engine with improvements on virtual machine and the compiler for better performance; foundation for just-in-time compilation (JIT) and JavaScript to native compilation (commonly referred to as “Static Hermes”).
- **In the synthetic benchmarks — Hermes V1 outperforms current version across the board with average improvement of 60%.**
- In real world examples ([Expensify](https://www.expensify.com/) app) — up to 9% improvements in Total TTI, Bundle Time, Current TTI; up to 7.6% on low-end devices.
- **Built-in native support** for modern JavaScript features (ES6 classes, public and private class fields, `let` and `const` bindings, async functions, new `Set` methods) — currently they go through Babel plugins, but Hermes V1 supports them natively, we can get rid of all polyfills and embrace **smaller bundles** and **faster loading** times for apps.
- Available starting today as [experimental feature](https://reactnative.dev/blog/2025/10/08/react-native-0.82#how-to-enable-hermes-v1) in React Native 0.82: [**Welcoming the Next Generation of Hermes**](https://swmansion.com/blog/welcoming-the-next-generation-of-hermes-67ab5679e184).
- Huge thank you to [Krzysztof Piaskowy](https://x.com/piaskowyk), [Jakub Piasecki](https://x.com/breskin67) and [Dawid Małecki](https://x.com/coado_dev) from Software Mansion for rolling out this feature.

![](https://strapi-production-5f3f.up.railway.app/uploads/react_conf_2025_recap_922c50d97318_inline_3_8da1400382.png)

### Wrap-up of the keynote

- React Native community is growing and getting stronger every day.
- New web-aligned capabilities with DOM and performance APIs; quality of life improvements made to the tooling; foundation of the future of React Native with Hermes V1.
- React Native has fundamentally changed they way people think about native app development.
- A lot of native UI frameworks have been influenced by this work, including declarative UI programming, component-based architecture, state management, hot reload, focus on developer experience are all industry standard now.

[**Migrate to the React Native New Architecture**](https://swmansion.com/react-native-new-architecture)[*Our team will take care of every step of the migration, so your app runs faster, uses the latest features, and stays…*](https://swmansion.com/react-native-new-architecture)[swmansion.com](https://swmansion.com/react-native-new-architecture)

**Need help with** [**enabling the New Architecture**](https://swmansion.com/react-native-new-architecture)**? Want to use new React features but don’t know how?**

We are Software Mansion — software development consultants, a team of React Native core contributors, multimedia and AI experts. Drop us a line at [projects@swmansion.com](mailto:projects@swmansion.com) and let’s find out how we can work together.

Related notes: [[React Compiler]]
