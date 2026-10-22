---
type: "twir-recovery"
issue: 294
item: 17
source: "https://share.transistor.fm/s/55d1846a"
final_url: "https://share.transistor.fm/s/55d1846a"
retrieved: "2026-10-22T11:30:07+00:00"
original_note: "frontend/raw/twir/294/articles/17 - This Month in React \u2013 July 2026 Podcast.md"
editorial_review: "pending"
truncated: true
---

Original intake note: [[../articles/17 - This Month in React – July 2026 Podcast|This Month in React – July 2026 Podcast]]

# This Month in React

Carl: Hello.

Thank you for joining us for the July
  
edition of This Month in React, as we

recap what's been going on with React
  
Native and other things across the web.

We are coming to you live
  
from Reactiflux, the place for

professional developers using React.

And I'm Carl.

I'm a staff product developer and
  
freelance community leader here at

Reactiflux, where I run community programs
  
like these events and build tools like

help keep the community operating.

Mark: Hi, I'm Mark.

My day job is replay.io, where
  
we've built time travel debugging,

are working on autonomous QA, and I
  
get to do all kinds of awesome time

travel-powered React analysis tools.

And outside of that, I am still
  
doing Redux stuff, and I'm actually

finding the energy to do a fair amount
  
of that right now, which is cool.

Carl: Nice.

Heck yeah.

Hell yeah for finding the energy
  
to invest in a project you love.

Mark: Yep.

I'm also actually back at home
  
after, like, two and a half months

of almost nonstop conference travel.

Carl: We were saying in prep, we
  
have kind of a grab bag this month.

There's not, like, one big thing
  
to discuss, but yeah, we're

gonna get into a couple things.

Uh, obviously there's been more
  
security stuff and new releases of

major projects, like TypeScript 7,
  
which we've discussed, like, four

times already, but y- it's here.

Yay.

We also are gonna get into some
  
open source governance questions.

There's been some developments
  
on the React Foundation.

And l- kind of out of left field at
  
the same time, Poimandres a cooperative

doing open source around Three.js.

It also published some governance work.

So yeah, we're gonna get into it.

But first, the first new release.

Vite+ from Voidzero is in beta now.

Mark: It's not paid anymore.

Oh, okay.

They dropped that.

I think they dropped the paid part
  
even before they got bought out.

They initially said it was paid.

Then they said, "No, no, we'll, we'll
  
make Vite+ free. We're gonna build

our own server runtime layer on top
  
of Cloudflare," and then Cloudflare

just bought the entire company.

So- Great … Plus itself, as far
  
as I know, is going to be entirely

free at this point multiply.

But it's just the Void Zero company
  
had been paying a bunch of people to

build out OXC, you know, that whole
  
layer of parser tooling, partly to use

in the Rolldown Rust-based bundler.

The latest version of Vite uses
  
Rolldown, but then there's all these

other Rust-based tools related to that.

And so Vite Plus is a combination
  
of we have pre-configured all these

different tools into one super package,
  
as well as added some additional

layers of functionality on top of that.

So it's essentially supposed to be
  
an entire JS development suite in

a box, sort of akin to what Rome
  
was promising a few years ago.

Carl: Cool.

Love that.

Mark: Meanwhile, as mentioned, we have
  
talked about this repeatedly, so I

don't have to go into a lot of details,
  
but TypeScript 7 is finally live.

Hooray.

This is the Go implemented native
  
implementation of the TypeScript

compiler that is supposed to be
  
up to 10X faster, so the actual…

If you install the actual TypeScript
  
package at latest now, it is actually

built with Go under the hood.

The biggest caveats here at the moment, as
  
we've again talked about, the programmatic

TypeScript API essentially does not exist
  
in version seven, because the API had

been partly official, partly unofficial
  
before that And lots of different tools

had various dependencies and needs.

A lot of them had hacked together
  
solutions in the past, and so the

TypeScript team said, "Okay, we
  
know the compiler itself's working.

We're gonna get that out the door.

We want to take our time and carefully
  
consider what a better and proper public

API would look like to support all the
  
different use cases people have come up

with, and we'll get that out the door in,
  
like, a version 7.1 or 7.2." so there is

some, there is an update on that front.

They've put up a PR for something
  
they're calling content mappers, and

the way I'm understanding this is that
  
for other languages like, say, View or

Angular that have templates, you want
  
to be able to type check the templates.

The TypeScript compiler handles
  
