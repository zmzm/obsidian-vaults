---
type: twir-item
issue: 263
item: 1
item_type: featured
date: 2025-12-17
source: https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components
tags:
  - "DoS"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-12-17-TWIR-263|Index]]

# Item 1: Denial of Service and Source Code Exposure in React Server Components

Source: [https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components)

Summary:
The React team disclosed new high- and medium-severity vulnerabilities in React Server Components, including denial of service (DoS) and source code exposure issues. These vulnerabilities affect multiple versions of react-server-dom-* packages and require immediate upgrades, even for users who previously patched for React2Shell. The issues can lead to server crashes or exposure of server function source code, especially if secrets are hardcoded. The React team emphasizes the importance of rapid patching and notes that such follow-up vulnerabilities are common after major security incidents.

Key takeaways:
- Immediate upgrade is required for all users of react-server-dom-webpack, -parcel, and -turbopack in affected versions.
- Previous patches (19.0.3, 19.1.4, 19.2.3) are incomplete; upgrade to 19.0.4, 19.1.5, or 19.2.4.
- DoS vulnerabilities can crash servers or exhaust resources via crafted HTTP requests; source code exposure can leak server function code and hardcoded secrets.
- Frameworks/bundlers like Next.js, react-router, waku, @parcel/rsc, @vite/rsc-plugin, and rwsdk are affected.
- Only apps using React Server Components are impacted; React Native and client-only apps are not affected.

Recommendation:
Read fully (if you maintain or deploy React Server Components)

Why it matters:
if you maintain or deploy React Server Components

Content:
# Denial of Service and Source Code Exposure in React Server Components

December 11, 2025 by [The React Team](/community/team)

*Updated January 26, 2026.*

---

Security researchers have found and disclosed two additional vulnerabilities in React Server Components while attempting to exploit the patches in last week’s critical vulnerability.

**These new vulnerabilities do not allow for Remote Code Execution.** The patch for React2Shell remains effective at mitigating the Remote Code Execution exploit.

---

The new vulnerabilities are disclosed as:

We recommend upgrading immediately due to the severity of the newly disclosed vulnerabilities.

### Note

#### The patches published earlier are vulnerable.

If you already updated for the previous vulnerabilities, you will need to update again.

