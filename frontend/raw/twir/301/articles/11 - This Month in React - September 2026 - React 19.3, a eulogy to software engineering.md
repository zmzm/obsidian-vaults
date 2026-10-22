---
type: twir-item
issue: 301
item: 11
item_type: item
date: 2026-10-14
source: https://share.transistor.fm/s/0c8a4fc2
tags:
  - "2026"
  - "193"
  - "TS"
status: auto
quality: keep
---

[[2026-10-14-TWIR-301|Index]]

# Item 11: This Month in React - September 2026 - React 19.3, a eulogy to software engineering?

Source: [https://share.transistor.fm/s/0c8a4fc2](https://share.transistor.fm/s/0c8a4fc2)

Summary:
This podcast episode covers the release of React 19.3, new features like View Transition support and Fragment Refs, and ecosystem updates (Redux docs, Vite+ 1.0, React-Redux useSignalSelector). The hosts discuss trends in software engineering, the evolving role of frameworks, and the impact of AI on developer workflows. The episode also touches on open source sustainability, conferences, and notable community news.

Key takeaways:
- React 19.3 introduces new APIs and features; ecosystem tools (Redux, Vite+, React-Redux) see major updates.
- Discussion of broader industry trends: the changing nature of software engineering, frameworks, and AI’s role.
- Open source sustainability and developer motivation are recurring themes.
- Useful for staying current on both technical and cultural shifts in the React ecosystem.

Recommendation:
Summary sufficient (listen if you want in-depth discussion or context on recent React/JS news)

Why it matters:
listen if you want in-depth discussion or context on recent React/JS news

Content:
# This Month in React

Carl: Hello. Thank you everyone for joining us for the September edition of This Month in React, as we recap what's going on in the React, React Native, and across the whole web ecosystems. We're coming to you live here in Reactiflux, the place for professional developers using React.

Carl: I'm Carl. I'm a staff product developer and freelance community leader here at Reactiflux, where I do community programs like this event and the event I did yesterday, and build tools to help keep the community operating, and unfortunately, somewhat neglect those tools after several years of maintaining them, resulting in some, uh, we've had a couple of people get kicked by accident because of some changes that happened there, but we'll fix that.

Mark: Hi, I'm Mark. My day job is still at Replay, where we're still building really awesome time travel-powered dev tools and an automated QA layer on top of that that can find bugs automatically. and boy, am I still doing a lot of Redux stuff in my spare time. Woo!

Carl: Yeah, you've got a few new things to announce there. The, the big headline here is we've got a new, you know, React minor version, 19.3. people are continuing to eulogize software engineering as a field, so we're gonna keep talking about that. I feel like we've been touching on that more and more the last couple of episodes.

Carl: Let's start off with some new releases

Mark: so speaking of me being busy, um, the first item on the list is that the Redux family of libraries now has a single unified combined docs site. we'd al- always had multiple separate doc sites because we had multiple separate libraries, each with their own repository. The Redux core, which also had all the tutorials and the usage guides, Redux Toolkit, React Redux, and then Reselect.

Mark: and so each of them had their own markdown files. They each had their own Netlify site and, and build previews and everything. And people had filed complaints over the years saying that it's confusing that I have to jump from site to site to follow links or, or information. Uh, the sites all had the same look and feel, which was good, except you get confused which site you're looking at, some pages were duplicated across sites just in case.

Mark: I had said for years, "I can't do that," because the only way I can think of to do it at the technical level is to combine all of our repositories into a giant monorepo, and this will require massive amounts of Git history surgery and changing all the pipelines and the issue management.

Mark: And, like, I'm doing this in my spare time. I... There's no way I can put hundreds of hours into this effort. Well, last year, actually pre-AI, I had very briefly prototyped an alternate idea, which is what if I just cloned the other repos whenever you do a Redux core docs build, and then you got the files on disk, and then Docusaurus lets you combine multiple sets of content into one site.

Mark: And so I'd at least proved that it was possible in theory. And so, as I'll talk about later, I'm doing a whole bunch of Redux-related cleanup work at the moment. And over the last, like, just two to three weeks, I said, "What if I just point my agent at this and say, 'Do it for me?'" And we worked through all the complexities.

Mark: We got all the content up and running in one site, worked through a bunch of issues around PR previews and other things, and I, uh, officially shipped it while I was 34,000 feet over the Atlantic on Monday. and so there's now a single site, redux.js.org. It's got a dropdown to s- you select which set of library docs you're looking at, de-duplicated pages.

Mark: I also did a massive cleanup sweep to find every place we had out-of-date explanations and content, and so that's all up there.

Carl: you got another news to announce too

Mark: Yep. so for the last couple months I've been saying that I was working on a new React Redux hook. It is now in alpha. It's called useSignalSelector. It is a drop-in replacement for useSelector that uses proxies and signals inside to try to optimize updates. It should not be the default one that you choose.

Mark: It's meant for large apps with thousands of connected components. It does have a larger bundle size, but it speeds those up as well. So, it's pretty solid at this point, and I'd love people to do some real-world testing on it.

Carl: Oh, yeah.

Carl: We mentioned this last month, as an RC, but it's now out for real. Vite+ has a 1.0 release. They... This l- this is pretty neat. It looks like it's trying to offer, like, a general kind of one-stop. I guess it's a little funny. It's kind of an abstraction over, you know, what we would typically do for NPM scripts.

Carl: , instead of, like, npm run, npm create, npm install, it's got vite+, you know, vp create, vp install, vp dev. That's interesting. It's, it's trying to provide d- sane defaults for a lot of these really common behaviors using, you know, the current cutting edge of tools, Oxlint and Vitest and Vite 8 rolldown.

Carl: I see TS Down mentioned, for packing libraries. It has a monorepo awar- aware task runner with caching. So you know, it's, it's trying to do a lot. I would love it if one tool did all of this. That's really great. I hope it works as well as advertised.

Carl: Stuff like monorepos gets really complicated. I'm actually, m- currently in a project where I'm looking at options for monorep- repos across different languages. You know, I wanna, I want to not lock myself into only using TypeScript, so that's, you know, that's a whole different prospect. so yeah, I'm curious. I'll have to play with this. I'll have to see what it actually looks like in practice. But yeah, so, Vite+ has a 1.0 now.

Mark: It, it is interesting to compare it to earlier similar things. Create React app at least tried to provide pre-built configs for Webpack and Jest and Babel and everything else so you didn't have to do it. And then the Rome project was originally supposed to be linter, formatter, everything else, one AST parse, and everything is fully combined.

Mark: And then it flopped as a company, and we were left with just the standalone formatter that became Biome. So kudos to the Voidzero folk for managing to build the separate tools and then figure out how to get a layer on top of that, sort of flipping the process.

Carl: We've also got Vitest 5. you know, I, I don't know. It's a test harness. It's advertising a lot of performance improvements, which is great. It's always good when our tests run faster. Not seeing a ton of, you know, major changes that would get me excited about a new test runner, but, hey, new version.

Carl: L- V- Vitest is great, and now it's great-er.

Carl: , we talked about this a couple of months ago. Uh, Cloudflare produced a open source Next runtime, so you can self-host it more effectively. they

Mark: a slop, it's a slop fork

Carl: It's a slop fork for sure, but you know, hey, the, the, if we have functional tests, what's the problem? so yeah, it's a slop fork.

Carl: We talked about this in February. Uh, they are now announcing a 1.0 seven months later, so it was a slop fork, and hey, maybe it's now revised down into something a little bit less sloppy. And it's a 1.0, so that's great.

Mark: , so Lovable spins up tens of thousands of dev servers for all the different apps that they build, and even with Vite using Rolldown and Rust powered inside, they decided it wasn't fast enough for them. So they, they similarly have reimplemented some of the guts of Vite to make it even more Rustified in some way, and this has apparently been fast enough to handle the, the speed of all the dev servers they need to spin up

Carl: Nice. Cool. Yeah, I mean, certainly they're dealing with a lot, l- large volume of code right now. Improvements they make and the, friction they experience is gonna be pretty representative of the industry. Cool.

Carl: Again, something we talked about last month as an RC, Preact version 11 was released.

Carl: We talked about most of the benefits last time, so I'm not gonna, going to exhaustively, you know, re-discuss them. In reduced package size on disk, you know, install size of the whole module. they're talking about tree shaking, which, man, you know, everyone always talks about how it's all tree shakable now, and then I feel like the next version talks about how it's really tree shakable for real now.

Carl: So I just always take that with a hefty dose of salt. But hey, they're advertising it. It seems great. Tree shakable per feature, which is lovely. Yeah, lots of deeper in the weed stuff. They're saying hydration 2.0, hydrating while lazy chunks are loading makes zero DOM mutations. Cool. Love that. yeah, Preact version 11 seems great

Mark: Meanwhile, MSW, Mock Service Worker, just released version three. This looks like it has some pretty meaningful changes. They're going ESM only, like a lot of other libraries. More granular entry points, which sort of ties into the tree-shaking sides of things. Um, they now support, uh, GraphQL subscriptions built in, and there's a whole new API for defining network sources that's kind of like a, an, an improved version of the handler definition approach that it had.

Mark: and it also has lower level support for being able to directly intercepts all the way down to the socket layer, even with, even within Node. So I know Artem's put a lot of time and research into figuring out how to make network interception more effective, so this one feels like a pretty big release.

Carl: Yeah. Love that. MSW is, I haven't used it lately. The times that I've had to reach for it, it's been like an absolute essential part of achieving whatever task I was working on. Like, if you're doing integration tests, then like, ugh, MSW is so good. so yeah, exciting.

Mark: React Router put out version 8.4. They've done some internal re-architecture and changing their context structure to reduce re-renders. they've also got some optional more efficient route matching. So I guess if you've got apps with lots of routes and that's a possible performance bottleneck, then they've got an option that will try to make that faster

Carl: Cool. And, uh, Remix is advertising its, V3 release candidate. I don't know, where... At what point do we stop including Remix in here? 'Cause they're, like, very publicly not a React framework anymore, you know? We're leaning on it for its historic relevance at, this point, starting to.

Carl: yeah, they're saying since the beta, it's grown a lot. A complete database workflow with migration seeding, status checks, full stack hot module replacement, reload server modules, improved public asset serving. So, you know, it's, it's a, full web framework. They are moving away from React.

Carl: They are... I believe it's pretty heavily relied on at Shopify, which I think we're gonna talk about later too, is, uh, moving off React Native. So I, yeah, wow. I g- you know, hey, come to think of it, actually, Shopify generally seems to be exiting the React ecosystem if they're doing Remix and native apps.

Carl: Interesting

Mark: And I, I don't think we actually have the link in here, but I believe Shopify just bought Tailwind

Carl: Oh, did they? Curious. Oh yeah, on September 9th. I missed that. Okay. Remix is great. Technically, our website, one or more of our websites runs on it for Reactiplex, or has run on it. I've lost track at this point. But yeah. Definitely paying attention

Carl: Jotai has a v3 release.

Mark: So Jotai is an Atom-based state management library. I believe Recoil was the original library from Facebook that introduced that paradigm. Recoil died. Jotai was a smaller version from Daishi Kato. Version three is mostly clean up. I believe it, it also went ESM only, and changed a few exports and shuffled around some API locations.

Mark: So mostly clean up, but there, there's a definite trend of libraries going ESM only at this point.

Carl: Mm-hmm. Oh, yes. Yes, we've talked about that trend several times in the last couple of months. Love to see it. Finally. Ugh

Mark: I heard an earful about it at a React Alicante last week. That may be a separate discussion topic

Carl: Ooh, interesting. Okay, cool. An earful about ASMR

Mark: the, uh, let's just say that a couple people have very, very strong opinions about this.

Carl: Against or for?

Mark: Uh, mostly against

Carl: Fascinating. Okay. All right.

Carl: again, something we talked about is, uh... we referenced this earlier 'cause, uh, this is a Pointmanders project, and they released a, a charter a couple of months ago, listing this as a project they were gonna be pursuing. But they've, uh, announced something.

Carl: - Pointmanders Glyph is a typography engine for web graphics. So, like, we're doing text rendering in WebGL, and generally in, you know, graphics pipelines is actually pretty complicated because of the way, like, sub-pixel grouping and, like, kerning and... I don't know. Actually, typography is an- typography and typesetting is an absolutely insane depth of, you know, complication. The closer you look at it, the weirder it gets.

Carl: so writing a new one f- from scratch i- targeting a new environment is a huge undertaking, and they have announced one. Um, so that's pretty cool. I don't do very much WebGL stuff. But especially if you work on fancy landing pages, check this out 'cause it can make your text look better, probably.

Carl: , yeah, Pointmanders does tons of WebGL stuff if you're not familiar with the name. So yeah, definitely h- I personally have a lot of trust for them in, in this domain. Looks pretty cool.

Mark: I feel like I've been, we've been seeing an explosion of more React-alike or React knockoff or React variation libraries. We talked about one recently called Octane from Dominic Ganaway. That was essentially React, but it has to have a compiler, and it tries to clean up some of the rough edges, like hook dependencies.

Mark: Dominic had also put out the TSRX, like, improved JSX syntax layer as well. There's a, there's a new React-alike called Vdact, which is also React with a compiler, but rather than having, like, the fiber runtime underneath, it acts more like Svelte and just compiles straight down to DOM manipulation code.

Mark: Have not tried it, have not looked at it, but it has some examples on the front page of you write a React component with a useState hook, and it just gets directly compiled into, like, createElement div and DOM append calls immediately. So keep the friendly syntax, skip the runtime, and presumably things end up smaller.

Mark: also, several months ago we had mentioned that Tanner Linsley wrote a post called Projecting React where he said, "I really don't need all the concurrency features that the React team has spent years building, and they're kind of making server-side rendering slow. What if I slop fork React to just rip out all the stuff I don't care about?"

Mark: And so he said he had done it, and technically the source was available somewhere if you looked very carefully. The repo is now more actually available, and he's calling it Redact, so React with a letter D in the middle. It's still essentially like a you probably shouldn't use this, but it is there and the source is available, and it is on npm if people really want to use it.

Mark: we're seeing a lot of people looking at React and saying, "Well, if this is kind of the default way to write apps today, but we don't like some of the behaviors or the syntax, what are some alternate ways we could rework this to fit our needs?"

Carl: you know what? I, this was a late addition, but it's a new release.

Carl: Uh, we have a new website.

Carl: I threw it together. This is, you know, it's sloppy. I threw this to a new model just as, kind of to explore capabilities. I've been, I've literally been meaning to rebuild our website for years at this point, um, because I just, you know, jerry-rigged it into the existing infrastructure we had for Reactiflux, and that was not built for this. So it was not a good experience, and I knew that the entire time I've been doing this.

Carl: so now we have a better one. It's, it's significantly better. Typography is way better. behavior of, you know, you can... Now we have a sidebar with all the links instead of them just being at the top, and if you click on one of them, it will jump the play ahead to the right time so you can start listening as you read.

Carl: we've also got some link search, some topic search. It should just be... I, I have already used this website a few times for myself as I'm doing the documentation or, you know, prep notes, and like, "When did we talk about that?" hey, it's already useful for me. Uh, it's live. There's a couple things still broken.

Carl: Please don't sign up for the newsletter, 'cause it doesn't work. I haven't set up a publishing flow, and you will get test emails if you do. Sorry.

Carl: You know, I'm, I'm calling it slop because I used AI to make it, but it's better than that. You know, I put more effort than slop into it.

Carl: yeah. Anyway, reasonably proud of that.

Carl: we actually have a sponsor this month, I'm proud to announce. Yeah. If you have ever launched a full-stack React, Next.js, or Remix app on serverless hosting, you know the pain points. Cold start latency on that first request, and then out of nowhere, unpredictable bandwidth bill at the end of the month.

Carl: Cloudways Velocity gives you fully managed, persistent Node.js and full-stack hosting built specifically for developer speed. Because it's running on always warm infrastructure, cold starts are off the table. You get seamless Git push deployments, zero downtime rollouts, built-in Cloudflare enterprise CDN, and enterprise security, all managed right from an intuitive UI.

Carl: No configuring nginx, no SSH head-scratching, and most importantly, flat, predictable monthly pricing with no surprise bills. Stop overpaying for serverless spin-ups and stop wasting time on server administration. Go to cloudways.com/velocity, deploy your project in minutes, and experience how fast your apps should be running.

Carl: , start your free trial, and you can use promo code CWREACT for 25% off your first month, exclusive to React to Flux. Yeah. Give it a shot if you're deploying a Next.js or full-stack React app.

Carl: Okay, cool. Main content.

Carl: There's a new React minor version, 19.3

Mark: Nice. And this has a couple features that we have, as usual, talked about multiple times already, partly because they've been in Canary for a while.

Mark: the first is official view transition support. There's now a new view transition component that is built in. once again, like I don't work with front-end code myself.

Mark: I don't write view transition-y things. But this is a major new capability of the web platform as a whole, being able to do crossfades and a- other animations between parts of a page, separate pages, et cetera. It's built into the browser, but there's a bunch of nuance in how you set it up and how it works properly, and my understanding is, is that React's component is doing a lot of heavy lifting for you internally to be able to set all those up properly.

Mark: if you look at the 19.3 release notes, there are a lot of examples in here on how you use the new component, how you specify different kind of animations, and apparently it also even integrates with Suspense as well. So that's a pretty major new feature.

Mark: The other one is fragment refs, and this is another... This deals with a longstanding pain point in React where you could get refs to an individual DOM element. But let's say you have, like, a list component where there might not even be a parent, a single parent DOM node. It's just a flat list of children. There might not be anything to get a handle to.

Mark: So fragment refs allow you to attach a ref to a fragment element in your component, and React essentially pretends that there is a fake synthetic parent wrapper around all the children and gives you the methods that you can call to interact with them just as if there were a real DOM element there. They've had to put a lot of work into this, and this definitely solves a gap in React's interop abilities.

Mark: There's also a new feature called Browser. Anytime you're doing server-side rendling, rendering, you run into the problem of I have some code in a component, and the component gets rendered on both the client and the server, but this bit of code should only run on the browser.

Mark: And so frameworks like Next.js have had their various, like, dynamic import or SSR Only or whatever other flags are in there to try to limit what logic runs in what environment. So there's now a new function called Browser in React DOM, and you call it and you pass the result to the Use hook. So it's Use, parentheses, Browser, parentheses, and that throws, that triggers suspense, and at that point, React on the server says, "Oh, I shouldn't actually render this.

Mark: Leave the hole." And then when it gets to the client side, it runs again and says, "Ah, yes, this is client-side code. We will only actually run it there." So it's an official built-in solution, again, for something that people have needed to do for years

Carl: Yeah, I like that. I like that a lot better than the, was it use server that was the,

Mark: Use server and use client are bo-are both directives. This is a, a function that you import and call inside of a component

Carl: I've been, like, casually whining about the use of directives for that and how I don't like directives because the, the whole thing with the use strict when we invented directives was just the one, no more.

Mark: and then they proliferated

Carl: and, like, this seems great. If you can just say this needs the browser APIs, then okay, if it doesn't say that, then you have free reign to assume that it might not have access to them, so cool.

Carl: , that seems like a, you know, I love that. This seems like a big improvement to me

Mark: One thing that's not listed in the release notes, but I, I saw some discussion somewhere on the R- React to Flux side, and it, it ties into the Preact thing. Bundle size. I don't have the hard numbers in front of me, but I saw some comments saying that 19.3 had a very significant jump in bundle size.

Mark: And React DOM is already a very, very large library, and clearly the view transition support and fragment refs and, you know, whatever other bits they added add a s- it's just a significant amount of extra code. And that code is in React, and React itself is 100% untree shakable. It's all intertwined together.

Mark: So your bundle is going to be getting the view transitions code whether or not you ever use a view transition in your app, and it keeps growing. And, you know, view transitions look like a very useful feature, but is anybody over there actually considering bundle size as an objective? I suspect not

Carl: Sure. Do you know what the best site to check bundle size is anymore? It used to be Bundlephobia

Mark: bundlejs.org. the problem with Bundlephobia and a couple of the others the npm and npmx websites just tell you how big is this on disk in node modules. Uh, Bundlephobia tries to figure out how big it is, but it's kind of simplistic in how it looks at the entry points.

Mark: and right, and so, you know, like number one, if you, if you just look at React, React itself is the platform agnostic piece. It's React DOM that matters. And in React 19, they changed the entry point structure, so it's React DOM/client. So you have to specifically know that's what you're importing from, and then it's actually in like a third file inside of that.

Mark: Bundlejs.org lets you explicitly write some snippets of code. So if you wanted to do like export create route from React DOM/client, it literally downloads the files and bundles them and tells you how big it is bundle size is 222K, 70K gzip

Carl: There's also React Dev Tools, a new major version, version eight. I gotta say, this is, you know, surely this is just updating to match the latest

Mark: they have actually been doing a fair amount of work on it. I believe the existing profiler tab is now deprecated or removed, and instead they're, they now better integrate with the performance tab that's built in. on the other hand, there's now a suspense debugging tab that is part of the dev tools.

Mark: that's supposed to do actually some slightly time travel-ish things and show you like sort of a, a skeleton layout of the page and the suspense loading sections as they come in

Carl: Love that. Yeah, I mean, the profiler and the performance features were great, but, it was a duplication. We had our own performance tab in the Chrome dev tools already

Mark: I will point out that replay's time travel abilities in our MCP have some awesome React Performance Insights tools because I built them

Carl: . Yeah. I'm looking at - the past releases for the Dev- React Dev Tools too. It looks like they're doing a major r- release about every year. Thereabouts the past couple years. Although, yeah, the, cadence of follow-up releases has definitely dropped in the last three or so.

Carl: You know, I see version 5 and then 5.1, and then 5.2, 5.3, 6, 6.1, 6.2. But yeah, 7 just got a single patch release, and now we have 8. But hey, maybe that means it's settling down. It's stabilizing.

Mark: And then a couple adjacent tidbits that are related to React Core, but not from the React team themselves. ,

Mark: there was an article on how the... You can now build a React app with a whole lot of Rust-based tools start to finish. A lot of that actually involves the React compiler having been slop forked to Rust by the React team, and then the other bundlers said, "Actually, even in its Rust form, it's kind of hard to integrate, so what if we then further fork and customize the integrations with our own tools?"

Mark: And so, like the OXC people essentially h- now have their own variation of the React compiler that better integrates and runs faster. And so the article points out that you can use that and some Vite plugins and some other pieces to more efficiently build a React app start to finish.

Mark: and then we've actually had some very interesting discussion going on in our very own #react-internals channel, a channel that I watch like a hawk.

Mark: Last year I was really interested in the, this concurrent store API discussion that Jordan Eldridge from the Relay team was working on that was essentially supposed to be useSyncExternalStore, but Transition compatible. And then that whole effort stalled, for a whole variety of reasons.

Mark: And just within the last couple weeks, a couple of community members, Xander and Justin, have been actively working on their own improved polyfill implementations of what this might look like, uh, and making some pretty significant progress on both. It's a long way from community members saying, "We've built a seemingly working version of this," to it ever actually landing in React itself, but I'm very truly hopeful that something like this will actually land in React at some point, because this is the missing piece that libraries like React Redux need to actually be properly Transition compatible.

Mark: So I'm, I'm excited to see anybody putting effort into this right now

Carl: Yeah, I love it.

Carl: All right. Into the sad topics.

Mark: Into the sad topics

Carl: Dave Kiss put out a blog post titled A Eulogy for the Software Engineer. In loving memory of the software engineer, 1968 to 2026. a- I view this as slightly tongue-in-cheek. I think this is overstating it a fair bit. But yeah, you know, like, our profession is totally different here at the end of September as it was one year ago, you know?

Carl: When I think back to what I was doing September of last year, I was pretty aggressively using AI agents for the first time. But I was doing it very much from a perspective of you know, watching it like a hawk, reviewing its code. We're using it as a more of a collaborator. a thing we've said in the past is, automation versus mech suit.

Carl: You know, do you climb in and drive it, or is it let do its thing and check on the results of? And for me personally, it's definitely moved much more towards something I check the results of rather than reading all of its output. You know, d- having it, directly enable the code that I'm writing, per se.

Carl: We also have the state of devs, from, uh, Devographics to talk about, so we c- if we do, we can put that into some greater context a little bit later. Eulogizing software engineers, though

Mark: I mean, I, I wrote my own blog post, you know, on a, on a similar theme back in April, you know, detailing how I'd gone from the idea of hating AI to trying it, just over a year ago. It's actually been just over a year that I've been using AI to write code. And I, I am still very intentionally on, uh, if I understand the analogy right, the mech suit side.

Mark: I'm the one doing the driving and it's improving my abilities. That is a very, very intentional choice that I'm making to limit myself to my context-switching ability and what I can keep in my own head. I will say that even within the last few weeks, I've noticed that I'm willing to let, my chat sessions be a little more autonomous.

Mark: some of it's been the, "Hey, I need to go run errands for a couple hours. You have permission to actually, like, run a few more experiments and try some stuff out while I'm gone." And oh look, I'm, I'm getting work done while I'm running, running errands. It's great. but also I have more trust in the output.

Mark: one of the biggest reasons why I was scared to use AI at all was because I considered it completely untrustworthy. I saw too many hallucinations. It's nondeterministic. I did not believe that you could safely b

... (content truncated)
