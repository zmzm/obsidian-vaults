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
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 4: React PR - Init Claude config

Source: [https://github.com/facebook/react/pull/35617](https://github.com/facebook/react/pull/35617)

Summary:
This PR introduces a Claude AI configuration for the React repository, handling the complexity of nested compiler setups. It ensures the correct context and skill files are loaded based on the working directory, using a SessionStart hook and context management. Several AI-assist skills are added (e.g., extract-errors, feature-flags, flow, test, verify), with before/after examples for Flow and test outputs. The CLAUDE.md file is intentionally minimal, with discussion about potentially expanding it for more repository context.

Key takeaways:
- Adds Claude AI config that adapts to root vs. compiler subdirectory, using context hooks.
- Introduces specialized AI skills for common React repo workflows (testing, error extraction, feature flags).
- Provides before/after examples for Flow and test command outputs.
- CLAUDE.md is minimal, with openness to future expansion for better AI tooling support.

Recommendation:
Read fully (read fully if interested in AI-assisted tooling or contributing to React repo automation)

Why it matters:
read fully if interested in AI-assisted tooling or contributing to React repo automation

Content:
# [repo] init claude config by rickhanlonii · Pull Request #35617 · facebook/react · GitHub

```
## Overview

Adds a claude setup that works with the nested /compiler setup.

The constraints are:
- when working in the root repo, don't use the compiler configs (easy)
- when working in the compiler/ don't use the parent contigs (hard)

The first one is easy: there's a claude.md and .claude directory in
/compiler that is only loaded when you start a session from /compuler.
The second one is hard, because if you start a session from /compiler,
the parent claude files and skills are loaded.

I was able to deny the permissions to the parent skills in
settings.json, but the descriptions are still loaded into context and I
don't think that's avoidable.

To keep the parent claude file out of context, I created a hook hack: I
moved all the non-compiler claude file context to instructions.md and
added a SessionStart hook to cat the file into context if the cwd isn't
the /compiler. Works well, but won't show it as part of the `/context`
slash command.

## Skills

I also added a number of skills specific to the React repo:

| Skill | Description |
|-------|-------------|
| `/extract-errors` |  `yarn extract-errors` |
| `/feature-flags` | how feature flags work and `@gate`  |
| `/fix` | linc and prettier |
| `/flags` | `yarn flags` |
| `/flow` | `yarn flow <variant>` |
| `/test` | `yarn test-*` |
| `/verify` | `run all the lints/tests/flow to verify` |

### Example: Flow

| before | after |
|-----|-----|
| <img width="1076" height="442" alt="flow-before"
src="https://github.com/user-attachments/assets/73eec143-d0af-4771-b501-c9dc29cc09ac"
/> | <img width="1076" height="273" alt="flow-after"
src="https://github.com/user-attachments/assets/292d33af-1d98-4252-9c08-744b33e88b86"
/> |

### Example: Tests

| before | after |
|-----|-----|
| <img width="1048" height="607" alt="test-before"
src="https://github.com/user-attachments/assets/aa558ccf-2cee-4d22-b1f1-e4221c5a59dd"
/> | <img width="1075" height="359" alt="test-after"
src="https://github.com/user-attachments/assets/eb795392-6f46-403f-b9bb-8851ed790165"
/> |

DiffTrain build for [a056625](facebook@a056625)
```