JSX, which means React kind of

got special treatment there.

But how can other languages
  
actually get similar behavior

for non-TypeScript syntax?

And so this content mappers proposal
  
from the TS team is a way that

they're hoping they can address
  
essentially a plug-and-play conversion

of other syntax into something
  
TypeScript itself can type check.

So there, there may be other API
  
integration things that they're looking

at as well, but this feels like it's
  
a, a good step in that direction.

And in the meantime, a bunch
  
of teams are doing things with

integrating with TS Go in hacky
  
ways you're not supposed to anyway.

Johnson Chu, who I think built the
  
Alien Signals library, and I think

also works on the Vue Volar language
  
extension, if I've got my connections

right, put together a package called
  
the TypeScript Native Bridge, which

is supposed to help polyfill some of
  
the, I think, the language server-type

integrations so that they're faster.

And then the OXC folks have been doing
  
their own hacky native TypeScript

integration to try to enable typed
  
lint rules within the OXC linter.

And so the typed linting support
  
has just gone stable as well.

So, lot of improvements around
  
TypeScript compiling and checking

in the entire tooling ecosystem.

Carl: Interesting.

Yeah, type-aware linting
  
would be a really big win.

I've wanted that a number of times,
  
and we've never really gotten there.

Mark: TS ESLint has them, but it requires
  
a lot of slower integration and running

full-blown standard TS type checking.

Carl: Cool.

Can you talk about this
  
install time security, Mark?

Mark: Due to the entire series of supply
  
chain attacks that we've seen happen over

the last year, one of the biggest issues
  
has been that packages are allowed to

run scripts after install by default.

And so you're just arbitrarily
  
executing remote code on your

machine with your privileges.

And so several other package
  
managers like pnpm had switched

to disallowing that by default.

And so npm 11 still allowed that,
  
but they started adding the options

to disable running scripts by
  
default and preparing things.

So npm 12 actually does flip the
  
switch on a lot of those options.

So npm 12 no longer runs
  
post-install scripts by default.

By default, it does not allow a Git
  
repo URL as a valid dependency, and

it has a couple other options that it
  
turns off by default to enable security.

I also saw that GitHub is changing
  
Dependabot, so it now has a cool

down by default, so it won't
  
install new deps until, like, two

or three days after they came out.

So we are very, very belatedly, as
  
an ecosystem, finally learning some

lessons we probably should have learned
  
many years ago, and changing some of

the default behaviors of our tools to
  
try to cut down on the blast radius

of some of these malware releases.

Carl: Yeah.

And we've covered some of that
  
in recent episodes, so I, let's

not rehash it entirely again.

Mm. Yeah, definitely some,
  
uh, long overdue changes here.

Mark: Yep.

Carl: As well as, I guess, in w-
  
security tweaks for server components

that were just released this week.

Mark: Yep.

Looks like another denial of
  
service attack possibility.

Carl: Okay.

Mark: So just bad, bad… So
  
not remote code execution, but

bad input freezes the server.

Carl: Okay.

Can't have that.

That's a denial of service vector.

Okay, well that's the, like,
  
brand-new releases we have.

There's some other new stuff, but a
  
little bit, like, less, you know…

N- we're not gonna start with it, but
  
we're gonna do that towards the end.

Main content.

We are gonna start with the React
  
org updates, and we're gonna frame

this against the backdrop of, like,
  
open source governance generally.

There have been some changes
  
announced by the, uh, you know,

React Foundation within the Discord.

There's been, you know, there's
  
been a, a couple of visible

changes to the website and PRs to
  
the actual governance repository.

Mark: I specifically had been
  
griping, I think in the last two

months, that I have no idea who's
  
even on the React team anymore.

And I don't know whether they literally
  
heard me or whether this was just,

you know, kind of coincidental timing.

But they did a significant update to the
  
existing React team page on the website.

They updated it both with, you
  
know, current people involved

in moving some folks to more
  
of, like, an emeritus status.

But the team page now actually
  
reflects a new team structure that is

coming out of this React foundation
  
itself, where there's, like, a set of

different working groups for topics
  
like, you know, server components

and compiler and, and other things.

But then there's, like, a leadership
  
council that appears to be essentially,

like, a, a representative from
  
each of those groups, as well

as possibly a couple others.

So I still don't, still don't have
  
a lot of details on the actual

responsibilities, but we're seeing some
  
visible evidence that they're working

on the organization process here.

