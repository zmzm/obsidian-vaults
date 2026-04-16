---
type: twir-item
issue: 265
item: 19
item_type: item
date: 2026-01-21
source: https://base-ui.com/react/utils/use-render#migrating-from-radix-ui
tags:
status: auto
quality: review
---

[[2026-01-21-TWIR-265|Index]]

# Item 19: Base UI composition pattern differs from Radix UI

Source: [https://base-ui.com/react/utils/use-render#migrating-from-radix-ui](https://base-ui.com/react/utils/use-render#migrating-from-radix-ui)

Summary:
Summary not available.

Key takeaways:
- No key takeaways extracted.

Recommendation:
Summary sufficient

Content:
# useRender · Base UI

# useRender

The `useRender` hook lets you build custom components that provide a `render` prop to override the default rendered element.

A `render` prop for a custom Text component lets consumers use it to replace the default rendered `p` element with a different tag or component.

Text component rendered as a paragraph tag

**Text component rendered as a strong tag**

The callback version of the `render` prop enables more control of how props are spread, and also passes the internal `state` of a component.

The `mergeProps` function merges two or more sets of React props together. It safely merges three types of props:

1. Event handlers, so that all are invoked
2. `className` strings
3. `style` properties

`mergeProps` merges objects from left to right, so that subsequent objects’ properties in the arguments overwrite previous ones. Merging props is useful when creating custom components, as well as inside the callback version of the `render` prop for any Base UI component.

Using mergeProps in the render callback

Copy

When building custom components, you often need to control a ref internally while still letting external consumers pass their own—merging refs lets both parties have access to the underlying DOM element. The `ref` option in `useRender` enables this, which holds an array of refs to be merged together.

In React 19, `React.forwardRef()` is not needed when building primitive components, as the external ref prop is already contained inside `props`. Your internal ref can be passed to `ref` to be merged with `props.ref`:

In older versions of React, you need to use `React.forwardRef()` and add the forwarded ref to the `ref` array along with your own internal ref.

The [examples](#examples) above assume React 19, and should be modified to use `React.forwardRef()` to support React 18 and 17.

To type props, there are two interfaces:

- `useRender.ComponentProps` for a component’s external (public) props. It types the `render` prop and HTML attributes.
- `useRender.ElementProps` for the element’s internal (private) props. It types HTML attributes alone.

Radix UI uses an `asChild` prop, while Base UI uses a `render` prop. Learn more about how composition works in Base UI in the [composition guide](/react/handbook/composition).

In Radix UI, the `Slot` component lets you implement an `asChild` prop.

Radix UI Slot component

Copy

In Base UI, `useRender` lets you implement a `render` prop. The example below is the equivalent implementation to the Radix example above.

The `render` prop is primarily designed for composing event handlers and behavioral props. In most cases it should render the same tag as the default element.

Using `render` for polymorphism (rendering a different tag) requires more care, as some default props may not be valid on the new element. For example, `type="button"` is only valid on a `<button>`. Since the component can’t know what element `render` will produce at render time and before hydration, props like these need an explicit signal. This is why Base UI’s [Button](/react/components/button) provides a `nativeButton` prop to control which defaults are applied.

#### Parameters

`useRender.Parameters`

Parameter properties table`render``ReactElement | function`

Description
:   The React element or a function that returns one to override the default element.

`ref``Union`

Description
:   The ref to apply to the rendered element.

`state``TState`

Description
:   The state of the component, passed as the second argument to the `render` callback.
    State properties are automatically converted to data-\* attributes.

`stateAttributesMapping``StateAttributesMapping<TState>`

Description
:   Custom mapping for converting state properties to data-\* attributes.

`props``Record<string, unknown>`

Description
:   Props to be spread on the rendered element.
    They are merged with the internal props of the component, so that event handlers
    are merged, `className` strings and `style` properties are joined, while other external props overwrite the
    internal ones.

`enabled``boolean`

Description
:   If `false`, the hook will skip most of its internal logic and return `null`.
    This is useful for rendering a component conditionally.

`defaultTagName``Union`

Description
:   The default tag name to use for the rendered element when `render` is not provided.

#### useRender.ComponentProps[Hide](#)

#### useRender.ElementProps[Hide](#)

#### useRender.ReturnValue[Hide](#)

#### UseRenderComponentProps[Hide](#)

#### UseRenderElementProps[Hide](#)

Notes:
No digest block matched; created from issue link fallback.
