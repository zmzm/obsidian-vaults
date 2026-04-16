---
type: twir-item
issue: 271
item: 9
item_type: item
date: 2026-03-04
source: https://github.com/adobe/react-spectrum/discussions/9696#discussioncomment-15942257
tags:
  - "JS"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 9: Devon from React Aria explains the limits of the native <dialog> vs JS/React abstractions

Source: [https://github.com/adobe/react-spectrum/discussions/9696#discussioncomment-15942257](https://github.com/adobe/react-spectrum/discussions/9696#discussioncomment-15942257)

Summary:
Devon from React Aria discusses why JS-based modal libraries are still relevant despite native <dialog> support in browsers. Key limitations of <dialog> include top-layer stacking issues, lack of animation/backdrop control, incomplete focus containment, and no built-in scroll prevention. JS libraries offer more flexibility and control for complex apps, especially when integrating with third-party overlays or requiring advanced accessibility and animation features.

Key takeaways:
- Native <dialog> has top-layer and stacking order constraints that can conflict with third-party overlays.
- Animations and backdrop transitions are limited with <dialog> compared to JS solutions.
- Focus containment and scroll prevention are more robust in JS-based modal libraries.

Recommendation:
Read fully (read fully if evaluating modal approaches for accessibility or complex overlays)

Why it matters:
read fully if evaluating modal approaches for accessibility or complex overlays

Content:
# Modal a11y · adobe/react-spectrum · Discussion #9696 · GitHub

👍
1
  reacted with thumbs up emoji

 👎
1
  reacted with thumbs down emoji

 😄
1
  reacted with laugh emoji

 🎉
1
  reacted with hooray emoji

 😕
1
  reacted with confused emoji

 ❤️
1
  reacted with heart emoji

 🚀
1
  reacted with rocket emoji

 👀
1
  reacted with eyes emoji

You can’t perform that action at this time.
