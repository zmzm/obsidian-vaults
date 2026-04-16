---
type: twir-item
issue: 271
item: 12
item_type: item
date: 2026-03-04
source: https://www.mux.com/blog/react-is-changing-the-game-for-streaming-apps-with-the-activity-component
tags:
  - "Activity"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 12: React is changing the game for streaming apps with the Activity component

Source: [https://www.mux.com/blog/react-is-changing-the-game-for-streaming-apps-with-the-activity-component](https://www.mux.com/blog/react-is-changing-the-game-for-streaming-apps-with-the-activity-component)

Summary:
This article demonstrates how React 19.2’s <Activity> component solves state loss issues in streaming apps by keeping components mounted when hidden, preserving playback and UI state. It contrasts traditional conditional rendering (which unmounts components) with the new approach, and shows how to combine <Activity> with useLayoutEffect to pause media when hidden, delivering a seamless user experience. The solution is especially relevant for apps with complex, stateful views like video players.

Key takeaways:
- <Activity> allows components to remain mounted and preserve state when hidden, improving UX for streaming and tabbed interfaces.
- Combining <Activity> with useLayoutEffect enables precise control over side effects (e.g., pausing video playback).
- The approach solves common issues with state loss and unwanted background activity in media-rich apps.

Recommendation:
Read fully (read fully if building streaming or tabbed UIs)

Why it matters:
read fully if building streaming or tabbed UIs

Content:
# React is changing the game for streaming apps with the Activity component

Video streaming applications can have complex UIs with multiple views, such as video players, chat, notes, transcripts, and related videos. Without proper state preservation, navigation actions can become a pain.

Let’s say a user hides the video player, and when they show it again, playback resets to the beginning. It’s one of those annoying issues that makes people wish they were watching their favorite videos somewhere else.

Now if you’re using React, this happens because React unmounts components when they're hidden, destroying all their state in the process.

In this post, we’re going to walk through three scenarios that build up to solving this problem using [React 19.2’s](https://react.dev/reference/react) new <Activity> component with [Mux Player](https://www.mux.com/docs/guides/mux-player-web)—covering the pitfalls along the way and ending with the smoothest out-of-the-box solution React has to offer.

Before React 19.2, you might have handled showing and hiding components with conditional rendering, like this:

tsx

CheckCopiedCopyCopyCheckCopiedCopyCopy

```
(`{isVideoTab ? <VideoPlayer /> : null}`)
```

Hiding the video player component unmounts it. When users return, React mounts a fresh instance, and the video starts from the beginning. Any playback progress is lost.

Like I said before, for streaming applications, this creates a poor user experience. It's like watching the latest episode of your favorite show: you hide the player to take a break, and when you’re ready to continue, you bring it back—only to find the episode has restarted from the beginning.

The <Activity> component introduces a new way to handle visibility in React. Instead of mounting and unmounting components, <Activity> keeps them in the DOM while toggling their visibility state. The component accepts a *`mode`* prop with two values:

- **Visible**: The component is displayed and interactive
- **Hidden**: The component stays mounted but becomes invisible

**Here's a basic example:**

tsx

CheckCopiedCopyCopyCheckCopiedCopyCopy

```
<Activity mode={activeTab === "video" ? "visible" : "hidden"}>
  <VideoPlayer />
</Activity>
```

In our examples we use tabs/buttons for the show and hide action. The Activity component keeps the video player mounted when you switch tabs, preserving all of its internal state: current playback position, buffered content, volume settings, and everything else.

Okay now it’s time to show you some of that new React secret sauce. Let's walk through three implementations, each building on the lessons of the previous one.

This example is super straight forward. It’s a classic implementation of conditional rendering. However nowadays we don’t have to do this anymore.   
  
Lets break it down:

tsx

CheckCopiedCopyCopyCheckCopiedCopyCopy

```
{isVideoTab ? (
  <div>
    <Player autoPlay muted />
  </div>
) : (
  <div>
    <NotesPanel />
  </div>
)}
```

When you switch from the video tab to notes, React unmounts the <Player> component entirely. When you switch back, a new instance mounts and playback starts from the beginning.

When you play a video, switch to the notes tab, and then come back, it starts over at 0:00. All progress is lost.

Looking at the implementation, this example uses straightforward conditional rendering. No <Activity> wrapper means the player component gets destroyed and recreated on every tab switch.

React's standard lifecycle treats component removal as permanent. There's no built-in mechanism to "pause" a component and bring it back with its state intact.

Now this is a little bit more like it! Here we're using the Activity component but it could be better.

tsx

CheckCopiedCopyCopyCheckCopiedCopyCopy

```
<Activity mode={isVideoTab ? "visible" : "hidden"}>
  <div>
    <Player autoPlay muted />
  </div>
</Activity>

<Activity mode={!isVideoTab ? "visible" : "hidden"}>
  <div>
    <NotesPanel />
  </div>
</Activity>
```

In this example the player stays mounted when hidden, preserving playback position. However, there's a catch: the video continues playing in the background. Users can switch to the notes tab, but audio keeps playing from the hidden video. Now this may or may not be the experience we’re looking for so I won’t say that this is wrong or incomplete. This is just a different way of doing things with the <Activity> component.

The <Activity> component sets display: none on hidden content, but it doesn’t stop JavaScript execution or media playback. As you can see, state preservation works fine. The video element remains in the DOM, so when you return to the video tab, playback continues exactly where it left off.

Nothing tells the video to pause when it’s hidden. So if we want users to keep their place in the latest episode of *The Pitt*, we’ll need to switch things up a bit in the next example.

[![](/images/transparent.png)](https://stream.mux.com/ZuL9oAjypgh3RC9hDJGtJetSOSeft6fb/highest.mp4)

To pick it up a notch we need to combine <Activity> with a useLayoutEffect hook that pauses the player when hidden.

tsx

CheckCopiedCopyCopyCheckCopiedCopyCopy

```
const PausingPlayerPanel = ({ isVisible, idPrefix }: PausingPlayerPanelProps) => {
  const playerRef = useRef<MuxPlayerElement | null>(null);

  useLayoutEffect(() => {
    const player = playerRef.current;
    return () => {
      player?.pause();
    };
  }, [isVisible]);

  return (
    <div hidden={!isVisible}>
      <Player autoPlay muted ref={playerRef} />
    </div>
  );
};
```

Heres how we wrap it with <Activity>:

tsx

CheckCopiedCopyCopyCheckCopiedCopyCopy

```
<Activity mode={isVideoTab ? "visible" : "hidden"}>
  <PausingPlayerPanel isVisible={isVideoTab} idPrefix="finished" />
</Activity>
```

When isVisible changes from true to false, the effect cleanup function runs and pauses the video before the tab switches. The <Activity> component keeps the player mounted, so the pause position is preserved. When you return, the player is still paused at the exact moment you left.

When we play the video and switch to the notes tab, it pauses immediately and silently. When you return to the video tab, you can pick up exactly where you left off.

The useLayoutEffect hook with [isVisible] dependency ensures the cleanup function runs synchronously before the browser paints the tab switch.

The key is using useLayoutEffect instead of useEffect. useLayoutEffect runs synchronously before the browser paints, ensuring the video pauses before the user perceives any transition. With useEffect, there could be a brief moment where audio plays from the hidden tab.

This solution give you the best of both worlds:

- State preservation from <Activity> (playback position, buffered content, player settings)
- Controlled playback behavior from the effect hook (no background audio)

The <MuxPlayer> component (find it in the repo at: src/components/player.tsx) is a thin wrapper around @mux/mux-player-react that forwards refs and sets some defaults:

tsx

CheckCopiedCopyCopyCheckCopiedCopyCopy

```
const Player = forwardRef<MuxPlayerElement, PlayerProps>(
  ({ playbackId = DEFAULT_PLAYBACK_ID, streamType = "on-demand", ... }, ref) => (
    <MuxPlayer ref={ref} playbackId={playbackId} {...rest} />
  )
);
```

The ref forwarding is crucial. It allows the parent component to access the underlying video element and call methods like pause() directly. Without this ref, the useLayoutEffect cleanup function couldn't pause the player.

The three examples in the app share the same <Player> component but differ in their state management:

1. **UnmountedExample**: Conditional rendering (no <Activity>)

2. **HiddenButPlayingExample**: <Activity> wrapper only

3. **FinishedExample**: <Activity> wrapper + useLayoutEffect with pause logic

The <Activity> component pattern solves certain state preservation issues elegantly while keeping the code easy to read. Keep in mind that it's not just useful for video players—this same approach works for some of the following examples:

- **Forms with unsaved data**: Keep form state when users switch tabs to reference other content
- **Data tables with filters**: Preserve sort, filter, and scroll position across navigation
- **Canvas or drawing apps**: Maintain complex drawing state when toggling tool palettes
- **Music players**: Continue playback while navigating through a music library

If you're adding this pattern to your own video app, here's what you need:

1. **Upgrade to React 19.2** to access the <Activity> component

2. Wrap your video player in <Activity> with conditional mode prop

3. Forward refs from your player component so parent components can access the video element

4. Add useLayoutEffect with pause logic that triggers on visibility changes

React's <Activity> component is a game-changer for building stateful UIs with complex navigation.

Whether you're building an educational platform, streaming service, or even just a video on a landing page, React's <Activity> component can be super useful. Clone the [repo](https://github.com/muxinc/Mux-React-Activity) and run it locally to experience the difference yourself.
