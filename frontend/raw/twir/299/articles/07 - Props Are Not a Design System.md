---
type: twir-item
issue: 299
item: 7
item_type: item
date: 2026-09-30
source: https://vitonsky.net/blog/2026/09/18/design-system/
tags:
status: auto
quality: keep
---

[[2026-09-30-TWIR-299|Index]]

# Item 7: Props Are Not a Design System

Source: [https://vitonsky.net/blog/2026/09/18/design-system/](https://vitonsky.net/blog/2026/09/18/design-system/)

Summary:
This opinion piece argues that passing arbitrary style props or utility classes to components undermines consistency and maintainability in UI codebases. Instead, it advocates for defining reusable, named variants and modifiers at the component level, ensuring semantic clarity and visual consistency. Examples are provided for various stacks (HTML, BEM, CSS Modules, ChakraUI).

Key takeaways:
- Inline style props or utility classes at the call site lead to inconsistent, unmaintainable UIs.
- Use variants and modifiers as the only API for component styling.
- Variants should encapsulate all visual details; modifiers provide controlled, semantic adjustments.
- Approach is technology-agnostic and scales across different UI libraries.

Recommendation:
Read fully (read fully if you are designing or refactoring a component library or design system)

Why it matters:
read fully if you are designing or refactoring a component library or design system

Content:
# Props Are Not a Design System

Most UI kits let you pass any style as a prop — radius, size, color, or a wall of Tailwind classes, whatever you need. That flexibility is exactly the problem: it turns every component call into a one-off styling decision, and no two buttons end up the same. Let’s talk about practices that prevent building an inconsistent, unmaintainable code base that won’t scale.

![](/_astro/the-red-circle-1970.Cr7V9FbP_2n57tx.webp)

The Red Circle (1970)

Look at this button built [with Tailwind](https://tailwindcss.com/docs/styling-with-utility-classes) for example:

```
<button
  className="
    inline-flex items-center justify-center gap-2
    ring-offset-background transition-colors
    focus-visible:outline-none focus-visible:ring-2
    focus-visible:ring-ring focus-visible:ring-offset-2
    disabled:pointer-events-none disabled:opacity-50
    bg-primary text-primary-foreground
    hover:bg-primary/90
    h-10 px-4 py-2
    dark:bg-primary dark:text-primary-foreground
    dark:hover:bg-primary/90
    sm:h-9 sm:px-3
    md:h-10 md:px-4
    lg:text-base
    [&_svg]:pointer-events-none
    [&_svg]:size-4
    [&_svg]:shrink-0
  "
>
  Save changes
</button>
```

You can do the same thing [with pure HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/style) too:

```
<button
  style="
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    white-space: nowrap;
    border-radius: 0.375rem;
    font-size: 0.875rem;
    line-height: 1.25rem;
    font-weight: 500;
    transition: color 150ms, background-color 150ms, border-color 150ms,
      text-decoration-color 150ms, fill 150ms, stroke 150ms;
    background-color: var(--primary);
    color: var(--primary-foreground);
    height: 2.5rem;
    padding: 0.5rem 1rem;
  "
>
  Save changes
</button>
```

Both examples do the same thing: *the style is decided at the call site*, instance by instance, instead of being named once and reused. That’s what I mean by **inlining** - *the mechanism doesn’t matter*, whether it’s a `style` attribute, [style props](https://chakra-ui.com/docs/styling/overview#style-props), or a [wall of utility classes](https://tailwindcss.com/docs/styling-with-utility-classes).

Aside from the obvious technical issues of page size and caching, there are a few more important foundational problems:

1. you cannot ensure visual consistency, even within a single file
2. such code has no semantics, so you can’t tell what it means
3. such code has [no system behind it](/blog/2024/10/11/system-approach/), so it is difficult to maintain - even with an LLM you’ll wait a long time, because this error-prone style requires many iterations to correct

To address these problems, we need to stop deciding style at the call site and start defining it once, as a [reusable](/blog/2023/08/16/bem-is-not-about-css/), named unit of the interface.

The implementation depends on the stack, but most projects today build on component-based UI kits, so that’s what the examples below will use. Each component will be built from **variants** and **modifiers**.

A variant is the self-contained style that completely describes all the visual aspects of a component, given a semantic name.

You can use a variant like this:

```
<Button variant="primary">Save changes</Button>
<Button variant="secondary">Cancel</Button>
```

In pure HTML with [BEM methodology](https://bem.info/en/methodology/quick-start/), it would look like this:

```
<button class="Button Button__variant_primary">Save changes</button>
<button class="Button Button__variant_secondary">Cancel</button>
```

A variant must contain all implementation details of the visual - inner geometry, colors, typography, everything. It must not expect its styles to be supplemented by anything external, whether that’s a [global reset](https://meiert.com/blog/stop-using-resets/), a stray `font-family`, or any other in-place styling.

A variant defines the semantic unit of the user interface. That’s what makes a design system observable: you can see exactly which variants of a component exist and consistently update all of them at once.

When you use a UI kit on a large project with a rich visual design, you may be tempted to write something like this:

```
<Button
	variant="primary"
	radius="xl"
	fontSize="xl"
	fontWeight={500}
	fontFamily="fancy"
>
	Buy
</Button>
```

This is the same call-site styling problem again, just typed: the props override the variant from outside, so it no longer defines the button’s final look. Worse, those overrides don’t track the variant — update the variant or introduce a new color scheme, and they silently fall out of sync.

If we need a variation of a view, we can implement a **modifier** instead, to keep things manageable. A modifier is part of the component’s API, at the same level as the variant - not an escape hatch around it.

For example, we can use `variant` to set the visual style of a button and add a modifier `size` to control its geometry:

```
<Button variant="primary" size="xl">Buy</Button>
```

*If we find ourselves applying many modifiers at once, that’s a signal to introduce another variant instead:*

```
<Button variant="fancy-primary" size="xl">Buy</Button>
```

This is the core discipline: variants and modifiers aren’t just two features of a UI kit, they’re a rule for where a styling decision is allowed to live, and when a recurring combination of modifiers has earned its own name.

The implementation example in vanilla CSS with a [BEM-style](https://bem.info/en/methodology/css/) [modifier](https://bem.info/en/methodology/key-concepts/#modifier):

```
.button__size_xl {
	border-radius: 12px;
	font-size: 3rem;
	font-weight: 500;
	/* ... */
}
```

CSS modules for [Mantine UI](https://mantine.dev/styles/styles-overview/#css-modules):

```
.root {
	&[data-size="xl"] {
		border-radius: 12px;
		font-size: 3rem;
		font-weight: 500;
		/* ... */
	}
}
```

[ChakraUI theme](https://chakra-ui.com/docs/theming/overview):

```
export default defineConfig({
	theme: {
		semanticTokens: {
			colors: {
				// ...
			},
		},
		recipes: {
			button: defineRecipe({
				variants: {
					size: {
						xl: {
							borderRadius: "12px",
							fontSize: "3rem",
							fontWeight: "500",
						},
					},
					variant: {
						accent: {
							// ...
						},
					},
				},
			}),
		},
	},
});
```

Same rule, three different technologies - variants and modifiers work regardless of the tools you use.

This approach can be applied to almost any UI kit, even one that wasn’t designed with this discipline in mind.

If you follow it, you’ll [eventually end up with a design system](/blog/2024/10/11/system-approach/) even if you didn’t set out to build one - you’ll naturally be forced to identify the reusable units of your interface. Your code will stop being a pile of one-off styling decisions and start being a system.
