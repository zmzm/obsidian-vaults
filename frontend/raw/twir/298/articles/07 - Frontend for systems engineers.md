---
type: twir-item
issue: 298
item: 7
item_type: item
date: 2026-09-23
source: https://tj-zhang.com/blog/frontend-for-systems-engineers/
tags:
status: auto
quality: keep
---

[[2026-09-23-TWIR-298|Index]]

# Item 7: Frontend for systems engineers

Source: [https://tj-zhang.com/blog/frontend-for-systems-engineers/](https://tj-zhang.com/blog/frontend-for-systems-engineers/)

Summary:
This article explains React’s data flow and rendering model from a systems engineering perspective, using a collaborative video playlist as an example. It covers how React derives views from state and props, manages local state, synchronizes with external systems via Effects, and the importance of keeping state and derived values separate. The piece also highlights common pitfalls, such as unnecessary state duplication and improper synchronization, and demonstrates best practices for predictable UI updates.

Key takeaways:
- React components are pure functions deriving the UI from state and props; the DOM is a materialized view.
- Local state should be owned at the appropriate component level and updated via event handlers.
- Effects are for synchronizing with external systems (e.g., media players), not for deriving UI state.
- Avoid copying derived values into state; derive them directly in render for consistency and atomic updates.

Recommendation:
Read fully

Content:
# Frontend for systems engineers

Consider a watch-together room with a shared playlist beside an embedded YouTube
player. You are watching on a laptop when Alice selects âDune: Part Twoâ from
her phone. Your laptop should highlight that row, show its title, and load the
selected video.

Select a video or toggle the playlist in this local demo. The player is simulated.

For each fact, we will identify its **owner**, the views **derived** from it,
and the **synchronization boundary** an update must cross.

We will build the room one capability at a time: display the playlist, toggle
the sidebar, control the player, remember the selection across reloads, then
share it between devices.

## Rendering derives the view

Our room's UI is a **tree of components**. React **renders** that tree to
compute a view, then **commits** its changes to the browser DOM:[1](#user-content-fn-engine)

render + commit

React renderer

Browser DOMDerived view

The room's [**render tree**](https://react.dev/learn/understanding-your-ui-as-a-tree#the-render-tree)
has `WatchRoom` at its root. Start with a fixed playlist, `videos`, and a
selected video ID, `selectedId`, as its inputs. It supplies its children with
**props**: the inputs each parent passes to its child components.

React component treeWatchRoom contains PlayerPanel and Playlist. PlayerPanel contains YouTubePlayer.WatchRoomPlayerPanelYouTubePlayerPlaylist

A component is a function that returns **React elements** describing its UI,
usually written in **JSX**. JSX describes the elements React should create;
braces insert values computed in JavaScript. For a video whose `title` is
`"Dune"`, this JSX:

asks React to create the DOM structure represented by this HTML:

`WatchRoom` looks up the selected video and supplies each child with the
inputs it needs:

```
function WatchRoom({ videos, selectedId }) {

const selectedVideo = videos.find(

(video) => video.id === selectedId,

<PlayerPanel video={selectedVideo} />

<Playlist videos={videos} selectedId={selectedId} />
```

On the initial render, React calls `WatchRoom`, then calls the children it
returns with their supplied props. It follows their children in turn until
it has worked out the DOM to produce. This evaluation of the component tree
is [**rendering**](https://react.dev/learn/render-and-commit#step-2-react-renders-your-components).

Each component is written as a
[**pure function**](https://react.dev/learn/keeping-components-pure): the same
inputs produce the same output, without changing those inputs or external
systems. `PlayerPanel` displays `video.title` beneath `YouTubePlayer`;
`Playlist` highlights the row matching `selectedId`.

The title and highlight agree by construction: both are **derived views** of
`selectedId` and the playlist. Changing `selectedId` gives the tree a new
input from which to compute both.

Think of the DOM as a
[**materialized view**](https://martin.kleppmann.com/2015/03/04/turning-the-database-inside-out.html#:~:text=You%20may%20already%20know%20what%20materialized%20views%20are)
of these inputs: components define the derivation, and React maintains the
view as the inputs change.

React compares the rendered output with the previous tree, then **commits**
the necessary changes to the browser DOM. The browser paints the updated UI.

## React owns local UI state

A selection should change when we click a playlist row. Let `WatchRoom` own
that choice: replace its `selectedId` prop with local state. It also owns
whether the sidebar is open:

```
const [selectedId, setSelectedId] = useState(videos[0].id)

const [isPlaylistOpen, setIsPlaylistOpen] = useState(true)
```

read

render + commit

set stateâsidebar toggle

React stateOwns sidebar visibility

React renderer

Browser DOMDerived view

React retains each value across renders while the same component instance
remains in the UI tree.
An **event handler** responds to a click: `WatchRoom` passes `setSelectedId`
to `Playlist` as an `onSelect` prop, and a row calls `onSelect(video.id)`.
The next render derives the new title and highlight from that selection.

The sidebar toggle calls `setIsPlaylistOpen(open => !open)`. `WatchRoom`
then includes or omits `Playlist`; the selected video is unchanged.

### Derived views become visible together

When `selectedId` changes, `PlayerPanel` and `Playlist` compute a new title
and highlight from the same inputs. Their output is a **candidate view**;
finishing one component does not publish it independently.

Once the candidate is ready, React [**commits**](https://react.dev/learn/render-and-commit#step-3-react-commits-changes-to-the-dom)
the necessary DOM changes without yielding. The browser does not paint
between those mutations, so the title and highlight become visible together.
This publication covers one **React root**, the tree managed by one React
entry point; it does not include the embedded playerâs independently owned state.

Derivation makes the values agree; commit makes their DOM changes visible
together. Keep props and state [**immutable**](https://react.dev/reference/rules/components-and-hooks-must-be-pure#props-and-state-are-immutable)
so calculations use the supplied values without changing each otherâs inputs.

## Effects synchronize with the player

read

render + commit

set stateâsidebar toggle

synchronize

React stateOwns sidebar visibility

React renderer

Browser DOMDerived view

YouTube playerPlayback state

Updating the title and highlighted row does not ask the embedded player to
load the video. `selectedId` expresses the desired video; the player owns
what is actually loaded and needs its own command.

Calling the player during rendering would let an unfinished candidate change
that external state. If React abandoned the candidate, the player could load
a video that never appeared in our UI. Instead,
[`useEffect`](https://react.dev/reference/react/useEffect#controlling-a-non-react-widget)
registers code to run after commit. An Effect in `YouTubePlayer` asks the
embedded player to load the committed selection. Assuming `player` is ready
and its instance stays the same between renders:

```
player.loadVideoById(selectedId)
```

Its [**dependency list**](https://react.dev/reference/react/useEffect#specifying-reactive-dependencies)
names the component values that code reads, including the selected videoâs ID. The Effect
runs after the first commit, and again after a commit in which a dependency
changed. It compares each dependency with its previous value using
`Object.is`. Closing the sidebar leaves the selection unchanged, so it does
not reload the player.

React derives the title and highlight from the selected video during rendering.
The player needs an Effect because its state lives outside that process.
Keep values such as `video.title` derived in render; copying them into state
and synchronizing the copy with an Effect adds an unnecessary update.

Why not synchronize the title with an Effect?

A common mistake is to copy a value derived from props into state, then use
an Effect to keep the copy in sync. Here, that would mean storing
`video.title` separately. Showing only the title rendering in `PlayerPanel`:

```
function PlayerPanel({ video }) {

const [title, setTitle] = useState(video.title)
```

When selection changes from video A to video B, the title copy still holds A's
title. React must commit before this Effect can request the correction:

Each commit applies its DOM changes together, but the first commit is
**inconsistent**. The extra state has split one logical update across two
commits, and the intermediate result can produce a visible flash.
Instead, [**derive the title during rendering**](https://react.dev/learn/you-might-not-need-an-effect#updating-state-based-on-props-or-state):

```
function PlayerPanel({ video }) {

return <h2>{video.title}</h2>
```

The title now follows the selected video in the same render as the highlight.
No extra state or Effect is needed.

## Remember selection across reloads

Until now, React owned selection through `useState`. To preserve it across
reloads, we move its durable record to
[**IndexedDB**](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API),
the browser's built-in transactional database. **IndexedDB now owns selection;**
React becomes a reader of that externally owned state.

IndexedDB reads are asynchronous. The **client store** exposes a synchronous,
in-memory snapshot for rendering and notifies React when it changes.

replicate

read

render + commit

set stateâsidebar toggle

synchronize

commandâplaylist click

IndexedDBOwns selection

Client storeCached selection

React stateOwns sidebar visibility

React renderer

Browser DOMDerived view

YouTube playerPlayback state

The client store also acts as the write adapter: after the IndexedDB transaction
[**commits**](https://developer.mozilla.org/en-US/docs/Web/API/IDBTransaction/complete_event),
previous selection displayed. Reloading reads the saved selection again.

This snapshot replaces React's `selectedId` state; the title and highlight derive
from it. Sidebar visibility stays in React state because it only needs to survive
the current visit.

### Connect the store to React

An **external store** is external to React, even when it lives in the same
browser. React reads its snapshot and registers a callback that the store
invokes when it changesâa **subscription**. Updating the store alone does not
request a React render.

Reading a snapshot into `useState` and subscribing in an Effect leaves a gap:
the store can change between the read and the subscription. If React pauses between components that read the store independently,
those components can observe different versions. React needs to coordinate those reads with rendering
so the committed view stays consistent.

[`useSyncExternalStore`](https://react.dev/reference/react/useSyncExternalStore)
provides that coordination: it manages the subscription and
[checks that snapshots remain consistent before committing](https://react.dev/reference/react/useSyncExternalStore#caveats).

snapshot for the component to render.

In our browser-rendered `WatchRoom`:

```
const { selectedId } = useSyncExternalStore(
```

This depends on the [store's snapshot contract](https://react.dev/reference/react/useSyncExternalStore#parameters):
`getSnapshot` must return an immutable value, and repeated calls must return the
same value while the relevant data is unchanged. React compares snapshots with
`Object.is`; a fresh object on every read would look like a change every time.

The lookup and props passed to its children stay the same; `isPlaylistOpen`
still uses `useState`. A libraryâs React hook can package this connection.
Committing the database write and keeping React's view consistent with its
cached result are separate responsibilities.

Why arenât useState and an Effect enough?

To see what the hook must coordinate, try connecting the store with the
primitives we already know:

1. During rendering, read the store's current **snapshot** into `useState`.
2. Use an **Effect** to register a callback after the component is first added
   to the UI tree (**mounts**) and committed. The store calls that callback when
   so React removes it when the component leaves the tree (**unmounts**).
3. Inside that callback, read the latest snapshot and call the state setter to
   request another render.

Subscribing during rendering could leave a live subscription behind for a render
React abandons.

**Avoid a race when subscribing**

The initial `useState` read happens during rendering; the subscription Effect
runs after commit. Suppose React reads selection A, then a pending database write
commits selection B and refreshes the client store. No listener exists yet to
receive that update:

Render component

Read snapshot

Video A selected

Return elements for A

Commit A

Cache refreshed to B

No update requestedUI still shows A

React renderer

React renderer

Component

Component

Client store

Client store

To close this [**subscription setup race**](https://www.postgresql.org/docs/18/sql-listen.html#id-1.9.3.153.7),
from the value rendered, call the setter to request another render. The reread
catches changes missed before listening started; the subscription handles
later changes.

**Keep the committed view consistent**

That reread repairs a missed update after commit. It cannot prevent an
inconsistent view from being committed.

Suppose a [**non-blocking navigation**](https://react.dev/blog/2022/03/29/react-v18#what-is-concurrent-react)
mounts the room. `PlayerPanel` and `Playlist` each initialize their own
`useState` copy by reading the store, instead of receiving selection through
`WatchRoom`. React can pause between those components. If the cache refreshes to B
during that pause:

Committing this result would display A's title while highlighting B. React
calls this visible inconsistency [**tearing**](https://github.com/reactwg/react-18/discussions/69).
Both components derive their views correctly, but from different versions of
the same source. Publishing their output together does not make it consistent.

Reactâs [external-store interface](https://github.com/reactjs/rfcs/blob/main/text/0214-use-sync-external-store.md#detailed-design)
can read the current snapshot; it cannot request an older version for the
rest of a render. Instead, React **validates before commit**: reread the
snapshots used to prepare the view and retry if they changed. This is the
[**optimistic concurrency control**](https://www.eecs.harvard.edu/~htk/publication/1981-tods-kung-robinson.pdf#page=3)
pattern applied to publishing a view.

`useSyncExternalStore` retries a changed snapshot as a blocking update.
Finishing that retry without yielding prevents another ordinary JavaScript
callback from changing the store between component reads and commit.

## Share selection between devices

Remembering a selection on one device is enough for personal viewing. To watch
together, Alice and Bob need one shared selection. The backend owns the room's
`selectedId`, and each client store holds a **replica**.[2](#user-content-fn-local-first) The
connection from the client store to React stays the same.

replicate

read

render + commit

set stateâsidebar toggle

synchronize

commandâplaylist click

BackendOwns room state

Client storeCached selection

React stateOwns sidebar visibility

React renderer

Browser DOMDerived view

YouTube playerPlayback state

A playlist click now sends a command to the backend. After accepting the change,
the backend replicates the updated selection to the clients.[3](#user-content-fn-optimistic) Each client store
notifies React, which reads its snapshot and derives the title and highlight.
After commit, the existing player Effect loads the selected video.

Sidebar visibility remains local: opening Alice's sidebar should not open Bob's.

### Where libraries fit

Libraries package these responsibilities in different combinations; one product
may handle both synchronization and the React connection.[4](#user-content-fn-sync-landscape)

**Backend to client store.** Synchronization keeps the client's state current
as the shared room changes:

replicate

BackendOwns room state

Client storeCached selection

React renderer

What crosses this boundary differs by library.
[Electric](https://electric.ax/docs/sync/) delivers Postgres record changes;
[Convex](https://docs.convex.dev/understanding/overview) keeps backend query
results updated on clients; [LiveStore](https://livestore.dev/) synchronizes
events and derives local SQLite tables from them. Each maintains client state
from which the UI is derived, but the synchronized data and the location of
that derivation differ.

**Client store to React.** Once state is available locally, the React integration
exposes a stable snapshot and notifies React when it changes:

replicate

BackendOwns room state

Client storeCached selection

React renderer

[TanStack DB](https://tanstack.com/db/latest/docs/overview)
maintains client collections and live queries; its
[React integration](https://github.com/TanStack/db/blob/main/packages/react-db/src/useLiveQuery.ts)
uses `useSyncExternalStore` to connect query results to rendering. It can work
with different data sources.[5](#user-content-fn-stores)

## The complete room

replicate

read

render + commit

set stateâsidebar toggle

synchronize

commandâplaylist click

BackendOwns room state

Client storeCached selection

React stateOwns sidebar visibility

React renderer

Browser DOMDerived view

YouTube playerPlayback state

Alice selects *Dune: Part Two* on her phone. Her playlist's event handler
sends a selection command to the backend. The backend accepts the change and
updates the authoritative room record.

Replication brings the accepted selection to Bob's client store, which
notifies React through its subscription. React reads the updated snapshot,
derives the title and playlist highlight from that selection, and commits
the DOM changes together.

After commit, Bob's player Effect asks the embedded player to load the selected video. Bob never clicked a
video: the Effect follows the committed selection, so Alice's change reaches
his player too.

Bob then clicks the sidebar toggle to give the video more room. Its event
handler requests that his local `isPlaylistOpen` become `false`. React omits
the playlist in the next render and commits the new layout. The player
Effect's dependencies are unchanged, so it does not load the video again.
Alice's sidebar is unchanged because its visibility belongs to her own client.

The familiar work is in the data: thinking carefully about ownership,
derivation, and synchronization. Get those relationships right, and React
handles the last mile from data to UIâkeeping the rendered view consistent
and up to date.
