---
type: "twir-recovery"
issue: 301
item: 7
source: "https://mattrothenberg.com/notes/classname-considered-harmful/"
final_url: "https://mattrothenberg.com/notes/classname-considered-harmful/"
retrieved: "2026-10-22T11:30:12+00:00"
original_note: "frontend/raw/twir/301/articles/07 - className Considered Harmful.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/07 - className Considered Harmful|className Considered Harmful]]

# className Considered Harmful

Most component libraries accept `className` everywhere. I get it. A team needs a special case, or thinks it does, and `className` lets them ship without waiting for a new variant or asking anyone. Marketing wants a pill-shaped button. Logs wants a shorter select in a dense toolbar. Settings wants green switches. Each of those is an override: a class passed to a system component to change how it looks. Other teams copy those versions, and after a couple of years the components look like this:

As shippedAs used

24months

64overrides

7teams

Button

Save

Saveh-6 text-xs

Saveh-9 px-5 +1

Saveh-6 text-xs

Saverounded-none

Saveuppercase

Saveh-9 px-5

Savebg-transparent

7 looks

Input

Name

Name

Name

Nameborder-2

Nameborder-2 +1

Name

Nameh-9 +1

Nameborder-2

4 looks

Tabs

AllLive

AllLivebg-muted +1

AllLive

AllLiveuppercase +1

AllLiveborder-b-4 +1

AllLiveborder-zinc-500 +1

AllLive

AllLiveborder-b-4

5 looks

Radio

Yes

Yesuppercase

Yesfont-mono +1

Yesfont-mono +2

Yesfont-mono +1

Yesflex-row-reverse +2

Yessize-5

Yesborder-4 +1

8 looks

Switch

bg-emerald-500 +2

\*:size-4 +2

h-6 w-11 +2

\*:size-4 +1

bg-zinc-500 +2

h-6 w-11 +2

h-6 w-11 +1

8 looks

Six components from one design system, eight places each, in a made-up product. Each override is labeled with its class.

