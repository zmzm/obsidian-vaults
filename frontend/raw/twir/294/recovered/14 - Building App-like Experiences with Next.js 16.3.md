---
type: "twir-recovery"
issue: 294
item: 14
source: "https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3"
final_url: "https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3"
retrieved: "2026-10-22T11:30:06+00:00"
original_note: "frontend/raw/twir/294/articles/14 - Building App-like Experiences with Next.js 16.3.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/14 - Building App-like Experiences with Next.js 16.3|Building App-like Experiences with Next.js 16.3]]

---
title: Building App-like Experiences with Next.js 16.3
description: Build app-like experiences with Instant Navigations, server-rendered data, optimistic updates, and live client state in Next.js 16.3.
url: "https://nextjs.org/blog/building-app-like-experiences-with-nextjs-16-3"
docs\_index: /docs/llms.txt
publishedAt: August 18th 2026
authors:
- Aurora Scharff
---
We released [Next.js 16.3](/blog/next-16-3) earlier this month with [Instant Navigations](/blog/next-16-3-instant-navigations), powered by Cache Components and Partial Prefetching. Cache Components make sure a route has UI it can show immediately, while Partial Prefetching brings that UI to the browser before someone clicks. Together, they give you the responsive navigation people expect from a single-page application (SPA), without giving up the benefits of Server Components.
Let's see how these features come together in a set of demo apps: the music player [Next Beats](https://next-beats.dev/), the social feed [Drop](https://next16-social-media.vercel.app/), the calendar [Flow](https://next16-calendar.vercel.app/), and the team chat [Huddle](https://next16-team-chat.vercel.app/).
## Navigating instantly
With Instant Navigations, you can click around and the next page is there right away, the way a single-page app feels.
In [Next Beats](https://next-beats.dev/), watch the loading fallback appear as soon as a track or playlist is selected:
The pages still render on the server. Cache Components ensure an initial prerendered shell of static, cached, and fallback UI, with dynamic content streaming through Suspense.
Partial Prefetching fetches that shell for visible `` components before the click and reuses one shell across links to the same route. The browser can show the prefetched UI immediately while the server finishes the rest.
Next Beats enables both features in `next.config.ts`:
```ts {4-5} filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
cacheComponents: true,
partialPrefetching: true,
};
export default nextConfig;
```
Read the [Instant Navigations guide](/docs/app/guides/instant-navigation) to see how to structure routes with UI ready when someone clicks. If your project is not using Cache Components yet, follow the [Cache Components migration guide](/docs/app/guides/migrating-to-cache-components), or give your coding agent the [adoption Skill](https://github.com/vercel/next.js/tree/canary/skills/next-cache-components-adoption).
## Caching across navigations
A loading fallback makes the first visit responsive. With Cache Components, the data behind a page can persist across navigations, so a revisit can skip that fallback.
In [Drop](https://next16-social-media.vercel.app/), compare the first visits to Home and Profile with the return visits at the end:
Mark the read with [`'use cache'`](/docs/app/api-reference/directives/use-cache) so Next.js can reuse the result instead of querying the data source on each render. The cached function's arguments become part of the cache key, and [`cacheLife`](/docs/app/api-reference/functions/cacheLife) can adjust how long the result stays fresh.
The browser also caches prefetched and visited route payloads. While a payload stays fresh, revisiting the page can reuse it without another server request.
In Drop, the post ID becomes part of the cache key, and the read adds tags that a later mutation can expire:
```ts {4-6} filename="features/drop/drop-queries.ts"
import { cacheLife, cacheTag } from 'next/cache';
async function getDrop(id: string) {
'use cache';
cacheLife('minutes');
cacheTag('drops', `drop-${id}`);
const row = await prisma.drop.findUnique({ where: { id } });
if (!row) notFound();
return toDrop(row);
}
```
Learn more about [caching in Next.js](/docs/app/getting-started/caching), including how cached data is reused and revalidated.
## Prefetching URL-specific content
Caching speeds up revisits. With Partial Prefetching, a first visit can arrive with more of its content already in place.
Back in [Next Beats](https://next-beats.dev/), notice how the track header is already there during the second set of clicks while the recommendations continue loading:
By default, a visible [``](/docs/app/api-reference/components/link) prefetches one App Shell per destination route, shared by links to that route. Static and cached content can be part of the shell, while dynamic or URL-dependent content streams in after navigation.
Add [`prefetch={true}`](/docs/app/api-reference/components/link#prefetch) when a specific link should also resolve its `params`, `searchParams`, or full URL before the click. URL-dependent reads marked with `'use cache'` can then be included in that link's prefetch, so a product or detail page arrives with its content ready.
A visible link with `prefetch={true}` can invoke the server as it enters the viewport, so use it where having the content ready is worth the request. The track links in Next Beats opt in:
```tsx {3}
import Link from 'next/link';
{track.title}
;
```
Read the [prefetching guide](/docs/app/guides/prefetching) for the default behavior and intent-triggered patterns, and [optimizing prefetching](/docs/app/guides/optimizing-prefetching) for URL-specific content and the trade-offs of `prefetch={true}`. To update an existing app, follow the [Partial Prefetching adoption guide](/docs/app/guides/adopting-partial-prefetching), or let your coding agent work through it with the [adoption Skill](https://github.com/vercel/next.js/tree/canary/skills/next-partial-prefetching-adoption).
## Adding client-side interactivity
Fast pages still need responsive controls. With Client Components, you can make the interactive parts of a page respond immediately while data fetching stays on the server.
In [Next Beats](https://next-beats.dev/), watch the play button, now-playing bar, and track controls stay in step as the player starts, pauses, and skips:
Mark an interactive module with [`'use client'`](/docs/app/api-reference/directives/use-client). Its components can use state, event handlers, and browser APIs, while the rest of the route stays server-rendered and ships less JavaScript.
Shared state can live in a context provider and be read through a hook, so interactive parts across the tree stay in sync. Placing the provider in a shared layout keeps it mounted as routes change, while its `children` can remain Server Components.
The shared layout in Next Beats wraps both the route content and persistent controls in the provider:
```tsx filename="app/(app)/layout.tsx"
import { NowPlayingBar } from '@/components/now-playing-bar';
import { PlayerProvider } from '@/providers/player-provider';
export default function AppLayout({ children }: { children: React.ReactNode }) {
return (
{/\* ...navigation... \*/}
{children}

);
}
```
Read about [combining Server and Client Components](/docs/app/getting-started/server-and-client-components) to add interactive islands without moving the whole app into the browser.
## Revalidating after mutations
When interactive controls change server data, the cached views that show it need to stay in sync. You can keep the data cached and still see your changes immediately across pages.
In [Drop](https://next16-social-media.vercel.app/), watch a repost appear on Profile after adding it from Home, then disappear after removing it:
Tag a [`'use cache'`](/docs/app/api-reference/directives/use-cache) read with [`cacheTag`](/docs/app/api-reference/functions/cacheTag), then call [`updateTag`](/docs/app/api-reference/functions/updateTag) from the Server Action to expire that tag. The current page can show local feedback while the Action runs.
The next request for the tagged data fetches a fresh result. With [Partial Prefetching](/docs/app/guides/adopting-partial-prefetching), a visible [``](/docs/app/guides/optimizing-prefetching#resolve-url-data-at-prefetch-time) can fetch that update ahead of the click, so the fresh content is ready on navigation.
The tags to expire depend on where the changed data appears. In Drop, toggling a repost changes both the drop and the signed-in user's profile, so the Action expires both after the write:
```ts {11-12} filename="features/drop/drop-actions.ts"
'use server';
import { updateTag } from 'next/cache';
import { verifyAuth } from '@/features/user/user-queries';
export async function toggleRepost(dropId: string) {
const me = await verifyAuth();
// ...create or delete the repost in the database...
updateTag(`drop-${dropId}`);
updateTag(`user-drops-${me}`);
// ...expire other affected views...
return { ok: true as const };
}
```
See how [revalidation](/docs/app/getting-started/revalidating) keeps cached data fresh after a mutation.
## Handling connection drops
App-like experiences should also survive a temporary connection loss. When the connection drops mid-session, your app can wait it out and pick back up when you reconnect.
In [Next Beats](https://next-beats.dev/), watch what remains visible as tracks and playlists open offline, then how the unfinished playlist recovers after reconnecting:
With offline retry enabled, a failed soft navigation, React Server Component fetch, prefetch, or Server Action stays pending instead of throwing, then retries automatically. The [`useOffline`](/docs/app/api-reference/functions/use-offline) hook lets you show a reconnecting bar while it waits.
Because the App Shell was already prefetched, a soft navigation can still render it, along with any data included in that prefetch.
Offline support is currently experimental and subject to change, and is not
recommended for production.
Next Beats enables offline retry alongside Cache Components and Partial Prefetching:
```ts {7} filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
cacheComponents: true,
partialPrefetching: true,
experimental: {
useOffline: true,
},
};
export default nextConfig;
```
Read our guide on [handling connectivity drops](/docs/app/guides/offline-support) for the supported requests, retry behavior, and reconnecting feedback.
## Streaming with Suspense
Depending on what is cached and prefetched, sections of a route can become ready at different times. With [Suspense](https://react.dev/reference/react/Suspense), you can control how they are revealed so the page loads fast (LCP) and stays stable (CLS).
In [Drop](https://next16-social-media.vercel.app/), compare how the replies appear below a long post and a short one:
Sometimes you don't know the size of your content until it loads. If you split it into separate boundaries, they resolve independently and can push each other around as they land.
Instead, you can nest the boundaries. The work can still run in parallel, but the nested boundary waits to show a section until the one above it is in place. The page settles from the top down without delaying the work.
The Drop post route places the replies inside the boundary for the post above them:
```tsx {3,7,9,12} filename="app/drop/[id]/page.tsx"
import { Suspense } from 'react';
}>
{params.then(({ id }) => (
<>
}>
))}
;
```
Read the [streaming guide](/docs/app/guides/streaming) for more ways to reveal content with Suspense.
## Updating optimistically
Streaming keeps navigation responsive while data loads. For mutations, React features like transitions and optimistic updates can show feedback immediately, however slow the network is.
In [Next Beats](https://next-beats.dev/), watch playlists and favorites change before each save finishes, including what happens when a change is rejected:
A [`useTransition`](https://react.dev/reference/react/useTransition) tracks the Server Action and resulting server update as one pending operation. Starting the Action inside `startTransition` keeps the update in the same transition.
Set an optimistic value with [`useOptimistic`](https://react.dev/reference/react/useOptimistic) inside that transition to render it immediately. If the Action fails, React returns to the last confirmed value, and you can show an error toast.
The favorite button in Next Beats applies the optimistic value before calling the Server Action:
```tsx {7-8,11-13} filename="features/track/components/track-interactions.tsx"
'use client';
import { useOptimistic, useTransition } from 'react';
import { toggleFavorite } from '@/features/track/track-actions';
export function FavoriteButton({ trackId, isFavorite }: FavoriteButtonProps) {
const [, startTransition] = useTransition();
const [optimisticFavorite, setOptimisticFavorite] = useOptimistic(isFavorite);
function handleToggle() {
startTransition(async () => {
setOptimisticFavorite(!optimisticFavorite);
await toggleFavorite(trackId);
});
}
return (
Favorite
);
}
```
The [interactive apps guide](/docs/app/guides/interactive-apps) walks through transitions, optimistic updates, and Server Actions together.
## Composing complex apps
Fetching on demand or per user doesn't have to mean blocked navigations or endless spinners. These patterns compose into complex apps that respond immediately while still rendering and fetching data on the server.
In [Flow](https://next16-calendar.vercel.app/), notice how switching views navigates instantly with content already available, and how creating a calendar and editing events for the signed-in user update right away:
Server Components verify the signed-in user and authorize the data, while Client Components own the interactions. A client provider can share interaction state across Client Components while its server-rendered children continue to fetch and render the user's data on the server.
The Flow calendar places the provider around the streamed month or week view:
```tsx {1,11} filename="app/(workspace)/calendar/[date]/page.tsx"
}>
{Promise.all([params, searchParams]).then(([{ date }, { view }]) =>
toView(view) === 'month' ? (
) : (
),
)}
```
Partial Prefetching prepares the route before the click, and dynamic data streams through the Suspense fallback. When another change happens before the previous save finishes, the provider can run the saves in order with `useActionState` and keep the pending changes on screen with `useOptimistic`.
The provider dispatches each change inside a transition:
```tsx {16,24,30-32} filename="providers/calendar-events-provider.tsx"
'use client';
import {
startTransition,
type ReactNode,
useActionState,
useOptimistic,
} from 'react';
import { toast } from 'sonner';
import { saveEventChange } from '@/features/calendar/calendar-actions';
import type { EventChange } from '@/features/calendar/types/calendar';
// ...context declarations...
export function CalendarEventsProvider({ children }: { children: ReactNode }) {
const [, dispatch] = useActionState(async (\_: void, change: EventChange) => {
const result = await saveEventChange(change);
if (result.error) {
toast.error(result.error);
}
// ...success toasts...
}, undefined);
const [pendingChanges, addOptimisticChange] = useOptimistic<
EventChange[],
EventChange
>([], (changes, change) => [...changes, change]);
function mutate(change: EventChange) {
startTransition(() => {
addOptimisticChange(change);
dispatch(change);
});
}
return (
{children}
);
}
```
## Fetching data on the client
Server Components can own most data fetching, but some interactions need the browser to keep server state synchronized as it changes. A client data library can poll for new data, revalidate on focus, dedupe requests, and coordinate updates across components without giving up the initial server render.
In [Huddle](https://next16-team-chat.vercel.app/), notice how Activity and unread markers clear, how the command palette searches on demand, then how replies remain available while moving between two Huddle Bot threads:
For on-demand data, fetch from the Client Component when the interaction needs the result. Handle the loading state inside the component with [`useSWR`](/docs/app/guides/client-side-data-fetching/swr) or [`useQuery`](/docs/app/guides/client-side-data-fetching/tanstack-query), or at a Suspense boundary with `suspense: true` or `useSuspenseQuery`.
When the initial view needs the data, start the request in a Server Component and provide it through [`SWRConfig`](/docs/app/guides/client-side-data-fetching/swr) or [`HydrationBoundary`](/docs/app/guides/client-side-data-fetching/tanstack-query). This avoids a client waterfall, and the browser can take over polling, on-demand queries, and optimistic updates when the data arrives.
In Huddle's SWR branch, the Server Component preloads the messages and passes them to the client tree through `SWRConfig`:
```tsx {8-10,13} filename="features/message/components/message-thread.tsx"
import { preload, SWRConfig } from 'swr';
import { messageKeys } from '@/features/message/message-cache';
import { getMessagesForUser } from '@/features/message/message-queries';
export async function MessageThread({ channelId }: { channelId: string }) {
const user = await getCurrentUser();
const messageData = preload(messageKeys.channel(channelId), () =>
getMessagesForUser(channelId, user.id),
);
return (

);
}
```
The Client Component reads the same key with suspense enabled and continues polling from there:
```tsx {8-11} filename="features/message/hooks/use-messages.ts"
'use client';
import useSWR from 'swr';
import { messageKeys } from '@/features/message/message-cache';
import { fetchJson } from '@/lib/fetch-json';
export function useSuspenseMessages(channelId: string) {
return useSWR(messageKeys.channel(channelId), fetchJson, {
refreshInterval: 10\_000,
suspense: true,
});
}
```
Read the [client-side data fetching guide](/docs/app/guides/client-side-data-fetching) for complete SWR and React Query examples.
## Animating with View Transitions
Once navigation, data, and mutations respond immediately, animation can make those changes easier to follow. With React's [``](https://react.dev/reference/react/ViewTransition), you can animate streamed reveals, list changes, and route transitions so content moves into place smoothly.
Watch streamed content fade in on [Drop](https://next16-social-media.vercel.app/), lists and nearby content move into place on [Next Beats](https://next-beats.dev/), and [Flow's](https://next16-calendar.vercel.app/) calendar slide with navigation:
### 1. Suspense reveals
In Drop, streamed feeds, posts, and replies are wrapped in a `` so they fade in when Suspense replaces the skeleton. A small wrapper handles each reveal:
```tsx {5} filename="components/ui/crossfade.tsx"
import { ViewTransition, type ReactNode } from 'react';
export function Crossfade({ children }: { children: ReactNode }) {
return (
{children}
);
}
```
On the post route, one `` wraps the post detail and another wraps the replies so the nested Suspense boundaries animate independently:
```tsx {4,7} filename="app/drop/[id]/page.tsx"
import { Suspense } from 'react';
}>

}>

;
```
### 2. Morphs
In Next Beats, removing a favorite shortens the list and gives the remaining rows and recommendations below it new positions. View Transitions animate those layout changes instead of letting the content jump. The favorite update already runs inside a transition, so React can capture the layout before and after the item is removed.
Wrap each keyed favorite in a `` so React can move the remaining rows into their new positions:
```tsx {5} filename="features/track/components/favorites-feed.tsx"
import { ViewTransition } from 'react';
{
tracks.map((track, i) => (
));
}
```
The shorter favorites list also moves the recommendations below it upward. A second `` animates that section into its new position:
```tsx filename="app/(app)/favorites/page.tsx"

```
### 3. Page transitions
A page transition can show whether navigation is moving forward or back. Flow's calendar links add transition types for both directions:
```tsx {6,14} filename="features/calendar/components/calendar-controls.tsx"
import Link from 'next/link';
Previous {period}
Next {period}
```
The Flow calendar maps those transition types to animation names on the content that changes, scoping the transition to the calendar board:
```tsx {18} filename="components/ui/directional-slide.tsx"
import { ViewTransition } from 'react';
import type { ReactNode } from 'react';
const directionalSlide = {
'nav-back': 'nav-back',
'nav-forward': 'nav-forward',
default: 'none',
};
export function DirectionalSlide({
children,
name,
}: {
children: ReactNode;
name: string;
}) {
return (
{children}
);
}
```
The class names style the old and new view-transition snapshots. For forward navigation, the old content moves left while the new content enters from the right:
```css {7-9,12-14} filename="app/globals.css"
@keyframes slide {
from {
translate: var(--slide-offset);
}
}
::view-transition-old(.nav-forward) {
--slide-offset: -60px;
animation: 200ms ease-in-out both slide reverse;
}
::view-transition-new(.nav-forward) {
--slide-offset: 60px;
animation: 200ms ease-in-out both slide;
}
```
Back navigation mirrors the offsets with the `nav-back` names.
Read our guide to [designing View Transitions](/docs/app/guides/view-transitions) for more patterns, guidance on choosing what should animate, and [isolating persistent elements](/docs/app/guides/view-transitions#anchoring-the-header) like headers and sticky controls, or give your coding agent the [React View Transitions Skill](https://skills.sh/vercel-labs/agent-skills/vercel-react-view-transitions) to add them for you.
## Demo apps
The videos in this post come from open-source apps you can clone and explore, built on Next.js 16.3:
- [\*\*Next Beats\*\*](https://github.com/nextjs/next-beats): A music player with a library, playlists, favorites, and playback that continues across navigation.
- [\*\*Drop\*\*](https://github.com/aurorascharff/next16-social-media): A developer-themed social network with posts, follows, profiles, tag feeds, and cached route data.
- [\*\*Flow\*\*](https://github.com/aurorascharff/next16-calendar): A calendar and booking tool. Events are created, dragged, and deleted in the client, while the calendar weeks are cached and revalidated by tag.
- [\*\*Huddle\*\*](https://github.com/aurorascharff/next16-team-chat): A Slack-like team chat with channels, threads, reactions, unread state, and mention autocomplete. It is available in equivalent TanStack Query and SWR variants.
The apps include Playwright end-to-end tests using the [`instant()`](/docs/app/guides/instant-navigation#prevent-regressions-with-e2e-tests) helper, which scopes assertions to the prefetched UI. An example from Next Beats asserts that the heading is already visible when opening the Library page:
```ts {5-8} filename="tests/navigation.spec.ts"
import { instant } from '@next/playwright';
await page.goto('/');
await instant(page, async () => {
await page.getByRole('link', { name: 'Library' }).click();
await page.waitForURL('/library');
await expect(page.getByRole('heading', { name: 'Library' })).toBeVisible();
});
```
## Feedback and Community
Share your feedback and help shape the future of Next.js:
- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)
