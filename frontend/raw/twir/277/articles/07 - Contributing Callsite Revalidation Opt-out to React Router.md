---
type: twir-item
issue: 277
item: 7
item_type: item
date: 2026-04-15
source: https://programmingarehard.com/2026/04/11/contributing-to-react-router.html/
tags:
  - "Ease"
status: auto
quality: keep
---

[[2026-04-15-TWIR-277|Index]]

# Item 7: Contributing Callsite Revalidation Opt-out to React Router

Source: [https://programmingarehard.com/2026/04/11/contributing-to-react-router.html/](https://programmingarehard.com/2026/04/11/contributing-to-react-router.html/)

Summary:
The author describes their contribution to React Router: enabling callsite-level opt-out for loader revalidation, allowing developers to control revalidation behavior directly where navigation or mutations are triggered. Previously, revalidation had to be managed via exported functions in each route, which was error-prone and hard to maintain. The new feature, released as "unstable_defaultShouldRevalidate," lets developers pass a flag to navigation methods, forms, and links, streamlining control and reducing boilerplate. The post also highlights the collaborative open-source process behind the feature.

Key takeaways:
- React Router now supports callsite-level opt-out of loader revalidation, reducing the need for repetitive shouldRevalidate functions.
- The feature is currently marked "unstable" for feedback before stabilization.
- Developers can control revalidation via navigation, fetcher, form, and link props.
- This change improves flexibility and maintainability in complex routing scenarios.

Recommendation:
Read fully (read fully if you use React Router and need granular revalidation control)

Why it matters:
read fully if you use React Router and need granular revalidation control

Content:
# Contributing Callsite Revalidation Opt-out to React Router

This post is long overdue since it happened back in November but alas here we are...

I contributed [callsite revalidation opt-out](https://github.com/remix-run/react-router/pull/14542) to React Router(with a lot of help from [Matt Brophy](https://x.com/brophdawg11)) and am pretty proud of that. React Router is very well established, and new features don't get incorporated without tons of thought and consideration from the steering committee. Pretty pumped I got to implement [a feature Ryan Florence pitched](https://github.com/remix-run/react-router/discussions/10006) way back in early 2023. Feels good to finally contribute *code*, not just feedback, after years of using the software.

## Revalidation

If you've worked with React Router for any length of time you'll immediately notice the nuclear approach to revalidations. What's a "revalidation" you ask?

Imagine you have three nested routes that each exports a `loader` to supply data.

```
app/routes/root.tsx                 -> supplies account data
app/routes/projects.tsx             -> supplies list of projects
app/routes/projects.$projectId.tsx  -> supplies project details
```

If you make a successful POST request to mutate some data in the `projects.$projectId.tsx`, then all three loaders will "revalidate": run again to fetch fresh data.

### History lesson

This behavior harkens back to the days where you just relied on `<form method="post" action="action.php">` and the browser would refresh the whole page. Your backend would *have* to refetch all the data that the page needs.

We've come along way since then though. The pendulum swung to SPA's where most people used [react-query](https://tanstack.com/query/latest) to make all their api calls and it was up to you to *explicitly* revalidate data. React Router's default behavior swings that pendulum all the way back and revalidates everything for you.

## Today

React Router does give you means to control revalidations in the form of exporting a [shouldRevalidate](https://reactrouter.com/start/data/route-object#shouldrevalidate) function from your route. This is your means of opting loaders out of rerunning based on certain app specific conditions. This is great but a bit unwieldy at times.

Imagine the `projects.$projectId.tsx` route allows you to "tag" the project. Think GitHub labels. You could tag the project "High Priority", "Feature", "Frontend", etc. In GitHub you can create new labels on the fly.

![](https://cdn.programmingarehard.com/cdn-cgi/image/fit=scale-down,width=1200/callsite-revalidation-optout/github-label.png)

You would most likely use a `fetcher.submit()` call for this request and since that's a mutation it will automatically revalidate all three loaders in our hypothetical app. This can lead to some wonky behavior and we know that for our use-case these automatic revalidations are completely unnecessary.

## Old solution

The old way was to export a `shouldRevalidate` function in *every* active route.

```
// app/routes/root.tsx
// app/routes/projects.tsx
// app/routes/projects.$projectId.tsx

import type { ShouldRevalidateFunctionArgs } from "react-router";

export function shouldRevalidate({
  defaultShouldRevalidate,
  formMethod,
  formAction,
}: ShouldRevalidateFunctionArgs) {

  const isTagCreate =
    formMethod === "post" &&
    formAction?.endsWith("/tags");

  if (isTagCreate) return false;

  return defaultShouldRevalidate;
};
```

Now, imagine your coworker needs to use your fancy new creatable tag combobox component. They better remember to do the same `shouldRevalidate` shenanigans in the active routes they're working in.

This gets messy and is prone to being missed.

After some research, I came across [Ryan's old proposal](https://github.com/remix-run/react-router/discussions/10006) for Callsite Revalidation Opt-out which is exactly what I wanted. I wanted to be able to control this revalidation at the *callsite*.

```
fetcher.submit(target, {
  method: 'post',
  shouldRevalidate: () => false
}
```

It was validating to see others experiencing this same pain point. It was at this point that I thought "Hey, maybe I can I figure this out and make it a reality".

## Rolling up my sleeves

I forked the repo and was able to figure out how to get the examples to run but I was struggling to figure out a workflow to modify the core code and test that out. I added some `console.log` and `debugger` statements but they were never being triggered when they absolutely should have been. I have been fairly active in the React Router discord so I headed to the `#contributing` channel.

![](https://cdn.programmingarehard.com/cdn-cgi/image/fit=scale-down,width=1200/callsite-revalidation-optout/discord-start.png)

I was able to get the `console.log`s to show up but couldn't get it to break with my `debugger` statements. After some head scratching, I figured out that my console had a rule to ignore files in `node_modules`. I needed to uncheck the checkbox in the **Custom exclusion rules** here.

![](https://cdn.programmingarehard.com/cdn-cgi/image/fit=scale-down,width=1200/callsite-revalidation-optout/node_modules-ignore.png)

I was in business after that! I could step through the code to see how React Router worked and flowed under the hood.

After a couple hours of investigation and trying things I was able to put a PR together.

![](https://cdn.programmingarehard.com/cdn-cgi/image/fit=scale-down,width=1200/callsite-revalidation-optout/discord-pr.png)

The steering committee met and made some design choices that made a lot of sense. Matt asked if i'd like to make the changes or hand it off.

![](https://cdn.programmingarehard.com/cdn-cgi/image/fit=scale-down,width=1200/callsite-revalidation-optout/issue-talk.png)

I wasn't going to come this far and *not* try to see it through myself.

I was able to make the requested changes and then Matt wrote a tests covering it. [Brooks Lybrand](https://x.com/BrooksLybrand) was checking out the PR and [discovered a bug](https://github.com/remix-run/react-router/pull/14542#issuecomment-3566813863) which I was quickly able to determine the cause but wasn't sure the best way to go about fixing. Matt figured out that another PR would solve the problem here so he merged that in and it was good to go. ð

The feature was included in the v7.11.0 version as "unstable" to give people a chance to try it out and let it soak before they're marked as stable. Here's what it looks like to use currently. Eventually the `unstable_` bit will drop off.

```
fetcher.submit(target, {
  method: 'post',
  unstable_defaultShouldRevalidate: false
}

<Form method="post" unstable_defaultShouldRevalidate={false}>
...
</Form>

<Link to={href('/some/where')} unstable_defaultShouldRevalidate={false}>
...
</Link>

const navigate = useNavigate()

navigate(href('/some/where'), {
  unstable_defaultShouldRevalidate: false
})
```

It's been added to all navigations which should cover any use-case you might have.

This gives you a lot of flexibility: the value you set becomes the `defaultShouldRevalidate` argument in the route's `shouldRevalidate` function, so you can control revalidation at both the callsite and the route level.

## Try it out

If you've been wrestling with React Router's aggressive revalidation behavior, this feature should make your life easier.

Big thanks to Matt Brophy and the React Router steering committee for guiding this through. Open source collaboration at its best.

Give it a go and [let me know](mailto:david@programmingarehard.com?subject=Callsite-Revalidation-Opt-out) how it works out for ya.

Enjoy this? Sign up for my newsletter below to get notified when I publish new posts. âï¸
