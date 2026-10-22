---
type: "twir-recovery"
issue: 295
item: 11
source: "https://share.transistor.fm/s/f48613c6"
final_url: "https://share.transistor.fm/s/f48613c6"
retrieved: "2026-10-22T11:30:11+00:00"
original_note: "frontend/raw/twir/295/articles/11 - This Month in React - Release candidate season; is that an asteroid hitting web educators.md"
editorial_review: "pending"
truncated: true
---

Original intake note: [[../articles/11 - This Month in React - Release candidate season; is that an asteroid hitting web educators|This Month in React - Release candidate season; is that an asteroid hitting web educators?]]

# This Month in React

Carl Vitullo: Thank you so much for joining us for the August edition of This Month in React as we recap what's going on with React, React Native, and generally on the web platform. We are coming to you live from Reactiflux, the place for professional developers using React.

Carl Vitullo: I am Carl generally known as vcarl on the internet. I'm a staff product developer, freelance community leader, occasional entrepreneur, sometimes consultant here helping run Reactiflux. And generally just trying to keep this place valuable and pro-social for everyone around it.

Mark Erikson: And I'm Mark. My day job is at Replay, where we've built a time traveling debugger and now an automated QA platform that uses t , the time travel awesomeness to help find bugs in your app. Replay QA, please check it out. And outside of that, I am still doing an awful lot of Redux stuff

Carl Vitullo: Mm-hmm. Cool. Yeah August is often a slower month. A lot of Europe is on vacation. you know, kind of the end of summer. It's the start of school. So just often there's not as much going on.

Carl Vitullo: We do have a lot of new releases or pre-releases, release candidates to talk about. Yeah. Let's get going.

Carl Vitullo: First off on our new releases, we've got Waku 1.0 as a release candidate. Yeah. Waku, I don't know, I feel like I've been thinking of it and describing it as a new framework for server components, and I actually went back and checked how we've discussed it, and we've been discussing it for three years now. Like, three years is no longer a new tool, you know? But yeah, here we are at 1.0 with a release candidate.

Mark Erikson: The, and, and, and to recap Waku is a React server components framework that's been built by Daishi Kato, who i- who is also the brains behind Zeustand and Voltio and Jotai, and a slew of other state management related libraries. And the goal is to be a minimal server components framework rather than something like the, the all-encompassing Next.js

Carl Vitullo: Yeah. So cool. Love to see things get to release candidates. The fact that they've been driving towards 1.0 for so long makes me think, I don't know, makes me think this is being thoughtfully approached. Generally they, they, are very thoughtful, so that's very cool to see.

Mark Erikson: It looks like they've, they've been doing some, some navigation fine-tuning and improvements, but other than that, it's mostly like we, we think we've got it close to being final soon

Carl Vitullo: yeah, a- actually I'm gonna, I'm gonna put out a little call to audience, anyone listening. If you have, like, built something with Waku, I would actually love to hear about it. I don't think I know anyone personally who has, like, any kind of extensive experience. So, yeah, if you have any feedback, I'd love to hear about it in the #general-tech channel or, you know, shoot me an email to hello@reactiveflux.com. Just general curiosity.

Mark Erikson: I was actually just wanting to try to look up download stats. Like, I've, I've seen it for a while. my general assumption is that it's not widely used, and certainly not in comparison to something like Next.js or React Router.

Carl Vitullo: Yeah. on that, I just checked. It has 22,000 downloads per week which compares to, you know, TanStack React Query at 60 million n. So yeah, definitely on the smaller side yeah. Okay, moving on.

Carl Vitullo: Another release candidate. We have Pre Act 11 coming out , the main thing they highlight is it's now tree shakable which is a claim that I always take with a pretty substantial helping of salt. Just never know. I don't know. There's so many ways to break tree shaking, and we've been... libraries have been working to be more tree shakable for, like, six, seven, eight years.

Carl Vitullo: So, you know, I don't know. It's cool. Love that. That's great. I hope it works. But yeah, Preact is generally interesting. It's cool. Last month we were talking about React alikes, and Preact is definitely the original React alike, although it is increasingly less alike as time goes on.

Mark Erikson: Yeah, although it do- it does say that the, the compat package now includes the several other React methods that have been added recently. So while the semantics have diverged somewhat over time, they are at least still making an effort to try to keep it relatively drop-in if possible.

