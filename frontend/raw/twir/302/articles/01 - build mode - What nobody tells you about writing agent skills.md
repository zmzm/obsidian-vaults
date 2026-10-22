---
type: twir-item
issue: 302
item: 1
item_type: featured
date: 2026-10-21
source: https://go.posthog.com/twir-oct21
tags:
status: auto
quality: keep
---

[[2026-10-21-TWIR-302|Index]]

# Item 1: build mode - What nobody tells you about writing agent skills

Source: [https://go.posthog.com/twir-oct21](https://go.posthog.com/twir-oct21)

Summary:
This article shares lessons learned at PostHog about writing effective "skills" for coding agents, focusing on how to structure and describe them for maximum utility. It emphasizes the importance of progressive disclosure, concise and discoverable skill descriptions, and balancing precision with flexibility. The piece also warns against over-specifying workflows, which can limit agent intelligence and adaptability. Practical tips are provided for making skills more effective and maintainable as agent usage scales.

Key takeaways:
- Skills should use progressive disclosure: only relevant context is loaded as needed, not all at once.
- Skill names and descriptions should focus on when to use them, not just what they do.
- Overly detailed or numerous skills can overwhelm agents and reduce effectiveness.
- Skills should be precise about goals and constraints but flexible about steps and runtime specifics.

Recommendation:
Read fully (especially if you are building or maintaining agent skills or AI-driven workflows)

Why it matters:
especially if you are building or maintaining agent skills or AI-driven workflows

Content:
# What nobody tells you about writing agent skills

They’re essential because agents have amnesia. Every conversation, they rediscover your codebase and workflows from scratch. They pick the wrong tool, fall for the same gotchas, and repeat old mistakes. They figure it out eventually, but only after wasting time and tokens.

This is irritating for engineers who hate repeating themselves. That’s why they automate, write abstractions, and keep handy scripts around. Skills are this instinct applied to agents. Write them once and never explain to agents again.

Here’s everything we’ve learned about writing skills that actually work, for both you and your product.

Agents can learn entire programming languages, figure out how to use nearly any tool you throw at them, and improve themselves in a loop, but only if they have context to do it in.

Context is usually dumped in all at once at the beginning, which limits the amount agents have to work with. Skills flip this. Instead of loading everything up front, they disclose information progressively. The skill’s information is only loaded when the agent decides it’s relevant, whether that is the main `SKILL.md` file or `references` and `scripts` within it. This means **good skills act as a router**.

First, the agent needs to choose to load the skill. The skill’s name and description should describe when to reach for it, not what the skill is, because they’re only part always in context.

Here’s [our SQL skill](https://github.com/PostHog/posthog/tree/master/products/posthog_ai/skills/querying-posthog-data) as an example:

- The name and first sentence define when to read the skill.
- The middle sentence defines when to use it.
- The last sentence defines what the skill does.

Sections *within the skill* also need to work as routers. The rest of [our SQL skill](https://github.com/PostHog/posthog/tree/master/products/posthog_ai/skills/querying-posthog-data) is a thin workflow that links to 26 schema files, 22 example query patterns, and a function index. This enables further progressive disclosure.

If done correctly, skills help agents succeed faster with fewer tokens, but only because the context isn’t loaded all at once.

> **Try this:** Read your skills through the lens of progressive disclosure. Do the names and descriptions help them get discovered? Are they split in a way that agents can only load what they need?

Look at these two mini-skills:

> 1. Run `git log --oneline -20`.
> 2. If you see a commit with “fix” in it, check the diff.
> 3. If the diff touches `auth.py`, read lines 40–120.
> 4. If the function is over 50 lines, flag it.

And

> Find recent changes that look risky and explain why. Start with the commit history.

They have the same spirit, but the first is over-specified. It breaks the moment the repo doesn’t match what the skill expects. The second survives because it embraces ambiguity, the agent can actually look at what’s in front of it.

This is how treating skills like code goes wrong. Skills are a superset of code. They can do everything code can (because agents can write code) as well as a lot of things it can’t (because they are smart). Agents can handle cases in your skills you can’t foresee, like errors or runtime context, but only if you let them do so.

This means skills should be precise about:

1. **The goal.** What does “done” look like? If you don’t say, the agent will decide for you. Give it examples of what good looks like or ways to self-verify. For example, the `creating-an-endpoint` [skill](https://github.com/PostHog/posthog/blob/master/products/endpoints/skills/creating-an-endpoint/SKILL.md) asks the agent to “confirm by calling `endpoint-run` with a sample payload to verify the response shape.”
2. **Constraints.** The boundaries and guardrails that prevent disaster.
3. **Context it can’t derive.** Where your data lives, which tool to use, the schema it would otherwise need to guess.

But ambiguous about:

1. **The steps.** You don’t need to be prescriptive about what files to check. Tell it to understand how billing works and it will find them.
2. **Failures.** You can’t know everything that will go wrong. The agent can read the error and you’re paying it to figure it out.
3. **Runtime specifics.** What the data actually looks like. Line numbers, file lists, counts, versions, and outputs all change more often than you think.

Over-specification turns a skill into a workflow and strips the intelligence you are paying for. Leaving the path ambiguous gives agents the flexibility they need to do what you want them to do.

> **Try this:** Make your skills *less* prescriptive. Give the agent the tools they need and the goal you want them to achieve then let them find a way to do it.

Products, APIs, CLIs, MCPs, models, behaviors, and best practices all change. When these changes break skills, most people just make fixes ad hoc, but this wastes time and tokens whenever it happens.

You can be more proactive than that. Preventing rot comes down to three principles:

1. **Split durable structure from volatile content.** Hand-write parts that rarely change, *reference* parts that drift.
2. **Point to a single source of truth.** For us, that’s docs. Skills that point to specific URLs are less likely to go out of date than ones that include all the content separately.
3. **Regenerate, don’t patch.** Rewrite and refine your skill from a stable base rather than piling on fixes. Repeated fixes cloud a skill’s focus until it rots into something less effective.

These principles work at the individual level, but can also scale to a robust pipeline for skill generation. Our [Wizard & Docs team](https://posthog.com/teams/wizard-and-docs) do this to publish 120+ skills on how to integrate and use PostHog correctly.

The main part of this pipeline is the [context mill](https://github.com/PostHog/context-mill) (above) which consists of three parts:

1. **Sourcing:** Pulls all our docs plus curated prompts and working example apps.
2. **Assembly:** Transforms and packages these into a portable, self-contained zip manifest.
3. **Delivery:** Creates a versioned release that is used by both the PostHog MCP (as resources and slash commands) and the install wizard.

You don’t need a pipeline like this to prevent your skills from rotting. The three principles work by hand. Done right, a skill doesn’t just resist rot, it improves on its own. Point it at the docs and it tracks their changes. Regenerate it from a prompt and it inherits model and implementation upgrades.

> **Try this:** Next time you need to do an ad hoc fix for a skill, think of and implement a way to prevent future rot like pointing to a URL or generating a part of the skill instead.

Agents, like people, work better when you understand them and what they need. So rather than jumping straight to making demands, try asking questions like:

1. **“What can you do to help?”** You need to know what tools and capabilities an agent has to help you accomplish your task. You should care about agent ergonomics and let it shape the skills you write.
2. **“What do you need to do better?”** Beyond what’s built-in, there might be other tools, capabilities, context access, or evaluations that might help it improve the skill.
3. **“Based on the last run, how can this skill improve?”** Runs often uncover errors or inefficiencies that can be fixed by tweaking the skill.

> **Try this:** Before building your next skill, build some empathy for the agent by asking the questions above. This is high leverage work, so use a more powerful model, like Fable, even if a less powerful model will run the skill.

Reading all this might inspire you to write skills for everything, but remember there are context and maintenance costs for each one. Picking the right ones matters, so you should write skills for work that…

- **Agents do badly by default.** Ask your agent to do the skill you’re planning to write. If it can accomplish it efficiently, it doesn’t need a skill. For example, it doesn’t really need a skill to write SQL, but it might need a skill to write ClickHouse-flavored SQL specific to PostHog.

> **Try this:** Run this prompt to create some new skill candidates.

*Words by [Ian Vanagas](https://x.com/ianvanagas), who’s definitely skill-pilled.*

---

---

---
