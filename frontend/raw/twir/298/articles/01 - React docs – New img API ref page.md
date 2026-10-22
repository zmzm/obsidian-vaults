---
type: twir-item
issue: 298
item: 1
item_type: featured
date: 2026-09-23
source: https://react.dev/reference/react-dom/components/img
tags:
  - "img"
  - "API"
status: auto
quality: keep
---

[[2026-09-23-TWIR-298|Index]]

# Item 1: React docs – New <img> API ref page

Source: [https://react.dev/reference/react-dom/components/img](https://react.dev/reference/react-dom/components/img)

Summary:
The React documentation has introduced a detailed reference page for the built-in <img> component, covering its usage, supported props, caveats, and advanced behaviors such as preloading and integration with View Transitions. The guide explains how React handles image preloading during server rendering, how to control that behavior, and what to consider when using <img> in conjunction with Suspense and ViewTransition. It also highlights common pitfalls and best practices for accessibility and performance.

Key takeaways:
- <img> supports all standard HTML image attributes, with React-specific notes on preloading and event handling.
- React auto-generates preload hints for images during server rendering unless loading="lazy" or fetchPriority="low" is set.
- For ViewTransition animations, React may wait for images to load unless loading="lazy" or an onLoad handler is present.
- Avoid side effects like passing an empty src or using children/dangerouslySetInnerHTML with <img>.

Recommendation:
Read fully (unless you need to implement advanced SSR/image loading optimizations, then read fully)

Why it matters:
unless you need to implement advanced SSR/image loading optimizations, then read fully

Content:
# <img> - React

Specify `width` and `height` when you know the image dimensions so the browser can reserve space before the image loads. For a decorative image, pass `alt=""` so that screen readers ignore it.

---

### Controlling image preloading during server rendering

During server rendering, React automatically generates a preload hint for an `<img>` by default. This can let the browser start fetching the image before it encounters the `<img>` in the rendered HTML.

Add `loading="lazy"` or `fetchPriority="low"` to an image that should not receive this hint:

```
function ProductPage() {

return (

<>

<img src="hero.jpg" alt="Featured product" />

<img src="thumbnail.jpg" alt="Related product" loading="lazy" />

<img src="secondary.jpg" alt="Another product" fetchPriority="low" />

</>

);

}
```

In this example, React generates a preload hint only for `hero.jpg`. Depending on the server API or framework, React may render the equivalent of this element:

```
<link rel="preload" as="image" href="hero.jpg" />
```

React may instead provide the same hint in a `Link` response header. The other two images keep their `loading` and `fetchPriority` props in the rendered HTML, but React does not generate preload hints for them. The `loading="lazy"` prop asks the browser to defer loading an image until it approaches the viewport. The `fetchPriority="low"` prop allows the image to load immediately, but tells the browser to fetch it at a lower priority.

React also does not automatically preload an image when it is inside a `<picture>` or `<noscript>` element, or when its `src` or `srcSet` is a data URL.

If you render an image through a framework or a component library, consult its documentation for the default behavior. React decides whether to generate an automatic preload from the props of the underlying `<img>`. For example, an image component may add `loading="lazy"` by default and provide a separate option for explicitly preloading selected images.

To create an explicit preload hint, call [`preload`](/reference/react-dom/preload).

---

### Waiting for an image during a View Transition

During a client-rendered [`<ViewTransition>`](/reference/react/ViewTransition) update, React may wait for an image to load and decode before starting the animation. This applies when a new `<img>` with a non-empty `src` is rendered, or when an existing image’s `src` or `srcSet` changes. The image must be inside the `<ViewTransition>` subtree and must not have `loading="lazy"` or an `onLoad` handler. React does not wait for images during synchronous updates.

When a Suspense boundary reveals streamed content inside a `<ViewTransition>`, React may also wait for visible images with a non-empty `src` that do not have `loading="lazy"`. React stops waiting after a timeout so that a slow image does not block the update indefinitely.

In this example, the Suspense boundary is wrapped in a `<ViewTransition>` and shows a profile skeleton until the portrait has loaded.

For comparison, the second button inserts the same card directly into the DOM. The card appears immediately, and the browser displays the image after it loads:
