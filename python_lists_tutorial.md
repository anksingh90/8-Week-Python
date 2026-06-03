# Python Lists — Complete Tutorial

> Covers every topic from basics to advanced. Each section includes examples.
> Practice questions are at the bottom — intermediate and advanced.

---

## Table of Contents

1. [What is a List?](#1-what-is-a-list)
2. [Creating Lists](#2-creating-lists)
3. [Accessing Elements — Indexing](#3-accessing-elements--indexing)
4. [Negative Indexing](#4-negative-indexing)
5. [Slicing](#5-slicing)
6. [Modifying Lists](#6-modifying-lists)
7. [List Methods](#7-list-methods)
8. [Iterating Over Lists](#8-iterating-over-lists)
9. [Practice Questions](#practice-questions)
10. [List Comprehensions](#9-list-comprehensions)
11. [Nested Lists (2D Lists)](#10-nested-lists-2d-lists)
12. [Copying Lists](#11-copying-lists)
13. [Sorting and Reversing](#12-sorting-and-reversing)
14. [Searching in Lists](#13-searching-in-lists)
15. [List Unpacking](#14-list-unpacking)
16. [zip(), map(), filter() with Lists](#15-zip-map-filter-with-lists)
17. [List as Stack and Queue](#16-list-as-stack-and-queue)
18. [Memory and Performance](#17-memory-and-performance)
19. [Common Mistakes](#18-common-mistakes)
20. [Practice Questions — Intermediate](#19-practice-questions--intermediate)
21. [Practice Questions — Advanced](#20-practice-questions--advanced)

---

## 1. What is a List?

A list is an **ordered, mutable, and indexed** collection. It can hold any data type — even mixed types in the same list.

| Property | Description |
|---|---|
| Ordered | Elements maintain insertion order |
| Mutable | Can be changed after creation |
| Indexed | Accessed by position (starts at 0) |
| Allows duplicates | Same value can appear multiple times |

```python
# A list holds anything
my_list = [1, "hello", 3.14, True, None]
print(my_list)  # [1, 'hello', 3.14, True, None]
```

---

## 2. Creating Lists

```python
# Empty list
empty = []
empty_alt = list()

# List with values
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

# Mixed types
mixed = [1, "Python", 3.14, True]

# List from range
from_range = list(range(1, 6))
print(from_range)  # [1, 2, 3, 4, 5]

# List from string — each character becomes an element
from_string = list("hello")
print(from_string)  # ['h', 'e', 'l', 'l', 'o']

# Repeated elements
repeated = [0] * 5
print(repeated)  # [0, 0, 0, 0, 0]

# Nested list
matrix = [[1, 2], [3, 4], [5, 6]]
```

---

## 3. Accessing Elements — Indexing

Index starts at **0** for the first element.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[4])   # elderberry

# Index out of range — this raises IndexError
# print(fruits[10])  # IndexError: list index out of range
```

---

## 4. Negative Indexing

Count from the end using negative numbers. `-1` is the last element.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[-1])  # elderberry
print(fruits[-2])  # date
print(fruits[-5])  # apple  (same as fruits[0])
```

---

## 5. Slicing

Extract a portion of a list using `[start:stop:step]`.

- `start` — index to begin (included)
- `stop` — index to end (excluded)
- `step` — how many to skip (default 1)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6])    # [2, 3, 4, 5]      — index 2 up to (not including) 6
print(numbers[:4])     # [0, 1, 2, 3]      — from start up to index 4
print(numbers[6:])     # [6, 7, 8, 9]      — from index 6 to end
print(numbers[::2])    # [0, 2, 4, 6, 8]   — every second element
print(numbers[1::2])   # [1, 3, 5, 7, 9]   — odd indices
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  — reversed
print(numbers[7:2:-1]) # [7, 6, 5, 4, 3]   — step backwards

# Slicing never raises IndexError
print(numbers[0:100])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] — stops at end
```

---

## 6. Modifying Lists

Lists are mutable — you can change, add, or remove elements.

### Changing a value

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

### Changing a slice

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]
print(numbers)  # [1, 20, 30, 4, 5]

# Replace with more or fewer elements
numbers[1:3] = [200, 300, 400]
print(numbers)  # [1, 200, 300, 400, 4, 5]

# Delete a slice by replacing with empty list
numbers[1:4] = []
print(numbers)  # [1, 4, 5]
```

---

## 7. List Methods

### Adding Elements

Extract a portion of a list using `[start:stop:step]`.

- `append` — add one item at end : `[list_name.append (new_value)]`
- `insert` — add at specific index : `[list_name.insert(pos, "new_value")]`
- `extend` — add all items from another iterable : `[list_name.extend(["new_value 1", "new_value 2"])]`
- `+ operator` — creates a new list : `new_list = old_list + ["new_value 1", "new_value 2"]`
- `+= operator` — operator updates the original list directly in memory rather than creating a brand-new list : `fruits += ["new_value 1"]`

```python
fruits = ["apple", "banana"]

# append — add one item at end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# insert — add at specific index
fruits.insert(1, "avocado")
print(fruits)  # ['apple', 'avocado', 'banana', 'cherry']

# extend — add all items from another iterable
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'avocado', 'banana', 'cherry', 'date', 'elderberry']

# + operator — creates a new list
more_fruits = fruits + ["fig", "grape"]
print(more_fruits)  # original + new items

# += operator — modifies in place
fruits += ["fig"]
```

### Removing Elements

```python
numbers = [1, 2, 3, 2, 4, 2]

# remove — removes FIRST occurrence of value
numbers.remove(2)
print(numbers)  # [1, 3, 2, 4, 2]

# pop — removes and returns element at index (default: last)
last = numbers.pop()
print(last)     # 2
print(numbers)  # [1, 3, 2, 4]

popped = numbers.pop(1)
print(popped)   # 3
print(numbers)  # [1, 2, 4]

# del — delete by index or slice
del numbers[0]
print(numbers)  # [2, 4]

del numbers[:]  # clears the list (same as clear())
print(numbers)  # []

# clear — removes all elements
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # []
```

### Other Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# count — number of times value appears
print(numbers.count(1))   # 2
print(numbers.count(5))   # 2

# index — first index of value or where value exist in the list.
print(numbers.index(4))   # 2   (value found at position : 2)
print(numbers.index(5))   # 4  (first occurrence only)

# sort — sorts in place (modifies original)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]

# reverse() — reverses in place
numbers.reverse()
print(numbers)

# copy() — copy into new list value
original = [1, 2, 3]
copy = original.copy()   # Copies value from original into copy []
copy.append(4)    # adds value in new list = copy []
print(original)  # [1, 2, 3]  — unchanged
print(copy)      # [1, 2, 3, 4]
```

### Full Method Reference Table

| Method | What it does | Returns |
|---|---|---|
| `append(x)` | Add x to end | None |
| `insert(i, x)` | Add x at index i | None |
| `extend(iterable)` | Add all items from iterable | None |
| `remove(x)` | Remove first x (raises ValueError if not found) | None |
| `pop(i=-1)` | Remove and return item at index i | The removed item |
| `clear()` | Remove all items | None |
| `index(x, start, end)` | First index of x | int |
| `count(x)` | Count of x | int |
| `sort(reverse=False)` | Sort in place | None |
| `reverse()` | Reverse in place | None |
| `copy()` | Shallow copy | New list |

---

## 8. Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# Simple for loop
for fruit in fruits:
    print(fruit)

# With index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# enumerate with custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry

# While loop with index
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Iterate in reverse
for fruit in reversed(fruits):
    print(fruit)

# Iterate two lists together
prices = [1.5, 0.8, 2.0]
for fruit, price in zip(fruits, prices):
    print(f"{fruit} costs ₹{price}")
```

---

## *Practice Questions*
<details>
1. You are provided with a list of daily temperature readings. An `"anomaly"` is defined as a temperature that is strictly greater than the average of the 3 days immediately preceding it and the 3 day[...]
Q : Write a function `find_anomalies(temps)` that returns a list of tuples containing `(index, temperature)` for every anomaly found.

** Input :**
```python
temps_1 = [20, 22, 21, 24, 35, 23, 22, 24, 25, 20, 19, 30, 21, 22, 20]
print(find_anomalies(temps_1))
```

** Output :**
```python
[(4, 35), (11, 30)]
```


2. Student Marks Analyzer : 
Write a Python program that takes a list of student marks and performs the following tasks : 
- Remove all invalid marks (less than 0 or greater than 100)
- Find the highest and lowest marks using indexing / negative indexing
- Sort the valid marks in descending order
- Print the top 3 marks using slicing
- Check whether a given target mark exists in the list


** Input Data :**
```python
Enter marks separated by spaces:
78 95 102 45 -5 88 67 99 120 54
Enter the mark to search: 88

```

** Output :**
```
Original Marks:
[78, 95, 102, 45, -5, 88, 67, 99, 120, 54]

Valid Marks:
[78, 95, 45, 88, 67, 99, 54]

Highest Mark: 99
Lowest Mark: 45

Marks in Descending Order:
[99, 95, 88, 78, 67, 54, 45]

Top 3 Marks:
[99, 95, 88]

88 is present in the list.

```

3. List Packing and Unpacking Challenge : 
Write a Python program to handle a list of employee details where each employee is stored as a list like `[id, name, age, salary]`.
The program should : 

- Unpack each employee record into separate variables
- Store employees with salary above a given limit in a new list
- Sort the filtered list by salary
- Extract only the employee names using list comprehension
- Search for a particular employee ID in the list

** Sample Data :**
```python

employees = [
    [101, "Amit", 25, 35000],
    [102, "Priya", 30, 52000],
    [103, "Rohan", 28, 47000],
    [104, "Neha", 32, 60000],
    [105, "Karan", 26, 42000]
]

```
** Input Data :**
```python
Enter minimum salary: 45000
Enter Employee ID to search: 103
```

** Output :**
```
Employee Records:

ID: 101  Name: Amit   Age: 25  Salary: 35000
ID: 102  Name: Priya  Age: 30  Salary: 52000
ID: 103  Name: Rohan  Age: 28  Salary: 47000
ID: 104  Name: Neha   Age: 32  Salary: 60000
ID: 105  Name: Karan  Age: 26  Salary: 42000

Employees with Salary Above 45000:

[103, 'Rohan', 28, 47000]
[102, 'Priya', 30, 52000]
[104, 'Neha', 32, 60000]

Employee Names:
['Rohan', 'Priya', 'Neha']

Employee ID 103 Found.
```

4. 2D List Matrix Operations : 
Write a Python program that works with a 2D list representing a class timetable or marks table.

The program should :-
-  Display the 2D list in matrix form
-  Find the sum of each row
-  Find the sum of each column
-  Replace all values less than 50 with `"F"`
-  Create a copy of the original matrix before modifying it
-  Reverse the order of rows and print the updated matrix

** Input Data :**
```python
Enter number of rows: 3
Enter number of columns: 4

Enter Row 1:
78 45 90 67

Enter Row 2:
34 88 55 40

Enter Row 3:
92 71 48 60
```

** Output Data :**
```python
Original Matrix:

[78, 45, 90, 67]
[34, 88, 55, 40]
[92, 71, 48, 60]

Row Sums:
Row 1 = 280
Row 2 = 217
Row 3 = 271

Column Sums:
Column 1 = 204
Column 2 = 204
Column 3 = 193
Column 4 = 167

Modified Matrix:

[78, 'F', 90, 67]
['F', 88, 55, 'F']
[92, 71, 'F', 60]

Rows Reversed:

[92, 71, 'F', 60]
['F', 88, 55, 'F']
[78, 'F', 90, 67]
```
</details>


---

## 9. List Comprehensions

List comprehensions are the Pythonic way to build lists. They replace many for-loops.

**Syntax:** `[expression for item in iterable if condition]`

```python
# Basic — square all numbers from 0 to 9

square=[]                # Old method
for x in range(10):
    square.append(x**2)
print(square)

squares = [x**2 for x in range(10)]        # List comprehensions method
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition — even numbers only
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform strings
fruits = ["apple", "banana", "cherry"]
upper = [fruit.upper() for fruit in fruits]
print(upper)  # ['APPLE', 'BANANA', 'CHERRY']

# Filter and transform together
long_upper = [fruit.upper() for fruit in fruits if len(fruit) > 5]
print(long_upper)  # ['BANANA', 'CHERRY']

# Conditional expression (if-else in expression)
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even', 'odd']

# Nested comprehension — flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Build multiplication table as list of tuples
table = [(x, y, x*y) for x in range(1, 4) for y in range(1, 4)]
for row in table:
    print(row)
```

---

## 10. Nested Lists (2D Lists)

```python
# Creating a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements — matrix[row][column]
print(matrix[0][0])  # 1   — row 0, col 0
print(matrix[1][2])  # 6   — row 1, col 2
print(matrix[2][1])  # 8   — row 2, col 1

# Iterating
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Get a full row
print(matrix[1])     # [4, 5, 6]

# Get a full column using list comprehension
col_1 = [row[1] for row in matrix]
print(col_1)         # [2, 5, 8]

# Modifying a value
matrix[1][1] = 99
print(matrix)  # [[1, 2, 3], [4, 99, 6], [7, 8, 9]]

# Creating a 3x3 grid of zeros using comprehension
zeros = [[0] * 3 for _ in range(3)]
print(zeros)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# WARNING: This creates 3 references to the SAME inner list
wrong = [[0] * 3] * 3  # Do NOT do this
wrong[0][0] = 1
print(wrong)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  — all rows changed!
```

---

## 11. Copying Lists

This is where many bugs come from. Understand the difference between shallow and deep copy.

```python
# Assignment — NOT a copy, both point to same list
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]  — a changed too!

# Shallow copy — 3 ways
c = a.copy()
d = a[:]
e = list(a)

c.append(99)
print(a)  # [1, 2, 3, 4]  — a unchanged

# Shallow copy problem with nested lists
original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0][0] = 99       # modifies nested list
print(original)          # [[99, 2], [3, 4]]  — original affected!

shallow.append([5, 6])   # only affects shallow copy
print(original)          # [[99, 2], [3, 4]]  — original unchanged

# Deep copy — fully independent
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]]  — original fully protected
```

---

## 12. Sorting and Reversing

```python
# sort() — in-place, modifies original
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() — returns new list, original unchanged
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5]  — unchanged
print(sorted_list)  # [1, 1, 3, 4, 5]

# Sort strings
names = ["Charlie", "alice", "Bob"]
names.sort()
print(names)   # ['Bob', 'Charlie', 'alice']  — uppercase before lowercase

names.sort(key=str.lower)    # case-insensitive
print(names)   # ['alice', 'Bob', 'Charlie']

# Sort by custom key
words = ["banana", "fig", "apple", "cherry"]
words.sort(key=len)
print(words)   # ['fig', 'apple', 'banana', 'cherry']  — sorted by length

words.sort(key=len, reverse=True)
print(words)   # ['banana', 'cherry', 'apple', 'fig']

# Sort list of dicts by a field
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
]
students.sort(key=lambda s: s["grade"])
for s in students:
    print(s)

# Sort by multiple criteria — by grade descending, then name ascending
students.sort(key=lambda s: (-s["grade"], s["name"]))

# reverse() — in-place reversal
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# reversed() — returns iterator, original unchanged
for n in reversed(numbers):
    print(n)
```

---

## *Practice Questions 2*
<details>
***Question 1: The Sensor Data Cleaner***
Topics Covered: List Comprehensions (Sec 9), Sorting (Sec 12), Slicing (Sec 5).
Scenario: An IoT sensor records temperature data, but sometimes it glitches and records a 0.
Task:
Write a program that takes a list of raw sensor readings.
- Use a list comprehension to create a new list that excludes all 0 readings.
- Sort this new list in descending order (highest to lowest).
- Use slicing to extract and print only the top 3 highest valid readings.

Sample Data : 
** Input Data**
    
    ```python
    raw_readings = [15, 0, 42, 0, 8, 99, 0, 23, 56, 4, 102]
    ```
** Output Data :**
    ```python
    Cleaned Data: [102, 99, 56, 42, 23, 15, 8, 4]
    Top 3 Readings: [102, 99, 56]
    ```
Question 2: Matrix Column Extraction & Mutation
Topics Covered: Nested Lists (Sec 10), List Comprehensions (Sec 9), Modifying Lists (Sec 6), Sorting (Sec 12).
Scenario: You have a 3x3 matrix representing scores in 3 different subjects across 3 different classes.
Task:
- Using a list comprehension, extract the 2nd column (index 1) of the matrix into a brand new 1D list.
- Sort this extracted 1D list in ascending order.
- Replace the entire 1st row (index 0) of the original matrix with this newly sorted list.
- Print the extracted column and the fully modified matrix.

Sample Input Data:
** Input Data**
```python
matrix = [
    [10, 88, 3],
    [5, 42, 7],
    [9, 99, 1]
]
```

** Output Data :**
```python
Extracted 2nd Column: [88, 42, 99]
Sorted Column: [42, 88, 99]

Modified Matrix:
[42, 88, 99]
[5, 42, 7]
[9, 99, 1]
```


</details>



---

## 13. Searching in Lists

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# in operator — check membership
print("banana" in fruits)    # True
print("mango" in fruits)     # False
print("mango" not in fruits) # True

# index() — find position of first occurrence
print(fruits.index("banana"))   # 1

# index() with bounds
print(fruits.index("banana", 2))   # 3  (search from index 2)

# count()
print(fruits.count("banana"))  # 2

# Linear search function
def find_all(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

print(find_all(fruits, "banana"))  # [1, 3]

# any() and all()
numbers = [1, 2, 3, 4, 5]
print(any(x > 4 for x in numbers))    # True  — at least one > 4
print(all(x > 0 for x in numbers))    # True  — all positive
print(all(x > 3 for x in numbers))    # False — not all > 3
```

---

## 14. List Unpacking

```python
# Basic unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3

# Must match count exactly
# a, b = [1, 2, 3]  # ValueError: too many values to unpack

# Extended unpacking with *
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*start, last = [1, 2, 3, 4, 5]
print(start)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Swapping values — Pythonic way
x, y = 10, 20
x, y = y, x
print(x, y)  # 20 10

# Unpacking nested list
point = [3, 7]
x, y = point
print(f"x={x}, y={y}")

# Ignoring values with _
_, second, _ = [10, 20, 30]
print(second)  # 20

# Unpacking in for loop
pairs = [(1, "one"), (2, "two"), (3, "three")]
for number, word in pairs:
    print(f"{number} = {word}")
```

---

## 15. zip(), map(), filter() with Lists

```python
# zip() — combine multiple lists element by element
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

combined = list(zip(names, scores))
print(combined)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")

# zip stops at shortest list
a = [1, 2, 3]
b = [10, 20]
print(list(zip(a, b)))  # [(1, 10), (2, 20)]  — 3 is ignored

# Unzip using zip(*list)
zipped = [(1, "a"), (2, "b"), (3, "c")]
numbers, letters = zip(*zipped)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

# map() — apply function to every element
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# map with named function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# filter() — keep only elements that pass condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Prefer list comprehensions over map/filter — more readable
evens_comp = [x for x in numbers if x % 2 == 0]
```

---

## 16. List as Stack and Queue

```python
# STACK — Last In First Out (LIFO)
# Use append() to push, pop() to pop
stack = []
stack.append("first")
stack.append("second")
stack.append("third")

print(stack.pop())  # third  — last in, first out
print(stack.pop())  # second
print(stack)        # ['first']

# QUEUE — First In First Out (FIFO)
# Use append() to enqueue, pop(0) to dequeue
# WARNING: pop(0) on a list is O(n) — use collections.deque instead

from collections import deque

queue = deque()
queue.append("first")
queue.append("second")
queue.append("third")

print(queue.popleft())  # first  — first in, first out
print(queue.popleft())  # second
print(queue)            # deque(['third'])
```

---

## 17. Memory and Performance

```python
import sys

# List takes more memory than generator
lst = [x**2 for x in range(1000)]
gen = (x**2 for x in range(1000))

print(sys.getsizeof(lst))  # ~8856 bytes
print(sys.getsizeof(gen))  # ~104 bytes — generator stores formula, not values

# Time complexity of common operations
# Access by index   O(1)     — instant
# Append            O(1)     — amortized constant
# Insert at index   O(n)     — shifts elements
# Delete at index   O(n)     — shifts elements
# Search (in)       O(n)     — checks every element
# Sort              O(n log n)

# Prefer set for membership check when list is large
big_list = list(range(1_000_000))
big_set = set(range(1_000_000))

# 999999 in big_list  → O(n) — slow
# 999999 in big_set   → O(1) — instant

# Pre-allocate with multiplication when size is known
zeros = [0] * 1000   # faster than appending 1000 times
```

---

## 18. Common Mistakes

```python
# Mistake 1: Aliasing instead of copying
a = [1, 2, 3]
b = a        # b is NOT a copy — same list
b.append(4)
print(a)     # [1, 2, 3, 4]  BUG

# Fix:
b = a.copy()

# Mistake 2: Mutable default argument in function
def add_item(item, lst=[]):  # lst=[] is created ONCE, shared across calls
    lst.append(item)
    return lst

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b']  — BUG: not a fresh list

# Fix:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Mistake 3: Modifying a list while iterating over it
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)  # BUG: skips elements

print(numbers)  # [1, 3, 5]  — looks right but 4 was skipped!

# Fix: iterate over a copy
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)

# Better fix: list comprehension
numbers = [n for n in numbers if n % 2 != 0]

# Mistake 4: Using list instead of set for membership
# O(n) every time — slow for large lists
if value in [1, 2, 3, 4, 5]:  # slow
    pass

if value in {1, 2, 3, 4, 5}:  # fast — use set literal
    pass

# Mistake 5: Wrong nested list creation
grid = [[0] * 3] * 3    # All rows are same object
grid[0][0] = 1
print(grid)             # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  BUG

# Fix:
grid = [[0] * 3 for _ in range(3)]
```

---

## 19. Practice Questions — Intermediate

Solve each problem by writing Python code. Do not use built-in sort for Q3 and Q4.

---

**Q1 — Remove Duplicates (preserve order)**

Given `[1, 3, 2, 1, 5, 3, 6, 2]`, write a function that returns `[1, 3, 2, 5, 6]` — duplicates removed but order preserved.

```python
def remove_duplicates(lst):
    # Your code here
    pass

print(remove_duplicates([1, 3, 2, 1, 5, 3, 6, 2]))  # [1, 3, 2, 5, 6]
```

---

**Q2 — Rotate List**

Write a function `rotate(lst, k)` that rotates the list left by k positions.
`rotate([1, 2, 3, 4, 5], 2)` → `[3, 4, 5, 1, 2]`

```python
def rotate(lst, k):
    # Your code here
    pass

print(rotate([1, 2, 3, 4, 5], 2))  # [3, 4, 5, 1, 2]
print(rotate([1, 2, 3], 5))         # [3, 1, 2]  — handle k > len
```

---

**Q3 — Bubble Sort**

Implement bubble sort from scratch. Do not use sort() or sorted().

```python
def bubble_sort(lst):
    # Your code here
    pass

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
```

---

**Q4 — Second Largest**

Write a function that returns the second largest element in a list without sorting.

```python
def second_largest(lst):
    # Your code here
    pass

print(second_largest([10, 5, 20, 8, 15]))  # 15
print(second_largest([5, 5, 5]))            # None (no second largest)
```

---

**Q5 — Chunk a List**

Write `chunk(lst, size)` that splits a list into sublists of given size.
`chunk([1,2,3,4,5,6,7], 3)` → `[[1,2,3], [4,5,6], [7]]`

```python
def chunk(lst, size):
    # Your code here
    pass

print(chunk([1, 2, 3, 4, 5, 6, 7], 3))  # [[1, 2, 3], [4, 5, 6], [7]]
```

---

**Q6 — Flatten Nested List (one level)**

Given `[[1, 2], [3, 4], [5, 6]]`, return `[1, 2, 3, 4, 5, 6]` using a list comprehension.

```python
def flatten(nested):
    # One line using list comprehension
    pass

print(flatten([[1, 2], [3, 4], [5, 6]]))  # [1, 2, 3, 4, 5, 6]
```

---

**Q7 — Merge Two Sorted Lists**

Given two sorted lists, merge them into one sorted list without using sort().

```python
def merge_sorted(a, b):
    # Your code here
    pass

print(merge_sorted([1, 3, 5, 7], [2, 4, 6, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print(merge_sorted([1, 2, 9], [3, 4, 5]))          # [1, 2, 3, 4, 5, 9]
```

---

**Q8 — Matrix Transpose**

Transpose a 2D matrix (rows become columns) without any library.

```python
def transpose(matrix):
    # Your code here
    pass

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Expected:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
print(transpose(matrix))
```

---

## 20. Practice Questions — Advanced

These require deeper thinking. Some combine multiple concepts.

---

**Q1 — Deep Flatten**

Flatten a list that may be nested to any depth.
`[1, [2, [3, [4, 5]], 6], 7]` → `[1, 2, 3, 4, 5, 6, 7]`

```python
def deep_flatten(lst):
    # Hint: use recursion
    pass

print(deep_flatten([1, [2, [3, [4, 5]], 6], 7]))  # [1, 2, 3, 4, 5, 6, 7]
```

---

**Q2 — Group Consecutive Duplicates**

Given `[1, 1, 2, 3, 3, 3, 4, 4, 1]`, group into `[[1,1], [2], [3,3,3], [4,4], [1]]`.

```python
def group_consecutive(lst):
    # Your code here
    pass

print(group_consecutive([1, 1, 2, 3, 3, 3, 4, 4, 1]))
# [[1, 1], [2], [3, 3, 3], [4, 4], [1]]
```

---

**Q3 — Sliding Window Maximum**

Given a list and window size k, return the max value in each window.
`sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3)` → `[3, 3, 5, 5, 6, 7]`

```python
def sliding_max(lst, k):
    # Your code here
    pass

print(sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
```

---

**Q4 — Implement a Stack Class Using a List**

Build a `Stack` class with `push`, `pop`, `peek`, `is_empty`, and `size`. Raise a custom `StackUnderflowError` when popping from empty stack.

```python
class StackUnderflowError(Exception):
    pass

class Stack:
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass  # Raise StackUnderflowError if empty

    def peek(self):
        pass  # Return top without removing

    def is_empty(self):
        pass

    def size(self):
        pass

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())   # 3
print(s.pop())    # 3
print(s.size())   # 2
```

---

**Q5 — Merge Sort Implementation**

Implement merge sort from scratch. This is O(n log n) — understand why.

```python
def merge_sort(lst):
    # Divide: split in half until single elements
    # Conquer: merge sorted halves
    pass

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # [3, 9, 10, 27, 38, 43, 82]
```

---

**Q6 — Find All Pairs with Given Sum**

Given a list and a target, find all unique pairs that sum to the target.
`find_pairs([1, 5, 3, 7, 4, 2, 6], 8)` → `[(1,7), (2,6), (3,5)]`

```python
def find_pairs(lst, target):
    # Use a set for O(n) solution
    pass

print(find_pairs([1, 5, 3, 7, 4, 2, 6], 8))  # [(1, 7), (2, 6), (3, 5)]
```

---

**Q7 — Run-Length Encoding**

Compress `[1,1,1,2,2,3,3,3,3,1]` to `[(1,3),(2,2),(3,4),(1,1)]` (value, count) pairs. Then write the decoder.

```python
def encode(lst):
    pass

def decode(encoded):
    pass

data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
encoded = encode(data)
print(encoded)            # [(1, 3), (2, 2), (3, 4), (1, 1)]
print(decode(encoded))    # [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
```

---

**Q8 — Custom sort without sort()**

Implement insertion sort. Then modify it to accept a `key` function the same way Python's built-in `sorted(key=...)` works.

```python
def insertion_sort(lst, key=None):
    # Sort in place using insertion sort
    # If key is provided, use it for comparison
    pass

data = ["banana", "fig", "apple", "cherry"]
insertion_sort(data, key=len)
print(data)   # ['fig', 'apple', 'banana', 'cherry']

nums = [3, 1, 4, 1, 5]
insertion_sort(nums)
print(nums)   # [1, 1, 3, 4, 5]
```

---

*End of Lists Tutorial*

> **Next:** Solve all intermediate questions without looking at solutions.
> Then attempt advanced questions. Bring stuck code to class — not the question.
