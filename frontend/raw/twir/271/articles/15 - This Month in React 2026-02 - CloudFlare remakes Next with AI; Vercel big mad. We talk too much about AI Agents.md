---
type: twir-item
issue: 271
item: 15
item_type: item
date: 2026-03-04
source: https://share.transistor.fm/s/de32a7b9
tags:
  - "2026-02"
  - "CloudFlare"
  - "mad"
  - "Vinext"
  - "Survey"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 15: This Month in React 2026-02 - CloudFlare remakes Next with AI; Vercel big mad. We talk too much about AI Agents

Source: [https://share.transistor.fm/s/de32a7b9](https://share.transistor.fm/s/de32a7b9)

Summary:
This podcast episode covers major React ecosystem news for February 2026, including the React Foundation launch, AI-driven framework development (Cloudflare’s vinext), and community/state-of-survey results. It discusses React core updates, new releases, and the broader impact of AI agents on software development productivity and workflow. The episode also touches on industry trends, open source project health, and developer experience.

Key takeaways:
- React Foundation’s launch and AI-generated framework clones are reshaping the ecosystem.
- State of JS/React/React Native surveys provide insights into developer pain points and adoption.
- AI agents are increasingly influencing development workflows, raising both opportunities and challenges.

Recommendation:
Summary sufficient (listen for deeper discussion or if interested in community/industry trends)

Why it matters:
listen for deeper discussion or if interested in community/industry trends

Content:
# This Month in React

[Transcript and links](http://reactiflux.com/transcripts/tmir-2026-02)

- ([00:00](#t=0m0s "Jump to 00:00 in this episode")) - This Month in React February 2026
- ([01:46](#t=1m46s "Jump to 01:46 in this episode")) - New releases
- ([01:50](#t=1m50s "Jump to 01:50 in this episode")) - [TS 6.0 beta](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)/! (last TS impl release; stricter defaults)
- ([02:34](#t=2m34s "Jump to 02:34 in this episode")) - [Yarn 6 preview](https://yarn6.netlify.app/blog/2026-01-28-yarn-6-preview/) (rewritten in Rust)
- ([02:52](#t=2m52s "Jump to 02:52 in this episode")) - [Electrobun](https://blackboard.sh/electrobun/docs/) (Tauri alternative)
- ([03:31](#t=3m31s "Jump to 03:31 in this episode")) - [React Native Gesture Handler v3](https://blog.swmansion.com/introducing-gesture-handler-3-0-hook-based-api-deeper-reanimated-integration-more-9185b0c8e305)
- ([04:20](#t=4m20s "Jump to 04:20 in this episode")) - [Next polyfills improved WebStreams and upstreaming to Node](https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster)
- ([05:25](#t=5m25s "Jump to 05:25 in this episode")) - [Webpack 2026 roadmap](https://webpack.js.org/blog/2026-04-02-roadmap-2026/)
- ([05:53](#t=5m53s "Jump to 05:53 in this episode")) - [Lodash maintenance roadmap](https://socket.dev/blog/inside-lodash-security-reset)
- ([07:07](#t=7m7s "Jump to 07:07 in this episode")) - [Gatsby React 19 support](https://www.gatsbyjs.com/docs/reference/release-notes/v5.16/) , [styled-components RSC support](https://styled-components.com/releases#styled-components@6.3.0)
- ([07:54](#t=7m54s "Jump to 07:54 in this episode")) - [npmx.dev](https://npmx.dev/) (alternate NPM site UI)
- ([08:43](#t=8m43s "Jump to 08:43 in this episode")) - [eslint-plugin-react-render-types](https://github.com/HorusGoul/eslint-plugin-react-render-types) (typed children)
- ([09:54](#t=9m54s "Jump to 09:54 in this episode")) - Main Content
- ([09:55](#t=9m55s "Jump to 09:55 in this episode")) - React Core updates:
- ([09:56](#t=9m56s "Jump to 09:56 in this episode")) - [React Foundation officially launched](https://react.dev/blog/2026/02/24/the-react-foundation)
- ([12:28](#t=12m28s "Jump to 12:28 in this episode")) - Docs updates: [/`useActionState/`](https://github.com/reactjs/react.dev/pull/8284) (merged), [/`use/`](https://github.com/reactjs/react.dev/pull/8305) and [RSC sandboxes](https://github.com/reactjs/react.dev/pull/8300) (wip)
- ([14:23](#t=14m23s "Jump to 14:23 in this episode")) - [React Native 0.84 released](https://reactnative.dev/blog/2026/02/11/react-native-0.84)
- ([17:47](#t=17m47s "Jump to 17:47 in this episode")) - [Hermes WASM support](https://x.com/tmikov/status/2023821160241393839) , [Hermes Node compat CLI](https://x.com/tmikov/status/2024609186936660170)
- ([18:43](#t=18m43s "Jump to 18:43 in this episode")) - “State of…” survey results
- ([18:43](#t=18m43s "Jump to 18:43 in this episode")) - [State of JS 2025 results](https://2025.stateofjs.com/en-US)
- ([19:06](#t=19m6s "Jump to 19:06 in this episode")) - [State of React 2025 results](https://2025.stateofreact.com/en-US)
- ([19:51](#t=19m51s "Jump to 19:51 in this episode")) - [Aurora Scharff’s conclusion](https://2025.stateofreact.com/en-US/conclusion/)
- ([20:44](#t=20m44s "Jump to 20:44 in this episode")) - [Josh Comeau’s takes on the results](https://bsky.app/profile/joshwcomeau.com/post/3mf642css6227)
- ([21:28](#t=21m28s "Jump to 21:28 in this episode")) - [API pain points](https://2025.stateofreact.com/en-US/features/#main\_apis\_pain\_points)
- ([21:53](#t=21m53s "Jump to 21:53 in this episode")) - [State of React Native 2025](https://results.2025.stateofreactnative.com/en-US/)
- ([24:29](#t=24m29s "Jump to 24:29 in this episode")) - [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)
- ([29:52](#t=29m52s "Jump to 29:52 in this episode")) - CloudFlare v Vercel beef
- ([35:42](#t=35m42s "Jump to 35:42 in this episode")) - Carl Vitullo monologs about AI Agents
- ([42:27](#t=42m27s "Jump to 42:27 in this episode")) - AI productivity and impacts on our attention
- ([44:42](#t=44m42s "Jump to 44:42 in this episode")) - ["wrote a spec, pointed Claude at an Asana board, and went home"](https://x.com/rvivek/status/2026385957596111044)
- ([47:26](#t=47m26s "Jump to 47:26 in this episode")) - [Bits AI SRE | Datadog](https://www.datadoghq.com/product/ai/bits-ai-sre/)
- ([51:04](#t=51m4s "Jump to 51:04 in this episode")) - [ThoughtWorks opines on AI productivity impacts](https://simonwillison.net/2026/Feb/14/thoughtworks/)
- ([01:00:28](#t=1h0m28s "Jump to 01:00:28 in this episode")) - ⚡ Lightning round ⚡
- ([01:00:37](#t=1h0m37s "Jump to 01:00:37 in this episode")) - [“Wall Street Raider” game modernization](https://www.wallstreetraider.com/story.html) (and uses Preact)
- ([01:01:16](#t=1h1m16s "Jump to 01:01:16 in this episode")) - [Github Stacked Diffs preview](https://x.com/jaredpalmer/status/2019817235163074881) , [faster Issues search](https://github.blog/changelog/2026-01-29-improved-search-for-github-issues-in-public-preview/)
- ([01:02:08](#t=1h2m8s "Jump to 01:02:08 in this episode")) - [Josh Comeau: Sprite animations](https://www.joshwcomeau.com/animation/sprites/)
- ([01:02:26](#t=1h2m26s "Jump to 01:02:26 in this episode")) - [Interop 2026](https://wpt.fyi/interop-2026), ([WebKit](https://webkit.org/blog/17818/announcing-interop-2026/), [Igalia](https://www.igalia.com/news/interop-2026.html))
- ([01:03:38](#t=1h3m38s "Jump to 01:03:38 in this episode")) - Conferences ([React](https://react.dev/community/conferences), [Javascript](https://confs.tech/javascript))

[Reply on Bluesky](https://bsky.app/profile/did:plc:yfqlzwi66ubgasg5z6pjiudc/post/3mg4zxws7vo2z "Reply on Bluesky")
**[★ Support this podcast ★](https://donate.stripe.com/14A4gyfrP5YS0Za6HbfMA04 "★ Support this podcast ★")**

#### Creators and Guests

![](https://img.transistorcdn.com/ftpSmkw9Tm5LjlTFZ4mO7VuEoI4CeHFeaHilFPP1c7o/rs:fill:0:0:1/w:400/h:400/q:60/mb:500000/aHR0cHM6Ly9pbWct/dXBsb2FkLXByb2R1/Y3Rpb24udHJhbnNp/c3Rvci5mbS81YzAz/ODMzZDM1YTMzM2U5/MTVkOWI1NGRlNmE0/MTA2NC5wbmc.webp)

Host

Mark Erikson

An engineer maintaining Redux and Redux Toolkit, working at Replay.io to make smarter AI chat bots and debuggers using time travel.

![](https://img.transistorcdn.com/emX7Ha137OD3RtqqqBJH-8ykM1wo9eVBe60JITJRiJA/rs:fill:0:0:1/w:400/h:400/q:60/mb:500000/aHR0cHM6Ly9pbWct/dXBsb2FkLXByb2R1/Y3Rpb24udHJhbnNp/c3Rvci5mbS9kN2Ex/YzczYTJhNWI1NmQy/MDQzYWRmOWZjYWZj/NjU2Mi5qcGVn.webp)

Host

Mo

Head of Mobile at Theodo, a software consultancy that does native app development for iOS and Android

![](https://img.transistorcdn.com/x2NNMOHgG1DVRiGIRNOaWB8cqKyUYJO2sjULdMIJhJg/rs:fill:0:0:1/w:400/h:400/q:60/mb:500000/aHR0cHM6Ly9pbWct/dXBsb2FkLXByb2R1/Y3Rpb24udHJhbnNp/c3Rvci5mbS82ODQ2/MzlmNWM3MjdlZGVm/YWY5MTA4ZWI4MGE5/ODU0NC5qcGVn.webp)

Producer

Carl Vitullo

Solopreneur just vibing, posts are probably bullshit. Community lead at Reactiflux, the largest chat community of React professionals.

#### What is This Month in React?

How busy professionals stay on top of the React ecosystem. We give you a 1 hour recap of the latest news and nuance in React's development and ecosystem, upcoming conferences, and open source releases. New episodes the first week of every month, with live recordings on the last Wednesday of every month in the Reactiflux stage.

Hosted Mark Erikson (Redux maintainer), Carl Vitullo (startup veteran), and Mo Khazali (head of mobile at Theodo). See something for us? Post to #tech-reads-and-news
