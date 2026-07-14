# Fibonacci Generator : Write a generator fibonacci() that yields Fibonacci numbers indefinitely 
# (0, 1, 1, 2, 3, 5, 8, ...). Combine it with your take() function from Q2 to get the first 10 Fibonacci numbers.

def fibonacci():
    """Yield Fibonacci numbers indefinitely starting from 0, 1."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(gen, n):
    """Return the first n values from any generator as a list."""
    result = []
    for _ in range(n):
        try:
            result.append(next(gen))
        except StopIteration:
            break
    return result

# 1. Initialize the infinite generator
fib_gen = fibonacci()

# 2. Extract the first 10 values using take()
first_10_fibs = take(fib_gen, 10)

# 3. Print the result
print(first_10_fibs)

