---
type: twir-item
issue: 259
item: 8
item_type: item
date: 2025-11-19
source: https://marmelab.com/blog/2025/11/14/react-server-components-with-parcel.html
tags:
  - "Nextjs"
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-11-19-TWIR-259|Index]]

# Item 8: React Server Components With Parcel

Source: [https://marmelab.com/blog/2025/11/14/react-server-components-with-parcel.html](https://marmelab.com/blog/2025/11/14/react-server-components-with-parcel.html)

Summary:
Parcel 2.9.0 adds support for React Server Components (RSC), enabling server-rendered React apps outside of Next.js. The article walks through building a task management app using RSC with Parcel, covering server setup, data fetching, URL parameter handling, navigation, and optimistic updates.

Key takeaways:
- Parcel now supports RSC, broadening the ecosystem beyond Next.js.
- RSC enables colocated data fetching and rendering logic, improving performance and developer experience.
- The guide demonstrates practical patterns for server-side routing, data access, and client-server interaction with Parcel.

Recommendation:
Read fully

Content:
# React Server Components With Parcel

React Server Components (RSC) is a new feature in React that allows developers to build server-rendered applications with React components that can run on the server.
The promise is that it allows for better performance and improved user experience, as the server can handle data fetching and rendering, while the client can focus on interactivity.
It also changes the way we structure our applications, allowing us to colocate data fetching and rendering logic in the same component.

RSC was only available in Next.js for a while, but other bundlers and frameworks are starting to support it. The good news is Parcel [added support for RSC](https://parceljs.org/recipes/rsc/) in version 2.9.0.

In this article, we will explore how to use RSC with Parcel by building a simple task management application.

Declaring a new page in Parcel involves declaring a new route in your server framework. For instance with Express:

```
import { renderRequest } from "@parcel/rsc/node";

import express from "express";

import { AboutPage } from "./pages/about/AboutPage";

app.get("/about", addDelay, async (req, res) => {

await renderRequest(req, res, <AboutPage />, { component: AboutPage });

console.log("Server listening on port http://localhost:3000");
```

![The about page](/_astro/about-page.BpXupwcb_V2Ew3.webp)

Nothing really new here. As you would expect, the React components are rendered server-side, so the browser mostly receives HTML markup (HTML at `1.5kB`, CSS at `10kB`), along with a small runtime (two files, a general one at `5.0kB` and a page specific at around `65kB`), speeding up the rendering process.

![Browser DevTool network tab showing the files mentioned above](/_astro/about-page-network.BSORB2x5_ZXutMz.webp)

RSC become interesting when you have to fetch data from a database or an API. Server components can now await their data by calling server-side functions. Here is an example of a task list page that fetches tasks from a database:

```
// In src/pages/tasks/TasksPage.tsx

import { Layout } from "../../layout/Layout";

import { TaskList } from "./TaskList";

import { getTasks } from "./tasks";

export async function TasksPage({

filter?: "active" | "completed" | undefined;

const { tasks, totalActiveTasks } = await getTasks(filter);

totalActiveTasks={totalActiveTasks}
```

As you can see, `<TasksPage>` calls a `getTasks` function and awaits it directly (no `useEffect` here). The `getTasks` function is declared in a file that has the `"use server";` directive:

```
// In src/pages/tasks/tasks.ts

import { db } from "../../db";

export const getTasks = async (filter?: string) => {

.order("created_at", { ascending: false });

if (filter === "active") {

query.is("completed_at", null);

} else if (filter === "completed") {

query.not("completed_at", "is", null);

const { data, error } = await query;

const { count: totalActiveTasks, error: errorActiveTask } = await db

.select("id", { count: "exact", head: true })

.is("completed_at", null);

if (error || errorActiveTask) {

`Error fetching tasks: ${

error ? error.message : errorActiveTask?.message

return { tasks: data, totalActiveTasks: totalActiveTasks ?? 0 };
```

Let’s expose this task list to the client. We’ll need a new Express route for that. The `<TasksPage>` component accepts an optional `filter` prop, so the route will read that filter from the URL and pass it to the component:

```
import { callAction, renderRequest } from "@parcel/rsc/node";

import express from "express";

import { TasksPage } from "./pages/tasks/TasksPage";

app.get("{/:filter}", addDelay, async (req, res) => {

const filter = getFilter(req.params.filter as string | undefined);

if (filter !== undefined && filter !== "active" && filter !== "completed") {

res.status(404).send("Not found");

await renderRequest(req, res, <TasksPage filter={filter} />, {

const getFilter = (filter: string | undefined) => {

if (filter === "active" || filter === "completed") {
```

This ensure that users accessing the `/active` route will only load the necessary tasks.

Thanks to RSC, just like the About page, the Task List page will be sent by the server as HTML code showing the list of tasks. As a result, the network payloads are very small, ensuring fast parsing and loading of the content.

![Browser DevTool network tab showing the files mentioned above](/_astro/list-page-network.BjqoZ-2D_Z1uWcA5.webp)

On the client side, the `<TaskList>` renders simple HTML links with some tailwind classes to filter the tasks:

```
// In src/pages/tasks/TaskFilter.tsx

currentFilter: "active" | "completed" | undefined;

filter?: "active" | "completed";

children: React.ReactNode;

data-active={currentFilter === filter ? true : undefined}

className="basis-1/3 group btn btn-sm join-item data-active:btn-primary"

<span className="hidden group-data-loading:block group-data-loading:loading group-data-loading:loading-spinner group-data-loading:loading-xs" />
```

Clicking on this link would normally trigger a full page reload, but the [Parcel documentation](https://parceljs.org/recipes/rsc/#routing) explains how to avoid this with a client-side script that intercepts link clicks and performs RSC navigation instead:

```
import { hydrate, fetchRSC } from "@parcel/rsc/client";

let updateRoot = hydrate();

async function navigate(pathname, push = false) {

let root = await fetchRSC(pathname);

history.pushState(null, "", pathname);

// Intercept link clicks to perform RSC navigation.

document.addEventListener("click", (e) => {

let link = e.target.closest("a");

link.dataset.loading = "true"; // Show loading state

navigate(link.pathname, true)

delete link.dataset.loading; // Hide loading state

// When the user clicks the back button, navigate with RSC.

window.addEventListener("popstate", (e) => {

navigate(location.pathname);
```

The original Parcel code was modified to add the `data-loading` attribute on the link while loading the page, allowing to notify users immediately that their action is being handled:

![The tasks page with the All link in active state and the Completed link in loading state](/_astro/list-page-links.DtERcpHq_HR4Sz.webp)

As explained in the Parcel documentation, note that this will still replace the whole page content and that we should rely on a routing library to update the page content more granularly. At the time of writing, [React Router just released experimental support for RSC](https://reactrouter.com/how-to/react-server-components#react-server-components) but we haven’t tried it yet.

Things get interesting when mutating data. With RSC, you can import server functions from a file that has the `"use server;"` directive and call it directly. Under the hood, a `fetch` request will actually happen, thus blurring the line between client and server code.

For instance, the TaskList may include a form to add a new task:

```
// In src/pages/tasks/TaskList.tsx

import { addTask } from "./tasks";

export const TaskList = ({

filter?: "active" | "completed";

totalActiveTasks: number;

const handleAddTask = async (formData: FormData) => {

<form action={handleAddTask}>

<li key={task.id}>{task.description}</li>

Total tasks: {totalActiveTasks}
```

The `addTask` function is a Server Function that inserts the new task in the database:

```
// In src/pages/tasks/tasks.ts

import { db } from "../../db";

export const addTask = async (formData: FormData) => {

const description = formData.get("description");

if (!description || typeof description !== "string") {

throw new Error("Invalid task description");

const { error } = await db.from("tasks").insert([{ description }]);

throw new Error(`Error adding task: ${error.message}`);
```

This works fine, but the user experience is perfectible. Users have to wait for the server response to see the newly inserted task. But we can do better with [optimistic updates](https://react.dev/reference/react-dom/components/form#optimistically-updating-form-data)!

For those unfamiliar with the term, it means that while the mutation (the `POST` request to the server that creates the new task) is being called, we can fake its result in the UI immediately.
In most cases, the server call should succeed but users will see an updated UI sooner. In case the server call fails, we can just rollback the UI changes.

React now provides the [`useOptimistic`](https://react.dev/reference/react/useOptimistic) hook for that:

```
import { addTask } from "./tasks";

import { getTaskFromFormData } from "./getTaskFromFormData";

export const TaskList = ({

filter?: "active" | "completed";

totalActiveTasks: number;

const initialOptimisticData = { tasks, totalActiveTasks };

const [optimisticData, setOptimisticTasks] = useOptimistic<

{ tasks: Task[]; totalActiveTasks: number },

>(initialOptimisticData, (currentOptimisticDataValue, newTasks) => {

const { totalActiveTasks } = currentOptimisticDataValue;

totalActiveTasks: totalActiveTasks + 1,

const handleAddTask = async (formData: FormData) => {

setOptimisticTasks([...tasks, getTaskFromFormData(formData)]);

startTransitionNewTask(async () => {

await addTask(formData).catch((error) => {

setOptimisticTasks(tasks); // rollback the tasks to the initial value

<form action={handleAddTask}>

{optimisticData.tasks.map(task => (

<li key={task.id}>{task.description}</li>

Total tasks: {totalActiveTasks}

Total tasks: {optimisticData.totalActiveTasks}
```

Now the UI is updated immediately when the user adds a new task, providing a smoother experience.

React Server Components allow a new type of reusable components, that contain both the frontend and backend logic. Think about a `<LikeButton>` component that displays the number of likes and allows users to like an item, including the data mutation logic to increment the like count on the server.

These components can be used in multiple places in your application, without duplicating the logic for fetching and mutating data. These are sometimes called *Full-Stack Components*. I borrowed this term from an [article by Kent C. Dodds](https://www.epicweb.dev/full-stack-components) that explains the pattern in the context of Remix (and applies to react-router as well) but the idea is mostly the same with RSC.

Let’s look at a practical example: a button component that toggles a task completion state.

```
// In src/pages/tasks/TaskCheckbox.tsx

import { useOptimistic, useTransition } from "react";

import type { Task } from "../../types";

import { updateTask } from "./api";

import { CircleCheckIcon, CircleIcon } from "./icons";

export const TaskCheckbox = ({

const [isPending, startTransition] = useTransition();

const [optimisticCompleted, setOptimisticCompleted] = useOptimistic<

task.completed_at ? true : false,

// Optimistic update function

className="group inline-flex w-auto"

data-loading={isPending ? "true" : undefined}

const completed_at = task.completed_at

? "" // If the task is completed, we want to mark it as not completed

: new Date().toISOString(); // If the task is not completed, we want to mark it as completed

formData.append("completed_at", completed_at);

setOptimisticCompleted(!optimisticCompleted);

startTransition(async () => {

await updateTask(formData);

<input type="hidden" name="id" value={task.id} />

data-tip={optimisticCompleted ? "Undo" : "Complete"}

className="btn btn-square btn-ghost hover:text-primary group-data-loading:text-base-content/75"

<span className="sr-only">

{optimisticCompleted ? "Undo" : "Complete"}

{optimisticCompleted ? <CircleCheckIcon /> : <CircleIcon />}
```

We can use `<TaskCheckbox>` in both a `<TaskListItem>` component and in another page that edit a single task.

Although I stripped most of the styling and non-essential code for clarity, you can find the full source code of this example application on GitHub: [marmelab/parcel-rsc-app](https://github.com/marmelab/parcel-rsc-app).

React Server Components are a powerful way to build server-rendered applications with React.
They allow you to fetch data directly in your components and calling your backend functions in a more natural way, making it easier to reason about your data flow and reducing the need for complex state management.
This ensures that your application is fast and responsive, while also providing a great user experience.

The great news is that RSC is not tied to a specific framework like Next.js anymore, and can be used with other bundlers like Parcel. But to build production-ready applications, you will need to address other concerns like routing, optimistic updates, and caching.

Related notes: [[Server Components]]
