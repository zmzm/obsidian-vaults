---
type: twir-item
issue: 255
item: 2
item_type: item
date: 2025-10-22
source: https://github.com/rickhanlonii/async-react
tags:
status: auto
quality: keep
---

[[2025-10-22-TWIR-255|Index]]

# Item 2: Async React demo

Source: [https://github.com/rickhanlonii/async-react](https://github.com/rickhanlonii/async-react)

Summary:
This repo demonstrates the future of writing product code in React with built-in async features, as showcased at React Conf 2025. It highlights default async routing, Suspense-based data fetching, and design components that handle optimistic updates and loading states automatically. The demo includes a network debugger to visualize fast and slow network scenarios and references a new Async React Working Group.

Key takeaways:
- Async React aims for seamless async flows: transitions and Suspense are default, reducing need for manual API usage.
- Design components are optimized for async actions and user feedback, including optimistic UI and delayed loading.
- The demo app shows how network speed affects UI, with automatic batching and loading state handling.
- The Async React Working Group is forming to make these patterns the default in React.

Recommendation:
Summary sufficient (read repo/docs if implementing or exploring async patterns in depth)

Why it matters:
read repo/docs if implementing or exploring async patterns in depth

Content:
# rickhanlonii/async-react: The final state of the React Conf 2025 Async React talk. · GitHub

The final state of the React Conf 2025 Async React talk.

View the app: <https://async-react.dev/>

Install:

Run the frontend:

Optional: you can use a real backend by updating `.env` to:

```
VITE_USE_REAL_SERVER=true
```

And run the backend:

This is useful when viewing React Performance Tracks because you can see the real network requests.

This repo shows the future vision for how product code will be written in React without needing additional APIs.

This is possible, but implementing Async React features in:

- **Routing**: The router uses transitions by default, so users don't need to wrap navigation updates in additional transitions.
- **Data Fetching**: The data fetching layer uses suspense by default, so users can use transitions and suspense throughout their app.
- **Design Components**: The design components expose `action` props so callbacks are in async transitions by default. To provide user feedback, these components also use optimistic updates to automatically show results and delayed loading states, no matter what the product code does in the action.

In the app, there is a network debugger at the bottom. By changing the timing for events, you can see the experience for:

- **Fast network (<150ms)**: No loading states, the app performs and feels synchronous.
- **Slow network (>150ms)**: Automatically displays loading states, and batches updates to prevent async bugs.

Our code for the login form is simple and declarative:

```
export default function Login() {
  const router = useRouter();
  const [fields, setFields] = useState(initialFieldData);

  async function submitAction() {
    await login(fields.username, fields.password);
    await prefetchLessons();
    router.navigate("/");
  }
  return (
    <Design.LoginForm fields={fields} setFields={setFields}>
      <Design.Button action={submitAction}>Login</Design.Button>
    </Design.LoginForm>
  );
}
```

When network is fast, login will instantly navigate to the logged in page, with no visible loading states:

async-react-login-sync.mov

[
](https://private-user-images.githubusercontent.com/2440089/501657209-6088811c-2a0f-4a14-a3bd-4a96b7dc12a8.mov?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzYxODc4MzksIm5iZiI6MTc3NjE4NzUzOSwicGF0aCI6Ii8yNDQwMDg5LzUwMTY1NzIwOS02MDg4ODExYy0yYTBmLTRhMTQtYTNiZC00YTk2YjdkYzEyYTgubW92P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTRUMTcyNTM5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9N2M5NmQ3MDg1NjkyMmEwMTkyMTlkNWM4NmJjYzgzYzE2NTkwZmM0OTYzOGEwNDEwYTM2MWRlNDEyYmJhZjJkNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGcXVpY2t0aW1lIn0.lmjMkMn_2Ln56RwS1UpvaIngSSLsKN8Xax6CaeqWwlI)

When network is slow, but under a second, the prefetching allows us to still animate in the logged in page without a glimmer:

async-react-login-async-fast.mov

[
](https://private-user-images.githubusercontent.com/2440089/501657512-51a158cc-f345-47d1-8408-bfdb48d3ba59.mov?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzYxODc4MzksIm5iZiI6MTc3NjE4NzUzOSwicGF0aCI6Ii8yNDQwMDg5LzUwMTY1NzUxMi01MWExNThjYy1mMzQ1LTQ3ZDEtODQwOC1iZmRiNDhkM2JhNTkubW92P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTRUMTcyNTM5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NWQxNWVlODAyMGZmNWZkZGNiMTM3Y2Y0ZWYwMWM2NDljOGViMjEyOGRjZjFmMzZmODQyZDI3ODY5YTc1YTM5ZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGcXVpY2t0aW1lIn0.-p8y-942dEmu70DDIJI_hYYAZpiiTMo8bS3Ps8jnroE)

When network is over 1s, we animate to fallbacks while the data loads:

async-react-login-async-slow.mov

[
](https://private-user-images.githubusercontent.com/2440089/501658593-6c04346e-903e-461c-b76e-b35b4c537698.mov?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzYxODc4MzksIm5iZiI6MTc3NjE4NzUzOSwicGF0aCI6Ii8yNDQwMDg5LzUwMTY1ODU5My02YzA0MzQ2ZS05MDNlLTQ2MWMtYjc2ZS1iMzViNGM1Mzc2OTgubW92P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTRUMTcyNTM5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZjcwMzM3NDVjZjZiMGI5MTVkZGI3MDNlNzU4Y2NkZTIwYTY3MGUyNDEzMjYxOWVjZGZiOWE1YTIwOTM2MWM0MiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGcXVpY2t0aW1lIn0.4UjWqVA3J0wRYpSUhenbDqF-RaD43s31wKbPPyF4yY8)

Our code for the home page is also simple and declarative:

```
export default function Home() {
  const router = useRouter();
  const search = router.search.q || "";
  const tab = router.search.tab || "all";

  function searchAction(value) {
    router.setParams("q", value);
  }
  function tabAction(value) {
    router.setParams("tab", value);
  }
  async function completeAction(id) {
    await data.mutateToggle(id);
    router.refresh();
  }
  return (
    <>
      <Design.SearchInput value={search} changeAction={searchAction} />
      <Design.TabList activeTab={tab} changeAction={tabAction}>
        <Suspense fallback={<Design.FallbackList />}>
          <LessonList
            tab={tab}
            search={search}
            completeAction={completeAction}
          />
        </Suspense>
      </Design.TabList>
    </>
  );
}
```

When network is fast, the app feels like it's synchronous:

async-react-flow-sync.mov

[
](https://private-user-images.githubusercontent.com/2440089/501660260-578a235c-92d7-467b-9664-16ec48f9555c.mov?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzYxODc4MzksIm5iZiI6MTc3NjE4NzUzOSwicGF0aCI6Ii8yNDQwMDg5LzUwMTY2MDI2MC01NzhhMjM1Yy05MmQ3LTQ2N2ItOTY2NC0xNmVjNDhmOTU1NWMubW92P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTRUMTcyNTM5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NDM3N2QwMjdhYThkMDg5ZGQxZDkxZDI2ODljYTdlNTkzMzUzZDI4ZDg5YmUzMmE2ZGQ0M2E4ZWFiYmE0ODc2ZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGcXVpY2t0aW1lIn0.lCuui4VMWxQoviHAA1u5QDcYXD7T7AFObkwwVoxo7GU)

As network slows, the app will automatically show loading states:

async-react-flow-async.mov

[
](https://private-user-images.githubusercontent.com/2440089/501660536-621f1789-19b0-4f29-b00e-55fd0b893cab.mov?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzYxODc4MzksIm5iZiI6MTc3NjE4NzUzOSwicGF0aCI6Ii8yNDQwMDg5LzUwMTY2MDUzNi02MjFmMTc4OS0xOWIwLTRmMjktYjAwZS01NWZkMGI4OTNjYWIubW92P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTRUMTcyNTM5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODU5NzUzNjE0MDYzOGNkMTE2NTk2Yzc4NDJkMjg2ODhlNzU2MmZkZGZmYzcxMmM0ODIyYWViN2ZkYWIwYjZlMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGcXVpY2t0aW1lIn0.GaHpTfznKWj2-Cqw2W3zOESmjYWepS8Kt6FHuUk8_2w)

# Async React Working Group

At React Conf 2025, we announced a new working group to make Async React the default for React apps.

Check out the [Async React Working Group](https://github.com/reactwg/async-react/discussions) to follow the progress.
