---
type: twir-item
issue: 297
item: 7
item_type: item
date: 2026-09-16
source: https://dev.to/subito/from-1256ms-to-96ms-fixing-inp-in-a-massive-react-dropdown-16l7
tags:
  - "INP"
status: auto
quality: keep
---

[[2026-09-16-TWIR-297|Index]]

# Item 7: Fixing INP in a Massive React Dropdown

Source: [https://dev.to/subito/from-1256ms-to-96ms-fixing-inp-in-a-massive-react-dropdown-16l7](https://dev.to/subito/from-1256ms-to-96ms-fixing-inp-in-a-massive-react-dropdown-16l7)

Summary:
The article details how Subito improved the Interaction to Next Paint (INP) metric for a React dropdown with over 1,000 options by implementing manual virtualization. Instead of rendering all options at once, a custom useVirtualScroll hook renders only the visible items plus a buffer, drastically reducing mount time and improving perceived performance. The solution is lightweight and tailored to lists with uniform row heights.

Key takeaways:
- Rendering large lists synchronously in React can cause severe performance issues, especially on mobile.
- Virtualization (rendering only visible items) is an effective way to improve INP and user experience.
- A custom hook can provide virtualization without heavy dependencies, assuming uniform row heights.
- The approach is practical for dropdowns and similar UI components with large, static lists.

Recommendation:
Summary sufficient

Content:
# From 1,256ms to 96ms: Fixing INP in a Massive React Dropdown

## The Scenario

In Subito's design system, we rely heavily on a custom [`MultiSelect`](https://github.com/Subito-it/articles-code/blob/main/multiselect-virtual-scroll/src/components/MultiSelect.tsx) component. We use it across our marketplace as a standard checkbox-style filter: you search, tick a few boxes, and hit Apply.  
Under the hood, it's built on top of [react-select](https://react-select.com/), completely re-skinned.

For most filters (like item condition or shipping), the option list has about a dozen entries. It felt instant because a dozen rows are nothing for React or the browser.

But then it was used for the "Marca" (Brand) filter. On a live page like our [Shoes category](https://www.subito.it/annunci-italia/vendita/abbigliamento-accessori/scarpe/), this filter has a catalog of **around 1,175 options**.

## The Problem

Suddenly, on a mobile device with a throttled CPU, opening that dropdown stopped being instant. It became one of the worst interactions on the entire page.

To diagnose it, we recorded a session with Chrome DevTools' Performance panel open, simulating a mobile viewport with a **4x CPU slowdown** (a standard way to approximate a mid-tier phone).

When the user clicked to open the "Marca" dropdown, the live INP (Interaction to Next Paint) metric exploded:

> **Local INP: 1,256 ms, rated "poor" and in the bottom 6% of real-user INP experiences.**

The interaction sat frozen for well over a second before the browser could paint the open menu. With Google's threshold for a "good" INP sitting at ≤200ms, this was completely unacceptable.

## Why It Happened

INP measures interaction latency across three phases: *input delay* → *processing duration* → *presentation delay*.

In our case, the *processing duration* was a massive synchronous block of work preventing the repaint.

We tracked the root cause down to the mounting cost of opening the menu.  
Our [`MenuList`](https://github.com/Subito-it/articles-code/blob/main/multiselect-virtual-scroll/src/components/MenuList.tsx) component received the entire array of 1,175 brands. Opening the menu forced React to simultaneously create ~1,175 [`Option`](https://github.com/Subito-it/articles-code/blob/main/multiselect-virtual-scroll/src/components/Option.tsx) component instances (each containing a label and a custom Checkbox, generating several DOM nodes).  
All this happened in a single synchronous commit, even though the visible window only had space to show about 6 rows at a time.

## How We Solved It

We didn't rewrite everything from scratch, nor did we import massive third-party virtualization libraries. We attacked the exact root cause using standard React APIs.

We could keep the solution this small thanks to one specific property of our option list, which we'll come back to right after the code.

### What is virtualization?

Instead of rendering every item in a list, virtualization renders only the items currently visible on screen, plus a small buffer just outside the viewport. Our "Marca" filter has around 1,175 brands, but the dropdown only shows a handful of rows at a time.

Without virtualization:

```
1,175 brands
┌──────────────────────────────┐
│ Brand 1                      │
│ Brand 2                      │
│ Brand 3                      │
│ ...                          │
│ Brand 1,175                  │
└──────────────────────────────┘

All 1,175 components are mounted
```

Enter fullscreen mode

Exit fullscreen mode

With virtualization:

```
1,175 brands
┌──────────────────────────────┐
│                              │
│     Brand 42                 │
│     Brand 43                 │
│     Brand 44                 │
│     Brand 45                 │
│     Brand 46                 │
│     Brand 47                 │
│     Brand 48                 │
│                              │
└──────────────────────────────┘

Only the visible items + a small buffer
are mounted in the DOM
```

Enter fullscreen mode

Exit fullscreen mode

We don't remove anything from the list itself. The full list is still there for scrolling and searching. We just avoid creating React components and DOM nodes for items the user can't currently see, and as the user scrolls, the visible window moves while React mounts the new rows and unmounts the ones no longer needed.

This is particularly effective for our `MultiSelect`: the user may have 1,175 brands available, but at any given moment they can only see around 6 rows.

There are two ways to do it: assume every row is the same height, or measure each row one by one. What follows is the first one, which is by far the simpler of the two.

### Virtualizing the list to fix the Mounting Cost

To fix the opening delay, we hand-rolled a small [`useVirtualScroll`](https://github.com/Subito-it/articles-code/blob/main/multiselect-virtual-scroll/src/hooks/useVirtualScroll.ts) hook (about 90 lines).

The concept is simple: track the scroll position and render *only* the visible rows, plus a small buffer (`OVERSCAN` of 5 items) to prevent blank flashes during fast scrolling.

It all starts from a single number: the height of one row, read from the DOM right after the menu mounts.

```
// Measure the actual rendered option height once after mount
useLayoutEffect(() => {
  const el = listboxRef.current?.querySelector<HTMLElement>('[role="option"]');

  if (el) {
    const h = el.getBoundingClientRect().height;
    if (h) setItemHeight(h);
  }
}, []);
```

Enter fullscreen mode

Exit fullscreen mode

Everything else is arithmetic on that one number:

```
// How tall the list would be, and which slice of it to render
const totalHeight = totalCount * itemHeight;

const startIdx = Math.max(0, Math.floor(scrollTop / itemHeight) - OVERSCAN);

const endIdx = Math.min(
  totalCount,
  Math.ceil((scrollTop + maxHeight) / itemHeight) + OVERSCAN,
);

const offsetTop = startIdx * itemHeight;
```

Enter fullscreen mode

Exit fullscreen mode

The rendered structure became a tall, empty container `div` (1,175 rows × 40px = 47,000px high, so the native scrollbar reflects the full list length) containing an absolutely positioned inner `div` with only the ~13 necessary rows actually mounted in the DOM.

> **Live demo & code:** we put together a [CodePen demo](https://codepen.io/editor/ale-grosselle/pen/01a03cfb-f544-7838-98ec-bda15344b8fc) showing a simplified version of this windowed rendering approach. The complete implementation is in our [GitHub repository](https://github.com/Subito-it/articles-code/tree/main/multiselect-virtual-scroll).

### The catch: every row must be the same height

Look at what those four values have in common: `itemHeight`. We measure one row and assume the other 1,174 are identical; the hook never asks how tall row 800 actually is.

When that's not true, the list breaks quietly. A row taller than `itemHeight` pushes everything below it out of place, and the error adds up row after row: the further you scroll, the more the content drifts away from where the scrollbar says it is, leaving gaps, overlapping rows, or options you simply can't reach.

The usual suspects:

- **Group headers**, styled bigger than a normal option row.
- **Labels that wrap**: "Alexander McQueen" is one line on a wide screen and two on a narrow phone.
- **Rows that change after we measured them**: a different density after a rotation or resize, or a web font landing late. We measure only once, when the menu opens.

So before copying this hook, check your own list. Open it while it's still un-virtualized, at the narrowest width you support, and count how many different row heights you get:

```
new Set(
  [...document.querySelectorAll('[role="option"]')].map(
    (el) => el.getBoundingClientRect().height,
  ),
);

// Set(1) { 40 }         → one height everywhere: this technique works
// Set(3) { 40, 64, 88 } → it doesn't, keep reading
```

Enter fullscreen mode

Exit fullscreen mode

Our rows pass that test because the component is built to keep them uniform: long brand names are truncated with an ellipsis instead of wrapping, and group headers aren't special; they're normal rows with a checkbox, with their children simply indented. That's a design decision as much as a technical one, and it's what buys us a 90-line hook.

### If your rows aren't uniform

Two honest options:

1. **Make them uniform.** One row height, truncation instead of wrapping. Usually the cheapest fix, but it's a design change: bring your designer into the conversation.
2. **Use a library.** [TanStack Virtual](https://tanstack.com/virtual) and [react-virtuoso](https://virtuoso.dev/) measure every row and keep track of where each one ends up. That's a lot more code than what you've seen here, plus edge cases like a row being re-measured while you scroll past it. If your rows genuinely vary, this is where a dependency earns its bytes.

The point isn't "don't hand-roll virtualization". It's that our hook is 90 lines because all our rows are the same height, not because virtualization is a 90-line problem.

## The Results

| Metric | Before | After (Fixed) |
| --- | --- | --- |
| **Local INP (Opening)** | **1,256 ms** ("poor") | **96 ms** ("good") |
| **DOM Nodes `[role="option"]`** | up to ~1,175 | **13** |

By addressing the mounting cost, we brought a completely broken interaction back under the 100ms mark, dropping the rendered DOM nodes from over a thousand to just 13.

*(Note: There is an accessibility trade-off. Virtualization physically removes off-screen items from the DOM, meaning the browser's native search (Ctrl+F) won't find brands that aren't currently visible in the window. Users have to rely on our custom search bar).*

## A Practical Checklist

If you're staring at a slow interaction on a massive list:

- **Check what mounts:** if a menu mounts 1,000 components when it only shows 6, you've found your first suspect.
- **Check that your rows are all the same height:** if they are, this technique is ~90 lines. If they're not, either make them uniform or use a library that measures each row.
- **Render only the visible rows:** track scroll position and mount just the rows in view, plus a small buffer, instead of the whole list.
- **Watch the DOM node count, not just the item count:** a list can hold thousands of entries as long as only a handful are ever mounted at once.

A list of 1,100 items is not inherently a performance problem. Rendering all of it, every single time, before the browser is allowed to draw the next frame... *that* is the problem.
