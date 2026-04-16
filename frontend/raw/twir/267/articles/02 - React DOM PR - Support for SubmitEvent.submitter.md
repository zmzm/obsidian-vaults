---
type: twir-item
issue: 267
item: 2
item_type: item
date: 2026-02-04
source: https://github.com/facebook/react/pull/35590
tags:
  - "DOM"
  - "PR"
  - "SubmitEventsubmitter"
  - "Bun"
status: auto
quality: keep
---

[[2026-02-04-TWIR-267|Index]]

# Item 2: React DOM PR - Support for SubmitEvent.submitter

Source: [https://github.com/facebook/react/pull/35590](https://github.com/facebook/react/pull/35590)

Summary:
A pull request to React DOM adds support for the SubmitEvent.submitter property, aligning React's event system with modern browser APIs. This exposes the element that triggered a form submission, aiding in more granular form handling. The change includes new tests and does not introduce significant bundle size changes.

Key takeaways:
- React forms will now have access to the submitter property on submit events, improving parity with native browser behavior.
- No polyfill is included for older browsers; assumes modern browser support.
- The update is backward-compatible and has negligible impact on bundle size.

Recommendation:
Summary sufficient

Content:
# [react-dom] Include `submitter` in `submit` events by eps1lon · Pull Request #35590 · facebook/react · GitHub

## Conversation

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

You can’t perform that action at this time.
