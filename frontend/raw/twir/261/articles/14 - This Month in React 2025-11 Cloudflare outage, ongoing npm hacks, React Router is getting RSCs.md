---
type: twir-item
issue: 261
item: 14
item_type: item
date: 2025-12-03
source: https://share.transistor.fm/s/8aea071c
tags:
  - "ReactRouter"
  - "2025-11"
  - "RSCs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-12-03-TWIR-261|Index]]

# Item 14: This Month in React 2025-11: Cloudflare outage, ongoing npm hacks, React Router is getting RSCs

Source: [https://share.transistor.fm/s/8aea071c](https://share.transistor.fm/s/8aea071c)

Summary:
A podcast episode covering recent React ecosystem updates, including React Router’s adoption of React Server Components, React Concurrent Stores, and discussions on async transitions. Other topics include major library releases, web ecosystem trends, npm supply chain security, and the performance gap in web devices.

Key takeaways:
- React Router is moving towards RSC support and async transitions.
- React Concurrent Stores and polyfills are being explored.
- Security and performance in the web ecosystem remain active concerns.
- Ongoing discussions about promoting the web platform over React.

Recommendation:
Summary sufficient (listen for in-depth discussion or if tracking React ecosystem trends)

Why it matters:
listen for in-depth discussion or if tracking React ecosystem trends

Content:
# This Month in React

2-vcarl: Hello.

Thank you for joining us for the
  
November edition of this month in React.

As we recap what's going on in the
  
React, react native and web ecosystems

We're coming to you live from
  
Reactive Flux, the place for

professional developers using React.

and I am Carl.

I'm a staff product developer and
  
freelance community leader here at

Reactive Flux, where I do community
  
programs like these events and build tools

to help keep the community operating.

1-acemarke: Hi, I am Mark.

My day job is working at replay and
  
doing various time travel debugging

and information architecture things.

Outside of that, I, I work on docs.

I complain about the React docs
  
and I collect links and I go

rewrite libraries like emer.

2-vcarl: mo unfortunately could not join.

He had a, fire drill happen.

Metaphorical fire drill happened at
  
work like an hour before we started,

but generally we have Mo who is
  
head of MO at Theto and is very

active , in the React native community.

Kind of sad that he had to skip
  
out this month because he just

did react Native London, and I
  
was hoping to hear how that went.

But yeah, let's get straight
  
into it with some new releases.

First off, we've got better off 1.4.

I actually use Better off now.

Woo.

I have been excited about it for a while
  
because I don't like authentication.

Libraries generally, like stuff
  
like Passport or what, you

know, even clerk or the SaaS
  
businesses, just like none of them.

I didn't like them very much, so, was
  
very pleased to see an open source

library that looked to cover many
  
of the bases that I want and can

confirm after using it that it does.

So I'm excited to see better off
  
1.4, which is the first release

since I believe July when it did 1.3.

A couple of quick highlights from it.

It's got stateless off, so you can
  
do sessions without a database just

by not giving it one, which is nice.

It's also got SCIM provisioning
  
for identities in multi-domain

scenarios, which is cool.

Also some other little details
  
like database joins and

custom state for OAuth flows.

But yeah, just auth is a shockingly deep
  
subject when you actually start dealing

with the nitty gritty weirdnesses of it.

And I have generally found most open
  
source projects trying to support

authentication to be, to leave
  
something to be desired and better

off leaves the least to be desired
  
of the projects I've tried, so.

Love it.

New version

1-acemarke: I have thus far managed
  
to stay away from dealing with

oath at all in my career, and I
  
would like to keep it that way.

2-vcarl: Yeah, that's not a bad call.

Since I haven't been able to avoid
  
it, I went a little bit deep on

it and I don't hate that either.

It's interesting.

It's fascinating actually.

I don't know.

One of the vague startup ideas in
  
the back of my brain is related

to authentication and identity
  
management, which could be cool.

I don't know, maybe I'll do
  
something with that eventually, I

want you to unveil your mag opus

1-acemarke: happily.

So I talked about this a bit last
  
time, but Redux Toolkit relies on

emer for immutable state updates.

It always has since day one.

And we've gotten various complaints over
  
the years that, you know, emer is kind of

slow, but we've always said that we prefer
  
the fact that it eliminates accidental

mutations, makes reducers easier to write.

Of course, we want Redux
  
Toolkit to be fast, but we

also want things to be correct.

End users do not have bugs.

So I'd done a little bit of perf
  
investigation into Imer like a year ago.

Saw that it had gotten slower, filed
  
an issue, it was kind of left there.

And at the start of September, I myself
  
dug in and started trying to see if

I could optimize I ER's performance.

And I spent well over a hundred
  
hours collectively across September

and October, deep diving into Immers
  
code base, comparing it to other

libraries understanding how it worked.

And trained to do a bunch of performance
  
optimizations and so ended up filing

a few different prs Imer 10.2, shipped
  
last month with some small tweaks, and

Michelle West Rate just merged a big
  
architectural change and released it as

Imer version 11 just a couple days ago.

And then I was able to put out RTK
  
two point 11, which picks that up.

So free performance wins
  
for Redux toolkit and nier.

2-vcarl: Heck yeah.

That was what was the average speed up?

1-acemarke: the current builds average
  
about 20 to 25% across all the different

benchmarks varying by scenario.

And then there's another outstanding
  
PR, which adds an optional array

methods override plugin, which
  
drastically speeds up array methods.

2-vcarl: Heck yeah.

That's awesome.

We love a core performance improvement
  
and I, I wanna shout out the ecosystem

performance, you know, I don't know,

1-acemarke: E 18 E folks are awesome.

They have been doing a ton of work to
  
clean up large dependency trees and slim

down packages and remove dependencies
  
across a wide variety of tools

2-vcarl: Yep.

a stat that I believe we'll talk
  
about later, I saw in general

ecosystem commentary yeah.

I guess in the NPM supply chain attack
  
that we'll talk about later, a a a

stat that came out of a blog post from
  
that was that the average JavaScript

project pulls in 683, I believe
  
in was it transitive dependencies?

Just like, yeah.

It's a lot.

So

when you've got that,

many dependencies, performance
  
of the ecosystem is challenging.

Yeah.

1-acemarke: that doesn't surprise me.

I know that React app the last I saw it
  
defaulted to about 1500 dependencies,

largely because of Webpac, et cetera.

Vet's obviously a lot fewer, but
  
still that's, that's not great,

just for a whole variety of reasons.

2-vcarl: I guess teaser for y'all.

Later towards the end of the episode
  
we're gonna talk about web ecosystem

and there's been some blog posts talking
  
about like AI and how it defaults to

building react instead of using the
  
web platform and, how do we promote

the web overreact, things like that.

Which I don't know, it just feels that
  
we just started bleeding into that

topic and so we will get much more
  
deeply into that later in the episode.

1-acemarke: Next release.

So, storybook 10 came out.

Few different big points there.

One of the biggest is that it's
  
now ESM only, they've removed

all the, the common JS artifacts.

So they've shrunk the install size
  
and they've also drastically shrunk

the dependency chains as well.

As well as some improvements
  
to things like the mocking and

some of the storybook formats.

And then one other release of note,
  
the remix folks are continuing to

work on , remix V three after the
  
initial demo and announcements.

And they're trying to build it,
  
as I understand it, with a lot

of smaller reusable packages.

And they just put out the first 0.1
  
alpha of their event interaction package,

which is providing an abstraction
  
for being able to compose events and

listeners and behaviors together.

Looks interesting.

I'm not gonna claim I understand
  
like exactly the benefits this comes,

but nice to see the progress there
  
and I suspect that a lot of folks

are gonna get some use outta this.

2-vcarl: Yeah, I'm reading the
  
syntax here and it looks like

a different way of adding event
  
listeners to dom nodes, which, sure.

I don't know.

There's weird quirks.

And certainly the remix team and, you
  
know, Michael Jackson and Ryan Florence

specifically have shown, have demonstrated
  
a great willingness to jump into.

What many people consider solved problems
  
to reexamine from first principles.

So I dunno, they, they've done that,
  
they've done that repeatedly with their

own solved problems of data loading
  
in routing the interaction between

data loading and routing I feel like
  
that's one of the bigger complaints

about React router is that they
  
keep reexamining that same question.

So, I don't know.

It's interesting that they do
  
have interesting things to say

when I've seen them reexamine,
  
quote unquote solved problems.

So, I'll, I'm curious.

This looks a little strange.

It looks pretty divorced from the
  
DOM structure, so if you just like on

input element and then add a bunch of
  
listeners for it, that's curious anyway.

Yeah.

O one release, we'll see
  
what they come out with.

Okay.

That's all the new releases we got so far.

Let's go into some main content.

First off we want to talk a bit about,
  
yeah, mark, you are on a, an ecosystem

panel at React Summit this month.

1-acemarke: So, Let's see.

Addie has money, was moderating.

We had Seth, Webster from the React
  
team, react Foundation shun person,

Amy Ner Nicholas Gallagher, and myself.

A lot of the discussion was.

Us asking Seth Webster questions
  
about, so this React Foundation thing,

like how is this actually gonna work?

What does this actually mean for the React
  
team and the project and the ecosystem?

there is a video for the panel.

It's not unlocked yet.

I have access to it because
  
I speak at GI Nation events.

But the video should unlock
  
within a couple weeks, I think.

a few different points that Seth made
  
during the panel itself, and then

I had a chance to have a follow-up
  
discussion with him afterwards.

And there's a few different very
  
interesting pieces of news about

how the foundation's going to
  
work and what their plans are.

he talked a bit about some
  
of the, the funding process.

So, you know, large companies pay, you
  
know, a good chunk of money to be members.

The, the existing board member
  
companies have already paid up

for like three to five years.

And it sounds like he'd actually been
  
working on putting the foundation

together for over four years.

Like this was a very long
  
term kind of a process.

And they're hoping to do a number
  
of different things with the money.

They want to, hire some
  
additional engineers.

And he even said some of
  
that would be spent on having

engineers triage the issues.

And if you've ever looked at the
  
React repo, you know, that's a thing

that they do not do very often.

So even something like that sounds good.

They want to hire some more people to work
  
on the actual docs and they're hoping to

give money out to communities in some way.

Don't know details on that,

2-vcarl: Tell me more.

1-acemarke: exactly.

Another data point.

So a lot of the plans have to
  
do with the development process

of re the React project itself.

And transparency around that.

Apparently they were even hoping to
  
launch the foundation like a year and

a half ago, and then they realized that
  
like our own in day-to-day development

processes aren't ready for that.

We need to dog food the processes
  
ourselves first so that we're more

ready when the foundation goes live.

And so some of that was you know,
  
actually having docs and plans as

new features are being developed or
  
treating things and kind of like a, you

know, TC 39 staged process approach.

But one of the biggest things that
  
Seth told me directly was that.

Up until now, the React team has had,
  
you know, their, like their weekly status

meetings, and those are purely internal.

First off it was just all the React
  
team working at Meta and then it

was, you know, meta plus Versal.

But those meetings have always been
  
internal, private, and non-visible.

And Seth said that they eventually want
  
to literally open up the weekly React team

planning meetings to the public even as
  
like a, like a Zoom call with no password.

And that eventually, like designated
  
community reps would even be able to

actively participate in those discussions.

So that's a radical change in
  
the development of React itself.

He also said that they're planning
  
to, resurrect or like completely

redo the RFC process, which frankly
  
was kind of dead from the beginning.

It was where random people from the
  
community posted ideas that got ignored

and the React team posted, finished.

things that they planned to ship and
  
then people argued over the naming

and the React team ignored that.

So like historically, the RFC
  
process was pretty much irrelevant

to actual React development.

Now they're talking about making it
  
like a real meaningful discussion

and part of the planning process.

Now, again, like do I know how
  
this is gonna work out in practice?

No.

But I can see the amount of effort and
  
the intent behind the foundation and

the plans that they're talking about.

And even if it doesn't end up going
  
exactly as they or we would hope, I

see good faith and good intentions
  
behind all the work that they're

trying to do around the process here.

So I'm actually very,
  
very excited about this.

2-vcarl: Yeah, that's interesting.

Oh got a lot of thoughts
  
rattling around my head.

'cause that's a lot of stuff that I've
  
looked at trying to contribute towards

the solution of but yeah, I don't know.

It's, I fundamentally, I feel like
  
the problem they're dealing with

is that a lot of people care about.

The outcome, the output, what
  
they make and what React is.

And not a lot of people actually have
  
like the context and the background

to like meaningfully contribute to the
  
advancement of that goal., you know,

to respond to what you just said about
  
like their motivations and their,

what they want to do, I don't think
  
that's ever really been the problem.

They've always had good intent and I
  
even think a pretty clear eye picture of

what the problems are, but I think the
  
problems are really thorny and complex

and the solutions to them are non-obvious.

And even when you have a good
  
solution idea, executing it in

a way that is effective and.

That operates on the, kind of like
  
timescales that React is around four.

It's just really challenging.

Like it's, you know, anyone can spin
  
up a process and run it twice and you

know, maybe that, like you do, you call
  
for comments and you run a community

discussion and round tables and whatever.

But like that plays out over the timescale
  
of like weeks and months and React

seems to plan on the order of years
  
and is now, has existed for a decade.

So, you know, with like there's
  
possibility for its scope to expand from

thinking in terms of years to thinking
  
in terms of, I don't wanna say decades,

but that's the next unit of time.

That's the next order of magnitude.

I hope they can achieve their goals.

I am looking forward to seeing
  
some more roadmap, transparency.

Of some sort actually.

That'll be really great for us, for
  
you and I. That'll would be great.

That'll be a great source of signal
  
that we can then pick apart and

analyze to surely, to much to their
  
chagrin by way of drawing attention

to things that are high context text.

1-acemarke: As opposed to like
  
stalking the open PRS list.

2-vcarl: Yeah.

Right.

Cool.

Nice.

Love that.

1-acemarke: So on that note Another
  
item that I've personally been

involved in is the work on the
  
upcoming React Concurrent Stores, API.

So when React 18 came out the React team
  
included the Uyc external store hook

as the official built-in way for third
  
party libraries like Redux, Zein, Jo Tai,

whatever else to integrate into React.

take an external state update, turn it
  
into a React re-render, and it worked.

But it also had a very intentional
  
design limitation that if you do an

update in the middle of a paused React
  
render, you know, something transition

like, then it bails out of that and just
  
does a complete top to bottom render.

So you're kind of throwing away
  
some of the benefits of React,

being able to pause itself.

And that was because they, they
  
really didn't have a better idea

for how to do that kind of interop.

So this concurrent store's API is
  
supposed to be essentially a new

equivalent to use sync external store,
  
but concurrent transition compatible.

And Jordan Eldridge, who's on the
  
relay team, has been working on

the design and initial prototype
  
IMP implementation for this.

And so he put out a polyfil package that.

Roughly implements the prototype
  
as a standalone library.

And then I've been talking with him
  
about, you know, here's what Redux

would probably need to make this work.

Here's our, our requirements for this.

And so I was able to then take his
  
proof of concept package and put

up a draft PR for React Redux that
  
just swapped out our use selector

implementation to use that instead.

And it basically worked, I mean, just
  
the one test file found a couple edge

cases, but like most of our tests
  
passed, we're not doing anything

transition related in our tests.

But it's good to know that like your
  
baseline standard behavior works.

And this also turned up several more
  
things we'll have to figure out, like.

Quality checks and how do you
  
handle selectors throwing errors?

And we're talking about when can react
  
safely, call selectors, can it delay it

due to batching and things like that.

So also very excited to see the
  
progress being made on this.

A PIA lot of people have asked
  
for external state transition

compatibility, and so this is going
  
to be a big deal for the ecosystem.

2-vcarl: Interesting.

Cool.

I'm just trying to put this in a
  
little bit of context for myself.

So this is a, an exploration of an API
  
for a concurrent store that they've

indicated intent to ship eventually.

1-acemarke: Mm-hmm.

Yeah.

so basically a, a new equivalent
  
of use syn external store, but

minus the sync restriction.

2-vcarl: Got it.

Okay, cool.

Interesting.

you called it a polyfill.

And I see in the blog post it's
  
labeled a pony fill, which I had to

refresh my memory on the distinction.

A polyfill fills in a gap in the
  
platform transparently, and a pony fill

offers the same functionality, but as a
  
standalone module that you have to import.

There you go.

Now you know.

1-acemarke: So one more item
  
kind of related to that.

At React Con Freaky Hanin announced
  
a new Async React working group to

provide support to the, you know, the
  
community and the ecosystem on, you

know, improving the React docs around
  
async behavior, helping libraries

get set up to use these methods.

And so Matt Brophy from the React Router
  
team had a good discussion with Ricky

about how they're trying to handle,
  
using transitions in React router.

So there was a, a good technical
  
discussion about the nuances of behavior.

And then the React router team also
  
put out a pre-release version or

unstable option to enable some of
  
the transition behavior as well.

So starting to see some adoption
  
and this ties into the React team

wanting to see libraries pick up
  
these behaviors like transitions and

action props and, and build them in.

I will say that I had a couple discussions
  
at JS Nation React Summit were some

people were questioning whether making
  
the entire ecosystem change semantics

and behaviors and add props to make
  
the React team happy was gonna be a

good idea or feasible, but we'll see.

2-vcarl: Yeah.

Interesting.

I see a bit of why they, why
  
the core team desires that.

Transitions are definitely like,
  
my understanding of the core

team's incentives and what they
  
care about is ability to use the

platform and things like that.

So given that like transitions are
  
a part of the platform and they are

interested in allowing people to take
  
advantage of platform improvements, I

understand why they would message, in
  
order to use this, the entire ecosystem

must make this change to the patterns
  
they use for compatibility reasons.

But that is very, I don't
  
know, that's a big challenge.

it's hurting a lot of cats
  
who don't necessarily.

Aren't even necessarily aware that
  
there's an attempt to herd being made.

1-acemarke: if you watch Ricky's
  
talk from React con, you know, he,

he demoed switching from like a bunch
  
of manual use effects and loading

states to suspense and transitions.

And then he pointed out, and so now
  
you have a much better experience,

but you also had to do, you know,
  
call start transition and all

your click handlers and so on.

, there's even some painful nuances there.

Because start transition
  
is based on setting a flag

internally for the current event.

Loop tick.

If you have a callback that has an await.

You leave the event loop tick, and
  
if you then want to do another state

update after the await, you have to call
  
start transition a second nested time.

And Ryan Cardo actually pointed out
  
to me that like Ricky has repeatedly

messed this up in his own demos.

It's a very foot gun
  
prone behavior pattern.

And so the combination of like you
  
currently have to call, start transition

yourself, plus trying to get the patterns
  
right is a good argument for let's

just build this into all the libraries.

But that takes time and
  
effort and coordination.

2-vcarl: Yeah.

Right.

Like that was one of my big takeaways from
  
Ricky's talk was, oh, this looks hard.

Which is not the best takeaway if
  
you're trying to convince the whole

ecosystem to move on to something.

1-acemarke: there is a
  
lot of complexity in.

Mental model of React and the kinds of
  
apps we're trying to build, and both

the fact that you now need to keep
  
track of additional API methods that

you have to call and the semantics
  
and when you're supposed to use them,

and the fact that your, your state is
  
now kind of in multiple Schrodinger

box, multiple versions at once.

It's, it's definitely a lot
  
of additional mental overhead.

2-vcarl: Yeah, right.

I'm just looking at in this GitHub
  
thread that you linked, Ricky

says, you know, oh, I think there
  
may have been some confusion.

Here's how you do it for navigations,
  
and it's, you know, function, navigate

to A URL that has start transition,
  
which, you know, wraps set router

state, which then wrap, you know,
  
it's argument is a function that.

I guess returns, A-A-U-R-L.

It's a thunk for set router
  
state in start transition.

In navigate.

I don't know, they're like,
  
that's just complicated.

Like what, why are we wrapping
  
this with so many different

functions just to navigate?

That's uncomfortable.

It feels like the wrong API in some
  
way, you know, like it an API should

obscure complexity and this does not
  
obscure the complexity so Interesting.

I, I want to be able to take
  
advantage of transitions in apps.

'cause that's super great if you
  
can just like, easily convey that

you are here and you're about to go
  
here instead of just going there.

Like, you get a lot of really powerful
  
things that you can do for user

experience and, you know, whatever,
  
all sorts of stuff if you communicate

the transition instead of just
  
updating the current state of your app.

But yeah, I don't, I,
  
I'm not sold on this.

I'm not sold on what I'm seeing so far.

1-acemarke: Okay.

Moving on to the.

Next related chunk of topic.

The Tans stack folks have a bunch
  
of updates that they've put out

both blog posts and versions.

So Tanner put out an article on the
  
State of Tans stack as an organization in

his own work as a full-time open source
  
maintainer for the last couple years.

Also, again heard, you know,
  
heard some of this from, from him

directly at react Summit loosely.

He himself has been full-time supported
  
open source for the last couple years

sponsorships to the TN stack org.

Hand stack libraries are, you know,
  
as we all know, very, very widely

adopted and Certainly query is the
  
standard fritz thing at this point.

Router and is picking up a lot, lot
  
of popularity start is almost 1.0.

And he's hoping to be able to start
  
to bring in some part-time or even

full-time people to hand stack
  
the company in the near future.

Essentially other current maintainers
  
for various hand stack libraries who

would then be able to potentially switch
  
to doing that as their actual job.

So essentially he's been fortunate
  
enough to have this workout for him and

he's hoping to share that ability with
  
other people working on the projects.

2-vcarl: I see says monthly
  
sponsorships for 12 core contributors

and short term contracts for
  
another three to five people.

I guess it's not clear what
  
monthly sponsorships means.

I, my assu, my assumption there
  
would be like their, maybe not full

time, but getting like sign, you
  
know, significant compensation, but

that may not necessarily be true.

1-acemarke: I don't know numbers, but
  
I think at the moment the others are

doing open source and they're full-time
  
and getting some, some stipends, and

in the next couple years he's looking
  
at actually hiring some of them.

2-vcarl: Cool.

Love that.

That's super hard.

Building revenue so that you can
  
actually support other humans

is actually really challenging.

I really like this blog post about,
  
you know, tan Stack for two years.

like this line.

You know, building a full
  
stack framework is hard.

I knew that from watching
  
other teams do it.

Most of them had something I didn't.

Capital Next Gatsby Redwood Remix all had
  
funding companies or acquisition paths.

And that, that definitely is something
  
that feels very different about Tan Stack.

It feels very much like
  
he couldn't not do this.

Like he just, has spent several years
  
working in this problem space and

solving his own problems with the
  
freedom to publish them so that other

people can take advantage of his work.

And then got to a point where it just made
  
sense to invest more effort and take those

a little bit further than they could go.

Absent that level of
  
dedication I, which I, I love.

That's just like, that's, I don't know,
  
finding that kind of work to do for

yourself is what I've been looking for.

And it's really hard to find,
  
and I love that Tanner Wesley

has apparently found it.

And also having 16 partners
  
doing sponsorships is also great.

Like that, that, that may not be
  
capital, but that's, that's great.

That's nice.

having tried to find sponsors myself,
  
like getting 16, it's like, oh shit.

Good job.

That's awesome.

1-acemarke: So it tens Stack DB is a new
  
work in progress package largely being

worked on by Kyle Matthews, formerly
  
of Gatsby, currently of electric SQL.

That is meant to be kind of
  
like a half a sync engine layer

on top of another data source.

And so like one of the common usage
  
patterns for that would be you

wrap it on top of your 10 stack
  
query, you know, API definitions.

And so maybe you've got
  
some endpoints for fetching,

post comments users, et cetera.

But then it presents like a sync engine
  
like interface on top of that, and

it's got a bunch of data flow analysis
  
baked in so that it can do things like

partial fetches or only re fetching,
  
you know, certain pieces of data.

joining.

Essentially presenting like a normalized
  
facade layer over the individual

endpoints so that they act like
  
they're unified almost as a, like a

replacement for a GraphQL style API.

And so they've been working on
  
this and it has integrations with

Tan Stack Query and then Electric
  
SQL and a few other data packages.

And Tanner pointed out to
  
me at React Limit that.

It really just needs an adapter layer to
  
be able to connect to another library and

I could totally build one for RTK query.

And so I was actually briefly
  
playing with that on the flight home.

Haven't had a chance to push it further,

but I'm actually, I'm actually very
  
excited to play with that more myself

because like 10 stack query, we made the
  
decision to make RTK query non normalized.

It just caches the
  
response from the server.

And so if this essentially let us
  
make a normalized layer on top of

our own library without us having
  
to make any further API changes.

That's very interesting to me.

2-vcarl: I'm also thinking about,
  
you know, this is from Kyle Matthews

who did Gatsby, which, you know,
  
notoriously exposed a GraphQL,

you know, layer on top of whatever
  
data sources you wanted to give it.

So just, I'm thinking about how
  
how much of Kyle Matthew's work

could be described as providing

query abstractions over
  
arbitrary data layers with data

1-acemarke: Yeah.

that's a good point.

I, I had, I hadn't even drawn that
  
connection that this is actually

very related to his prior work.

2-vcarl: if you describe this at a
  
certain level of abstraction, this

sounds just like GraphQL, relay Gatsby,
  
a bunch of other stuff, but I do see

the niche that it occupies and how
  
it's distinct from those projects.

it's kind of like GraphQL except
  
instead of the network boundary,

it's like the component to data
  
store boundary on your client app.

Which that's useful if you can, like
  
what you just said about how you

don't normalize in RTK query I've
  
landed on that as being generally a

good architectural decision to make
  
in applications because like if you

start doing data transformations.

You know, bespoke data transformations
  
per endpoint, then it becomes really

hard to change those endpoints.

If, if you're changing the underlying
  
data, then you've gotta change

all the code at the same time.

Whereas if you just take whatever
  
the API gives you and then write like

a transformer on top of that, then
  
it's just you, you add a layer of

abstraction for yourself that gives
  
you a little bit more flexibility


... (content truncated)

Related notes: [[Server Components]]
