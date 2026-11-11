---
type: twir-item
issue: 304
item: 11
item_type: item
date: 2026-11-04
source: https://playfulprogramming.com/posts/writable-derived-state/
tags:
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 11: Writable Derived State: Stop Synchronizing State

Source: [https://playfulprogramming.com/posts/writable-derived-state/](https://playfulprogramming.com/posts/writable-derived-state/)

Summary:
This post discusses the pitfalls of synchronizing server-derived state with local React state, using the example of keeping user data in sync with server updates. It highlights common anti-patterns, such as resetting local state on every server fetch, which can lead to poor user experiences (e.g., losing unsaved changes). The article advocates for treating server state as a source of truth and deriving local state as needed, rather than synchronizing them directly.

Key takeaways:
- Synchronizing server and local state can lead to data loss and confusing UX.
- React patterns often encourage unnecessary duplication of state.
- Prefer treating server state as the source of truth and deriving local state as needed.
- Provides code examples illustrating both the problem and better approaches.

Recommendation:
Read fully (read fully if you often deal with server/client state synchronization issues)

Why it matters:
read fully if you often deal with server/client state synchronization issues

Content:
# Writable Derived State: Stop Synchronizing State

## Post contents

> I've [added a skill to my personal skill collection to help fetch and sync data with the server better.](https://github.com/crutchcorn/skills)
> It follows the outline of this article, but adds more than just this to your agent's capabilities.

Applications regularly find themselves needing to implement a common problem: Provide the user with a default value from the server, but allow them to overwrite the defaults.

The intuitive code sample many picture in their mind often looks something like this:

```
const userData = useServerState();onServerUpdate(() => {	userData.reset()})
```

And is often implemented something like this:

```
import { useState, useEffect, useCallback } from "react";import { getTodos, updateTodos, type Todo } from "./services";// Enums to avoid problems outlined by TkDodo here: https://tkdodo.eu/blog/why-you-want-react-querytype GetServerState<T> = {status: "loading"} | {status: "data", payload: T} | {status: "error", error: Error}function App() {	const [serverState, setServerState] = useState({status: "loading"} as GetServerState<Todo[]>);	const [todos, setTodos] = useState([] as Todo[]);	// The most problematic part of this code sample	useEffect(() => {		if (serverState.status === "data") {			setTodos(serverState.payload)		}	}, [serverState])	const fetchServerData = useCallback((signal?: AbortSignal) => {		setServerState({status: "loading"});		 getTodos({signal: signal})		 	.then(data => setServerState({status: "data", payload: data}))			.catch(err => setServerState({status: "error", error: err}))	}, []);	useEffect(() => {		const controller = new AbortController();		fetchServerData(controller.signal);		return () => controller.abort();	}, [fetchServerData])    // ...}
```

This works out pretty well at first glance. Let's now implement a "refresh server data when the user revisits the tab":

```
function useOnRevisit(fn: () => void) {	useEffect(() => {		function onVisibilityChange() {			if (!document.hidden) {				// User returned to the tab				fn();			}		}		document.addEventListener("visibilitychange", onVisibilityChange);		return () => document.removeEventListener("visibilitychange", onVisibilityChange);	}, [])}function App() {	// ...	useOnRevisit(() => fetchServerData());	// ...}
```

But "oh no!", once we refresh the page it reset the user data; why?

```
import { useState, useEffect, useCallback, useRef } from "react";import { getTodos, updateTodos, type Todo } from "./services";// Enums to avoid problems outlined by TkDodo here: https://tkdodo.eu/blog/why-you-want-react-querytype GetServerState<T> = {status: "loading"} | {status: "data", payload: T} | {status: "error", error: Error}type SetServerState = {status: "idle"} | {status: "pending"} | {status: "error", error: Error} | {status: "success"}function useOnRevisit(fn: () => void) {	useEffect(() => {		function onVisibilityChange() {			if (!document.hidden) {				// User returned to the tab				fn();			}		}		document.addEventListener("visibilitychange", onVisibilityChange);		return () => document.removeEventListener("visibilitychange", onVisibilityChange);	}, [])}export default function App() {	const [serverState, setServerState] = useState({status: "loading"} as GetServerState<Todo[]>);	const [todos, setTodos] = useState([] as Todo[]);	// The most problematic part of this code sample	useEffect(() => {		if (serverState.status === "data") {			setTodos(serverState.payload)		}	}, [serverState])	const fetchServerData = useCallback((signal?: AbortSignal) => {		setServerState({status: "loading"});		 getTodos({signal: signal})		 	.then(data => setServerState({status: "data", payload: data}))			.catch(err => setServerState({status: "error", error: err}))	}, []);	useOnRevisit(() => fetchServerData());	useEffect(() => {		const controller = new AbortController();		fetchServerData(controller.signal);		return () => controller.abort();	}, [fetchServerData])	const [fetchTodoState, setFetchTodoState] = useState({status: 'idle'} as SetServerState)	const saveTodosController = useRef<AbortController>(undefined)	function saveTodos(todos: Todo[]) {		 if (saveTodosController.current) {			saveTodosController.current.abort();		 }		 saveTodosController.current = new AbortController();		 setFetchTodoState({status: "pending"});			updateTodos({data: todos, signal: saveTodosController.current.signal})		 	.then(() => setFetchTodoState({status: "success"}))			.catch(err => setFetchTodoState({status: "error", error: err}))	}    return (        <div>            {serverState.status === "loading" && <p>Loading...</p>}            {serverState.status === "error" && <p>Error loading todos</p>}            <ul>                {todos.map(todo => (                    <li key={todo.id}>                        {todo.title} {todo.completed ? "(Completed)" : "(Pending)"}                    </li>                ))}            </ul>            <button onClick={() => setTodos([...todos, { id: Date.now(), title: 'New Todo', completed: false }])}>Add Todo</button>            <button onClick={() => saveTodos(todos)}>Save Todos</button>            {fetchTodoState.status === "pending" && <p>Saving...</p>}            {fetchTodoState.status === "error" && <p>Error saving todos</p>}            {fetchTodoState.status === "success" && <p>Todos saved successfully</p>}        </div>    );}
```

Well, it's because when we refresh the server data, we have few/no controls to retain the user data. This is the problem with "syncing" client data from the server: We're explicitly saying that the server's state should win all updates.

What if I told you that we could swap a few small lines of code to fix this bug?

```
// Beforeconst [serverState, setServerState] = useState({status: "loading"} as GetServerState<Todo[]>);const [todos, setTodos] = useState([] as Todo[]);useEffect(() => {    if (serverState.status === "data") {        setTodos(serverState.payload)    }}, [serverState])
```

```
// Afterconst [serverState, setServerState] = useState({status: "loading"} as GetServerState<Todo[]>);const [userTodos, setTodos] = useState(null as Todo[]);const todos = userTodos ?? (serverState.status === "data" ? serverState.payload : []);
```

As it turns out, the mental model of "sync client data from the server state" can be more accurately reflected by "use server data when the client's data is missing"

This approach even works for TanStack Query data fetching:

```
import { useMutation, useQuery } from "@tanstack/react-query";import { useState } from "react";import { getTodos, updateTodos, type Todo } from "#/services";function App() {    const { data: serverTodos, error, isLoading, refetch } = useQuery({        queryKey: ['data'],        queryFn: async ({signal}) => {            return getTodos({signal});        }    })    const [manualTodos, setTodos] = useState<Todo[] | null>(null);    const todos = manualTodos ?? serverTodos ?? [];    const saveTodos = useMutation({        mutationFn: async (todos: Todo[]) => {            await updateTodos(todos)        },        onSuccess: () => {            refetch().then((result) => result.isSuccess && setTodos(null));        }    });    return (        <div>            {isLoading && <p>Loading...</p>}            {error && <p>Error loading todos</p>}            <ul>                {todos.map(todo => (                    <li key={todo.id}>                        {todo.title} {todo.completed ? "(Completed)" : "(Pending)"}                    </li>                ))}            </ul>            <button onClick={() => setTodos([...todos, { id: Date.now(), title: 'New Todo', completed: false }])}>                Add Todo            </button>            <button                disabled={saveTodos.isPending}                onClick={() => saveTodos.mutate(todos)}            >                Save Todos            </button>            {saveTodos.isPending && <p>Saving...</p>}            {saveTodos.error && <p>Error saving todos</p>}            {saveTodos.isSuccess && <p>Todos saved successfully</p>}        </div>    );}
```

In fact, this guidance allows us to remove a `useEffect` in both code samples; in line with [React's official "You Might Not Need an Effect" documentation page](https://react.dev/learn/you-might-not-need-an-effect).

Hopefully, this approach clarifies how to manage client and server state in a more predictable and efficient manner, reducing the need for unnecessary effects and keeping your components simpler and easier to reason about.
