---
type: twir-item
issue: 261
item: 6
item_type: item
date: 2025-12-03
source: https://www.epicreact.dev/use-react-activity-to-preload-a-video-y2lmw
tags:
  - "Activity"
status: auto
---

[[2025-12-03-TWIR-261|Index]]

# Item 6: Use React <Activity /> to preload a video

Source: [https://www.epicreact.dev/use-react-activity-to-preload-a-video-y2lmw](https://www.epicreact.dev/use-react-activity-to-preload-a-video-y2lmw)

Summary:
Kent C. Dodds explains how React 19’s <Activity> component enables preloading of videos (or other content) even when conditionally hidden, solving the issue where preload="auto" fails if the element isn’t in the DOM. By wrapping the video in <Activity> and toggling its visibility, the video preloads in the background, improving user experience. The article includes a custom hook for managing autoplay and discusses Activity’s broader benefits for state and effect management.

Key takeaways:
- <Activity> keeps hidden elements in the DOM, enabling true preloading.
- Preserves component state and cleans up effects when hidden.
- Useful for tabs, modals, and any content that benefits from background loading.
- Includes practical code examples and a custom autoplay hook.

Recommendation: Read fully (especially if you handle media or dynamic content in React 19+)