Mark Erikson: MobX 7 came out. it's funny because Mo- like MobX, I think technically was, like the first releases of it were actually a few weeks before Redux came out back in 2015. So MobX has been around for a while. MobX 7 is primarily a cleanup and modernization release. They've dropped the legacy implementation and now it now requires proxies to actually track things, which has always been the default behavior.

Mark Erikson: Improved some bundle sizes, some tweaks to the, to the React bindings. So still out there and still being worked on

Mark Erikson: And on a much bigger note Next 16.3 is out, and the, the Next team talked a lot about this release. they seem to feel this is one of the bigger releases they've done in quite a while.

Mark Erikson: there's a bunch of dev improvements. It's supposed to build faster, less memory usage but it also has what, what they're calling instant navigations for s- better spa-like behavior as well

Mark Erikson: There weren't a lot of great secrets revealed in that.

Carl Vitullo: Right. Yeah. And it's just like it's been such a consistent through line for two or three years now of like, yes, caching is hard. Local development is hard, especially if you're dealing with, like, 100,000 pages being generated. So, you know, it's just like , the challenges and the stated improvements have a certain sameness to me over time for Next.

Carl Vitullo: I'm su- You know, it does improve. It gets better. It, it... But, like, the challenges are still pretty similar.

Mark Erikson: And, you know, may- maybe this is just a snide comment from the gallery from someone who doesn't even use Next at all, but it always... It, it's felt like a little bit of that complexity was sort of self-inflicted in a way

Carl Vitullo: Right. Yeah. I think we have another thing to talk about later on. I can't remember what this got in the doc, but Lovable put out a blog post about moving away from Next to TanStack. And yeah, you know, it's, a, a lot of it is like, oh yeah, we had performance problems, and those performance problems got resolved by moving to Vercel, but we would, would like to have more optionality f- than in our hosting.

Carl Vitullo: So, you know, it's, the same kind of complaints, and agreed that a lot of the complexity seems kinda self-inflicted. they keep trying to fix it by adding more complexity, it feels like. You know, it's, it's a continuous additive system, and the fact that they keep adding new things to try to address the problems, and the root problems being solved don't seem to be changing, makes me suspect that the, they have gone deep into the diminishing returns of additions.

Carl Vitullo: I think it's perhaps time to subtract. But subtracting is usually a major version bump anyway.

Carl Vitullo: Okay. We have a new React Native version 0.87. Man, I- every time we have got a release, I miss having Mo out here because

Carl Vitullo: he

Mark Erikson: was just about to say that

Carl Vitullo: He's got such a good breadth. Maybe I should bring him on as an analyst or something like that. But yeah, the, the big highlight here looks, to me at least, looks to be that they now have a strict TypeScript API and type definitions are being actually generated rather than hand-authored. That's a huge... Going from hand-authored types to generated types is always a massive project. It looks like this has been in the works since about point or 0.80. So, you know, that's seven, seven releases now that they've been going towards it. So, their strict TypeScript API is now the default. Not everything will be compatible, so there's an opt-out, but they've stated the intention of this - you know, the, the opt-out going away over time.

Mark Erikson: TanStack Table version nine is out, and I believe I, I, I know I'd at least pasted a couple of the prior blog posts in the tech reads and news channel. I don't remember if we actually linked them in the, in the podcast last month. Some of the updates they now have a increasingly wide range of adapters for different frameworks React, Preact, Vue, Solid, Svelte, Angular, Lit, Alpine, Ember and Octane. So pretty much anywhere you're using a framework you could use TanStack Table if you wanted to.

Mark Erikson: They've made a whole lot of improvements to performance. They've pulled off some very nifty JavaScript tricks to try to cut down on memory usage rewritten the internal state management, improved type safety, and as we d- were just saying, things are more tree shakable.

Mark Erikson: Wonderful

Carl Vitullo: Wonderful. Yeah. Tables. Man, ugh. I love that, I love that TanStack has been so persistent at trying to make a good table abstraction, but I'm gonna be honest, I settled in, like, 2017 of saying, like, "Nope. There is no table abstraction worth its weight in the bundle. I'm gonna re- write every table from scratch," which has its own trade-offs.

