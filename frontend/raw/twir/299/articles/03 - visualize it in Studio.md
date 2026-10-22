---
type: twir-item
issue: 299
item: 3
item_type: item
date: 2026-09-30
source: https://panda-css.com/blog/see-your-design-system
tags:
  - "Panda"
status: auto
quality: keep
---

[[2026-09-30-TWIR-299|Index]]

# Item 3: visualize it in Studio

Source: [https://panda-css.com/blog/see-your-design-system](https://panda-css.com/blog/see-your-design-system)

Summary:
Panda Studio is a web tool that visualizes your design-system.json, showing resolved tokens (colors, spacing, fonts, etc.) and now tracks which tokens are actually used in your codebase. You can analyze usage by dropping in your source files and config, and share the results via a link. The analysis runs locally in the browser using the Panda compiler compiled to WebAssembly.

Key takeaways:
- Visualizes and analyzes actual token usage in your design system.
- Helps identify unused tokens for cleanup and maintenance.
- Sharing and collaboration are enabled via link-based reports.
- No data leaves your browser unless you explicitly share.

Recommendation:
Read fully (read fully if you manage design systems or want to use the tool)

Why it matters:
read fully if you manage design systems or want to use the tool

Content:
# See your design system, and what it uses

You already have a design system written down. It's the `design-system.json` Panda emits: every color, space, font, radius, and
shadow, with values resolved. Describing the system was never the hard part. Seeing it was.

![Studio, a full color system rendered straight from design-system.json](/blog/spec-studio-hero.png)

Studio renders that file. Drop it in and every category paints. Colors become a swatch grid, spacing becomes a
sorted scale, fonts become specimens, durations and easings become chips that animate. No install, no account, no config.

![The colors category in Studio: a swatch grid with values and WCAG contrast readouts, categories down the side](/blog/spec-studio-tokens.png)

It's the same idea as the [JSON Spec](/docs/theming/json-spec) docs, where Panda hands you the data. Studio is the
viewer already built on top of it. Two things are new this release: it can tell you which tokens your code uses, and you
can share any of it as a link.

## Which tokens are you actually using?

Every design system collects tokens nobody references. A `red.500` that got replaced, a spacing step added for one screen
and never touched again. You can't spot them in the config, because a used token and an unused one look identical there.

**Analyze usage** answers the question. Drop your source files, or the whole repo folder, and it reports per category:
which tokens are used, which are unused, and which are hot. Read the unused list first. Those are the tokens you can
delete.

![Analyze usage: a coverage donut, the hottest tokens ranked, and the unused list, here 11 of 300 tokens used](/blog/spec-studio-analyze.png)

How it counts depends on what you drop:

- **Include your `panda.config.ts`** and the real Panda compiler runs in your browser, through `@pandacss/compiler-wasm`.
  Same extraction and token resolution as a build, so a bare-numeric token like `spacing.4` is counted exactly. It's the
  compiler reading your code, not a guess at it.
- **Leave the config out** and a name-match scan runs instead. It's accurate for named tokens like `red.500` and
  approximate for numeric ones. A badge on the report tells you which tier you got.

The compiler running in the browser is the same Rust engine we [shipped in Panda 2.0](/blog/panda-css-v2), compiled to
WebAssembly. When your config is in the drop, the numbers come from an actual compile of your code on your own machine.
Nothing is uploaded.

## Share it as a link

A rendered system is easier to talk about than a config file. The **Share** button saves the tokens and opens a
read-only page at `/s/<slug>` that anyone can view. Share an analysis and the usage report goes with it, at `/a/<slug>`,
so whoever you send it to sees the same used and unused breakdown you did.

No accounts, no teams, no ownership. Make a spec, get a link, send it. It's the quickest way to put a design system in
front of a teammate, a designer, or a review thread without asking anyone to clone a repo.

## It's still your data

The hosted studio doesn't replace building your own viewer. The [Studio docs](/docs/theming/studio) still show you how in
about thirty lines: every category is `{ name, value }`, so a color grid is one `.map()`. Studio is just the version
you don't have to build.

Get your file with `panda codegen --spec`:

```
styled-system/specs/design-system.json
```

Open the studio, drop it in, and hit Analyze. Nothing leaves your browser until you press Share.

#announcement#tokens#tooling
