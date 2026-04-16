---
type: twir-item
issue: 262
item: 12
item_type: item
date: 2025-12-10
source: https://shramko.dev/blog/react-elements-children
tags:
  - "Re-Renders"
status: auto
quality: keep
---

[[2025-12-10-TWIR-262|Index]]

# Item 12: React Elements, Children as Props, and Re-Renders

Source: [https://shramko.dev/blog/react-elements-children](https://shramko.dev/blog/react-elements-children)

Summary:
The article explains how passing React elements as children props can prevent unnecessary re-renders, especially when state must live at the top level. By extracting stateful logic into a wrapper component and passing expensive children as props, React can avoid re-rendering those children during frequent state updates. The post clarifies the distinction between components and elements, and how React’s reconciliation leverages element reference equality.

Key takeaways:
- Passing elements as children props decouples stateful logic from expensive subtrees.
- React skips reconciling children if their element references remain unchanged.
- This pattern is useful when state cannot be moved down but performance is critical.
- Understanding the difference between components and elements is key for advanced optimization.

Recommendation:
Read fully (read fully if optimizing render performance in complex layouts)

Why it matters:
read fully if optimizing render performance in complex layouts

Content:
# React Elements, Children as Props, and Re-Renders

Welcome back, fellow React enthusiasts!

Previously, we discussed [re-renders and the "moving state down" pattern](/blog/react-rerender). That technique works
great when you can isolate stateful logic into a leaf component. But sometimes the architecture doesn't allow for that.

What do you do when state *must* live at the top, yet you don't want to tank performance?

Let's explore a real scenario. You're building a dashboard with a resizable sidebar. The sidebar width is controlled
by dragging a handle, and the entire content area needs to respond to this width change.

## The Challenge

Here's what you need:

- A draggable divider that updates the sidebar width in real-time.
- The sidebar wraps around `ExpensiveChart`, `DataGrid`, and `AnalyticsPanel`.
- As you drag, the layout adjusts smoothly.

The naive approach puts the drag state at the top level (or perhaps tries to hide it in
a [custom hook](/blog/react-hooks-pitfalls), which doesn't change anything):

```
const Dashboard = () => {
  const [sidebarWidth, setSidebarWidth] = useState(300);

  const handleDrag = (e) => {
    setSidebarWidth(e.clientX);
  };

  return (
    <div className="dashboard-layout">
      <div className="sidebar" style={{ width: sidebarWidth }}>
        <DragHandle onDrag={handleDrag} />

        {}
        <ExpensiveChart />
        <DataGrid />
        <AnalyticsPanel />
      </div>
      <MainContent />
    </div>
  );
};
```

![React DevTools screenshot titled 'The Problem: Re-rendering Everything' showing App component with scrollPosition state triggering re-renders on BunchOfStuff and VerySlowComponent children](/_next/image?url=%2Fstatic%2Fimages%2Felements.png&w=3840&q=75)

This implementation will stutter badly. Every mouse movement fires a state update, causing `Dashboard` to re-render.
When `Dashboard` re-renders, so does everything nested inside it. The "moving state down" approach fails here because
the `sidebar` div needs to wrap the expensive components while also knowing about the width.

You might reach for `React.memo`, but there's a cleaner compositional approach that leverages how React handles
elements.

## The Fix: Composition with Children

Extract the resize logic into a dedicated component that accepts its contents as children:

```
const ResizableSidebar = ({ children }) => {
  const [width, setWidth] = useState(300);

  const handleDrag = (e) => {
    setWidth(e.clientX);
  };

  return (
    <div className="sidebar" style={{ width }}>
      <DragHandle onDrag={handleDrag} />
      {children}
    </div>
  );
};
```

Refactor `Dashboard` to use this wrapper:

```
const Dashboard = () => {
  return (
    <div className="dashboard-layout">
      <ResizableSidebar>
        {}
        <ExpensiveChart />
        <DataGrid />
        <AnalyticsPanel />
      </ResizableSidebar>
      <MainContent />
    </div>
  );
};
```

Now dragging is fluid. The expensive components stay untouched even though they visually live inside a component that
updates dozens of times per second.

## The Mechanics Behind It

This behavior stems from the distinction between **Components** and **Elements**.

A **Component** is the function itself (`Dashboard`, `ResizableSidebar`).

An **Element** is the object produced when JSX executes (`{ type: ExpensiveChart, props: {...} }`).

Here's what happens step by step:

1. `Dashboard` renders once and creates Element objects for `<ExpensiveChart />`, `<DataGrid />`, and
   `<AnalyticsPanel />`.
2. These Element objects get passed into `ResizableSidebar` through the `children` prop.
3. User starts dragging. `ResizableSidebar` updates its `width` state repeatedly.
4. `ResizableSidebar` re-executes, returning a new sidebar div with the updated width.
5. React checks the `children` prop. Has the reference changed?
6. No. `Dashboard` never re-rendered, so `children` points to the exact same objects in memory.
7. React skips reconciling that entire subtree.

The key insight: **React compares element references, not their visual position in the tree.**

## Understanding the JSX Transformation

Remember that `children` is an ordinary prop. The nested syntax is syntactic sugar.
Elements are [expressions](/blog/expressions-statements), so these two snippets produce identical results:

```
<Wrapper>
  <Content />
</Wrapper>
```

```
<Wrapper children={<Content />} />
```

You could use any prop name: `content`, `slot`, `body`. The optimization works as long as the Element is created in a
scope that doesn't re-render and then passed to the stateful component.

## Wrapping Up

The [previous article](/blog/react-rerender#moving-state-down) showed how pushing state into a child component
prevents unnecessary re-renders. This article demonstrated the inverse: lifting static UI *out* of the stateful
component by passing it as props.

Both patterns serve the same purpose: decoupling what changes from what stays stable.