Carl Vitullo: You know, it's, it, then you have to copy functionality and stuff is missing. But, like, man, just, like, seeing this release talking about how they have, like, a new architecture that, y- you know, with a record number of framework adapters, it's just like, man, tables are so much more complex than we give them credit for.

Carl Vitullo: It's so hard to make a good table

Mark Erikson: But I thought coding was solved

Carl Vitullo: Coding is? It's completely solved. , it gets more and more solved the less closely you look at the outputs.

Mark Erikson: On a completely different note we've talked in the p- past about w- what was known as the records and tuples proposal for the JavaScript spec, which was supposed to add new data types to the language that were gonna be deeply immutable, and then you could just say, "Is this value equal to the other?"

Mark Erikson: And the triple equals operator would do a deep comparison. That proposal eventually got withdrawn. It's dead, it's gone, it ain't happening. So there's now a new proposal called composites, which is sort of trying to solve the same problem, but in a very different way. Reading it, it looks like you create these wrapper objects, and then the wrapper objects will do the value comparisons for you, I think.

Mark Erikson: So nothing immediately actionable here, but it, it is interesting to see that the design committee champions are still trying to figure out a valid solution for this problem

Carl Vitullo: Yeah, that's interesting. Looks like it's kind of I'm looking at this example in the actual spec, the stage one draft spec basically wrapping an object in a composite constructor, and then, you know, you do the same object keys and values in two, and then do a triple equals comparison, and cool, they're equal.

Carl Vitullo: Th- so that's awesome. That's interesting. That's useful. But yeah, stage one, that's pretty far away from released

Mark Erikson: And then we've talked some previously about Solid 2.0 being on the way and having a major change in how it handles async, to how that's baked into the signals graph. They've officially hit release candidate this month. So there's the 2.0 RC announcement blog post but then there's also some deep dives that we'll touch on later that talk in more detail about how the async graph works and what that means for your code.

Mark Erikson: I continue to say that, like, Ryan Carniato is probably doing some of the absolute deepest research into framework development and data modeling and how to build better tools than pretty much anyone else out there. Obviously the React team put a lot of thought into server components. The Next team's putting a lot of thought into, you know, building their framework.

Mark Erikson: Ryan's doing, like, the bleeding edge research here

Carl Vitullo: I love that, so the async lives in the graph is for one, just a great header. I love that as a thing to unpack and understand. But it's a, I, I wanna call out this little parenthetical that says, "A computation can return a promise, parentheses, or an async iterator." And man, a, promises versus async the iterator is just so much more powerful. So being able to support those, like, you know, it's a little aside because everyone knows and uses promises and those, you know, everyone assumes those. But man, I've been using async iterators more and more lately, and they're so powerful.

Mark Erikson: I, I was, I was skimming through the third of the three explainer blog posts, and they fleshed that one out in more detail. And I think the example there shows a component that, like, looking at it, you almost wouldn't even know that it would get updates because it just works reading the data

Carl Vitullo: Yeah. I've been using them mostly because I have been doing all of my code in effect the last couple of months, and, like, or everything is a generator. And generators can be iterated upon. But yeah, like, you know, it, an async iterator is basically a promise that can resolve multiple times.

Carl Vitullo: Like, ugh, that's incredible. I don't know. So just, like, So many times when you're modeling something as an asynchronous request, it may actually be better to model it as a stream of incoming data, and you can't do that with a promise. You cannot have an, a stream a stream of events. So i- iterators are just, like, this really magical in-between point between events, like, you know, event-driven architecture and promises. anyway,

Mark Erikson: Ben Lesh would like to have a word with you about RxJS and Observables at this point

Carl Vitullo: Ha ha. Fair enough. Yeah, super cool though. Last thing I'll say on that is definitely lend... early and prominent shout-out of async iterators, I think, lends credence to what you were saying about him being on the cutting edge of the research here. Like, yeah. Everyone else needs to catch up. go become familiar with async iterators, because it will level up your professional, capabilities. Okay, moving on.

Carl Vitullo: Bun has had a big release

Mark Erikson: it's the single biggest change log I've ever seen. It's for what is technically a minor release, except that they also literally rewrote the entire thing from Zig to Rust with AI. Technically, there's no breaking changes, so yeah.

