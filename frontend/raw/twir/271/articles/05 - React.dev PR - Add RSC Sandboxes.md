---
type: twir-item
issue: 271
item: 5
item_type: item
date: 2026-03-04
source: https://github.com/reactjs/react.dev/pull/8300
tags:
  - "RSC"
  - "Reactdev"
  - "PR"
  - "Bun"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 5: React.dev PR - Add RSC Sandboxes

Source: [https://github.com/reactjs/react.dev/pull/8300](https://github.com/reactjs/react.dev/pull/8300)

Summary:
This pull request introduces a browser-only <SandpackRSC> component to the React documentation site, enabling interactive React Server Component (RSC) sandboxes using web workers and react-server-dom-webpack. It leverages sucrase for JSX transpilation and streams RSC chunks to the client for real-time editing and testing. The PR also discusses bundle size impacts, streaming behavior, and the potential for further CI validation.

Key takeaways:
- Adds interactive RSC sandboxes to React docs, improving hands-on learning and experimentation.
- Uses web workers and streaming to simulate RSC behavior in the browser.
- Some bundle size increase is noted; further CI automation is considered for future maintenance.

Recommendation:
Summary sufficient (read PR for implementation details or if contributing to docs)

Why it matters:
read PR for implementation details or if contributing to docs

Content:
# Add RSC Sandboxes by rickhanlonii · Pull Request #8300 · reactjs/react.dev · GitHub

## Conversation

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

You can’t perform that action at this time.

Related notes: [[Server Components]]
