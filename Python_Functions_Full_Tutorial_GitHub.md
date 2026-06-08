
# Python Functions – Complete Tutorial (Beginner to Advanced)

## 1. What is a Function?
A function is a reusable block of code designed to perform a specific task.

```python
def greet():
    print("Hello World")

greet()
```

### Benefits
- Code Reusability
- Better Organization
- Easier Maintenance
- Reduced Duplication

---

## 2. Creating and Calling Functions

```python
def welcome():
    print("Welcome to Python")

welcome()
```

---

## 3. Parameters and Arguments

```python
def greet(name):
    print("Hello", name)

greet("Ankit")
```

### Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Practice Questions
1. Create a function that prints a student's name.
2. Create a function that multiplies two numbers.
3. Create a function that accepts three marks and prints total.

---

## 4. Return Statement

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

### print() vs return

```python
def test():
    print("Hello")
```

```python
def test():
    return "Hello"
```

### Practice Questions
1. Return square of a number.
2. Return area of a rectangle.
3. Return reverse of a string.

---

## 5. Types of Functions

### No Arguments, No Return

```python
def display():
    print("Python")
```

### Arguments, No Return

```python
def square(n):
    print(n**2)
```

### No Arguments, Return Value

```python
def get_value():
    return 100
```

### Arguments and Return Value

```python
def multiply(a, b):
    return a * b
```

---

## 6. Default Arguments

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Ankit")
```

---

## 7. Keyword Arguments

```python
def student(name, age):
    print(name, age)

student(age=18, name="Rahul")
```

---

## 8. Variable Length Arguments (*args)

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)
```

### Practice
1. Find average using *args.
2. Find maximum value using *args.

---

## 9. Keyword Variable Arguments (**kwargs)

```python
def student(**details):
    for k, v in details.items():
        print(k, v)

student(name="Ankit", age=25)
```

---

## 10. Scope of Variables

### Local Variable

```python
def show():
    x = 10
    print(x)
```

### Global Variable

```python
x = 100

def show():
    print(x)
```

### Using global

```python
count = 0

def increase():
    global count
    count += 1
```

---

## 11. Recursive Functions

### Factorial

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

### Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Practice
1. Recursive sum of first n numbers.
2. Recursive string reversal.

---

## 12. Lambda Functions

```python
square = lambda x: x**2
print(square(5))
```

```python
add = lambda a, b: a + b
```

---

## 13. Higher Order Functions

### Function as Argument

```python
def square(x):
    return x*x

def apply(func, value):
    return func(value)
```

### Function Returning Function

```python
def outer():
    def inner():
        print("Inside Inner")
    return inner
```

---

## 14. map(), filter(), reduce()

### map()

```python
nums = [1,2,3,4]
result = list(map(lambda x:x*2, nums))
```

### filter()

```python
nums = [1,2,3,4,5,6]
result = list(filter(lambda x:x%2==0, nums))
```

### reduce()

```python
from functools import reduce

result = reduce(lambda a,b:a+b, [1,2,3,4])
```

### Practice
1. Double all numbers using map().
2. Extract odd numbers using filter().
3. Multiply all values using reduce().

---

## 15. Closures

```python
def outer(msg):
    def inner():
        print(msg)
    return inner
```

---

## 16. Decorators

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def greet():
    print("Hello")
```

### Practice
1. Logging decorator.
2. Authentication decorator.
3. Timing decorator.

---

## 17. Function Annotations (Type Hints)

```python
def add(a: int, b: int) -> int:
    return a + b
```

Benefits:
- Better IDE support
- Better readability
- Easier debugging

---

## 18. Docstrings

```python
def square(n):
    \"\"\"Returns square of a number\"\"\"
    return n*n
```

```python
print(square.__doc__)
```

---

## 19. Generator Functions

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

### Infinite Generator

```python
def counter():
    n = 1
    while True:
        yield n
        n += 1
```

---

## 20. Nested Functions

```python
def outer():
    def inner():
        print("Inner Function")
    inner()
```

---

## 21. Intermediate Topics

### Positional Only Parameters (Python 3.8+)

```python
def divide(a, b, /):
    return a / b
```

### Keyword Only Parameters

```python
def create_user(name, *, role):
    print(name, role)
```

### Unpacking Arguments

```python
def add(a, b):
    return a + b

nums = [10, 20]
print(add(*nums))
```

---

## 22. Advanced Topics

### First-Class Functions

```python
def greet():
    return "Hello"

message = greet
print(message())
```

### Function Aliasing

```python
def show():
    print("Python")

display = show
display()
```

### Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

---

## 23. Common Interview Questions

1. Difference between return and yield.
2. Difference between *args and **kwargs.
3. What is a closure?
4. What is a decorator?
5. Explain recursion with examples.
6. Why are mutable default arguments dangerous?

```python
def test(a=[]):
    a.append(1)
    return a
```

Predict the output.

---

## 24. Mini Projects

### Calculator
- Addition
- Subtraction
- Multiplication
- Division

### Student Management System
- Add Student
- Search Student
- Update Student
- Delete Student

### Bank Management System
- Deposit
- Withdraw
- Check Balance

### Employee Payroll System
- Salary Calculation
- Tax Deduction
- Bonus Calculation

---

# Mastery Checklist

- Function Creation
- Function Calling
- Parameters & Arguments
- Return Values
- Default Arguments
- Keyword Arguments
- Positional Arguments
- *args
- **kwargs
- Scope
- Recursion
- Lambda Functions
- Higher Order Functions
- map(), filter(), reduce()
- Closures
- Decorators
- Type Hints
- Docstrings
- Generators
- Nested Functions
- Advanced Function Concepts
