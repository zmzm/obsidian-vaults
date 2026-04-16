---
type: twir-item
issue: 265
item: 7
item_type: item
date: 2026-01-21
source: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types
tags:
  - "Navigation"
  - "API"
status: auto
quality: keep
---

[[2026-01-21-TWIR-265|Index]]

# Item 7: Navigation API

Source: [https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)

Summary:
The Navigation API is a modern browser API standardizing client-side routing for SPAs, replacing the older History API with a centralized "navigate" event. It allows interception and handling of navigation events (including links, forms, and programmatic navigations) in a unified way, supporting advanced routing, scroll restoration, and transition management. The article provides usage examples and discusses the benefits over legacy approaches.

Key takeaways:
- Navigation API centralizes routing logic, improving reliability and maintainability in SPAs.
- Enables interception and custom handling of all navigation types, not just link clicks.
- Supports scroll restoration and transition tracking out of the box.
- Will impact future React router implementations and custom navigation logic.

Recommendation:
Read fully (for those building or maintaining SPA routing systems)

Why it matters:
for those building or maintaining SPA routing systems

Content:
# Using view transition types

We'll demonstrate what you need to know about view transition types by walking through code contained in the following three examples:

- [SPA transition types gallery](https://mdn.github.io/dom-examples/view-transitions/spa-gallery-transition-types/) ([source code](https://github.com/mdn/dom-examples/tree/main/view-transitions/spa-gallery-transition-types)): An SPA image gallery that uses transition types to apply different transition animations when the images are moved between using the prev button, next button, and by clicking directly on an image.
- [MPA transition types example](https://mdn.github.io/dom-examples/view-transitions/mpa-chapter-nav-transition-types/) ([source code](https://github.com/mdn/dom-examples/tree/main/view-transitions/mpa-chapter-nav-transition-types)): A story app with a chapter on each page. Demonstrates how to apply view transition animations across pages selectively with a transition type.
- [MPA multiple transition types example](https://mdn.github.io/dom-examples/view-transitions/mpa-chapter-nav-multiple-transition-types/) ([source code](https://github.com/mdn/dom-examples/tree/main/view-transitions/mpa-chapter-nav-multiple-transition-types)): Builds on the previous example by demonstrating how to apply different view transition animations across pages selectively with different transition types. The transition type is determined on-the-fly with JavaScript during the navigation.

We won't explain how all the code works, just the bits relevant to view transition types. We've provided comments in the code to explain what each part is doing.

To apply different types to SPA view transitions, we pass the type names into the [`Document.startViewTransition()`](/en-US/docs/Web/API/Document/startViewTransition) method call that kicks off the transition. The method can accept an object as a parameter containing an `update` callback function that handles the DOM updates you want to animate, and a `types` array containing strings representing the type names.

Let's look at an example from our [SPA transition types gallery](https://mdn.github.io/dom-examples/view-transitions/spa-gallery-transition-types/):

js

```
document.startViewTransition({
  update() {
    displayedImage.src = `${baseURL}${images[newId].filename}`;
    displayedImage.alt = images[newId].alt;
    displayedImage.setAttribute("data-id", newId);
    caption.textContent = images[newId].alt;
  },
  types: ["backwards"],
});
```

When the "Previous" button is pressed, this code is run â the callback function updates the displayed image to display the previous image in the sequence (including updating its alt text, `data-id` representing the sequence number, and caption), and the `types` array specifies that the view transition should be run with a type of `backwards`.

**Note:**
The types set on the view transition in the `types` array can be accessed via the [`types`](/en-US/docs/Web/API/ViewTransition/types "types") property of the [`ViewTransition`](/en-US/docs/Web/API/ViewTransition) object returned by the `startViewTransition()` method. The `types` property is a [`ViewTransitionTypeSet`](/en-US/docs/Web/API/ViewTransitionTypeSet). This is a [Set-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis), which means you can modify the types applied to a view transition on-the-fly using methods available on it such as `clear()`, `add()`, and `delete()`.

Over in the CSS, we can customize styles for the active transition using the [`:active-view-transition`](/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition) and [`:active-view-transition-type()`](/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type) pseudo-classes. Respectively, these allow you to create selectors that match when any view transition is active, or only when a view transition with a certain type is active.

First of all, we define a bunch of styles that are applied when a view transition is active, regardless of its type, selected using `:active-view-transition`. In this nested block, we apply a [`view-transition-name`](/en-US/docs/Web/CSS/Reference/Properties/view-transition-name) value of `none` to the document [`:root`](/en-US/docs/Web/CSS/Reference/Selectors/:root) to turn view transitions off for most of the document. We then apply `view-transition-name` values of `image` and `caption` to the [`<img>`](/en-US/docs/Web/HTML/Reference/Elements/img) and [`<figcaption>`](/en-US/docs/Web/HTML/Reference/Elements/figcaption) elements respectively, so changes to their DOM state are captured in separate snapshots and they can be animated independently.

Finally, we use the [`::view-transition-old()`](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old) and [`::view-transition-new()`](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new) pseudo-elements to apply specific animations to the `caption` outgoing and incoming view. We want these animations to be applied to the `<figcaption>` regardless of the specified type.

css

```
html:active-view-transition {
  :root {
    view-transition-name: none;
  }
  .displayed-img {
    view-transition-name: image;
  }
  figcaption {
    view-transition-name: caption;
  }

  &::view-transition-old(caption) {
    animation-name: fade-out;
  }
  &::view-transition-new(caption) {
    animation-name: fade-in;
    animation-delay: 0.6s;
  }
}
```

The next stage is to apply different animations to the `image` outgoing and incoming views, depending on whether the `type` of the active view transition is `forwards` (the "Next" button was pressed), `backwards` (the "Previous" button was pressed), or `upwards` (a thumbnail image was clicked). This is done using three `:active-view-transition-type()` rulesets, each applying different [`animation-name`](/en-US/docs/Web/CSS/Reference/Properties/animation-name) values to the `::view-transition-old()` and `::view-transition-new()` pseudo-elements for each separate type:

css

```
html:active-view-transition-type(forwards) {
  &::view-transition-old(image) {
    animation-name: slide-out-to-left;
  }
  &::view-transition-new(image) {
    animation-name: slide-in-from-right;
  }
}

html:active-view-transition-type(backwards) {
  &::view-transition-old(image) {
    animation-name: slide-out-to-right;
  }
  &::view-transition-new(image) {
    animation-name: slide-in-from-left;
  }
}

html:active-view-transition-type(upwards) {
  &::view-transition-old(image) {
    animation-name: slide-out-to-top;
  }
  &::view-transition-new(image) {
    animation-name: slide-in-from-top;
    animation-delay: 0.6s;
  }
}
```

In the case of the `::view-transition-new(image)` animation for the `upwards` type, we've also included an [`animation-delay`](/en-US/docs/Web/CSS/Reference/Properties/animation-delay) value of `0.6s` to stop the new content sliding in from the top of the screen until the old content has finished sliding out. It looks strange if the two overlap, in this case.

Further down the stylesheet, we set the [`animation-duration`](/en-US/docs/Web/CSS/Reference/Properties/animation-duration) of all animations in all groups to `0.6s`, which explains why the delay set earlier was `0.6s`:

css

```
::view-transition-group(*) {
  animation-duration: 0.6s;
}
```

**Note:**
For brevity, we've not shown all of the [`@keyframes`](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes) definition code for the animations referenced above. You can find these in the [source code](https://github.com/mdn/dom-examples/tree/main/view-transitions/spa-gallery-transition-types).

To apply different types to cross-document view transitions, you can set them in the [`types`](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#types) descriptor of the [`@view-transition`](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition) at-rule, which contains one or more types separated by commas.

For example, in our [MPA transition types example](https://mdn.github.io/dom-examples/view-transitions/mpa-chapter-nav-transition-types/), the `@view-transition` at-rule in the shared stylesheet looks like this:

css

```
@view-transition {
  navigation: auto;
  types: slide;
}
```

Over in the CSS, we can customize the animations applied to the active view transition based on its type in the same way as we did in the SPA example:

css

```
html:active-view-transition-type(slide) {
  :root {
    view-transition-name: none;
  }
  section {
    view-transition-name: chapter;
  }
  &::view-transition-old(chapter) {
    animation-name: slide-out-to-left;
  }
  &::view-transition-new(chapter) {
    animation-name: slide-in-from-right;
  }
}
```

Here we apply several styles when the active view transition has a `type` of `slide` using the `:active-view-transition-type(slide)` selector. We apply a `view-transition-name` of `none` to the `:root` element to stop any snapshot capture, and then override it with a `view-transition-name` of `chapter` set on the page `<section>` element â this is the only part of the documents we want to apply a view transition to.

Next, we use `::view-transition-old(chapter)` and `::view-transition-new(chapter)` to apply custom animations to the `<section>` as its content transitions between pages.

The above works OK, but it's not ideal â when a new page is navigated to, the old page content always disappears to the left, and the new page content always appears from the right. This animation is fine when you are moving to a later chapter, but (at least, for users of left-to-right languages like English) it feels counter-intuitive when moving to an earlier chapter. For later-to-earlier chapter movements, it would be better to reverse the animation direction.

To apply different types to the active view transition based on different navigation types, we need to manipulate the [`types`](/en-US/docs/Web/API/ViewTransition/types "types") property of the corresponding `ViewTransition` object. This is available in the:

The [MPA multiple transition types example](https://mdn.github.io/dom-examples/view-transitions/mpa-chapter-nav-multiple-transition-types/) demonstrates how to use this technique. This is similar to the previous example, but with some notable differences, which we'll explain below.

Let's look at the shared JavaScript file. First of all, we define a custom function, `determineTransitionType()`, which looks at the URL of the outgoing page and incoming page and from those determines whether the navigation type is `backwards` (moving to an earlier chapter) or `forwards` (moving to a later chapter).

The chapter pages are named sequentially (`index.html`, then `index2.html`, `index3.html`, etc.), therefore, we compare the number contained in the filenames to see whether the navigation is `backwards` (outgoing page number is higher than incoming page number) or forwards (outgoing page number is lower than incoming page number).

The code you use to determine the type to apply will depend on your project. You can find detailed comments explaining how the below code works in our [source code](https://github.com/mdn/dom-examples/tree/main/view-transitions/mpa-chapter-nav-multiple-transition-types).

js

```
const determineTransitionType = (oldNavigationEntry, newNavigationEntry) => {
  const currentURL = oldNavigationEntry.url;
  const destinationURL = newNavigationEntry.url;

  function determinePageIndex(url) {
    const array = url.split("/");
    const slug = array[array.length - 1];
    if (slug.indexOf("html") === -1) {
      return 0;
    }
    const pageIndex = slug.replace("index", "").replace(".html", "");
    if (pageIndex === "") {
      return 0;
    }
    return parseInt(pageIndex, 10);
  }

  const currentPageIndex = determinePageIndex(currentURL);
  const destinationPageIndex = determinePageIndex(destinationURL);

  if (currentPageIndex > destinationPageIndex) {
    return "backwards";
  } else if (currentPageIndex < destinationPageIndex) {
    return "forwards";
  }
};
```

Next, we use a [`pageswap`](/en-US/docs/Web/API/Window/pageswap_event "pageswap") event listener to set the transition type for the outgoing page. Inside the event handler function, we grab the old and new navigation entries from the event object's [`activation`](/en-US/docs/Web/API/PageSwapEvent/activation "activation") property, pass these to the `determineTransitionType()` function to determine the type, then assign the type to the view transition using the [`ViewTransition.types`](/en-US/docs/Web/API/ViewTransition/types) property's `add()` method.

js

```
window.addEventListener("pageswap", async (e) => {
  const transitionType = determineTransitionType(
    e.activation.from,
    e.activation.entry,
  );

  console.log(`pageSwap: ${transitionType}`);
  e.viewTransition.types.add(transitionType);
});
```

Finally, we use a [`pagereveal`](/en-US/docs/Web/API/Window/pagereveal_event "pagereveal") event listener to set the transition type for the incoming page. Inside the event handler function, we grab the old and new navigation entries from the [`Navigation.activation`](/en-US/docs/Web/API/Navigation/activation) property and pass these to the `determineTransitionType()` function to determine the type. We assign the type to the view transition using the [`ViewTransition.types`](/en-US/docs/Web/API/ViewTransition/types) property's `add()` method, unless the type is `undefined`, in which case we skip that step.

js

```
window.addEventListener("pagereveal", async (e) => {
  const transitionType = determineTransitionType(
    navigation.activation.from,
    navigation.activation.entry,
  );

  console.log(`pageReveal: ${transitionType}`);
  if (transitionType !== undefined) {
    e.viewTransition.types.add(transitionType);
  }
});
```

**Note:**
The `determineTransitionType()` function can return `undefined` if neither the `backwards` or `forwards` conditions are true. This can occur if the user reloads the page, in which case the current page and destination page are the same page, therefore the index values are the same.

Now we've got an appropriate type set on the active view transition depending on the navigation type, we can set different animations for each type in our CSS, in the same way as we saw in previous examples:

css

```
html:active-view-transition {
  nav {
    view-transition-name: none;
  }
  section {
    view-transition-name: chapter;
  }
}

html:active-view-transition-type(forwards) {
  &::view-transition-old(chapter) {
    animation-name: slide-out-to-left;
  }
  &::view-transition-new(chapter) {
    animation-name: slide-in-from-right;
  }
}

html:active-view-transition-type(backwards) {
  &::view-transition-old(chapter) {
    animation-name: slide-out-to-right;
  }
  &::view-transition-new(chapter) {
    animation-name: slide-in-from-left;
  }
}
```

Note also that we have removed the `types` descriptor from the `@view-transition` at-rule in the shared CSS. We need the `navigation` descriptor to enable cross-document view transitions, but we are handling types in our JavaScript, so we don't need to set them here.

css

```
@view-transition {
  navigation: auto;
}
```
