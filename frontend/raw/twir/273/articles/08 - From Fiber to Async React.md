---
type: twir-item
issue: 273
item: 8
item_type: item
date: 2026-03-18
source: https://www.nonsoo.com/posts/async-react
tags:
  - "AsyncReact"
status: auto
quality: keep
---

[[2026-03-18-TWIR-273|Index]]

# Item 8: From Fiber to Async React

Source: [https://www.nonsoo.com/posts/async-react](https://www.nonsoo.com/posts/async-react)

Summary:
This article provides a deep dive into the evolution from React's stack reconciler to Fiber and the advent of "Async React" in React 19. It explains how Fiber enables interruptible, prioritized rendering and sets the stage for modern async features, including data fetching and concurrent UI updates. The piece encourages developers to rethink how async work is handled within the React rendering model.

Key takeaways:
- React Fiber introduced incremental, interruptible rendering, enabling better responsiveness.
- Async React (React 19) integrates asynchronous work directly into the rendering system.
- Developers should adapt their mental models and component patterns to leverage new async capabilities.
- The shift impacts library authors and application structure, expanding possible UI experiences.

Recommendation:
Read fully (for those interested in React internals or adopting React 19+ features)

Why it matters:
for those interested in React internals or adopting React 19+ features

Content:
# From Fiber to Async React

It been some time since React 19 was released and since then we've seen new api's, hooks, and components that we can add to our apps. Some may argue that these are welcome changes while others may argue that these additions are cool but what's the point?

Let's pose the following question to begin! How would we go about doing data fetching or any async operation within React? Yes, of course we can reach for data-fetching/async libraries such as TanStack Query, swr, etc but let's pretend that we didn't have access to these libraries. How would we go about doing this?

The following code snippet may look familiar!

```
const UsersList = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch("/api/users");

        if (!response.ok) {
          throw new Error("Failed to fetch users");
        }

        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);
};
```

Traditionally, we would often reach for a `useEffect` to handle any asynchronous work (data fetching included) within our React applications. Here we've setup a component that calls the `fetchUsers` function when the component gets mounted to the DOM. We are then setting the data, loading, and error states appropriately such that we can display the correct UI to the user.

This approach works, but as many within the React community and the core React team have noted, this approach has many shortcomings and is not the advised method of handling asynchronous work with React.

Truthfully, React has always dealt with asynchronous work, even if it didn’t explicitly model it. Data fetching, code splitting, user input, animations, and navigation all happen asynchronously, yet for much of React’s history these concerns lived **around** the rendering system rather than **within** it.

As we've seen this meant that we were responsible for stitching together loading states, effects, and imperative updates so that we could keep the UI coherent while asynchronous work was completed. But should that be the responsibility of the application developer or should that responsibility be put elsewhere?

Let's consider the following; What would a React codebase look like if asynchronous work lived **within** the rendering system rather than **around** it? How would it change the way we approach building components, component systems and eventual whole applications?

The release of React 19 brought about the completion story of **"Async React"**, a term we'll unwrap throughout this article. We'll look at how "Async React" solves the coordination problem between UI and async work and we will attempt to answer the questions we posed above. We'll also look at new questions; Knowing that Async React is here, how do we expect React Library authors to build and compose the tools they expose to application developers?

It's a whole new world for developers in terms of how we structure our React applications and these changes can expand the types of experiences we can create. Throughout the article, we'll do a lot of deep dives, so these are just a few things to keep in mind while we explore the modern way of building React applications.

You'll often notice that two important packages are installed when you create a React web app; **React** and **React-dom**. The React package is the library that allows us to describe UI as a function of some state. We often see this represented as the following equation **UI = f(state)** and we use JSX as the method to represent it.

Great! So where does `react-dom` come into play?

React-dom is the package that contains the **React reconciler** and **renderer for the web**. The reconciler is the engine responsible for comparing render outputs over time, scheduling work, and determining the minimal set of updates needed to be applied to the host platform\*. The renderer then takes the output from the reconciler and applies it to the host platform; in this case the DOM.

The reconciler becomes important when speaking about Async React and how the new APIs were made possible. During [React conf 2017](https://www.youtube.com/watch?v=ZCuYPiUIONs) it was revealed that the React reconciler was rebuilt from the ground up as we went from what was known as the **stack reconciler** to **React Fiber**.

The stack reconciler was reconciliation engine that was used in the earlier versions of React up until React 16. It was designed to closely mirror how JavaScript executes function calls; therefore it relied directly on the call stack to traverse and render the component tree.

When a render was triggered—typically by a change in state—React would start at the root and recursively walk the component tree from top to bottom calling each components render function, reconciling the diff and then committing the result. This meant that once reconciliation/render began, React was required to complete the entire process before yielding control back to the browser.

We can see this in the following render example below. Press the **"start render"** button and see how rendering is taking place to update the count value within the dashboard component.

AppLayoutDashboardcount: 0SidebarSidebarItemSidebarItemFooter

idle

render

commit

Browser Main Thread

Ready

Responsive to user input

Start renderReset Component Tree

This approach was entirely synchronous and non-interruptible. All rendering work happened in a single pass, and all updates were treated with the same priority. While this made the system straightforward and predictable, it also meant that long renders could block the main thread, delaying user input and causing visible stutters in complex applications.

Considering the limitations of the stack reconciler, could we imagine a world where improvements could be made?

**POP Quiz!**

With the stack reconciler, React had no way to pause work, reprioritize updates, or abandon rendering that was no longer relevant

TrueFalse

Submit

Enter **React Fiber**; a complete rewrite of React’s reconciler which was introduced in React 16 to address the limitations of the stack-based approach. Instead of implementing rendering in one single uninterrupted pass, Fiber would implement its own internal representation of the component tree--a Fiber Tree--and its own scheduling model.

In Fiber, each component is represented as a unit of work (a fiber) which can be processed independently. Rendering is broken into small, incremental steps, allowing React to pause work, yield to the browser \*, and resume later. This means that Fiber splits the **reconciliation/rendering phase** and **commit phase** into two independent processes.

A Fiber node is a lightweight object that describes the metadata associated with a component. Importantly, each Fiber contains pointers that link it to its parent, child, and sibling components. A very contrived fiber node can be seen below however the full implementation can be viewed within the react codebase.

```
const fiberNode = {
  tag: "",
  key: "key",
  type: null,

  return: null,
  child: null,
  sibling: null,
  ref: null,

  pendingProps: null,
  memoizedProps: null,
  updateQueue: null,
  memoisedState: null,
};
```

Since each Fiber represents a discrete unit of work, React can process the tree one unit at a time, rather than relying on a recursive function call that must run to completion. Between units, React can check whether it should continue rendering or yield control back to the browser. If rendering needs to pause, React simply stops traversal, retains its place in the Fiber tree, and yields. When work resumes, React continues from the next Fiber as if nothing happened.

This process is known as time slicing, and it is a direct consequence of modeling rendering work as a JavaScript object.

During the reconciliation/rendering (now referred to as the reconciliation phase), a list of all changes to be rendered in the UI is generated but does not get committed to the DOM. Rather, the changes are scheduled to be committed in the next phase. The **commit phase**, is when these changes are committed to the DOM.

The important thing to note here is that the **reconciliation phase** can be interrupted, paused/resumed, and discarded completely. The **commit phase** **cannot** be interrupted; therefore once the commit phase starts, it must finish before any other work can be done.

**POP Quiz!**

Fibre can prepare multiple versions of a UI over time, but only commit the final change to the DOM thereby avoiding unnecessary DOM updates

TrueFalse

Submit

Since the **reconciliation phase** can be interrupted, it suggests that the two independent pieces of work can be within the **reconciliation phase** and then progress into the **commit phase** out of order. This allows Fiber to introduce the concept of prioritization when speaking about showing render updates within the DOM.

Fiber allows React to schedule high-priority updates first while deferring lower-priority updates, thereby improving both perceived performance and user experience. We can imagine that typing into an input is more urgent than rendering data that just finished loading in the background. So why not defer rendering of the data so that we can show the state of the input field immediately. The rendering of the data will just happen after the user is done typing. This is what we mean by improved perceived performance.

So what are the priorities for Fiber? They are as follows:

- Synchronous Work (involves clicking/typing -- works like the stack reconciler)
- Task Work
- Animation (started by **`requestAnimationFrame()`** )
- high priority
- low priority
- off-screen (anything not currently in view but would be nice to have rendered in case it gets shown)

Understanding these priority groups will be important later on when we speak of the APIs, hooks, and components that were introduced in React 18 and 19. But the core thing here is that without the move to Fiber the concept of **Async React** would not be possible.

React Fiber was such a monumental feat of engineering as it introduced the ability to have interruptible renders, cooperative scheduling, prioritization, and so much more. With these concepts introduced, we could begin to imagine a new world of building React applications. However, the core entities that were missing from the Fiber release were the APIs that would allow developers to hook into this new way of building.

To note, I use the term APIs loosely here to refer to hooks, functions, and components that are available by React. However, React has a formal definition of **API** which refers to the functions made available by the React package.

Throughout the article I will make the distinction between the loose term APIs and specific React APIs.

When React 18 was released, it brought about APIs that allowed developers to finally use **some** of the concepts that were introduced with Fiber. You'll notice that I used the keyword **some** as it wouldn't be until React 19, specifically React 19.2 that developers would gain the remaining APIs that unlocked access to the full capability of Fiber.

APIs such as the following:

- Suspense
- startTransition (api) & useTransition
- useDeferredValue
- useOptimistic
- useFormStatus
- useActionState
- use (api)
- Activity
- View transitions (experimental)

These APIs are extensively documented within the React docs and there are also a number of tutorials that go over how each of them work. But let's speak on a few of these APIs and how they relate to React Fiber.

Earlier we stated that the move to Fiber was integral to the existence of transitions. To visualize this let's look at the following example using the stack reconciler.

Add some high priority work followed by some low priority work and see when tasks are get completed/rendered to the screen.

#### Pending

#### Processing

#### Completed

Here we see that regardless of priority there is no difference in when items are rendered to the screen. In the event that we have a mix of components that are supposed to be high and low priority updates, we can see that rendering occurs in a certain order that follows a **last-in first-out principle**.

This brings about a challenge because we have a scenario in which we have a number of lower priority updates that are scheduled after the high priority updates. In the **stack reconciler world**, the higher priority updates will not be rendered until the lower priority updates are finished rendering. In essence we're unable to schedule the priority of rendering work.

Fiber fixed this problem as it introduced the concept of prioritization; it would schedule higher priority updates first then work on lower priority updates later. Let's take a look at the same example but with fiber enabled.

Again, add some high priority work followed by some low priority work and see when tasks are get completed/rendered to the screen.

#### Pending

#### Processing

#### Completed

It's different right!! Here we can see that all the high priority updates are rendered before the low priority updates. Moreover, if we're in the middle of rendering low priority updates and a high priority update comes in, the low priority work is paused, the high priority work is rendered, and then the low priority work resumes.

The APIs that enables this prioritization of state updates is **transitions**; specifically the startTransition API and the useTransition hook. These APIs allow us to mark a set of lower priority updates and let React know that the update within this function can be deferred until all the high priority work is complete.

We've seen that Fiber introduced the concept interruptible renders; thereby allowing React to pause/resume renders, and completely throw away work that was yet to be committed to the DOM.

The switch to Fiber also has implications when we think about the Suspense component which allows developers to display fallback UI until it's children have finished loading. A component is said to be **suspended** when it throws a promise during the reconciliation phase. Rather than treating this as an error, React interprets the thrown promise as a signal that the component cannot finish rendering yet. The promise is caught by the nearest Suspense boundary, rendering of that subtree (ie the suspended component) is paused, and the fallback UI is rendered instead. Rendering of the sub-tree will only resume once the promise is resolved.

This can happen because fiber allows React to interrupt renders within the reconciliation phase. No DOM mutations have actually occurred at this point, so any partially rendered work can be safely abandoned.

We can see the Suspense component in action here:

Once we click the "Render Component" button the `Suspended component` begins rendering. During its render, it throws a promise that resolves after 3 seconds. While the promise is pending, the Suspense component catches it and displays the fallback UI ("Loading"). Once the promise resolves, rendering of `Suspended component` resumes and the final content is displayed.

There is a lot more intricacy to how Fiber enables this feature and although it's not directly mentioned, the mechanism is detailed in [Lin Clark's Talk](https://www.youtube.com/watch?v=ZCuYPiUIONs). The important thing here is that without the introduction of interruptible renders, the Suspense component would not exist.

By this point, we've examined the role of the React reconciler, explored the architectural shift from the stack reconciler to React Fiber and seen how Fiber enabled the modern React APIs we have today—Suspense, transitions, optimistic updates, and actions.

What’s important to recognize is **how we got here**. We've seen that the rewrite of the reconciler laid the groundwork for async/concurrent rendering; however, the features that were built on top of it emerged **incrementally**, over multiple React releases.

As a result, these features continued to be documented, taught, and adopted **in-isolation**. **Suspense** was taught as a **loading mechanism**, **transitions** were framed as a **performance optimization**, **optimistic updates** were used for **UX enhancements**, and **actions** were concerned with **server form features**. While none of these descriptions were wrong, they missed the bigger picture.

These APIs are not separate ideas but rather they are **different expressions of the same underlying model** made possible by Fiber: coordinated, priority-aware, async/concurrent rendering.

While these features can be incrementally adopted, it results in a codebase that has a hybrid architecture that never fully benefits from Async React. The code works, but the mental model remains fragmented, and the system becomes harder to reason about as complexity grows.

To build modern React applications it requires us to shift our perspective on how we approach the architecture of said applications.

So what do we mean when we say build async first?

Async first means building applications where we use declarative tools to express user intent, loading, priority, and visual continuity. This allows React to treat rendering as a schedulable, and interruptible operation that React itself coordinates.

This means that we are defining a contract with the user; when the user acts immediately, the UI should respond immediately while some asynchronous work is done in the background. When the data is ready and no other higher priority work is to be done then we can show the completed state in a coordinated operation.

Ricky Hanlon modeled this in his talk [Async React](https://www.youtube.com/watch?v=B_2E96URooA) at React Conf 2025.

Event

busy

Update

loading

Render

done

Commit

Taken together, this process looks something like our Instagram-like demo below. Let’s see how the interactions behave when we render the view, like/dislike a post, archive/unarchive a post, and switch tabs. Press **Render view** to begin!

Did you try mixing up the interactions? How did the experience change when you archived a post and then switched tabs immediately?

This demo is built using async first principles! We're using a combination of optimistic states, transitions, suspense, and activity to craft this experience. You may have noticed that switching tabs was pretty instantaneous; however, when we archived a post and then switched tabs immediately, we **optimistically** switched to the **archive tab** and showed a loading indicator within the tab viewer. Since the render for the **archive tab** wasn't ready yet, React kept the experience within the **feed tab**. Once the async work resolved with it's data, React could fully switch to the **archive tab** showing all updated archived posts.

The important thing here is that all of this coordination is handled by React and we are just defining how these interactions should look. There is **no useEffect** within this demo that handles any of the async work! So how do we build async first components??

With async first components we can **assume** that when the component renders, it's rendering with all the data it requires.

We've seen that we can use suspense to coordinate the rendering between a loading fallback and a suspended component when data is not immediately available. But if we're making these assumptions and using suspense to allow React to do the coordination then what happens in the case of an error? What happens when that promise is rejected?

This is where error boundaries come into play. Similar to how the suspense component allows us to show a fallback when a promise is thrown, error boundaries allow us to show a fallback when an error thrown within a component. React is still handling the coordination but we are just providing the fallback UI and possibly a way to reset state to before the error occurred.

The implementation details of error boundaries have not moved forward into the functional component world, however, error boundaries become a crucial aspect of async React.

We can manually write error boundaries or we can opt to use libraries that have implemented the functionality for us. Libraries such as [react-error-boundary](https://www.npmjs.com/package/react-error-boundary) become a welcome addition in the world of async first.

We do make assumptions with this model but it's important to note that embedded within these assumptions is work that React itself coordinates. This pattern allow us to say that "async" is built **within** the rendering system of React rather than **around** it. So rather than asking "How do **I** coordinate asynchronous work over time?", this model shifts our perspective to ask "How should **React** coordinate this asynchronous work over time?".

So what does this look like in practice? Let's look at the example below to find out how we can build an async first React component.

```
const UsersList = ({ userDataPromise }) => {
  const userList = use(userDataPromise);

  return (
    <div>
      {userList.map((user) => (
        <p key={user.id}>{user.name}</p>
      ))}
    </div>
  );
};

const AsyncFirstDemo = ({ userDataPromise }) => {
  return (
    <ErrorBoundary fallback={<ErrorFallback />}>
      <Suspense fallback={<LoadingFallback />}>
        <UsersList userDataPromise={userDataPromise} />
      </Suspense>
    </ErrorBoundary>
  );
};
```

Do you remember our data fetching useEffect example from above? This looks a lot simpler right!?? We can see that an async first component brings the core principles of React to a world where data may not be immediately available. We describe to React how we want our components to look and function, and we let React coordinate the rest.

You'll notice that in the example above we did not include the data fetching logic. This was intentional as the focus here was to show how we could build an async first component. However, we can fetch data in a number of ways; be it through server components, data fetching libraries, or even manually fetching data and passing down promises as props.

Libraries such as TanStack Query have embraced this model and provide hooks that return promises which can be used directly within async first components. However, we can of still write our own data fetching logic that returns a promise as well.

**Yes!** We keep saying **promise** here as we are not the ones that are writing the coordination! So whether the promise is pending, resolved, or rejected, it's React that is handling the coordination.

## Component Systems and Routers with Async React

WOW!! This is a real paradigm shift in the way we think about building components. At first glance, it can feel like we’re trading simplicity for abstraction; adding new concepts like actions, Suspense/Error boundaries, transitions, and optimistic state just to achieve a more declarative, async-first model.

So it's natural to ask:

**Is this really how we’re supposed to be building applications now?** In short, yes but also no! It's more nuanced than that!

Naturally this is where we would reach for component libraries or systems; A shared set of reusable, composable UI components which are already responsible for encoding design, behaviour, and accessibility decisions. These libraries/systems should also be able to participate within the async first model.

This is where **Action props** come into play! An action prop is just a prop that wraps the accepted synchronous/asynchronous function within a transition. This small change has large implications and it looks something like this:

```
<Button action={saveUserAction}>Save</Button>
```

By accepting an action, the `Button` component can automatically reflect where it is within the rendering lifecycle. Be it pending states, disabled states, preventing duplicate interactions by default, or propagating errors to the nearest boundary; the action integrates these concerns into the component thereby allowing the consumer of the component to just declare what the button does.

We're already seeing this concept being added to React elements, specifically the form element. Instead on passing an `onSubmit` function to the form element, you can pass an `action` (ie sync/async function) to a form. This allows the children components to have access to the pending transition state or returned value from that action. Async first component libraries and systems are just an extension of this concept!

So in essence, async first component become **intent-driven**. They allow us to focus on declaring what the UI should do, rather than wiring up boilerplate for every async operation. We are essentially walking up the abstraction tree -- **Again**!

Combining async-first components, and async component systems with suspense enabled routers builds on the notion of embracing an async first architecture within a React application.

**Suspense enabled routers** are routing systems designed to natively handle components that may suspend while loading data or code. These routers automatically wrap route rendering within suspense boundaries and show a defined fallback UI until the route is ready to render. We still have to define the fallback UI for the page, be it a skeleton or loading spinner, but then the router handles the rest. Moreover, similar to how we can define a fallback UI for the suspense boundaries, suspense enabled routers also allow us to define an error fallback UI in the event that the suspended component cannot be resolved.

Using suspense enabled routers also means that we are opting into navigation and data fetching solutions that are using React’s async rendering strategy. This means that navigation's are wrapped within transitions and thus considered low-priority updates. Here React **keeps the current UI responsive and visible** while the next route is being prepared. This becomes important when route components suspend for data or code, because the transition prevent unnecessary loading UI.

This looks something like this! Click through the tabs to see how the router handles async components.

## Community Integrations

Explore how the community is leveraging Async React Priority in their projects.

- Installed
- Explore
- Recommended

### Recommended

We can see that clicking on the Explore tab reveals a pending state within the navigation bar while the router prepares the component in the background. Once the component/route is ready, the router switches to the Explore tab. The important thing to note here is that the current UI remains visible and interactive while the next route is being prepared. So if we were to switch to the Explore tab and then quickly switch to the Recommended tab, the router would cancel the preparation of the Explore route and begin preparing the Recommended route instead. This creates a seamless experience when navigating through the application and updates aren't jarring to the user.

These mechanisms are exposed through the routers APIs and can differ in implementation but the core logic that enables us to hook into suspense and transitions remains the same.

Frameworks like NextJS App router support a suspense enabled router solution. These routers allow us to define a fallback UI for both suspense and error boundaries within the routing API and the suspended components are automatically handled. Since NextJS has a file-based routing system, we just define a `loading.tsx` and `error.tsx` to enable fallbacks for route pages to be visible.

Libraries such as React Router V7 framework/data mode also support a suspense enabled routing solution; however, this library is not a pure suspense driven router. Here all navigations are wrapped within transitions and thus considered low priority updates. The feature that this router lacks is automatically wrapping all components defined within the router within a suspense boundary. It is something to be aware of as we transition into the async first world and we can still manually wrap our routes within a suspense boundary to have an appropriate fallback UI shown.

It is pretty fascinating how all these pieces come together right!?? Async first components, async first component libraries/systems, and suspense enabled routers all work in tandem to allow us to build React applications that embrace **async** as the default.

WOW!! Async React, it only took 10 years but it's here!! This is an incredible feat of engineering and also a huge mindset shift in how we should build React applications today.

But through our journey we discovered that we didn't get to Async React by accident. We found that the change in the underlying mechanism of the React reconciler, the shift from the stack reconciler to React Fiber, enabled the ability to schedule, interrupt, prioritize, and abandon renders before any updates were committed to the DOM. We further uncovered the role Fiber played in the mechanisms behind features like suspense and transitions.

This then opened up the conversation around Async React and how the APIs released within React 18/19 were not isolated ideas but rather an expression of an underlying mental model made possible by Fiber.

So, what is **Async React**?!??

We found that it’s a **way of thinking and building with React that embraces async as the default**, rather than treating it as an edge case or an afterthought. Here **React** does the coordination of when and how UI updates happen instead of forcing components to manage these dependencies themselves. This allows components to assume that data is available, suspend when it isn’t, and resume automatically without manual loading or lifecycle orchestration. So we a

... (content truncated)
