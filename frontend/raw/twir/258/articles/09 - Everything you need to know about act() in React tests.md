---
type: twir-item
issue: 258
item: 9
item_type: item
date: 2025-11-12
source: https://howtotestfrontend.com/resources/react-act-function-everything-you-need-to-know
tags:
status: auto
quality: keep
---

[[2025-11-12-TWIR-258|Index]]

# Item 9: Everything you need to know about act() in React tests

Source: [https://howtotestfrontend.com/resources/react-act-function-everything-you-need-to-know](https://howtotestfrontend.com/resources/react-act-function-everything-you-need-to-know)

Summary:
The act() function is essential for ensuring that all state updates and side effects in React tests are fully processed before assertions are made. While many testing utilities wrap their actions in act() automatically, developers need to use it explicitly when triggering state changes outside these utilities to avoid stale assertions and common “not wrapped in act()” warnings. The article explains best practices, import sources, and provides practical examples of correct usage.

Key takeaways:
- act() ensures React state updates and effects are processed before test assertions.
- Testing libraries like RTL often handle act() internally, but manual use is sometimes necessary.
- Import act() from @testing-library/react for best compatibility.
- Omitting act() can lead to flaky tests and missed bugs.

Recommendation:
Summary sufficient

Content:
# Absolutely everything you need to know about act() in React tests

When writing React tests, you will quickly become familiar with the `act()` function. Despite being a fundamental concept to testing your React apps, it is often one of the most confusing and misunderstood aspects of testing React applications.

I've also in the past found it hard to articulate why we need it to engineers learning how to test their React apps. (But hopefully I clear it up for you in this page!).

## What is act(), why do we need it and when should you use it?

In your tests, functionality that updates internal state of a rendered React component should be wrapped in `act()` so we can be sure that all state changes and side effects have been fully processed by React, before the rest of your test (i.e. assertions) continues.

This makes sure that your tests are testing things in a realistic way (without it, you might be making assertions on 'old' state values, without realising).

If you use React Testing Library (RTL) functions like the following, you don't have to think about `act()` **as they already wrap their functionality in `act()`**:

- user interaction with `userEvent` (like `await userEvent.click(...)`)
- the `await findBy...` functions like `await screen.findByText("...")`
- the `waitFor(...)` function

But - there will definitely be times you will see the famous *update was not wrapped in act()* error that will plague your command line output if you are not careful.

## Understanding the "update was not wrapped in act(...)" error

You have probably seen this a few times in your test result output:

```
An update to %s inside a test was not wrapped in act(...).

When testing, code that causes React state updates
should be wrapped into act(...):

act(() => {
  /* fire events that update state */
});
/* assert on the output */
```

This is warning you that your tests are not wrapped in `act()`. This means you might be making assertions in your test *against 'old' state* and you might not notice or catch real bugs.

(I've definitely ignored the warnings in the past, and introduced big bugs that were so easy to catch if I had used `act()` correctly!).

To see some ways to get rid of the error, see the section below

## Now, let's look at it in depth

The above is really all you need to know about React's `act()`. But if you are reading this blog, you are probably interested in really understanding everything about it. It is a very important part of writing tests, so it makes sense to fully understand it.

## Which act() should you import (React vs Testing Library)?

Firstly to clear up some confusion: React itself includes `act`. You can `import React, { act } from 'react'`.

*But you should never do this. Always import from `@testing-library/react`:*

```
import { act } from '@testing-library/react';
```

This versions from `@testing-library/react` is a very lightweight wrapper without much extra functionality. It just wraps around the actual `act()` implementation from `react`, but with these changes:

- ensures some environment configuration is in place.
  - React will warn you if you try to call `act()` outside of a test environment (when `IS_REACT_ACT_ENVIRONMENT` is not set to true).
  - Using this `act()` wrapper from `@testing-library` ensures that is set up correctly.
- it also adds better compatibility if you are running an older version of React, although in 2025 it is unlikely you will need this. I won't go into detail here, as this won't affect many people nowadays.

If you are interested, you can see how RTL's `act()` is implemented [on GitHub](https://github.com/testing-library/react-testing-library/blob/1c931a6c03091d725eccee7767d9ec696d5d33c6/src/act-compat.js#L5)  (and you might notice there is a third version of `act()`, for legacy reasons).

It was more of an issue years ago, and in 2025 you can often get away with using `act()` from the `react` package, but for consistency and those very rare edge cases it is better to always import from the RTL one!

## An example

In the following example, I will show when forgetting to use `act()` will mean your current rendered state in the test is outdated.

Let's test this simple component, it will automatically update the `count` by 1 after 10ms:

```
const AutoCounter = () => {
  const [count, setCount] = useState(0);

  

  useEffect(() => {
    setTimeout(() => {
      setCount(c => c + 1);
    }, 10);
  }, []);

  return <h1>Count: {count}</h1>;
};
```

If we write the following test, which uses fake timers, it will fail, as the rendered component is still showing `Count: 0`:

```
vi.useFakeTimers();

test('auto-increments after 10ms', () => {
  render(<AutoCounter />);
  const heading = screen.getByRole('heading');

  expect(heading).toHaveTextContent('Count: 0');

  
  
  
  vi.advanceTimersByTime(10);
  

  expect(heading).toHaveTextContent('Count: 1'); 
});
```

But if you wrap the `vi.advanceTimersByTime(10)` in `act(...)`, it will now pass:

```
vi.useFakeTimers();

test('auto-increments after 10ms', async () => {
  render(<AutoCounter />);
  const heading = screen.getByRole('heading');

  expect(heading).toHaveTextContent('Count: 0');

  
  
  
  
  await act(async () => {
    vi.advanceTimersByTime(10);
  });

  expect(heading).toHaveTextContent('Count: 1');
});
```

In a real test, you could also just
`await screen.findByText('Count: 1')`
too!

Because the `await findBy...` functions use `act()` internally

Another example, this time calling the `click` functionality *directly on a HTMLButton* (not via `userEvent`)

```
const Counter = () => {
  const [count, setCount] = useState(0);

  const onClick = () => setCount(prev => prev + 1);
  return (
    <div>
      <button onClick={onClick}>Increment</button>
      <h1>Count: {count}</h1>
    </div>
  );
};

test('clicking button updates count', async () => {
  render(<Counter />);

  const button = screen.getByRole('button');
  const heading = screen.getByRole('heading');

  expect(heading).toHaveTextContent('Count: 0');

  
  await act(async () => {
    button.click();
  });

  expect(heading).toHaveTextContent('Count: 1'); 
  
  
});
```

## Using act() when testing hooks

I find this is one of the most common ways where you have to use `act()`.

If you are testing a hook in isolation with `renderHook()`, you might be calling functions which update state. In those cases you have to wrap it in `act()`

**Example of using act() in a hook test:**

This is a simple hook we want to test:

```
const useCounter = () => {
  const [value, setValue] = useState(0);
  const increment = () => {
    setValue(val => val + 1);
  };
  return {
    increment,
    value,
  };
};
```

The following test **will fail** as the value of `result.current.value` remains at 0

```
test('can increment the counter', async () => {
  const { result } = renderHook(useCounter);

  expect(result.current.value).toBe(0); 

  result.current.increment();

  expect(result.current.value).toBe(1); 

  result.current.increment();
  expect(result.current.value).toBe(2); 
});
```

But using our friend `act()`, it will now have correct state value

```
test('can increment the counter', async () => {
  const { result } = renderHook(useCounter);

  expect(result.current.value).toBe(0); 

  await act(async () => {
    result.current.increment();
  });

  expect(result.current.value).toBe(1); 

  await act(async () => {
    result.current.increment();
  });
  expect(result.current.value).toBe(2); 
});
```

## When are times that you may have to use `act()`?

- When testing hooks & you are making state changes
- If you are manually triggering state change, for example calling `someButtonElement.click()` directly
- When manually dispatching events (not via `userEvent`)
- Sometimes when triggering events (like clicks) via `fireEvent` - especially when it triggers some async functionality
- When state change happens in timers, like `setTimeout`, `setInterval`
- When using fake timers in Jest/Vitest
- When async promises resolve and result in state changes

As explained elsewhere in this post, you should normally try to wait for render/state changes
(with `waitFor` or `findBy...`) rather than overuse `act()`.

## A note on fireEvent

In most cases, you don't need to wrap your `fireEvent` calls (such as `fireEvent.click(...)`) in `act()`.

However there are times when you will have to, especially if `fireEvent` triggers an async function which itself has some `await` inside of it.

This might be a bit controversial, but in my experience, I tend to skip `act()` for fireEvent, unless the warning shows up in the terminal or it isn't working as I expect. (Note: it is better if you can to just use `userEvent` functionality to trigger things like clicks if possible anyway.)

## Testing async behaviour

Here is a contrived example (realistically, you can avoid `act()` and just use `await screen.findBy...`).

```
import { render, screen, act } from '@testing-library/react';
import { useState } from 'react';

const AsyncButton = () => {
  const [status, setStatus] = useState('idle');

  const handleClick = async () => {
    setStatus('loading');
    
    await new Promise(resolve => setTimeout(resolve, 100));
    setStatus('done');
  };

  return (
    <div>
      <button onClick={handleClick}>Click me</button>
      <p>Status: {status}</p>
    </div>
  );
};

test('button updates status after async operation', async () => {
  render(<AsyncButton />);

  const button = screen.getByRole('button');

  expect(screen.getByText('Status: idle')).toBeInTheDocument();

  
  await act(async () => {
    button.click();
    
    await new Promise(resolve => setTimeout(resolve, 100));
  });

  expect(screen.getByText('Status: done')).toBeInTheDocument();
});
```

(like many of these examples, you can also just `await screen.findByText("Status: done")` to avoid act() too)

## Async vs sync behaviour of act()

In almost all cases where inside your `act()` call you are not calling async functions you can normally do it without async/await. But - there are some edge cases where due to how React updates it won't always work.

So you should just default to always `await act(async () => {...})`.

Note: there are plans to deprecate the non `async` version.

Here is the official React docs describing it, which I will copy/paste in as I don't think I can explain it in a more succinct way:

> async actFn: An async function wrapping renders or interactions for components being tested. Any updates triggered within the actFn, are added to an internal act queue, which are then flushed together to process and apply any changes to the DOM. Since it is async, React will also run any code that crosses an async boundary, and flush any updates scheduled.

You should **always use async** when:

- The code inside `act()` contains promises, async/await, or timers
- If you are not sure if you need to - because async is always safe

You can use the **sync** version when:

- Simple synchronous state updates only
- But async is still recommended for consistency

(Most of the examples in this page would work with just `act(() => {...})` btw. But it is easier to just always use async/await)

## When NOT to use act()

Using `act()` should be a last resort. For most code you don't need it.

Here is when not to use it:

### Do not wrap *React Testing Library* functions in `act()`

As mentioned elsewhere in this post, you shouldn't wrap things like `userEvent.click()` in act().

(They do it internally anyway).

```
await act(async () => {
  await userEvent.click(button);
});

await userEvent.click(button);
```

### Avoid `act()` if you can just `await waitFor()` or `await findBy...`

It is very common to be able to avoid calling `act()` by just using the `waitFor` or any of the `findBy...` functions which will run async code within act, until their assertions pass.

For example, the following can be replaced with a .findBy call

```
await act(async () => {
  someElement.click();
});

expect(screen.getByText('you clicked something')).toBeInTheDocument();
```

The following (manually triggering click(), then `await findByText()`) will almost definitely work too, without any warning from React saying a state change was not wrapped in act():

```
someElement.click();

expect(await screen.findByText('you clicked something')).toBeInTheDocument();
```

Another example where we can replace `act()` with a `waitFor`:

```
await act(async () => {
  vi.runOnlyPendingTimers();
});

expect(screen.getByText('some updated text')).toBeInTheDocument();
```

Can be replaced with:

```
vi.runOnlyPendingTimers();

await waitFor(() => {
  expect(screen.getByText('some updated text')).toBeInTheDocument();
});
```

## Why is it called act?

In the testing world, there is a concept of:

- *arrange* (set up the world, ready for your test)
- *act* (run the code that you are testing)
- *assert* (make assertions to check the unit under test works correctly)

## Performance issues when over using act()

When you use React Testing Library you cannot avoid using `act()` as it is used in many of the core functionality that you need to use. But overusing (e.g. wrapping everything in an unnecessary act()) can end up affecting how long your tests take to run.

## Tips/best practices

- remember to always use the `act()` imported from `@testing-library/react`, not the one imported from the `react` package.
- always use the async version - `await act(async () => ...)`
- don't wrap everything in `act()`. Try to use it as infrequently as possible, and wrap very small chunks (ideally just 1 line/function call)

## Debugging React Testing Library "act(...)" Warnings

If you get that warning about act, or some state change is not reflected in your tests, here are the steps I normally take to debug it:

First, find the code/function in your component that is triggering the warning:

- Add `.only` to one test: `test.only('my test', ...)` to find one test that has a `act()` warning
- Add early `return` statements after each step to narrow down where the warning occurs
  - Can't find it? Put `return` right after `render()`
  - If warning appears: the component has automatic state updates (likely async)

Now you know where / what is causing it, use the following tips & ideas to fix the issue:

### Wrap manual state changes from your tests in act()

In your test, wrap any of your code that triggers state changes in act:

```
await act(async () => {
  
});
```

### Wait for (or findBy...) DOM updates

In your test, use the `.findBy...()` (or `waitFor()`) functions to wait until an assertion passes. This uses `act()` internally, so should make the warning go away.

```
await screen.findByText('expected text');
await waitFor(() => expect(someMockFunction).toHaveBeenCalled());
```

## Still stuck?

- **Missing `await`**? Add `await` before any `act()` calls
- **Double wrapping**? Check you're not wrapping `act()` inside another `act()`
- **Third-party components**? Dropdowns, modals often cause issues
- **Test cleanup**? Check `beforeEach`/`afterEach` hooks clear everything
- **useEffect cleanup**? Check the cleanup function (returned in the useEffect) in components
- **End-of-test flush**? Add `await act(() => {})` at test end to make sure act() runs when any state changes at the end of the test

## How to fix `Warning: The current testing environment is not configured to support act(...)` warning in test terminal output?

This error comes up because when you call `act()`, it will check that `global.IS_REACT_ACT_ENVIRONMENT` is equal to `true`

If you use React Testing Library (which I highly recommend you do - this entire site HowToTestFrontend.com is assuming you use it), then you shouldn't have to set this

But if you do, in your Vitest or Jest setup file, ensure you set:

```
global.IS_REACT_ACT_ENVIRONMENT = true;
```
