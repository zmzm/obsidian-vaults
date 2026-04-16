---
type: twir-item
issue: 264
item: 5
item_type: item
date: 2026-01-14
source: https://handlewithcare.dev/blog/transition_low_priority_editor_updates/
tags:
status: auto
quality: keep
---

[[2026-01-14-TWIR-264|Index]]

# Item 5: Using React Transitions for low-priority text editor updates

Source: [https://handlewithcare.dev/blog/transition_low_priority_editor_updates/](https://handlewithcare.dev/blog/transition_low_priority_editor_updates/)

Summary:
The article demonstrates using React’s Transition APIs (useDeferredValue, startTransition) to deprioritize non-critical UI updates in a rich text editor scenario. By deferring updates to a preview component, the main editor remains responsive, even as complex renders occur elsewhere. The author also discusses potential pitfalls, such as state tearing, and advises caution when using deferred state for anything that could mutate data.

Key takeaways:
- React Transitions can improve perceived performance by making secondary UI updates interruptible.
- useDeferredValue is effective for lagging non-essential components (e.g., previews) behind immediate user interactions.
- Care must be taken to avoid using deferred state for mutations, as it may be stale.
- For most editors, React ProseMirror is already fast enough; this pattern is for edge cases.

Recommendation:
Read fully (for advanced performance tuning or complex editor UIs)

Why it matters:
for advanced performance tuning or complex editor UIs

Content:
# Using React Transitions for low priority text editor updates

Recently, I was working on performance improvements for a client whose product
includes a text editor. Specifically, they have what I would consider a “very
rich” text editor, with several layers of complex, interactive node types. We
were in the process of migrating them to use
[React ProseMirror](https://github.com/handlewithcarecollective/react-prosemirror),
which is, generally speaking, quite fast. Even for very large documents, React
ProseMirror easily stays under 10ms per update by utilizing a high level of
ProseMirror-aware memoization, limiting React re-renders to only the nodes whose
content actually changed.

In addition to being fast, React ProseMirror attempts to provide an idiomatic
React interface for ProseMirror. This means that, among other things, it's
possible to
[lift the EditorState](https://react.dev/learn/sharing-state-between-components#lifting-state-up-by-example)
out of the ProseMirror component and make use of it elsewhere in the tree. We
were making good use of this pattern for our client — a single EditorState
powered both the primary text editor and a scaled down, read-only preview of the
editor.

This introduces a new performance challenge. With each update, we're now
re-rendering at least twice as many node view components as necessary — one set
in the primary editor, and one set in the preview. And what if, as in this case,
we have other furniture around our primary editor that needs to react to changes
to the EditorState, as well?

This is, I think, an excellent use case for React's Transition APIs. These APIs
(`useDeferredValue`, `startTransition`, and `useTransition`) lets us tell React
that an update should be “non-blocking” — that is, any resulting render should
be prioritized below an “immediate” (non-Transition) render, and can be
interrupted if another immediate render starts before it finishes. We don't want
to use this for our primary editor, nor for any components that mark up or are
positioned around our primary editor. Those need to be updated immediately as
the user makes changes. Other components, though, such as the preview editor, do
*not* need to be updated immediately — it's acceptable if the preview editor
contents lag a fraction of a second behind the user's input.

Let's walk through how we could implement this pattern. This is a stripped down
version of our starting point:

```
export function Editor() {

const [editorState, setEditorState] = useState(() =>

EditorState.create({

schema,

plugins: [reactKeys()],

}),

);

return (

<>

<aside>

<ProseMirror static state={editorState}>

<ProseMirrorDoc />

</ProseMirror>

</aside>

<main>

<ProseMirror

state={editorState}

dispatchTransaction={(tr) => {

setEditorState((prev) => prev.apply(tr));

}}

>

<ProseMirrorDoc />

</ProseMirror>

</main>

</>

);

}
```

We’re using the new `static` prop to render our preview editor as a static
document. This means that it won’t mount an EditorView or any of the event
listeners, and that `contenteditable` will be set to `false`.

This is a demo editor. I've intentionally introduced ~20 ms of lag per render to imitate a complex React component with a slow render function.

As you type, every node that renders will flash.

Notice how the main and preview editors both flash immediately on every change. If you type quickly, both cards will be highlighted continuously.

This has the issue that we identified earlier. Any time the main editor is
updated, the preview editor will also need to be re-rendered, because its
`state` prop will also have changed.

To resolve this, we need to introduce a second piece of state, the “deferred”
EditorState. We’ll update this state with a Transition, so that any re-renders
it triggers will be deprioritized and interruptible.

```
export function Editor() {

const [editorState, setEditorState] = useState(() =>

EditorState.create({

schema,

plugins: [reactKeys()],

}),

);

const deferredEditorState = useDeferredValue(editorState);

<ProseMirror static state={deferredEditorState}>

<ProseMirrorDoc />

</ProseMirror>

</aside>

<main>

<ProseMirror

state={editorState}

dispatchTransaction={(tr) => {

setEditorState((prev) => prev.apply(tr));

}}

>

<ProseMirrorDoc />

</ProseMirror>

</main>

</>

);

}
```

This is a demo editor that uses Transitions. Again, I've intentionally introduced ~20 ms of lag per render to imitate a complex React component with a slow render function.

As you type, every node that renders will flash.

Notice how only the main editor flashes immediately on every change. If you type one character at a time, you'll see the preview editor flash a moment later. If you type several characters very quickly, you'll see that the preview editor does not flash at all until you pause for a moment.

Play around with those demo editors a bit to get a sense for the difference. The
editor with Transitions effectively has a render-aware debounce — if it manages
to complete its render before it gets interrupted, then the user will see the
result. If not, the render will be cancelled and tried again after the higher
priority render finishes.

To scale this up, we can put the deferred EditorState in a context and create a
hook, `useDeferredEditorState`, for consuming it. This would allow us to tack on
more consumers of the EditorState without slowing down the editing experience
for the primary editor.

For these reasons, this pattern may never make it into the React ProseMirror
library itself. Safety is a priority for React ProseMirror, and we try to avoid
introducing any footguns. The good news is that for most editors, React
ProseMirror is already fast enough that you’re unlikely to need to use
Transitions yourself. Notably, I had to manually add 20 ms of delay to the
`CardNodeView` component’s render function in order to even demonstrate the
utility of Transitions — without the delay, both demo editors appeared to update
the preview card instantly!