Carl Vitullo: Yep, they've moved out every zig. They're now on Rust.

Mark Erikson: Deep cuts

Carl Vitullo: Deep cuts. You know, you can't just put an opportunity like that in front of me.

Carl Vitullo: Yeah, I think this is super cool. there's been a bunch of drama, a bunch of words typed and spoken about the Rust rewrite, and, like, I just, I don't find that very interesting. The most interesting thing I think is that they used Basically a fully automated workflow and the existing test suite to say, "This works. Go fix it so that it works in this language instead." and then $160,000 in tokens later, they had a Rust-authored version that is apparently good enough to release, and not only good enough to release, but good enough to build a, like, remarkable set of additional features on as part of that release.

Carl Vitullo: So, that's fascinating. That's cool. It's a little crazy to see that much coming out. J- Jared Sumner has always been, like, kind of confusingly prolific at, in terms of, like, level of output here. So I don't know, just seeing him become AI-enabled is remarkable.

Carl Vitullo: But I was gonna say, oh, this is the most important one, and then I'm looking at the whole list and they're all pretty wild. Like, bun.image lets you do a lot of really powerful image manipulation for the web natively, you know, just within Bun, which is great, 'cause I have previously done stuff like that with FFmpeg and Sharp, and those feel like they were written in the early 2000s, because they were. those have been around for a long time because nobody wants to rewrite them, because doing that work in a way that is performant and, like, usable is really hard. So, you know, kudos for shipping something like that. I haven't played with it myself yet. I want to. But yeah, decode, resize, rotate, encode JPEG PNG, WebP, GIF. Yeah, just, like, all of the image formats, doing resizing and basic editing kind of stuff is really, really interesting.

Carl Vitullo: But then they've also got bun.webview, which is basically like Playwright or, you know, Cheerio or something, just natively within the standard library, which is wild and really helpful.

Carl Vitullo: I haven't made use of this yet, but I did go through... I have a skill that I made for myself that is like, "Here's how to set up a new project here. You know, here's how to set up the linting, here's what tools to use." And I told it, "You should use bun 1.4 because the web view stuff makes it really easy to do end-to-end testing," allegedly. I still need to validate this.

Carl Vitullo: But they've also got, like, a markdown parser and, like, a cron scheduler a pseudo terminal so you can dri... You know, they, they say, "So you can drive Bash, Vim or whatever from JavaScript without Node PTY." I've been rigging up a bunch of, like, experimental AI agent harness stuff, as part of doing that, I've been writing a lot of wrappers for Bash to be like, "I need this service to be running in the background while this server runs. it's really janky. I've had AI write a shit ton of, like, bash-compatible things that are, like, forwarding control codes, and making sure output redirection works as expected, and all those little subtle details. So again, one more thing that is, like, a pretty big load off of my mind building something if I can just ship it out to a standard library.

Carl Vitullo: So anyway, yeah, it's a massive change log. Lots of controversial practices involved in producing it and releasing it, but mm, it's pretty cool. End result is pretty neat

Carl Vitullo: Cool. And uh, man, another thing I've been dreaming of for years and years and years, GitHub is now doing a public preview of stacked pull requests stacked PRs. we've talked about this a couple times. I'm not sure how widely familiar, you know, the ecosystem is with stacked PRs.

Carl Vitullo: This has been a, the way that I work intuitively for a number of years at this point, like probably dating back to 2019. Where, like, work on something, produce a finished branch, push that up, create a pull request, and then I'll ... Most of the time, the thing I just built was to enable future work. You know, it was to unblock other work that I mean to be doing. So then I'll just take that branch and continue working off of it, off a new branch, and boom, that's a stacked, you know, that's a series of stacked branches.

Carl Vitullo: I'm, while branch A is being merged, I'm working on branch B, and then, you know, when branch A gets merged, I push up branch B for review. The, the revision here is that now you can just push them all up and mark the PRs as stacked on top of each other and it will automatically do lots of rebase and branch juggling for you.

Carl Vitullo: Yeah, the challenge there is, okay, you stack branches up like that, like I was just describing, but then when you merge them, you know, the, the, the commit SHA changes. You know, maybe you do a squash merge. You know, maybe it's a, Anything other than a fast-forward, and you now have to do a rebase in order to have the, have the branch

