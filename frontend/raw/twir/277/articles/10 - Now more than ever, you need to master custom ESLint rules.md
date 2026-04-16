---
type: twir-item
issue: 277
item: 10
item_type: item
date: 2026-04-15
source: https://neciudan.dev/master-eslint-rules
tags:
  - "ESLint"
status: auto
quality: keep
---

[[2026-04-15-TWIR-277|Index]]

# Item 10: Now more than ever, you need to master custom ESLint rules

Source: [https://neciudan.dev/master-eslint-rules](https://neciudan.dev/master-eslint-rules)

Summary:
The author shares their experience writing a custom ESLint rule to enforce best practices around useEffect, highlighting the power of AST-based linting. The post explains how ESLint parses JavaScript into an Abstract Syntax Tree (AST), how rules traverse and match nodes, and provides a simplified example of a no-console rule. Tools like AST Explorer are recommended for understanding and developing custom rules. The piece emphasizes that custom linting can automate code review feedback and deepen understanding of JavaScript internals.

Key takeaways:
- ESLint rules operate on ASTs, enabling precise, automated code checks.
- Custom rules can enforce team conventions and reduce manual review cycles.
- AST Explorer is a valuable tool for developing and testing custom rules.
- Understanding ASTs deepens knowledge of JavaScript tooling and code structure.

Recommendation:
Read fully (read fully if interested in custom linting or advanced JavaScript tooling)

Why it matters:
read fully if interested in custom linting or advanced JavaScript tooling

Content:
# Now more then ever, you need to master custom ESLint rules

Three days ago, I had a problem.

I posted about `useEffect` on LinkedIn (again), and the comments split into two camps (again): people shouting that I shouldn’t use `useEffect` in the code snippet, and people arguing that my usage was correct. Someone linked my [useEffect article](https://neciudan.dev/you-dont-need-an-effect). Someone else linked the React docs. A third person said “just write an ESLint rule for it.”

That last comment stuck with me.

My useEffect article kept generating the same PR comments across our team’s codebase: someone would write `useEffect(() => setFiltered(data.filter(...)), [data])`, and three reviewers would pile on with “you don’t need an effect here.” The author would push back. A thread with seven comments about a three-line change.

I wanted to stop having that conversation manually.

So I wrote a custom ESLint rule to catch it. And what I found during those three days taught me more about how JavaScript works than any article I’ve read in the last five years.

## Your code is a tree

When you write JavaScript, you see text. When ESLint sees your JavaScript, it sees a tree.

```
const name = "Dan";
```

You see a variable declaration. ESLint’s parser (Espree) converts that into something like this:

```
{
  "type": "VariableDeclaration",  // the whole "const name = ..." line
  "kind": "const",                // const vs let vs var
  "declarations": [
    {
      "type": "VariableDeclarator", // the "name = 'Dan'" part
      "id": {
        "type": "Identifier",       // the variable name
        "name": "name"
      },
      "init": {
        "type": "Literal",          // the value being assigned
        "value": "Dan"
      }
    }
  ]
}
```

That’s an Abstract Syntax Tree. AST for short.

Every piece of your code gets a node: the `const` keyword, the variable name, the string value. All nested inside each other in a tree structure that describes exactly what your code means, without caring about whitespace, semicolons, or formatting.

The “abstract” part means it strips away the stuff that doesn’t matter for understanding the code’s structure. Whether you write `const name = "Dan"` or `const name = "Dan"`, the AST is identical.

This is the representation that every tool in the JavaScript ecosystem works with. Babel transforms your code through it. Prettier reformats code by reading the tree and printing it back out. TypeScript has its own AST for type-checking. And ESLint walks the tree to lint it.

## How ESLint actually works

The whole process is three steps.

First, ESLint parses your file into an AST. It walks through the source text and builds the tree.

Second, it traverses the tree. It visits every node, one by one, depth-first. Think of it like reading a table of contents: it goes all the way into a section’s subsections before moving to the next section.

Each node gets visited twice: once on the way down (entering) and once on the way back up (exiting). Rules can listen to either phase. Most rules only care about the enter phase, but you can register an exit listener by appending `:exit` to the node type, like `"FunctionExpression:exit"`. You’d use exit listeners when you need to collect information from child nodes before making a decision at the parent level.

Third, for each node it visits, it checks if any rules care about that node type. If a rule registered a listener for `VariableDeclaration`, ESLint calls that listener function and hands it the node.

That’s it. That’s the entire architecture.

An ESLint rule is a JavaScript object with a `create` function that returns an object. Its keys are node types from the AST, and the values are callback functions that ESLint invokes when it encounters a matching node.

Here’s a simplified version of the built-in `no-console` rule.

Before reading it, think about what `console.log("hello")` looks like as a tree. It’s a function call (`CallExpression`), but what’s being called? It’s not just `log`. It’s the `log` property accessed on the `console` object. That property access is a `MemberExpression`.

The `callee` is the “thing being called” in any function call node.

```
module.exports = {
  meta: {
    type: "suggestion",
    docs: {
      description: "Disallow console.log",
    },
  },
  create(context) {
    return {
      // ESLint calls this function for every function call in your code
      CallExpression(node) {
        if (
          // Is the thing being called a property access (like obj.method)?
          node.callee.type === "MemberExpression" &&
          // Is the object "console"?
          node.callee.object.name === "console" &&
          // Is the property "log"?
          node.callee.property.name === "log"
        ) {
          context.report({
            node,
            message: "Unexpected console.log",
          });
        }
      },
    };
  },
};
```

`meta` describes the rule. `create` does the work. `context.report()` surfaces the warning in your editor.

That’s a simplified `no-console` rule. One of the most common rules in every JavaScript project, and at its core it’s just a function that checks if a `CallExpression` node is calling `console.log`.

## AST Explorer changed everything

The moment this clicked for me was when I opened [AST Explorer](https://astexplorer.net).

Paste any JavaScript on the left. The AST appears on the right. Click on a piece of code, and the corresponding node highlights in the tree. Click on a node in the tree, and the corresponding code highlights on the left.

Set the parser to `espree` (ESLint’s default) and toggle the Transform to “ESLint v4” at the top. (The “v4” label is just what AST Explorer calls its ESLint transform; the rule format hasn’t changed, and the rules you write there work with any ESLint version.) Now you get four panels: code top-left, AST top-right, your rule bottom-left, and the rule’s output bottom-right. You can write a rule and see it flag code in real time, without leaving the browser.

I spent an embarrassing amount of time just pasting random code and clicking around the tree. My first attempt at finding `console.log` in the AST, I kept clicking on `console` expecting a `CallExpression`. Nope. `console` is just an `Identifier`. The call is the whole `console.log(...)` expression. The dot access is a `MemberExpression` inside it. I had to click on the parentheses to find the actual `CallExpression`.

Once that clicked, I started seeing the patterns. `ArrowFunctionExpression` for arrow functions. `CallExpression` for function calls. `MemberExpression` for property access like `object.property`. `Identifier` for variable names.

Once you see your code as a tree, writing a rule becomes a pattern-matching problem. You know what the bad code looks like. You paste it in AST Explorer. You find the node types. You write a function that matches that pattern. Done.

(If you just want to use AST knowledge without writing a full rule, skip ahead to “The five-minute version.” You can flag patterns with a single line of config.)

## Building the real rule

Back to my actual problem. I wanted to catch this:

```
useEffect(() => {
  setFiltered(data.filter(item => item.active));
}, [data]);
```

A derived state antipattern. Derived state is a value you can compute from data you already have.

Here, `filtered` is just `data` with a `.filter()` applied. There’s no reason to store it in a separate state variable and sync it with an effect. You can compute it directly during render: `const filtered = data.filter(item => item.active)`. The effect version causes an extra render cycle for no reason.

I pasted the code into AST Explorer and clicked on `useEffect`. Here’s what I saw, piece by piece:

`useEffect(...)` is a `CallExpression`. The `callee` (the thing being called) is an `Identifier` with `name: "useEffect"`. The first argument is the arrow function, an `ArrowFunctionExpression`.

Inside that arrow function, `setFiltered(data.filter(...))` is a line of code. As a standalone line, the AST wraps it in an `ExpressionStatement`. That’s the AST’s way of saying “this expression is being used as a statement.” The actual function call to `setFiltered` lives inside it as a `CallExpression`.

I’ll be honest: it took me a while to understand why `setFiltered(...)` was both an `ExpressionStatement` and a `CallExpression`. They’re nested. The statement wraps the expression. Once I saw it in the tree, it made sense. Before that, I kept trying to match `CallExpression` and wondering why the AST had an extra layer.

So the detection logic is: find `CallExpression` nodes where the callee is `useEffect`, look at the first argument’s body, and check if every statement in that body is a call to a state setter (a function whose name matches the `set*` pattern from `useState`).

Here’s the simplified version. I’ll show it in two parts because each part does a different job.

First, the rule’s metadata and the visitor that learns setter names:

```
// eslint-rules/no-derived-state-in-effect.js
module.exports = {
  meta: {
    type: "suggestion",
    docs: {
      description: "Disallow setting derived state inside useEffect",
    },
    messages: {
      noDerivedState:
        "This effect only sets state derived from '{{ dep }}'. " +
        "Compute the value during render instead, or use useMemo if expensive.",
    },
    schema: [],
  },
  create(context) {
    // Collect setter names from useState calls
    const setterNames = new Set();

    return {
      // Track useState calls to learn setter names
      VariableDeclarator(node) {
        if (
          node.init?.type === "CallExpression" &&
          node.init.callee?.name === "useState" &&
          node.id?.type === "ArrayPattern" &&
          node.id.elements.length === 2
        ) {
          const setter = node.id.elements[1];
          if (setter?.type === "Identifier") {
            setterNames.add(setter.name);
          }
        }
      },
```

The `messages` object defines reusable warning messages. Instead of writing `message: "some text"` in every `context.report()` call, you reference a message by its key using `messageId: "noDerivedState"`. The `{{ dep }}` is ESLint’s placeholder syntax; it gets replaced by whatever you pass in the `data` object of `context.report()`.

The `VariableDeclarator` visitor fires for every variable declaration. It checks: is this a `useState` call? Is it destructured as an array with two elements, like `const [value, setValue] = useState()`? If so, it remembers the setter name (`setValue`, `setFiltered`, etc.) in a `Set`.

Now the second part, the visitor that checks `useEffect` calls:

```
      // Check useEffect calls
      CallExpression(node) {
        if (node.callee?.name !== "useEffect") return;

        const callback = node.arguments[0];
        if (!callback) return;

        const body =
          callback.body?.type === "BlockStatement"
            ? callback.body.body
            : null;
        if (!body) return;

        // Check if EVERY statement is just a setter call
        const allSetters = body.every(
          (stmt) =>
            stmt.type === "ExpressionStatement" &&
            stmt.expression.type === "CallExpression" &&
            stmt.expression.callee?.type === "Identifier" &&
            setterNames.has(stmt.expression.callee.name)
        );

        if (allSetters && body.length > 0) {
          const deps = node.arguments[1];
          const depName =
            deps?.type === "ArrayExpression" && deps.elements.length > 0
              ? context.sourceCode.getText(deps.elements[0])
              : "dependencies";

          context.report({
            node,
            messageId: "noDerivedState",
            data: { dep: depName },
          });
        }
      },
    };
  },
};
```

This visitor ignores everything that isn’t a `useEffect` call. When it finds one, it grabs the callback function (the first argument) and looks at the statements inside its body. For each statement, it checks: is this just a call to one of the setter functions we collected earlier? If *every* statement is a setter call and nothing else, the effect is only computing derived state. Flag it.

This doesn’t catch everything. The rule is intentionally narrow: it flags the obvious cases with zero false positives rather than trying to be clever about edge cases.

For example, it won’t catch this:

```
useEffect(() => {
  if (data) {
    setFiltered(data.filter(item => item.active));
  }
}, [data]);
```

That’s an `IfStatement` wrapping the setter call, not a bare `ExpressionStatement`, so the `body.every(...)` check skips it.

An effect might also call a setter alongside other work, or inside a `.then()` callback. Plugins like `eslint-plugin-react-you-might-not-need-an-effect` handle these cases because they do deeper analysis of the call graph.

My rule catches the low-hanging fruit. Honestly, that’s fine. The first version of any custom rule should be narrow. You can always widen it later when you see what it misses.

## Turning it into a local plugin

A custom rule needs to live inside a plugin for ESLint to load it. But you don’t need to publish anything to npm.

With ESLint’s flat config, you don’t even need a separate plugin file. You can define a virtual plugin directly in `eslint.config.js` by importing the rule file:

```
my-project/
├── eslint-rules/
│   └── no-derived-state-in-effect.js
├── eslint.config.js
└── src/
```

```
// eslint.config.js
import { defineConfig } from "eslint/config";
import noDerivedStateInEffect from "./eslint-rules/no-derived-state-in-effect.js";

export default defineConfig([
  {
    plugins: {
      local: {
        rules: {
          "no-derived-state-in-effect": noDerivedStateInEffect,
        },
      },
    },
    rules: {
      "local/no-derived-state-in-effect": "warn",
    },
  },
]);
```

One rule file, one config entry. You don’t need `package.json` symlinks or a separate plugin index file. The `local` namespace can be any name you want; it’s just a prefix for referencing the rules.

One thing you’ll notice: the rule file uses `module.exports` (CommonJS) while the config file uses `import` (ESM). That’s normal. ESLint’s flat config expects ESM, but rule files work with either format. If your project has `"type": "module"` in `package.json`, you can use `export default` in your rule files too.

If you have multiple custom rules and want to organize them, you can create an `index.js` that exports them all and import that instead:

```
// eslint-rules/index.js
import noDerivedStateInEffect from "./no-derived-state-in-effect.js";
import noAnonymousEffects from "./no-anonymous-effects.js";

export default {
  rules: {
    "no-derived-state-in-effect": noDerivedStateInEffect,
    "no-anonymous-effects": noAnonymousEffects,
  },
};
```

```
// eslint.config.js
import { defineConfig } from "eslint/config";
import local from "./eslint-rules/index.js";

export default defineConfig([
  {
    plugins: { local },
    rules: {
      "local/no-derived-state-in-effect": "warn",
      "local/no-anonymous-effects": "warn",
    },
  },
]);
```

## Testing the rule

ESLint ships a `RuleTester` utility that makes this trivial. You give it arrays of valid and invalid code, and it verifies the rule behaves correctly:

```
const { RuleTester } = require("eslint");
const rule = require("./no-derived-state-in-effect");

const ruleTester = new RuleTester({
  languageOptions: {
    ecmaVersion: 2022,
    sourceType: "module",
    parserOptions: {
      ecmaFeatures: { jsx: true },
    },
  },
});

ruleTester.run("no-derived-state-in-effect", rule, {
  valid: [
    // Legitimate effect: syncing with external system
    `
    const [data, setData] = useState([]);
    useEffect(() => {
      const ws = new WebSocket(url);
      ws.onmessage = (e) => setData(JSON.parse(e.data));
      return () => ws.close();
    }, [url]);
    `,
    // Derived value computed inline (no effect)
    `
    const [todos, setTodos] = useState([]);
    const filtered = todos.filter(t => t.active);
    `,
  ],
  invalid: [
    {
      code: `
      const [data, setData] = useState([]);
      const [filtered, setFiltered] = useState([]);
      useEffect(() => {
        setFiltered(data.filter(item => item.active));
      }, [data]);
      `,
      errors: [{ messageId: "noDerivedState" }],
    },
  ],
});
```

The `RuleTester` works with any test runner. Jest, Vitest, Node’s built-in test runner. It’s just assertions. Save the code above as `no-derived-state-in-effect.test.js` next to your rule file and run it with `node no-derived-state-in-effect.test.js`. If the tests pass, you’ll see no output. If a test fails, you’ll get a clear error showing which code was expected to pass or fail and why.

## Adding auto-fix

Static detection is useful, but auto-fix is where things get interesting.

ESLint rules can include a `fix` function inside `context.report()`. The function receives a `fixer` object with methods like `replaceText`, `insertTextBefore`, and `remove`. ESLint runs the fixer, applies the change to the source code, and re-lints the result to confirm no new violations were introduced.

For the derived state rule, auto-fix gets complicated. You’d need to remove the `useState` for the derived value, remove the entire `useEffect`, and insert a `const` declaration with the derived computation. That’s a lot of source manipulation, and getting the variable scoping right requires more AST analysis than the detection itself.

I didn’t add auto-fix to this rule. Some rules are better as warnings than as auto-fixers.

For simpler patterns, auto-fix is a single function. Say you’re writing a rule that catches `==` and wants to replace it with `===`. The `==` comparison is a `BinaryExpression` node with `node.left` (the thing on the left), `node.right` (the thing on the right), and `node.operator` (the `"=="` string).

Here’s a detail the auto-fix API cares about: `fixer.replaceText` doesn’t accept raw strings as the first argument. It accepts AST nodes or tokens. Tokens are the individual characters and symbols in your source code (like `==`, `{`, `const`, `"hello"`), while nodes are the structural groupings (like `VariableDeclaration`, `BinaryExpression`). You need to find the actual `==` token in the source code and replace that:

```
context.report({
  node,
  message: "Use === instead of ==",
  fix(fixer) {
    // Find the operator token between left and right operands
    const sourceCode = context.sourceCode;
    const operatorToken = sourceCode.getTokenAfter(
      node.left,
      token => token.value === node.operator
    );
    return fixer.replaceText(operatorToken, "===");
  },
});
```

The ESLint docs have a full list of fixer methods. The one rule is that a fix must produce valid code and must not change the code’s behavior. If you can’t guarantee both, skip the fix and let the developer handle it.

## Rules worth writing

After building the derived state rule, I kept going. Three more rules came out of patterns I kept seeing in code reviews.

**No anonymous effects.** This one ties directly into my [naming useEffect functions article](https://neciudan.dev/name-your-effects). The detection is clean: find `CallExpression` nodes where the callee is `useEffect` and the first argument is an `ArrowFunctionExpression`. Arrow functions can’t have names in the call site. Flag them.

```
CallExpression(node) {
  if (node.callee?.name !== "useEffect") return;
  const callback = node.arguments[0];
  if (callback?.type === "ArrowFunctionExpression") {
    context.report({
      node: callback,
      message:
        "Name your useEffect callback. Use a function expression: " +
        "useEffect(function descriptiveName() { ... })",
    });
  }
}
```

The fix is either an inline named function expression (`useEffect(function connectToWebSocket() { ... })`) or passing a separately declared function by reference (`useEffect(connectToWebSocket, [roomId])`). Both give you a name in stack traces and React DevTools.

**No setState in submit handlers without form reset.** A pattern I kept catching: the form’s `onSubmit` handler calls `mutation.mutate()` but never resets the form fields. The rule checks if a function whose name contains “submit” (case-insensitive) calls a state setter but never calls a form reset setter.

The core detection logic looks like this:

```
// Inside the create function
FunctionDeclaration(node) {
  if (!node.id?.name.toLowerCase().includes("submit")) return;

  const body = node.body.body;
  const calledFunctions = body
    .filter(s => s.type === "ExpressionStatement" &&
                 s.expression.type === "CallExpression")
    .map(s => s.expression.callee?.name || "");

  const callsSetters = calledFunctions.some(n => setterNames.has(n));
  const callsReset = calledFunctions.some(n =>
    n.toLowerCase().includes("reset")
  );

  if (callsSetters && !callsReset) {
    context.report({
      node,
      message: "Submit handler sets state but never resets the form.",
    });
  }
}
```

It’s not a perfect heuristic. But it catches the most common case. The first time it flags a forgotten form reset in a PR, it pays for itself.

**No effect chains.** Detect when an effect’s dependency array contains a state variable that is set by another effect in the same component. This one requires two passes: first collect all the state setters and which effects call them, then check if any effect depends on state that another effect sets. It’s the most complex rule of the four, but it catches the cascading effect pattern from my useEffect article.

## The plugin that already exists

After building my rules, I found `eslint-plugin-react-you-might-not-need-an-effect` by Nick van Dyke. It covers most of the patterns from the React docs page: derived state, event handlers disguised as effects, chained state updates, passing data to parents, and more.

It has nine rules, each targeting a specific antipattern. The analysis is deeper than what I built; it traces state variables through their upstream sources and considers the dependency array when deciding if logic is redundant.

Install it and extend the recommended config:

```
// eslint.config.js
import { defineConfig } from "eslint/config";
import reactYouMightNotNeedAnEffect from
  "eslint-plugin-react-you-might-not-need-an-effect";

export default defineConfig([
  reactYouMightNotNeedAnEffect.configs.recommended,
]);
```

React’s own `eslint-plugin-react-hooks` also has a `set-state-in-effect` rule that flags synchronous `setState` calls inside effects.

Between the two, you cover most of the common misuses. My custom rules fill the gaps specific to our codebase.

## Why you should build one anyway

You might read this and think, “I’ll just install the existing plugin and call it done.”

Do that. But also try building one rule yourself.

In the LinkedIn comments on my original post, someone shared that they’d written ESLint rules to enforce unique `data-test-id` attributes across their Angular templates. Another person linked a set of rules built from their company’s entire JS handbook. A third shared a YouTube playlist about ASTs and the visitor pattern. The common thread: every person who’d built a custom rule said the same thing. It changed how they understood JavaScript.

The exercise of looking at your code through the AST changes how you think about code. You stop seeing text and start seeing structure. `const x = 1` and `let x = 1` are the same node type (`VariableDeclaration`) with a different `kind` property. `foo.bar()` is a `CallExpression` whose callee is a `MemberExpression`. Destructuring, optional chaining, and template literals all have their own node types with their own properties.

This matters beyond linting. Babel plugins use the same visitor pattern: walk AST nodes, transform them, output new code. Codemods do too. If you ever need to do a large-scale refactor across a codebase, tools like `jscodeshift` let you find patterns in the AST and replace them programmatically.

Story time: a team I worked with needed to rename a prop across 400 components. Find-and-replace would have caught most of them, but not the destructured ones, not the spread ones, not the ones aliased in intermediate variables. A codemod using `jscodeshift` walked the AST, found every `JSXAttribute` with the old name, renamed it, and handled the edge cases. The whole migration ran in under a minute. Doing it by hand would have taken a week.

## Teaching your AI assistant

If you’re using an AI coding assistant, custom ESLint rules are the most precise way to enforce patterns.

You can put instructions in a system prompt. You can add documentation to a `.cursorrules` file. But the AI might ignore them, or apply them inconsistently, or forget them after a long context window.

An ESLint rule runs after the AI writes its code. It flags the violation, the AI sees the red underline, and it fixes the code. The rule doesn’t forget after a long context window. It doesn’t decide “well, sometimes it’s fine.”

For patterns that are specific to your project, a custom local rule is more effective than any prompt engineering. The AI sees the lint error, fixes the code, and moves on. It never needs to understand *why* the pattern is wrong.

This also feeds the loop in the right direction. AI models are trained on open-source code. The more codebases have good lint rules enforcing good patterns, the more good patterns show up in training data. Your lint rule today improves the AI’s defaults tomorrow.

I’ve packaged the decision tree from my [useEffect article](https://neciudan.dev/you-dont-need-an-effect) as a Claude Code skill in the [react-tips-skill](https://github.com/Cst2989/react-tips-skill) plugin. The skill forces the AI to check each case before writing a `useEffect`. But a skill is a suggestion. A lint rule is an enforcement mechanism.

The two work together. The skill prevents the AI from writing unnecessary effects in the first place. The lint rule catches the ones that slip through, whether they’re written by the AI, by a teammate, or by you at 11pm when you just want the feature to work.

```
# For your AI rules file:

Before writing useEffect, answer:
Is this syncing with an external system?
If no, check: derived state? event handler? state reset? data fetch?

# For your ESLint config:

"local/no-derived-state-in-effect": "warn",
"local/no-anonymous-effects": "warn",
"react-you-might-not-need-an-effect/no-derived-state": "warn",
"react-you-might-not-need-an-effect/no-event-handler": "warn",
```

Soft guardrails plus hard guardrails. The AI learns from the skill. The linter catches what slips through. And the PR review stops being a debate about whether this particular effect is necessary.

## The five-minute version

If you want to try this right now without building a full plugin, ESLint has a built-in escape hatch: the `no-restricted-syntax` rule. It uses AST selectors (they work like CSS selectors but for code) to flag specific node patterns.

```
// eslint.config.js
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    rules: {
      "no-restricted-syntax": [
        "warn",
        {
          selector:
            "CallExpression[callee.name='useEffect'] > ArrowFunctionExpression",
          message:
            "Name your useEffect callback. Use a named function expression instead of an arrow function.",
        },
      ],
    },
  },
]);
```

One selector, no plugin, no custom rule file. The selector `CallExpression[callee.name='useEffect'] > ArrowFunctionExpression` matches any arrow function that’s a direct child of a `useEffect` call.

You can get surprisingly far with `no-restricted-syntax`. It supports descendant selectors, attribute matching, `:not()` pseudo-selectors, and regex patterns. For complex logic that requires tracking state across nodes, you need a real rule. For simple pattern matching, this is enough.

## Get started

Open [AST Explorer](https://astexplorer.net). Set the parser to `espree`. Paste a piece of code you wish you could lint. Click around the tree until you find the node types.

Write the `create` function. Return an object with visitor methods. Call `context.report()` when you find a match.

Wrap it in a local plugin. Add it to your config. Run ESLint.

That PR comment you keep writing? You just automated it. Go write a rule.

## References

⚡ LIVE · APRIL 27 – 30 · ONLY 3 SESSIONS LEFT

![](/images/lizard/lizard.png) 

🏆 SOLD OUT IN SINGAPORE · ATHENS · LONDON

### From Lizard to Wizard

4 hours. Algorithms, system design, security, observability, AI.  
The workshop that turns mid engineers into senior ones.

€250 4-HOUR INTENSIVE

 [Pick your date →](/lizard-to-wizard/signup) 

Spots are vanishing. Don't be the one who waited.

 ![](/images/lizard/wizard.png)

![Author](/images/logo.png)

### Discover more from The Neciu Dan Newsletter

A weekly column on Tech & Education, startup building and occasional hot takes.
