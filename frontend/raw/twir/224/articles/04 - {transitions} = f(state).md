---
type: twir-item
issue: 224
item: 4
item_type: item
date: 2025-03-05
source: https://jordaneldredge.com/blog/transitions-f-of-state/
tags:
  - "StateMachine"
  - "Expo"
status: auto
quality: keep
---

[[2025-03-05-TWIR-224|Index]]

# Item 4: {transitions} = f(state)

Source: [https://jordaneldredge.com/blog/transitions-f-of-state/](https://jordaneldredge.com/blog/transitions-f-of-state/)

Summary:
This article proposes thinking of React’s component tree as a state machine, where the UI and valid transitions are both functions of state. It highlights how asynchronous and concurrent updates can expose invalid transitions, and discusses strategies for guarding against them, such as optimistic updates or marking state as pending. The model helps clarify when synchronous updates are needed to prevent users from triggering invalid actions.

Key takeaways:
- React’s UI and allowed transitions can be modeled as functions of state.
- Asynchronous and concurrent updates require explicit handling to avoid invalid user actions.
- Optimistic or pending state updates help maintain correct transition guards.
- React’s concurrent features (e.g., useTransition) provide built-in support for managing pending states.

Recommendation:
Read fully (read fully if interested in state machines or advanced state management patterns)

Why it matters:
read fully if interested in state machines or advanced state management patterns

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
