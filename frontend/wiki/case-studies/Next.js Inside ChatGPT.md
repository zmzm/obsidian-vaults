---
type: case-study
status: active
updated: 2026-04-14
tags:
  - nextjs
  - apps
  - mcp
  - chatgpt
---

# Next.js Inside ChatGPT

This case study captures what it takes to run a full Next.js application inside ChatGPT through MCP-style app integration.

## Context

- The app runs inside a triple-iframe sandbox with nonstandard navigation and asset-loading constraints.
- The challenge is not ordinary web deployment, but integration into a hosted app runtime with strict boundaries.

## What Had To Be Solved

- Relative assets and routing assumptions had to be adapted.
- Browser history and client-side navigation needed patching.
- Fetch behavior and RSC-related network expectations had to be made compatible with the environment.
- A starter template emerged to automate much of the integration work.

## Why It Matters

- This is a strong example of framework behavior being shaped by host-environment constraints.
- It is interesting even beyond Next.js because it shows how app frameworks behave when embedded inside another product surface.
- It also connects directly to the growing agent/app/tooling branch in the vault.

## Main Lesson

- Host environment constraints can become first-class architecture concerns, not just deployment details.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../sources/Next.js Agentic Future|Next.js Agentic Future]]

## Raw Source

- [[../../raw/twir/255/articles/10 - Running Next.js inside ChatGPT A deep dive into native app integration|TWIR item note]]
- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
