---
type: twir-item
issue: 259
item: 1
item_type: featured
date: 2025-11-19
source: https://go.posthog.com/twir-nov19
tags:
status: auto
quality: keep
---

[[2025-11-19-TWIR-259|Index]]

# Item 1: Product for Engineers - Non-obvious pricing advice for startups

Source: [https://go.posthog.com/twir-nov19](https://go.posthog.com/twir-nov19)

Summary:
PostHog shares lessons learned from pricing their suite of developer-focused products. The article emphasizes that pricing strategy shapes product identity, advocates for charging early (even if imperfect), and normalizes frequent pricing changes. Real-world examples and cautionary tales (like Kite) illustrate the importance of aligning pricing with customer profiles and iterating based on feedback.

Key takeaways:
- Pricing structure impacts product perception and customer behavior as much as features or design.
- Charging something early yields more valuable feedback than free users provide.
- Frequent pricing changes are normal and necessary; communication with customers is key.
- Align pricing models with your ideal customer profile for best results.

Recommendation:
Summary sufficient

Content:
# Non-obvious pricing advice for startups

We’re constantly thinking, debating, and learning about pricing at PostHog:

This is what we’ve learned.

---

---

Pricing isn’t just how you make money, it defines your identity, how you market, and how you sell. It’s just as impactful as your product’s functionality or design.

To illustrate, let’s imagine two feature flag tools.

**Feature Flags “R” Us** charges by **seats** and **flags created**:

- Their customers think about every flag and user they add, so they do less of both.
- The flags they *do* create are more heavily relied on.

This model appeals to companies that ship slowly and make more requests per flag. This means enterprise features, like auditability and access controls, are a priority.

**The Flag Company of New York** charges by **requests**:

In short, **how much** you charge often doesn’t matter as much as **how** you charge. While they’re superficially similar products, how these two products charge leads to a totally different experience, and different sales motions, too.

---

It’s easy to give things away, especially zero marginal cost software, but it’s a trap for early-stage startups. Typically, startups delay figuring out pricing because:

1. They are scared no one will pay them
2. They are afraid of getting pricing wrong and damaging growth
3. They think user growth is more important than revenue

But, unless you’re building Facebook, you’re always better off charging something as soon as possible, even if the unit economics don’t add up yet. Why? Because paying customers give you different, and more valuable, feedback than free users.

Don’t believe us? Consider the fate of Kite, a failed AI coding startup that had 500k monthly active users when it shut down. As the founder reflected in a [blog post](https://kite.com/):

> We failed to build a business because our product did not monetize, and it took too long to figure that out.
>
> We sequenced building our business in the following order: First we built our team, then the product, then distribution, and then monetization.

The first three steps worked. They built a “world-class engineering team” and grew the product to 500k developers with “almost no marketing spend.”

But monetization let them down. Those developers did not pay to use Kite. All the work on previous steps did not pay off and they had to shut down after seven years.

If they had charged earlier, they would have learned faster and possibly avoided the “innumerable sacrifices” they had to make it keep the business going for so long.

> **Remember this:** Pricing is just like product. The sooner you ship something, the sooner you’ll learn what users want. Speaking of which…

---

You’ll almost certainly get your pricing wrong, especially if you are charging early. That’s normal, all companies do it.

Later, in March 2021, we added our first iteration of usage-based pricing for a single product and have kept iterating on this model ever since.

Finally, in May 2021, we increased our free tier for events 100x and this combination of usage-based pricing with a generous free tier has been the core of our pricing ever since.

All of your favorite companies who aren’t called PostHog change their pricing regularly, too:

> **Remember this:** Pricing changes require good communication. Give customers:
>
> - Plenty of notice about changes. Figma gave three months.
> - A warning, grace period, and discount if you’re raising prices.
> - The option to keep old pricing unless it is more expensive or you have a good reason not to.

---

How much free stuff should we give away? It’s easy to either debate this endlessly, or fall into one of two extremes:

1. **Give away as much as possible.** Users love free stuff, increasing your free tier is a good way to get more users.
2. **Charge for everything.** This makes more money and money is good.

- Features that increase stickiness should be free with a reasonable limit. A good question to ask here is: “If I were to switch away to a competitor, what would I feel like I am losing?” It’s tough to leave Figma when all your projects and designs are in one place.

> **Remember this:** Principles prevent every discussion about the free tier from becoming a debate, while avoiding the extremes of giving away too much or charging for too little. Pricing principles should guide *all* your pricing decisions, too.

---

If you want to go beyond the simple subscription model most billing systems offer, you will need at least one engineer dedicated to it.

Why do we need so many people involved in billing?

- It enables us to charge the way we want. It can be tempting to just accept the simple subscription model most billing systems offer, but this limits your ability to have pricing that aligns with your value creation. Our billing team lets us price products, add-ons, and platform packages how we want.
- The billing system needs the flexibility to handle many situations, such as discounts, contracts, credits, invoicing, and weird payment methods (pay by cheque anyone? *Please don’t*).
- It needs to be reliable. Charge too much and customers will be super unhappy. Charge too little (or miss failed/late payments) and you are literally leaving money on the table.
- It enables us to make more accurate revenue models and projections, which helps us with everything from hiring to fundraising to product roadmaps.

> **Remember this:** Without someone dedicated to billing, pricing launches are painful, your ability to charge users is limited, more errors and unhappy customers pop up, and any decision involving revenue becomes more difficult.

---

Everyone hates being charged more than they expected. This, of course, hurts the customer, but it also hurts you, as it leads to more churn and a worse reputation.

The solution to this, for many companies, is to make their pricing simpler. Fewer tiers, a unified credit system, a single subscription for everything. For B2B companies, this is a mistake as it limits your ability to charge users for the value they receive.

The alternative we recommend is making your pricing more predictable and transparent. Some ways to do this include:

- **Add spend limits.** If customers don’t want to pay over a certain amount, respect that, but make it clear what they’ll lose when they hit the cap.

Some may call this “leaving money on the table” but we see it as doing the right thing. I’m sure others have had success with the dodgiest pricing tactics possible, but the trust we’ve built with customers is core to what makes PostHog successful, so we won’t be changing these.

*Words by [Ian Vanagas](http://x.com/ianvanagas), free tier enjoyer.*

---

---
