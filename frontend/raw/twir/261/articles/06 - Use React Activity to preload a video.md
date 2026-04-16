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
quality: keep
---

[[2025-12-03-TWIR-261|Index]]

# Item 6: Use React <Activity /> to preload a video

Source: [https://www.epicreact.dev/use-react-activity-to-preload-a-video-y2lmw](https://www.epicreact.dev/use-react-activity-to-preload-a-video-y2lmw)

Summary:
Kent C. Dodds introduces React 19’s <Activity> component, which allows preloading videos (and other content) even when conditionally hidden. By keeping the video in the DOM but visually hidden, preload="auto" works as intended, improving user experience. The article also provides a custom hook for managing video playback state.

Key takeaways:
- <Activity> keeps hidden content in the DOM, enabling preloading and state preservation.
- Useful for tabs, modals, and media that should be ready instantly.
- Handles effect cleanup and state restoration automatically.
- Includes practical example and custom hook for video autoplay management.

Recommendation:
Read fully (read fully if implementing advanced media or tabbed UIs)

Why it matters:
read fully if implementing advanced media or tabbed UIs

Content:
# Use React <Activity /> to preload a video

Did you know that `preload="auto"` on a video element won't work if the video is
conditionally rendered? React's new `<Activity>` component solves this problem
elegantly. Here's how.

## The Problem

Let's say you have a movie catalog with trailers. You want to show a video when
the user clicks "Watch Trailer", and you'd like to preload it for a better user
experience:

`showTrailer ? <video src={movie.videoUrl} preload="auto" controls /> : null`

The problem? If the video element isn't in the DOM, the browser can't preload
it. So when a user on a slow connection clicks "Watch Trailer", they have to
wait for the video to load, defeating the purpose of preloading.

You might think: "I'll just use `display: none` or something instead of
conditional rendering!" And that might work, but there's a better way.

## The Solution: Activity

React 19's `<Activity>` component is perfect for this. Instead of conditionally
rendering the video, wrap it in an Activity boundary:

`<Activity mode={showTrailer ? 'visible' : 'hidden'}>

<div className="overflow-hidden rounded-lg">`

Now the video element is always in the DOM, so `preload="auto"` actually works!
When the user clicks "Watch Trailer" on a slow connection, the video appears
instantly because it was already loading in the background.

Here's the complete component:

`export function MovieTrailer({ movie }: { movie: Movie }) {

const [showTrailer, setShowTrailer] = useState(false)

onClick={() => setShowTrailer(!showTrailer)}

className="rr-button mb-4"

{showTrailer ? 'Hide Trailer' : 'Watch Trailer'}

<Activity mode={showTrailer ? 'visible' : 'hidden'}>

<div className="overflow-hidden rounded-lg">`

## Why Activity?

Activity does more than just hide/show with `display: none`. When hidden, it:

- Visually hides children
- Cleans up Effects (pausing subscriptions, etc.)
- Preserves component state for when it becomes visible again
- Still allows the DOM to exist (so preloading works!)

This makes it perfect for content that users are likely to interact with again,
like tabs, modals, or in our case, videos that should preload.

## Handling Video Autoplay

Since the video is always in the DOM when using Activity, you'll want to handle
autoplay carefully. Here's a custom hook that handles pausing when hidden:

`function useAutoplay(showTrailer: boolean) {

const video = document.querySelector('video')

if (!(video instanceof HTMLVideoElement)) return`

This ensures the video pauses when hidden and plays when shown, giving you the
best of both worlds: preloading and proper playback control.

## Learn More

Activity is a powerful new component in React 19 with many use cases beyond
video preloading. Check out the
[React docs](https://react.dev/reference/react/Activity) to learn about:

- Restoring component state when hidden
- Preserving DOM state (like form inputs)
- Improving hydration performance
- And more!

Activity is a great example of React solving real-world problems. Give it a try
in your next project!
