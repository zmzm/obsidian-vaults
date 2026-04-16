---
type: twir-item
issue: 267
item: 8
item_type: item
date: 2026-02-04
source: https://www.developerway.com/posts/debugging-with-ai
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2026-02-04-TWIR-267|Index]]

# Item 8: Can AI actually debug complex React/Next.js issues?

Source: [https://www.developerway.com/posts/debugging-with-ai](https://www.developerway.com/posts/debugging-with-ai)

Summary:
The author tests whether large language models (LLMs) can debug and fix real-world React/Next.js bugs, comparing AI-generated fixes to manual investigation. Using a sample app with intentional issues, the LLM successfully patches a broken user profile page by adding missing fields, but the article emphasizes the importance of understanding root causes and schema validation (with Zod). The piece is both a practical AI evaluation and a React debugging tutorial.

Key takeaways:
- LLMs can identify and fix some React/Next.js bugs, especially those related to missing or mismatched data.
- Schema validation (e.g., Zod) is crucial for catching subtle data issues in React apps.
- Human verification is essential to ensure AI fixes address root causes, not just symptoms.
- The article provides a useful debugging workflow for React developers.

Recommendation:
Summary sufficient

Content:
# Debugging with AI: Can It Replace an Experienced Developer?

How's everyone's experience with AI so far? Love or hate? I've been using it extensively for work in the last few months, so I thought I might start sharing some tips and tricks on how to use it without losing your mind (and skills).

But writing yet another "10 tricks for better prompt engineering" article is mind-numbingly boring. Want to play detective instead and investigate some weird stuff? And in the process, we'll find out how good AI is at debugging and fixing things. And hopefully, learn a thing or two about React and Next.js internals, for the fans of digging very deep.

To do that, I implemented an app with a few problems. In this article, I'm going to throw those problems at LLMs with a "fix-it" prompt and see the result. And then investigate the same bug manually, show you how I'd actually fix it, and validate whether AI fixed the bug and its root cause correctly. And share my debugging process and train of thought, in case you want to follow along and investigate by yourself.

Hope you have your debugging tools ready!

The Study Project is on [GitHub](https://github.com/developerway/debugging-with-ai) if you want to follow along or try your own AI tools. It's a React/Next.js app, with a few pages, a few API endpoints, TanStack for data fetching, and Zod for schema validation. Almost like a real app!

When you open it, you'll see a beautiful dashboard page. Click an Order ID to see more detailed Order information. Click a Product ID to see more info on a Product. Clicking the user's name in the top-right corner opens a dropdown with a few more links. Clicking "User Profile" leads to a page with all the information about the user.

Or, to be precise, it should. But that route is fundamentally broken in several ways. This is what we're going to be fixing today!

![](/assets/debugging-with-ai/user-profile-link.png)

For the investigation part with the LLM, I'll first try to pretend I don't really know anything about the tech stack and try to investigate "blind". And then validate the fix by doing the investigation manually with the knowledge of the tech stack, since I actually have it.

If you've never worked with Next.js, TanStack, and/or Zod, try doing your own prompting and manual investigation first, to get the most fun out of it. And then share the results, I'm really curious how your investigation turns out!

I'm going to use Opus 4.5 that comes with my personal Claude Pro subscription. I feel it's good enough for the test. If you have access to other tools or models and want to compare them, please share the results as well!

And finally, over the course of this investigation, I want to understand the following:

1. Did the LLM fix the problem?
2. Did the LLM identify the root cause of the problem correctly?
3. Did the LLM fix the root cause of the problem correctly?

Let the fun begin!

## Investigation 1: User Page is Broken

Start the project with `npm run dev` and navigate to the User Profile page via the dropdown or directly via the`/users/1` route. You'll see the "Something went wrong" page with handy errors right there:

![](/assets/debugging-with-ai/investigation1-user-page-broken.png)
And in the browser console, you'll see those errors in a more detailed format:

![](/assets/debugging-with-ai/investigation1-user-page-broken-browser-console.png)

Server logs are totally clean, so the error is clearly on the frontend.

### LLM Attempt

Let's feed all this information to the LLM and see what it comes up with.

**LLM prompt**

*When I navigate to the /users/1 route, the page shows a "Something went wrong" error. In the browser console, I see the following errors [copy-paste the entire error stack]. Server logs are clean. Can you fix it?*

The LLM does its thing, reports that it's done, I refresh the page - and woohoo! The page is not broken anymore! I can mark the question "Did the LLM fix the problem?" as a success.

Looks like it's going to be a very short article 😅

Opus's opinion on what's broken is this:

**LLM investigation**

*The issue was that the getUser service was returning a user object missing the phone and
address fields required by UserSchema in src/lib/schemas.ts:238-255. When Zod validated the API response on the client side, it threw an error because these required fields were undefined. I added the missing fields to the user data. The /users/1 page should now load correctly.*

I.e., there are missing fields in the data sent to the client. And the fix it came up with was adding those missing fields in the file with the data:

```
```
export const getUser = async () => {

const user = {

id: 1,

name: 'John Doe',

email: 'john.doe@example.com',

phone: '+1 (555) 123-4567',

address: {

street: '123 Main Street',

city: 'San Francisco',

state: 'CA',

postalCode: '94102',

country: 'United States',

},

...

};

if (!user) {

throw new Error('User not found');

}

return user;

};
```
```

Now let's verify whether the fix is correct or not.

### Human Overview

In order to understand whether the fix is correct or not, I need to actually understand what the problem was. By myself, if I want to be 100% sure.

So let's look at it again. In the browser console I see this:

```
```
Uncaught ZodError: [ { "expected": "number", ...

at fetchUser (useUser.ts:11:21)

at UserPage (webpack-internal:/
```
```

Something-something Zod-related in the `fetchUser` function triggered from the `UserPage` component.

In `UserPage.tsx`, I see this code:

```
```
const { data: user, isLoading, error } = useUser();
```
```

Where `useUser` is a TanStack Query:

```
```
export function useUser() {

return useQuery({

queryKey: ['user'],

queryFn: fetchUser,

});

}
```
```

Where `fetchUser` is a function that fetches the User info:

```
```
async function fetchUser() {

const response = await fetch('/api/user');

const data = await response.json();

return UserSchema.parse(data);

}
```
```

Which indeed uses Zod to parse and validate data coming from the REST endpoint. If you've never worked with [Zod](https://zod.dev/), it's literally its purpose: to parse and validate raw data according to the schema. And to throw an error if the data is incorrect.

Which is exactly what is happening in our case: the `UserSchema` is failing. So something is wrong with the `data` coming from `/api/user`. In the Network panel, I can see the endpoint and its output:

![](/assets/debugging-with-ai/investigation1-endpoint-result.png)

So the endpoint works perfectly fine, which is corroborated by the clean backend log.

The only explanation here is that the returned data, while it looks good, doesn't satisfy our schema. And if I actually just read the error output in the browser console:

![](/assets/debugging-with-ai/investigation1-user-page-broken-browser-console.png)

I'll see exactly which fields violate the schema and how: the phone field is expected to be a `string` but received `undefined`. The `address` field is expected to be an `object` but received `undefined`.

Here's the schema:

```
```
export const UserSchema = z.object({

...

phone: z.string(),

address: z.object({

street: z.string(),

city: z.string(),

state: z.string(),

postalCode: z.string(),

country: z.string(),

}),

...

});
```
```

Indeed, phone and address are expected to be present, otherwise they'd be `.optional()`.

Which is exactly what LLM told me! What a clever robot 🤖. I'll mark the "did it identify the root cause" part as a success as well:

Now to the fix.

There are two ways to fix it. We either need to make sure that the data is always present, which is exactly what LLM did by adding `phone` and `address` data to the mock.

Or we can make the schema for those fields optional like this:

```
```
export const UserSchema = z.object({

...

phone: z.string().optional(),

address: z.object({

...

}).optional(),

...

});
```
```

Which fix is correct?

Well, it depends on the context, actually. If it were a mock for a unit test, then LLM might've been correct in fixing the mock. Relaxing the schema to make a unit test pass is the opposite of how tests are supposed to work. Although even that depends on the test.

In our case, our mocks clearly serve as a substitute for the real data coming from the backend, which is probably going to be implemented as the next step. And in a real app like this, it's highly, highly unlikely that `phone` and `address` fields will be mandatory as part of a general User profile.

So the "correct" fix here would be to relax the schema: either make those fields optional or nullable (depending on the backend and data conventions in the repo).

Funnily enough, in a "real" app with an actual backend, the LLM would relax the schema right away: it tends to play loose with the rules and introduce optionals and `any` as a default solution to everything. The fact that I'm using mocks here confused it.

When I revert the LLM fix, make the fields in the schema optional, and refresh the page, the experience is back to being broken.

![](/assets/debugging-with-ai/investigation1-user-page-broken2%202.png)

The console shows the same thing:

```
```
installHook.js:1 TypeError: Cannot read properties of undefined (reading 'street')

at UserPage (UserPage.tsx:177:58)

...
```
```

Considering that we just relaxed the schema, it should be pretty obvious what happens here: we're trying to access the `street` property of the `address` value that is now optional. All we need to do is render those fields conditionally:

```
```
user.address && <div ... >// bunch of stuff that render address
```
```

LLM is actually able to fix this one with almost zero prompting, nice and clean.

But considering it didn't fix the original root cause, I'll give it half a point instead of a full one.

## Investigation 2: Double Loaders Problem

We fixed the most obvious bug, but we still have more to investigate on this page.

Load the root page `/`, refresh it to get rid of all the cache, throttle your Internet to at least "Fast 4G", and navigate to the Profile page via the dropdown in the top right corner. The slower the internet, the more noticeable the problem will be: there are two different loading "skeletons" that show up while the page is loading.

![](/assets/debugging-with-ai/investigation2-weird-skeletons.png)

But if you just refresh the User page, only the second skeleton shows up, regardless of the internet settings.

That's just weird. And nothing in the logs 🤔 Let's see whether LLM can solve this one.

### LLM Attempt

Let's feed the LLM exactly what is happening in the description of the problem.

**LLM prompt**
When I'm on the root page and navigate to the User page, I see two different loading skeletons appear. However, when I just refresh the User page, I see only one. Why is that and how to fix it?

This is where things are getting interesting. In the previous investigation, Claude pretty consistently was just adding data to the mock.

In this case, every time I tried this exact prompt, it came up with a different root cause and different fixes.

Sometimes, it thinks that the root cause is that Next.js first shows the root-level `loading.tsx` from the `app` folder, then the route-level `loading.tsx` file from `app/users/[id]` folder.

Sometimes, it thinks that Next.js first shows the route-level `loading.tsx` file from `app/users/[id]` folder, and then `<UserPageSkeleton />` component inside `UserPage.tsx`.

For solutions, it sometimes suggests removing the `loading.tsx` inside `app/users/[id]` folder. Sometimes, it moves the root `loading.tsx` along with `page.tsx` from the app folder to the `app/(dashboard)` folder.

Those don't work, by the way.

When prompted about that, it sometimes says that the solution is to fetch data on the server, and refactors the app to use `useSuspenseQuery` instead of `useQuery`.

This actually works.

Sometimes it arrives at the `useSuspenseQuery` solution right away, in different variations of explanations.

Most of the time, it will say that the double loading doesn't happen on refresh because the User page is server-rendered, so the `loading.tsx` there is not triggered.

So I'll give it a ✅ for fixing the problem, even if not on the first try. And ❌ for finding the actual root cause, since it clearly didn't: too many contradictory root causes here.

And let's investigate manually which of the above is actually the correct root cause and whether `useSuspenseQuery` is the correct fix.

By the way, if you're trying your own prompting, save somewhere LLM's detailed explanations about what's happening. So that you can compare those with the manual investigation and the actual root cause.

### Human Overview

So, **first of all,** let's figure out which of the loading states are actually showing during that navigation. As correctly identified by the LLM, we have at least three:

1. "Root" `loading.tsx` inside the `app` folder.
2. "Route" `loading.tsx` inside the `app/users/[id]` folder.
3. "Client" skeleton in the form of a `<UserPageSkeleton />` that is rendered conditionally when `isLoading` is true inside the `UserPage.tsx` file.

All of them look similar, but are implemented differently, so it's a bit hard to actually identify which is which from their visuals. What I usually do in situations like this is the good old "red border" method 😅 Anyone who's debugged CSS issues before Tailwind took over knows it. Basically, if I add **red** border to the "root" skeleton, **green** to the "route", and **black** to the "client", I'll immediately see which follows which.

In this case, it's green followed by black. We see a flash of "route" level `loading.tsx` skeleton, followed by the client-side `<UserPageSkeleton />`. The "root" level skeleton is not in the picture, Claude was wrong about that part.

**Second question** - why only the "client" skeleton shows up when I refresh the page?

Claude thought it's because this page is server-rendered, so `loading.tsx` is not triggered.

This one is not true as well 😉 In reality, this pattern [creates a Suspense boundary](https://nextjs.org/docs/app/api-reference/file-conventions/loading) around a page-level Server Component in the `page.tsx` file. It has nothing to do with server *rendering* - everything in Next.js is server rendered regardless of whether you use Server Components or not.

When this Suspense boundary is created, Next.js renders the content of the `loading.tsx` until the promise that is an async `page.tsx` is resolved, after which it swaps it with its content. The only reason we don't see the "green" loading is because we don't do anything asynchronous in the `page.tsx`. So there is nothing to wait for, and the promise is resolved almost immediately.

Try adding a delay like this, and the "green" loading will show up as expected:

```
```
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export default async function Page({ params }) {

const { id } = await params;

await delay(10000);

return <UserPage userId={id} />;

}
```
```

If the difference between Server Components and Server Rendering made your brain explode right now, don't worry, it happens all the time. Those topics are very complicated and very confusing. I have a few very detailed articles that might help here, if you're up for even more detail-filled reading: [SSR Deep Dive for React Developers](https://www.developerway.com/posts/ssr-deep-dive-for-react-developers) and [React Server Components: Do They Really Improve Performance?](https://www.developerway.com/posts/react-server-components-performance)

In the meantime, here's a **third question**: if the promise resolves so fast that we don't see the "green" loading during refresh, why do we see it when we're navigating from the dashboard? 🤔

The easiest way to figure it out is to record the performance profile of the navigation. First, build the project with `npm run build` and start it with `npm run start`. Always record performance on the production build, unless it's necessary to see the dev for some reason.

Then, in Chrome DevTools, open the Performance tab, click the top left "Record" button, and navigate to the User page by clicking the link in the Profile dropdown. The recording should be something like this:

![](/assets/debugging-with-ai/investigation2-performance-navigation.png)

If you hover over the screenshots area, you'll see that before the blue `1 (localhost)` bar, the page shown was Dashboard. While the blue bar is present, we see the "green" route loading. After it ends, and the gray `user (localhost)` bar starts, the "black" client skeleton is visible.

Hovering over those bars will give you the information on what's what. The blue bar shows the browser downloading the RSC payload for the User page, and the gray bar shows the request to the `/api/user` API endpoint. The one that returns the user data.

This RSC payload is the layout generated by the Page server component that React needs to construct the page's actual HTML. When we access that page directly (via refresh), that layout is returned with the first HTML response. When we access the page via an SPA transition (via Link navigation), that layout is downloaded as its own file over the Network. As a result, with a throttled internet, it takes a bit of time, the Suspense boundary kicks in, and we always see the "green" loading skeleton.

Which actually raises **another question**: why no prefetching here? I thought Next.js is famous for aggressively caching and [pre-fetching everything by default](https://nextjs.org/docs/app/guides/prefetching). What makes this use case different? 🤔

Searching through the docs gives [*some* answer](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching): pre-fetching only works partially on dynamic routes. A [dynamic route](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) is the one that is generated on-the-fly, the `[id]` part of our path. Not really clear what "partial" means in this case, but my guess is it doesn't include page's RSC. Otherwise, it would've been prefetched, and we wouldn't have seen the "green" loading skeleton.

To test that theory, I need to [force prefetching](https://nextjs.org/docs/app/api-reference/components/link#prefetch) on the `Link` component that navigates to the Page:

```
```
<Link href={`/users/${user.id}`} prefetch={true}>

<User />

Profile

</Link>
```
```

If I build `npm run build`, start the project again `npm run start`, and navigate from the dashboard to the User page, the "green" loading state will be gone. Only the "black" client loading is there. Prefetching worked!

This is not a proper fix, however. You wouldn't want to manually add prefetching to every Link component you have. It's just a way to test and verify our mental model of how data fetching and prefetching work in the app.

And the most important part of that mental model is that the "green" route-level loading, the one implemented via `loading.tsx`, stays visible until the Page component on that route remains suspended.

Using `useSuspenseQuery` instead of `useQuery` seems to be [doing exactly that](https://tanstack.com/query/latest/docs/framework/react/guides/suspense) - keeping the component "suspended" until the query is resolved. Which is why the fix proposed by Claude works.

Is this the correct fix, however?

"While we don't necessarily recommend it, it is possible to replace this [useQuery] with `useSuspenseQuery` instead **as long as you always prefetch all your queries**." And then this: "If you do forget to prefetch a query when you are using useSuspenseQuery, the consequences will depend on the framework you are using. In some cases [...] you will get a markup hydration mismatch, because the server and the client tried to render different things."

Basically, it could be bad, depending on the framework. And indeed, if you apply the `useSuspenseQuery` fix suggested by Claude, you'll see errors in the Chrome console when you refresh the User page.

![](/assets/debugging-with-ai/Investigation2-wrong-fix.png)

So I'll give Claude the final ❌ on this problem: its fix introduces another problem down the line.

So, what is the actual fix then?

Three things we could do here, depending on the time we're willing to invest in refactoring.

The easiest, simplest, and most "hacky" fix would be to reuse the "black" skeleton instead of "green" (or vice versa). In this case, we'd still have two skeletons showing up in sequence, but since they will look identical, the user won't notice.

We could also refactor the User page to only hide the dynamic data under the skeletons. So instead of loading skeletons that cover the entire page, we'll show *some* text almost immediately, after the "green" skeleton, giving the user the impression that the page is progressively loading.

Or, the most advanced and probably the most "correct" solution, given we already use Next.js, is to fetch the user data in a Server Component. Thus eliminating the need for the "black" client loader altogether.

If you want to practice more AI skills, try to achieve that with prompting first, before looking into the solution below.

The solution with **Server Components data fetching** is this.

We already use TanStack to fetch data, and refactoring the entire repo away from it will be unwise. However, TanStack is an advanced library that [can be hydrated](https://tanstack.com/query/latest/docs/framework/react/guides/ssr) on the server. Including from [Next.js App router](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr#server-components--nextjs-app-router).

The repo is already set up correctly for it to work; we just need to use it.

```
```
export default async function Page({ params }) {

const { id } = await params;

const queryClient = new QueryClient();

await queryClient.prefetchQuery({

queryKey: ['user'],

queryFn: async () => {

await new Promise((resolve) => setTimeout(resolve, DELAYS.USER));

const user = await getUser();

return user;

},

});

return (

<!-- Pass the dehydrated state to HydrationBoundary component -->

<HydrationBoundary state={dehydrate(queryClient)}>

<UserPage userId={id} />

</HydrationBoundary>

);

}
```
```

Only three steps: initialize the `queryClient`, trigger and await prefetch (to receive the data right away), and pass that client to the `<HydrationBoundary />` component.

As a result, you should see only the "green" loading state both when navigating from the dashboard and when refreshing the page. And if you open the Network panel in Chrome, you'll see that the client request for the User information is no more.

## Investigation 3: Weird Redirect Error

Final investigation.

Navigate to the `/users` URL: you'll see a very quick flash of the error page, and then it will redirect to the `/users/1`. The redirect is expected. The intention here is to redirect non-admins: they should be able to see the info about themselves, but shouldn't have access to managing users.

The error, however, is not expected and needs to go away. In the browser's console, I see the same error: `Rendered more hooks than during the previous render.`

![](/assets/debugging-with-ai/investigation3-error.png)

Let's try LLM again!

### LLM Attempt

Same prompt again: explain what happens and what I see in the console.

**LLM prompt**

*When I navigate to the `/users` page, I see a "Something went wrong" page, and in the console I see the following error: [error code]. Investigate why the error happens and how to fix it.*

This one failed miserably.

The LLM just kept going in circles. Over the course of this investigation it tried, very confidently, to fix the issue with:

- Moving redirect to `useEffect` (no, thank you, do you know what this will do to performance?).
- Moving redirect to `next.config.ts` file (not going to work, I'll need access to database there soon).
- Moving redirect to `proxy.ts/middleware.ts` (not maintainable, I'll need a bunch of those redirects with a bunch of logic there soon, plus I don't want to reimplement routing there).
- Messing with the `QueryProvider` and moving it to the state (didn't fix it).
- Saying that the redirect should be returned (nope).
- Saying that Next.js version is obsolete (didn't fix it).
- Adding `loading.tsx` next to the `page.tsx` with redirect (nope, didn't fix).

For every one of them, it had a very believable and very detailed explanation of why that solution should fix the problem.

So this one was a real head scratcher to investigate properly.

### Human Overview

In most of its attempts to fix it, LLM would mention that throwing an error is how `redirect` is supposed to behave. Which is interesting and worth a bit of old-fashioned googling and documentation reading.

And indeed, in Next.js docs it's [mentioned](https://nextjs.org/docs/app/guides/redirecting#redirect-function) that *`redirect` throws an error so it should be called **outside** the `try` block when using `try/catch` statements.* So I imagine somewhere at the root, Next.js catches that error, separates it from "regular" errors, and then performs the actual redirect.

Although this is a bit misleading for this problem: the error I see in the UI and console is about hooks, not redirects.

Even more googling reveals this GitHub issue in the Next.js repo: [Rendered more hooks than during previous render" when using App Router](https://github.com/vercel/next.js/issues/63121). Exactly our use case.

After reading through comments, one of them mentioned that [they had the same issue](https://github.com/vercel/next.js/issues/63121#issuecomment-2795371192), and it was fixed by adding `loading.tsx`. This is probably why half the time LLM tries to add the loading state next to the page in an attempt to fix it. Unfortunately, in our case, it doesn't fix it.

Then, slightly below, there is another comment, explaining that ~~we all are morons~~ [we just need to use redirect correctly](https://github.com/vercel/next.js/issues/63121#issuecomment-3140443106). Double-checking the code reveals that everything is fine on our end.

Another comment mentioned that nothing worked for them other than removing `loading.tsx` completely. I wonder what will happen if I do this?

And it actually fixes the error! 🤯 Although removing all `loading.tsx` is unlikely to be a good solution, users won't be able to navigate quickly between pages without it.

Continue reading that GitHub thread, but that's it. There are no more suggestions, another dead end. 😭

Okay, let's approach it from another end. If seeing the error were normal behavior, the internet would've been full of complaints, and the issue would've been fixed long ago. Same if the error were very common and obvious. LLM would've fixed it by now.

So, there's something wrong in our app's code, and it's pretty unique.

This is the time again to do the old-fashioned boring debugging known as "kill things one by one until the error goes away". Basically, I need to start ripping out all components and everything from the `layout/page/loading` structure, leaving only bare-bones Next.js.

Removing everything from the User page does nothing. The error is still there. Same as removing everything except `children` from `app/users/layout.tsx`. But removing `<SendAnalyticsData />` component from the root layout finally moves the needle! 🎉 The error disappears!

Restoring everything other than `<SendAnalyticsData />` in the root, just to make sure we've isolated the root cause, and... the error is back again 🤦🏼‍♀️ Luckily, we're professional debuggers by now, so It should be relatively easy to find out in this repo why: the `UserLayout` component inside the second `layout.tsx` file also has a `<SendAnalyticsData />` component.

In real life, it took me days to debug that thing, it actually was a very complicated combination of different components and function calls 😅

Okay, so something is wrong inside the `<SendAnalyticsData />` component. The component itself is rather primitive:

```
```
export function SendAnalyticsData({ value }: { value: string }) {

useEffect(() => {

sendAnalyticsData(value);

}, [value]);

return <></>;

}
```
```

Literally just one tiny `useEffect` that calls a function. But that function is... a Server Action:

```
```
'use server';

export async function sendAnalyticsData(name: string) {

console.log('analytics data sent', name);

}
```
```

That can't possibly be true? Completely legitimate way to call an Action caused so much trouble? 🤔

Easy to verify. I just need to restore everything to the original form and comment out that Action.

And the error goes away! 🤯 Now that I know what to google (i.e., a combination of "Suspense, Next.js, Actions, Redirect, Error"), I can find a few mentions of [exactly this problem](%5Bhttps://github.com/vercel/next.js/issues/78396%5D(https://github.com/vercel/next.js/issues/78396#issuecomment-2841028402)) here and there. Finally, the actual root cause! Looks like a combination of a server-side redirect and an action-in-progress wrapped in Suspense confuses Next.js.

How exactly and what is confused doesn't really matter at this point. Although if you google enough, you'll be able to find clues. But I'll leave it for you as homework.

Because the solution here is clear: I just need to either remove this Action or refactor it into a simple REST endpoint, and the error is fixed. Yet another reason not to use Actions, in my opinion. If you missed the previous reasons, here's another deep dive: [Can You Fetch Data with React Server Actions?](https://www.developerway.com/posts/server-actions-for-data-fetching)

But for this investigation, it's time to wrap it up.

## TL;DR

So, what's the verdict? Can AI replace an experienced developer for debugging?

No, of course not. AI is very good at pattern recognition, and it can be very, very useful. It will do exceptionally we

... (content truncated)
