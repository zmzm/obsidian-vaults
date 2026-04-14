---
type: twir-item
issue: 266
item: 4
item_type: item
date: 2026-01-28
source: https://github.com/facebook/react/pull/35617
tags:
  - "PR"
  - "Skills"
status: auto
---

[[2026-01-28-TWIR-266|Index]]

# Item 4: React PR – Init Claude config

Source: [https://github.com/facebook/react/pull/35617](https://github.com/facebook/react/pull/35617)

Summary:
This PR introduces a Claude AI configuration for the React repository, designed to work with both the root and nested /compiler setups. It includes logic to isolate context and permissions between root and compiler directories, and adds several AI-assist skills (e.g., extract-errors, feature-flags, test, flow, verify) tailored for React development workflows. The PR also provides before/after examples for Flow and test outputs, and invites further expansion of the CLAUDE.md documentation.

Key takeaways:
- Sets up Claude AI context management for React repo and compiler subdirectory.
- Adds custom skills for common React repo tasks (error extraction, feature flags, testing, Flow, etc.).
- Uses hooks and instructions to manage context loading and permissions.
- Documentation is intentionally minimal, with openness to future expansion.

Recommendation: Summary sufficient (read PR if you work on React repo automation or AI-assisted tooling)