If you updated to 19.0.3, 19.1.4, and 19.2.3, [these are incomplete](#additional-fix-published), and you will need to update again.

Please see [the instructions in the previous post](/blog/2025/12/03/critical-security-vulnerability-in-react-server-components#update-instructions) for upgrade steps.

---

*Updated January 26, 2026.*

Further details of these vulnerabilities will be provided after the rollout of the fixes are complete.

## Immediate Action Required

These vulnerabilities are present in the same packages and versions as [CVE-2025-55182](/blog/2025/12/03/critical-security-vulnerability-in-react-server-components).

This includes 19.0.0, 19.0.1, 19.0.2, 19.0.3, 19.1.0, 19.1.1, 19.1.2, 19.1.3, 19.2.0, 19.2.1, 19.2.2, and 19.2.3 of:

Fixes were backported to versions 19.0.4, 19.1.5, and 19.2.4. If you are using any of the above packages please upgrade to any of the fixed versions immediately.

As before, if your app’s React code does not use a server, your app is not affected by these vulnerabilities. If your app does not use a framework, bundler, or bundler plugin that supports React Server Components, your app is not affected by these vulnerabilities.

### Note

#### It’s common for critical CVEs to uncover follow‑up vulnerabilities.

When a critical vulnerability is disclosed, researchers scrutinize adjacent code paths looking for variant exploit techniques to test whether the initial mitigation can be bypassed.

This pattern shows up across the industry, not just in JavaScript. For example, after [Log4Shell](https://nvd.nist.gov/vuln/detail/cve-2021-44228), additional CVEs ([1](https://nvd.nist.gov/vuln/detail/cve-2021-45046), [2](https://nvd.nist.gov/vuln/detail/cve-2021-45105)) were reported as the community probed the original fix.

Additional disclosures can be frustrating, but they are generally a sign of a healthy response cycle.

### Affected frameworks and bundlers

Some React frameworks and bundlers depended on, had peer dependencies for, or included the vulnerable React packages. The following React frameworks & bundlers are affected: [next](https://www.npmjs.com/package/next), [react-router](https://www.npmjs.com/package/react-router), [waku](https://www.npmjs.com/package/waku), [@parcel/rsc](https://www.npmjs.com/package/@parcel/rsc), [@vite/rsc-plugin](https://www.npmjs.com/package/@vitejs/plugin-rsc), and [rwsdk](https://www.npmjs.com/package/rwsdk).

Please see [the instructions in the previous post](/blog/2025/12/03/critical-security-vulnerability-in-react-server-components#update-instructions) for upgrade steps.

### Hosting Provider Mitigations

As before, we have worked with a number of hosting providers to apply temporary mitigations.

You should not depend on these to secure your app, and still update immediately.

### React Native

For React Native users not using a monorepo or `react-dom`, your `react` version should be pinned in your `package.json`, and there are no additional steps needed.

If you are using React Native in a monorepo, you should update *only* the impacted packages if they are installed:

- `react-server-dom-webpack`
- `react-server-dom-parcel`
- `react-server-dom-turbopack`

This is required to mitigate the security advisories, but you do not need to update `react` and `react-dom` so this will not cause the version mismatch error in React Native.

See [this issue](https://github.com/facebook/react-native/issues/54772#issuecomment-3617929832) for more information.

---

## High Severity: Multiple Denial of Service

**CVEs:** [CVE-2026-23864](https://www.cve.org/CVERecord?id=CVE-2026-23864)
**Base Score:** 7.5 (High)
**Date**: January 26, 2026

Security researchers discovered additional DoS vulnerabilities still exist in React Server Components.

The vulnerabilities are triggered by sending specially crafted HTTP requests to Server Function endpoints, and could lead to server crashes, out-of-memory exceptions or excessive CPU usage; depending on the vulnerable code path being exercised, the application configuration and application code.

The patches published January 26th mitigate these DoS vulnerabilities.

### Note

#### Additional fixes published

The original fix addressing the DoS in [CVE-2025-55184](https://www.cve.org/CVERecord?id=CVE-2025-55184) was incomplete.

This left previous versions vulnerable. Versions 19.0.4, 19.1.5, 19.2.4 are safe.

---

*Updated January 26, 2026.*

---

## High Severity: Denial of Service

**CVEs:** [CVE-2025-55184](https://www.cve.org/CVERecord?id=CVE-2025-55184) and [CVE-2025-67779](https://www.cve.org/CVERecord?id=CVE-2025-67779)
**Base Score:** 7.5 (High)

Security researchers have discovered that a malicious HTTP request can be crafted and sent to any Server Functions endpoint that, when deserialized by React, can cause an infinite loop that hangs the server process and consumes CPU. Even if your app does not implement any React Server Function endpoints it may still be vulnerable if your app supports React Server Components.

This creates a vulnerability vector where an attacker may be able to deny users from accessing the product, and potentially have a performance impact on the server environment.

The patches published today mitigate by preventing the infinite loop.

**CVE:** [CVE-2025-55183](https://www.cve.org/CVERecord?id=CVE-2025-55183)

A security researcher has discovered that a malicious HTTP request sent to a vulnerable Server Function may unsafely return the source code of any Server Function. Exploitation requires the existence of a Server Function which explicitly or implicitly exposes a stringified argument:

```
'use server';

export async function serverFunction(name) {

const conn = db.createConnection('SECRET KEY');

const user = await conn.createUser(name);

return {

id: user.id,

message: `Hello, ${name}!`

}}
```

An attacker may be able to leak the following:

```
0:{"a":"$@1","f":"","b":"Wy43RxUKdxmr5iuBzJ1pN"}

1:{"id":"tva1sfodwq","message":"Hello, async function(a){console.log(\"serverFunction\");let b=i.createConnection(\"SECRET KEY\");return{id:(await b.createUser(a)).id,message:`Hello, ${a}!`}}!"}
```

The patches published today prevent stringifying the Server Function source code.

### Note

#### Only secrets in source code may be exposed.

Secrets hardcoded in source code may be exposed, but runtime secrets such as `process.env.SECRET` are not affected.

The scope of the exposed code is limited to the code inside the Server Function, which may include other functions depending on the amount of inlining your bundler provides.

Always verify against production bundles.

---

## Timeline

- **December 3rd**: Leak reported to Vercel and [Meta Bug Bounty](https://bugbounty.meta.com/) by [Andrew MacPherson](https://github.com/AndrewMohawk).
- **December 4th**: Initial DoS reported to [Meta Bug Bounty](https://bugbounty.meta.com/) by [RyotaK](https://ryotak.net).
- **December 6th**: Both issues confirmed by the React team, and the team began investigating.
- **December 7th**: Initial fixes created and the React team began verifying and planning new patch.
- **December 8th**: Affected hosting providers and open source projects notified.
- **December 10th**: Hosting provider mitigations in place and patches verified.
- **December 11th**: Additional DoS reported to [Meta Bug Bounty](https://bugbounty.meta.com/) by Shinsaku Nomura.
- **December 11th**: Patches published and publicly disclosed as [CVE-2025-55183](https://www.cve.org/CVERecord?id=CVE-2025-55183) and [CVE-2025-55184](https://www.cve.org/CVERecord?id=CVE-2025-55184).
- **December 11th**: Missing DoS case found internally, patched and publicly disclosed as [CVE-2025-67779](https://www.cve.org/CVERecord?id=CVE-2025-67779).
- **January 26th**: Additional DoS cases found, patched, and publicly disclosed as [CVE-2026-23864](https://www.cve.org/CVERecord?id=CVE-2026-23864).

---

## Attribution

Thank you to [Andrew MacPherson (AndrewMohawk)](https://github.com/AndrewMohawk) for reporting the Source Code Exposure, [RyotaK](https://ryotak.net) from GMO Flatt Security Inc and Shinsaku Nomura of Bitforest Co., Ltd. for reporting the Denial of Service vulnerabilities. Thank you to [Mufeed VH](https://x.com/mufeedvh) from [Winfunc Research](https://winfunc.com), [Joachim Viide](https://jviide.iki.fi), [RyotaK](https://ryotak.net) from [GMO Flatt Security Inc](https://flatt.tech/en/) and Xiangwei Zhang of Tencent Security YUNDING LAB for reporting the additional DoS vulnerabilities.

Related notes: [[Server Components]]
