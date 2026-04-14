---
type: twir-item
issue: 255
item: 3
item_type: item
date: 2025-10-22
source: https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey-part-3
tags:
  - "2025"
  - "Nextjs"
status: auto
quality: keep
---

[[2025-10-22-TWIR-255|Index]]

# Item 3: The Pragmatic Engineer 2025 Survey

Source: [https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey-part-3](https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey-part-3)

Summary:
The survey analyzes tool usage among 3,000+ engineers, with React confirmed as the dominant frontend framework and Next.js as the leading meta-framework. The report covers observability, oncall, feature flags, developer tools, and custom/niche solutions, but React-specific insights are limited to its continued popularity.

Key takeaways:
- React remains the most popular frontend framework; Next.js leads as a meta-framework.
- React Native is the top cross-platform mobile solution.
- The survey covers a broad range of tooling, with React's dominance unchallenged in frontend.
- Useful for benchmarking stack choices or justifying React/Next.js adoption.

Recommendation:
Summary sufficient (full article valuable for broader tooling context, not React-specific details)

Why it matters:
full article valuable for broader tooling context, not React-specific details

Content:
# The Pragmatic Engineer 2025 Survey: What’s in your tech stack? Part 3

---

During April and May, we asked readers which tools you use in your stack, and your opinions of them. Previous articles in this mini-series about the results of that survey have focused on AI-related tools, IDEs, and CI/CD [in Part 1](https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey), while [Part 2](https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey-part-2) covered project management, collaboration tools, databases, and backend-related tools.

In the third and final part of this dive into the feedback, we cover:

1. **Observability, monitoring, and logging.** Grafana, Datadog, and Sentry all stand out, with a long list of open source tools and vendors offering observability platforms.
2. **Oncall tooling and incident management.** PagerDuty and OpsGenie remain the most-used solutions, but young startups like incident.io, Rootly, and FireHydrant are challenging them.
3. **Feature flags, analytics, and experimentation.** LaunchDarkly is the most-used solution, with a long tail of analytics, experimentation, and feature flag vendors.
4. **Frontend and mobile tooling.** React is the most popular frontend framework, and Next.js is the most popular “meta frontend framework”. React Native is the most-mentioned cross-platform mobile framework. In these categories, it’s not even a contest.
5. **Developer tools.** Postman is popular for API development, Sonar for static analysis, and Backstage for developer portals.
6. **Custom-built tools.** Feature flagging, A/B testing, and CI/CD systems are the most common reasons to build custom tools.
7. **Niche tools readers love.** Lesser mentioned tools that are highly rated by readers, like Tuple (remote pair programming), Tmux (terminal multiplexer), Ansible (infrastructure automation), and many others.

As mentioned, check out more on the latest survey results in other articles, including:

**[Part 1:](https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey)**

- Demographics
- AI tools
- Most used, most-loved programming languages
- Most hated (and loved) tools
- IDEs and terminals
- Version control and CI/CD
- Cloud providers, IaaS, and PaaS

**[Part 2:](https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-2025-survey-part-2)**

- Most-mentioned tools
- Project management
- Communication and collaboration
- Databases and data stores
- Backend infrastructure
- Load balancers
- Forks of popular open-source projects

The leading observability vendor in this space, Datadog, was founded in 2010 with a focus on server and infrastructure monitoring: collecting metrics from servers, cloud instances, and with AWS as a focal point. Since then, Datadog has continued adding new products, and now supports dozens of features from APM (Application Performance Monitoring – distributed tracing, service maps), through RUM (Real User Monitoring – frontend performance, user sessions), to CI/CD visibility (pipeline monitoring, test analytics), and dozens more products. Datadog lists more than 50 on its website, and most are integrated to work together.

Other platforms are similar: they started with a narrow focus, added more capabilities, and became the full-blown platforms of today. A good example is Sentry: it started in 2008 as an open source monitoring tool for the Django platform in Python, then got incorporated in 2015 as a company, and today has products for APM (Application Performance Monitoring), error monitoring, session replay, and more.

