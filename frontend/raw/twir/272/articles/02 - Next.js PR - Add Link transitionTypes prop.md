---
type: twir-item
issue: 272
item: 2
item_type: item
date: 2026-03-11
source: https://github.com/vercel/next.js/pull/90701
tags:
  - "Nextjs"
  - "PR"
  - "Navigation"
status: auto
quality: keep
---

[[2026-03-11-TWIR-272|Index]]

# Item 2: Next.js PR - Add Link transitionTypes prop

Source: [https://github.com/vercel/next.js/pull/90701](https://github.com/vercel/next.js/pull/90701)

Summary:
A new transitionTypes prop is added to the Next.js <Link> component, allowing developers to specify transition animations for navigations in the App Router. This prop triggers React.addTransitionType for each type specified, enabling view transitions during navigation. The update also fixes a bug where transitionTypes could leak onto DOM elements in the Pages Router, and clarifies that this feature is only supported in the App Router. The prop is reactive and works with state-driven transitions.

Key takeaways:
- transitionTypes enables animated transitions for navigations in Next.js App Router.
- The prop is ignored in the Pages Router to maintain compatibility with shared link components.
- Bug fix prevents transitionTypes from appearing as invalid attributes in rendered HTML.
- The feature leverages React.addTransitionType, available in React Canary.

Recommendation:
Summary sufficient (read the PR for implementation details or if planning to use animated transitions in Next.js)

Why it matters:
read the PR for implementation details or if planning to use animated transitions in Next.js

Content:
# Add `transitionTypes` prop to `next/link` by eps1lon · Pull Request #90701 · vercel/next.js · GitHub

```
… pages router Link component, causing it to leak onto the `<a>` DOM element via `restProps` spread.

This commit fixes the issue reported at packages/next/src/client/link.tsx:328

**Bug explanation:**

In `packages/next/src/client/link.tsx` (the pages router Link component), the `transitionTypes` prop was added to the `InternalLinkProps` type (line 129) and validation logic (line 462), but was NOT included in the destructuring at lines 313-328. The destructuring pattern:

```js
const { href, as, children, prefetch, ..., legacyBehavior, ...restProps } = props
```

omits `transitionTypes`, which means when a user passes `<Link href="/about" transitionTypes={['slide-in']}>About</Link>`, the `transitionTypes` value ends up in `restProps`. At line 716, `restProps` is spread onto the rendered `<a>` element:

```jsx
<a {...restProps} {...childProps}>{children}</a>
```

This causes React to emit a warning like: "Warning: React does not recognize the `transitionTypes` prop on a DOM element." It also places an invalid attribute on the `<a>` tag in the HTML output.

In contrast, the app-dir link at `packages/next/src/client/app-dir/link.tsx` line 362 properly destructures `transitionTypes` out of props before spreading the rest.

**Fix explanation:**

Added `transitionTypes,` to the destructuring statement at line 328, right before `...restProps`. This ensures the prop is captured in a named variable and excluded from `restProps`, preventing it from being spread onto the DOM `<a>` element. This matches the pattern used in the app-dir version of the Link component.

Co-authored-by: Vercel <vercel[bot]@users.noreply.github.com>
Co-authored-by: eps1lon <silbermann.sebastian@gmail.com>
```
