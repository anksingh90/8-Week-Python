# Python Tuples — Complete Tutorial

> Covers every topic from basics to advanced. Each section includes examples.
> Practice questions are at the bottom — intermediate and advanced.

---

## Table of Contents

1. [What is a Tuple?](#1-what-is-a-tuple)
2. [Creating Tuples](#2-creating-tuples)
3. [Accessing Elements — Indexing](#3-accessing-elements--indexing)
4. [Negative Indexing](#4-negative-indexing)
5. [Slicing](#5-slicing)
6. [Tuple Immutability — What it Really Means](#6-tuple-immutability--what-it-really-means)
7. [Tuple Methods](#7-tuple-methods)
8. [Iterating Over Tuples](#8-iterating-over-tuples)
9. [Tuple Packing and Unpacking](#9-tuple-packing-and-unpacking)
10. [Tuples vs Lists — When to Use Which](#10-tuples-vs-lists--when-to-use-which)
11. [Tuple as Dictionary Key](#11-tuple-as-dictionary-key)
12. [Named Tuples](#12-named-tuples)
13. [Tuples in Functions](#13-tuples-in-functions)
14. [Nested Tuples](#14-nested-tuples)
15. [zip() with Tuples](#15-zip-with-tuples)
16. [Memory and Performance](#16-memory-and-performance)
17. [Common Mistakes](#17-common-mistakes)
18. [Practice Questions — Intermediate](#18-practice-questions--intermediate)
19. [Practice Questions — Advanced](#19-practice-questions--advanced)

---

## 1. What is a Tuple?

A tuple is an **ordered, immutable, and indexed** collection. Once created, its contents cannot be changed.

| Property | Description |
|---|---|
| Ordered | Elements maintain insertion order |
| Immutable | Cannot be changed after creation |
| Indexed | Accessed by position (starts at 0) |
| Allows duplicates | Same value can appear multiple times |
| Hashable | Can be used as dictionary keys (if contents are hashable) |

```python
# A tuple holds any data types
point = (3, 7)
person = ("Alice", 25, "Engineer")
mixed = (1, "hello", 3.14, True)

print(type(point))   # <class 'tuple'>
```

The key difference from lists: **tuples signal that this data should not change**. This is intentional design, not just a restriction.

---

## 2. Creating Tuples

```python
# Empty tuple
empty = ()
empty_alt = tuple()

# Single-item tuple — MUST have trailing comma
single = (42,)
print(type(single))       # <class 'tuple'>

# Without comma — not a tuple
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

# Multiple items — parentheses are optional
coordinates = 3, 7
print(coordinates)        # (3, 7)
print(type(coordinates))  # <class 'tuple'>

# Tuple from list
from_list = tuple([1, 2, 3])
print(from_list)   # (1, 2, 3)

# Tuple from string
from_string = tuple("hello")
print(from_string) # ('h', 'e', 'l', 'l', 'o')

# Tuple from range
from_range = tuple(range(1, 6))
print(from_range)  # (1, 2, 3, 4, 5)

# Nested tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
```

---

## 3. Accessing Elements — Indexing

Indexing works exactly like lists — starts at 0.

```python
person = ("Alice", 25, "Engineer", "Mumbai")

print(person[0])   # Alice
print(person[1])   # 25
print(person[2])   # Engineer
print(person[3])   # Mumbai

# Index out of range raises IndexError
# print(person[10])  # IndexError: tuple index out of range
```

---

## 4. Negative Indexing

```python
person = ("Alice", 25, "Engineer", "Mumbai")

print(person[-1])   # Mumbai   — last element
print(person[-2])   # Engineer — second from last
print(person[-4])   # Alice    — same as person[0]
```

---

## 5. Slicing

Slicing works identically to lists. Returns a new tuple.

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[2:6])    # (2, 3, 4, 5)
print(numbers[:4])     # (0, 1, 2, 3)
print(numbers[6:])     # (6, 7, 8, 9)
print(numbers[::2])    # (0, 2, 4, 6, 8)
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# A slice of a tuple returns a tuple
result = numbers[1:4]
print(type(result))    # <class 'tuple'>
```

---

## 6. Tuple Immutability — What it Really Means

Tuples cannot be changed after creation. But the meaning of "cannot be changed" needs precision.

```python
point = (3, 7)

# Cannot reassign elements
# point[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Cannot append, remove, or sort
# point.append(1)   # AttributeError
# point.remove(3)   # AttributeError

# However — if a tuple contains a MUTABLE object, that object can still be changed
data = ([1, 2, 3], "hello", 42)

# Reassigning the reference — not allowed
# data[0] = [9, 9, 9]  # TypeError

# Modifying the mutable object inside — allowed
data[0].append(4)
print(data)   # ([1, 2, 3, 4], 'hello', 42)  — the list changed!

# The tuple itself is still the same — same list object at index 0
# The list object's contents changed, not the tuple's structure
```

### Tuple vs List mutability summary

```python
my_list  = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 99     # Works — list is mutable
# my_tuple[0] = 99  # TypeError — tuple is immutable

my_list += [4]      # Extends in place
my_tuple += (4,)    # Creates a NEW tuple — original not changed

t = (1, 2, 3)
id_before = id(t)
t += (4,)
id_after = id(t)
print(id_before == id_after)  # False — different object
```

---

## 7. Tuple Methods

Tuples have only two methods — because they are immutable.

```python
numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

# count() — number of occurrences
print(numbers.count(1))   # 2
print(numbers.count(5))   # 2
print(numbers.count(7))   # 0

# index() — first index of value
print(numbers.index(4))   # 2
print(numbers.index(5))   # 4  (first occurrence)

# index with bounds — search between start and end
print(numbers.index(5, 5, 10))   # 8

# ValueError if not found
# numbers.index(99)  # ValueError: tuple.index(x): x not in tuple

# All other common operations work via built-in functions
print(len(numbers))    # 10
print(max(numbers))    # 9
print(min(numbers))    # 1
print(sum(numbers))    # 39
print(sorted(numbers)) # returns a list, original tuple unchanged

# Concatenation — creates new tuple
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)  # (1, 2, 3, 4, 5, 6)

# Repetition
d = (0,) * 5
print(d)  # (0, 0, 0, 0, 0)
```

---

## 8. Iterating Over Tuples

```python
fruits = ("apple", "banana", "cherry")

# Simple for loop
for fruit in fruits:
    print(fruit)

# With index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Enumerate with custom start
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Iterate in reverse
for fruit in reversed(fruits):
    print(fruit)

# Iterate two tuples together
prices = (1.5, 0.8, 2.0)
for fruit, price in zip(fruits, prices):
    print(f"{fruit}: ₹{price}")

# Check membership
print("apple" in fruits)    # True
print("mango" in fruits)    # False
```

---

## 9. Tuple Packing and Unpacking

This is one of the most useful features of tuples — and it's used constantly in Python.

```python
# Packing — multiple values assigned to one tuple
point = 3, 7           # parentheses optional
person = "Alice", 25, "Engineer"
print(point)   # (3, 7)
print(person)  # ('Alice', 25, 'Engineer')

# Unpacking — values assigned to separate variables
x, y = point
print(x)  # 3
print(y)  # 7

name, age, job = person
print(name)  # Alice
print(age)   # 25

# Must match count exactly
# a, b = (1, 2, 3)  # ValueError: too many values to unpack

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]   — note: rest becomes a list

*start, last = (1, 2, 3, 4, 5)
print(start)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = (1, 2, 3, 4, 5)
print(middle)  # [2, 3, 4]

# Swap variables — uses tuple packing/unpacking internally
a, b = 10, 20
a, b = b, a    # Python creates tuple (b, a) then unpacks
print(a, b)    # 20 10

# Ignore values with _
_, second, _ = (10, 20, 30)
print(second)  # 20

# Unpacking in for loop
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"x={x}, y={y}")

# Nested unpacking
nested = ((1, 2), (3, 4))
(a, b), (c, d) = nested
print(a, b, c, d)  # 1 2 3 4
```

---

## 10. Tuples vs Lists — When to Use Which

This is a judgment call that matters for code clarity and performance.

| Scenario | Use | Reason |
|---|---|---|
| Coordinates: (x, y) | Tuple | Won't change; signals fixed structure |
| RGB color: (255, 0, 128) | Tuple | Won't change; fixed 3 values |
| Collection of items to process | List | Will change — append, remove, sort |
| Function returning multiple values | Tuple | Convention; values won't be modified |
| Dictionary key | Tuple | Lists cannot be keys; tuples can |
| Storing database rows | Tuple | Row data shouldn't change |
| Building a list iteratively | List | append() needed |
| Sequence of heterogeneous items | Tuple | (name, age, city) — different types, fixed structure |
| Homogeneous collection | List | [1, 2, 3, 4] — same type, variable size |

```python
# Tuple — fixed record, heterogeneous
student = ("Alice", 20, "Computer Science", 8.9)

# List — variable collection, homogeneous
grades = [85, 92, 78, 96, 88]

# Function returning multiple values — tuple by convention
def get_min_max(lst):
    return min(lst), max(lst)

low, high = get_min_max(grades)
print(low, high)  # 78 96

# Tuple as dict key — works
locations = {
    (28.6, 77.2): "Delhi",
    (19.0, 72.8): "Mumbai",
    (13.0, 77.5): "Bengaluru"
}
print(locations[(19.0, 72.8)])  # Mumbai

# List as dict key — fails
# d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
```

---

## 11. Tuple as Dictionary Key

Lists cannot be dictionary keys. Tuples can — because they are hashable.

```python
# Grid positions as keys
grid = {}
grid[(0, 0)] = "player"
grid[(3, 5)] = "enemy"
grid[(7, 2)] = "treasure"

print(grid[(3, 5)])   # enemy

# Check if position exists
if (0, 0) in grid:
    print("Something at origin")

# Iterate over positions
for (row, col), value in grid.items():
    print(f"At ({row},{col}): {value}")

# Adjacency representation in graphs
edges = {
    ("A", "B"): 10,
    ("A", "C"): 5,
    ("B", "C"): 3,
}
print(edges[("A", "B")])   # 10

# Tuple in a set (works — hashable)
seen_positions = set()
seen_positions.add((1, 2))
seen_positions.add((3, 4))
seen_positions.add((1, 2))   # duplicate ignored
print(seen_positions)         # {(1, 2), (3, 4)}
```

---

## 12. Named Tuples

Named tuples let you access elements by name instead of index — making code much more readable.

```python
from collections import namedtuple

# Define the structure — like a lightweight class
Point = namedtuple("Point", ["x", "y"])
Person = namedtuple("Person", ["name", "age", "city"])

# Create instances
p = Point(3, 7)
alice = Person("Alice", 25, "Mumbai")

# Access by name — readable
print(p.x)         # 3
print(p.y)         # 7
print(alice.name)  # Alice
print(alice.age)   # 25

# Access by index still works
print(p[0])        # 3

# Still immutable
# p.x = 10  # AttributeError

# Unpacking works
x, y = p
print(x, y)

# Convert to dict
print(alice._asdict())
# {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

# Replace a field — creates new named tuple
alice2 = alice._replace(city="Delhi")
print(alice)   # original unchanged
print(alice2)  # Person(name='Alice', age=25, city='Delhi')

# Named tuples work as dict keys too
cache = {}
cache[Point(0, 0)] = "origin"
print(cache[Point(0, 0)])   # origin

# Useful for representing records
Employee = namedtuple("Employee", ["id", "name", "department", "salary"])
emp = Employee(101, "Bob", "Engineering", 80000)
print(f"{emp.name} works in {emp.department}, earns ₹{emp.salary}")
```

### namedtuple with defaults (Python 3.6.1+)

```python
from collections import namedtuple

Config = namedtuple("Config", ["host", "port", "debug"])
Config.__new__.__defaults__ = ("localhost", 8080, False)

c1 = Config()
print(c1)   # Config(host='localhost', port=8080, debug=False)

c2 = Config(port=9000)
print(c2)   # Config(host='localhost', port=9000, debug=False)
```

---

## 13. Tuples in Functions

Tuples are the standard way for functions to return multiple values.

```python
# Return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([3, 1, 4, 1, 5, 9])
print(result)         # (1, 9)  — returned as tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)      # 1 9

# Return different types
def divide(a, b):
    if b == 0:
        return None, "division by zero"
    return a / b, None

value, error = divide(10, 3)
print(value)    # 3.3333...
print(error)    # None

value, error = divide(10, 0)
print(value)    # None
print(error)    # division by zero

# Function that returns tuple of stats
def describe(numbers):
    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    minimum = min(numbers)
    maximum = max(numbers)
    return n, total, mean, minimum, maximum

count, total, avg, lo, hi = describe([10, 20, 30, 40, 50])
print(f"Count: {count}, Total: {total}, Avg: {avg}, Min: {lo}, Max: {hi}")
```

---

## 14. Nested Tuples

```python
# 2D grid as tuple of tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Access — matrix[row][col]
print(matrix[0][0])   # 1
print(matrix[1][2])   # 6
print(matrix[2][1])   # 8

# Iterating
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Extract column using comprehension
col_1 = tuple(row[1] for row in matrix)
print(col_1)   # (2, 5, 8)

# Nesting depth
deep = ((1, (2, 3)), (4, (5, 6)))
print(deep[0][1][0])   # 2
print(deep[1][1][1])   # 6

# Tuple of named tuples
students = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
)

for name, score in students:
    grade = "Pass" if score >= 80 else "Fail"
    print(f"{name}: {score} — {grade}")

# Sort a tuple of tuples using sorted()
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
for name, score in sorted_students:
    print(f"{name}: {score}")
```

---

## 15. zip() with Tuples

```python
# zip creates tuples by default
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
cities = ("Mumbai", "Delhi", "Bengaluru")

zipped = list(zip(names, ages))
print(zipped)   # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Each item is a tuple
for item in zip(names, ages):
    print(type(item), item)  # <class 'tuple'>

# Zip three tuples
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")

# Unzip — transpose using zip(*)
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
unzipped_names, unzipped_ages = zip(*data)
print(unzipped_names)   # ('Alice', 'Bob', 'Charlie')
print(unzipped_ages)    # (25, 30, 35)

# Building a dict from two tuples
keys = ("name", "age", "city")
values = ("Alice", 25, "Mumbai")
person_dict = dict(zip(keys, values))
print(person_dict)  # {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
```

---

## 16. Memory and Performance

Tuples are faster and smaller than lists for fixed data.

```python
import sys
import timeit

# Size comparison
lst   = [1, 2, 3, 4, 5]
tup   = (1, 2, 3, 4, 5)

print(sys.getsizeof(lst))   # 104 bytes (approx)
print(sys.getsizeof(tup))   # 80 bytes  (approx)
# Tuple is smaller — no over-allocation for growth

# Creation speed
list_time  = timeit.timeit("[1, 2, 3, 4, 5]", number=10_000_000)
tuple_time = timeit.timeit("(1, 2, 3, 4, 5)", number=10_000_000)

print(f"List:  {list_time:.3f}s")
print(f"Tuple: {tuple_time:.3f}s")
# Tuple is faster — Python caches small tuples

# Iteration speed is roughly equal
# Access speed is roughly equal

# Tuples are hashable — can be used as set elements or dict keys
# Lists cannot
valid = {(1, 2), (3, 4), (5, 6)}
# invalid = {[1, 2], [3, 4]}  # TypeError

# When to choose tuple over list:
# - Fixed data that shouldn't change
# - Dict keys or set elements
# - Returning multiple values from functions
# - Slightly better performance for read-only access
```

---

## 17. Common Mistakes

```python
# Mistake 1: Forgetting the comma for single-element tuple
t = (42)       # This is an int, not a tuple
t = (42,)      # Correct — tuple with one item

print(type((42)))    # <class 'int'>
print(type((42,)))   # <class 'tuple'>

# Mistake 2: Trying to modify a tuple
point = (3, 7)
# point[0] = 10   # TypeError — remember, tuples are immutable

# If you need to change, convert to list and back
lst = list(point)
lst[0] = 10
point = tuple(lst)
print(point)  # (10, 7)

# Mistake 3: Confusing immutability with deep immutability
data = ([1, 2, 3], [4, 5, 6])
data[0].append(99)     # Works — inner list is mutable
print(data)            # ([1, 2, 3, 99], [4, 5, 6])
# data[0] = [9, 9, 9]  # TypeError — can't reassign slot

# Mistake 4: Trying to use a tuple with mutable contents as dict key
# t = ([1, 2], [3, 4])
# d = {t: "value"}  # TypeError: unhashable type: 'list'
# Tuples are only hashable if ALL contents are hashable

# Correct:
t = (1, 2, 3)
d = {t: "value"}   # Works — ints are hashable

# Mistake 5: Using + to add many tuples in a loop — creates many objects
result = ()
for i in range(1000):
    result += (i,)   # Creates new tuple each time — O(n²) total

# Better: build a list, convert at end
result_list = []
for i in range(1000):
    result_list.append(i)
result = tuple(result_list)  # One conversion at end

# Or use generator expression
result = tuple(i for i in range(1000))
```

---

## 18. Practice Questions — Intermediate

Solve each problem by writing Python code.

---

**Q1 — Swap Without Temp Variable**

Write a function that takes a tuple `(a, b)` and returns `(b, a)` using tuple unpacking. No temp variable allowed.

```python
def swap(t):
    # One line using unpacking
    pass

print(swap((10, 20)))    # (20, 10)
print(swap(("x", "y"))) # ('y', 'x')
```

---

**Q2 — Tuple to Dict**

Given a list of 2-element tuples, convert to a dictionary. Then write the reverse: dict to list of tuples.

```python
def tuples_to_dict(pairs):
    pass

def dict_to_tuples(d):
    pass

pairs = [("name", "Alice"), ("age", 25), ("city", "Mumbai")]
d = tuples_to_dict(pairs)
print(d)                    # {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
print(dict_to_tuples(d))    # [('name', 'Alice'), ('age', 25), ('city', 'Mumbai')]
```

---

**Q3 — Find Duplicates in a Tuple**

Write a function that returns a tuple of values that appear more than once.

```python
def find_duplicates(t):
    pass

print(find_duplicates((1, 2, 3, 2, 4, 3, 5)))  # (2, 3)
print(find_duplicates((1, 2, 3)))               # ()
```

---

**Q4 — Unzip Nested Tuples**

Given `((1, "a"), (2, "b"), (3, "c"))`, extract two tuples: `(1, 2, 3)` and `("a", "b", "c")`.

```python
def unzip(nested):
    # Use zip and *
    pass

data = ((1, "a"), (2, "b"), (3, "c"))
numbers, letters = unzip(data)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

---

**Q5 — Sort List of Tuples**

Given a list of `(name, score)` tuples, return them sorted by score descending. If scores are equal, sort by name ascending.

```python
def rank_students(students):
    pass

students = [("Alice", 85), ("Charlie", 92), ("Bob", 85), ("Diana", 78)]
print(rank_students(students))
# [('Charlie', 92), ('Alice', 85), ('Bob', 85), ('Diana', 78)]
```

---

**Q6 — Tuple Statistics**

Write a function that takes a tuple of numbers and returns a named tuple with `count`, `total`, `mean`, `minimum`, `maximum`.

```python
from collections import namedtuple

def stats(numbers):
    # Define a Stats namedtuple and return it
    pass

result = stats((10, 20, 30, 40, 50))
print(result.count)    # 5
print(result.mean)     # 30.0
print(result.minimum)  # 10
print(result.maximum)  # 50
```

---

**Q7 — Nested Unpacking**

Given `data = ((1, (2, 3)), (4, (5, 6)))`, extract all 6 numbers using nested unpacking in a for loop.

```python
data = ((1, (2, 3)), (4, (5, 6)))

for outer, (inner1, inner2) in data:
    # Print all three values
    pass

# Expected output:
# 1 2 3
# 4 5 6
```

---

**Q8 — Build a Record System**

Create a named tuple `Student` with fields `name`, `roll_no`, `marks`, `grade`. Write a function that takes a list of `Student` named tuples and returns the top scorer.

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "roll_no", "marks", "grade"])

def top_scorer(students):
    pass

students = [
    Student("Alice", 1, 92, "A"),
    Student("Bob", 2, 78, "B"),
    Student("Charlie", 3, 95, "A"),
    Student("Diana", 4, 88, "A"),
]

best = top_scorer(students)
print(f"{best.name} scored {best.marks}")  # Charlie scored 95
```

---

## 19. Practice Questions — Advanced

These require deeper thinking. Some combine tuples with other concepts.

---

**Q1 — Immutable Point Class Using Named Tuple**

Build a `Point` named tuple with `x` and `y`. Add a method `distance_to(other)` that computes Euclidean distance between two points. Named tuples don't support methods natively — figure out how to add one.

```python
# Hint: inherit from namedtuple
import math
from collections import namedtuple

# Your implementation here

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))  # 5.0
print(p2.distance_to(p1))  # 5.0
```

---

**Q2 — Tuple as Immutable Cache Key**

Write a function `cached_power(base, exponent)` that:
1. Uses a dictionary with `(base, exponent)` tuples as keys
2. Returns cached result if key exists
3. Computes and stores result if key does not exist
4. Prints whether result came from cache or was computed

```python
cache = {}

def cached_power(base, exponent):
    pass

print(cached_power(2, 10))   # Computed: 1024
print(cached_power(2, 10))   # From cache: 1024
print(cached_power(3, 5))    # Computed: 243
```

---

**Q3 — Run-Length Encoding with Tuples**

Compress a sequence using run-length encoding. Return a tuple of `(value, count)` pairs.

```python
def rle_encode(sequence):
    # Returns tuple of (value, count) namedtuples
    pass

def rle_decode(encoded):
    # Returns flattened tuple
    pass

data = (1, 1, 1, 2, 2, 3, 3, 3, 3, 1)
encoded = rle_encode(data)
print(encoded)          # ((1, 3), (2, 2), (3, 4), (1, 1))
print(rle_decode(encoded))  # (1, 1, 1, 2, 2, 3, 3, 3, 3, 1)
```

---

**Q4 — Matrix Operations Using Tuples of Tuples**

Represent a matrix as a tuple of tuples. Implement:
1. `add_matrices(a, b)` — element-wise addition
2. `multiply_matrices(a, b)` — matrix multiplication
3. `transpose(m)` — transpose

All inputs and outputs must be tuples of tuples (not lists).

```python
def add_matrices(a, b):
    pass

def transpose(m):
    pass

def multiply_matrices(a, b):
    pass

A = ((1, 2), (3, 4))
B = ((5, 6), (7, 8))

print(add_matrices(A, B))       # ((6, 8), (10, 12))
print(transpose(A))             # ((1, 3), (2, 4))
print(multiply_matrices(A, B))  # ((19, 22), (43, 50))
```

---

**Q5 — Implement a Coordinate System**

Build a system using named tuples:
- `Point2D(x, y)`
- `Line(start, end)` — where start and end are Point2D
- Write `line_length(line)` to compute length
- Write `midpoint(line)` to return midpoint as Point2D
- Write `are_parallel(line1, line2)` that returns True if two lines are parallel

```python
from collections import namedtuple
import math

# Your namedtuple definitions here

# Your functions here

p1 = Point2D(0, 0)
p2 = Point2D(4, 0)
p3 = Point2D(0, 3)
p4 = Point2D(4, 3)

l1 = Line(p1, p2)   # Horizontal line from (0,0) to (4,0)
l2 = Line(p3, p4)   # Horizontal line from (0,3) to (4,3)
l3 = Line(p1, p3)   # Vertical line from (0,0) to (0,3)

print(line_length(l1))       # 4.0
print(midpoint(l1))          # Point2D(x=2.0, y=0.0)
print(are_parallel(l1, l2))  # True
print(are_parallel(l1, l3))  # False
```

---

**Q6 — Tuple-Based Immutable Stack**

Implement a functional (immutable) stack where every operation returns a NEW stack rather than modifying in place. Use a tuple internally.

```python
class ImmutableStack:
    def __init__(self, data=()):
        self._data = data  # Tuple — never changes

    def push(self, item):
        # Return new ImmutableStack with item added
        pass

    def pop(self):
        # Return (new_stack, popped_value) tuple
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

    def __repr__(self):
        return f"Stack{self._data}"

s = ImmutableStack()
s1 = s.push(1)
s2 = s1.push(2)
s3 = s2.push(3)

print(s)     # Stack()
print(s3)    # Stack(1, 2, 3)

s4, val = s3.pop()
print(val)   # 3
print(s4)    # Stack(1, 2)
print(s3)    # Stack(1, 2, 3) — unchanged
```

---

**Q7 — Frequency Table with Sorted Named Tuple Output**

Write `frequency_table(sequence)` that:
1. Counts occurrences of each element in a sequence
2. Returns a tuple of `Item(value, count, percentage)` named tuples
3. Sorted by count descending

```python
from collections import namedtuple

Item = namedtuple("Item", ["value", "count", "percentage"])

def frequency_table(sequence):
    pass

data = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
table = frequency_table(data)

for item in table:
    print(f"{item.value}: {item.count} times ({item.percentage:.1f}%)")

# Expected:
# 4: 4 times (40.0%)
# 3: 3 times (30.0%)
# 2: 2 times (20.0%)
# 1: 1 times (10.0%)
```

---

*End of Tuples Tutorial*

> **Next:** Solve all intermediate questions without looking at solutions.
> Then attempt advanced questions. Bring stuck code to class — not the question.
>
> **Key reminder:** Whenever you find yourself asking *"should this be a list or a tuple?"* — ask *"will this change after creation?"* If no, use a tuple.