Carl: Interesting.

Cool Curious, the reason I'm in the
  
Discord is 'cause, 'cause somebody reached

out asking if I wanted to help with
  
community, and so now seeing a bunch of

people listed as on the Docs and Community
  
Working Group and nobody reached out to

me makes me feel like I got left out.

But that's okay.

I'm an independent actor, unaffiliated.

Mark: The list of working groups is, uh,
  
server, DOM, fiber, docs and community,

compiler, DevX, and React Native.

Carl: Yep.

I am s- slightly surprised to see
  
React Native generally put into its

own single group, because they're
  
a- at least as large as React.

I would say technically, you know,
  
problem space they operate within

is larger than React itself.

So I'm slightly surprised to see
  
it positioned as a single working

group under the umbrella of React.

But I guess, you know, there's
  
other organizations that are more

meaningfully invested in React
  
Native, so, uh, maybe this is more

of, you know, division of labor.

This is the pipeline more
  
than the umbrella, per se.

Mark: It's also worth noting that
  
there, there's like seven or eight

people on the leadership council,
  
which I guess, you know, matches

roughly the number of working groups.

And then the working group members section
  
is at least a good 20-plus people long

for current people, and then there's a set
  
of advisors and a set of emeritus people.

So there, there's a good 30 to
  
35 names listed on this page.

Like, it's not just, you
  
know, two to three people.

Carl: It's quite a long list,
  
and it is much more specific.

I don't know.

We just complained about this, and
  
it's really nice to see a, like,

full refresh that looks reliable.

That's nice.

I was reading a little bit of the charter.

It is pretty interesting.

It looks like they're quite earnestly
  
trying to make this, like, you know, open

participation, and I've thought a lot
  
about governance questions and stuff like

cooperatives and, like, how do you do…
  
If you have multiple people with opinions

about what to do with a project, a shared
  
good, I don't know, it's really hard, it's

really hard to do that right in a way that
  
allows people to feel represented and like

they have agency in the overall system.

So I appreciate the challenge
  
of what they are trying to do.

It is difficult to set up a general
  
organization that lets many people

in many walks of life feel heard.

I like the, the way they scoped it
  
as, you know, "the mission and scope

of the project is to develop and
  
maintain React and associated open

source software. The leadership council
  
will be responsible for technical

oversight of the open source project."

You know, like, this is… I can
  
tell that from reading this, that

the way that they are discussing
  
responsibilities and constraints and

decision-making and work delegation,
  
like they are very meaningfully

trying to make this open participation
  
And with a high bar of quality.

Yeah.

This is, you know, primary
  
source kind of stuff.

This is-- The commit on this
  
charter.md document is two days

old, so this is, like, brand new.

No one has really been…
  
This is a- as yet untested.

The processes described here are
  
not currently fully implemented.

But yeah, what I see here
  
looks quite good to me.

I like it.

Mark: And to be clear, like,
  
the, the repo's public.

I mean, I can look at this
  
information right now.

I don't-- The- there hasn't been,
  
like, a formal team announcement of the

leadership council and the charter per
  
se, but clearly they're trying to put all

the pieces together to be able to say,
  
"This is the way we're gonna do things."

Carl: Yes.

Okay, I don't see-- I heard rumor of a,
  
uh, pending blog post, but I, I don't

see it yet, so… But yeah, I expect that
  
there should be some broader announcement

of what this is and what it means and
  
what their intentions are coming soon.

But what I see here looks quite good.

I like it.

It seems like a good effort.

Mark: Like I said, I, I griped a
  
little bit about the lack of visible

progress in the last few months, but
  
clearly what we're seeing here, and

even what I'd heard about the amount of
  
effort that was needed to just create

the foundation in the first place.

Like, there is a lot of effort going on
  
behind the scenes, clearly, and there's

a lot of good faith intention behind
  
what they're trying to accomplish.

Like, this is not just for show.

Carl: Yes.

Agreed.

Mark: One of the longstanding complaints
  
about- You know, the community with

React and React with the community has
  
been, they do most of their coding work

in public, but there's also some that
  
happens behind the scenes in private.

And historically, they've had the
  
problem that any time they push

a draft PR, people jump on it.

It's like, "Oh, React is working on this
  
new feature," and they start writing

blog posts and tutorials and everything.

And so that has actually made the React
  
team less likely to show their work in

public, because a lot of times it is an
  
experiment or a prototype, and there's no

