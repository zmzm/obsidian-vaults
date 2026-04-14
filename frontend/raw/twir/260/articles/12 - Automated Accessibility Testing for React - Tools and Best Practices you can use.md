---
type: twir-item
issue: 260
item: 12
item_type: item
date: 2025-11-26
source: https://howtotestfrontend.com/resources/accessibility-testing-your-react-app
tags:
status: auto
---

[[2025-11-26-TWIR-260|Index]]

# Item 12: Automated Accessibility Testing for React - Tools and Best Practices you can use

Source: [https://howtotestfrontend.com/resources/accessibility-testing-your-react-app](https://howtotestfrontend.com/resources/accessibility-testing-your-react-app)

Content:
# Automated Accessibility Testing for React - Tools and Best Practices you can use

As a frontend engineer, I think it is very important to make sure that anything I work on is *accessible and usable by anyone and everyone*. (Hopefully I've done ok on this site! Still a few improvements I want to make though)

I always find that the majority of the (very) basic things that make a website accessible are quite easy to implement, it is just hard to remember.

So for all my personal projects & at work **I always try to use automated tools to at least try to catch some basic accessibility issues** before they hit production.

In this article I'm going to explain **what tools, scripts, frameworks, services and libraries that I (and you) can use to automate these accessibility checks**, and how to get them in your CI/CD deployment pipeline.

**What is CI/CD** *(Show details)*

CI/CD stands for continuous integration/continuous deployment.

It means that every time you make changes to your code and push them to a repository (like GitHub), automated processes will run to build, test, and potentially deploy your application without manual intervention.

I want to point out very early on that **you can't 100% rely on automated tests to find all accessibility issues**. It is impossible for them to catch every type of accessibility issue, and cannot eliminate the need for proper manual accessibility checks.

But also I cannot count the number of times these tools have caught dumb mistakes in my code where I forgot or misconfigured something simple! So despite them not able to catch everything, they do catch valid issues worth fixing.

## Introduction & quick accessibility explainer

Before getting into what tools, libraries and services you can use, I'll start with a very quick and brief intro into accessibility.

**If you know what accessibility is then you can skip down a few paragraphs**! This next section
is meant to be a *very simplified* and very basic intro into what web accessibility is.

### What is web and digital accessibility?

In one sentence, the way I see web accessibility is: **If a website has good web accessibility, then it means it can be used by everyone (including those with disabilities)**.

So the website/app should have things such as:

- clear **plain language**,
- text colours should have **good contrast** to make them easy to read,
- interactions should be possible by **keyboard only** (not just with a mouse)
- **images should have alt text** that is screen reader friendly
- buttons and interactive elements should have a **large enough 'tap target'** so you can easily click it or tap on it.
- (and much more)

**What are screen readers?** *(Show details)*

Screen readers are what people with
sight issues can use to read out the
contents of your app.

They'll describe what is on the page. If you focus on a
`<button>join</button>` for example,
it will explain that it is a button
with the text of "join".

This is why it is so important to use 'semantically correct' HTML - this means using a `button` HTML element, not a `div` with an `onClick` function. Or why using headings (like `h1`) is important - if you style a `p` or `div` to visually look bigger and like a heading, the screen reader technology won't announce it as a heading.

There are also other 'assistive technologies' such as voice recognition software,
magnification tools and more, and they tend to have the same requirements of semantically correct HTML in order to accurately be used.

**Why accessibility matters and who it affects** *(Show details)*

There are various stats going around when it comes to accessibility, but the generally accepted guidance is that accessibility affects around 15-20% of the global population.

This includes people with:

- *permanent* disabilities,
- *temporary* impairments (like a broken arm)
- or what is often called *situational limitations* (like being in a bright environment where screen glare makes text hard to read).

**Why is it important to consider accessibility?** *(Show details)*

Obviously there are **moral reasons to make accessible apps/sites** that are inclusive and usable by anyone

There are also **legal reasons** - most countries (including USA, UK, and the EU) have legal requirements for web and digital accessibility.

By making your site accessible, it **improves the user experience for everyone**. This isn't something that only benefits disabled people

In my opinion, with the rise of AI agents, having a website with great accessibility will no doubt help AI agents understand your app and interact with it better.

**Examples of how to make things accessible** *(Show details)*

**Use semantically correct HTML**. For example, use a `<button onClick={fn}>click me</button>` tag, **and not another element that acts like a button** (for example `<div onClick={fn}>click me</div>`).

**Don't use tiny text** - make sure your font size is at least 16px for body text.

**Use `alt` attributes correctly** on images - describe what the image shows, not just "image" or "picture".

Have **good colour contrast** (dark text on a light background, or vice versa).

Make sure you **can use your app with just a keyboard** (hitting Tab to focus on elements, hitting Enter or other keys to interact with them).

Ensure all form inputs (like `input` and `select` elements) are **properly labelled**.

**What is a11y?** *(Show details)*

The word `accessibility` is quite long, and is often shortened to just `a11y`, as there are 11
characters between the 'a' and 'y' in accessibility.

---

Ok accessibility intro over! **Let's get into the main part of this blog post - how to run automated accessibility checks**...

I'll break this up into a few sections, with a summary at the end of what I recommend for typical apps/organisations.

The following is a list of all the tools and libraries that you can use to run automated tests, as part of your CI/CD workflows.

There is quite a lot listed here, I am by no means suggesting any company should set *all* of these up. But there will be some which are more suitable (depending on your current CI/CD setup - for example you may use Cypress already so using tools that work well with that makes much more obvious sense to look into)

**The only one that I would say should be required in every JS app is to add the ESLint rule for accessibility**, as it can catch things **very quickly and easily**, and will be compatible with almost any Javascript based frontend app!

#### React Testing Library - how it encourages you to think about accessibility

[React Testing Library](https://testing-library.com/docs/)  is a very popular testing library for testing React apps. One of it's [guiding principles](https://testing-library.com/docs/guiding-principles/)  is that it **encourages you to write tests that are more accessibility focused**.

(BTW - a huge chunk of [this website focuses on teaching how to write good quality frontend tests](https://howtotestfrontend.com)  - with a big focus on using React Testing Library!)

It is very common to use RTL to test your React based apps, so hopefully a lot of you are already using this. **But you do have to use the library as it is intended...**

Instead of querying for elements by class names or IDs (which is not how your users interact with your site!), **React Testing Library encourages you to query for elements by their role, label, or text content** - which is much closer to how users (including those using assistive technologies) would interact with your app.

For example, instead of:

```
const button = document.body.querySelector('.submit-btn');
```

React Testing Library encourages you to query with things like `byRole('button')`, `byAltText('dog pictures')` etc.

```
const button = screen.getByRole('button', { name: 'Submit' });
```

This approach **means that if your HTML is not semantically correct** (for example if there is a `<div>` instead of a `<button>`), **then your tests wouldn't work when trying to query semantically** (like with `screen.getByRole('button')`). Which is great - **it highlights an error in your implementation and pushes you to fix it**.

Another example is if you have a form input with something visually to label it (e.g. 'enter your name' as a heading). But if you forget to properly link it with a `<label>`, then screen readers will have issues describing it accurately. If you use React Testing Library's `getByLabelText('enter your email')` then **it will only pass if you have linked up your input to the label** correctly.

There are lots of functions in React Testing Library ([I have a 17 lessons just on these RTL query functions here](/courses/finding-elements-with-react-testing-library-queries)), but here are some examples of common ones:

- `getByRole()` - finds elements by their ARIA role (button, heading, link and so on)
- `getByLabelText()` - finds form input elements by their label
- `getByAltText()` - finds images by their alt text value
- `getByText()` - finds elements by their visible text content

Note: There are other testing libraries and test runners that have a very similar syntax to React
Testing Library (Vitest Browser Mode being the main one that has risen in popularity. A lot of
what I say about React Testing Library applies to them too).

#### Testing keyboard navigation in your tests

The easiest cheat code to making user interaction accessible is to code it in a way that makes it easy to use only keyboards to interact.

By this, I mean that you should be able to navigate your functionality using only the keyboard -
Tab key, Enter key, arrow keys, Escape key, etc.

With React Testing Library you can simulate all of this with their `userEvent` library.

Here's an example of testing keyboard navigation:

```
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('can navigate dropdown with keyboard', async () => {
  const user = userEvent.setup();
  render(<DropdownMenu />);

  const btn = screen.getByRole('button', {
    name: 'Open menu',
  });

  
  await user.tab();
  expect(btn).toHaveFocus();

  
  
  await user.keyboard('{Enter}');

  
  const firstItem = screen.getByRole('menuitem', { name: 'First option' });
  expect(firstItem).toHaveFocus();

  
  await user.keyboard('{ArrowDown}');
  const secondItem = screen.getByRole('menuitem', { name: 'Second option' });
  expect(secondItem).toHaveFocus();

  
});
```

I realise that suggesting everything is tested with keyboard only (in addition to mouse interaction - for example, with `userEvent.click(btn)`) is a lot more hassle.

So realistically you probably won't want to do this everywhere. But for important and complex UI with lots of interaction it is very important. **And using React Testing Library, it is so easy** (just time consuming to write it all out)!

#### Enforce basics with eslint rules from `eslint-plugin-jsx-a11y`

One of the lowest effort ways to get some accessibility checks in your build process in your CI/CD pipeline is to add this excellent ESLint plugin: [eslint-plugin-jsx-a11y](https://www.npmjs.com/package/eslint-plugin-jsx-a11y) .

**What is Eslint?** *(Show details)*

ESLint is a code linting tool which can point out (and automatically fix some) problems with the code.

It is normally used to enforce coding style guidelines and syntax issues.

It doesn't run any code, just looks at your source code to figure out if things are set up correctly

So for example when doing accessibility checks, it can look for all your `input` and check it has a `label` associated with it.

`eslint-plugin-jsx-a11y` is an ESLint plugin for checking your JSX (in your `.tsx` or `.jsx` files).

**It can only catch common & basic accessibility mistakes**. But it is so little effort **I always install it by default when setting up new React (JSX) based projects**.

You can catch things such as:

- Form inputs **without proper labels**
- Incorrect/**invalid ARIA** attributes
- Interactive elements that **aren't keyboard accessible**
- **Missing alt text** on images
- Missing or **incorrect semantic HTML**
- and other similar things

##### Using `axe-core`

[axe-core](https://www.npmjs.com/package/axe-core)  is a very popular accessibility testing engine.

It is created and maintained by [Deque](https://www.deque.com/) , a company that is held in high
regard by the accessibility community

`axe-core` is a JavaScript based library, that can take your HTML and create a report based on rules that you can configure.

You will probably want to use [vitest-axe](https://www.npmjs.com/package/vitest-axe)  or [jest-axe](https://www.npmjs.com/package/jest-axe) , which are wrappers around `axe-core`.

Once set up, you can use it when rendering your React components. Here is an example:

```
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

test('should not have accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

#### Using `react-axe`

You can also use [@axe-core/react](https://www.npmjs.com/package/@axe-core/react)  to run axe-core.

This is **more for manual testing than automated CI**, but worth noting here. Once set up you make sure to only run it on non production builds. Then once it is set up and running, it will console log (in your browser console) accessibility violations.

#### Axe Core with Playwright

**If you use Playwright for your end-to-end tests**, then you can easily use `axe-core` with their [@axe-core/playwright](https://www.npmjs.com/package/@axe-core/playwright)  package.

Once installed, you just need to add a few lines to existing tests to **ensure there are no accessibility violations**.

```
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('check a11y', async ({ page }) => {
  await page.goto('http://localhost:8080');

  const accessibilityScanResults = await new AxeBuilder({
    page,
  }).analyze();

  expect(accessibilityScanResults.violations).toHaveLength(0);
});
```

You can also pass a configuration object to `new AxeBuilder`, to enforce specific WCAG guidelines that you want to enforce.

#### Cypress with axe-core

**If you're using Cypress** for end-to-end testing, you can **add accessibility checks with [cypress-axe](https://www.npmjs.com/package/cypress-axe)** , which like the previous tips above also uses `axe-core`.

After installation, you can add accessibility checks to any Cypress test:

```
it('page loads & no accessibility issues', () => {
  
  
  cy.visit('/');

  
  
  cy.injectAxe();
  
  cy.checkA11y();
});
```

#### Other E2E frameworks

Most modern E2E testing frameworks have similar integrations with axe-core:

The pattern is roughly the same for any of the e2e test runners - inject axe-core into your page during tests and run the analysis against the rendered DOM.

As they are all using the same `axe-core` under the hood, they all tend to report the same accessibility issues.

#### Using Storybook for accessibility checks

![Storybook accessibility addon, with accessibility violations and checks in view](/_next/image?url=%2Fblog-images%2Ftest-a11y-overview.png&w=3840&q=75&dpl=ed29a710fd477d5afc322679d987c612e502a94f62ee0105e9219f39dd55e6b0363964376637643863633132323230303038333065303736)

[Storybook](https://storybook.js.org/)  is a popular tool for developing and documenting UI components. Many big teams with frontend apps use Storybook, so hopefully you're familiar with it.

If you already have Storybook set up, then you can very **easily get it to do accessibility audits on your components as part of your build process**.

You just need to add and configure the [@storybook/addon-a11y](https://www.npmjs.com/package/@storybook/addon-a11y)  addon.

(This - like other tools on this page - uses `axe-core` under the hood. )

The setup is quite minimal - just need to install `@storybook/addon-a11y` as a dependency, then add `'@storybook/addon-a11y'` as a addon in your storybook config. (See the link above for a full set up guide)

Then once you have this installed and configured, when you view your storybook components you will see a new accessibility tab. You can also automate it to **require no violations in your CI/CD checks**.

#### Use Lighthouse (from Google) to automatically report back accessibility issues

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)  is an open-source tool **built directly into Chrome DevTools** that audits web pages for performance, SEO, PWA capabilities, and accessibility.

(If you have ever run accessibility checks from the Chrome dev tools in your browser - this was with a Lighthouse report!)

**They also have a CLI version** with [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) , which you can get running automatically.

In my experience it catches simpler and fewer accessibility issues than axe-core, however it can still be a very useful tool, and debugging (or fixing) the issues can be quite easy as you can often replicate exactly in your Chrome browser.

**If you want to set it up on your CI/CD pipeline, then I'd recommend [this web.dev guide](https://web.dev/lighthouse-ci/)**

#### Pa11y

[Pa11y](https://pa11y.org/)  is a **command-line accessibility testing tool that can load a URL** and report back with accessibility issues that it finds.

Pa11y is **more useful when testing entire websites**, and not specific features within an app. It is also better at testing large amounts of pages (**it can crawl your entire website**/app automatically)

There are basically two ways to use Pa11y

On your local machine, you can run `pa11y https://your-website.com` for an instant accessibility report.

Or use their [pa11y-ci](https://github.com/pa11y/pa11y-ci)  tool to run it against a deployed site (easy with many frontend apps being deployed on Vercel, Netlify etc) and report back in your CI runner (e.g. GitHub Actions etc).

You can configure it to report back against a specific WCAG standard, and get it to ignore some rules

```
{
  urls: [
    'https://your-website.com',
    'https://your-website.com/about',
    'https://your-website.com/contact',
  ],
  standard: 'WCAG2AA',
  ignore: [
    
    'color-contrast',
  ],
}
```

## Manual testing

This blog post is about how to automatically run your tests on CI/CD, but I again **want to emphasise that automated tests can only catch basic violations**.

You still need to be manually checking how usable and accessible your website, app and features are.

Without going into too much detail (after all, this blog post is about automated accessibility testing!), here are some simple manual things you should be checking:

### Test with keyboard navigation only

One of the most important manual tests you can do is to **try using your entire app with only the keyboard**.

**If it is accessible with just a keyboard, then it is likely usable by assistive technology too**. If it isn't usable by a keyboard only, then it is *almost definitely not usable by assistive technology*.

So try to throw away your mouse and avoid a touch screen, just use Tab, Enter, Space, and arrow keys to try to use your app.

BTW you can automate this (as explained above, React Testing Library makes it easy to simulate keyboard events), however nothing beats a real user manually testing it out to confirm it truly does work as you think it does.

### Check focus indicators and visual clarity

When you navigate with just a keyboard, it will be obvious to you if you have missed some focus state. You will tab to an item but it won't be clear what is focused.

**Focus indicators** should be obvious and easy to see. So this means something like an outline when you focus on it.

### Manually testing screen readers

One important part is manually testing how screen readers *actually* work on your app.

There have been tons of times I've been convinced the HTML markup was all correct and useful. And despite being completely valid semantically, as soon as we tested with a real screen reader it was obvious there were usability issues like confusing navigation flows, unclear content relationships, or information that was technically accessible but practically unusable.

The main screen reader systems are these (and they all behave slightly differently so you really do have to test on them all...)

- **VoiceOver (Apple)** on all iOS and Mac devices
- **Narrator (Microsoft)** is built into Windows
- **TalkBack (Android)** is built into Android devices
- **NVDA** is an open-source and popular tool on Windows
- **JAWS** is also popular, only on Windows

Ideally, test on multiple screen readers **as they behave differently**.

At minimum, test on VoiceOver (Mac/iOS) and NVDA or JAWS (Windows). For mobile apps, include TalkBack (Android).

As far as I am aware, there is no automated way to test with real screen readers. The closest you could get is to check that elements have correct labels and text content.

## My recommendations for automating accessibility checks in your projects:

While it is hard to say that there are some tools that should be used for all websites/apps, here is my recommendation for a typical application (assuming a normal JS/React based frontend application).

With these tools in place you can start to get reports in your CI/CD pipelines.

(How to actually triage and address these issues will be a future blog post)

### For Every Project (Minimum Requirements)

- Always use `eslint-plugin-jsx-a11y` as its effort to value is so high
- **If you already use Storybook**, then get the Storybook accessibility add-on set up. Again, because the amount of effort is small, but it has a lot of value
- Don't rely just on automatic tests - manual testing is very important

### In your unit/integration FE tests

If you are testing an React app, **I'd strongly recommend using React Testing Library**. But don't just stop there - make sure you and your team listen to their [guiding principles](https://testing-library.com/docs/guiding-principles/)  to make sure you write tests in a way that encourage good accessibility in the components you're testing.

You should also consider running axe-core against your components that are rendered ([vitest-axe](https://www.npmjs.com/package/vitest-axe)  or [jest-axe](https://www.npmjs.com/package/jest-axe)  - especially for widgets and features with lots of complex UI interaction.

### In your End-to-End (E2E) tests

If you use **Cypress** or **Playwright** to run end-to-end tests, use the packages mentioned previously to automatically run axe-core and report violations.

They are often quite easy to install and configure, and you can be explicit about what tests and what pages you want to run accessibility checks on.

### Against a deployed site

If you use a service like Vercel or Netlify, you probably have 'preview branches' that automatically deploy on each pull-request, so you can preview out your changes.

If that is the case, it **can be really simple to get some very basic accessibility checks on each of these deploys with something like Pa11y**. Tools like that can crawl your site and check the basics, without having to manually set up tests for each page. However, they won't test any interaction.

You can also get a lot of value out of Google Lighthouse - although if you use Netlify for example this is built in to your deploy logs.

![Screenshot of netlify showing google lighthouse report and scores](/_next/image?url=%2Fblog-images%2Fnetlify-google-lighthouse-report.png&w=3840&q=75&dpl=ed29a710fd477d5afc322679d987c612e502a94f62ee0105e9219f39dd55e6b0363964376637643863633132323230303038333065303736)

Using something like pa11y or Google Lighthouse like this can be useful if you have a lot of pages, for example a blog or mostly static content.

---

### I hope that this helped - please get in touch if you have suggestions

I am always keen to try out new tools and services.

If you know of something decent that I've missed **please get in touch** and I will check it out & update this post!

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