Mark Erikson: Which means you have to pull down locally, you have to do the rebase, you have to, you have to do some juggling locally, push it back up, actually create things, and you have to repeat that for every time you do, you, you merge one of those PRs

Carl Vitullo: Right. And so when you've got, you know, branch A and branch B, it's not so much work. But when you've got branch A that drives branch B, that drives branch C, that drives branch D, and you've got eight people all contributing to a shared code base, like that pull, rebase, push cycle ends up being a pretty substantial amount of work.

Carl Vitullo: So it's really cool that GitHub is now enabling this. There's a, there's a pretty closely related concept here as well called a merge queue, which is basically like an engineering practice where as part of review, you know, you don't just mer- you don't just merge when approved. You don't say like, "Okay, this, this PR is now approved for ship," whatever. "Let's merge it now." it's part of a queue, you know, it's in line. So, just as a way to manage conflicts, avoid doing rework because, you know, it... When you ha- when the work that's being merged into release is more predictably sequenced, a lot of benefits fall out of that. And stacked pull requests are a really interesting way to enable a simplified version of that for a, a larger number of people.

Carl Vitullo: So I... This is really cool. I'm excited about it. I I'm gonna have to play with it.

Mark Erikson: mean, it's, it's, it's worth noting that on GitHub, the unit of review is the PR. Like, you can have as many commits as you want, but what you see by default is the final result on the branch, and that is what we're all very used to reviewing, and it's, it's what many other GitHub-like tools have copied.

Mark Erikson: But there were, there have been plenty of other code hosting and review tools Gerrit, Phabricator, and others, where the unit of review was the commit. And so another part of this usage-wise is how big of a unit am I trained to review at once? So, like, maybe you have your, you know, your 5,000-line PR, but it makes sense to review the changes in smaller chunks.

Mark Erikson: Well, on GitHub, it becomes difficult to go through and review, like, one commit at a time or something. So either you say, "Here's the whole thing. Looks good to me," or you have to split it into multiple PRs so that smaller chunks are more easily reviewable, but then you have to do the branch juggling dance.

Carl Vitullo: Yeah, and I guess I, I also wanna say this was, like, Jared Palmer's pet project while he was at GitHub.

Mark Erikson: For about three months

Carl Vitullo: For the... Right. So it appears that Jared Palmer legitimately joined GitHub specifically to ship this, got it into a state where it

Mark Erikson: It's the meme. It's the

Carl Vitullo: Yeah.

Carl Vitullo: Right. And then left, and then went... Yeah, so anyway, that's, that's pretty funny. Uh.

Carl Vitullo: Okay. Into our main content yeah.

Carl Vitullo: Yeah.

Carl Vitullo: Right

Mark Erikson: Right so a few smaller items from React core news-ish stuff this month.

Mark Erikson: There's a new API that's coming out for React DOM. It's a function called Browser, which is intended to be passed to the increasingly expanding use method. So it's use. The idea is it re- the return value of use will differ depending on whether you're calling this on the server or on the client.

Mark Erikson: So if you call it on... If you have a component and it's getting rendered on the server, in a server component or whatever React will see that and essentially leave a hole in your component output. And then it knows that when this run, runs again on the client, then it will fill in. pretty much every code base at this point has some form of a do this logic only on the client util or, or something along those lines.

Mark Erikson: This is essentially building that functionality directly into React DOM itself

Mark Erikson: Let's see.

Mark Erikson: We, we... I believe I mentioned last month that, that there were updates on the way for the React Foundation website, and then they were also talking about governance-related things. They have shipped an update to the website, so it at least looks less AI vibe coded at this point. still Looking and waiting for more public details on what the foundation is going to do long term, but again, you know, bits of activity.

Mark Erikson: Things presumably are churning away behind the scenes.

Mark Erikson: So good to know that's on the way

Mark Erikson: And then the other interesting bit was that the OXC team has shipped their official support for React Compiler built into Oxlint, et cetera. And, and this is interesting for multiple reasons. So React Compiler itself was originally written in TypeScript and also required a Babel plugin. And so it existed, but we've spent all these years converting our build tool chains to Rust.