This also makes change management hard. Callers end up relying on implementation details that should have been private, often without knowing it. That is [Hyrum’s Law](https://www.hyrumslaw.com/):

> With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.

One team used `*:size-4` to make the switch’s knob bigger, and that class only works as long as the switch’s markup stays the same. Change the markup and their switch breaks. You might even say the markup is load-bearing ![](/notes/classname/claude-thinking.gif). With `className`, every class and element inside a component becomes part of its API.

Design tokens help. They limit which colors and sizes a team can pick, but teams can still combine them however they like. Here is a `Badge` with a soft-green `success` variant that three teams changed using only approved tokens:

Projects

api-gateway

Updated 2h ago

Active

Billing

Invoice #2291

$1,240.00 · Oct 1

Paid

Settings

Two-factor auth

Authenticator app

Enabled

Deploys

Production

v2.14.0 · us-east-1

Live

Projects

api-gateway

Updated 2h ago

Active

Billing

Invoice #2291

$1,240.00 · Oct 1

Paid

Settings

Two-factor auth

Authenticator app

Enabled

Deploys

Production

v2.14.0 · us-east-1

Live

Projects

<Badge variant="success">

Billing

<Badge className="px-2.5 bg-success-subtle text-success">

Settings

<Badge className="bg-success-solid text-on-success rounded-sm">

Deploys

<Badge variant="success" className="px-1 text-[10px] font-bold">

All four badges are on brand: every color and size comes from an approved token. They are still four different badges for the same status.

## How some libraries limit it

className

Custom CSS can't override the components.

Instead

Props like tone and variant. The merchant's branding sets the rest.

className

Not accepted, except on Box.

Instead

Box props for layout and spacing.

className

The recommended lint config errors on any className, even on a div.

Instead

An xcss prop that takes @atlaskit/css styles, which only allow token values.

<Box xcss={styles.root} />

className

UNSAFE\_className still exists, but is strongly discouraged.

Instead

A styles prop for layout, spacing, sizing, and position. Colors and internal padding can't change.

<Button styles={style({marginStart: 8})}>Edit</Button>

className

Renamed to UNSAFE\_className, “a last resort.”

Instead

Style props for layout, spacing, and size.

<ActionButton marginStart="size-150">Submit</ActionButton>

className

Accepted everywhere, and the caller's classes win.

Instead

You own the source, so you can edit the component itself.

className

Accepted everywhere. The components are unstyled, so className is how you style them.

Instead

className can be a function of the component's state.

<ListBoxItem
 className={({isSelected}) => isSelected ? 'selected' : 'unselected'}>

Roughly strictest to loosest. Each name links to that system's styling docs, and the snippets are copied from them. Atlassian deprecated its older xcss() function in favor of @atlaskit/css.

In Polaris and Braid, a component’s look only changes through its props, so if you need something the props don’t cover, you wait for the library to ship it. With `UNSAFE_className`, a team can still override anything, but the name makes it obvious in code review and easy to grep for. In React Aria and shadcn/ui, you write the styles, so keeping them consistent is up to you.

No design system team can know every case the teams using it will run into, so some flexibility has to live somewhere. Polaris and Braid keep it in the library. `className` leaves it with the team using the component. I think picking between those is mostly a decision about people: how quickly the design system team can ship a new variant, and how long the teams using it can wait. Whatever your library does, you still need to see how it’s being used.

## Trust, but verify

Start with an inventory: every `className` passed to a component from your design system package, plus `style` props and CSS that targets its markup, grouped by component and class. Before you change a component, this tells you what might break. It also tells you when a new variant is taking shape that nobody has raised with the design system team yet. That kind of drift is useful. Overrides are often the first place a team’s unmet need shows up.

A scary prop name is the cheapest way to get this list. `UNSAFE_className` only exists on system components, so a text search finds every use. React did the same thing to its own internals, which shipped under this name until React 19:

1import React from "react";

2

3const internals = React.\_\_SECRET\_INTERNALS\_DO\_NOT\_USE\_OR\_YOU\_WILL\_BE\_FIRED;

The classes that repeat across teams matter most. If five teams add `rounded-full` to `Button`, that might be a variant worth adding. If five teams add `-mt-px` to `Checkbox` to line up its label, that might be a bug nobody reported.

A lint rule keeps new overrides from getting in. Atlassian’s rule errors on any `className`, with this message: “Avoid `className` because it invites the use of unsafe global styles and is impossible to determine via local tooling.” [shadcn/lint](https://github.com/shadcn-ui/lint)’s `no-restyle` rule reports classes outside the categories you allow, such as layout.

Think of it as CI for your design system. On every pull request, compare the override inventory with main and post anything new to the team that manages the design system. Blocking the pull request is the strictest option, and depending on how many overrides already exist, it can stall a lot of teams at once.

tkato pushed 1 commit 3f9c2e1 Add invoice dialog

ds-auditbotcommented 2 minutes ago

3 new overrides on design system components

Not blockingA copy went to #design-system

Override

Repo-wide

Suggestion

<Dialog className="p-0">

billing/InvoiceDialog.tsx

Consider `padding="none"`

<Badge className="px-1 text-[10px]">

settings/StatusBadge.tsx

Consider a `size` prop

<Banner className="mb-2">

workers/QuotaBanner.tsx

Use `gap` in the parent

mattrothenberg added the needs-variant label

What the audit might post on a pull request. The numbers are made up. The repo-wide count is the useful part, because it shows a missing variant while it's still cheap to add.

## Where I’ve landed

[Kumo](https://github.com/cloudflare/kumo), the design system I help maintain at Cloudflare, accepts `className` on most of its components. `Text` is the one that doesn’t: it only takes `DANGEROUS_className` and `DANGEROUS_style`. I’d like to rename it on every component. Then one grep finds every override:

$ rg DANGEROUS\_className apps --glob '\*.tsx'

apps/marketing/src/Hero.tsx

41:<Button DANGEROUS\_className="rounded-full">

apps/marketing/src/PricingCard.tsx

19:<Text as="h3" DANGEROUS\_className="font-bold">

apps/logs/src/Toolbar.tsx

118:<Select DANGEROUS\_className="h-6 text-xs">

131:<Button DANGEROUS\_className="h-6 text-xs">

apps/settings/src/TwoFactor.tsx

88:<Switch DANGEROUS\_className="\*:size-4">

apps/billing/src/InvoiceRow.tsx

64:<Badge DANGEROUS\_className="px-2.5 bg-success-subtle text-success">

apps/deploys/src/Environment.tsx

27:<Badge variant="success" DANGEROUS\_className="px-1 text-[10px] font-bold">

apps/access/src/PolicyForm.tsx

203:<Checkbox DANGEROUS\_className="-mt-px">

`Text` has worked this way for a while. `font-bold` showed up in the grep often enough that `Text` got a `bold` prop and our design guidelines got a rule against the override.

I haven’t opened that pull request yet.

Rename `className` to `DANGEROUS_className` on every component #4821

Draft

mattrothenberg wants to merge 1 commit into `main` from `rename-classname`

Conversation0

Commits1

Checks0

Files changed1,284

Showing 1,284 changed files with 3,917 additions and 3,917 deletions.+3,917−3,917

Large diffs are not rendered by default.

If you’ve made this change on a library that was already in use, I’d like to hear how it went.
