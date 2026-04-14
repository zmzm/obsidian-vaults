---
type: twir-item
issue: 257
item: 7
item_type: item
date: 2025-11-05
source: https://evilmartians.com/chronicles/why-startups-choose-react-and-when-you-should-not
tags:
  - "Storybook"
status: auto
quality: keep
---

[[2025-11-05-TWIR-257|Index]]

# Item 7: Why startups choose React (and when you shouldn't)

Source: [https://evilmartians.com/chronicles/why-startups-choose-react-and-when-you-should-not](https://evilmartians.com/chronicles/why-startups-choose-react-and-when-you-should-not)

Summary:
An analysis of 334 funded startups shows React dominates with 88.6% of startup funding, largely due to its vast ecosystem and tooling. However, the article notes that most projects (across all frameworks) are abandoned, and smaller frameworks like Svelte have higher project survival rates. It also highlights that cross-framework libraries are more successful, and that React’s dominance is partly due to inertia rather than technical superiority.

Key takeaways:
- React is the default for most funded startups, but project abandonment rates are high across all frameworks.
- Svelte and Vue, while less popular, have higher-quality project survival rates.
- Cross-framework libraries (e.g., Storybook, TanStack) are disproportionately successful.
- Choosing React offers ecosystem advantages, but intentional framework choices may yield better long-term outcomes.

Recommendation:
Summary sufficient (read full article for detailed data and nuanced discussion)

Why it matters:
read full article for detailed data and nuanced discussion

Content:
# Why startups choose React (and when you shouldn't)

Most funded startups in 2025 chose React, capturing $2.52 billion out of $2.85 billion (88.6%). But, some surprises: 85% of GitHub projects are abandoned, Vue dominates admin dashboards despite lower funding, and smaller frameworks like Svelte show better survival rates. We analyzed 334 startups founded in 2024 and thousands of GitHub repositories to learn why React maintains dominance—and if you should follow the crowd.

In this post, we’ll cover:

- Why React captured 88.6% of startup funding ($2.52B of $2.85B)
- The universal pattern of 85% project abandonment across all frameworks
- Why *smaller* ecosystems actually have greater longevity
- When to follow the money vs. when to buck the trend

In particular, we’ll take a closer look at React ([facebook/react](https://github.com/facebook/react)), Angular ([angular/angular](https://github.com/angular/angular)), Vue ([vuejs/core](https://github.com/vuejs/core)), and Svelte ([sveltejs/svelte](https://github.com/sveltejs/svelte)).

Why these? Because these are the frameworks used by the majority of software startups founded in 2024 and funded in 2025.

## Fun, fun, funds

React seems to be everywhere these days, even though there are more [enjoyable frameworks](https://2024.stateofjs.com/en-US/libraries/front-end-frameworks/) to work with. If there are alternatives beyond React, why does it continue to be the top choice?

We analyzed 985 software startups founded in 2024 with the last funding round in 2025 ($1M minimum). We auto-detected the frameworks for 334 startups’ apps (with $2.85 billion in total funding). Here’s the breakdown:

88.6%6.6%3.9%28418225

- **React** • $2.52B • 284 startups
- **Vue** • $187M • 18 startups
- **Angular** • $110M • 22 startups
- **Svelte** • $27M • 5 startups

*We analyzed software startups founded in 2024 with last funding round in 2025 (≥$1M). Framework detection based on app inspection (not landing pages).*

Note that we checked the apps, not the landing pages! Sometimes they hide behind a “Book a Demo” or auth provider redirects. Handling these cases involves some guesswork, spamming checks with [Playwright](https://github.com/microsoft/playwright), and checking open roles, hoping the stack is mentioned.

Anyway, you could say the data kind of confirms a gut feeling about React. Nonetheless, I’m very happy to see Svelte gaining traction.

## Dead or alive on GitHub

One common argument for choosing React is its massive ecosystem: ready-made solutions, out-of-the-box tools, and the ability to find libraries for almost anything. We saw React accounted for 88.6% of startup funding, likely because of this ecosystem advantage.

But what does that ecosystem actually look like? How many of those projects are actively maintained? How does it compare to others? Let’s check GitHub’s data.

Well, could you guess that approximately 85% of projects within these framework ecosystems are no longer maintained?

So what does this tell us about React’s ecosystem advantage?

Despite an 83% death rate, React still has 1.1 million projects alive out there. Compare this to Angular (128K alive) or Vue (114K alive)—React provides 8-10× more working libraries and tools.

Even with massive levels of abandonment, the sheer scale of projects means startups still get the ecosystem advantage that attracted them to React in the first place.

But here’s what is interesting: **when you filter for higher-quality projects (>10 stars), survival rates jump dramatically**. React improves to 20.7% alive, Svelte jumps to 36.1%, and the overall ecosystem improves to 19.8%.

Most React projects have ≤10 stars (only 13,153 of 1.1M alive projects exceed this quality threshold 🤯). Once a project gains real traction, it’s more likely to be maintained.

And here’s where it gets even more interesting: **even with the quality filter (stars >10), Svelte (36.1% alive) maintains the best survival rate, followed by React (20.7%), Vue (18.0%), and Angular (13.9%)**.

Why is that so? A few guesses:

**More intentional choices**: When you pick React, you’re following the crowd. When you pick Svelte, you’ve made an intentional decision to do so. This intentionality probably correlates with shipping actual products.

**Different project types**: React dominates startup funding. Startups fail at high rates by design. Svelte and Vue power more internal tools and admin dashboards—  
projects that just need to exist, not succeed venture-style.

**React’s age**: React accumulated 6.4M repos over more years, including plenty of abandoned legacy code. Svelte’s smaller pile is newer and less burdened by the past.

(Honestly, we can’t prove any of this without analyzing project creation dates, code complexity, and actual use cases. These are educated guesses based on the numbers we have.)

In any case, new repository creation is slowing down. Here’s how that looks across frameworks (2022, 2023, 2024):

## A closer look at repositories

We analyzed 2,816 repositories with 100+ stars that were created before 2020 and with pushes in 2025. I think you’ll agree these can be safely considered reputable.

### Top Categories

Categories were assigned using Claude Haiku to analyze repository descriptions, README files, and GitHub topics. Each repository was assigned to its primary purpose (e.g., “UI Components & Design Systems” for component libraries, “Admin & Dashboard” for backend management tools, “Learning Resources” for tutorials and examples).

Some repositories could fit multiple categories; in those cases, we prioritized the most prominent use case based on the repository’s stated purpose.

Let’s take a look at the 5 categories from each ecosystem. (For more details please take a look at this [gist](https://gist.github.com/vadirn/ceac7ee86dc1d66ab7136f27a00b6cb6#file-3-react-md).)

A quick glance shows us that “UI Components & Design Systems” is the most popular category across all frameworks.

### Cross-framework projects

While 94.6% of repositories commit to a single framework, those spanning multiple frameworks tell a different story.

Out of 2,816 analyzed repositories, only 151 support multiple frameworks, and yet, they’re disproportionately successful. The correlation is striking: **single-framework projects average 3,177 stars, but projects supporting all four frameworks average 15,254 stars**. Storybook (88k stars across React, Angular, Vue, and Svelte) stands as the ultimate example.

Other top cross-framework projects like [TanStack/query](https://github.com/TanStack/query), [xyflow](https://github.com/xyflow/xyflow), and [ueberdosis/tiptap](https://github.com/ueberdosis/tiptap) all surpass 25k stars.

The most common combinations reveal natural pairing patterns:

- **React + Vue**: 52 repositories
- **React + Angular + Vue**: 42 repositories
- **React + Angular**: 27 repositories

UI Components dominate cross-framework projects (25.2%), followed by Learning Resources (19.9%), that is, the same categories that benefit most from framework-agnostic design.

This pattern reinforces a critical insight: **the highest-quality tools and libraries treat frameworks as interchangeable concerns, not as an identity**.

Framework lock-in is real (and probably necessary for most projects), but the most successful open-source projects architect their code to survive framework migrations.

## Developer experience

Developer satisfaction tells a different story than funding and repository counts.

While React dominates the money and the repos, Svelte maintains the highest satisfaction at 88%, Vue surged +12 points to 87%, and Angular improved to 54%. Meanwhile, React’s satisfaction slipped to 75% despite powering 67% of professional projects.

In short, the gap between “what gets funded” and “what developers actually enjoy using” has never been wider.

## When to move beyond React?

React’s dominance doesn’t lie in technical superiority, rather, it’s about hiring. React’s massive repository base proves one thing: React developers exist, and you can find them.

When VCs fund React startups, they’re betting on predictable talent acquisition, not framework performance. The 67% “at work” usage reflects hiring ease, not developer preference.

But here’s the question: **do you actually need the hiring advantage that React brings?**

- If you’re planning to double your team every quarter, React makes sense. If you need to replace developers frequently or scale headcount aggressively, that massive talent pool matters.
- But if you’re building with a stable team, or growing at normal pace, you can optimize for something more important: developer experience.

The gap between React’s 75% satisfaction and Svelte’s 88% compounds over time. Happier developers stay longer, ship faster, and write better code. The 12-point satisfaction surge in Vue and Angular isn’t noise. Instead, it’s developers telling us which tools they actually enjoy using once they get past the hiring constraint.

And about that ~85% project abandonment rate across all frameworks? That’s not a bug, it’s reality. Frameworks evolve, get deprecated, and get replaced. The real lesson isn’t “pick the most popular framework”—it’s “design your architecture so your business logic survives framework migrations.” Keep your domain code portable and framework-independent. Your rendering layer should be replaceable.

**If you’re not constrained by aggressive hiring needs, consider Vue.** It hits the sweet spot: 87% satisfaction (up 12 points), 31% work adoption (sufficient for normal hiring), and proven strength in admin dashboards and internal tools where it genuinely excels. You’ll find developers, they’ll be happier, and your codebase will thank you.

**For specific contexts:**

- **Large enterprises:** Angular’s opinionated structure (54% satisfaction, climbing) provides guardrails that prevent architectural chaos at scale
- **Performance-critical apps:** Svelte (88% satisfaction) delivers better DX with smaller bundles and exceptional developer satisfaction

So, the “safest choice” isn’t always the best choice. Make informed decisions based on your actual constraints:team size, growth rate, hiring needs, performance requirements—not just popularity contests.

*P.S. Many excellent frameworks ([Solid](https://github.com/solidjs/solid), [Qwik](https://github.com/QwikDev/qwik), [Alpine](https://github.com/alpinejs/alpine), etc.) didn’t appear in our startup dataset. This isn’t because they’re inferior, but because our sample was limited to specific [Crunchbase](https://www.crunchbase.com/) coverage. The frontend ecosystem is richer than any single analysis can capture!*
