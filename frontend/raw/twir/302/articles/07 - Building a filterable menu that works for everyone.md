---
type: twir-item
issue: 302
item: 7
item_type: item
date: 2026-10-21
source: https://base-ui.com/blog/building-a-filterable-menu
tags:
  - "Navigation"
status: auto
quality: keep
---

[[2026-10-21-TWIR-302|Index]]

# Item 7: Building a filterable menu that works for everyone

Source: [https://base-ui.com/blog/building-a-filterable-menu](https://base-ui.com/blog/building-a-filterable-menu)

Summary:
This article explores the accessibility and interaction challenges of building a filterable menu in React, as implemented in Base UI. It discusses why common patterns like comboboxes and aria-autocomplete were not suitable, and how the team settled on a dialog-based approach to balance keyboard navigation, screen reader support, and usability. The post provides detailed reasoning and API examples for creating accessible, filterable menus.

Key takeaways:
- Filtering a menu impacts keyboard, screen reader, and interaction patterns.
- Combobox and aria-autocomplete patterns were rejected due to mismatched user expectations.
- Dialog-based approach with proper ARIA roles provides better accessibility and usability.
- Implementation supports intuitive navigation for both sighted and screen reader users.

Recommendation:
Read fully (if you build accessible menus or care about UI accessibility)

Why it matters:
if you build accessible menus or care about UI accessibility

Content:
# Building a filterable menu that works for everyone

On the surface, filtering a menu seems relatively simple to demonstrate. Add a text field, compare its value with each item’s label, and hide the items that don’t match. But making it work well with a keyboard, a screen reader, or a submenu requires a little more attention to detail.

While building filtering for Base UI, we found that adding an input affected almost every part of the interaction. Keys that normally navigate a menu also edit text. Moving focus between items can interrupt typing. Even the way a screen reader announces the popup changes what someone expects to find inside it.

In this post, we’ll look at some of those details and how they shaped the API we ended up with:

Before choosing a pattern, we needed to think through the interaction carefully. Imagine an “Actions” menu containing Rename, Duplicate, and Delete. A user can browse the actions normally, or type “dup” to narrow the menu to Duplicate. They can then activate it with the keyboard, mouse, or assistive technology.

We started with the keyboard. How should it work? From the input, a user should be able to press `↓` to highlight a match, use the arrow keys to explore the others, and press `Enter` to run an action. If an item opens a submenu, they should be able to enter it and return with the arrow keys, without the input swallowing those keys. After highlighting an action, they should still be able to keep typing, edit their query, or clear it and browse again, without first moving focus back to the input.

That interaction sounds familiar.

A combobox lets users type and explore matching choices with the arrow keys. To decide whether that pattern was right for our filterable menu, we needed to look at what the role tells users to expect.

ARIA [roles and attributes](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Techniques) communicate affordances. They help users understand what they can do with a control. For example, when a screen reader announces [a button](https://www.w3.org/WAI/ARIA/apg/patterns/button/#keyboardinteraction), someone familiar with buttons knows they can press `Enter` or `Space` to activate it. With [a combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/#keyboardinteraction), they know they can use the arrow keys to explore choices and select a value for the control, without leaving the control.

These interactions become familiar through use. Once someone has learned how a button or combobox works, they can reuse that knowledge in an application they’ve never used before. And we can avoid cluttering our interfaces with verbose labels and descriptions, which would quickly become tedious to hear again and again.

So why does that matter for our menu? Because that convenience relies on us delivering the behavior the role suggests. The APG calls this [“a role is a promise”](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/#principle-1-a-role-is-a-promise), and unfortunately, a combobox would break that promise if we used it here.

For example, choosing France in a country combobox should supply a value for the country field, but choosing Duplicate in our menu runs a command. We aren’t completing the search field with the word “Duplicate”. So, while both controls need to support typing and arrow keys, what the user chooses has a different purpose.

Another way we might try to communicate that familiar arrow-key interaction is to add `aria-autocomplete` to the input. Like combobox, this could suggest that users can explore suggestions with the arrow keys.

But `aria-autocomplete` also describes suggestions that complete the input’s value, and each of its values sets its own expectations:

These lead users to expect a suggestions popup that can expand and collapse, but our input doesn’t open a popup. The menu is already visible alongside the input, and typing updates which actions are visible, so adding `aria-haspopup` would describe an interaction the field doesn’t provide.

Using `Esc` illustrates why that could be confusing. In the [autocomplete and combobox patterns](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-list/), `Esc` dismisses the input’s popup and returns focus to the input. Someone expecting that behavior could try to exit our suggestions and continue filtering in the input, but that would close the menu popup, removing the input with it.

So, `aria-autocomplete` was off the table too. We’re filtering commands, and we want the announced control to match the interaction we provide.

We decided to use a dialog containing a search field and a menu. The search field filters the actions, and each action keeps its menu semantics. We put `aria-haspopup="dialog"` on the menu trigger so it announces the type of popup it actually opens. This affordance implies ahead of time that there is more than just the “Actions” to explore.

Inside, the dialog affordance helps communicate to screen reader users that they’ve entered a context they can explore with their usual navigation keys. If you haven’t used a screen reader before, here are the defaults for three common desktop screen readers:

VoiceOver goes even further and announces that the dialog contains two items. It doesn’t say what they are, but the count reinforces that there’s more to explore. In our case, those two items are the input and the menu.

button

“Actions”

aria-haspopup="dialog"

searchbox

“Filter actions”

aria-activedescendant

button (clear)

Not tabbable

Accessibility structure of a filterable menu.

The roles were settled, but the harder part was making a single text field feel natural whether someone is typing, browsing, or switching between the two.

A search field above a menu may look familiar enough that a sighted keyboard user tries `↓` to reach the results, so we support that interaction. Browser focus stays in the input, while `aria-activedescendant` identifies the highlighted item.

But screen reader users start somewhere else. Because `aria-activedescendant` identifies the highlighted item, their virtual cursor lands in the menu first, not the field. The surrounding [dialog](https://www.w3.org/TR/wai-aria-1.2/#dialog) tells them there’s more to explore than the menu, so they can move their virtual cursor out of it with their usual navigation keys and find the field. A field labeled “Filter actions” then tells them what they can search.

Once there though, hearing “search box” doesn’t make them aware of the arrow-key shortcut. We give the input the [searchbox role](https://www.w3.org/TR/wai-aria-1.2/#searchbox), which identifies a field for entering search criteria. It doesn’t communicate the combobox convention of using arrow keys to explore choices. Screen reader users can still use those keys, but we don’t depend on them discovering it.

Those who do discover the arrow-key behavior need a way to and from the input. As they arrow through the actions, their virtual cursor moves with the highlighted item, and a highlighted menu item doesn’t communicate that they can continue typing. For this reason, we decided that pressing `↓` on the last item or `↑` on the first should return the highlight to the field, so they can refine their query.

Sighted keyboard users never leave the field, but that arrow-key behavior of looping back to the input could feel invisible to them. Pressing `↓` on the last menu item might seem to do nothing, especially if the user expects navigation to loop back to the first item. So, we added `data-highlighted` to `Menu.Input` so applications can show where that step actually took them. Moving the visual highlight to the input shows that the user is back at the field and can continue filtering.

Another thing to consider is that the same key can mean different things depending on the context you’re in. In an ordinary menu, `Home` and `End` follow the familiar [menu keyboard conventions](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/#keyboardinteraction) of moving to the first or last item. In a text field, they move the caret to the beginning or end of the text.

Browser focus stays in our input while users navigate the menu though, so focus alone can’t tell us which behavior to use.

When the input is empty and a menu item is highlighted, `Home` and `End` move to the first or last item. When the highlight returns to the input, they move the caret, and `data-highlighted` shows the user is editing the field.

When the input has a value, those keys move the caret regardless of whether a menu item is highlighted, because entering a query signals the user’s intent to search.

Try it below. This is a small sketch of the behavior rather than Base UI itself.

Input
:   empty

Home / End
:   move caret

Highlighted
:   input

Last key
:   —

With the input empty, press `↓`, then `Home` or `End`.

Type "de", highlight a match, and try again to move the caret.

`Enter` runs the highlighted action.

Simplified for illustration; the real component also handles groups, submenus, and IME
composition.

With submenus, we also need to decide when the input should receive focus. We want users to be able to start navigating and filtering as soon as they enter a submenu, but opening it doesn’t always mean they’ve decided to enter it.

With the keyboard, the intent is clear. Pressing `→` on a highlighted submenu trigger asks to enter that submenu, so we focus its input immediately and the user can start typing a query or use the arrow keys straight away.

With keyboard we can easily infer the intent of the user and focus the input accordingly.

Hovering over a trigger isn’t as clear-cut. The pointer might simply pass over it while the user is still navigating the parent menu, so we show the submenu but leave focus where it is. Once the pointer moves into the submenu itself, that signals intent, so we focus its input and the user can start typing without another click. This lets users preview a submenu without it stealing their next keystroke.

For hover, we defer focus on the submenu input until the intent is clear.

In an ordinary menu, arrow keys move through the actions, while `Tab` moves to the next part of the page and closes the menu. We purposefully don’t trap focus inside the menu so that screen reader users on touch devices can also move their virtual cursor out of the menu to leave.

We could have added a hidden dismiss button for touch screen reader users, but it would need a label in the application’s language. Asking developers to provide that label through a prop or hidden part would make the exit depend on configuration that’s easy to skip because the hidden button’s purpose isn’t obvious. Letting users navigate past the menu instead keeps the exit available without extra setup.

Why does this matter for filterable menus? Our first version put `Menu.Clear` in the tab order, which seemed fine until we tried leaving the menu and had to press `Tab` twice. So, we removed that extra stop. Clear remains available to pointer users, and keyboard and screen reader users can delete the input text directly. This keeps the learned way to leave a menu consistent across filterable and non-filterable menus.

An input using `type="search"` already provides search box semantics, but some browsers also give it a built-in clear button. Replacing that button with our own can mean first removing it with browser-specific CSS, such as the [`::-webkit-search-cancel-button`](https://github.com/WebKit/WebKit/blob/main/Source/WebCore/css/html.css).

We use a text input with `role="searchbox"` instead, a combination [permitted by ARIA in HTML](https://www.w3.org/TR/html-aria/#el-input). It keeps native text editing and exposes the field as a search box, without adding the browser’s search-specific controls. Applications can then add `Menu.Clear` and style it like any other Base UI part, so the clear button becomes something developers choose to include rather than something they first have to undo.

Revisiting Menu testing with screen readers for filterables also uncovered bugs in Menu and shared popup code that affected every menu (filterable or not). We fixed them separately so everyone benefits.

1. **Double announcements in VoiceOver.** A menu group could announce its name twice. The group was named by `Menu.GroupLabel`, but the same label appeared as another stop for the virtual cursor. With the new dialog affordance, a custom scrollbar could also be counted as something to explore, even though a screen reader user could not reach it. The [accessibility-tree fix](https://github.com/mui/base-ui/pull/5598) removed the redundant stops while keeping the group named and the content scrollable.
2. **Getting lost on the way out.** `Shift`+`Tab` out of an open menu trigger could drop focus onto the page body. A [shared focus-guard fix](https://github.com/mui/base-ui/pull/5733) corrected that path. On iPhone VoiceOver, returning from a submenu to its trigger left the submenu open, so moving forward entered it again instead of reaching the next item in the parent menu. [Closing the submenu on that focus return](https://github.com/mui/base-ui/pull/5793) restored the path forward.
3. **Stuck in TalkBack.** Moving TalkBack’s virtual cursor doesn’t move DOM focus, so a user could open a submenu but could not close it. [Pressing an open submenu trigger now toggles the submenu](https://github.com/mui/base-ui/pull/5824), letting the user continue through the parent menu.

These were mostly bugs in ordinary menu interactions rather than requirements unique to filtering, but finding them while building the new behavior gave us a chance to improve both.

Adding an input might seem like a small change, but the decisions we’ve worked through affect the whole interaction. The trigger needs to announce a dialog, highlighting an action needs to work alongside text editing, entering a submenu needs to put the user in the right place to continue, and the popup needs to let screen reader users explore both the input and the menu.

An input part can’t tell the whole menu to do all that, so we needed a way to opt the menu into that behavior as a whole. That’s the purpose of `Menu.FilterProvider`:

We explored [adding filtering directly to Menu](https://github.com/mui/base-ui/pull/5429) and [introducing a separate FilterMenu component](https://github.com/mui/base-ui/pull/5490), but the provider won for three reasons:

- Applications keep their existing menu parts and styles.
- The trigger can announce a dialog before the input mounts.
- Apps that don’t filter don’t ship filtering code.

Inside the popup, `Menu.List` contains the actions, with `Menu.Input` alongside it, and the same provider can wrap `Menu.SubmenuRoot` when a submenu needs filtering.

Testing the ways people would actually use the menu took us well beyond filtering the items. Each interaction gave us another part of the design to consider, from the role announced when the popup opens to where focus goes when the pointer enters a submenu.

The input is the most visible addition. But getting the interactions and accessibility right is what lets someone open the menu, find an action, and carry on without having to figure out how it all works.

---

Try it yourself in the [Menu docs](/react/components/menu#filtering)