Mark Erikson: Babel is slower. People saw that build times got slow again, and like, "We don't like this. Can you just do it in Rust?" The React team did an AI-assisted port of the compiler logic from TypeScript to Rust. That is in the React repo. But then the question is: how will that integrate with other build tools? So other teams, Biome, OXC, Bun, et cetera, have been taking the Rust code and trying to figure out the best way to integrate it, and the OXC team in particular has actually pushed ahead in a lot of ways.

Mark Erikson: They tried to integrate it once, and then they decided that it made their binaries too big, and they didn't wanna ship that to everybody, including people who don't use React at all. So apparently they went back to the drawing board. They found some ways to optimize the code, shrink the bundle size, make it semi-optional maybe.

Mark Erikson: And apparently now the both the build performance and the binary size are good enough that they felt ready to actually ship it. So that, that support is now baked in at this point.

Mark Erikson: And Biome is trying to do some integration as well. Bun 1.4 is supposed to have React Compiler support. So slowly but surely, these pieces are all coming out in the ecosystem in a much faster way, and so hopefully that means that more projects will be actually be adopting the compiler over time and thus seeing whatever runtime performance benefits you get from using it

Carl Vitullo: Should we go to Asteroid?

Mark Erikson: Yes, the asteroid not astro, asteroid

Carl Vitullo: Yeah. Yeah. Nolan Lawson, who is is somebody who's been, like, individually fairly influential on me as a developer I just first encountered him 10, like, more, 15 years ago when I was still in college. So it's cool to see his name still around. he put out a great blog post called The Asteroid Currently Hitting Front-End Web Development. , basically the same thing I actually said on, at the end of our last episode about impacts of AI on educators, on content creators, especially in the front-end engineering space. And basically, you know, he's highlighting that He says, "A lot of the educators I admire in the front-end web space seem to be either bowing out or dialing back their efforts."

Carl Vitullo: And like, yeah, Axel Rauschmeyer, hugely influential blogger about the standards process and, you know, JavaScript itself as a language. Salma Alam N- Naylor, well, Selma and Josh we talked about specifically at the end of the last episode. And, and then he calls out, too, that, like, Kenzie Dodds, Addy Osmani, Rachel Neighbors, Lydia Hallie have all moved more from front-end development into, like, AI agents software development. Which I, which I think is fair. You know, I don't, I, I, I think comparing people stepping back versus staying on the cutting edge. for a long time front-end was the cutting edge, and then it was, like, React Native and where are we gonna put React next? And so now it's not as much that. Now it's AI and how do you build stuff? How do you build a software factory?

Mark Erikson: , we've even talked about, like, the energy at React conferences seems to be down, whereas the AI conferences have all the energy. So, like, there,

Carl Vitullo: Right

Mark Erikson: like, a lot of trend here

Carl Vitullo: . This post from Nolan Lawson, he talks about the future of front end. And I'm just gonna read a couple of, like, high-level points he makes. The front end is less risky to just hand to an agent. Developer experience is becoming less critical overall. Standards will catch up. I think this is interesting.

Carl Vitullo: I, these rhyme with points of contention that I've seen in the industry for essentially my entire career. Like, you know,

Carl Vitullo: is front end... Right. Front end is easy, and developer experience isn't worth the time investment. , I wanna call this out. He says, under developer experience becoming less critical, "The agents know React. For better or worse, React is heavily over-represented in the training weights." And again, like, something we talked about last episode, I believe, was Aiden Bai put together a benchmark of not just React, can it make something functional, but how well does it actually execute React best practices across different models?

Mark Erikson: they know what React code looks like. They don't really know how to write good React code

Carl Vitullo: Right. So

Mark Erikson: They know what bad React code looks like

Carl Vitullo: Yes, bad React code is heavily overrepresented in the training set, but, I used to, I used to work, when, when I was more earnestly working full time, I went to a lot of different companies for, you know, a year, six months, a year and a half, and the reason I was able to be very successful at that is because every company used the same set of very bad practices that represented a fundamental misunderstanding of the advantages that React offered.

Carl Vitullo: And so it's like, cool, I understand those, let me come in and fix this incrementally one thing at a time, and the improvements are so mind-blowing to you as somebody who doesn't understand the tools you're using, that, you know, great, cool, great, awesome. Who... Lovely performance revie

... (content truncated)
