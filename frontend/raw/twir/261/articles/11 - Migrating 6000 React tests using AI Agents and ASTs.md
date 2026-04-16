---
type: twir-item
issue: 261
item: 11
item_type: item
date: 2025-12-03
source: https://eliocapella.com/blog/ai-library-migration-guide/
tags:
  - "6000"
  - "ASTs"
status: auto
quality: keep
---

[[2025-12-03-TWIR-261|Index]]

# Item 11: Migrating 6000 React tests using AI Agents and ASTs

Source: [https://eliocapella.com/blog/ai-library-migration-guide/](https://eliocapella.com/blog/ai-library-migration-guide/)

Summary:
A case study on migrating a large React codebase’s tests from Testing Library v13 to v14 using AI agents and AST-based codemods. The process involved preparing migration guides, running both package versions in parallel, automating code changes with jscodeshift, and validating each migration step with tests and coverage checks.

Key takeaways:
- Large-scale test migrations can be automated with codemods and AI assistance.
- Running multiple package versions in parallel eases incremental migration.
- Migration to v14 required significant code and timing behavior changes.
- Automated validation (linting, testing, coverage) is essential for reliability.

Recommendation:
Read fully (read fully if planning large-scale test migrations)

Why it matters:
read fully if planning large-scale test migrations

Content:
# Migrating 6000 React tests using AI Agents and ASTs

The internet is flooded with very impressive vibe-style coding demos, but
in my day-to-day job at
[Filestage](https://www.filestage.io) we rarely
start codebases from scratch and we have to deal with
**hundreds of thousands of lines of code** and their
dependencies.  
I set out to explore if AI could help migrate our
**970 test files** with over
**6000 test cases** in our frontend from React Testing
Library v13 to v14.
*How hard could it be...*

At first, I naively told
[Claude Code CLI](https://www.claude.com/product/claude-code)
to migrate our codebase to the new package version. It started working,
updated the package to the latest version, and then ran the tests. On
every test failure, it tried to debug and fix the test, but there were
*too many test failures*, so it started to
**spiral out of control**.

I quickly understood this was not going to work, so I decided to dig
deeper. I used the web version of Claude and using the research tool I
asked it to build a **migration guide** and best practices. I
read through this guide to learn about all the changes and
*oh boy there were a lot of them!*

The update to v14 **fundamentally changed** how you write
tests by making *all APIs asynchronous* and introducing a new setup
pattern. This means a lot of code changes, but the worst part is that the
**timing behaviors also changed**, which meant that many
tests will start failing, others will have less coverage, and will require
manual debugging to fix.

This update would require **thousands of changes** and would
require days even with AI, increasing the possibility for the team to
create new tests and create conflicts.  
To be able to split the change in multiple PRs I had to find a way to have
**both versions of the package running at the same time**,
luckily that is pretty easy with NPM:

```
{
  "devDependencies": {
    "@testing-library/user-event": "13.5.0",
    "@testing-library/user-event-new": "npm:@testing-library/user-event@14.5.2"
  }
}
```

So my first PR was ready, have both versions installed and the migration
guide in md format in our repo.

I decided to first focus on the easy part. I gave the migration guide to
Claude Code and told it to built a **codemod**. I used
[jscodeshift](https://jscodeshift.com/) which
parses the code into a
[AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
which is just nested object structure that you can manipulate, the tool
takes care of then getting that new AST and generating the output code.

![Sample of an AST structure in astexplorer.net](./ast-example.png)

Sample of an AST structure in
[astexplorer.net](https://astexplorer.net)

Great thing about jscodeshift is that you can
**easily write tests** for your codemod and use them to
**verify what the AI has done**. You have input and output
fixtures and it will run the codemod on them and compare them with the
expected output.

```
"use strict";

const path = require("path");
const { defineTest } = require("jscodeshift/dist/testUtils");

describe("migrate-to-userevent-v14 codemod", () => {
  for (const test of [
    "sample",
    /* ... */
  ]) {
    defineTest(
      path.resolve(__dirname, "codemods"),
      "migrate-to-userevent-v14",
      null,
      `migrate-to-userevent-v14/${test}`,
    );
  }
});
```

```
@@ -1,26 +1,33 @@
-import { render, screen } from "@testing-library/react";
-import userEvent from "@testing-library/user-event";
+import { screen } from "@testing-library/react";
+import { renderWithUserEvent } from "@shared/test/utils";

 import { Button } from "./Button";

 describe("Button", () => {
   it("should render button text", () => {
-    render(<Button>Click me</Button>);
+    renderWithUserEvent(<Button>Click me</Button>);
     expect(screen.getByText("Click me")).toBeInTheDocument();
   });

   it("should call onClick when clicked", async () => {
     const handleClick = jest.fn();
-    render(<Button onClick={handleClick}>Click me</Button>);
+
+    const {
+      userEvent
+    } = renderWithUserEvent(<Button onClick={handleClick}>Click me</Button>);

     await userEvent.click(screen.getByText("Click me"));
     expect(handleClick).toHaveBeenCalled();
   });

   it("should type text into input", async () => {
-    render(<input placeholder="Enter text" />);
+    const {
+      userEvent
+    } = renderWithUserEvent(<input placeholder="Enter text" />);
+
+    await userEvent.click(screen.getByPlaceholderText("Enter text"));

-    await userEvent.type(screen.getByPlaceholderText("Enter text"), "Hello");
+    await userEvent.keyboard("Hello");
     expect(screen.getByPlaceholderText("Enter text")).toHaveValue("Hello");
   });
 });
```

Diff of the sample input and output test fixtures

The second PR was ready, the first codemod iteration and its tests.

Now the fun part begins, I gave Claude Code this prompt to start
migrating:

```
We are migrating the frontend tests to the latest version of userevent testing library v14, the migration guide frontend/doc/user-event-testing-library-migration-guide.md.
We have created a codemod to help with the migration at frontend/codemods/migrate-to-userevent-v14.js.
We have created new render utility functions that return the userEvent instance at frontend/src/shared/test/utils.js.
Until the migration is done we have both user event versions installed, v13 as "@testing-library/user-event" and v14 as "user-event-new".

I want you to continue migrating the next 10 tests (`grep -rl 'from "@testing-library/user-event"' src | head -n 10`), for each test:
*Make sure to set your working path to the frontend dir so the commands run correctly.*
- Apply the codemod to the test file
- After migrating a test we need to execute `npm run validate:fix` to verify we didn't introduce linting issues in the file, fix introduced issues if any
- Then we have to execute `npm run test -- <test-file>` to verify the test is working, fix any issues if any
- Finally verify the coverage is still 100% then we can move to the next test file, fix any coverage issues if any, eg: `npm test -- PasswordField.test.jsx --coverage --collectCoverageFrom=src/supporting/components/PasswordField/PasswordField.jsx --reporter=json` then read the coverage report at frontend/jest-coverage/coverage-final.json

Improve the migration codemod if you find any patterns repeated in the codebase that are not being covered.
Improve the migration guide if you find any patterns repeated in the codebase that are not being covered.
```

This wasn't the first version of the prompt I started with a very basic
one and watched for the AI to fail and
**improved it iteratively**. At the beginning there were many
*edge cases* found, some of them could be fixed automatically by
improving the codemod but others required
**manual intervention** so the iterative learnings were
consolidated in the migration guide. The migration guide started with
**4532 words** and ended up with **7517**.
[Here is the resulting codemod](https://gist.github.com/eliOcs/61092b2f406f4ebf2144edeed271bb4a)
which started with **271 lines of code** and one test and
ended up with **992** and **14 test cases**.

![Claude Code CLI agentic AI migrating tests](./migration-on-the-works.png)

Claude Code CLI agentic AI migrating tests

This step was repeated 50 times until all tests were migrated, creating a
PR for each.

I've been thoroughly impressed by the AI performance for this use case,
the ability to **debug and fix tests** has really surprised
me. I did find some shortcomings during this project.  
As
when the AI reaches its **context limit** normally during
long running tasks it will really have a hard time remembering what to do
next and following the original plan. For me I found that
**10 tests at a time** was the sweet spot.  
**Verifying the results is critical**, this project was a
perfect example because apart from manually reviewing the code changes, we
could easily run the tests and verify they worked as expected with
**100% coverage** and make sure
*no original source code was modified*. Having
**good automated tests** is even more valuable than ever.  
AI will tend to **skip problems it can't solve easily**. I
noticed that it wasn't able to maintain the code coverage until I added to
the prompt the instructions on how to collect the coverage in JSON format
so it could understand the coverage problem and have enough context to
make the necessary fixes.  
AI providers are having trouble keeping up with the demand. During this
migration I had multiple outages.

![Claude Code status page with multiple outages](./sample-outages.png)

Claude Code status page with multiple outages

Although I was tempted to automate even further this migration by creating
a script to loop over each migration stage and create the PR
automatically, I decided against it because when faced with an edge case,
the solution from the AI wasn't always the best. Sometimes it relied on
hacks, for example using
`fireEvent` instead of deeply understanding the real root
causes under the hood with `userEvent`. So right now I prefer
to be vigilant instead of making a fool of myself in front of the whole
team.

It took me **one week** to do this migration. It consisted of
**50 PRs** and each one took around half an hour. There were
many tricky situations which the agent figured out that would've taken me
*hours to debug myself*, and the changes involved, although mostly
mechanical and repetitive, would've taken
**months to complete**. The worst part of this kind of work
is how energy-draining it is because there is little creativity involved.
I'm truly amazed, and this is not a Claude ad, I'm a big fan of
[OpenAI Codex CLI](https://chatgpt.com/en-ES/features/codex/)
or
[Google Gemini CLI](https://geminicli.com/)
too. Paying for more usage and better models has been totally worth it,
[check the leaderboard to see if you are missing out](https://lmarena.ai/leaderboard/webdev)
on better performance.

**Traditional strong software development fundamentals still
apply**: work on small changes iteratively, make sure you have good automated
validation to give you confidence to push those changes, and make sure you
have a good understanding of what is going on under the hood when the time
comes to debug because I'm sure it will.

I'm truly excited because **mundane maintenance tasks** are
very common in long-running projects and it seems we are getting close to
forgetting about them and having them **truly automated**.
Giving software developers more time to actually work on
*solving real customer problems* with software, what an amazing
revolution we are living.

## Let's build something solid.

Stop firefighting. Start shipping with confidence. Let's talk about what
predictable delivery looks like for your team.
