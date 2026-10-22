---
type: "twir-recovery"
issue: 302
item: 8
source: "https://mattrothenberg.com/notes/pure-ui-agentic-era/"
final_url: "https://mattrothenberg.com/notes/pure-ui-agentic-era/"
retrieved: "2026-10-22T11:30:13+00:00"
original_note: "frontend/raw/twir/302/articles/08 - Pure UI in the Agentic Era.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/08 - Pure UI in the Agentic Era|Pure UI in the Agentic Era]]

# Pure UI in the Agentic Era

Guillermo Rauch’s [Pure UI](https://rauchg.com/2015/pure-ui) gave me a useful rule as a front-end developer: where possible, a UI should be “a pure function of application state.”

I stopped thinking of UI as event handlers that change the DOM and started thinking of it as a snapshot of data at a point in time.

In this contrived example, each account sees a slightly different version of the screen. Anyone who changes it, person or agent, needs to know which of those states the change touches.

Storybook already works this way: choose inputs, render a component. Front-end teams have previewed and tested states like this for years. I keep coming back to it because agents now write most of the UI code I review.

This matters most in products with lots of conditional UI: free and enterprise accounts, owner and viewer roles, overdue invoices, feature flags, regional rules, and one-off customer exceptions. Each is an input to the otherwise simple equation of `ui = fn(state)`.

Most teams, human or agent, do not have a complete picture of the states their UI can occupy. Nobody is clicking through every relevant combination by hand. As agents take on more implementation work, how do we know they considered the states a change might affect?

## The state is scattered

In a real product, the state that determines a screen rarely arrives as one neat object. Role might come from a query, plan from context, and billing status from a layout that conditionally renders a banner.

When I build a feature, I first want to know what states its screen can occupy. In a large React app, the component alone rarely tells you. You have to inspect hooks, providers, and parent layouts, then hold the result in your head.

<FunctionsPage functions={functions} />

RoleuseSession()AccountProvider, five layers upPlanusePlan()a context set at the app rootBilling<BillingGate>a layout wrapper, four layers upLive logs betaisOn("live\_logs")a global flag client

Each highlighted value comes from a different place in the tree above this component.

## Looks good on my machine

I ask an agent to add a delete action to each row in the functions table. I forget to say that people with the viewer role should not see it. A few minutes later, the agent reports back:

Add a delete action to each row of the functions table.

EditedFunctionsTable.tsx+41

Editedapi/functions.ts+12

Rannpm run typecheckpassed

Openedlocalhost:5173/functions

Done. Each row in the functions table now has a Delete action that removes the function and refreshes the list. I checked it in the browser and it renders correctly.

Four steps, all green, and one screenshot from whatever account the dev server was already signed in as.

The feature is done for the account the agent tested, anyway. My local dev server was authenticated against production with the owner role. Here is the same page with the viewer role:

What the agent saw· Owner

The same page as a Viewer

Same page, same data, different role. The header calls out that it's 'View only', but the table still shows a 'Delete' button.

The example is contrived, but I have seen versions of it in nearly every React codebase I have worked in. The header knows the role because it displays a “View only” badge. The table does not: no role check had ever lived there, and my prompt only asked the agent to change that component.

You can ask an agent to check more. It can drive a browser, sign in as other accounts, and compare screenshots if those accounts and their data exist. Without careful direction, though, it may declare success after checking only the state it happened to start in.

People miss these cases too. The difference is that an agent can report “done” with the same confidence whether it checked one state or sixteen, while each generated change gets less review time.

## Tests only cover chosen states

Tests help, but they only cover cases someone chose to write down. If a component reads state through hooks, each case may require mocking those hooks before it can render. When its relevant display state is explicit input instead, a test can render selected combinations directly:

Dashboard.test.tsxVitest Browser

```
1import { expect, test } from "vitest";2import { render } from "vitest-browser-react";3import { Dashboard, type DashState } from "./Dashboard";45test("renders a Free viewer", async () => {6  const state: DashState = {7    role: "Viewer",8    plan: "Free",9    billing: "Paid",10    beta: "Off",11  };1213  const { getByText } = await render(14    <Dashboard s={state} uid="viewer-free" />,15  );1617  await expect.element(getByText("View only")).toBeInTheDocument();18  await expect.element(getByText("Pro only")).toBeInTheDocument();19});
```

PASS2 DOM assertionsViewer · Free · Paid · beta off

PASS`getByText("View only")`found

PASS`getByText("Pro only")`found

Rendered screens

Viewer · Free

Paid · beta off

Owner · Pro

Paid · beta on

Viewer · Past due

Past due · beta off

Viewer · Beta on

Paid · beta on

## Pick a state, any state

Guillermo rendered application states as “artboards” side by side:

> If you think up and hand out 20 distinct states in which your application can behave, then you should be able to clearly see them rendered on a screen as HTML.

When screen output is close to `fn(state)`, you can render a chosen set of input combinations and inspect what a change does before merging.

The dashboard at the top takes four inputs: role, plan, billing status, and the live-logs beta flag. In this demo, each has two values, yielding sixteen screens. The grid below renders them all with the agent’s version of the page. The earlier agent checked only the teal-ringed screen.

What the agent checkedEvery state

The agent's version of the page called sixteen times. The agent checked the first screen. The eight amber screens are viewers. The header says View only, and every row has a Delete button anyway. Click any screen to see it at full size.

The grid exposes the earlier bug. The eight amber-ringed screens use the viewer role. Compare their headers with their tables.

For this screen, rendering sixteen states is cheaper than setting up sixteen accounts, and a grid of visual outputs is faster to scan than a diff.

## Make the relevant state explicit

Storybook and Playwright are useful here. They work alongside Pure UI. Storybook gives you a place to render chosen component states. Playwright checks that those states are reachable in the real app. Both depend on somebody deciding which role, billing, flag, and data combinations matter.

Pure UI does not make that decision for you, either. It gives you a cleaner place to record it. When a screen’s display-relevant state is explicit input, its API becomes a working list of what can change the output. That makes those states easier to turn into stories, tests, or a visual grid.

The refactor is to move display-relevant state to an explicit page or view boundary, then pass it as arguments to the pieces you want to exercise. Across a page, that can look like this:

Each component reaches outThe page is handed its world

worldfunctionsPageAnswers(world) → answersFunctionsPage{ functions }PageHeader{ title }UsageCard{ usage }FunctionsTable{ functions }BulkBar{ selected }FunctionRow{ fn }RowMenu{ fn }who you areplanbillingflagsnetwork

The tree declares seven props. The dashed lines are the 15 reads it doesn't declare.

## Ask where your confidence comes from

Guillermo wanted designers to stop drawing only the happy screen. A mockup filled with Lorem Ipsum has the same problem: it presents one idealized state instead of the conditions people actually encounter. An agent that checks one account has the same blind spot.

Before you merge, ask what the agent actually saw. One account is one path, not the whole screen. Looking at the states that matter will not catch everything, but it gives you more confidence in what you ship, and more chances to catch the awkward stuff before a customer does.
