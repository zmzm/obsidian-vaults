---
type: twir-item
issue: 262
item: 8
item_type: item
date: 2025-12-10
source: https://slicker.me/react/useEffectEvent.html
tags:
  - "useEffectEvent"
status: auto
quality: keep
---

[[2025-12-10-TWIR-262|Index]]

# Item 8: Do's and Don'ts of useEffectEvent in React

Source: [https://slicker.me/react/useEffectEvent.html](https://slicker.me/react/useEffectEvent.html)

Summary:
useEffectEvent is a new React hook for extracting non-reactive logic from effects, allowing access to the latest props/state without triggering unnecessary re-runs. The article provides clear guidance on correct and incorrect usage, with practical examples and migration advice. It emphasizes that useEffectEvent should not be used in event handlers or asynchronously, and is best for effect-related callbacks.

Key takeaways:
- useEffectEvent enables reading latest values in effects without adding them to dependency arrays.
- Should only be called synchronously inside effects, not in event handlers or after delays.
- Helps avoid unnecessary effect re-runs and improves code clarity.
- Wait for stable release before using in production.

Recommendation:
Read fully (read fully if adopting useEffectEvent or refactoring effect logic)

Why it matters:
read fully if adopting useEffectEvent or refactoring effect logic

Content:
# useEffectEvent in React

## What is useEffectEvent?

`useEffectEvent` is a React Hook that allows you to extract non-reactive logic from Effects. It solves the common problem where you need to read the latest value of props or state inside an Effect without causing that Effect to re-run when those values change.

**Key Concept:** useEffectEvent creates a stable function reference that always reads the latest values, but doesn't trigger Effect re-execution when those values change.

## The Problem It Solves

Consider a chat application where you want to log a message when the room changes, but you need to include the current theme in your log. Traditionally, you'd need to add theme to the dependency array, causing the Effect to re-run every time the theme changes, even though you only want to react to room changes.

â Traditional Problem:

```
useEffect(() => {
  logVisit(roomId, theme); // Re-runs when theme changes
}, [roomId, theme]); // Had to include theme!
```

â With useEffectEvent:

```
const onVisit = useEffectEvent((roomId) => {
  logVisit(roomId, theme); // Reads latest theme
});

useEffect(() => {
  onVisit(roomId); // Only re-runs when roomId changes
}, [roomId]);
```

## Do's and Don'ts

### â DO

- Use it to read the latest props/state without adding them to dependencies
- Call it directly from inside Effects
- Use it for event handlers that need to access Effect context
- Use it to separate reactive and non-reactive logic
- Call it synchronously within your Effect

### â DON'T

- Don't call it from regular event handlers
- Don't call it during rendering
- Don't pass it as a prop to components
- Don't call it asynchronously or after a delay
- Don't use it as a replacement for proper memoization

## Detailed Examples

### â DO: Extract Non-Reactive Logic

```
function ChatRoom({ roomId, theme }) {
  const onConnected = useEffectEvent(() => {
    showNotification('Connected!', theme);
  });

  useEffect(() => {
    const connection = createConnection(roomId);
    connection.on('connected', onConnected);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]); // Only roomId is reactive
}
```

This Effect only reconnects when `roomId` changes, but `onConnected` always uses the latest `theme`.

### â DON'T: Call from Event Handlers

```
function Component() {
  const onClick = useEffectEvent(() => {
    // â Wrong! Don't use in event handlers
    doSomething();
  });

  return <button onClick={onClick}>Click</button>;
}
```

Use regular functions or `useCallback` for event handlers instead.

### â DO: Reading Latest Props in Effects

```
function Timer({ interval, onTick }) {
  const onTickEvent = useEffectEvent(() => {
    onTick(); // Always calls latest onTick
  });

  useEffect(() => {
    const id = setInterval(onTickEvent, interval);
    return () => clearInterval(id);
  }, [interval]); // Only interval is reactive
}
```

### â DON'T: Call Asynchronously

```
function Component() {
  const onData = useEffectEvent((data) => {
    processData(data);
  });

  useEffect(() => {
    fetchData().then(data => {
      onData(data); // â Risky! Called asynchronously
    });
  }, []);
}
```

The function might be called after the component unmounts or after values have changed.

### â DO: Combine with Cleanup Logic

```
function Analytics({ userId, page }) {
  const logPageView = useEffectEvent(() => {
    analytics.track('page_view', { userId, page });
  });

  useEffect(() => {
    logPageView();
    
    return () => {
      // Cleanup can also use Effect Events
      const logPageExit = useEffectEvent(() => {
        analytics.track('page_exit', { userId, page });
      });
      logPageExit();
    };
  }, []); // Empty deps - runs once per mount
}
```

### â DON'T: Pass as Dependencies to Other Hooks

```
function Component() {
  const onEvent = useEffectEvent(() => {
    doSomething();
  });

  // â Don't do this
  const memoized = useMemo(() => {
    return onEvent();
  }, [onEvent]);
}
```

## Common Use Cases

### 1. Logging and Analytics

When you need to log events with the latest user preferences or settings without re-subscribing.

```
const logEvent = useEffectEvent((eventName) => {
  analytics.log(eventName, { theme, locale, userId });
});

useEffect(() => {
  logEvent('page_visit');
}, [pathname]); // Only react to pathname changes
```

### 2. Callbacks with Latest State

When passing callbacks to third-party libraries that shouldn't cause re-subscriptions.

```
const onMessage = useEffectEvent((msg) => {
  showToast(msg, { variant: userPreference });
});

useEffect(() => {
```

### 3. Debouncing with Latest Values

When implementing debouncing while always using the latest callback logic.

```
const onSearch = useEffectEvent(() => {
  performSearch(query, filters, sortBy);
});

useEffect(() => {
  const timeoutId = setTimeout(onSearch, 500);
  return () => clearTimeout(timeoutId);
}, [query]); // Debounce query, but use latest filters/sortBy
```

## Best Practices

- Only use `useEffectEvent` when you've identified a genuine need to read non-reactive values
- Consider if your logic really belongs in an Effect or if it could be in an event handler
- Keep the Event function focused on a single purpose
- Document why you're using it to help future maintainers
- Wait for stable release before using in production applications

## Migration Path

If you're currently using `useCallback` with constantly changing dependencies or suppressing the linter with eslint-disable comments, `useEffectEvent` might be the solution you need. However, first consider if restructuring your component logic might be more appropriate.

## Conclusion

`useEffectEvent` is a powerful tool for solving the challenge of reading the latest values in Effects without causing unnecessary re-executions. By following these do's and don'ts, you'll be able to use it effectively when it becomes stable. Remember that it's meant for specific scenarios where you need to separate reactive from non-reactive logic within Effects.