guarantee that this will even ship at all.

So there's been discussion on both sides
  
that it would be really helpful if they

tried to follow a TC39 stages model, where
  
it's very clear that we are working on

concept X. It is a stage one prototype, a
  
stage two, like, we think this is likely.

Stage three, this is probably gonna ship.

Stage four, it's ready.

That kind of thing.

  
saying that they've been trained

to follow that model themselves
  
internally and had some success with it.

But essentially, they're trying to prove
  
to themselves that they can actually work

using that approach before they fully
  
publicly commit to doing that and making

the scale, the stages and progress public.

Carl: Yeah, and we've talked a couple
  
times in past episodes about the

general challenges, like the tensions
  
there of them earnestly wanting to

work in public and having repeatedly
  
tripped over the same problem every

time they've tried to of, you work in
  
public and then you get just a bunch

of yahoos talking over you as you're…

You know, the, the people who don't,
  
people who haven't seen the work that went

into the current state that is actually
  
now public and end up just re-litigating

all the same issues or, you know.

So there, there are a lot of very
  
real challenges there, and I earnestly

appreciate the continued exploration of
  
how to make that actually functional and

work well for as many people as possible.

Mark: One other small but related item.

You know, there are a bunch of React
  
folks at Vercel at this point, and

Guillermo just announced that Pete Hunt
  
and Nick Schrock have both joined Vercel.

Pete Hunt was one of the first advocates
  
for React at Facebook at the time.

He did one of the more famous talks that
  
helped get React off the ground in public.

He had spent the last few years,
  
I think, working at a company

called Dagster that just got
  
acquired, and so this is presumably

his chance to move on from that.

But the announcement is that
  
he'll be leading the frameworks

group in Next.js itself.

And then Nick Schrock was instrumental
  
in the development of GraphQL as a spec

at Meta, and he is gonna be working on
  
Agent DX or something along those lines.

So Ver- Vercel continues to scoop
  
up more and more of the folks

who were involved with React at
  
Meta at some point in the past.

Carl: Yeah, I'm curious to see about
  
the interplay between Agent DX and

the GraphQL, because increasingly
  
so, what an agent needs to do with an

arbitrary server is get the data it
  
wants And that's what GraphQL's good at.

Hey.

Yeah, I'm skeptical of MCP.

MCP is gonna die.

Actually, no, it's not gonna die.

It's gonna, it's gonna live forever
  
the way that, like, SOAP does.

Yeah.

It's gonna be an early exploration of
  
a, an A- API, and I think it's going

to be widely hated in five years.

Calling it now.

There's my mark on the yardstick.

Related to the org updates and open
  
source governance more than that

last update, though, Polymanders
  
has published their charter as well.

It's been around for, I would
  
say, at least eight years,

maybe 10 years at this point.

Oriented around Three.js and 3D
  
rendering on the web, I think

is a fair characterization.

Mark: A, a number of, number of folks
  
there have prior experience in game

development one way or the other.

Sort of a set of artists
  
collaborating to build related

things together kind of a vibe.

Carl: Yes.

Yes.

Right.

We all have a shared interest,
  
a shared passion in this.

You know, I open their website and it's
  
full of WebGL demos with, you know,

parallax and physics and refraction
  
and, you know, translucent interact…

You know, so it's, that's generally
  
what they're anchored around.

It's a bunch of artists doing art on
  
the web in different ways, playing

with visual technology on the web.

And I- when I say playing,
  
I don't mean to diminish.

I mean earnest play in
  
the sense of exploration.

Mark: It's also worth noting that
  
was originally developed by one of

the, one of the earlier folks in that
  
org, and I b- and I think Z- possibly

Zeustin and Jotai and Vultio are
  
still owned by that org on GitHub.

Carl: Yeah.

Zeusstand, React Three Fiber,
  
React Spring, Jotai, Volto, Drei.

Mark: Some very solid well-known
  
libraries in the React ecosystem.

Carl: Yes.

Yeah.

Tons and tons of well-known projects.

Yeah, so like, I hope that
  
didn't sound diminishing because

I do not mean to diminish.

These are talented, respected.

But yeah, so they, they… As a
  
point of comparison, these other

technical, highly technical, highly
  
skilled folks have also published a

charter, and I think the React one is
  
a little bit more clearly articulated.

I appreciate this charter.

It is, you know, it discusses the
  
core principles and what it means to

be a member and how decision-making
  
