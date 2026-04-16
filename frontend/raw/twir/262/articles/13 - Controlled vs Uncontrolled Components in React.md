---
type: twir-item
issue: 262
item: 13
item_type: item
date: 2025-12-10
source: https://certificates.dev/blog/controlled-vs-uncontrolled-components-in-react
tags:
status: auto
quality: keep
---

[[2025-12-10-TWIR-262|Index]]

# Item 13: Controlled vs Uncontrolled Components in React

Source: [https://certificates.dev/blog/controlled-vs-uncontrolled-components-in-react](https://certificates.dev/blog/controlled-vs-uncontrolled-components-in-react)

Summary:
This article clarifies the concepts of controlled and uncontrolled components, both for form inputs and general component design. Controlled components have their state managed externally (via props), while uncontrolled components manage state internally. The post provides practical examples, explains trade-offs, and shows how to support both modes for flexible APIs.

Key takeaways:
- Controlled components: parent manages state via props; uncontrolled: component manages its own state.
- For forms, controlled means using value/onChange; uncontrolled uses defaultValue and DOM state.
- Custom components can support both modes by checking for the presence of control props.
- Pattern choice affects testability, predictability, and API design.

Recommendation:
Read fully (read fully if you need a refresher or are designing reusable components)

Why it matters:
read fully if you need a refresher or are designing reusable components

Content:
# Controlled vs Uncontrolled Components in React

Understanding controlled vs uncontrolled in React is about one question: who owns the state? Learn both meanings for form inputs and component design patterns.

The terms "controlled" and "uncontrolled" appear frequently in React documentation, but they can be confusing because they seem to mean different things in different contexts. In reality, they're asking the same question: **who owns the state—the parent or the component itself?**

This article clarifies the terminology and helps you recognize the pattern in everyday React code.

## The Core Question: Who Owns the State?

Both uses of "controlled" and "uncontrolled" share the same underlying concept:

- **Controlled**: State is owned externally and passed in via props
- **Uncontrolled**: State is owned internally by the component itself

For form inputs, "internal state" means the DOM manages the value. For custom components, "internal state" typically means React's `useState`. But it's the same question: does the parent control the state, or does the component manage it internally?

This distinction matters because it determines where the "source of truth" lives and who can change it.

## Form Inputs: The Common Introduction

The terms are commonly introduced with form inputs, where the question is whether the parent component controls the input's value via props, or the input manages its own value internally via the DOM.

A **controlled input** has its value managed by the parent through React state:

```
      function SearchForm() {
  const [query, setQuery] = useState('');

  function handleSubmit(event) {
    event.preventDefault();
    console.log(query);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  );
}
```

React fully controls this input's value. The `value` prop sets what's displayed, and `onChange` updates the state. Anything that updates `query`—whether typing, a "Clear" button, or selecting a suggestion—will update the input.

This means `value` and `onChange` [must work together](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable). If you pass `value` without `onChange`, it will be impossible to type into the input—React will revert every keystroke back to the value you specified.

An **uncontrolled input** manages its value internally via the DOM:

```
      function SearchForm() {
  function handleSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    console.log(formData.get('query'));
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="query" defaultValue="" />
      <button type="submit">Search</button>
    </form>
  );
}
```

React doesn't know about this input's value—it doesn't set or update it, and doesn't know when it changes. The `defaultValue` prop only sets the initial value; after that, the DOM owns the state.

## Components: Props vs Internal State

Beyond forms, "controlled" and "uncontrolled" describe a general component design pattern. The same question applies: does the parent own the state via props, or does the component manage it internally?

Consider a simple `Toggle` component:

```
      function Toggle({ label }) {
  const [isOn, setIsOn] = useState(false);

  return (
    <button onClick={() => setIsOn(!isOn)}>
      {label}: {isOn ? 'ON' : 'OFF'}
    </button>
  );
}
```

This component uses `useState`, so React is managing the state. But that doesn't make it "controlled" in the component design sense. The parent component has no way to read or set the toggle's value:

```
      function App() {
  return <Toggle label="Dark Mode" />;
}
```

Since the parent can't influence the state, this `Toggle` is **uncontrolled**—it manages its own internal state, and the parent just renders it.

### Making Components Controlled

To make `Toggle` controlled, we move the state to the parent and pass it via props:

```
      function Toggle({ label, isOn, onToggle }) {
  return (
    <button onClick={onToggle}>
      {label}: {isOn ? 'ON' : 'OFF'}
    </button>
  );
}

function App() {
  const [darkMode, setDarkMode] = useState(false);

  return (
    <>
      <Toggle
        label="Dark Mode"
        isOn={darkMode}
        onToggle={() => setDarkMode(!darkMode)}
      />
      <p>Theme: {darkMode ? 'dark' : 'light'}</p>
    </>
  );
}
```

Now `App` controls the toggle's value. It can read the state to update the theme, reset it, or coordinate multiple toggles. The component renders from props instead of internal state.

Notice how this mirrors native inputs: controlled inputs use `value` and `onChange`, and our controlled `Toggle` uses a similar pattern with `isOn` and `onToggle`. Modeling custom components after native HTML elements makes their APIs intuitive and predictable.

### Supporting Both Modes

Some components support both controlled and uncontrolled usage, just like native `<input>` elements. For our `Toggle`, it could look like this:

```
      function Toggle({ label, isOn, onToggle, defaultOn = false }) {
  const [internalOn, setInternalOn] = useState(defaultOn);

  const isControlled = isOn !== undefined;
  const on = isControlled ? isOn : internalOn;

  function handleToggle() {
    if (isControlled) {
      onToggle?.();
    } else {
      setInternalOn(!internalOn);
    }
  }

  return (
    <button onClick={handleToggle}>
      {label}: {on ? 'ON' : 'OFF'}
    </button>
  );
}
```

This allows flexible usage:

```
      // Uncontrolled - Toggle manages its own state
<Toggle label="Notifications" defaultOn={true} />

// Controlled - Parent manages the state
<Toggle label="Dark Mode" isOn={darkMode} onToggle={() => setDarkMode(!darkMode)} />
```

The key is checking `isOn !== undefined` to determine the mode. When controlled, the component uses the prop and delegates changes to the parent via `onToggle`. When uncontrolled, it manages its own state internally.

One important rule: a component shouldn't switch between controlled and uncontrolled modes during its lifetime. If `isOn` starts as `undefined` and later becomes a value (or vice versa), the behavior becomes unpredictable. You may have seen the warning ["A component is changing an uncontrolled input to be controlled"](https://react.dev/reference/react-dom/components/input#im-getting-an-error-a-component-is-changing-an-uncontrolled-input-to-be-controlled)—this is React telling you that an input switched modes, and custom components should follow the same principle.

Many UI libraries use this pattern. However, supporting both modes adds complexity. For simpler components, it's often better to choose one approach.

## Real-World Examples

The controlled/uncontrolled pattern appears throughout React UI libraries:

**Tabs**: An uncontrolled tabs component manages which tab is active internally. A controlled version accepts `activeTab` and `onTabChange` props, letting the parent programmatically change tabs or sync with URL state.

**Modals**: An uncontrolled modal might have an internal `isOpen` state and expose a `trigger` element. A controlled modal accepts `isOpen` and `onClose` props, letting the parent control visibility based on application state.

**Accordions**: An uncontrolled accordion lets each panel manage its own open/closed state. A controlled version accepts `expandedPanels` and `onChange` props, enabling "single panel open" behavior that requires coordination.

**Date Pickers**: An uncontrolled date picker manages selection internally. A controlled version accepts `selectedDate` and `onChange`, letting the parent validate dates, sync with other fields, or implement date range constraints.

The key insight is that controlled components enable coordination. When multiple components need to stay in sync, or when parents need to implement complex behavior, controlled components make this possible.

## Trade-offs and Considerations

The choice between controlled and uncontrolled comes down to one question: does the parent need to know about or influence the state?

### Form Inputs

For forms, uncontrolled inputs are often simpler. You let the DOM handle the state and read values on submit using `FormData`. This approach works well with React's modern form features like the `<form>` action prop, `useFormStatus`, and `useActionState`.

Controlled inputs become valuable when you need the value while the user is typing—for real-time validation, transforming input (like formatting phone numbers), or coordinating multiple fields. The trade-off is that controlled inputs re-render on every keystroke, while uncontrolled inputs avoid this.

Form libraries like [React Hook Form](https://react-hook-form.com/) navigate this trade-off by using uncontrolled inputs with refs by default for performance, while still providing validation and error handling. They support controlled inputs via a `Controller` component when the parent needs access to intermediate values.

### Custom Components

For custom components, the question is whether the component should work independently or be coordinated by its parent.

An uncontrolled component manages its own state and works out of the box—the parent just renders it. This is simpler when the state is an implementation detail the parent doesn't care about.

A controlled component receives its state via props and notifies the parent of changes. This enables coordination: the parent can sync multiple instances, implement complex behavior like "only one open at a time," or integrate the state with the rest of the application. The trade-off is more wiring in the parent component.

When building reusable component libraries, supporting both modes gives consumers flexibility—but for application code, picking one approach keeps things simpler.

## Conclusion

The terms "controlled" and "uncontrolled" always ask the same question: who owns the state? Whether it's a form input (where internal state lives in the DOM) or a custom component (where internal state lives in `useState`), the choice is between props from the parent and internal state managed by the component.

The key insight is that using `useState` doesn't make a component "controlled." From the parent's view, a component is uncontrolled if the parent can't influence its state. Understanding this helps you design component APIs that give parents the right level of control for their needs.

---

**Sources:**
