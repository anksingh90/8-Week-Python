
def take(gen, n):
    """Return the first n values from any generator as a list."""
    result = []
    for _ in range(n):
        try:
            val = next(gen)
            print(f'Accepting Values from infinite_even() in take() : {val}')
            result.append(val)    # Get the next item from the generator
        except StopIteration:
            break                       # Stop if the generator runs out of items before reaching n
    return result

# An infinite generator of even numbers
def infinite_evens():
    num = 0
    while True:
        print(f'Value from infinite_even() : {num}')
        yield num
        num += 1

evens = infinite_evens()    # Create the generator instance

print(take(evens, 5))       # Take only the first 5 elements
