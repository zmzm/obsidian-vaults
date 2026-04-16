---
type: twir-item
issue: 264
item: 11
item_type: item
date: 2026-01-14
source: https://howtotestfrontend.com/resources/how-to-write-good-frontend-tests
tags:
  - "37"
  - "Ant"
status: auto
quality: keep
---

[[2026-01-14-TWIR-264|Index]]

# Item 11: How to write good frontend tests: 37 tips and tricks

Source: [https://howtotestfrontend.com/resources/how-to-write-good-frontend-tests](https://howtotestfrontend.com/resources/how-to-write-good-frontend-tests)

Summary:
This resource compiles practical advice for writing clear, maintainable frontend tests, emphasizing clarity, avoiding implementation details, and focusing on user-facing behavior. It advocates splitting tests by concern, using semantic queries in React Testing Library, and not testing third-party code or framework internals. The tips are broadly applicable to React and other frontend frameworks.

Key takeaways:
- Write focused tests that are clear about what they verify; avoid mixing unrelated assertions.
- Test public behavior, not internal implementation details.
- Use semantic queries (getByRole, getByLabelText) for more robust and accessible tests.
- Don’t waste effort testing framework/library code; focus on your own logic.

Recommendation:
Read fully (read fully for actionable test-writing examples)

Why it matters:
read fully for actionable test-writing examples

Content:
# How to write good frontend tests: 37 tips and tricks

I love working with tests. It is always a fun process writing a test, and then updating the code to get the test to pass and go green.

But there is nothing more frustrating than trying to figure out what some existing tests were doing. (Often, when I was the original author of those tests too!)

Here are all my tips for writing high quality frontend tests.

Some examples I've simplified by removing the frontend specific parts, just to make the point
easier. This is a site all about testing frontend apps, but to be honest most clean testing
principles apply to frontend or backend testing!

### Good tests are clear about what they are testing

If you are testing a component, having separate `test()` (or `it()`) for different assertions makes it much easier to maintain.

Important to note: I am **not** suggesting a strict rule of 1 test = 1 assertion.

That is a silly rule that some take too far. But keep unrelated assertions in different `test()` calls.

For example, the following example is messy and hard to maintain, and when it fails it isn't clear what it is testing:

```
test('component works ok', async () => {
  render(<SomeComponent />);

  
  expect(screen.getByText('Loading...')).toBeInTheDocument();

  await waitFor(() => expect(fetch).toHaveBeenCalled());
  expect(await screen.findByText('your mock data from api')).toBeInTheDocument();

  expect(screen.queryByText('Loading...')).toBeNull();

  
  await userEvent.click(
    screen.getByRole('button', {
      name: 'Create',
    })
  );
  expect(await screen.findByText('Created ok message')).toBeInTheDocument();
  expect(fetch).toHaveBeenCalledWith('/create');

  
  await userEvent.click(
    screen.getByRole('button', {
      name: 'Delete',
    })
  );
  expect(screen.getByText('Deleted item')).toBeInTheDocument();
  expect(fetch).toHaveBeenCalledWith('/delete');
});
```

In that test, we are:

- testing it loads data/calls fetch
- *and* testing we can use the create form
- *and* testing we can use the delete form

This is a bit of a made-up example, but it is so easy to add these sorts of test (especially when adding a tiny feature at a time... easier to update an existing test and test that small new bit functionality in the same test).

These sorts of tests are annoying to maintain, because if they fail it isn't immediately clear what part failed.

So in this example, I would suggest splitting up into three tests. The overhead of 3 different tests, re-rendering each time is worth it, to get better developer experience and cleaner tests.

### Avoid testing implementation details

Try to avoid testing implementation details. In the non-frontend world of testing, we would always try to test public methods on classes. In frontend tests we do the same concept - but we test everything via what our components are rendering and the interaction we can perform on them (via buttons).

This should be an obvious one as it is so commonly referenced, but it is very easy to get carried away and start testing implementation details, and not the behaviour that users (real users on a UI, or a public API) would use.

For example - testing a hook vs testing a component that uses the hook.

```
test('component uses useState correctly', () => {
  const { result } = renderHook(() => useState(0));
  expect(result.current[0]).toBe(0);
});

test('counter displays initial value of 0', () => {
  render(<Counter />);
  expect(screen.getByText('Count: 0')).toBeInTheDocument();
});
```

If you are only testing the hook, then there is no proof your component is working as expected.

It also means if you refactor your component (same functionality, but maybe you change how you increment - with another hook), your existing test is going to pass.

Note: there are times that it makes sense to test your component, *but also test some of the internals in isolation*. Maybe your component uses a hook, and it is much easier to test the various combinations of things that the hook returns. But just remember if you switch out that hook to something else, your component is going to be missing test coverage...

### Test your application logic, not third-party code

Don't test framework or library (React, Next) specific code.

If you're using a framework or library, there isn't much value in you testing that.

Of course, test *your code* that uses it.

This means for React apps

- don't bother testing that it can take some JSX and render it
- if you pass in `style={someStyleObject}`, there is no point testing that React is setting the style object correctly

Where it gets a bit less clear is for things like how to check that a NextJS app changes pages. I often find the only reliable way is to run end-to-end tests (Playwright or Cypress) and check the url changed.

### Using the correct (most suitable) query functions in React Testing Library or Vitest Browser Mode

I've written about this a lot on this site - but it is important to use the correct query functions (like `getByText()`, `getByPlaceholderText()` etc).

Using the correct ones means:

- it is easier to read the test (it is **clearer what you're trying to do in the test**),
- it encourages a **more realistic test** (finding elements by their label text for example is basically what real humans do when interacting with a form),
- and nudges you into **using semantically correct HTML elements** (which helps with accessibility).

For example:

```
const button = screen.getByTestId('submit-btn');
const heading = screen.getByTestId('main-title');
const input = screen.getByTestId('email-input');

const button = screen.getByRole('button', { name: 'Submit' });
const heading = screen.getByRole('heading', { name: 'Sign Up' });
const input = screen.getByLabelText('Email address');
```

The RTL query priority order is:

1. `getByRole` - best for buttons, headings, forms
2. `getByLabelText` - perfect for form inputs
3. `getByPlaceholderText` - good for inputs without labels
4. `getByText` - for non-interactive content
5. `getByDisplayValue` - for form elements with values
6. `getByAltText` - for images
7. `getByTitle` - for elements with title attributes
8. `getByTestId` - last resort only

Note: `getByRole` can be the slowest of all, so although it is higher priority, if you are seeing slow tests on components with a lot of elements it is something to bear in mind.

When writing tests, the easiest way is to add a `data-testid` to everything and use `getByTestId(...)`. But it takes only a tiny bit more effort to use better query function.

Note: data-testid definitely has its uses. Sometimes it makes tests much much easier to write and maintain. Just don't overdo it.

### Avoiding mocking, and prefer testing real implementations

Sometimes you see tests which is testing a React component, and every component it includes is mocked.

This comes from one way of thinking about unit tests - testing something completely in isolation. In my opinion this is an outdated way of testing that should be avoided.

And sometimes it can be easier to initially write (as you don't have to care about those components. Just mock them so they do nothing).

I've noticed AI loves to over mock when you ask it to test a component (I would guess because it isn't sure how the other components should actually work).

```
vi.mock('./Header', () => ({
  Header: () => <div data-testid="header">Mocked Header</div>,
}));

vi.mock('./Sidebar', () => ({
  Sidebar: () => <div data-testid="sidebar">Mocked Sidebar</div>,
}));

vi.mock('./Footer', () => ({
  Footer: () => <div data-testid="footer">Mocked Footer</div>,
}));

vi.mock('./UserProfile', () => ({
  UserProfile: () => <div data-testid="user-profile">Mocked User</div>,
}));

test('dashboard renders correctly', () => {
  render(<Dashboard />);

  expect(screen.getByTestId('header')).toBeInTheDocument();
  expect(screen.getByTestId('sidebar')).toBeInTheDocument();
  expect(screen.getByTestId('footer')).toBeInTheDocument();
  expect(screen.getByTestId('user-profile')).toBeInTheDocument();
});
```

This test isn't really testing any real implementation. It is just testing your test mocks. So I find to hard to see any value in that test.

Here is an improved version - still mocking some things, but this time just the data fetching part. It is also making assertions that every element (like the header, sidebar etc) contains the expected real value, not just that there is a `data-testid` with that value in the DOM.

```
vi.mock('./api/userService', () => ({
  fetchUserData: vi.fn().mockResolvedValue({
    name: 'John Doe',
    email: 'john@example.com',
  }),
}));

test('dashboard displays user information after loading', async () => {
  render(<Dashboard />);

  
  expect(await screen.findByText('Welcome, John Doe')).toBeInTheDocument();
  expect(screen.getByText('john@example.com')).toBeInTheDocument();

  
  expect(screen.queryByText('Loading...')).not.toBeInTheDocument();
});
```

The main times I will mock or spyOn:

- mock api responses
- mock errors (to check the thing you're testing handles it)
- mock a third party library/component
- mock when the component is using web APIs such as Canvas which is not supported in React Testing Library. (ideally you can extract that part of the component out into its own export, so you can mock a small subset of the component)
- mock something that you know is tested elsewhere, which are not relevant to this component's test.

### If you do mock, try to avoid over mocking

If you do decide to use `vi.mock()` or `jest.mock()` (or their slight variations like `.doMock()`) be aware that you are mocking the entire module.

This means that if that module starts exporting a new property, your mocks probably all need updating.

I've seen this multiple times where a module was mocked, then several months later another export added and all the tests break.

There is a workaround with `vi.importActual()` (in Jest, use `jest.requireActual()`), which can help:

```
vi.mock('./userService', () => ({
  fetchUser: vi.fn().mockResolvedValue({
    name: 'John',
  }),
  updateUser: vi.fn(),
  deleteUser: vi.fn(),
}));

vi.mock('./userService', async () => {
  const actual = await vi.importActual('./userService');
  return {
    ...actual,
    fetchUser: vi.fn().mockResolvedValue({
      name: 'John',
    }),
    
  };
});

jest.mock('./userService', () => ({
  ...jest.requireActual('./userService'),
  fetchUser: jest.fn().mockResolvedValue({
    name: 'John',
  }),
  
}));
```

This way, if the `userService` module gets new exports, your tests won't break because you're only overriding the specific functions you need to mock.

Another (nicer) workaround is to try to extract the things you will mock into separate files, so you can 'safely' mock the entire file.

But a much better 'workaround' is to use `vi.spyOn()` (or `jest.spyOn()`). You get automatic TypeScript typings, you can easily restore it, and when reading a test it is much easier to read and figure out what is going on.

```
beforeEach(() => {
  vi.spyOn(userService, 'fetchUser').mockResolvedValue({
    name: 'John',
  });
});
```

### Prioritise fixing flaky tests

Personally I see flaky tests as *almost* as important as a bug which has made it to production.

If you have to keep re-running tests because some of your tests sometimes pass, sometimes fail then:

- firstly, it is an obvious waste of time
- the flaky test *might* be due to a real bug in your app (not just buggy test code)
- and very soon engineers figure out that a file is always failing, and just ignore it and merge without your CI all passing. This can easily result in accidentally merging *another failing test* without realising.

There are times when deleting a flaky test has more value than keep re-running a test that might pass. But ideally remove the flakiness!

### Don't only test the happy path

The "happy path" is the most important path - the "successful" or error-free flow.

For example a "contact form submits OK and sends the form details to the backend" would be the happy path.

However the **sad path** is equally as important.

The sad path means the opposite of the happy path. In other words - when things go wrong.

- error states
- form validation issues
- network issues
- authentication or authorisation issues
- and edge cases

These are all part of the user experience that real users will experience.

And these are the types of things that any QA department will not notice as easy as bugs in the happy path

```
test('submits contact form successfully', async () => {
  render(<ContactForm />);

  
  

  expect(await screen.findByText('Message sent successfully!')).toBeVisible();
});

test('shows error when form submission fails', async () => {
  
  vi.mocked(fetch).mockRejectedValueOnce(new Error('Network error'));

  render(<ContactForm />);

  
  

  expect(await screen.findByText('Failed to send message. Please try again.')).toBeVisible();
});
```

### Good tests do not overuse snapshots

**What are snapshots?** *(Show details)*

There are two types of snapshots.

The first is just `expect(val).toMatchSnapshot()` which after the first run of the test will write a file with the output of `val`. In future test runs it will compare the current value to that snapshot file.

The second - `expect(val).toMatchInlineSnapshot()` is very similar, but updates the test file and stores the output of the value inline.

After the first run, Jest or Vitest will replace that line with something like `expect(val).toMatchInlineSnapshot("some-output")` (note: it can be a serialised object, array etc too)

I love `.toMatchInlineSnapshot()`. I use it all the time during development.

Even with TDD, sometimes I know it is just faster to use inline snapshots than write out complex objects in the `.toStrictEqual(...)`.

But they are the cause of many problems in my opinion.

If the codebase overuses snapshots, we all get used to `yarn test:watch` and then hitting `u` (to update the snapshots). Bugs make it through, and it is so easy to miss.

I like them for things like error message strings, especially if you expect in a future edit they will change soon. It just makes development quicker with minimal drawbacks.

But if you use them with massive objects, huge arrays, or serialised DOMs, it quickly makes tests very confusing. It is much better to test just the parts that are relevant for the test

For example, instead of this overly complex snapshot:

```
test('updates theme to dark mode', () => {
  updateTheme(mockUserId, 'dark');

  const userProfile = getUserProfile(mockUserId);

  expect(userProfile).toMatchInlineSnapshot(`
    {
      "id": "user123",
      "name": "John Doe",
      "email": "john@example.com",
      "preferences": {
        "theme": "dark",
        "language": "en",
        "notifications": {
          "email": true,
          "push": false,
          "sms": true,
          "marketing": false,
          "newsletter": true,
        },
        "privacy": {
          "showEmail": false,
          "showPhone": true,
          "allowAnalytics": true,
          "cookieConsent": true,
        },
      },
      "profile": {
        "bio": "Software engineer passionate about testing",
        "location": "San Francisco, CA",
        "website": "https://johndoe.dev",
        "socialMedia": {
          "twitter": "@johndoe",
          "github": "johndoe123",
          "linkedin": "john-doe-engineer",
        },
      },
      "metadata": {
        "createdAt": "2023-01-15T10:30:00Z",
        "updatedAt": "2024-03-20T14:45:30Z",
        "lastLoginAt": "2024-03-21T09:15:22Z",
        "loginCount": 247,
        "accountStatus": "active",
      },
    }
  `);
});
```

When that test starts failing, how do you know what we were really testing there???

I find that the following version is much cleaner and focuses only on what matters for this specific test:

```
test('updates theme to dark mode', () => {
  updateTheme(mockUserId, 'dark');

  const userProfile = getUserProfile(mockUserId);

  expect(userProfile.preferences.theme).toBe('dark');
});
```

The second version is much easier to read and understand what the test is actually verifying.

Another advantage is that if the `user profile` data structure gets new attributes (or some removed), this test will be unaffected (unless the `userProfile.preferences.theme` gets updated).

**If you and your team do use snapshots** I have two main tips:

- be very careful of developers seeing a test fail, hitting `u` (to update the snapshot) and committing it. It is very easy to not realise that a bug was introduced, and all we've done is update the test so the bug passes
- avoid snapshotting HTML. You can do something like `expect(screen.getByText('hi')).toMatchInlineSnapshot(...)`. This will end up being huge chunks of HTML, hard to maintain (other than hitting `u` to update it).

### Well organised test file structure, with correctly named tests

Using a mix of nested `describe()` blocks, `test()` (or `it()`) with clear titles, and using `.each()` where appropriate make maintaining your tests much easier.

They let you:

- Quickly/easily find tests and/or know where to add a new test so related behaviours are tested near each other
- Understand what each test does without reading the implementation
- Run specific groups (in a describe block) of tests during development, with `.only()`

When you start working on huge test files (another code smell) with no structure, you can end up adding duplicate tests or not realising something has no test coverage.

### Good tests run fast

Nothing *feels* less productive than having to wait 30+ seconds for your tests to run.

Of course, running *all* your tests will take longer than 30 seconds on any decent sized app.

But when you are running just one test or two test files, making changes in one or two components it is so much nicer when you get nearly instant feedback.

Tip: make use of the `--watch` mode when running tests, and filter down by a specific filename. For example `vitest --watch UserProfile.test.tsx`.

### Avoid Querying for elements based on classnames or other similar attributes

A common mistake that I sometimes see in tests is trying to query for elements in the DOM based on things like their class names.

```
const { container } = render(<SomeComponent />);

const submitButton = container.querySelector('.submit-btn');
const errorMessage = container.querySelector('.error-text');
```

(And it is even worse when those classnames are auto generated random string from CSS-in-JS)

Access to things like `.querySelector()` should be seen as an escape hatch for those few times you genuinely do need to reach for it.

Normally you should be able to use React Testing Library (or Vitest Browser Mode) standard queries (like `getByRole()` or `getByText()`.

Writing tests like this end up being a pain to maintain, and break the core principle of React Testing Library, which is to query for elements semantically. But I've written about that enough previously in this post so I won't go into it again.

### Avoid asserting that elements have specific classnames

In the last tip, I mentioned how it is bad to **query for elements based on their classname**.

The opposite side to that coin is also true - we **shouldn't be making assertions checking that specific classes were set**.

There are exceptions. I probably do it a few times a year. If you were testing *theming* related code, then go for it.

But for regular tests, I always see `.toHaveClass` as a code smell to avoid.

Without visual regression tests (taking real screenshots and comparing them) you are often not really proving that these classes are doing anything anyway.

There are so many built in matchers that you can normally use them to achieve what you were trying to do via class names. Here are some examples:

```
expect(button).toHaveClass('sc-bdVaJa-d');
expect(button).toHaveClass('border-red-500');

expect(button).toBeVisible();
expect(button).toBeEnabled();

expect(button).toHaveAttribute('aria-pressed', 'false');

expect(button).toHaveTextContent('Submit Form');

expect(input).toBeRequired();
expect(input).toHaveValue('john@example.com');
```

### Avoid Testing State management (like Redux) internals

When testing components that use state management libraries such as Redux, or Zustand, you should test the component behaviour and not test the internals of your state management system. This is very similar to a tip at the top of this post - but I have seen it crop up many times on bigger apps that use tools like Redux or Zustand.

```
test('dispatches correct action', () => {
  const store = createMockStore();
  render(
    <Provider store={store}>
      <TodoList />
    </Provider>
  );

  const addButton = screen.getByRole('button', { name: 'Add Todo' });
  userEvent.click(addButton);

  expect(store.getActions()).toEqual([
    {
      type: 'ADD_TODO',
      payload: 'New todo',
    },
  ]);
});

test('adds new todo when button is clicked', () => {
  render(
    <Provider store={mockStore}>
      <TodoList />
    </Provider>
  );

  const addButton = screen.getByRole('button', { name: 'Add Todo' });
  userEvent.click(addButton);

  expect(screen.getByText('New todo')).toBeInTheDocument();
});
```

**Test what real users experience, not the implementation details**. This is much more maintainable and gives much more value to your tests.

### Avoid testing with .toBeDefined() - use a more useful test instead

If you are testing some return value from a function, it can be tempting to just stick a `expect(something).toBeDefined()` to prove that it isn't empty

But why stop there? In most cases it is more valuable as a test (and easier to read, you know what is going on) if it asserted the exact value it should be...

```
test('user profile has data', () => {
  const user = getUserProfile();

  expect(user).toBeDefined();
  expect(user.name).toBeDefined();
  expect(user.email).toBeDefined(); 
});

test('user profile contains correct data', () => {
  const user = getUserProfile();

  expect(user.name).toBe('John Doe');
  expect(user.email).toBe('john@example.com');
  expect(user.isActive).toBe(true);
});
```

In the first test it was proving that we return *something* that has a name and email value. But doesn't prove we set those up correctly.

What if `user.name` is an empty string? Or what if `user.email` is invalid? The test would still pass.

BTW In the second test I didn't even assert `expect(user).toBeDefined()`. It is just noise, the subsequent tests prove that it is an object anyway.

And `.toBeDefined()` will pass even if `null` is returned:

```
const getUserById = id => {
  
  return null;
};

test('getUserById returns user data', () => {
  const user = getUserById('123');

  expect(user).toBeDefined(); 
});

test('getUserById returns user with correct properties', () => {
  const user = getUserById('123');

  expect(user).toEqual({
    id: '123',
    name: 'John Doe',
    email: 'john@example.com',
  });
  
});
```

The same issue happens with functions that return empty arrays or empty strings:

```
const getErrorMessages = () => {
  return []; 
};

test('returns error messages', () => {
  const errors = getErrorMessages();
  expect(errors).toBeDefined(); 
});

test('returns validation error messages', () => {
  const errors = getErrorMessages();
  expect(errors).toEqual(['Email is required', 'Password must be at least 8 characters']);
});
```

### In TypeScript: Avoid overuse of `as any` - be more specific

I think in tests we can be more lenient about using incorrect types.

For example if in the following, we know that in `userCanCreatePost()` we only need to send `active: false`, so we could get away with this:

```
expect(
  userCanCreatePost({
    active: false,
  } as any)
).toBe(false);
```

But it is much safer, with the same amount of effort, to use a type assertion of the actual type - e.g. `{active: false} as User`.

Then if there is a typo, we'd get an TypeScript error:

```
expect(
  userCanCreatePost({
    isActive: false,
  } as any)
).toBe(false);
```

The best way around this is in the next tip - using fixture and helper functions.

### Use fixtures and helper functions to make tests easier to read & write

If you are often writing similar code to create mock data, consider using prebuilt objects with that shape, or fixture functions to generate them:

```
interface User {
  id: string;
  name: string;
  email: string;
  isActive: boolean;
  preferences: {
    theme: 'light' | 'dark';
    notifications: boolean;
  };
}

export const createUser = (overrides?: Partial<User>): User => {
  return {
    id: 'user-123',
    name: 'John Doe',
    email: 'john@example.com',
    isActive: true,
    preferences: {
      theme: 'light',
      notifications: true,
    },
    ...overrides,
  };
};

export const createInactiveUser = (): User => {
  return createUser({
    isActive: false,
  });
};

export const createAdminUser = (): User => {
  return createUser({
    name: 'Admin User',
    email: 'admin@example.com',
  });
};

test('displays user profile correctly', () => {
  const user = createUser({
    name: 'Jane Smith',
    email: 'jane@example.com',
  });

  render(<UserProfile user={user} />);

  expect(screen.getByText('Jane Smith')).toBeInTheDocument();
  expect(screen.getByText('jane@example.com')).toBeInTheDocument();
});

test('shows inactive status for inactive users', () => {
  const inactiveUser = createInactiveUser();

  render(<UserProfile user={inactiveUser} />);

  expect(screen.getByText('Status: Inactive')).toBeInTheDocument();
});

test('shows list of users', () => {
  const users = [
    createUser({ name: 'User 1' }),
    createUser({ name: 'User 2' }),
    createInactiveUser(),
  ];

  render(<UserList users={users} />);

  expect(screen.getByText('User 1')).toBeInTheDocument();
  expect(screen.getByText('User 2')).toBeInTheDocument();
  expect(screen.getByText('Status: Inactive')).toBeInTheDocument();
});
```

This makes your tests much easier to read. You can easily understand that if we are passing `createUser({isActive: false})` in, that the thing that is important for this test is just the `isActive: false` part.

This means when tests fail, it is more obvious what the test was trying to do (as only the important fields in the helper function will be used).

### Good use of render helper functions, to set up common context providers

In most real apps, you end up with a `_app.tsx` or `main.tsx` with something like:

```
return (
  <ThemeProvider currentTheme="dark">
    <ReduxProvider>
      <UserOptionsProvider>
        <FeatureFlagProvider enabled={query.featureSwitch}>
          <AuthProvider currentUser={user}>{props.children}</AuthProvider>
        </FeatureFlagProvider>
      </UserOptionsProvider>
    </ReduxProvider>
  </ThemeProvider>
);
```

So then often in your tests, you end up calling render with some of those parent providers, as they're crucial for your components to work:

```
render(
  <ThemeProvider currentTheme="dark">
    <ReduxProvider>
      <FeatureFlagProvider>
        <AuthProvider currentUser={mockUser}>
          <YourActualComponentHere />
        </AuthProvider>
      </FeatureFlagProvider>
    </ReduxProvider>
  </ThemeProvider>
);
```

(Or sometimes you will see all those providers and their `useContext()` hooks mocked!)

It would be much easier to have some helper functions like this, which works the same as standard `render()` but with all the parent components passed in.

```
const renderWithProviders = component => {
  return render(component, {
    wrapper: props => {
      return (
        <ThemeProvider currentTheme="dark">
          <ReduxProvider>
            <UserOptionsProvider>
              <FeatureFlagProvider enabled={query.featureSwitch}>
                <AuthProvider currentUser={user}>{props.children}</AuthProvider>
              </FeatureFlagProvider>
            </UserOptionsProvider>
          </ReduxProvider>
        </ThemeProvider>
      );
    },
  });
};

renderWithProviders(<YourActualComponentHere />);
```

If you then notice you are still having to provide some providers, for example to test a specific user `<AuthProvider currentUser={adminUser}>...</AuthProvider>` or a feature flag `<FeatureFlagProvider enabled="demo">...</FeatureFlagProvider>` then adding these as options in your render helper makes it much easier to read:

```
const renderWithProviders = (component, options) => {
  return render(component, {
    wrapper: props => {
      return (
        <ThemeProvider currentTheme={options?.currentTheme ?? 'dark'}>
          <ReduxProvider>
            <UserOptionsProvider>
              <FeatureFlagProvider enabled={options?.featureFlag}>
                <AuthProvider currentUser={options?.currentUser ?? user}>
                  {props.children}
                </AuthProvider>
              </FeatureFlagProvider>
            </UserOptionsProvider>
          </ReduxProvider>
        </ThemeProvider>
      );
    },
  });
};

renderWithProviders(<YourActualComponentHere />, {
  featureFlag: 'demo',
  currentUser: adminUser,
});
```

This is a bit messy to write the actual `renderWithProviders()` function, but you rarely have to update it. And your tests are so much cleaner and easier to read/write.

### Tests should be as clean as production code (with a bit more copy/paste duplication)

Some codebases treat tests as messy code, with no code standards. They're like an afterthought.

I believe that test files should be *almost* as high quality as production code.

I say 'almost' as I think there are some exceptions such as:

- In TypeScript codebases, I think it is ok to use `any` or other type assertions more often. Sometimes it can make tests clearer to read (you can do `const mockData = {disabled: true} as SomeProduct` - it is clear that this test only cares about `disable

... (content truncated)
