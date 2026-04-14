---
type: twir-item
issue: 257
item: 5
item_type: item
date: 2025-11-05
source: https://blacksheepcode.com/posts/encapsulate_as_much_state_as_possible
tags:
  - "PPR"
  - "Storybook"
status: auto
quality: keep
---

[[2025-11-05-TWIR-257|Index]]

# Item 5: Encapsulate as much state as possible in your component

Source: [https://blacksheepcode.com/posts/encapsulate_as_much_state_as_possible](https://blacksheepcode.com/posts/encapsulate_as_much_state_as_possible)

Summary:
The article argues that React components should encapsulate their own state rather than relying on parent-driven state via props. While prop-driven state can make testing and Storybook usage easier, it complicates state transitions and increases boilerplate for both consumers and testers. Encapsulating state within components leads to more maintainable, reusable, and testable code, and the article demonstrates this with practical examples and test patterns.

Key takeaways:
- Prop-driven state increases complexity for consumers and makes testing state transitions awkward.
- Encapsulating state within components simplifies usage and testing of stateful behavior.
- Testing approaches differ significantly depending on where state is managed.
- Encourages designing components that own their own logic and transitions.

Recommendation:
Read fully (for React developers designing reusable components or improving testability)

Why it matters:
for React developers designing reusable components or improving testability

Content:
# Encapsulate as much state as possible in your component

*Published: October 31, 2025*

Let's say we have a nice simple component like this:

☝️ Interactive demo

Click Me

Click the button to see it transition from pending to loading to success.

You click the button, it transitions to a loading state, then it transitions to either a success or error state.

What I commonly see, is the component will be implemented with a interface like this:

```
type SpecialButtonProps = {
    onClick: () => void;
    state: "loading" | "error" | "success" | "pending";
};
```

Implementation

```
export function SpecialButton(props: SpecialButtonProps) {
    return <button onClick={props.onClick} disabled={props.state === "loading"} className={`special-button ${props.state}`}>
        {props.state === "loading" && <span>Loading...</span>}
        {props.state === "error" && <span >Error!</span>}
        {props.state === "success" && <span >Success!</span>}
        {props.state === "pending" && <span>Click Me</span>}
    </button>
}
```

Whereby every bit of state that component could be in, is controlled by the parent and passed in as props.

## Interfaces like this are a mistake

There's a sense that components with an interface like this would be easy to test, we could write something like:

```
    it("renders with pending state and correct text", () => {
        const mockOnClick = vi.fn();

        render(
            <SpecialButton
                onClick={mockOnClick}
                state="pending"
            />
        );

        expect(screen.getByRole("button")).toBeInTheDocument();
        expect(screen.getByText("Click Me")).toBeInTheDocument();
        expect(screen.getByRole("button")).not.toBeDisabled();
    });

    it("renders with loading state and is disabled", () => {
        const mockOnClick = vi.fn();

        render(
            <SpecialButton
                onClick={mockOnClick}
                state="loading"
            />
        );

        expect(screen.getByText("Loading...")).toBeInTheDocument();
        expect(screen.getByRole("button")).toBeDisabled();
    });
```

It might be desirable to to write examples like this for Storybook, where we *just* want to see the component as it is loading.

But these tests do not test one of the key aspects of what we are interested in here - the state transitions.

If we did want to test the state transitions, we could do it one of two ways:

### 1. Create a wrapper component to contain the state in

```
    it("transitions from pending to loading state", async () => {
        const TestWrapper = () => {
            const [state, setState] = React.useState<"loading" | "error" | "success" | "pending">("pending");

            const handleClick = async () => {
                await new Promise((res) => setTimeout(res, 50));
                setState("loading");
            };

            return (
                <SpecialButton
                    onClick={handleClick}
                    state={state}
                />
            );
        };

        render(<TestWrapper />);

        const button = screen.getByRole("button");

        
        expect(screen.getByText("Click Me")).toBeInTheDocument();
        expect(button).not.toBeDisabled();

        
        await userEvent.click(button);

        
        expect(await screen.findByText("Loading...")).toBeInTheDocument();
        expect(button).toBeDisabled();
    });
```

Here, we are getting a good demonstration of 'tests are test of how usable your code is' - that we're having to create a bit of external state and manage its transitions in the test, is *also what every consumer of our component is going to have to do*.

### 2. Change the props via `rerender`

```
    it("responds to prop changes when rerendered", () => {
        const mockOnClick = vi.fn();

        const { rerender } = render(
            <SpecialButton
                onClick={mockOnClick}
                state="pending"
            />
        );

        let button = screen.getByRole("button");

        
        expect(screen.getByText("Click Me")).toBeInTheDocument();
        expect(button).not.toBeDisabled();

        
        rerender(
            <SpecialButton
                onClick={mockOnClick}
                state="loading"
            />
        );

        button = screen.getByRole("button");
        expect(screen.getByText("Loading...")).toBeInTheDocument();
        expect(button).toBeDisabled();
    });
```

This is no test at all. We're simply stipulating that the props changed accurately, there's no guarantee that our parent component will in fact make this change correctly.

What this kind of interface really does, is it *makes the parent responsible for the logic of the state transition* from pending to loading to error/success.

Remember, the above example is a *very simple* component. An Autocomplete component, which we will look at later, will contain state about what text the user has entered, whether it is loading, are there results, and so forth.

## The better interface - one that encapsulates the state transitions internally.

If instead we create an interface like this:

```
type SpecialButtonProps = {
    onClick: () => Promise<{ success: boolean }>;
};
```

Note the difference being that this `onClick` handler returns a `Promise<{success: boolean}>`.

Implementation

```
export function SpecialButton2(props: SpecialButtonProps) {
    const [state, setState] = useState<"loading" | "error" | "success" | "pending">("pending");

    const handleClick = async () => {
        setState("loading");
        try {
            const result = await props.onClick();
            setState(result.success ? "success" : "error");
        } catch (error) {
            setState("error");
        }
    };

    return <button onClick={handleClick} disabled={state === "loading"} className={`special-button ${state}`}>
        {state === "loading" && <span>Loading...</span>}
        {state === "error" && <span>Error!</span>}
        {state === "success" && <span>Success!</span>}
        {state === "pending" && <span>Click Me</span>}
    </button>
}
```

Now we can write our tests like this:

```
    it("manages async operation state internally from pending to loading to success", async () => {
        const mockAsyncOperation = vi.fn().mockImplementation(
            async () => {
                await new Promise((res) => setTimeout(res, 100));
                return { success: true };
            }
        )

        render(<SpecialButton2 onClick={mockAsyncOperation} />);

        expect(mockAsyncOperation).not.toHaveBeenCalled();

        const button = screen.getByRole("button");

        
        expect(screen.getByText("Click Me")).toBeInTheDocument();
        expect(button).not.toBeDisabled();

        
        userEvent.click(button);

        
        expect(await screen.findByText("Loading...")).toBeInTheDocument();
        expect(button).toBeDisabled();

        
        await waitFor(() => {
            expect(screen.getByText("Success!")).toBeInTheDocument();
        });

        expect(button).not.toBeDisabled();
        expect(mockAsyncOperation).toHaveBeenCalledOnce();
    });
```

This is much nicer!

Our test now resembles how we're going to use the component in practise, and it's very straight forward what's happening.

## There's nothing say that you couldn't do both

Technically what we could do is do something like expose these components with less functionality as `SpecialButtonStateless` and then use this component in our `SpecialButton` component that then provides the functionality.

I think this would be of limited use - but might be helpful in a larger team with a dedicated design system, and wanting to see the component state statically.
I would argue that the functioning `SpecialButton` component that is the important for actually building the application.

## Why is this pattern so common?

I suspect a big part of the reason that this pattern is so prevalent, is because of tools like Tanstack Query, which provide an interface that, to simplify, looks like this:

```
type LoadingResult<T> = {
  data: T; 
  state: "success"
}| {
  data: null;
  state: "pending" | "error" | "loading" 
}
```

that is, they're not providing async functions as their primary means of interface.

When developers see that their means for fetching data looks like this, then they're going to tend to reproduce that interface onto the components they're creating.

RTKQ does helpfully provide a [useLazyQuery](https://redux-toolkit.js.org/rtk-query/api/created-api/hooks#uselazyquery) hook which lends itself more to the style that I advocate.

You can see [this discussion on TanStack's Github](https://github.com/TanStack/query/discussions/1205) the basic answer to why a lazy/imperative function is not provided, is because it would be trivial for someone to implement themselves.

Here is how we extract such a lazy query from TanStack - it really is not well advertised:

```
function useSearchFn() {
    const qc = useQueryClient();
    return useCallback(async (searchTerm: string) => {
        return qc.ensureQueryData({ queryKey: ['search', searchTerm], queryFn: () => search(searchTerm) });
    }, []);
}
```

We use TanStack Query's [`queryClient.ensureQueryData`](https://tanstack.com/query/v4/docs/reference/QueryClient#queryclientensurequerydata) which is essentially a lazy query that will return the data if it already cached.

This isn't at all to say that tools like Tanstack are bad. Tools like Tanstack are very useful in that they provide query deduplication and caching.

However, async functions as a particular example, are often the right abstraction to represent 'user does a thing, it loads for a bit, and then the state changes'.

## A more complex example - Autocomplete

Here we have an Autocomplete component:

☝️ Interactive demo

Enter some search terms to see the behaviour of the Autocomplete component

Hint: Use the terms 'apple', 'cherry' or 'grape'

Importantly, an autocomplete is a *non-trivial* component. Done well, an autocomplete needs to handle:

- Debouncing the search - so each keystroke doesn't trigger a new API request.
- Cancelling previous requests - we don't want a situtation where a slower earlier request clobbers the the latest request.
- Pagination - if the API response is paginated and the user scrolls the bottom of the list, we need to load more.

The above example *does not* implement these behaviours - this is an intentional decision - it represents the realistic evolution of a codebase as functionality is added or extended.

Keep this in mind.

A naive interface for this component might look like this:

```
export type AutocompleteProps<T> = {

  searchValue: string;
  onChangeSearchValue: (str: string) => void;

  onSelectValue: (value: T) => void;
  renderItem: (value: T) => React.ReactNode;

  isLoading: boolean;
  availableOptions: Array<T>;
```

And then we could use this in our application like this:

```
export function Interactive() {

    
    const [selectedValue, setSelectedValue] = React.useState<Todo | null>(null);

    const [searchValue, setSearchValue] = React.useState("");
    const [availableOptions, setAvailableOptions] = React.useState<Array<Todo>>([]);
    const [isLoading, setIsLoading] = React.useState(false);

    React.useEffect(() => {

    }, [searchValue]);

    return <div>
        <pre>
            {JSON.stringify({ selectedValue, searchValue }, null, 2)}
        </pre>
        <Autocomplete
            searchValue={searchValue}
            onChangeSearchValue={async (str) => {
                setSearchValue(str);
                if (searchValue.length < 3) {
                    setAvailableOptions([]);
                    return;
                }
                setIsLoading(true);
                try {
                    const result = await searchFn(searchValue, 1);
                }
                catch {
                    setAvailableOptions([]);
                }
                finally {
                    setIsLoading(false);
                }
            }}
            onSelectValue={(value) => {
                setSelectedValue(value);
                setSearchValue(value.name);
                setAvailableOptions([]);
            }}
            renderItem={(v) => { return <div>{v.name}</div> }}
            isLoading={isLoading}
            availableOptions={availableOptions}
        ></Autocomplete>
    </div >
}
```

The consuming component needs to manage *three* pieces of state to make this work, and needs to implement all of the loading logic.

Now imagine if you had a form that had three of these Autocompletes! Imagine if you were also handling debouncing, cancellation and pagination logic!

Chances are, the developer will be copy-pasting what they see, and copy pasting is always prone to copy paste errors.

A better interface looks like this:

```
export type AutocompleteProps<T extends Record<string, unknown>, TKey extends keyof T> = {
  searchFn: (searchTerm: string, pageNumber: number) => Promise<AutocompletePayload<T>>;
  renderItem: (item: T) => React.ReactNode;
  itemKey: TKey;

  onSelectValue?: (itemKey: TKey, itemValue: T) => void;

  
  selectedValueDisplayStringFn: (item: T) => string;
};
```

The use of it is *much* simpler:

```
export function Interactive() {
    return (
        <div>
            <Autocomplete
                searchFn={searchFn}
                renderItem={(item) => <div>{item.name} - {item.description}</div>}
                itemKey="id"
                selectedValueDisplayStringFn={(item) => item.name}
            />
        </div>
    );
}
```

And writing tests make sense:

```
        it('should select item with Enter key', async () => {
            const onSelectValue = vi.fn();
            const searchFn = createMockSearchFn(true);

            render(
                <Autocomplete
                    searchFn={searchFn}
                    renderItem={(item: TestItem) => <div>{item.name} - {item.description}</div>}
                    itemKey="id"
                    onSelectValue={onSelectValue}
                    selectedValueDisplayStringFn={(item: TestItem) => item.name}
                />
            );

            const input = screen.getByPlaceholderText('Type to search...');

            
            await user.type(input, 'apple');

            await waitFor(() => {
                expect(screen.getByText('Apple - A red fruit')).toBeInTheDocument();
            });

            expect(screen.getByRole("list")).toBeInTheDocument();

            
            await user.keyboard('{ArrowDown}');
            await user.keyboard('{Enter}');

            
            expect(onSelectValue).toHaveBeenCalledWith('id', mockItems[0]);

            await waitFor(() => {
                expect(screen.queryByRole("list")).not.toBeInTheDocument();
            });
            expect((input as HTMLInputElement).value).toBe('Apple');
        });
```

Importantly, coming back to the debouncing, cancelling, pagination logic, all of that is *encapsulated*, hidden away inside, the component - the consumer does not need to think about, it's all taken care of for them.

Now you might think that that `selectedValueDisplayStringFn` stuff doesn't really look like we're *simplifying* the interface - but we are.

The component interface is *forcing* the developer handle the transition from 'having a search term entered and selecting an item' to 'an item is selected and something is displayed in the search box', and it does this does this in a manner that can't forgotten (you'll get a type error).

The complexity of the interface comes from the inherrent complexity of the problem space - and as much as possible, the component has already done the thinking for you as a developer - and it's telling you 'these are the decision you need to make - what should be displayed when an item is selected?'.

Questions? Comments? Criticisms?

[Get in the comments! 👇](#comments)
