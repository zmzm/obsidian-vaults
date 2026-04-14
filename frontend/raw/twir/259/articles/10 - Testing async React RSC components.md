---
type: twir-item
issue: 259
item: 10
item_type: item
date: 2025-11-19
source: https://howtotestfrontend.com/resources/testing-async-react-rsc-components
tags:
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-11-19-TWIR-259|Index]]

# Item 10: Testing async React RSC components

Source: [https://howtotestfrontend.com/resources/testing-async-react-rsc-components](https://howtotestfrontend.com/resources/testing-async-react-rsc-components)

Summary:
Testing async React Server Components (RSCs) is challenging, especially with nested async components and Suspense. The article explores the limitations of React Testing Library for RSCs and suggests workarounds, such as directly awaiting async components before rendering, but notes that e2e tests are often more reliable for RSCs.

Key takeaways:
- Unit testing RSCs with React Testing Library has significant limitations, particularly with Suspense and nested async components.
- Awaiting async components before rendering can work for simple cases.
- End-to-end testing (e.g., Playwright, Cypress) is recommended for comprehensive RSC coverage.

Recommendation:
Summary sufficient

Content:
# Testing async React RSC components

Testing React Server Components (RSCs) is quite difficult.

This is because of the async behaviour of the components.

It is so hard in fact, that the normal recommended approach to testing is to use e2e tests (like Playwright or Cypress) to test RSC components.

**Here is my guide to testing RSC components** with React Testing Library's `render(...)` functionality as best as I can figure out.

I am only going to cover 'regular' tests (unit tests, with React Testing Library) with Jest or Vitest and React Testing Library.

Want to skip to my recommended way? See the section on `use()` below.

## What I am trying to test

I've made some very simple RSC components which do some data fetching. As I am testing with Vitest, I am mocking `window.fetch` with `vitest-fetch-mock`:

```
import createFetchMock from 'vitest-fetch-mock';
import { vi } from 'vitest';
createFetchMock(vi).enableMocks();
```

The mocked data for the fetch isn't important. The important thing is that the `await` inside the RSC component is actually awaited, we get the mock data, and render the JSX showing the count of rows (5 in the mock data)

```
const dummyData = {
  results: [
    { name: 'bulbasaur' },
    { name: 'ivysaur' },
    { name: 'venusaur' },
    { name: 'charmander' },
    { name: 'mew' },
  ],
};
```

And here are 3 components - an outer container (with suspense), and a couple of RSC components which do some data fetching.

(One of the difficulties of testing RSC components *is when you need to test components which render nested async RSC components*, which is why this example component has the mix of different nested RSC components)

```
export const ContainerWithSuspenseAndLoading = () => {
  return (
    <div>
      <Suspense fallback={<b>loading 1</b>}>
        <FetchData />
      </Suspense>
    </div>
  );
};

export const FetchAndChildComponentFetches = async () => {
  const data = await fetch('/data').then(res => res.json());

  return (
    <div>
      <h1>FetchAndChildComponentFetches</h1>
      <h2>
        Another Fetch rows:
        {data.results.length}
      </h2>

      <ContainerWithSuspenseAndLoading />
    </div>
  );
};

async function FetchData() {
  const data = await fetch('/data').then(res => res.json());

  return (
    <div>
      <h1>Fetch Results</h1>
      <h2>Num rows: {data.results.length}</h2>
    </div>
  );
}
```

## How to test it?

Using these versions of `react` and `react-dom`:

```
{
  "react": "19.1.5",
  "react-dom": "19.1.5"
}
```

Let's start with the easiest.

### Testing a RSC component without any nested RSC components or Suspense

This is the **most simple RSC component**, as we have no nested child async components, and no `<Suspense>` to deal with.

However, even in such a simple setup, the following will *not* work:

```
it('renders FetchData', async () => {
  render(<FetchData />);

  
  expect(
    await screen.findByText('Num rows:', { exact: false }) 
  ).toHaveTextContent('Num rows: 5');
});
```

It fails as it still sees the rendered document as just `<body></body>`.

You can even check that `window.fetch` was called, and it is called! So it is *running* our RSC component, but not rendering it all into the DOM for React Testing Library to find.

```
it('renders FetchData - await syntax', async () => {
  render(<FetchData />);

  
  await waitFor(() => {
    expect(window.fetch).toBeCalledTimes(1);
  }); 

  
  expect(
    await screen.findByText('Num rows:', { exact: false }) 
  ).toHaveTextContent('Num rows: 5');
});
```

But there is a simple workaround - use `await FetchData()`.

```
it('renders FetchData - await syntax', async () => {
  
  render(await FetchData());

  expect(window.fetch).toBeCalledTimes(1); 

  
  expect(
    screen.getByText('Num rows:', {
      exact: false,
    })
  ).toHaveTextContent('Num rows: 5'); 
});
```

Note: because of the await inside `render(await FetchData())`, we don't need to `await screen.findByText(...)`.

If you need to pass props, you can just do `render(await SomeComponent({someProp: true}))`

But using this method only works when the top level component is the only async RSC component!

In this next test, the component has `<Suspense>` with its child being the `<FetchData />` component from the previous tests. But because of that Suspense, it fails to render anything other than the fallback (loading).

```
it('renders ContainerWithSuspenseAndLoading - await syntax', async () => {
  
  render(await ContainerWithSuspenseAndLoading());

  expect(screen.getByText('loading 1')).toBeInTheDocument(); 

  
  expect(
    await screen.findByText('Num rows:', { exact: false }) 
  ).toHaveTextContent('Num rows: 5');
});
```

It will never render anything past the initial Suspense fallback, even with `await screen.findBy...`

Sometimes though, using the `render(await SomeComponent())` is good enough, if all of your data loading is done in that component. You can assume any parent component (with `<Suspense>`) is going to call it correctly.

But it is still not ideal.

### Use a helper render function to render nested RSC components

After lots of research and digging through tons of GitHub issue comments, I found a couple of workaround render functions.

Check it out here: [renderServerComponent](https://gist.github.com/sroebert/a04ca6e0232a4a60bc50d7f164f101f6)

This helper function will render RSC components *and child async RSC components* correctly.

```
it('using renderServerComponent, renders <Container />', async () => {
  
  renderServerComponent(<ContainerWithSuspenseAndLoading />);
  
  expect(document.body).toMatchInlineSnapshot(`<body />`); 

  
  expect(await screen.findByText('Num rows:', { exact: false })).toHaveTextContent('Num rows: 5'); 
});
```

Getting the initial Suspense fallback component (the loading one) wasn't possible. (Even adding a setTimeout - I thought at first my mock data was being immediately returned).

It figures out if the component it is rendering is a RSC component, and fully awaits for it to return (recursively awaiting the entire tree where needed). Then when it has evaluated the entire tree, it uses *that* to pass into `render()`

### Use a specific version of React which renders 'correctly'

There is a specific version of React 19 on NPM which can be used that seems to work really well for testing RSC components.

This specific version will work:

```
{
  "react": "19.0.0-rc-380f5d67-20241113",
  "react-dom": "19.0.0-rc-380f5d67-20241113"
}
```

If you use this (**bear in mind: there are security issues with such an older version** and I am listing it here just as reference. I would not suggest using this on production.), then writing tests with RSC components is easy - you can test Suspense, you can just use regular `render(<SomeRSCComponent />)`.

But as far as I can tell (I tried many other rc and proper release versions) this is the only version that works.

So I've had success by using Next 15 (which bundles its own React 19 version), but in my package.json (which Vitest/Jest will use) I use the rc versions above. The actual Next app works correctly, and the tests (which use the 'rc' version) are easily testable). I am very sure this hacky workaround (not nice to be testing on different versions of React) will cause problems on some repos though - and definitely has security issues (as the rc version is not the latest with security fixes). I would not recommend it. However it does work.

### Using act(render(...)) with use()

```
import { act, render, screen } from '@testing-library/react';
import { use, Suspense } from 'react';

const ComponentUsingUse = ({ params }: { params: Promise<{ lang: string }> }) => {
  const { lang } = use(params);
  return <div>hello from {lang}</div>;
};

const ComponentUsingUseAndSuspense = ({ params }: { params: Promise<{ lang: string }> }) => {
  return (
    <div>
      <Suspense fallback={<b>loading</b>}>
        <ComponentUsingUse params={params} />
      </Suspense>
    </div>
  );
};

it('renders content from use, without suspense', async () => {
  await act(() =>
    render(
      <ComponentUsingUse
        params={Promise.resolve({
          lang: 'en',
        })}
      ></ComponentUsingUse>
    )
  );
  expect(screen.getByText('hello from en')).toBeInTheDocument(); 
});

it('renders with suspense', async () => {
  await act(() =>
    render(
      <ComponentUsingUseAndSuspense
        params={Promise.resolve({
          lang: 'en',
        })}
      ></ComponentUsingUseAndSuspense>
    )
  );
  expect(screen.getByText('hello from en')).toBeInTheDocument(); 
});

it.skip('renders content from use, without suspense, without act()', async () => {
  
  render(
    <ComponentUsingUse
      params={Promise.resolve({
        lang: 'en',
      })}
    ></ComponentUsingUse>
  );

  expect(await screen.findByText('hello from en')).toBeInTheDocument(); 
});
```

Here is an example showing data fetching, using `use()`, with a working test:

```
const Component = () => {
  
  
  const fetchPromise = fetch('/data').then(res => res.json());
  const data = use(fetchPromise);

  return (
    <div>
      <h1>Loaded data</h1>
      <h2>Rows: {data?.results?.length}</h2>
    </div>
  );
};

it('renders fetch using use', async () => {
  fetchMock.mockResponse(JSON.stringify(dummyData));

  await act(() =>
    render(
      <Suspense>
        <Component />
      </Suspense>
    )
  );

  expect(screen.getByText('Loaded data')).toBeInTheDocument(); 
  expect(screen.getByText('Rows: 5')).toBeInTheDocument(); 
});
```

Note: using this approach of `await act(() => render(...)` with the other previous components (which `await`-ed in the component) will not work.

If you are starting a new app (where you don't have lots of `await` inside your existing components) I think this might be the best approach so far. It isn't hacky (ignoring the `act()` wrapped around the render call) and feels like it should work fine with future versions of React.

## Ok, so what should I do if I want to test RSC components

- If possible, the easiest way for you to test your async RSC components is remove the `async` part and wrap your promises in `use()`.
- If you are using Next.js, and are happy to test with a different version of React, you can use a specific (slightly older) version of React. I don't recommend this for big production apps.
- If you have nested async RSC components, you might find it easier to test each async component individually. Using standard `react` versions, with nested `async` RSC components is a pain to do.
- For most confidence that your components are running as expected, doing E2E (for example, Cypress or Playwright) is the best route.

## Resources and links

- [Big GitHub issue](https://github.com/testing-library/react-testing-library/issues/1209)
- The reason the `19.0.0-rc` version which works well may be documented [here](https://github.com/facebook/react/issues/29905)  (found via [here](https://x.com/nikgraf/status/1857414850957234565?lang=en) ) - note that this is a much older version of React, with known security issues at this point
- source for [renderServerComponent](https://gist.github.com/sroebert/a04ca6e0232a4a60bc50d7f164f101f6) , with a backup [here](https://gist.github.com/HowToTestFrontend/ffe161b500dfd93d5a2c400e2df0318b)
- Another version [here](https://gist.github.com/tarunsahnan/93418e81882f2e343e09894bc6de6f35)
- Old twitter post about MSW in Next RSC components [here](https://x.com/ApiMocking/status/1656249306628915208?s=20)
- [vitest-plugin-rsc](https://github.com/kasperpeulen/vitest-plugin-rsc)  - but this is for Vitest browser mode tests (so not useful for RTL tests)

## Do you know of other tips/tricks/resources/urls for testing React Server components in your unit tests?

Please [contact me](/static/contact) and I will try it out & update this.

Related notes: [[Server Components]]
