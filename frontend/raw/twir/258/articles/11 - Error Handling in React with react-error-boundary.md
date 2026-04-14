---
type: twir-item
issue: 258
item: 11
item_type: item
date: 2025-11-12
source: https://certificates.dev/blog/error-handling-in-react-with-react-error-boundary?friend=TWIR
tags:
status: auto
quality: keep
---

[[2025-11-12-TWIR-258|Index]]

# Item 11: Error Handling in React with react-error-boundary

Source: [https://certificates.dev/blog/error-handling-in-react-with-react-error-boundary?friend=TWIR](https://certificates.dev/blog/error-handling-in-react-with-react-error-boundary?friend=TWIR)

Summary:
The react-error-boundary library provides flexible and composable error handling for React applications, allowing developers to display fallback UIs and capture errors at route or feature boundaries. It supports static and dynamic fallback components, error logging, and integrates with async error handling via the useErrorBoundary hook. The article also notes React 19’s improvements in automatic error boundary integration, especially with form actions and useTransition.

Key takeaways:
- react-error-boundary offers multiple ways to render fallback UIs and handle errors gracefully.
- Strategic placement of error boundaries isolates failures without disrupting the whole app.
- Async errors can be handled via throwing during render or using useErrorBoundary in event handlers.
- React 19 enhances error boundary integration with new features.

Recommendation:
Summary sufficient

Content:
# Error Handling in React with react-error-boundary

Learn how to handle errors in React applications with react-error-boundary. Explore fallback UIs, async error handling with useErrorBoundary, and React 19's automatic error boundary integration with form actions and useTransition.

When React components throw errors during rendering, they crash your entire application, leaving users with a blank screen. The `react-error-boundary` library solves this by catching errors and displaying fallback UIs instead.

This post explores using `react-error-boundary` for error handling in React. We'll cover the three ways to render fallback UIs, strategic placement at route and feature levels, and handling async errors through throwing, the `useErrorBoundary` hook, and React 19's automatic error boundary integration with Actions.

## Getting Started

First, install the `react-error-boundary` library from npm:

```
      npm install react-error-boundary
```

Once installed, import the `ErrorBoundary` component and wrap it around any part of your component tree where you want to catch errors.

## Three Ways to Render Fallbacks

The `ErrorBoundary` component accepts fallback UIs in three different ways, giving you flexibility based on your needs.

### Simple Fallback Element

The simplest way to use error boundaries is with a static fallback element. Use this when you need to display a basic error message without access to error details or recovery options:

```
      import { ErrorBoundary } from "react-error-boundary";

<ErrorBoundary fallback={<div>Something went wrong</div>}>
  <MyComponent />
</ErrorBoundary>
```

The fallback element doesn't receive any props - it's just a static React element displayed when an error occurs.

### Fallback Component

When you need access to the error details and reset functionality, pass a component to the `FallbackComponent` prop:

```
      function ErrorFallback({ error, resetErrorBoundary }) {
  return (
    <div role="alert">
      <h2>Something went wrong</h2>
      <pre>{error.message}</pre>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

<ErrorBoundary FallbackComponent={ErrorFallback}>
  <MyComponent />
</ErrorBoundary>
```

The component receives `error` and `resetErrorBoundary` as props, letting you display specific error messages and provide recovery options.

### Render Prop

The `fallbackRender` prop is functionally identical to `FallbackComponent` but uses a render prop pattern instead of a separate component:

```
      <ErrorBoundary
  fallbackRender={({ error, resetErrorBoundary }) => (
    <div role="alert">
      <p>Error: {error.message}</p>
      <button onClick={resetErrorBoundary}>Retry</button>
    </div>
  )}
>
  <MyComponent />
</ErrorBoundary>
```

Use `fallbackRender` for inline error UIs and `FallbackComponent` when you want to reuse the error component across multiple boundaries.

Error boundaries work composably with other React features like Suspense, letting you build declarative UIs where loading and error states are handled at the boundary level rather than within individual components. This keeps your component logic focused on the happy path while boundaries handle the edge cases.

## Error Logging

Beyond displaying errors to users, you'll want to track them for debugging. The `onError` callback lets you send errors to monitoring services or log them to your backend:

```
      const logError = (error, info) => {
  console.error("Caught error:", error);
  console.error("Component stack:", info.componentStack);
  // Send to error tracking service
};

<ErrorBoundary FallbackComponent={ErrorFallback} onError={logError}>
  <MyComponent />
</ErrorBoundary>
```

The callback receives the error and component stack trace, which you can send to monitoring services like Sentry or LogRocket.

## Strategic Error Boundary Placement

Where you place error boundaries determines how much of your UI becomes unavailable when something breaks. Avoid wrapping every component - this creates visual chaos with scattered error messages. Instead, place boundaries at logical divisions like routes or features where errors can be isolated without disrupting the entire user experience.

### Route-Level Boundaries

Place error boundaries at the route level to keep navigation functional when a page crashes:

```
      <Layout>
  <Header />
  <ErrorBoundary FallbackComponent={PageError}>
    <Route />
  </ErrorBoundary>
  <Footer />
</Layout>
```

The header, footer, and navigation remain functional even when a route throws an error.

### Feature-Level Boundaries

Wrap independent features in separate boundaries to isolate failures:

```
      <Dashboard>
  <ErrorBoundary fallback={<WidgetError />}>
    <AnalyticsWidget />
  </ErrorBoundary>
  <ErrorBoundary fallback={<WidgetError />}>
    <NotificationsWidget />
  </ErrorBoundary>
</Dashboard>
```

If the analytics widget crashes, notifications continue working independently.

## Handling Async Errors

Error boundaries catch errors during rendering, but they don't catch errors from event handlers, async callbacks, or promises. This means you need a different approach for async operations.

### Throwing Errors

The simplest approach is to throw errors during rendering. If your hook returns an error, throw it to propagate it to the nearest error boundary:

```
      function UserProfile() {
  const { status, data, error } = useUser();
  if (error) throw error;

  return status === 'success' ? <div>{data.name}</div> : <div>Loading...</div>;
}
```

This eliminates the need for try-catch blocks or local error state. Data fetching libraries like TanStack Query can also provide this functionality automatically with options like `throwOnError`.

### Using the useErrorBoundary Hook

When you can't throw during rendering (like in event handlers or async callbacks), you can use the `useErrorBoundary` hook to manually propagate errors:

```
      import { useErrorBoundary } from "react-error-boundary";

function MyComponent() {
  const { showBoundary } = useErrorBoundary();

  const handleSubmit = async () => {
    try {
      await submitForm();
    } catch (error) {
      showBoundary(error);
    }
  };

  return <button onClick={handleSubmit}>Submit</button>;
}
```

The `showBoundary` function propagates the error to the nearest error boundary, triggering the fallback UI just like a rendering error would.

### Using Actions

Alternatively, React 19 Actions provide automatic error boundary integration without needing manual error handling. Actions are functions called inside transitions - they can update state and perform side effects while the work is done in the background without blocking user interactions. React automatically catches any errors thrown by Actions and propagates them to the nearest error boundary.

To learn more about React 19 Actions, check out [Building Reusable Components with React 19 Actions](https://certificates.dev/blog/building-reusable-components-with-react-19-actions).

### Form Actions

The simplest way to use Actions is with the React 19 form `action` prop or any other library that provides action props:

```
      function SubmitForm() {
  async function submitAction(formData) {
    await submitFormData(formData.get('email'));
  }

  return (
    <form action={submitAction}>
      <input name="email" required />
      <button type="submit">Submit</button>
    </form>
  );
}

function FormError({ error, resetErrorBoundary }) {
  return (
    <div role="alert">
      <p>{error.message}</p>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

<ErrorBoundary FallbackComponent={FormError}>
  <SubmitForm />
</ErrorBoundary>
```

The `action` prop wraps the function in a transition, catching any errors and displaying the fallback with a retry option. You can track pending states with `useFormStatus`, `useActionState`, or an individual `useTransition`.

### useTransition Actions

For non-form async code, use the `useTransition` hook:

```
      import { useTransition } from "react";

function DeleteButton({ itemId }) {
  const [isPending, startTransition] = useTransition();

  const handleDelete = () => {
    startTransition(async () => {
      await deleteItem(itemId);
    });
  };

  return (
    <button onClick={handleDelete} disabled={isPending}>
      {isPending ? "Deleting..." : "Delete"}
    </button>
  );
}
```

This works exactly like the form action example above - errors are automatically caught by the nearest error boundary.

## Conclusion

The `react-error-boundary` library provides a declarative approach to error handling in React. The `ErrorBoundary` component catches rendering errors and displays fallback UIs with flexible options for static elements, components, or render props. For async operations, you can throw errors during rendering, use the `useErrorBoundary` hook for event handlers, or leverage React 19's automatic error boundary integration with form actions and `useTransition`.

Strategic placement at route and feature levels keeps your UI functional when errors occur, avoiding the visual chaos of scattered error messages. Combined with error logging, reset functionality, and React 19's built-in transition support, error boundaries create resilient applications that handle failures gracefully.

For more on how to utilize error boundaries in practice, check out [Building an Async Combobox with useSuspenseQuery() and useDeferredValue()](https://certificates.dev/blog/building-an-async-combobox-with-usesuspensequery-and-usedeferredvalue).

---

**Sources:**
