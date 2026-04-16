---
type: twir-item
issue: 268
item: 8
item_type: item
date: 2026-02-11
source: https://www.reactiflux.com/transcripts/tmir-2026-01
tags:
  - "CVEs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-02-11-TWIR-268|Index]]

# Item 8: This Week in React - Oops more CVEs. AI has React "skills", Astro exits and Tailwind struggles

Source: [https://www.reactiflux.com/transcripts/tmir-2026-01](https://www.reactiflux.com/transcripts/tmir-2026-01)

Summary:
This transcript summarizes recent updates in the React ecosystem, including security advisories (CVEs) for React, Next.js, and React Router, as well as documentation updates and new features in React (e.g., useStore, ViewTransition, Fragment Refs). It also covers ecosystem news such as the acquisition of Astro by CloudFlare, Tailwind's revenue decline, and the introduction of AI "skills" for React. The transcript highlights ongoing work on RSC data fetching patterns, security improvements across the stack, and notable community projects.

Key takeaways:
- Critical security updates: React, Next.js, and React Router have new CVEs—update to the latest patched versions.
- React docs updated for useOptimistic and useEffectEvent; ongoing discussion about documentation quality.
- New features in React: ViewTransition API, Fragment Refs, and useStore for concurrent state.
- Ecosystem changes: Astro acquired by CloudFlare, Tailwind facing financial challenges, and AI integrations (Claude Skills) entering the React space.

Recommendation:
Summary sufficient (read the full transcript for in-depth context or if you need details on specific updates or security issues)

Why it matters:
read the full transcript for in-depth context or if you need details on specific updates or security issues

Content:
# TMiR 2026-01: Oops more CVEs. AI has React "skills", Astro exits and Tailwind struggles

- `[00:58]` New releases
- `[12:29]` Main Content
  - `[12:34]` React Core
  - `[21:34]` Other security issues
  - `[28:28]` Claude Skills in the React world
  - `[43:49]` RSC roundup
  - `[46:01]` Ecosystem economics
- `[52:56]` ⚡ Lightning round ⚡
- `[01:03:33]` Conferences ([React](https://react.dev/community/conferences), [Javascript](https://confs.tech/javascript))
  - [CityJS New Delhi](https://india.cityjsconf.org/), 18-19 Feb, New Delhi, India
  - [State of the Browser](https://2026.stateofthebrowser.com/) Feb 28, London, UK
  - [AppDevCon](https://appdevcon.nl/) Mar 10-13, Amsterdam Netherlands
  - [Programmable](https://www.programmable.tech/) Mar 17 / Mar 19, Melbourn / Sydney, Australia
  - [Frontrunners](https://frontrunners.tech/) Mar 27, Washington DC, USA
  - [T3chfest](https://t3chfest.es/2026/en/) Mar 12-13, Madrid, Spain
  - [React Paris](https://react.paris/) Mar 26-27 Paris, France
  - [CFP (closed)](https://docs.google.com/forms/d/e/1FAIpQLSfLICWs7vpK5fuMkZyJk4GyDtZBs08NMKJ0eIOOZBUxo98beQ/viewform), [Also a community survey](https://docs.google.com/forms/d/e/1FAIpQLSd0pjOsMo0z3fvhv9EhgvUBWA4CdIcsivOCQi8wBmiNc_yXPQ/viewform)
  - [React Native Connection](https://reactnativeconnection.io/) Mar 30-31, Paris, France
  - [CityJS London](https://london.cityjsconf.org/), Apr 15-17, London, UK
  - [jsday](https://www.jsday.it/) Apr 9-10, Bologna, Italy
  - [SmashingConf Amsterdam](https://smashingconf.com/amsterdam-2026) Apr 13-16, Amsterdam, Netherlands
  - [React Miami](https://www.reactmiami.com/) Apr 22-25
- `[01:04:56]` Outro

**Carl:** Hello everyone. Thank you for joining us for the first this month in React of 2026 January edition. As we recap what's going on in React, react Native and across the web, we're coming to you live from Reactiflux, the place for professional developers using React. [00:00:00]

And yeah, I'm Carl. I'm a staff product developer and freelance community leader here in Reactiflux where I do programs like these events uh, and a couple of other things. [00:00:16]

**Mark:** Hi, I'm Mark. My day job is working at Replay. My second unpaid job is working on Redux and I'm not wearing glasses. [00:00:25]

**Carl:** Yeah. Congrats on LASIK! [00:00:33]

**Mo:** And I'm Mo I'm the head of Mobile at Thero. I'm an active part of the React Native community, and I organize the React Native London Meetup and Conference. [00:00:35]

**Carl:** and like 10 minutes fresh off, traveling back home. Right? [00:00:43]

**Mo:** yeah. Just got home. Just got home. I'm still still wearing my coat. [00:00:48]

**Mark:** Make yourself comfortable. [00:00:52]

**Mo:** We're gonna be here. [00:00:54]

**Carl:** Cool. Okay. Uh, Let's get straight into some new releases. [00:00:55]

## New releases

**Carl:** Yeah, Mark, take us through those. [00:00:58]

## [Next 16.1](https://nextjs.org/blog/next-16-1) (Turbopack updates, bundle analyzer)

**Mark:** Okay. Item one we have next. 16.1 just came out not a lot. Huge. There, there's some improvements to Turbo pack. They have a new bundle analyzer feature built in. I'm always in favor of, you know, actually understanding what's going into your system. [00:00:59]

**Mark:** Looks like some of the Turbo Pack file caching stuff ought to make the dev mode a little bit faster. [00:01:15]

Hopefully I don't think we put the link in here, but the next folks did put out an article sometime in the last couple weeks talking about a lot of the internal memo work they do in Turbo Pack. That is, you know, the core of how it's supposed to make builds faster. So that's probably worth looking at as well. [00:01:21]

**Mo:** React navigation version 8.0 is an alpha now. So we've seen a little bit of this stuff come around, but things like native bottom tabs being sort of the default, which a lot of the other libraries in the ecosystem are moving towards and expert route has been pushing for a while, which uses react navigation under the hood. [00:01:38]

Some better TypeScript configs and just some general improvements. With the major changes, those native bottom tabs, which won't make the apps feel just that much more native. [00:01:55]

**Mo:** And then the next one is React Native Windows, version 0.81. Is out. And the same is actually the case with React Native Mac Os because they're both maintained by Microsoft. [00:02:03]

big thing here is that the sort of new architecture or the fabric architecture is now enabled by default. So the Windows and Mac os the desktop equivalents of Rack Native are a little bit behind because of some legacy that's in the code base and some stuff that needs to be refactored in a little bit of tech debt. [00:02:14]

But they're definitely catching up. So, they're getting close to fully adopting the new architecture, which is exciting. [00:02:32]

**Mark:** I would love to know what the adoption numbers are for either the, the macro windows ports outside of Microsoft. Early outta curiosity, [00:02:37]

**Mo:** It's not as well publicized or showcased, but I have a great talk, which I'm gonna use this opportunity to plug by one of the maintainers. [00:02:46]

**Mo:** so this was at the conference that we hosted at Arn Lko and one of the maintainers, one of the maintainers of React Native macOS did a joint talk with Jay Meistrich, who maintains Legend List. And they talked about react Native macOS in the state of React Native Macs. It's a very cool talk to get an idea of what's in store. So, [00:02:55]

**Carl:** great. Love that. [00:03:13]

**Mark:** All right. Next item. Josh Goldberg is a wonderful one. Wonderful human being if you ever had a chance to talk to him. He's also a major proficient linting tool maintainer. He's been the primary maintainer of TSES lint. He's worked on a number of other linting projects. He's had a lot of interactions with the ES lint maintainers and the TypeScript maintainers. [00:03:15]

And as a result, he has formed very many strong opinions about how winters should work and what's wrong with current winters. And, you know, like most people, he's, you know, griped about things he doesn't like for a while. And this has finally result in Josh building his own winter. So he's calling it Flint. [00:03:39]

he'd written several previous blog posts talking about. You know, what would a better winter look like? And that was the, you know, the hidden background on I am actually building my own winter. So if you look at the Flint announcement it goes through some of the points that he's trying to make. [00:03:58]

Things like it's, there's a hybrid architecture where it can use native built linting tools, but most of the coordination is still being done in TypeScript. It, it would still have TypeScript based plugins. Most of the rules would be in the core, much more consistent naming and error messages and configuration. [00:04:17]

So. I don't know the full status of it. I know he's been working on it and that, like an early proof of concept exists. I don't think it's anywhere near a usable state at all. But Josh knows linting and he's very good at this stuff. So, we've got oxalate and es lint and excellent and bio at this point. [00:04:35]

You know, maybe we don't need another, but I love that Josh has the enthusiasm to try to put his ideas into practice here. [00:04:56]

**Carl:** Yeah, if you're gonna complain about something, putting your money where your mouth is on investing the energy to try and execute on those gripes is something that I would love to see everybody try and do. [00:05:03]

## [Immer 11.1](https://github.com/immerjs/immer/releases/tag/v11.1.0) (array methods override)

**Mark:** A personal item and one that I've been, you know, waiting to see come together for a while. So those of you who have been paying attention to the podcast over the last few months have heard me talk about the performance optimization work I did on Emer in September and October. [00:05:15]

And so that had ended up with three different prs that I'd filed. A small set of tweaks that it went out as Imer 10.2 a major internal rewrite that went out as Imer 11.0. And then the other piece I'd put up is a new optional plugin that overrides ier array methods so that instead of accidentally proxying every field you access as you loop over an array, it just defers to the underlying array and skips most of the overhead in that, a couple K to the bundle size if you actually import and turn on the plugin. But it does make pretty much any array access noticeably faster. And you know, the goal of this was to make ER faster. So I did that. So that came out as ER 11.1 and that is all the performance changes I had except for one other spot where I was investigating the possibility of trying to improve the object spread handling in some way. [00:05:30]

I may try to get back to look at that at some point, but this is all I'd put up. So very happy to see all that's come out. [00:06:31]

**Mark:** Couple other items. [00:06:37]

Back to the theme of tools being built in rust. Rolldown has hit 1.0 rc I believe this is already available for use in the latest V eight betas. I don't have a release timeline on that, but it looks like that one's coming together pretty well. [00:06:38]

**Mark:** And then yarn has announced yarn version six, which yes, is a rewrite it and rust announcement. I don't think I missed a yarn five. I would've to go back and reread the post to see if they actually mention it, but I'm pretty sure the current version is still four x. So it's a rewrite and rest rewrite. The goal is to make it faster. I think the blog post has some benchmarks that compare it to PNPM in a few different modes but happening there. [00:06:54]

**Carl:** Yeah, that's interesting. I just pulled up the Yarn docs and can confirm. The most recent version is listed as 4.1, so it's curious that they're announcing version six. [00:07:26]

**Mark:** Maybe it's the winamp approach somehow. [00:07:35]

**Carl:** taking inspiration from ECMAScript, you know, skip version four. [00:07:38]

Strange. [00:07:41]

**Mo:** I got an interesting thing that I was just looking at not yarn but roll down. And so it's obviously made by the creators of vt, but I was just going on the Void Zero website and I saw that they seem to be trying to launch a paid unified tool chain called VT Plus. I don't know if you folks have seen this, [00:07:42]

**Mark:** they talked about that at vConf a couple months ago. The idea is that. Void Zero is sponsoring slash owning a lot of the work on the underlying tools OXC, oxalate OX format, EV and all that stuff. And the purpose of ROLLDOWN is that right now v relies on ES build for dev mode and roll up for prod builds. [00:07:59]

And Es builds fast roll ups, not, and you've got two different tool chains. So roll down is an attempt to unify both, of those. One consistent build system, roll up public API do it a lot faster and you know, they own it. V plus then is supposed to be what if we took all our tooling together and made kind of like what Rome slash Biome was supposed to be a few years ago, the Uber Unified everything tool chain. [00:08:25]

And then that would be their enterprise sales kind of a thing. [00:08:56]

**Carl:** In other news. So WebKit has shipped an initial version, an attempt at CSS grid masonry layouts. This has been like a hot a subject of hot debate for years. Like it's been this, like simmering. We want something that does this, but exactly what the semantics or should be, are unclear. Basically, grids are great, but they require, they, they place constraints in two dimensions. [00:08:59]

it's a grid, it's a bunch of squares or a bunch of rectangles or whatever. And there's lots of layouts where each item in them may be a variable size, like for instance a grid of photos. You know, you look at your photos in whatever app you like to use. And it, there are different aspect ratios, there are different dimensions. [00:09:27]

And that's where Masonry comes in. It's called masonry because it resembles like the layout of bricks or stones. So, cool that I've literally been hearing about that for at least four years, I'd say. I think, I feel like as soon as CSS grid came out, people were like, great. What about masonry? So it's cool that we've now got something functional shipped in Safari. [00:09:44]

It looks like it's in the technology preview, so it's not fully usable now, but meaningful progress. [00:10:06]

**Mark:** think a lot of the debate there was should this become like another named CSS display mode or is this another set of options for grid or something else? What's the naming, how does it play with the existing layouts? And so there, there was a lot of discussion iteration to try to figure out what the right approach was there. [00:10:13]

**Carl:** And it sounds like they have, or at least close enough to where there's something has been shipped, which is great. Cool. [00:10:33]

**Carl:** Other, not quite released, but major progress .Temporal has been released in Chrome, I believe in the main release branch Chrome 1 [00:10:39]

**Mark:** I think this, this is actually out. [00:10:49]

**Carl:** yeah. [00:10:51]

Which is being actually out is a clears a roadblock to being officially standardized. Anything that is stage four must be present. I believe in a like fully released browser version, it must be used not in alpha or release candidate. And that's great. JavaScript dates suck to work with. [00:10:52]

There are a bunch of pretty major gotchas. My favorite is that there is no way to encode the time zone in a date. It always relies on the system time zone for whatever computer is executing that code which is a pain in the butt. And actually it, it has a b that cause of the bug in Reactiflux.com because the way we calculate what date a transcript is from diff is different if you build it locally versus on. [00:11:11]

In production because of the five hour time difference. So I, I ha this is something I have to account for when I release these transcripts because JavaScript is dumb about dates. So, great. Love to see that. There was another great summary from Matt Marques Wilto, which, oh I recognize that name. [00:11:38]

I've followed him on social media for 12 years now, something like that. Just, he did a great blog post about temporal Date is out, temporal is in definitely recommend it as a good technology summary of this tool. [00:11:57]

**Mark:** And interesting implementation. I, I only saw this in passing, but I think the actual core of the temporal implementation that Chromium is using is indeed in rust and then exposed up through the JS engine. [00:12:11]

**Carl:** fascinating. Cool. [00:12:24]

**Mark:** I'd have to go back and double check details, but I think I saw it somewhere. [00:12:25]

**Carl:** Okay. Neat. [00:12:28]

## Main Content

**Carl:** That's all the new releases we got for you. Let's go into main content [00:12:29]

**Mark:** Okay. [00:12:33]

## React Core

**Mark:** A number of items from around the React core area. [00:12:34]

**Mark:** Item number one, update your reacts again. So we, we had the multiple sets of CVEs and security issues with server components. Was that only last month, two months ago when, whenever that was. the initial remote code execution follow on reports found some denial of service and source code exposure, vulnerabilities, and apparently further investigation has found other ways to trigger denial of service and issues. [00:12:37]

And so I, I was actually confused if this was. The same CVE or something different. It looks like there is actually a separate 2026 CVE entry for the new denial of service entries, but it's probably the same basic idea. So there are new versions of React Out. Again, please update to 19.0 0.5, 19.1 0.5, or 19.2 0.4 I think approximately. [00:13:05]

Just update everything. Again, [00:13:35]

**Carl:** Yep. Geez, not ideal. [00:13:38]

## [Next.js DoS CVes](https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472) for Image Optimizer and Partial Pre-Rendering

**Mark:** these for their own internal pieces image optimizer and partial pre rendering. So again, please update your next JS to the latest as well. [00:13:40]

**Mark:** hopefully slightly happier news. Ricky Hanlon just put up some docs updates. I don't think they're even merged yet. To rewrite the API reference pages for use Optimistic and Use Effect event and tracing this a bit. I think the, there were a couple triggers for him trying to make those changes. [00:13:50]

**Mark:** And in the discussion on Blue Sky, Dan actually popped in and said, I'm really not happy with the use Optimistic Docs, or, you know, a few of the other docs pages, I feel like. You know, the team kind of missed the boat on some of the docs work after I, you know, after I set the bar pretty high with a lot of the initial tutorials and references and stuff. [00:14:32]

And Ricky very right, rightfully pointed out, it's like, yeah, there's only so many people doing things. I'm one of 'em, I've been on family leave. And also, you know, we had this giant CVE drop that we've had to, you know, go deal with so very fair point. But I think Ricky took that as inspiration to go try to do a rewrite. [00:14:55]

So he's got a rewrite up for both Use Optimistic and Use Effect Event. One interesting thing I noticed this morning, I, I believe the use optimistic update was probably done by hand. The React team has added some Claude code agent files to both repos and I think Ricky did some of that and added in some skills and commands for both improving docs and looking at things like the React compiler internals and stuff. [00:15:16]

And I believe the effect event Doc PR said the first pass on this was done by Claude, and then I went up and tried to clean it up myself. So number one, hopefully better docs wonderful all around. Two, the React team is experimenting with Claude code and seeing what they can do with that. So, you know, just interesting to watch that progress along. [00:15:46]

**Carl:** Yeah. That's interesting. I was, I've been curious, you know, I've never worked at big companies. I generally understand them to be pretty touchy about stuff like uploading code to third party servers. [00:16:10]

So I've been curious what kind of access to tools like Claude you know, teams like React Core would have so interesting to see that they're visibly starting to experiment with it in the actual React code base. [00:16:21]

**Mo:** It's quite interesting that like they're kind of allowed to almost come and say it publicly, given that Meta has been a big advocate of their own sort of open source models. Like, so, you know, it's almost like, hey, we use the direct competitors tools and it's, you know, it's fine. You know, so I think that's quite interesting. [00:16:35]

**Mo:** We actually had some people from the React Native Core team where we talked about this at the conference. So I'm gonna do another, I'm gonna be doing a lot of self [00:16:57]

**Mark:** Please plug your stuff. [00:17:02]

**Mo:** yes. It's not really my stuff. I mean, I was I was moderating the panel, but I, if you want to get a little bit of insight into what the React Native Core team does with ai, this might be an interesting panel for you to watch. [00:17:05]

We have a really good chat. [00:17:15]

**Mark:** Cool. [00:17:16]

**Mark:** Meanwhile, in the midst of all the CVEs and everything else the React team is continuing to work on actual core functionality. We had the view transitions, alpha APIs came out last year, and Sebastian Markbåge has continued working on that and is expanding the view transition support with relation to gestures and some other animation things as well. [00:17:17]

I have not looked at these, I don't know details, but I know that lack of animation support has always been a complaint about React as opposed to libraries like view and spelt. And so it seems like the work that they've done on Fiber in the past and now the baseline that they've put in place for view transitions is something that they're building on and trying to actually expand that functionality as well. [00:17:39]

they're also continuing to make some tweaks to fragment refs. I actually legitimately do not remember, are fragment refs out in 19.2 or were they alpha in 19.2? [00:18:03]

Anyway I, I saw, I saw a few additional prs come through with some improvements to fragment, ref handling dealing with text nodes and a few other things and [00:18:15]

**Carl:** Can confirm, fragment refs are canary only right now. [00:18:24]

**Mark:** okay. Okay. So still work in progress. [00:18:27]

## [<ViewTransition> underlying tech](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/types) is now supported in all major browsers as of Firefox 147. React features is still in Canary.

**Mark:** And related to the view transitions aspect like a lot of other things, they came out in Chrome first and, you know, therefore all the different chromium based browsers Firefox has finally shipped view transitions as of Firefox 1 47, I have no idea about Safari. [00:18:30]

I don't use safari. I don't look at safari. I don't know [00:18:46]

**Carl:** small, small clarification actually. So, Firefox has supported view transitions themselves since 1 44, but there's a sub thing, view transition types, that they have not supported until now in Firefox 1 47. I don't fully understand what the difference is, but I guess it's like, you know, the types property on view transition is now supported and I guess the react view transition component depends on that. [00:18:48]

**Mark:** Gotcha. [00:19:17]

**Carl:** Yes, the view transition component, which is still in canary. [00:19:18]

**Mark:** Mm-hmm. All right. [00:19:21]

**Mark:** And finally, two other prs to note. I've talked in previous episodes about the concurrent store's work that Jordan Eldridge has been working on. He had put up the React Concurrent Store, poly Fill. I had tried it out in React Redux. I had submitted some prs to improve the poly fill and offer some feedback on things that we probably need to cover when we actually go to implement it. [00:19:22]

And Jordan actually put up the PR to actually implement the initial concurrent store, API in React itself. Remember, this is supposed to be a better replacement for the current used sync external store, API, but concurrent transition compatible. [00:19:44]

Honestly, there's been surprisingly little discussion on this PR at all. Like, I think there's like one or two comments. One person just asking like, how is this different from the use hook or something like that. I expected more people to jump on this and say, what is this? What does it do? What are the trade-offs? How soon can we land this? And there's been no chatter. [00:20:03]

But I mean, he also put it up like, I don't know, right at the end of December, early January. So not much. But again it's very exciting to see this being worked on at all. It's very exciting to see. We're at the point where he feels confident enough in the API design to put up a PR and say, here's what I think we're trying to do and an implementation that does that. Now let's discuss it and get further public feedback. So very, very excited by this. [00:20:25]

**Mark:** And last item there was a types PR put up and I think possibly actually merged to improve the react types around form events. Trying to get better typing for the target field, I believe. [00:20:54]

**Carl:** It did get merged. Can I confirm? [00:21:07]

**Mark:** cool. [00:21:10]

**Carl:** So it looks like the form event had previously been matched on types to the React synthetic event. But it was not identical to the actual DOM event. And so this types change corrects that. So the the types are now matching what is in the dom it looks like. Cool. Looks great. [00:21:11]

**Mark:** Yep. And that's it from the roundup around the world of the core. [00:21:28]

**Carl:** Heck yeah. Cool. [00:21:32]

## Other security issues

**Carl:** Let's go back into some more security issues around the ecosystem. [00:21:34]

**Carl:** Yeah. I guess we briefly touched on some. You know, CVEs and other, you know, denial of service vulnerabilities. In next react Router has also put up a thread discussing six CVEs. It says they publish six CVEs identifying vulnerabilities between React router and remix B two. [00:21:39]

They're saying safe versions are react router seven point 12 version six is 6.3, 30.3 and remix V two is two point 17.2. these are pretty weedsy kind of vulnerabilities. I was looking at the list and didn't see any that immediately jumped out as like, oh shit, that's gonna be a problem for me. [00:22:00]

But it's like a couple of cross site scripting vulnerabilities. Let's see. Yeah, one in the meta component when it's generating script IDs. Okay, but that says framework mode only. Yeah. So it's a lot of these are in framework or data mode only if you're using that, I think that's the recommended, more more common. [00:22:21]

Yeah. Yeah, so it's like in the meta component, it's got unauthorized file access for some session storage. If your cookies aren't signed, an unexpected external redirect via untrusted path, I don't quite know what that's supposed to imply. All of these just link to the actual, like GitHub security advisories rather than any kind of blog post or anything. [00:22:41]

I'm not seeing like discussion of or explanation in depth of what these vulnerabilities are on a technical level. Just kind of here's what it was and here's what's safe. So that's great. I guess. [00:23:05]

**Carl:** node likewise also had a, couple of security patches also pretty deep in the weeds. Several of these I believe, were uncovered as a result of investigations started after the React CVEs last month. [00:23:18]

Yeah, you know, it's like you can update the timestamp of files if, even if you don't have right permissions. So that's, you know, technically a permissions bypass memory leak that enables a remote denial of service. Uncatchable maximum call stack exceeded error that can cause process crashes even if you think you're handling all possible errors because you can't catch it. [00:23:31]

So it's a couple of little things like that. Mostly it looks like some file system errors and server crashes in general. One, one that's like super deep in the weeds. It says timeout based race conditions make unsigned into eight array buffer slash buffer allocation non-zero filled. So like if you go to allocate a type array buffer, I guess in certain circumstances, you know, that could be exploited so that what you think is a zeroed out, a ray buffer is not actually zeroed out, which you know, sure. [00:23:55]

That's the kind of thing that absolutely security researchers can tap into and get it turning into some other vulnerability, I guess. I don't see a path towards it, but Sure. [00:24:27]

**Carl:** Here's a name I haven't thought of in a minute. Lodash they rolled out a major security overhaul as this blog post titles it. [00:24:38]

**Carl:** An interesting detail that I, I noticed while reading the blog post, it was actually funded by a sovereign tech agency is what it's called. And it says that they're, we invest globally in the open software components that underpin Germany and Europe's competitiveness and ability to, to innovate. [00:24:46]

So this is the like government sponsored open source grant that was used to fund security work at Lodash to the tune of $200,000. So that's interesting. I, that's. Some fun details. I, I guess, you know, as we were talking about financial ecosystem for open source, look at that, here's a major foundational open source project getting like government investment money from the government in order to make it more secure. That's pretty cool. I appreciate that. that better than, you know, venture capital exits or whatever. Yeah. [00:25:01]

**Carl:** Moving on a bit. GitHub put out a blog post towards the end of last month. I think we missed it because we recorded early in December to avoid the holidays. But they put out a blog post about strengthening supply chain security, just across GitHub and NPM. [00:25:35]

It's a lot of retrospective on the Shai-Halud attacks that we discussed in pretty deep detail over the last two or three months. Looks like they're, it says, what's next for NPM, bulk OIDC onboarding. So I guess, you know, OIDC is a authentication standard for sharing authentication information, previously they didn't have great support for that. Now they have much better support for it, but people have to transition. So this [00:25:50]

**Mark:** the biggest issue is I've now done this for a couple packages and you have to go in directly into the NPM settings for that package. Manually click through. I want to turn on trusted publishing for this package. Here's the repo name, the, YML file that will publish this and confirm the settings. [00:26:16]

Now, what happens if you have hundreds of packages? I think people even went ahead and started creating user scripts in the browser to try to automate clicking through that. [00:26:35]

**Carl:** Oh man. writing an automated user script to [00:26:44]

**Mark:** automate [00:26:48]

**Carl:** changes, what could go wrong. Yeah, so they also expanded to support more OIDC providers, so it's not just GitHub and GitLab as well as staged publishing. So it's a new publication model that gives maintainers a review period before packages go live with multifactor authentication, verified approval. [00:26:49]

So, cool. Like this is a bunch of like [00:27:09]

**Mark:** Boring, but critical stuff. [00:27:12]

**Carl:** Right. Boring but critical stuff around. Ensuring that who is publishing code to a specific package is who is supposed to, and pr

... (content truncated)

Related notes: [[Server Components]]
