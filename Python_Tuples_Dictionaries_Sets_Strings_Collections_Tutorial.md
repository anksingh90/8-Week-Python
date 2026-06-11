# Python Tutorial: Tuples, Dictionaries, Sets, Strings & Collections

## FundaClass Academy

This tutorial covers:
- Tuples
- Dictionaries
- Sets
- Strings
- Collections Module

---

# TUPLES

## What is a Tuple?

A tuple is an ordered and immutable collection.

```python
t = (10, 20, 30)
```

## Creating Tuples

```python
t1 = (1, 2, 3)
t2 = 1, 2, 3
t3 = tuple([1, 2, 3])
```

### Single Element Tuple

```python
t = (5,)
```

> The comma is mandatory.

## Accessing Elements

```python
colors = ("red", "green", "blue")

print(colors[0])
print(colors[-1])
```

## Immutability

```python
t = (1, 2, 3)

# t[0] = 100
```

## Iteration

```python
for item in t:
    print(item)
```

## Membership Test

```python
print(2 in t)
```

## Useful Functions

```python
t = (1, 2, 2, 3)

print(len(t))
print(t.count(2))
print(t.index(3))
```

## Type Conversion

```python
lst = list(t)
t2 = tuple(lst)
```

## Slicing

```python
nums = (10, 20, 30, 40, 50)

print(nums[1:4])
print(nums[::-1])
```

## Unpacking

```python
person = ("Ankit", 25, "Delhi")

name, age, city = person
```

### Star Unpacking

```python
nums = (1, 2, 3, 4, 5)

first, *middle, last = nums
```

## Performance Comparison

```python
import sys

lst = [1,2,3]
tpl = (1,2,3)

print(sys.getsizeof(lst))
print(sys.getsizeof(tpl))
```

### Practice Questions

1. Create a tuple of 10 numbers.
2. Reverse a tuple.
3. Count occurrences of a value.
4. Convert tuple to list.
5. Unpack tuple elements.

---

# DICTIONARIES

## Creating Dictionaries

```python
student = {
    "name": "John",
    "age": 18
}
```

Using dict()

```python
student = dict(name="John", age=18)
```

## Accessing Values

```python
print(student["name"])
```

### KeyError Example

```python
# print(student["marks"])
```

## Adding and Updating

```python
student["marks"] = 95
student["age"] = 19
```

## Removing Items

```python
del student["age"]

student.pop("marks")

student.popitem()
```

## Membership Testing

```python
print("name" in student)
```

## Iteration

```python
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for k, v in student.items():
    print(k, v)
```

## Copying Safely

```python
copy_dict = student.copy()
```

## Merging Dictionaries

```python
d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
```

## Valid Key Types

Valid:

```python
data = {
    "name": "John",
    10: "Number",
    (1, 2): "Tuple"
}
```

Invalid:

```python
# {[1,2]: "value"}
```

### Practice Questions

1. Create a student dictionary.
2. Add marks field.
3. Remove a key.
4. Merge two dictionaries.
5. Print keys and values.

---

# SETS

## Creating Sets

```python
s = {1, 2, 3}

empty_set = set()
```

## Adding Elements

```python
s.add(10)
```

## Removing Elements

```python
s.remove(10)
s.discard(20)
```

```python
s.pop()
```

```python
s.clear()
```

## Iteration

```python
for item in s:
    print(item)
```

## Membership Test

```python
print(5 in s)
```

## Mathematical Operations

```python
A = {1,2,3}
B = {3,4,5}
```

### Union

```python
A.union(B)
```

### Intersection

```python
A.intersection(B)
```

### Difference

```python
A.difference(B)
```

### Symmetric Difference

```python
A.symmetric_difference(B)
```

## In-Place Updates

```python
A.update(B)
A.intersection_update(B)
A.difference_update(B)
A.symmetric_difference_update(B)
```

## Comparisons

```python
A.issubset(B)
A.issuperset(B)
A.isdisjoint(B)
```

## Copying

```python
new_set = A.copy()
```

## Frozenset

```python
fs = frozenset([1, 2, 3])
```

### Practice Questions

1. Create a set.
2. Add elements.
3. Find union and intersection.
4. Check subset relationship.
5. Create a frozenset.

---

# STRINGS

## Creating Strings

```python
name = "Python"
name2 = 'Python'
```

### Multi-line Strings

```python
text = '''Welcome
to
Python'''
```

## Escaping Quotes

```python
text = "He said \"Hello\""
```

## Indexing

```python
word = "Python"

print(word[0])
print(word[-1])
```

## Slicing

```python
print(word[0:4])
print(word[::2])
print(word[::-1])
```

## Immutability

```python
# word[0] = "J"
```

## Useful Methods

```python
text = "  Hello World  "

print(text.strip())
print(text.upper())
print(text.lower())
print(text.startswith("Hello"))
print(text.endswith("World"))
print(text.find("World"))
print(text.count("o"))
print(text.replace("World", "Python"))
```

## Split

```python
sentence = "Python is easy"

words = sentence.split()
```

## Join

```python
words = ["Python", "is", "easy"]

result = " ".join(words)
```

## String Formatting

### Percent Formatting

```python
name = "Ankit"
print("Hello %s" % name)
```

### format()

```python
print("Hello {}".format(name))
```

### f-string

```python
marks = 95

print(f"Marks = {marks}")
```

### Practice Questions

1. Reverse a string.
2. Count vowels.
3. Replace spaces with hyphens.
4. Split a sentence.
5. Join a list into a string.

---

# COLLECTIONS MODULE

```python
from collections import *
```

## Counter

```python
from collections import Counter

c = Counter("banana")

print(c)
```

### Useful Methods

```python
c.items()
c.keys()
c.values()
```

```python
c.most_common(2)
```

```python
list(c.elements())
```

### Practice

1. Count letters in a word.
2. Find top 3 most common characters.

---

## NamedTuple

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

pt = Point(10, 20)

print(pt.x)
print(pt.y)
```

### Practice

1. Create a Student namedtuple.
2. Store roll number and name.

---

## OrderedDict

```python
from collections import OrderedDict

od = OrderedDict()

od["a"] = 1
od["b"] = 2
```

> Python 3.7+ dictionaries already preserve insertion order.

---

## DefaultDict

```python
from collections import defaultdict

d = defaultdict(int)

print(d["new_key"])
```

### List Default

```python
d = defaultdict(list)

d["python"].append("easy")
```

### Practice

1. Create defaultdict(int).
2. Create defaultdict(list).

---

## Deque

```python
from collections import deque

dq = deque([1, 2, 3])
```

### Adding Elements

```python
dq.append(4)
dq.appendleft(0)
```

### Removing Elements

```python
dq.pop()
dq.popleft()
```

### Extend

```python
dq.extend([5, 6])
dq.extendleft([-2, -1])
```

### Rotate

```python
dq.rotate(2)
dq.rotate(-1)
```

### Clear

```python
dq.clear()
```

### Practice

1. Create a queue using deque.
2. Rotate elements by 3 positions.
3. Add and remove elements from both ends.

---

# Mini Projects

## Student Record System

Use:
- Dictionaries
- Strings
- Tuples

## Word Frequency Analyzer

Use:
- Counter
- Strings

## Library Management System

Use:
- Dictionaries
- Sets
- Strings

---

# End of Tutorial
