---
type: twir-item
issue: 271
item: 1
item_type: featured
date: 2026-03-04
source: https://thisweekinreact.com/newsletter/270#react
tags:
  - "Vinext"
  - "Nextjs"
  - "Router"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 1: covered Vinext

Source: [https://thisweekinreact.com/newsletter/270#react](https://thisweekinreact.com/newsletter/270#react)

Summary:
The React Foundation has officially launched, moving React and related projects under the Linux Foundation with new founding members. Cloudflare rebuilt the Next.js API surface using AI in a week, resulting in a performant, test-covered alternative called vinext, now running in production for some sites. Next.js is adding version-matched documentation to support AI agents, and several new patterns and tools are highlighted, including improvements in React Router, component design, and performance. The section also notes the importance of comprehensive test suites for enabling rapid, reliable software development, especially in the context of AI-generated code.

Key takeaways:
- React is now governed by a new foundation under the Linux Foundation, no longer solely by Meta.
- Cloudflare’s AI-driven vinext demonstrates the power and risks of AI-generated framework clones, emphasizing the value of strong specs and tests.
- Next.js is improving documentation to better support AI agents and developer workflows.
- Several new patterns and tools are emerging for React Router, component abstraction, and performance optimization.

Recommendation:
Summary sufficient

Content:
# This Week In React #270: Next.js, React Router, TanStack, Ink, Async, AI

Hello everyone, Krzysztof and Kacper from [Software Mansion](https://swmansion.com/) here 👋

The React Foundation officially launched. Cloudflare rebuilt the whole Next.js in a week using AI. In the meantime, the real Next.js is adding version-matched docs so agents always have context on new and recently updated APIs.

On the React Native side, Hermes is moving beyond mobile: Hermes-node brings the engine to Node.js as a potential V8 swap. CSS Grid is also coming to React Native, and TanStack Router has an early PoC running natively.

Let's dive in!

As always, thanks for supporting us on your favorite platform:

**Don't miss the next email!**

It works like magic in the background:

- Near-exhaustive coverage on every test run
- No test creation
- **No maintenance (seriously)**
- Zero flakes (built on a deterministic browser)

## ⚛️ React[​](#react "Direct link to ⚛️ React")

[![How we rebuilt Next.js with AI in one week](https://thisweekinreact.com/emails/issues/270/vinext.jpg)](https://blog.cloudflare.com/vinext/)

**[How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)**

A single Cloudflare engineer rebuilt the Next.js API surface (App Router, RSC, Server Actions, middleware) on Vite in one week using AI for $1,100. Using Oxc/Rolldown, it builds 4.4x and produces 57% smaller bundles. Using the Vite Environment API, it overcomes OpenNext limits, making it compatible with edge runtimes such as Cloudflare Workers.

What started as a bold experiment became [vinext](https://github.com/cloudflare/vinext). It passes 2000+ tests and has 94% test coverage of the Next.js 16 API surface. The `cio.gov` website already runs it in production. It also introduces new concepts such as “Traffic-aware Pre-Rendering”.

This AI-driven port was only possible because Next.js has a well-documented API surface and a comprehensive test suite. A reminder of something TDD practitioners have known for years, but seems more important than ever today: the real value lies in the specification, the test suite, and the API design. Even Guillermo Rauch now believes that [most software will start as markdown spec files](https://x.com/rauchg/status/2026091504280944802) implemented by coding agents. In [Tests Are The New Moat](https://saewitz.com/tests-are-the-new-moat), the author argues that we may see more open-source projects with private test suites: that’s what SQLite is already doing.

![](https://thisweekinreact.com/emails/separators/christmas.png)

- 📣 [The React Foundation has officially launched, hosted by the Linux Foundation](https://react.dev/blog/2026/02/24/the-react-foundation) - React, React Native, and supporting projects like JSX are no longer owned by Meta. Huawei joined the previously announced founding members.
- 📖 [Next.js - AI Agents Guide](https://nextjs.org/docs/app/guides/ai-agents) - Upcoming Next.js releases will include version-matched docs to provide agents with up-to-date context, improving [Next.js Evals](https://nextjs.org/evals) success rate by ~20%.
- 📜 [Aurora Scharff - Building Design Components with Action Props using Async React](https://aurorascharff.no/posts/building-design-components-with-action-props-using-async-react/) - Pattern for encapsulating optimistic updates, pending indicators, and rollback inside reusable components
- 📜 [TkDodo - Creating Query Abstractions](https://tkdodo.eu/blog/creating-query-abstractions) - Using `queryOptions` is an alternative to hooks for achieving a reusable data object. This approach allows you to use the object even outside of React components.
- 📜 [Kent C. Dodds - Migrating Remix v2 to React Router v7 with Cursor](https://kentcdodds.com/blog/how-i-used-cursor-to-migrate-frameworks) - Showcases how he used Composer for large-scale dependency upgrades completed in a day.
- 📜 [React Router Loaders and Actions as Integration Points](https://sergiodxa.com/articles/react-router-loaders-and-actions-as-integration-points) - Testing routing with business logic in isolation is tough due to complex mocking. The author suggests that mixing unit and e2e tests can solve that.
- 📜 [Create a Multi-Directory Route Organization in React Router](https://sergiodxa.com/tutorials/create-a-multi-directory-route-organization-in-react-router) - By using `flatRoutes`, you can maintain a scalable structure with better logic separation in a growing React Router application.
- 📜 [Removing Next.js Taught Me Why Frameworks Are Still Essential Even for AI](https://zenn.dev/smartvain/articles/coding-agent-kills-framework-nextjs-reverse-truth?locale=en) - The author tried building with HTML and vanilla JS, then concludes that frameworks are necessary precisely because we are in the era of agents, giving them useful constraints. Note that Elon Musk predicts something different: AI will bypass coding and directly create binaries ([tweet](https://x.com/XFreeze/status/2021699619927781842)).
- 📜 [React’s useTransition: The hook you’re probably using wrong](https://www.nutrient.io/blog/react-usetransition-guide/)
- 📜 [Creating a 3D Product Grid with React Three Fiber](https://tympanus.net/codrops/2026/02/24/from-flat-to-spatial-creating-a-3d-product-grid-with-react-three-fiber/)
- 💸 [Product for Engineers - 10x job posts for 10x engineers](https://go.posthog.com/twir-feb25)
- 📦 [Ink 6.8 - `renderToString()`, React DevTools v7, performance caching](https://github.com/vadimdemedes/ink/releases/tag/v6.8.0)
- 📦 [Split Pane 3.2 - `pointerType` in ResizeEvent](https://github.com/tomkp/react-split-pane/releases/tag/v3.2.0)
- 📦 [Vercel Chat SDK - Lets you build chatbots, supports JSX syntax](https://vercel.com/changelog/chat-sdk)
- 🎥 [Josef Bender - Build a blog with type-safe Markdown and TanStack Start](https://www.youtube.com/watch?v=Cw8scPKibe8)
- 🎥 [Fireship - TanStack Start in 100 Seconds](https://www.youtube.com/watch?v=1fUBWAETmkk)
- 🎥 [Hamed Bahram - Master nuqs in 1 hour - URL state in NextJs with François Best](https://www.youtube.com/watch?v=_L3uM8hD1wg)

**Don't miss the next email!**

Tired of rewriting the same MUI forms across projects? **FormEngine Core** lets you build once in JSON and deploy everywhere no deep React knowledge required.

**Why developers are switching**

- **Write once, use anywhere:** One JSON schema works across all your apps
- **Native MUI support:** Ready-to-use component package
- **Lightweight:** 188.54 KB gzipped (FormEngine Core + MUI)
- **Next.js & Remix ready:** Drop-in support for modern frameworks
- **Localization:** Powerful form localization with Fluent.js
- **Custom actions:** Interactive logic through custom JavaScript

**Perfect for:** backend-driven forms, conditional logic, complex forms, admin panels, and multi-step wizards.  
**Open source & free forever** no vendor lock-in, no nonsense. Trusted by enterprises.  

## 📱 React-Native[​](#react-native "Direct link to 📱 React-Native")

[![Hermes-node](https://thisweekinreact.com/emails/issues/270/hermes.jpg)](https://x.com/tmikov/status/2024609186936660170)

**[Hermes-node](https://x.com/tmikov/status/2024609186936660170)**

Tzvetan Mikov from the Hermes team announced Hermes-node, a CLI version of Hermes compatible with the Node.js API. Since Hermes-node acts as a compatibility layer, it can use original Node.js module implementations without needing to rewrite them - most work out of the box. You can think of this as simply swapping the V8 engine for Hermes. If combined with compiling Hermes to binary code, this feature could bring significant benefits to the entire Node.js ecosystem.

![](https://thisweekinreact.com/emails/separators/christmas.png)

- 💸 [Amazon Developer – Build Fire TV apps with React Native on Vega OS. Port your apps, expand your reach, and monetize.](https://fandf.co/3My3pHO)
- 👀 [React Native PR - CSS Grid is coming to React Native](https://github.com/facebook/react-native/pull/55665)
- 👀 [Keyboard Controller PR - New `<KeyboardChatScrollView>` component](https://github.com/kirillzyusko/react-native-keyboard-controller/pull/1314) - Eliminates re-layouts during keyboard animations to improve performance
- 🐦 [Tanner Linsley announced](https://x.com/tannerlinsley/status/2024945690737254601) a PoC of TanStack Router running in React Native ([GitHub code](https://github.com/TanStack/router/compare/feat/react-native))
- 🐦 [React Navigation 8 is experimenting with `<Activity>` for freezing and unmounting inactive screens](https://x.com/reactnavigation/status/2025525954618052746)
- 🐦 [Jay Meistrich is testing Legend List v3 in production (Legend App), resulting in significant performance improvements](https://x.com/jmeistrich/status/2024455646368977393)
- 📜 [Brownfield React Native app with multiple screens](https://adrov.me/brownfield-navigation/) - Fixes a ReactFragment lifecycle race condition on Android and a static RN View Factory pattern on iOS - both needed to avoid crashes when pushing multiple RN screens.
- 📜 [The experience of adding E2E testing to React Native with Maestro](https://addjam.com/blog/2026-02-18/our-experience-adding-e2e-testing-react-native-maestro/) - A case study on the benefits of using Maestro over Detox: simpler, platform-agnostic configuration, fewer technical quirks, and a lower barrier to entry.
- 📜 [React Native Comes to Meta Quest](https://reactnative.dev/blog/2026/02/24/react-native-comes-to-meta-quest) - Meta officially announced support for Horizon OS, allowing developers to build VR applications using their existing Android tools and knowledge.
- 📜 [Do you need an MCP to build your native app?](https://sentry.engineering/blog/do-you-really-need-an-mcp-to-build-your-app) - A simple Markdown file with basic instructions can work better and is more affordable than a complex MCP from Xcode.
- 📦 [QuickPush 2.0 - MacOS menu bar app for testing Expo Push Notification](https://codewithbeto.dev/tools/quickPush) - Paid tool, can be used for free by compiling it from sources.
- 📦 [RN Vibe Code - an open-source IDE for vibe coding](https://github.com/react-native-vibe-code/react-native-vibe-code-sdk) - Runs in the browser.
- 📦 [Sentry React Native 8.1 - `enableTombstone` for native crash reporting on Android 12+, iOS view filtering for session replay](https://github.com/getsentry/sentry-react-native/releases/tag/8.1.0)
- 📦 [Posthog React Native 4.36 - Manual session replay control](https://github.com/PostHog/posthog-js/releases/tag/posthog-react-native%404.36.0) - New `startSessionRecording`, `stopSessionRecording`, and `isSessionReplayActive` methods.
- 📦 [Stripe React Native 0.59 - Connect Embedded Components (preview), Radar session support](https://github.com/stripe/stripe-react-native/releases/tag/v0.59.0)
- 📦 [Datadog 3.1.0 - Feature Flags](https://github.com/DataDog/dd-sdk-reactnative/releases/tag/3.1.0) - Using an open standard for feature flag management.
- 📦 [Bottom Tabs 7.14 - Support hiding the native tab bar](https://github.com/react-navigation/react-navigation/releases/tag/%40react-navigation/bottom-tabs%407.14.0)
- 📦 [Screens 4.24 - Last release with Legacy Architecture support, Split View enhancements, iOS 26 fixes](https://github.com/software-mansion/react-native-screens/releases/tag/4.24.0) - Next version will drop support for RN < 0.82 and only support the New Architecture.
- 📦 [Async Storage 3.0 - Instance-based storage, promise-only API, renamed batch methods](https://github.com/react-native-async-storage/async-storage/releases/tag/%40react-native-async-storage%2Fasync-storage%403.0.0) - Breaking major, consult migration guide to v3.
- 📦 [Number Flow 0.2 - New library that provides Text component with build in rolling counter animation](https://github.com/Rednegniw/number-flow-react-native)
- 📦 [Markdown Renderer 4.0](https://github.com/mientjan/react-native-markdown-renderer/releases/tag/v4.0.0)
- 📦 [Quick Crypto 1.0.12 - Full NodeJS Crypto API compatibility](https://github.com/margelo/react-native-quick-crypto/releases/tag/v1.0.12)
- 🤖 [Expo Skills - Official collection](https://expo.dev/expo-skills)
- 🎥 [React Universe Meetup x Zalando - All the talks are online](https://www.youtube.com/playlist?list=PLZ3MwD-soTTHSEF1_8J3JTTe6SfHGTc8w)
- 🎥 [Callstack - Using Apple Intelligence Seamlessly With @react-native-ai/apple](https://www.youtube.com/watch?v=do1NdvGQRlg)
- 🎥 [Callstack - MLC LLM + React Native: On-Device AI Without the Pain](https://www.youtube.com/watch?v=ohFPD_hWUzU)
- 🎙️ [Rocket Ship 92 - React Native 0.84, Hermes V1 & A TanStack React Native Framework?](https://share.transistor.fm/s/c2223e49)

![](https://thisweekinreact.com/emails/separators/christmas.png)

## 🔀 Other[​](#other "Direct link to 🔀 Other")

## 🤭 Fun[​](#fun "Direct link to 🤭 Fun")

[![alt](https://thisweekinreact.com/emails/issues/270/meme.jpg)](https://x.com/AdrianDittmann/status/2026184733743587420)

See ya! 👋
