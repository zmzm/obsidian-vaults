---
type: twir-item
issue: 257
item: 11
item_type: item
date: 2025-11-05
source: https://share.transistor.fm/s/ad1a1c53
tags:
  - "directives"
  - "2025-10"
  - "192"
  - "architecture"
  - "Nextjs"
  - "PPR"
status: auto
quality: keep
---

[[2025-11-05-TWIR-257|Index]]

# Item 11: This Month in React 2025-10: Post-conf; React 19.2, React Foundation, React Native removing old architecture. Next.js has too many directives

Source: [https://share.transistor.fm/s/ad1a1c53](https://share.transistor.fm/s/ad1a1c53)

Summary:
This podcast episode recaps major React ecosystem news for October 2025, including React Conf highlights, the launch of the React Foundation, React 19.2 features, and debates around Next.js 16’s directive-heavy approach. It also covers new releases, performance talks, cross-framework trends, and community events. The episode is hosted by prominent community figures and provides a broad, opinionated overview of current developments.

Key takeaways:
- React Foundation announced, signaling new governance and direction for React.
- React 19.2 introduces features like Activity and useEffectEvent.
- Next.js 16’s proliferation of directives sparks debate about complexity and platform boundaries.
- Covers major releases, performance research, and community events.

Recommendation:
Summary sufficient (listen for in-depth discussion or community perspectives)

Why it matters:
listen for in-depth discussion or community perspectives

Content:
# This Month in React

This Month in React - October 2025 (SM)
  
===

[[00:00:00](#t=0h0m0s "Jump to 00:00:00 in this episode")] Intro
  
---

[[00:00:00](#t=0h0m0s "Jump to 00:00:00 in this episode")] Carl: Hello everyone. Thank you for joining us for the October edition of This Month in React. As we recap what's going on with React, React native in the web, we're coming to you live from React Flux, the place for professional developers using React.

[[00:00:12](#t=0h0m12s "Jump to 00:00:12 in this episode")] I'm Carl. I'm a staff staff product developer and freelance community leader here at React Flux, where I run community programs like these events and build tools to help keep the community operating.

[[00:00:23](#t=0h0m23s "Jump to 00:00:23 in this episode")] Mark: Hi, I'm Mark. My day job is at Replay.io and in my copious amounts of spare time, I maintain Redux and rewrite Immer.

[[00:00:30](#t=0h0m30s "Jump to 00:00:30 in this episode")] Mo: I am Mo, I head the mobile team at Theo. I'm an active part of the React native ecosystem and community, and I organize the React Native London Meetups and conference, which is coming up in two weeks.

[[00:00:42](#t=0h0m42s "Jump to 00:00:42 in this episode")] Terrifyingly so.

[[00:00:43](#t=0h0m43s "Jump to 00:00:43 in this episode")] Carl: Coming right up. Yeah. And you got a shout out that we're gonna talk about.

[[00:00:46](#t=0h0m46s "Jump to 00:00:46 in this episode")] New releases
  
---

[[00:00:46](#t=0h0m46s "Jump to 00:00:46 in this episode")] Carl: Let's start with some new releases. Mark, tell us about Immer.

[[00:00:49](#t=0h0m49s "Jump to 00:00:49 in this episode")] [Immer 10.2](https://github.com/immerjs/immer/releases/tag/v10.2.0)
  
---

[[00:00:49](#t=0h0m49s "Jump to 00:00:49 in this episode")] Mark: Okay, I can, I can do both these things. So I actually take very full credit for this one. So to be clear, I do not maintain the Immer immutable update library that is Michelle West Rate, who created it and has maintained it all the easier years.

[[00:01:01](#t=0h1m1s "Jump to 00:01:01 in this episode")] However, since the start of September, I have sunk a stupid amount of time, something like 120 plus hours into trying to rewrite the internals of Immer for faster performance after some re users filed complaints to the Redux repos, that it was kind of slow. So I filed a few different prs, one to make some relatively small tweaks, and then a couple larger architectural changes.

[[00:01:26](#t=0h1m26s "Jump to 00:01:26 in this episode")] And Michelle just merged and released Immer 10.2 with the small options. And we are hoping to land the larger architectural changes in the near future. And those will probably come out as Immer version 11, hopefully in the next few weeks or something. So I'm excited faster for performance free upgrades.

[[00:01:45](#t=0h1m45s "Jump to 00:01:45 in this episode")] Yeah, should be.

[[00:01:46](#t=0h1m46s "Jump to 00:01:46 in this episode")] Carl: Yeah, love some big core performance improvements of deep packages. That's awesome.

[[00:01:51](#t=0h1m51s "Jump to 00:01:51 in this episode")] Mark: And I will also hopefully turn this into a conference talk. Nice.

[[00:01:55](#t=0h1m55s "Jump to 00:01:55 in this episode")] [ArkType ArkRegex](https://arktype.io/docs/blog/arkregex) (typed regex)
  
---

[[00:01:55](#t=0h1m55s "Jump to 00:01:55 in this episode")] Mark: Along with that, I, I just saw the announcement, I think like yesterday, that the author of the ARC type validation Library, which is a, a competitor to Zod that takes a, a rather different API approach, just released a, a similar tool called ARC RegX.

[[00:02:12](#t=0h2m12s "Jump to 00:02:12 in this episode")] It's a function that is supposed to be a replacement for defining regular expressions in JavaScript, but it actually parses the RegX string into TypeScript types so that it can both. Interpret at the type level, what the regular expression is doing, and also even provide syntax errors if the reg itself is invalid.

[[00:02:38](#t=0h2m38s "Jump to 00:02:38 in this episode")] Just looking at the docs, my mind is blown.

[[00:02:41](#t=0h2m41s "Jump to 00:02:41 in this episode")] Main Content
  
---

[[00:02:41](#t=0h2m41s "Jump to 00:02:41 in this episode")] Carl: Well, yeah, other than new releases, we have a bunch of main content this month.

[[00:02:45](#t=0h2m45s "Jump to 00:02:45 in this episode")] React Conf
  
---

[[00:02:45](#t=0h2m45s "Jump to 00:02:45 in this episode")] Carl: The React conf happened, what, three weeks ago, and a bunch of new stuff came out of there.

[[00:02:50](#t=0h2m50s "Jump to 00:02:50 in this episode")] [Official ReactConf 2025 Recap](https://react.dev/blog/2025/10/16/react-conf-2025-recap)
  
---

[[00:02:50](#t=0h2m50s "Jump to 00:02:50 in this episode")] Carl: They did put up an official recap blog post from it on the 16th, about a week after the event happened.

[[00:02:57](#t=0h2m57s "Jump to 00:02:57 in this episode")] [Introducing the React Foundation](https://react.dev/blog/2025/10/07/introducing-the-react-foundation) (also from [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-intent-to-launch-the-react-foundation), [Meta engineering](https://engineering.fb.com/2025/10/07/open-source/introducing-the-react-foundation-the-new-home-for-react-react-native/), and [Seth Webster](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework/))
  
---

[[00:02:57](#t=0h2m57s "Jump to 00:02:57 in this episode")] Carl: The big takeaway here, I think, well, I don't know, we got a couple of big takeaways, but one of the headlines is definitely the React Foundation. This is a pretty big change to, or this sounds like it will be a moderately large change to the governance of React. They're pretty light on details of the actual governance, so far. They have talked about like a new technical steering committee. But they also say that the governance of that is not finalized. The members are not finalized, but they do have the founding members of the founding sponsors basically of this foundation, which are Amazon Call Stack, Expo, Meta, Microsoft Software Mansion, and Vercel with Seth Webster.

[[00:03:39](#t=0h3m39s "Jump to 00:03:39 in this episode")] Seth Webster is executive director and he's the what manager of the React core team,

[[00:03:44](#t=0h3m44s "Jump to 00:03:44 in this episode")] Mark: Basically. Yes.

[[00:03:46](#t=0h3m46s "Jump to 00:03:46 in this episode")] Carl: Yeah, so that makes sense. He is basically already doing that role and expanding what the core team means to an intercompany organization. But yeah, it's a lot of the details that I was most curious about, like what does, what does this mean for governance? Like how will decisions be made are not yet answered right now from the, from the various posts on this. A quote is, the React team is actively working on this new technical governance structure, and we'll share more details in a future post. So this is an announcement of a future announcement in some ways, but it's pretty real.

[[00:04:19](#t=0h4m19s "Jump to 00:04:19 in this episode")] So this is in collaboration with the Open JS Foundation, which is a partner to the Linux Foundation. So like th these are very large, pretty well-founded organizations that the React team is glomming onto in support of like a neutral home for React, as they call it.

[[00:04:38](#t=0h4m38s "Jump to 00:04:38 in this episode")] It's sounds like they're in incorporating React Native into this as well, which I think is not necessarily a given. You know, if you're talking about the governance of React, what that means for React Native is not necessarily implied. But just looking at the founding members like Amazon, Call Stack, Software Mansion, and Expo, and I guess Microsoft too, like those are all heavy React native investors.

[[00:05:01](#t=0h5m1s "Jump to 00:05:01 in this episode")] Mo: I think it's quite surprising in that sense because it's more heavy on the React native side. Like Vercel is really the key sort of non-react native player. The rest are really heavy on React Native and there's like noticeably missing membership from like Shopify on the Remix side as an example. I, I actually find it's very skewed towards React Native, almost shockingly.

[[00:05:24](#t=0h5m24s "Jump to 00:05:24 in this episode")] Carl: Yeah, I'd agree with that. It's, it is almost shockingly skewed towards React. React Native, given that it was not really pitched as the React Native foundation. That's true. I guess Software Mansion does do a fair amount of web React work. But I, I believe Call Stack is predominantly a React native shop as well.

[[00:05:42](#t=0h5m42s "Jump to 00:05:42 in this episode")] Mark: So I'll do my usual thing where I, I step back and provide historical context and what matter at all. So React was invented at Facebook. It has always been a project owned by Facebook and Meta. The code has been open source, but. You know, for years the entire development team was Facebook meta employees paid by Meta to work on React. And I've said even in my conference talks this year about Meta, Vercel, React ownership, that the React team has had the freedom to work on what they want. And that's true, but I've, I was reminded in some conversations with React team members at React Con, how much their work is constrained by, like the fact that their performance reviews are, "what have you done to further meta's goals this year?"

[[00:06:38](#t=0h6m38s "Jump to 00:06:38 in this episode")] And so in some ways their ability to push React in the technical directions that they think are right, are limited by how much they can make the case for that. Inside Meta, even something like the Concurrent Stores work is essentially being pitched as, how can we make Facebook's Ads Manager app faster in a lot of ways?

[[00:07:02](#t=0h7m2s "Jump to 00:07:02 in this episode")] So we saw multiple React team members move over to Vercel. Like people used to complain that this is all a Facebook app, all the meetings are inside Meta. There's no public roadmap, it's only meta. And then we had team members move to Vercel, and then it became, well, now Vercel is applying too much ownership to React and all the stuff we've talked about with Next and server components and Vercel and how that's supposedly driving the roadmap, et cetera.

[[00:07:30](#t=0h7m30s "Jump to 00:07:30 in this episode")] And so the team itself has been split across two companies, and they're working together. It's one team, but it's kind of within these two companies. And so because of Reacts widespread usage, there's been calls for many, many years that there ought to be some kind of an independent foundation that would own the trademarks, the rights, the development process.

[[00:07:56](#t=0h7m56s "Jump to 00:07:56 in this episode")] To React itself. And it always seemed kinda like one of those pipe dreams. The calls on Twitter to build, React into the browser. And obviously there's no way that's going to happen. And, and this felt like much of the same kind of idea. And so they, they did the initial React and the initial keynote at React Con, and they were mostly focusing on technical things.

[[00:08:17](#t=0h8m17s "Jump to 00:08:17 in this episode")] Like last year we, we fixed the, the sibling preloading bug. That was the suspense gate problem that everyone was talking about last year. And 19.2 came out and the compiler is 1.0. And then Seth came out and he did the one more thing routine and as soon as he put the React Foundation slide up, my jaw dropped.

[[00:08:40](#t=0h8m40s "Jump to 00:08:40 in this episode")] And I think I even said out loud, oh my word, they actually did it. And my first reaction was, even without knowing. Any actual details about what the foundation is or how it's going to work or whether this is even going to work out in practice. The fact that they have taken the time to do the legal preparation work to try to make this happen and are actually attempting to execute on that is a huge deal for React and the ecosystem.

[[00:09:12](#t=0h9m12s "Jump to 00:09:12 in this episode")] It, it is a statement of good faith and intent for how they want React to proceed in the future. Like without any details, my immediate reaction is, yes, finally, this is a good step forward. We'll see what it means in practice, but this is a really big deal.

[[00:09:32](#t=0h9m32s "Jump to 00:09:32 in this episode")] Carl: Yeah, I would agree with that. It's a really big deal that they're moving in this direction.

[[00:09:37](#t=0h9m37s "Jump to 00:09:37 in this episode")] I'm really curious about the details because I think there's a lot of, I don't know, like in the past they've done working groups and et cetera. And my understanding of the takeaway is generally, has generally been that they found it really difficult to manage participation in those like open access kind of arenas.

[[00:09:56](#t=0h9m56s "Jump to 00:09:56 in this episode")] So maybe the, this is kind of like adding a new layer of abstraction perhaps with administrative support from currently thriving independent foundations. Mm-hmm. So that, that definitely makes me think that this has a real chance of being something real and valuable that goes on for a long time. I'm curious what it means for things like, like in practice, it's not like anyone's employer is changing.

[[00:10:23](#t=0h10m23s "Jump to 00:10:23 in this episode")] No details have been shared yet. At least that anyone is being paid from this new foundation. I, I don't know whether to call it meta or Facebook 'cause it's on the fb.com domain. Mm-hmm. But in the Facebook engineering announcement here, they do say that Meta has committed to a five year partnership with over $3 million in funding.

[[00:10:42](#t=0h10m42s "Jump to 00:10:42 in this episode")] I don't know what other funding they might have. I don't know what other sources of funding they might have in the future, but like just looking at five years, $3 million, like that's 600,000 per year, which is like, you know, for meta engineers, that's like free engineers. So I don't know. I don't know what that means for people's incentives and where they will work and how their focus and performance will be evaluated.

[[00:11:04](#t=0h11m4s "Jump to 00:11:04 in this episode")] Yeah.

[[00:11:05](#t=0h11m5s "Jump to 00:11:05 in this episode")] Mo: What that rules out is that effectively the React Native or React and React Native Core teams will definitely not be unemployed by the React Foundation. Right. 'cause that would basically cover three salaries, which is far smaller than what the React teams are.

[[00:11:19](#t=0h11m19s "Jump to 00:11:19 in this episode")] Carl: I think the React core team has like 10 engineers.

[[00:11:22](#t=0h11m22s "Jump to 00:11:22 in this episode")] Mo: And RN is about the same. So you're talking 20 engineers. It's definitely not going to cover those employees to move them over, which is in some capacity. And then details are to be fleshed out. But in some capacity it is a bit disappointing because it would be great if they had more freedom as the React Native Core team to play around without the restrictions, like you mentioned, of the reviews that Meta has internally.

[[00:11:44](#t=0h11m44s "Jump to 00:11:44 in this episode")] And so it's gonna be interesting to see how that Dyna dynamic plays out effectively because there is still gonna be that same team. At Meta

[[00:11:51](#t=0h11m51s "Jump to 00:11:51 in this episode")] Mark: I, I have three sources of information that I'm piecing together for some of how the foundation is supposed to work. Seth Webster answered a few questions about this during the q and a session that was broadcast at React Conf.

[[00:12:05](#t=0h12m5s "Jump to 00:12:05 in this episode")] I had a conversation with a couple React team members and the topic came up about how things would be governed. And then there was an article on the new stack where Seth Perry was interviewed and was giving some further details about some of the governance.

[[00:12:21](#t=0h12m21s "Jump to 00:12:21 in this episode")] So as best I understand it, so you've got kind of the corporate level stuff that's Meta, Amazon, Callstack, Vercel, et cetera. They will then elect a technical steering committee. Which is, I guess sort of similar to how Node and other projects work, Seth said in the q and a, that meta will start with five votes on that corporate board, and then it will go down to one over the next five years. So you kind of a decreasing amount of influence in that sense.

[[00:12:53](#t=0h12m53s "Jump to 00:12:53 in this episode")] The technical steering committee, I assume, would be able to make decisions themselves, but obviously the fact that they are employees of the companies elected by those companies, et cetera, they would be taking their company's interests into account in the process. The article says that the technical governance will be in the open more than it once was.

[[00:13:17](#t=0h13m17s "Jump to 00:13:17 in this episode")] Request for comments, sets of stages, et cetera. But a lot of the process is still to be figured out. The article also talks about the foundation doing things like investing in React hubs, helping boot camps teach React better, possibly some things with conferences and alignment and such. So it sounds like the foundation is going to be doing more outreachy things.

[[00:13:43](#t=0h13m43s "Jump to 00:13:43 in this episode")] So there, there's a lot of this that is not clear what it means in practice yet, but certainly. React is not solely a meta owned thing at this point. There are multiple companies that are invested in it. There is a, a future for React independent of META'S ownership and goals. And this all feels like the people who care are trained to do the right thing.

[[00:14:11](#t=0h14m11s "Jump to 00:14:11 in this episode")] And

[[00:14:11](#t=0h14m11s "Jump to 00:14:11 in this episode")] Mo: on the conference side, I mean, I hope that's the case because one of the, as a conference organizer, one of the things that's perhaps challenging is that Meta doesn't necessarily sponsor any conferences beyond just React conf, right? And so, look, it's well known that that's sort of the case. And so maybe the React Foundations that is going to be able to sponsor those conferences, even if it's not a meta badge to speak, which would be very, very interesting if some of that is used for that.

[[00:14:38](#t=0h14m38s "Jump to 00:14:38 in this episode")] So I'm sure it's not just Meta who's investing, right? Like I, I suspect that there's funding coming in from. Amazon and Microsoft, at least from the bigger, bigger sort of established enterprises

[[00:14:49](#t=0h14m49s "Jump to 00:14:49 in this episode")] Carl: hopefully. And that's interesting. And the new Stack article interviewed Seth and has a bunch of poll quotes from him and they do talk about that, that like the foundation will look at expanding the annual React conf.

[[00:15:00](#t=0h15m0s "Jump to 00:15:00 in this episode")] I guess that's not sponsoring other conferences, but they're talking about conferences at least. But also something that caught my attention. They say while React Comp is one of the few conferences that actually makes a profit, it basically only paid for itself. And also it's a thousand dollars a ticket conference.

[[00:15:14](#t=0h15m14s "Jump to 00:15:14 in this episode")] So like hopefully the mode of making conferences self-sustaining is not making them cost a thousand dollars.

[[00:15:22](#t=0h15m22s "Jump to 00:15:22 in this episode")] Mo: Yeah. I mean conferences are from experience a very, very expensive endeavor. And if you don't have companies backing them, they will make a loss.

[[00:15:31](#t=0h15m31s "Jump to 00:15:31 in this episode")] Carl: I do wanna shout out, as we mentioned at the start, Seth says "We have lots of boot camps out there that are doing their best, but they're also sending people out into the world misinformed about how React works."

[[00:15:40](#t=0h15m40s "Jump to 00:15:40 in this episode")] This is interesting there. It's a, it's funny, they're actually hitting on a couple of points that I've investigated myself about how to do businesses in like a community since like I had previously connected with a bootcamp. Somebody was working there as the curriculum lead and they were doing a curriculum overhaul.

[[00:15:59](#t=0h15m59s "Jump to 00:15:59 in this episode")] 'cause they hadn't changed what they were teaching in three or four years. And they were like, is this still relevant? Is this what the industry's using? And I was like, cool. I help run a community. I know lots of experts. I would be happy to facilitate some kind of professional review. And then the bootcamp curriculum lead got laid off because that was 2022 and lots of things were not happening. So it's interesting to see them talk about things that I've thought a lot about.

[[00:16:22](#t=0h16m22s "Jump to 00:16:22 in this episode")] And also a lovely shout out, Seth says there are also cohorts such as meetups and local groups that could be assisted. One meetup actually led to the creation of the conference React Native London. So that's super cool. Love that for you, Mo.

[[00:16:36](#t=0h16m36s "Jump to 00:16:36 in this episode")] Mo: Yeah, I didn't, I, I did not have that on my Bingo card to get a shout out from Seth Webster on an interview, which is awesome. Yeah, it was good to have him last year.

[[00:16:44](#t=0h16m44s "Jump to 00:16:44 in this episode")] Carl: Mo is the organizer of React Native London and that one meetup that led to the creation. So that, that's just fun.

[[00:16:51](#t=0h16m51s "Jump to 00:16:51 in this episode")] That's cool. We have actual players in the ecosystem in the podcast right now.

[[00:16:55](#t=0h16m55s "Jump to 00:16:55 in this episode")] Mo: Well, you got Mark. So I'm stepping up to very, very, very high standards. Pretending to.

[[00:17:00](#t=0h17m0s "Jump to 00:17:00 in this episode")] Carl: Cool though. Yeah. So I don't know. I don't know if there's more to say there.

[[00:17:03](#t=0h17m3s "Jump to 00:17:03 in this episode")] 19.2 (Activity, useEffectEvent)
  
---

[[00:17:03](#t=0h17m3s "Jump to 00:17:03 in this episode")] Mark: Some of the more technical stuff. So they, they talked about React 19.2 coming out, which if you've been paying attention to this podcast for the last several months, you would've known all the details already. Like the new activity component for being able to hide components while persisting state use effect event for hopefully fewer use effect related bugs, et cetera. React compiler hit 1.0 and then

[[00:17:27](#t=0h17m27s "Jump to 00:17:27 in this episode")] React Native news
  
---

[[00:17:27](#t=0h17m27s "Jump to 00:17:27 in this episode")] Mark: Mo as like as usual, you wanna talk about the React Native-y things?

[[00:17:32](#t=0h17m32s "Jump to 00:17:32 in this episode")] [New architecture only from v0.82](https://reactnative.dev/blog/2025/10/08/react-native-0.82#new-architecture-only)
  
---

[[00:17:32](#t=0h17m32s "Jump to 00:17:32 in this episode")] Mo: So a few updates that they did, one of which was quite surprising was that the next release of React native version 0.82 is going to be new architecture only.

[[00:17:44](#t=0h17m44s "Jump to 00:17:44 in this episode")] So obviously earlier on a few months ago, we talked about how they deprecated the old architecture than they froze the old architecture. Now they're dropping the old architecture. And so to me that was a much faster deprecation cycle than I, I would've expected. Specifically when it comes to the fact that there are still a fair few libraries that are using the old architecture and only support the old architecture.

[[00:18:06](#t=0h18m6s "Jump to 00:18:06 in this episode")] So to give you a very concrete example, we had our monthly meetup literally yesterday, and there was a talk about Arrive, which is this animation engine that a lot of people are using to animate websites and make really, really cool stuff. But what we learned surprisingly was that Rive only supports the old architecture.

[[00:18:24](#t=0h18m24s "Jump to 00:18:24 in this episode")] So what that means is that this company who's a very popular healthcare company, really don't have a path to sort of migrate to the new architecture and hence version 0.82 until Rive starts to support the new architecture. So there are still libraries, albeit the majority of major libraries have been ported to the new architecture that are still hanging behind.

[[00:18:44](#t=0h18m44s "Jump to 00:18:44 in this episode")] So I'm quite surprised by this, but we'll see how it goes. It probably means that these library maintainers really need to like step up in the next month or two and get ready.

[[00:18:52](#t=0h18m52s "Jump to 00:18:52 in this episode")] [Vega OS announcement](https://developer.amazon.com/apps-and-games/blogs/2025/09/announcing-vega-os)
  
---

[[00:18:52](#t=0h18m52s "Jump to 00:18:52 in this episode")] Mo: The second big thing, which I have a little bit about later on, but just a quick one, is that Amazon did the Vega Os announcement earlier.

[[00:19:02](#t=0h19m2s "Jump to 00:19:02 in this episode")] It was towards the end of September that they actually announced it, but

[[00:19:04](#t=0h19m4s "Jump to 00:19:04 in this episode")] [Vega introduction at React Conf](https://www.youtube.com/watch?v=p9OcztRyDl0&t=5737s)
  
---

[[00:19:04](#t=0h19m4s "Jump to 00:19:04 in this episode")] Mo: they formally talked to the React and React native communities about it during React Conf. This is a completely new operating system that's fully built from scratch by Amazon folks and React Native is the UI layer. It's the only way that you can write apps for it, which is quite a big investment from Amazon's perspective into React Native as a technology.

[[00:19:27](#t=0h19m27s "Jump to 00:19:27 in this episode")] So Amazon makes a lot of devices. For a little bit of context, you might've seen their Fire TV devices, some of the Kindle fire devices that they had, but also like Echo dots and a whole slew of different devices that they manufacture. And previously a lot of these were running on Android or a variety of Android called Fire Os that they had adopted from the Android open source projects.

[[00:19:47](#t=0h19m47s "Jump to 00:19:47 in this episode")] And so now they've kind of completely ditched that and they're betting long term on React native now at our company at Theo and a bunch of other companies have been sort of working with Amazon behind the scenes on this. And we're aware of this but weren't really allowed to speak about it. So it's now out in the public.

[[00:20:02](#t=0h20m2s "Jump to 00:20:02 in this episode")] But it has been a good while, which I cannot specify how long that duration is that I have been aware of this, but just not able to talk about it and have been working with the Amazon folks to make sure that things are ready for their launch. So they have an introduction video at React Con, which I think is interesting because TV apps need to run on very, very limited specs. You're talking like a few gigs of Ram one or two gigs of ram and like very, very, very slow CPUs and some of them are even worse than that. So effectively they really had to optimize the living crap out of their operating system and make sure that React plays nice with it and is like the first class citizen when it comes to it.

[[00:20:38](#t=0h20m38s "Jump to 00:20:38 in this episode")] So it's, it's very interesting how they had to optimize it and it was a big undertaking for them. So. I guess congrats to the Amazon team, but beyond that, it's quite interesting for people that are interested in performance and React and React native.

[[00:20:48](#t=0h20m48s "Jump to 00:20:48 in this episode")] Carl: Yeah, I was just scanning this to see if I could find any details about what they built on top of, because like, I don't know, nobody builds a whole OS from scratch anymore. And this is on top of Linux?

[[00:20:59](#t=0h20m59s "Jump to 00:20:59 in this episode")] Mo: Yeah, it's c plus plus on top of Linux. Basically it's a Linux. Or is a Unix based system.

[[00:21:05](#t=0h21m5s "Jump to 00:21:05 in this episode")] Carl: Right, like, and so is Android. Like, I'm curious to what extent this is a locked down, stripped back version of Android that they're calling Vega. They don't say that anywhere, but like reading the tea leaves here, I, my assumption is that the, I don't know, Android was such a massive undertaking that Google then acquired and commercialized.

[[00:21:28](#t=0h21m28s "Jump to 00:21:28 in this episode")] Curious to hear more technical details about the OS layer here and how it…

[[00:21:32](#t=0h21m32s "Jump to 00:21:32 in this episode")] Mo: I can tell you a little bit about that because I've known about it for a while. It's not on top of Android in any capacity. It is fully, the Android open source project components of it are fully stripped out. It's built from scratch, which means that compatibility with old apps is.

[[00:21:47](#t=0h21m47s "Jump to 00:21:47 in this episode")] Limited and there's other solutions. It's not that you can run Android apps on it as an example that we're the old Fire OS apps.

[[00:21:54](#t=0h21m54s "Jump to 00:21:54 in this episode")] Carl: So wait, it sounds a little bit like you're saying there is a shared lineage with Android, but it's different enough that its own technically distinct thing.

[[00:22:02](#t=0h22m2s "Jump to 00:22:02 in this episode")] Mo: They share a technical lineage in the same capacity that like Mac Os and Androids here, which is, they are both unique systems and that's pretty 

... (content truncated)
