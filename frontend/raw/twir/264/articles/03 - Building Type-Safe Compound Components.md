---
type: twir-item
issue: 264
item: 3
item_type: item
date: 2026-01-14
source: https://tkdodo.eu/blog/building-type-safe-compound-components
tags:
  - "Type-Safe"
status: auto
quality: keep
---

[[2026-01-14-TWIR-264|Index]]

# Item 3: Building Type-Safe Compound Components

Source: [https://tkdodo.eu/blog/building-type-safe-compound-components](https://tkdodo.eu/blog/building-type-safe-compound-components)

Summary:
The article explores the design pattern of compound components in React, focusing on achieving type safety, especially when building component libraries. It discusses the strengths of compound components—flexibility and explicitness in markup—while noting that they’re not always the best fit, particularly when a fixed layout suffices. The author critiques common examples and hints at type-level limitations with children in React, suggesting that true type safety is not about restricting children but about other aspects of the API.

Key takeaways:
- Compound components are valuable for flexible composition in component libraries.
- They’re not always appropriate; sometimes prop-based APIs are simpler and clearer.
- Type safety in compound components is challenging, especially regarding restricting children types.
- The article provides practical insights but also sets realistic expectations about current type system limitations.

Recommendation:
Read fully (for those building or maintaining component libraries)

Why it matters:
for those building or maintaining component libraries

Content:
# Building Type-Safe Compound Components

   Photo by [Jeremy Thomas](https://unsplash.com/@jeremythomasphoto)

I think compound components are a really good design-pattern when building component libraries. They give consumers flexibility in how components are composed, without forcing every variation into a single, prop-heavy API. Additionally, they make relationships between components explicit in the markup.

This doesn’t mean that compound components are *always* a good fit. Sometimes, using `props` is just better.

A common example we’ll see regarding compound components is a `Select` with `Options`, likely because that’s also how it works in HTML.

```
function ThemeSwitcher({ value, onChange }: Props) {

<Select value={value} onChange={onChange}>

<Option value="system">🤖</Option>

<Option value="light">☀️</Option>

<Option value="dark">🌑</Option>
```

There are a couple of reasons why I think this example is not ideal at showing what compound components are good for.

Compound components excel at allowing users to layout `children` however they want. For `Selects`, we likely don’t need that. The `options` go into a menu, and we want to show each option one after the other. This is exactly why lots of people want to [limit what you can pass (opens in a new window)](https://github.com/microsoft/TypeScript/issues/21699) into `children` on type-level - like only allowing `Option` to be passed into `Select`.

This is not only [impossible (opens in a new window)](https://www.totaltypescript.com/type-safe-children-in-react-and-typescript) as of now (the issue is open since 2018), it’s also undesirable. I know you were hoping that I would tell you how to make compound components type-safe in this article, and I will - it’s just not about `children` at all. My take is that if you want to limit `children` to a specific type, compound components are the wrong abstraction.

Compound components are really good when your content is mostly static. The above example has three hardcoded options, so it qualifies, right?

In reality, we likely won’t have `Selects` with just three options, as the content will mostly likely come from an API call with a dynamic resultset. Also, most design guides will tell us that we [shouldn’t use a Select for less than five options (opens in a new window)](https://baymard.com/blog/drop-down-usability), as hiding a small number of choices in a dropdown adds unnecessary clicks and cognitive load.

In fact, at Adverity, we started out with a compound component `Select` and then had to write this mapping code for most of our usages:

```
function UserSelect({ value, onChange }: Props) {

const userQuery = useSuspenseQuery(userOptions)

<Select value={value} onChange={onChange}>

{userQuery.data.map((option) => (

<Option value={option.value}>{option.label}</Option>
```

At that point, we just switched to exposing a `Select` that used `props` instead of `children`:

```
function UserSelect({ value, onChange }: Props) {

const userQuery = useSuspenseQuery(userOptions)
```

This not only allowed us to get rid of the tedious mapping we had to do everywhere, it also gave us the type safety we wanted, as there were no `children` that we needed to restrict. Also, `Select` can easily be made generic to make sure `value`, `onChange` and `options` all get the same type:

```
type SelectValue = string | number

type SelectOption<T> = { value: T; label: string }

type SelectProps<T extends SelectValue> = {

onChange: (value: T) => void

options: ReadonlyArray<SelectOption<T>>
```

A `ModalDialog` component is another example where we’d rather not give our users the full power of compound components. I mean, it doesn’t make sense to render the `DialogFooter` above the `DialogHeader`. We also don’t want anyone to accidentally leave out the `DialogBackdrop` or create different spacings between `DialogBody` and `DialogFooter`. In cases where consistency and order is important, slots are usually a better abstraction:

```
function ModalDialog({ header, body, footer }: Props) {

<DialogHeader>{header}</DialogHeader>

<DialogBody>{body}</DialogBody>

<DialogFooter>{footer}</DialogFooter>

return <ModalDialog header="Hello" body="World" />
```

They still allow some form of flexibility by injecting arbitrary React components into specific positions while making sure no one has to copy-paste that boilerplate everywhere. It is of course great to have these `Dialog` primitives inside a design-system, I would just not expose them for consumers.

---

So those are two indicators - fixed layout and mostly dynamic content - that make me question if we really want a compound component. So when is it a really good fit then? And what does it have to do with type safety?

A good use-case that would likely benefit from dynamically laid out children with mostly fixed elements is a `<ButtonGroup>`, a `<TabBar>` or a `<RadioGroup>`:

```
function ThemeSwitcher({ value, onChange }: Props) {

<RadioGroup value={value} onChange={onChange}>

<Flex direction={['row', 'column']} gap="sm">

<RadioGroupItem value="system">🤖</RadioGroupItem>

<RadioGroupItem value="light">☀️</RadioGroupItem>

<RadioGroupItem value="dark">🌑</RadioGroupItem>
```

The main difference to `Select` is that we explicitly want to have `children` that aren’t of type `RadioGroupItem`. Being able to layout them how we want, maybe even with additional help texts, is essential. Sure, we might have some instances where our `RadioGroup` needs dynamic options as well, but in that case, creating a loop like I’ve shown before isn’t the end of the world.

That still leaves the problem of type safety, as `value` passed to `ThemeSwitcher` hopefully isn’t just a string - it’s likely a string literal:

```
type ThemeValue = 'system' | 'light' | 'dark'
```

The `value` and `onChange` props can be tied to `ThemeValue` simply by making `RadioGroup` generic like I’ve shown before, but what about `RadioGroupItem` ? How do we make sure that the `value` passed to each one of them can be statically analyzed?

We can of course also make `RadioGroupItem` generic. The problem with that approach is that types from the `RadioGroup` wouldn’t be automatically available to the items, because JSX children don’t “inherit” type parameters from the parent component. So even if `RadioGroup` is perfectly typed and infers `<ThemeValue>`, we would still need to parameterize each `RadioGroupItem`:

```
type ThemeValue = 'system' | 'light' | 'dark'

onChange: (value: ThemeValue) => void

function ThemeSwitcher({ value, onChange }: Props) {

<RadioGroup value={value} onChange={onChange}>

<Flex direction={['row', 'column']} gap="sm">

<RadioGroupItem<ThemeValue> value="system">🤖</RadioGroupItem>

<RadioGroupItem<ThemeValue> value="light">☀️</RadioGroupItem>

<RadioGroupItem<ThemeValue> value="dark">🌑</RadioGroupItem>
```

That’s not a great API, because every manual type annotation is easily forgotten. If you know me, you know that I like my types fully inferred whenever possible. The best way to do this for compound components is by *not* exposing those components directly, but by only giving your users a method to invoke.

### Component Factory Pattern

Not sure if this is the correct name for this pattern, but I think it’s good enough to get the concept across. Basically, we can’t fully get rid of the manual type annotation, but we can try to hide it and make it explicit. Instead of exposing `RadioGroup` and `RadioGroupItem`, we only export a function called `createRadioGroup` that should be called once with a type parameter. This function will then return the statically typed `RadioGroup` and its `RadioGroupItem` with types that are tied together:

```
export const createRadioGroup = <T extends GroupValue = never>(): {

RadioGroup: (props: RadioGroupProps<T>) => ReactElement

RadioGroupItem: (props: Item<T>) => ReactElement

} => ({ RadioGroup, RadioGroupItem })
```

This doesn’t do anything at runtime, except wrapping our internal `RadioGroup` and `RadioGroupItem` into an object. But on type-level, it ties the type parameters together. And the fact that we default our generic to `never` means users will have to pass it in order to be able to do anything meaningful with the result, allowing us to use it like this:

```
type ThemeValue = 'system' | 'light' | 'dark'

onChange: (value: ThemeValue) => void

const Theme = createRadioGroup<ThemeValue>()

function ThemeSwitcher({ value, onChange }: Props) {

<Theme.RadioGroup value={value} onChange={onChange}>

<Flex direction={['row', 'column']} gap="sm">

<Theme.RadioGroupItem value="system">🤖</Theme.RadioGroupItem>

<Theme.RadioGroupItem value="light">☀️</Theme.RadioGroupItem>

<Theme.RadioGroupItem value="dark">🌑</Theme.RadioGroupItem>

<Theme.RadioGroupItem value="wrong">🚨</Theme.RadioGroupItem>

Error ts(2322)  ― Type '"wrong"' is not assignable to type 'ThemeValue'.
```

Of course, this version isn’t bullet proof. We can still create a differently typed `RadioGroup` and pass those items to our `Theme.RadioGroup`, but this is far less likely to happen by accident.

All in all, this approach preserves the flexibility that makes compound components great while adding strong type guarantees. The only real cost is that consumers don’t import the components directly, but instead create a typed instance of the component family via a function call. I think that’s a worthwhile tradeoff and the best way to make a compound component as type-safe as possible for the users of your design-system.

---

That’s it for today. Feel free to reach out to me on [bluesky (opens in a new window)](https://bsky.app/profile/tkdodo.eu)
if you have any questions, or just leave a comment below. ⬇️

Like the monospace font in the code blocks?

Check out [monolisa.dev](https://www.monolisa.dev/?ref=dominik)

 [![Bytes - the JavaScript Newsletter that doesn't suck](/.netlify/images?w=4096&h=256&fit=cover&url=%2Fblog%2F_astro%2Fbytes.PgTxoh9S.jpg)](https://bytes.dev/?r=dom)
