---
type: twir-item
issue: 260
item: 10
item_type: item
date: 2025-11-26
source: https://jjenzz.com/judging-apis-by-syntax-is-misleading/
tags:
  - "APIs"
status: auto
quality: keep
---

[[2025-11-26-TWIR-260|Index]]

# Item 10: Why Judging APIs by Syntax is Misleading You

Source: [https://jjenzz.com/judging-apis-by-syntax-is-misleading/](https://jjenzz.com/judging-apis-by-syntax-is-misleading/)

Summary:
This article argues that APIs with similar syntax can operate at very different abstraction layers, affecting portability, constraints, and capabilities. Using styling libraries and the "use client" directive as examples, it emphasizes the importance of understanding the underlying layer rather than judging by surface appearance.

Key takeaways:
- APIs that look similar may have very different runtime, build-time, or framework assumptions.
- Layer differences impact portability, developer experience, and integration options.
- "use client" is a low-level primitive, enabling frameworks to build consistent behaviors on top.
- Evaluating APIs by their abstraction layer leads to better architectural decisions.

Recommendation:
Summary sufficient

Content:
# Why Judging APIs by Syntax is Misleading You

Okay, the title is a bit hooky, but the idea behind it is feeling more relevant than ever. We often see new APIs with similar goals to pre-existing APIs, which leads to a familiar reaction:

> "I know what that is. I can already do that today. Why would I need this new one?"

This reaction is natural. But these APIs often behave very differently underneath. What matters is not just how an API looks on the surface, but also the abstraction layer it belongs to. That is often where the ah-ha moment lives.

Once the layer becomes clear, it becomes easier to understand why two things that look identical on the outside can offer completely different capabilities.

To set the scene, I'll use an example using styling libraries. This isn't an article about styling though, it's really about the assumptions that similar APIs do the same thing.

## Understanding Layers Through Styling Libs

These three tools provide a useful comparison because their APIs can look similar whilst living in very different abstraction layers.

### Restyle

Using the [Restyle](https://www.restyle.dev/) CSS-in-JS lib looks something like this:

```
import { styled } from "restyle";

const Button = styled("button", {
  color: "white",
  backgroundColor: "rebeccapurple",
  padding: "0.5rem 1rem",
  borderRadius: "999px"
})
```

We describe styles in an object and get back a React component. Under the hood, Restyle integrates directly with React's rendering model and [new styling features](https://react.dev/blog/2024/12/05/react-19#support-for-stylesheets), which places Restyle in a high-level layer.

This layer offers the strongest convenience in terms of developer experience, because it is tightly coupled to React itself. But with that convenience comes constraints:

- it cannot run outside React (or even below React v19)
- it's not suitable for cross-framework design systems

Comparatively, [Vanilla Extract](https://vanilla-extract.style/) sits a little lower.

### Vanilla Extract

Vanilla Extract usage looks like this:

```
import { style } from "@vanilla-extract/css";

export const button = style({
  color: "white",
  backgroundColor: "rebeccapurple",
  padding: "0.5rem 1rem",
  borderRadius: "999px"
})
```

You then manually attach the returned class name to your desired component or element.

This looks similar to Restyle: object-based styles, a familiar shape, but the layer is different. It:

- does not assume React
- does assume a bundler
- relies on static extraction
- must run somewhere in the build pipeline

A design system authored in Vanilla Extract can be consumed by anyone (they don't need to use VE or React) but it still depends on bundler-based extraction when authoring.

To go lower in the abstraction hierarchy, we can remove the bundler assumption entirely. That is where a library like [Tokenami](https://tokenami.com) sits.

### Tokenami

Tokenami usage looks like this:

```
import { css } from "@tokenami/css";

export const button = css({
  "--color": "white",
  "--background-color": "rebeccapurple",
  "--padding": "0.5rem 1rem",
  "--border-radius": "999px"
})
```

Again, the returned value is something you attach manually. The surface shape looks familiar, but the layer is different.

Tokenami runs below the bundler. It is a CLI tool that scans source files and outputs plain CSS, similar to Tailwind. Tokenami requires:

- Node
- TypeScript/JavaScript

And not much else. This simplicity gives it more environmental flexibility than bundler-based tools, since it doesn't require a new plugin each time a new bundler comes along.

Lower-layer tools often allow more freedom because they impose fewer assumptions. But every layer comes with its own set of trade-offs.

Vanilla Extract and Tokenami require attaching styles to components manually, and their static-analysis approach makes dynamic styling trickier to different degrees, so they tend to offer less convenience. Higher-level tools like Restyle offer more convenience but at the cost of portability. These kinds of constraints are all part of weighing up different APIs.

## Why These Layer Differences Matter

The three code snippets all share the same basic shape.

1. describe styles in a JS object
2. get some form of class name or component API
3. attach that result to your elements

If we judge only by syntax or shared goal (styling our apps), they appear almost interchangeable. But once the layer comes into focus, they're not interchangeable at all.

Layer differences explain why two APIs that appear the same can behave completely differently. Understanding the layer helps us anticipate:

- Portability
- Environmental requirements
- Bundler assumptions
- Runtime vs build-time constraints
- Where dynamic behaviour is possible
- What limitations come from design vs layer

Once we see the layers, we stop comparing tools by how they look. We compare them by what they fundamentally are.

This brings us nicely to an API many of us pushed back on for similar surface-level reasons.

## The "use client" Directive

When React introduced the `"use client"` directive, many of us reacted the same way:

> "I already have client/SSR features in Remix or Next. What is this even solving?"

Much of the confusion comes from responding to the syntax rather than the layer it operates in.

Before the directive, the decision between server or client lived inside frameworks. Each framework implemented this differently, often through conventions or bundler logic. These were high-level solutions.

The directive brings that decision into React itself. It becomes a primitive rather than a framework feature.

Low-level primitives can often feel inconvenient. They may require us to split components, be more explicit about boundaries, or accept less coverage around things like type safety (e.g. Tailwind).

Higher-level abstractions usually smooth these things over, which makes dropping to a lower layer feel uncomfortable. But this lower-level position is what gives the primitive its power: it makes fewer assumptions, enabling frameworks to build consistent ([or even custom](https://github.com/jjenzz/next-client-attr-webpack-plugin)) behaviour on top of it.

The directive could even, in theory, sit at an even lower layer. Its shape resembles `"use strict"`, the kind of directive JavaScript engines understand.

Obviously `"use client"` isn't one of those, but the fact that it shares the same low-level form is interesting. It's the kind of primitive that could, in theory, travel further down the stack than a React-specific API.

## Seeing Past the Syntax

When a new API appears, it’s common to compare its shape to the nearest thing we recognise. If it looks familiar, we assume it behaves like the things we already know.

But many disagreements or confusions around new APIs become less mysterious once the underlying layer is clear. The assumptions start to make sense. The constraints make sense. The trade-offs make sense. Even the friction sometimes makes sense.

Once we understand the layers, we stop evaluating tools by surface-level syntax and start evaluating them by their assumptions and capabilities.

- We see why portability and convenience rarely come from the same layer.
- We see why two APIs that look the same may not serve the same role.
- We see why high-level tools feel magical and low-level tools feel inconvenient.
- We see why a directive in React may feel uncomfortable yet represent a deeper shift.

## Conclusion

If two APIs look the same, surface syntax doesn't tell us much. The interesting differences usually come from what they constrain or allow.

- The more freedom an API removes, the higher-level it usually is.
- The more freedom it leaves open, the lower-level it usually sits.

Once we acknowledge the layer, we can finally understand the tool behind the surface. A small shift in perspective often reveals a deeper story—one that isn't visible from syntax alone.
