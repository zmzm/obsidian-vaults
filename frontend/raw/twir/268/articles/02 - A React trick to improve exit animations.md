---
type: twir-item
issue: 268
item: 2
item_type: item
date: 2026-02-11
source: https://barvian.me/react-exit-animations
tags:
status: auto
quality: keep
---

[[2026-02-11-TWIR-268|Index]]

# Item 2: A React trick to improve exit animations

Source: [https://barvian.me/react-exit-animations](https://barvian.me/react-exit-animations)

Summary:
The author describes a common issue in React where exit animations are disrupted by state updates, causing distracting UI changes during component unmount. After exploring several workarounds, the article introduces a "Freeze" component that leverages Suspense to pause DOM updates for exiting components, enabling smoother animations. The solution involves overriding Suspense's default hiding behavior and works well with libraries like React Aria Components, though it is somewhat hacky and may not be future-proof.

Key takeaways:
- Exit animations can be disrupted by state updates that affect the exiting component's content.
- The "Freeze" component uses Suspense to prevent DOM updates, keeping the UI visually stable during exit.
- Implementation details include using insertion effects and a custom observer to manage DOM nodes.
- This approach is a clever hack and may break with future React versions, but works in React 18 and 19.2.

Recommendation:
Read fully (for those interested in advanced animation control and the implementation details)

Why it matters:
for those interested in advanced animation control and the implementation details

Content:
# A React trick to improve exit animations

Suspense can pause a component's DOM updates, ensuring smoother exit animations.

## The problem

When I was building out the component library for the
[Clerk](https://clerk.com) dashboard I often ran into an issue with
exit animations: the component’s contents would change during the animation.

I think this is distracting. You probably don’t care about something
that’s exiting, but if it updates at the same time it draws
attention to itself.

The problem is that in React, updates that trigger
exit animations often affect the contents of the exiting component too.
An example can be seen in the left demo above, where the search placeholder
changes once you select a label and selected labels are kept at the top of the list for quick access.
React batches these updates with the one that closes the popover.

## Exploration

I tried a few workarounds to prevent these unwanted updates. The first was to save the component’s state
before exiting and use that state during the animation to prevent re-renders.
This worked but I felt it was too burdensome for other engineers building their own
components, as you had to keep track of all the state that could cause the exiting component to re-render.

I’ve also seen approaches that delay updating certain state until exit animations complete.
Libraries like Base UI include props like [`onOpenChangeComplete`](https://base-ui.com/react/components/select) to
make this easier. This can work, but I think it can get a bit complex
when handling interruptions to the exit animations.

What I really wanted was a way to
tell React to stop committing DOM changes in exiting components. Something like this:

```
<Select.Root>
	<Select.Trigger />
	<Freeze frozen={isExiting}>
		<Select.Content />
	</Freeze>
</Select.Root>
```

(Hat tip to my coworker [Rafa](https://www.cmrg.me/) who proposed the name `Freeze`.)

## The solution

After a bit of digging, I discovered one component in React that behaves this exact way: Suspense. React continues to render suspended subtrees but doesn’t commit their changes to the DOM, so they remain “frozen” in their pre-suspended state.
The only problem is that React also hides them with `display: none !important` while they’re suspended.

My final solution was to create a small wrapper around `Suspense` that un-applied this style.
I used a [Fragment ref](https://react.dev/reference/react/Fragment#fragmentinstance) to target the child DOM nodes of the `Suspense`.
Here’s the full code:

```
import * as React from 'react'

export function Freeze({ frozen, children }: { frozen: boolean; children: React.ReactNode }) {
	const elementsRef = React.useRef(new Set<HTMLElement>())
	const fragmentRef: React.RefCallback<React.FragmentInstance> = (frag) => {
		if (!frag) return
		// Use a custom observer to store the child DOM nodes in a ref,
		// because FragmentInstance doesn't offer an API to do it directly.
		const observer = new ElementsObserver(elementsRef)

		frag.observeUsing(observer)
		return () => {
			frag?.unobserveUsing(observer)
		}
	}

	// An insertion effect is the earliest opportunity to undo Suspense's `display: none`
	React.useInsertionEffect(() => {
		if (!frozen) return
		elementsRef.current.forEach((element) => {
			element.style.display = ''
		})
	}, [frozen])

	return (
		<React.Fragment ref={fragmentRef}>
			<React.Suspense>
				{frozen && <Suspend />}
				{children}
			</React.Suspense>
		</React.Fragment>
	)
}

// A custom observer to store DOM nodes in a ref:
class ElementsObserver {
	constructor(private readonly elementsRef: React.RefObject<Set<HTMLElement>>) {}

	observe(element: HTMLElement) {
		this.elementsRef.current.add(element)
	}
	unobserve(element: HTMLElement) {
		this.elementsRef.current.delete(element)
	}
	disconnect() {
		this.elementsRef.current.clear()
	}
}

const infinitePromise = new Promise<never>(() => {})
function Suspend() {
	React.use(infinitePromise)
	return null
}
```

(Note: this simple implementation will wipe out any inline `display` style the element had before it was frozen.)

And here’s an example using [React Aria Components](https://react-aria.adobe.com/Select):

```
<Select>
	<Button>
		<SelectValue />
	</Button>
	<Popover>
		{({ isExiting }) => (
			<Freeze frozen={isExiting}>
				<ListBox>{/* ... */}</ListBox>
			</Freeze>
		)}
	</Popover>
</Select>
```

You can see this in action in the right demo above.

## Closing thoughts

I’ve used this in a few projects now and it’s worked well so far.
It works particularly well with React Aria Components which uses
React state for hover, press, and focus interactions, so
things like hover state get “frozen” too (compared to CSS `:hover` which doesn’t freeze).

It’s obviously a bit of a trick, though, and something that could
break in a future version of React. I tested it in React 18 & 19.2 and it worked in both of them, though.

I’m hopeful the React team could add support for this behavior, especially
after reading their [blog post about Activity](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024#offscreen-renamed-to-activity):

> while researching [Activity] we realized that it’s possible for parts of the app to be visible and inactive, such as content behind a modal.

”Visible and inactive” sounds similar to the “frozen” state here,
so I hope they consider supporting it with an Activity mode in the future.