With the caveat that comparing vendors in this crowded space is no simple task, below are listed the most-mentioned observability platforms by 3,000 respondents. (Thanks again to everyone who filled in the survey!):

Observability platforms, ranked by readers

**Open source tools:** several of these tools are open source (meaning they have permissive licenses):

- **[Grafana](https://grafana.com)**: an open source tool for displaying dashboards for observability. It’s often used with Prometheus, Elasticsearch, and other backend observability databases. *Grafana Labs (creator of the project) offers a managed service and additional products like Loki and Tempo.*
- **[Prometheus](https://prometheus.io)**: an open-source metrics monitoring system originally built at SoundCloud. It’s the de facto standard for Kubernetes monitoring, and often paired with Grafana for visualization.
- **[The ELK stack:](https://www.elastic.co/elastic-stack)** this stands for “Elasticsearch, Logstash, Kibana”, also known as the “Elastic stack”. These tools are designed to work with one another. Elasticsearch and Kibana moved from being open source [in 2021](https://newsletter.pragmaticengineer.com/i/149455064/elasticsearch-stops-being-open-source) to a more restrictive license, before returning to open source [in 2024](https://newsletter.pragmaticengineer.com/i/149455064/elasticsearch-unexpectedly-goes-open-source-again). Logstash has always been open source. *In the survey, we saw 102 mentions of Kibana, 90 for Elasticsearch, 78 for the ELK stack, and 16 for Logtash. We assumed all mentions refer to the ELK stack. In an earlier version of this article, we separated these: this has now been updated.*
- **[OpenTelemetry](https://opentelemetry.io)**: an open-source observability framework providing standardized APIs, SDKs, and tools for instrumenting applications to collect traces, metrics, and logs.
- **[Elasticsearch](https://www.elastic.co/elasticsearch)** is an open-source distributed search and analytics engine, designed for storing and querying large volumes of data in near-real time.
- **[Loki](https://grafana.com/oss/loki/)**: an open-source log aggregation system created by Grafana Labs, inspired by Prometheus and designed for logs, instead of metrics. Integrates nicely with Grafana for visualization and with Prometheus for unified observability.
- **[Tempo](https://grafana.com/oss/tempo/)**: an open-source distributed tracing backend that’s designed for massive scale and cost-effectiveness by Grafana Labs. It integrates nicely with Grafana and Prometheus.
- **[Jaeger](https://www.jaegertracing.io)**: an open-source distributed tracing system originally developed by Uber for monitoring microservices-based architectures. Commonly used as a backend for OpenTelemetry tracing data.
- **[Zabbix](https://www.zabbix.com)**: an open-source enterprise monitoring solution for networks, servers, and infrastructure components that’s popular in more traditional environments.
- **[SigNoz](https://signoz.io)**: an open-source, full-stack observability platform that provides APM (Application Performance Monitoring), distributed tracing, metrics, and logs in a single application. Built as an open-source alternative to commercial platforms like Datadog or New Relic, using OpenTelemetry for instrumentation.

Grafana coupled with Prometheus is a popular combination for companies to build an in-house observability stack. This is [what Shopify did](https://newsletter.pragmaticengineer.com/i/120772763/will-shopify-migrate-onto-an-in-house-observability-tool) when it moved off Datadog – and it was also the stack which Coinbase built after receiving an eye-watering $65M bill from Datadog [in 2023.](https://newsletter.pragmaticengineer.com/p/the-scoop-47)

Some vendors and solutions in the observability platforms table above are not permissive open source (several of them have source-available licenses):

- **[Datadog](https://www.datadoghq.com)**: the market-leading observability vendor.
- **[Sentry](https://sentry.io)**: an error tracking and application monitoring platform (APM).
- **[New Relic](https://newrelic.com)**: a full-stack observability platform. In 2023, New Relic [published a blog post](https://newsletter.pragmaticengineer.com/i/136371856/new-relic-explained-why-private-equity-buying-a-vendor-is-bad-for-customers-then-it-was-bought-by-one) saying customers should consider leaving vendors acquired by private equity (PE). As fate would have it, 6 months later [it was acquired by PE](https://newsletter.pragmaticengineer.com/i/136371856/new-relic-explained-why-private-equity-buying-a-vendor-is-bad-for-customers-then-it-was-bought-by-one).
- **[Splunk](https://www.splunk.com)**: another fullstack observability platform.
- **[AWS CloudWatch](https://aws.amazon.com/cloudwatch/)**: AWS’s native monitoring and observability service.
- **[Kibana](https://www.elastic.co/kibana)**: an open source tool for dashboards, charts, and maps. Often used with an Elasticsearch backend.
- **[Honeycomb](https://www.honeycomb.io)**: an observability platform designed for debugging complex distributed systems with [high-cardinality](https://docs.honeycomb.io/get-started/basics/observability/concepts/high-cardinality/) analysis and exploratory queries.
- **[Dynatrace](https://www.dynatrace.com)**: a software intelligence platform providing automatic observability across applications and infrastructure.
- **[Graylog](https://www.graylog.org)**: a source-available log management platform, positioned as a more user-friendly, cost-effective alternative to Splunk and ELK Stack.
- **[Logstash](https://www.elastic.co/logstash)**: a source-available data processing pipeline. It’s the “L” in ELK Stack, and handles the collection and enrichment layer of log management.
- **[Coralogix](https://coralogix.com)**: observability platform that focuses on real-time analytics and cost optimization.
- **[Papertrail](https://www.papertrail.com)**: a cloud-based log management service. Popular with smaller teams and startups looking for simple log management.
- **[Sumo Logic](https://www.sumologic.com)**: a SaaS platform for log management, observability, and security.
- **[Chronosphere](https://chronosphere.io/)**: an observability platform purpose-built for microservices and containerized environments, with a focus on cost efficiency. We previously covered [how Chronosphere is built,](https://newsletter.pragmaticengineer.com/p/chronosphere) with cofounder and CEO Martin Mao.
- **[Airbrake](https://airbrake.io)**: an error monitoring and application performance tracking tool (APM).

Incident management-related tools mentioned by readers

Tools which readers use:

- **[PagerDuty](https://www.pagerduty.com)**: market leader in incident response and on-call management.
- **[Opsgenie](https://www.atlassian.com/software/opsgenie)**: Atlassian’s on-call management and alerting. In 2022, OpsGenie [was fully down for 2 weeks](https://newsletter.pragmaticengineer.com/p/scoop-atlassian) for hundreds of customers during Atlassian’s longest-ever outage.
- **[incident.io](https://incident.io)**: oncall, incident response, and status pages *(note: [I’m an investor](https://blog.pragmaticengineer.com/investing/)).*
- **[Grafana IRM](https://grafana.com/products/cloud/irm/)**: incident response and management built into the Grafana stack
- **[Rootly](https://rootly.com)**: a Slack-native incident management platform.
- **[FireHydrant](https://firehydrant.com)**: an incident management platform.
- **[Pingdom](https://www.pingdom.com)**: an uptime monitoring and website performance tool. While primarily a monitoring tool, it’s often used as part of oncall workflows for uptime tracking.
- **[Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/)**: the alerting component of the Prometheus ecosystem that handles alerts from Prometheus servers and routes them to appropriate receivers. Popular in Kubernetes environments as part of the Prometheus monitoring stack.
- **[VictorOps](https://www.splunk.com/en_us/products/on-call.html)**: an incident management platform, today called ‘Splunk On-Call’ after Splunk acquired it.
- **[Squadcast](https://www.squadcast.com)**: an incident management platform. It positions itself as an affordable alternative to PagerDuty.
- **[Statuspage](https://www.atlassian.com/software/statuspage)**: Atlassian’s status page solution to communicate service status and incidents to customers.

**A new generation of incident management tools appears to be challenging the old guard.** PagerDuty was founded in 2009 and OpsGenie in 2012, and these two tools are still the most mentioned in our survey. However, a group of startups is emerging as challengers:

What seems to have shaken things up and helped the “new generation” of incident management startups spread, was PagerDuty and OpsGenie being slow to add support for handling incidents inside Slack. incident.io, Rootly, and FireHydrant gained initial momentum by offering this.

Today, pretty much all the above oncall tooling vendors describe themselves on their landing pages as “AI platforms” or “AI-first operations platforms”, as they’re experimenting with new features built on top of LLMs like incident summaries, or taking a first stab at root cause analysis using LLMs.

*Note: the above list was updated on 18 October 2025, adding Grafana IRM, which we incorrectly omitted in the original version.*

Shipping features behind a feature flag and A/B testing features are common practices for products with many users. The tools most mentioned in this category:

*Most-mentioned feature flag and experimentation products*

Vendors cited:

- **[LaunchDarkly](https://launchdarkly.com)**: the clear leader in feature flag management. Supports things like progressive delivery with percentage-based rollouts, kill switches, and more.
- **[Amplitude](https://amplitude.com)**: a product analytics platform that helps teams understand user behavior. It’s an experimentation platform that supports feature flags.
- **[Mixpanel](https://mixpanel.com)**: a product analytics platform focused on tracking user interactions and analyzing product usage.
- **[PostHog](https://posthog.com)**: an open-source product analytics platform that combines analytics, feature flags, session replay, and experimentation in one place. It can be self-hosted or used as a cloud service.
- **[Unleash](https://www.getunleash.io)**: an open-source feature flag management platform that can be self-hosted or used as a managed service.
- **[Statsig](https://statsig.com)**: a feature management and experimentation platform founded by former Meta engineers who built Facebook’s experimentation infrastructure. It was acquired by OpenAI for $1B, last month.
- **[GrowthBook](https://www.growthbook.io)**: an open-source feature flagging and experimentation platform.
- **[Optimizely](https://www.optimizely.com)**: an experimentation platform targeting enterprise customers.
- **[Flagsmith](https://www.flagsmith.com)**: an open-source feature flag and remote config platform that can be self-hosted or used as a managed service.
- **[Harness](https://www.harness.io)**: a software delivery platform that includes feature flags as part of a broader continuous delivery and DevOps suite.
- **[ConfigCat](https://configcat.com)**: a feature flag service focused on simplicity and transparent pricing. Popular with smaller teams and startups looking for an easy-to-use feature management tool.
- **[Split](https://www.split.io)**: a feature delivery platform combining feature flags with detailed impact analysis and experimentation capabilities.

**Feature flags are the most likely tool to be built in-house**, as we’ll see in the “Custom tools” section below.

The most-used frontend frameworks by respondents to our survey:

*Most-mentioned frontend frameworks*

React continues to be the most popular by far, and not much has changed since 2022 when 76% of web developers used it, as we covered at the time in the [State of Frontend 2022](https://newsletter.pragmaticengineer.com/p/state-of-frontend-2022).

“Meta frameworks” are frameworks built on top of one of the above technologies. They add features like server-side rendering (SSR), static site generation (SSG), routing, data fetching, and other features that most production applications need, but which core frameworks don’t provide.

The most popular meta frameworks in the responses:

- **[Next.js](https://nextjs.org/)** (163 mentions): a React framework that provides server-side rendering, static site generation, API routes, and automatic code splitting out of the box. Built by Vercel.
- **[Nuxt](https://nuxt.com/)** (29 mentions): a Vue.js framework that provides server-side rendering, static site generation, and automatic routing.
- **[Remix](https://remix.run/)** (24 mentions): a full-stack React framework focused on web standards, progressive enhancement, and optimized data loading.
- **[Astro](https://astro.build/)** (16 mentions): a modern static site builder that ships zero JavaScript by default, and supports using multiple frameworks in one project.

**CSS frameworks and styling:**

- **[Tailwind CSS](https://tailwindcss.com/)** (170 mentions): provides low-level utility classes for building custom designs without writing custom CSS. Seems to be becoming the preferred choice for many frontend teams.
- **[Bootstrap](https://getbootstrap.com/)** (52 mentions): a popular CSS framework providing pre-built responsive components, utilities, and a flexible grid system based on Flexbox.
- **[Material-UI (MUI)](https://mui.com/)** (44 mentions): a React component library implementing Google’s Material Design specification.
- **[Sass/SCSS](https://sass-lang.com/)** (29 mentions): Sass is a CSS preprocessor that extends CSS with variables, nesting, [mixins](https://en.wikipedia.org/wiki/Mixin), and functions for more maintainable stylesheets. SCSS syntax is CSS-compatible, and it compiles to standard CSS.

**Package managers:**

- **[npm](https://www.npmjs.com/)** (34 mentions): the default package manager for [Node.js](http://node.js), which also happens to be the world’s largest software registry.
- **[pnpm](https://pnpm.io/)** (16 mentions): a fast, disk-space efficient, package manager. It saves significant disk space by sharing packages across projects. It’s getting more popular among developers and companies with large monorepos and multiple projects.
- **[yarn](https://yarnpkg.com/)** (13 mentions): a fast, reliable, and secure package manager developed by Meta. Popular for larger projects and monorepos.

**Build tools**:

- **[Vite](https://vitejs.dev/)** (75 mentions): a modern build tool with extremely fast development server startup.
- **[Webpack](https://webpack.js.org/)** (20 mentions): formerly the industry-standard bundler. It’s less popular since faster build tools like Vite and Bun appeared.
- **[Bun](https://bun.sh/)** (14 mentions): a very fast, all-in-one, JavaScript runtime, bundler, test runner, and package manager written in the programming language of Zig. It offers dramatically faster performance than npm (for package management) and webpack (for builds).

**Testing tools:**

- **[Playwright](https://playwright.dev/)** (36 mentions): a modern end-to-end testing framework by Microsoft supporting multiple browsers (Chromium, Firefox, WebKit) with a single API.
- **[Jest](https://jestjs.io/)** (31 mentions): a JavaScript testing framework developed by Meta
- **[Cypress](https://www.cypress.io/)** (22 mentions): an end-to-end testing framework with time-travel debugging and automatic waiting.
- **[Vitest](https://vitest.dev/)** (20 mentions): a very fast unit test framework powered by Vite. Increasingly the preferred testing framework for Vite projects and modern JavaScript applications.

**CDNs:** content delivery networks (CDNs) speed up web and mobile applications by caching frequently accessed resources like images and video streams. There are three major players in this field: Cloudflare, Fastly, and Akamai. This is how they compare, based on mentions by 114 respondents:

*Split of mentions: Cloudflare (100 mentions), Fastly (7) and Akamai (7)*

In the survey, there’s an almost equal number of engineers working with iOS (400 mentions) as on Android (398 mentions) – a remarkably even split!

*An almost exactly even split between devs working with iOS and those working with Android*

The most popular iOS languages and frameworks, by number of mentions:

- **[Swift](https://www.swift.org/)**: Apple’s modern programming language for iOS, macOS, watchOS, and tvOS development, replacing Objective-C. Five times more developers say they use Swift (162) than who use Objective C (32)
- **[Xcode](https://developer.apple.com/xcode/)**: Apple’s IDE for creating apps across all its platforms. It includes code editors, debugging tools, Interface Builder, simulators, and testing frameworks in one comprehensive package. An essential tool for iOS and macOS developers.
- **[SwiftUI](https://developer.apple.com/xcode/swiftui/)**: Apple’s declarative framework for building user interfaces across all its platforms with Swift code. It enables faster development with live previews, automatic dark mode support, and seamless integration with existing UIKit apps. Rapidly gaining adoption since its 2019 release, especially for new projects.
- **[Objective C](https://en.wikipedia.org/wiki/Objective-C)**: increasingly replaced by Swift when building iOS applications.

Most-mentioned Android languages and frameworks:

- **[Kotlin](https://kotlinlang.org/)**: the preferred programming language for modern Android development. Google announced it as its preferred language for Android in 2019.
- **[Java](https://www.java.com/en/)**: increasingly replaced by Kotlin for modern Android development.
- **[Android Studio](https://developer.android.com/studio)**: Google’s official IDE for Android development, built on IntelliJ IDEA.
- **[Jetpack Compose](https://developer.android.com/jetpack/compose)**: Android’s modern declarative UI toolkit for building native interfaces with Kotlin.

The most commonly mentioned cross-platform frameworks in our survey:

*React Native is the most popular cross-platform framework among respondents*

Based on this data, React Native is the most popular choice for cross-platform development among respondents at startups, scaleups, and in Big Tech. This mirrors what we see with startups and scaleups choosing React Native more often. It’s more popular than Flutter in the US and UK, as we cover in the deepdive, [Cross-platform mobile development](https://newsletter.pragmaticengineer.com/p/cross-platform-mobile-development).

**API developer tools:**

- **[Postman](https://www.postman.com/)** (105 mentions): an API development platform to design, test, document, and monitor APIs.
- **[Insomnia](https://insomnia.rest/)** (8 mentions): a REST and GraphQL client to test and debug APIs.
- **[cURL](https://curl.se/)** (7 mentions): a tool to make API requests from the command line
- **[Bruno](https://www.usebruno.com/)** (6 mentions): an API client that is Git-integrated, fully offline, and open-source

**API gateways:** these handle tasks like authentication, request routing, rate limiting, and monitoring. Common ones mentioned:

- **[AWS API Gateway](https://aws.amazon.com/api-gateway/)** (90 mentions): an AWS service that acts as a reverse proxy to accept all API calls, aggregate various services, and return the appropriate result.
- **[Kong](https://konghq.com/)** (48 mentions): an open-source API gateway and microservices management layer.
- **[GCP Apigee](https://cloud.google.com/apigee)** (26 mentions): Google’s full-lifecycle API platform to design, secure, deploy, monitor, and scale APIs.
- **[Apache APISIX](https://apisix.apache.org/)** (5 mentions): an open source, high-performance API gateway.

Sonar stands out as the most-oft mentioned tool for static analysis:

Tools that readers include in their responses:

- **[Sonar/SonarQube](https://www.sonarsource.com/)**: a code quality and security analysis platform.
- **[Snyk](https://snyk.io/)**: a platform that scans code, dependencies, containers, and infrastructure-as-code, for vulnerabilities.
- **[ESLint](https://eslint.org/)**: a linting tool for JavaScript and TypeScript to catch potential errors, and enforce coding standards.
- **[Prettier](https://prettier.io/)**: an opinionated code formatter that enforces a consistent coding style.
- **[Ruff](https://docs.astral.sh/ruff/)**: a fast Python linter and code formatter written in Rust.
- **[Checkmarx](https://checkmarx.com/)**: static application security testing.
- **[Mypy](https://mypy-lang.org/)**: a static type checker for Python.
- **[Trivy](https://trivy.dev/)**: a security scanner for containers to detect vulnerabilities and misconfiguration.
- **[PHPStan](https://phpstan.org/)**: static analysis tool for PHP.
- **[RuboCop](https://rubocop.org/)**: static code analyzer and code formatter for Ruby.

As teams grow, developer portals start to become useful for service discovery and API directories. The most frequently mentioned tools in our survey with this functionality:

- ***[ServiceNow](https://www.servicenow.com/)** (56 mentions): devs use ServiceNow for ticketing (instead of e.g., JIRA), on-call (an alternative to things like PagerDuty), and service management (rather than Backstage, for example). Survey responses are somewhat negative about ServiceNow’s complexity, but it is the go-to solution in large enterprises for Information and Communication Technology (ICT) management, as it allows setting up custom workflows, and supports clear audit trails.*
- **[Backstage](https://backstage.io/)** (48 mentions): an open source platform by Spotify for building developer portals, and to offer a unified frontend for all infrastructure tooling and services. *We published a [deepdive into Backstage.](https://newsletter.pragmaticengineer.com/p/backstage)*
- **Custom-built internal developer portals** (17 mentions): internally-built developer portals, usually made by internal platform teams for use in things like managing home-grown feature flags and deploying systems.
- **[Compass](https://www.atlassian.com/software/compass)** (9 mentions): Atlassian’s developer experience platform that allows tracking engineering output and health. Offers service catalogs, scorecards, and metrics to understand software quality and developer productivity.

GitHub, GitLab, and Bitbucket all have code review functionality, but readers tell us about other smaller tools which they rate for their code review capabilities:

- **[Graphite](https://graphite.dev/)** (43 mentions): a modern code review tool that supports stacked pull requests and faster code reviews with a command-line interface, and now with AI code review as well.
- **[CodeRabbit](https://coderabbit.ai/)** (13 mentions): an AI-powered code review assistant that automatically reviews pull requests and provides AI-augmented feedback.
- **[Gerrit](https://www.gerritcodereview.com/)** (12 mentions): an open source, web-based code review tool originally developed for Android, which integrates nicely with Git.
- **[Phabricator](https://www.phacility.com/phabricator/)** (10 mentions): an open-source suite of web-based software development collaboration tools originally created by Meta. It has not been maintained since 2021, but a few companies still use it via forks like **[Phorge](https://we.phorge.it/)**.

Graphite, Gerrit, and Phabricator all support the stacked diff workflow. We covered more on why this is a useful way to work in the deepdive, [Stacked Diffs (and why you should know about them)](https://newsletter.pragmaticengineer.com/p/stacked-diffs?utm_source=publication-search).

We asked readers what kind of home-grown or custom tools their team or company uses. And your responses are varied! Here’s a summary of the most popular custom-built tools mentioned in the survey:

*Word cloud of home-grown / custom-built tools used by readers*

What stands out:

- **Feature flagging.** According to our survey, the type of system that’s most often custom-built in house is for feature flagging. I’d speculate this is because it’s easy to build a first version, and vendors can be expensive. Of course, *maintaining* such systems is where things get tricky, but large-enough companies can have a platform team own it.
- **A/B testing and experimentation.** Another common mention. Integrating A/B testing into internal systems – such as tools for the data team to analyze results, or to integrate with the feature flag system – is a common reason to build in-house.
- **CI/CD systems**. Using custom continuous integration / continuous deployment systems is common enough, although it’s more common to integrate software like [Jenkins](https://www.jenkins.io/) and run it on existing infrastructure, instead of building “truly” custom software.
- **Logging systems**: another pretty common mention. As with feature flags, it’s easy enough to write your own – at least in the beginning.

To close, let’s spotlight some lesser-mentioned tools that some respondents say they love. Why not consider giving them a spin when facing a problem they might solve?

**[Tuple](https://tuple.app/):** remote pair programming app

> “Tuple is amazing! I work fully remotely and my team pair on everything, so good tooling for remote pairing is essential. The video quality is great, I never have problems with screen resolution (which I do when sharing my large monitor on Google Meet, when my colleague is viewing on a laptop screen). It’s easy to point at things, annotate your pair’s screen, and even take control when you need to”. – Senior engineer at a mid-sized company.

**[Tmux](https://www.redhat.com/en/blog/introduction-tmux-linux):** a terminal multiplexer

> “Tmux makes my work extremely efficient. I want to fire up a server, open a new window or a pane, query my database, and open a new pane. I can do whatever I want without moving my eyes from the screen and my hands from the keyboard”. – Senior engineer at a startup.

**[Ansible](https://www.redhat.com/en/ansible-collaborative)**: infrastructure automation

> “Ansible lets me ‘do stuff’ to multiple hosts all at once. It’s great!” – Senior security enginee

... (content truncated)
