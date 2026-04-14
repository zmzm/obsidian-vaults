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
---

[[2026-03-04-TWIR-271|Index]]

# Item 9: Devon from React Aria explains the limits of the native <dialog> vs JS/React abstractions

Source: [https://github.com/adobe/react-spectrum/discussions/9696#discussioncomment-15942257](https://github.com/adobe/react-spectrum/discussions/9696#discussioncomment-15942257)

Summary:
Devon Govett (React Aria maintainer) explains why React Aria and similar JS modal libraries are still valuable despite broad support for the native <dialog> element. Key reasons include top-layer stacking issues, lack of animation/backdrop control, incomplete focus management, and missing scroll prevention in native dialogs.

Key takeaways:
- Native <dialog> has limitations in stacking, focus trapping, and scroll prevention.
- JS-based modals offer greater control and compatibility with third-party overlays and accessibility needs.
- Native dialogs may suffice for simple apps, but complex UIs often require JS abstractions.
- The web platform is evolving, but many production apps still need custom modal handling.

Recommendation: Summary sufficient