works and how they adopt projects.

But, you know, it's like the
  
membership is one paragraph and

says, "What are the working roles?
  
There's no strict definition of a

working role." So it's more vague.

There's less buttoned down there.

Which makes sense.

You know, this is an open source
  
collective of artists who are very

talented, and they're very talented
  
in more along technical things.

Like whereas people coming from Meta are
  
much more experienced in the corporate

aspect of precision of language and
  
clarity of, you know, communication

and definitions in documentation like
  
operating agreements and charters.

So i-it's, I'm positioning these
  
in reference to each other, mostly

because of the coincidence of
  
timing of them having both come

out at the same time, and because
  
I think that's a really interesting

and valuable comparison to draw.

What does it look like when a corporation
  
helps found a foundation versus what

does it look like when artists as part
  
of a collective do the same thing?

These are contrasting ideologies creating
  
something, and these are two examples.

I think it is fascinating to look at both.

Mark: So let's say they wanna work
  
on a, uh, React Three Fiber version

10 to be able to make use of WebGPU
  
and make it more AI agent friendly.

They'd like to work on their
  
own design system for common

look and feel and behavior.

And then they also want to
  
work on better quality text

rendering in WebGL, apparently.

Carl: Okay.

Cool.

I appreciate that.

Yeah, text rendering is really hard
  
because it's actually insane when you

start drilling into the details of how
  
glyphs are rendered on your screen.

F- 'cause like for instance, if you're on
  
a low DPI monitor, they will do all sorts

of crazy sub-pixel rendering in order
  
to make it look, you know, 20% crisper.

Which ironically actually Apple gets
  
flack for now because all of their

displays are high DPI, and so they
  
don't do those anymore, and then it's

really hard to get crisp icons on OSX.

Mark: Yeah, anytime a text rendering
  

end up reading it, 'cause there,
  
there's some deep stuff there.

Carl: Yes.

If you see text rendering or Unicode
  
in a blog post title, like I highly

recommend checking it out, because you
  
probably take it for granted, and it's

probably like insanely complicated.

Text rendering in WebGL is likely
  
going to be a fascinating project

that deserves its own full initiative
  
from a, uh, collective of expert

engineers with visual experience.

Cool.

Okay, let's move on a little bit.

Recently, we've been covering more
  
and more React-alike projects.

I'm gonna coin it, I'm calling
  
it, these are React-alikes.

Yeah, we've got a new one,
  
Octane, from Dominic Ganaway.

Mark: Yeah.

Okay, so there's, there's a
  
whole causational chain here.

So Dominic started off by creating
  
a library called Inferno back in

2014 or 2015, and the idea was React
  
similar, but much, much faster.

Whereas Preact was, say, like React, but
  
only for the web and as small as possible.

So, like, there was like a Inferno-React
  
compat library that tried to fill in

some of the differences in behavior,
  
but the whole point of Inferno was let's

make something very small and very fast.

Dominic joined the actual React
  
team and was there for a few years.

He left Meta.

He, I believe, worked with Rich Harris in
  
some of the Svelte 5 stuff for a while.

And we actually covered Dominic just
  
in the last couple months because he

recently released a- another different
  
framework called Ripple, which tried

to pull together a few different ideas,
  
and he also released a JSX improvement

language called TSRX, and then
  
iterated on its design a couple times.

So he's back, and he has another new
  
framework called Octane, and the sales

pitch for this one is very intriguing.

It's essentially what if we took
  
React's syntax and pretty much almost

all the semantics, but we have a
  
compiler, and thanks to the compiler,

we can eliminate the virtual DOM, we
  
can get rid of the rules of hooks, and

actually have, like, conditional hooks,
  
and we don't need a dependency array.

And so there's actually a, a very strong
  
connecting line through all these things.

It's like what if React,
  
but better in certain ways.

Svelte was all compiled.

TSRX is a compiler syntax layer.

So there's a lot of different previous
  
threads of work that are getting

pulled together in this project.

Now, I took a look at the
  
commit history for this project.

It looks like he only started working
  
on this, like, a month or a month

or and a half ago, thereabouts.

You can pretty s- quickly see the commit
  
messages going from, you know, first test,

try this, oops, broke, fix, whatever, to,
  
like, very quickly building up the pieces

And he's officially launched it in some
  
sort of like, well, I don't know what

the actual version number is, but like he
  
feels it's ready enough for people to try.

The implementation has
  
