
# Python Functions - 

## 1. Variable Length Arguments (Arguments (*args) & Keyword Variable Arguments (**kwargs))

### Differences Between Them - 

| Feature | `*args` (Positional) | `**kwargs` (Keyword) |
| :--- | :--- | :--- |
| **Data Structure** | Unpacks into a **Tuple** (`tuple`) | Unpacks into a **Dictionary** (`dict`) |
| **Syntax Operator** | Single asterisk `*` | Double asterisk `**` |
| **Passing Mechanism** | Passed as a sequence of unnamed values: `func(1, 2, 3)` | Passed as named key-value pairs: `func(a=1, b=2)` |
| **Ordering** | Must appear **before** `**kwargs` | Must appear **after** `*args` |
| **Empty State** | Evaluates to an empty tuple `()` | Evaluates to an empty dictionary `{}` |
<!-- 
### Key Architectural Insights Included:
* **The `*` and `**` Operators:** They act as *packing* mechanics when defining a function, and *unpacking* mechanics when invoking a function.
* **Strict Order Enforcement:** Python parsing rules mandate that formal positional parameters must come first, followed by `*args`, and finally `**kwargs`.
* **Forwarding Pattern:** Ideal for writing structural code like decorators, wrappers, and object-oriented class inheritance (e.g., passing dynamic initializers to a `super().__init__()` call). -->


*args Example - 
```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)
```

**kwargs Sample - 
```python
def student(**details):
    for k, v in details.items():
        print(k, v)

student(name="Amit", age=25)
```


### Practice
1. Find average using *args.
2. Find maximum value using *args.
3. Write a function called build_config(*args, kwargs) that accepts:
   - An arbitrary number of dictionaries (*args).
   - An arbitrary number of explicit keyword arguments (kwargs).

The function should merge all dictionaries from left to right. Finally, any explicit keyword arguments passed via kwargs must overwrite the values accumulated from the dictionaries.

```python
# Sample Inputs : 
default_layer = {"host": "localhost", "port": 8080, "secure": False}
env_layer = {"port": 9000, "debug": True}
user_layer = {"debug": False, "profile": "developer"}

# Output : 
{
    'host': 'localhost', 
    'port': 9000, 
    'secure': True, 
    'debug': False, 
    'profile': 'developer', 
    'timeout': 30
}

```


---


## 2. Scope of Variables

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

## 3. Recursive Functions

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

## 4. Lambda Functions

```python
square = lambda x: x**2
print(square(5))
```

```python
add = lambda a, b: a + b
```

---
<!--
## 5. Higher Order Functions

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
-->
---

## 5. map(), filter(), reduce()

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
<!--
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
-->
## Mini Projects

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
<!--
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
-->
