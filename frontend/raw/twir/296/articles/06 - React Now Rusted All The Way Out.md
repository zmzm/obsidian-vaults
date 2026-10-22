---
type: twir-item
issue: 296
item: 6
item_type: item
date: 2026-09-09
source: https://blog.master.dev/react-now-rusted-all-the-way-out/
tags:
  - "ReactCompiler"
  - "Vite"
status: auto
quality: keep
---

[[2026-09-09-TWIR-296|Index]]

# Item 6: React Now Rusted All The Way Out

Source: [https://blog.master.dev/react-now-rusted-all-the-way-out/](https://blog.master.dev/react-now-rusted-all-the-way-out/)

Summary:
A production React codebase (Outlyne) switched to the Rust-based React Compiler, seeing a ~17× speedup in compilation and a 2.4× overall build time improvement. The Rust compiler, now supported in @vitejs/plugin-react and via a minimal plugin, removes many limitations of the earlier Babel-based compiler and brings improved JS support and toolchain consistency. The post details migration steps for both standard and framework-mode Vite setups, and highlights remaining limitations and the benefits of unified lint/build pipelines.

Key takeaways:
- Rust React Compiler offers dramatic speedups over Babel, especially for large codebases.
- New compiler removes prior JS limitations (e.g., try/catch logic, computed property keys), with some edge cases still unsupported.
- Toolchain consistency: lint and build now use the same compiler, reducing coverage gaps.
- Migration is straightforward for Vite users; alternative plugin available for React Router framework mode.

Recommendation:
Read fully (for teams considering build performance improvements or migrating to the Rust React Compiler)

Why it matters:
for teams considering build performance improvements or migrating to the Rust React Compiler

Content:
# React Now Rusted All The Way Out

Following the oxc team’s release of [official support](https://www.npmjs.com/package/oxc-transform-react) for the Rust React Compiler on August 4, 2026, we switched our 1,036-file React Router codebase ([Outlyne](https://outlyne.com), a website builder) over to it and saw a ~17.6× speedup on the compiler portion of our build.

The [v6.1.0 release of](https://github.com/vitejs/vite-plugin-react/releases/tag/plugin-react%406.1.0) `@vitejs/plugin-react` brought “experimental native React Compiler support”, which you can opt in to by passing `{ compiler: true }` to the plugin in your Vite config. And for those unable to use the Vite React plugin (e.g. if, like us, you’re using React Router in framework mode), `@acusti/vite-plugin-react-compiler` is a minimal Vite plugin to React-compile your codebase regardless of the rest of your build pipeline.

## Faster Builds = Happier Devs + Cheaper CI

The headline feature of this change is the speedup. [Per Boshen](https://oxc.rs/blog/2026-08-18-react-compiler-support.html), the oxc project lead:

> It is more than 10 times faster than Babel in our preliminary benchmark.

We saw more than a 17× speedup, with 1,036 files going from 14.3s when built with Babel to 0.81s natively (single-threaded). This is huge for us because, with the speed of change brought about by agent-assisted software development, CI usage and GitHub Actions minutes have become a real cost center, and waiting on CI is a bummer and puts further pressure on our already overly fragmented task-management brains.

Note that those speedups apply only to the compiler part of the build process. You likely have a lot of other stuff going on during the build, so the overall build time improvement won’t be nearly as dramatic. In our case, the build got around 2.4× faster (22.1s → 9.3s).

## What about React Compiler’s limitations?

```
export default function Foo({ value }: { value: null | string }) {
  value = value ?? "this is a fallback";
  return <button onClick={() => console.log(value)}>{value}</button>;
}Code language: JavaScript (javascript)
```

Skipped before, fully supported now. A third common pattern that caused bailouts in the Babel compiler that’s now supported is computed object property keys, e.g.:

```
import { clsx } from "clsx";

export default function Header({ itemCount }: { itemCount: number }) {
  return (
    <header className={clsx({ [`items-${itemCount}`]: itemCount > 0 })}>
      {/* ... */}
    </header>
  );
}Code language: JavaScript (javascript)
```

Those fixes mean that the new version expands compiler compatibility in our app by an additional seven functions: five thanks to the try/catch improvement, two thanks to computed object property keys. To be clear, there are still limitations to what it supports. The two patterns that I have come across that will still cause the compiler to skip a component/hook are a `throw` from inside a `try` block and logical assignment operators (`??=`, `&&=`, `||=`). But being on the Rust compiler means you will get those fixes when they land. No such luck if you’re stuck on the dead-end Babel-based compiler.

## Toolchain Consistency Means No Coverage Gaps

The final reason I’m excited about switching my build over is that my full toolchain is now using the same version of React Compiler with equivalent feature support. After adopting Oxlint’s React Compiler support while still on an earlier version of React Compiler for my build, I filed an [erroneous issue in oxc](https://github.com/oxc-project/oxc/issues/25910) based on the destructured component prop bailout I described earlier, because the component wasn’t optimized during build but also didn’t trigger a lint error, so I thought there was a lint disconnect with the compiler output. Turns out the issue was that Oxlint was using `oxc-transform-react` v0.145.0, which supports that pattern, whereas I was testing with v0.144.0 of the same package.

Now, linter and build use the exact same React Compiler, with the same improvements and limitations, so we don’t have to worry about uncompiled components slipping into our production build.

## How to Use It

### Using `@vitejs/plugin-react`

As long as you’re on Vite v8+, switching an existing React Vite build to native React Compiler really just means simplifying it. The current Babel-based [react.dev instructions](https://react.dev/learn/react-compiler/installation#vite) specify to run:

```
npm install -D @rolldown/plugin-babelCode language: Bash (bash)
```

With the following Vite config:

```
// vite.config.js
import { defineConfig } from "vite";
import react, { reactCompilerPreset } from "@vitejs/plugin-react";
import babel from "@rolldown/plugin-babel";

export default defineConfig({
  plugins: [react(), babel({ presets: [reactCompilerPreset()] })],
});Code language: JavaScript (javascript)
```

Going native means shedding some config dead weight. You run:

```
npm install -D oxc-transform-react
```

And simplify your Vite config:

```
// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react({ compiler: true })],
});Code language: JavaScript (javascript)
```

This also means you can remove `@rolldown/plugin-babel` from your `package.json` dev dependencies.

### Not Using `@vitejs/plugin-react` (e.g. React Router Framework Mode)

For codebases that are on React Router in framework mode, the switch is a little different. React Router has its own Vite plugin that should be run in place of the Vite React plugin, so whereas you previously needed to run:

```
npm install -D vite-plugin-babel babel-plugin-react-compiler @babel/preset-typescriptCode language: Bash (bash)
```

With the following Vite config:

```
// vite.config.js
import { defineConfig } from "vite";
import babel from "vite-plugin-babel";
import { reactRouter } from "@react-router/dev/vite";

const ReactCompilerConfig = {
  /* optional config if you have it */
};

export default defineConfig({
  plugins: [
    reactRouter(),
    babel({
      babelConfig: {
        presets: ["@babel/preset-typescript"], // if you use TypeScript
        plugins: [["babel-plugin-react-compiler", ReactCompilerConfig]],
      },
      exclude: /node_modules/,
      include: /\.[jt]sx?$/,
    }),
  ],
});Code language: JavaScript (javascript)
```

You can now drop `vite-plugin-babel`, `babel-plugin-react-compiler`, and `@babel/preset-typescript` entirely and instead just install:

```
npm install -D @acusti/vite-plugin-react-compilerCode language: Bash (bash)
```

And simplify your config to:

```
// vite.config.js
import { defineConfig } from "vite";
import reactCompiler from "@acusti/vite-plugin-react-compiler";
import { reactRouter } from "@react-router/dev/vite";

export default defineConfig({
  plugins: [reactRouter(), reactCompiler()],
  // or, if you need to pass custom compiler config:
  // reactCompiler({ compiler: { /* your existing ReactCompilerConfig */ } })
});Code language: JavaScript (javascript)
```

Simpler, faster, and more capable. Cheers to that. I think I know [just the right drink](https://en.wikipedia.org/wiki/Rusty_nail_(cocktail)).

Related notes: [[React Compiler]], [[Vite]]