obviously been AI built.

Here's where it gets interesting.

So he just joined OpenAI to
  
work on their own web front end.

I believe he'd been using
  
Claude To do the implementation.

But in some discussion on Twitter, he
  
said, like, "I am actually seriously

pushing Octane forward because
  
OpenAI heavily relies on React in

their web stack, and we need to
  
essentially, like, find ways to make

that faster and more optimized."

So there's both the personal history of,
  
"I am very familiar with React and its

ecosystem, and I'm trying to push it to
  
the next level, and now I have a day job

that will fund me to do that, and also g-
  
they get to benefit from them." One other

interesting technical point out of this.

So it's React syntax and almost React
  
semantics, but it's totally different

packages, which would normally
  
mean that there's no ecosystem out

of the box because there are no
  
packages that import from Octane.

There are packages that import from React.

So if you look at the Octane repo, there
  
is an entire subfolder where he has

programmatically built adapter layers
  
for commonly used React libraries to

make them work with Octane, ranging
  
from component libraries to, in our

case, React Redux and Redux Toolkit.

Essentially, look at the actual
  
source code, create a port or thin

adapter layer that imports from Octane
  
instead, and I assume they work?

So it's brand new and no one's using
  
it yet, but this looks very genuinely

fascinating on multiple levels.

Carl: The thing I'm observing on the
  
homepage in the announcement, you

know, code snippet, it looks extremely
  
familiar, except for there's no return

in this function, which is strange.

Mark: That'd be the TSRX.

Carl: Right.

Mark: In fact, n- notice if you look
  
carefully, there is a, there's an @ symbol

right before the opening curly brace.

That's apparently the TSRX symbol
  
that this just auto-returns.

Carl: See, I don't like that.

Th- th- those feel like personal
  
preference decisions that

don't actually really matter.

It reminds me of, like, CoffeeScript.

That was so mixed.

It was so perfect.

They had the single versus the
  
double arrow function, which would

change the behavior of binding this.

You know, a hyphen greater than did normal
  
function binding, and equals greater than

bound this automatically to the function.

And people loved that so much that we
  
pulled it into this language, and that's

where we got arrow functions from.

And I don't think that this at symbol
  
justifies it to the same degree.

Like, I don't think implicit return…
  
Like, JSX had an implicit return, too.

You know, it was like you
  
add braces or you don't.

And so adding a new symbol to
  
the language in order to change

the behavior of something that we
  
already have a, a variable on, I

think is gonna be a distraction.

I think that's a, I think that's
  
an API failure, I would say.

Like, the rest, plenty of these, you
  
know, the rest of these all seem…

It bothers me that it's so close
  
to being familiar, while m- making

a, a dramatic departure like that.

Implicit return is a big difference.

Mark: It's worth noting that it
  
does support both existing JSX

syntax and the new modified TSRX
  
syntax, so it is pick and choose.

Carl: Skeptical.

It's interesting.

Overall, I think this is a really good
  
idea and a good direction to explore.

I'm reacting strongly to that small note
  
because I think this is good to explore,

and that feels like a, that feels like a
  
unintentional self-injury that will make

it more difficult for this to succeed,
  
I think is why I'm calling it out.

But yeah, I think that's really cool.

Like, you know, boom, they
  
got a use effect in an if.

Can't do that in React.

So conveniences like that seem
  
really cool, and I'm excited to

see if this works, and I hope
  
that it doesn't introduce foot

guns that make it less successful.

Mark: Yep.

That ties into the next bit conveniently
  
because we organized it that way.

I think partly in, in response to
  
the release of Octane and some other

related discussions, Ryan Carniato had
  
a couple tweets that relate to this.

So, like, you know, one of Solid's
  
selling points has been that it

mostly looks like it re- like React.

It uses JSX syntax.

It is JavaScript inside.

Okay, the state and the effects are
  
different, and the getters are different.

But, like, it looks like React
  
much more than Angular would be.

So Ryan had a couple tweets where he was
  
commenting that, you know, at this point,

he feels like the… React is commonly
  
used largely because of complacency.

It's the modern no one got fired
  
for choosing IBM kind of a thing.

And then he also had a, a tweet
  
commenting on, like, do people just

not feel that there's going to be
  
any more innovation in front end?

So I mean, like, he's been talking about
  
a number of these points for a while,

so, like, there's not necessarily,
  
like, new changing details there.

That, we've talked 

... (content truncated)
