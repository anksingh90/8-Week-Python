# OOP in Python — Pending Topics Tutorial
## Class 1: Dunder Methods | Class 2: Abstract Base Classes | Class 3: Operator Overloading

A focused 3-class tutorial covering the remaining OOP topics before moving to Week 8. Follows the same format as the main OOP guide: mental model first, real-world analogy, code examples, then graded practice. Every practice question uses **SQLite3** for data persistence — because objects that don't get saved don't exist.

---

## Table of Contents

1. [Class 1 — Dunder Methods](#class-1--dunder-methods)
   - [\_\_str\_\_ vs \_\_repr\_\_](#1-__str__-vs-__repr__)
   - [\_\_len\_\_ and \_\_bool\_\_](#2-__len__-and-__bool__)
   - [\_\_eq\_\_, \_\_lt\_\_, \_\_gt\_\_](#3-__eq__-__lt__-__gt__)
   - [\_\_iter\_\_ and \_\_next\_\_](#4-__iter__-and-__next__)
2. [Class 2 — Abstract Base Classes (ABC)](#class-2--abstract-base-classes-abc)
   - [Why ABC Exists](#1-why-abc-exists)
   - [Defining an ABC](#2-defining-an-abc)
   - [ABC vs NotImplementedError](#3-abc-vs-notimplementederror)
3. [Class 3 — Operator Overloading via Dunder Methods](#class-3--operator-overloading-via-dunder-methods)
   - [Arithmetic Operators](#1-arithmetic-operators)
   - [\_\_contains\_\_, \_\_getitem\_\_, \_\_setitem\_\_](#2-__contains__-__getitem__-__setitem__)
   - [Mini-Project: Smart Shopping Cart](#3-mini-project-smart-shopping-cart)

---

---

# Class 1 — Dunder Methods

**Mental Model:** Every time Python does something that looks like magic — `print(obj)`, `len(obj)`, `obj == other`, `for x in obj` — it is secretly calling a special method on your object. These special methods all have double underscores on both sides: `__str__`, `__len__`, `__eq__`, `__iter__`. They are called **dunder methods** (short for *double underscore*). You define them. Python calls them automatically.

**Real-World Analogy:** Think of dunder methods as standardised plug sockets. Python's built-in functions (`print`, `len`, `sorted`, `for`) are appliances. If your class has the right socket built in, every appliance works with it out of the box. If not, you get a `TypeError`.

---

## 1. `__str__` vs `__repr__`

| Method | When Python calls it | Audience |
|---|---|---|
| `__str__` | `print(obj)`, `str(obj)` | End user |
| `__repr__` | REPL, debugging, `repr(obj)` | Developer |

**Rule:** `__str__` should be readable. `__repr__` should be unambiguous — ideally something you could paste back into Python to recreate the object.

```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        # User-facing: clean and readable
        return f'"{self.title}" by {self.author} — ₹{self.price}'

    def __repr__(self):
        # Developer-facing: unambiguous, recreatable
        return f'Book(title={self.title!r}, author={self.author!r}, price={self.price})'


b = Book("Clean Code", "Robert Martin", 599)

print(b)        # "Clean Code" by Robert Martin — ₹599       ← __str__ called
print(repr(b))  # Book(title='Clean Code', author='Robert Martin', price=599)  ← __repr__ called
```

> **Note:** If you only define `__repr__`, Python uses it as a fallback for `__str__` too. If you only define `__str__`, `repr()` falls back to the default ugly output. Always define both.

---

## 2. `__len__` and `__bool__`

`__len__` lets your object respond to `len()`. `__bool__` controls what happens when your object is used in an `if` statement or boolean context.

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        # len(cart) → number of items
        return len(self.items)

    def __bool__(self):
        # if cart → True only if cart has items
        return len(self.items) > 0


cart = ShoppingCart()
print(len(cart))    # 0
print(bool(cart))   # False

cart.add("Apple")
cart.add("Mango")
print(len(cart))    # 2
print(bool(cart))   # True

if cart:
    print("Cart has items — proceed to checkout")
else:
    print("Cart is empty")
```

> **Note:** If you define `__len__` but not `__bool__`, Python uses `len(obj) != 0` as the truth value automatically. Define `__bool__` only when you need custom logic beyond "is it non-empty."

---

## 3. `__eq__`, `__lt__`, `__gt__`

These override comparison operators. Without them, `==` compares memory addresses (two different objects are never equal, even with identical data).

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        # Two students are "equal" if they have the same marks
        return self.marks == other.marks

    def __lt__(self, other):
        # self < other
        return self.marks < other.marks

    def __gt__(self, other):
        # self > other
        return self.marks > other.marks

    def __str__(self):
        return f"{self.name} ({self.marks} marks)"


s1 = Student("Ravi", 85)
s2 = Student("Meena", 92)
s3 = Student("Arjun", 85)

print(s1 == s3)   # True  — same marks
print(s1 == s2)   # False
print(s1 < s2)    # True  — 85 < 92
print(s2 > s1)    # True

# Once __lt__ is defined, sorted() works on a list of Students
students = [s2, s1, s3]
ranked = sorted(students)
for s in ranked:
    print(s)
# Arjun (85 marks)
# Ravi (85 marks)
# Meena (92 marks)
```

> **Note:** Defining `__lt__` and `__eq__` is enough for `sorted()` to work. Python derives `<=`, `>=`, `!=` automatically if you add `@functools.total_ordering` from the `functools` module — but for most cases, defining the three above is sufficient.

---

## 4. `__iter__` and `__next__`

These turn your class into an **iterator** — something a `for` loop can walk through directly.

```python
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Must return the iterator object — here, self is the iterator
        self.current = self.start  # Reset on each new iteration
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration    # Tells the for loop to stop
        value = self.current
        self.current -= 1
        return value


cd = Countdown(5)

for num in cd:
    print(num)
# 5
# 4
# 3
# 2
# 1

# Can iterate again — __iter__ resets current
for num in cd:
    print(num, end=" ")
# 5 4 3 2 1
```

> **Note:** `__iter__` is called once at the start of a `for` loop. `__next__` is called once per iteration. When you raise `StopIteration`, the loop stops cleanly — no crash.

---

## 🧪 Practice — Class 1: Dunder Methods

**Mental model reminder:** Dunder methods are contracts with Python. When you define `__len__`, you are telling Python "this object supports `len()`". When you define `__iter__` and `__next__`, you are telling Python "this object can be looped over." SQLite3 is where the objects live between runs — implement `save()` and `load()` methods alongside the dunder methods in every question.

---

### Intermediate

**Q1 — Movie Class with Representation (\_\_str\_\_ + \_\_repr\_\_)**

Create a `Movie` class with `title`, `director`, and `year`. Implement both `__str__` and `__repr__`. Write a `save(self)` method that inserts the movie into a `movies` SQLite table. Write a `load_all()` classmethod that returns a list of `Movie` objects from the database, and uses `print()` on each (triggering `__str__`).

```python
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        # Your code here — user-friendly format
        pass

    def __repr__(self):
        # Your code here — developer format
        pass

    def save(self):
        # Your code here — insert into movies.db
        pass

    @classmethod
    def load_all(cls):
        # Your code here — return list of Movie objects
        pass
```

**Q2 — ShoppingCart with \_\_len\_\_ and \_\_bool\_\_**

Create a `ShoppingCart` class that stores items as a list. Implement `__len__` and `__bool__`. Write `save_cart(cart_id, cart)` that saves each item as a row in a `cart_items` table (`cart_id INTEGER, item TEXT`). Write `load_cart(cart_id)` that returns a `ShoppingCart` object populated from the database.

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        # Your code here
        pass

    def __bool__(self):
        # Your code here
        pass

def save_cart(cart_id, cart):
    # Your code here
    pass

def load_cart(cart_id):
    # Your code here — return a ShoppingCart object
    pass
```

---

### Advanced

**Q3 — Fibonacci Iterator with SQLite Logging**

Build a `FibonacciIterator` class that yields Fibonacci numbers up to a given limit using `__iter__` and `__next__`. Every number yielded should be logged to a `fibonacci_log` table (`run_id INTEGER, position INTEGER, value INTEGER`). Run it twice with different `run_id` values and query the table to confirm both runs are stored separately.

```python
class FibonacciIterator:
    def __init__(self, limit, run_id):
        self.limit = limit
        self.run_id = run_id
        # Your setup code here

    def __iter__(self):
        # Your code here
        pass

    def __next__(self):
        # Your code here — raise StopIteration when value exceeds limit
        # Also log each value to SQLite before returning it
        pass
```

**Q4 — Comparable Product Class with Sorted Retrieval**

Create a `Product` class (`name`, `price`, `stock`). Implement `__eq__`, `__lt__`, `__gt__` based on `price`. Save products to a `products` SQLite table. Write `get_products_sorted_by_price()` that loads all products, returns them as a list of `Product` objects sorted using Python's `sorted()` (which will use your dunder methods — not SQL ORDER BY).

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __eq__(self, other):
        # Your code here
        pass

    def __lt__(self, other):
        # Your code here
        pass

    def __gt__(self, other):
        # Your code here
        pass

    def save(self):
        # Your code here
        pass

def get_products_sorted_by_price():
    # Load from DB, return sorted list using Python sorted() — not SQL ORDER BY
    pass
```

---

---

# Class 2 — Abstract Base Classes (ABC)

**Mental Model:** An Abstract Base Class is a contract. It says: "Every class that inherits from me *must* implement these methods. No exceptions." If a subclass forgets to implement even one required method, Python refuses to let you create an object from it — you get a `TypeError` at instantiation, not a surprise crash later at runtime.

**Real-World Analogy:** A payment gateway provider gives you a specification: "Every payment method must implement `charge()` and `refund()`. We don't care how — just that you do." ABC is Python's way of enforcing that specification.

---

## 1. Why ABC Exists

Without ABC, you can define a base class with methods that raise `NotImplementedError`. But the problem is Python lets you create objects of incomplete subclasses — the error only appears when the missing method is actually *called*.

```python
# WITHOUT ABC — the problem
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Square(Shape):
    pass  # Forgot to implement area()

s = Square()    # No error here — Python lets this through
s.area()        # TypeError only appears here — too late
```

ABC catches this at the right moment — at object creation:

```python
# WITH ABC — the fix
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    pass  # Still forgot area()

s = Square()    # TypeError: Can't instantiate abstract class Square
                # without an implementation for abstract method 'area'
```

---

## 2. Defining an ABC

```python
from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def charge(self, amount):
        """Charge the customer"""
        pass

    @abstractmethod
    def refund(self, amount):
        """Refund the customer"""
        pass

    def receipt(self, amount):
        # Non-abstract — shared behaviour all subclasses get for free
        return f"Receipt: ₹{amount} processed via {self.__class__.__name__}"


class CreditCard(PaymentGateway):
    def charge(self, amount):
        return f"Credit Card charged ₹{amount}"

    def refund(self, amount):
        return f"Credit Card refunded ₹{amount}"


class UPI(PaymentGateway):
    def charge(self, amount):
        return f"UPI payment of ₹{amount} sent"

    def refund(self, amount):
        return f"UPI refund of ₹{amount} initiated"


# Works fine — both abstract methods implemented
cc = CreditCard()
upi = UPI()

print(cc.charge(500))       # Credit Card charged ₹500
print(upi.refund(200))      # UPI refund of ₹200 initiated
print(cc.receipt(500))      # Receipt: ₹500 processed via CreditCard
```

> **Note:** A class can have both abstract and non-abstract methods. Non-abstract methods in an ABC are shared implementations that subclasses inherit automatically. Abstract methods are the ones every subclass *must* override.

---

## 3. ABC vs `NotImplementedError`

| | ABC + `@abstractmethod` | `raise NotImplementedError` |
|---|---|---|
| When error occurs | At object creation | When the method is actually called |
| Enforces interface | Yes — Python checks automatically | No — developer discipline only |
| IDE support | Yes — IDEs highlight missing methods | No |
| Use in production code | Preferred | Acceptable for simple cases |

```python
# CORRECT — ABC enforces the contract
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"SMS sent: {message}"

# Polymorphism — same interface, different behaviour
notifications = [EmailNotification(), SMSNotification()]
for n in notifications:
    print(n.send("Server is down!"))
# Email sent: Server is down!
# SMS sent: Server is down!
```

---

## 🧪 Practice — Class 2: Abstract Base Classes

**Mental model reminder:** An ABC defines what a class family *must* be able to do. It enforces the interface without dictating the implementation. Every subclass in the exercises below must save its data to SQLite — that is the shared real-world constraint, just as in production systems.

---

### Intermediate

**Q1 — Employee Payroll Hierarchy**

Create an abstract `Employee` class with abstract method `calculate_pay()` and a concrete method `save(self)` that inserts into an `employees` SQLite table (`name TEXT, role TEXT, pay REAL`). Implement `FullTimeEmployee` (fixed monthly salary) and `ContractEmployee` (hourly rate × hours worked). Both must call `save()` after calculating pay.

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

    def save(self):
        pay = self.calculate_pay()
        # Your code here — insert into employees.db
        # Columns: name, role (class name), pay
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        # Your code here
        pass


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        # Your code here
        pass
```

**Q2 — Notification Service with Logging**

Create an abstract `NotificationService` with abstract method `send(message)`. Implement `EmailService` and `PushNotification`. Every `send()` call must log to a `notification_log` table (`service TEXT, message TEXT, timestamp TEXT`). Use Python's `datetime` module for the timestamp.

```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        # Your code here — send logic + log to SQLite
        pass

class PushNotification(NotificationService):
    def send(self, message):
        # Your code here — send logic + log to SQLite
        pass
```

---

### Advanced

**Q3 — Payment Gateway with Transaction History**

Build a `PaymentGateway` ABC with abstract methods `charge(amount)` and `refund(amount)`. Add a concrete method `log_transaction(type, amount)` that saves every transaction to a `transactions` table (`gateway TEXT, type TEXT, amount REAL, timestamp TEXT`). Implement `CreditCard` and `UPI` gateways. Write a `get_transaction_history(gateway_name)` function that returns all transactions for a given gateway as a formatted report.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def log_transaction(self, transaction_type, amount):
        # Your code here — insert into transactions.db
        # Use self.__class__.__name__ as gateway name
        pass


class CreditCard(PaymentGateway):
    def charge(self, amount):
        # Your code here + call self.log_transaction()
        pass

    def refund(self, amount):
        # Your code here + call self.log_transaction()
        pass


class UPI(PaymentGateway):
    def charge(self, amount):
        # Your code here + call self.log_transaction()
        pass

    def refund(self, amount):
        # Your code here + call self.log_transaction()
        pass


def get_transaction_history(gateway_name):
    # Your code here — query and return formatted report
    pass
```

---

---

# Class 3 — Operator Overloading via Dunder Methods

**Mental Model:** When Python sees `a + b`, it calls `a.__add__(b)`. When it sees `"item" in obj`, it calls `obj.__contains__("item")`. When it sees `obj[key]`, it calls `obj.__getitem__(key)`. Operator overloading lets your custom classes behave like built-in types — so domain objects like `Vector`, `Cart`, or `Money` support natural Python syntax instead of awkward method calls.

**Real-World Analogy:** A spreadsheet cell supports `+`, `-`, `*` regardless of whether it holds a number, a date, or a currency value — because whoever built those types defined what `+` means for each. You do the same for your classes.

---

## 1. Arithmetic Operators

| Dunder Method | Operator | Example |
|---|---|---|
| `__add__` | `+` | `v1 + v2` |
| `__sub__` | `-` | `v1 - v2` |
| `__mul__` | `*` | `v1 * 3` |
| `__truediv__` | `/` | `v1 / 2` |
| `__floordiv__` | `//` | `v1 // 2` |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vector(self.x // scalar, self.y // scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(4, 6)
v2 = Vector(1, 2)

print(v1 + v2)     # Vector(5, 8)
print(v1 - v2)     # Vector(3, 4)
print(v1 * 3)      # Vector(12, 18)
print(v1 / 2)      # Vector(2.0, 3.0)
print(v1 // 2)     # Vector(2, 3)
```

> **Note:** `__mul__` as written handles `v1 * 3` (Vector × scalar). For `3 * v1` to also work, you need `__rmul__` — the "right multiply" version. For most student-level use cases, `__mul__` alone is sufficient.

---

## 2. `__contains__`, `__getitem__`, `__setitem__`

These make your object support the `in` operator and subscript notation (`obj[key]`).

```python
class Cart:
    def __init__(self):
        self.items = {}     # {item_name: quantity}

    def __contains__(self, item):
        # Supports: "apple" in cart
        return item in self.items

    def __getitem__(self, item):
        # Supports: cart["apple"]
        return self.items[item]

    def __setitem__(self, item, quantity):
        # Supports: cart["apple"] = 3
        self.items[item] = quantity

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Cart({self.items})"


cart = Cart()

cart["apple"] = 3       # __setitem__
cart["mango"] = 5       # __setitem__

print(cart["apple"])    # 3          — __getitem__
print("mango" in cart)  # True       — __contains__
print("grape" in cart)  # False      — __contains__
print(len(cart))        # 2          — __len__
print(cart)             # Cart({'apple': 3, 'mango': 5})
```

---

## 3. Mini-Project: Smart Shopping Cart

**Combining all Class 3 concepts + SQLite persistence.**

Build a `SmartCart` class that supports:
- `cart["item"] = qty` — add/update item (`__setitem__`)
- `cart["item"]` — get quantity (`__getitem__`)
- `"item" in cart` — membership check (`__contains__`)
- `cart1 + cart2` — merge two carts (`__add__`)
- `cart * 2` — scale all quantities (`__mul__`)
- `repr(cart)` — developer-readable output (`__repr__`)
- `save(cart_id)` — persist to SQLite
- `load(cart_id)` — restore from SQLite

```python
import sqlite3


class SmartCart:
    def __init__(self):
        self.items = {}

    def __setitem__(self, item, quantity):
        self.items[item] = quantity

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        # Merge: quantities of matching items are summed
        merged = SmartCart()
        for item, qty in self.items.items():
            merged[item] = qty
        for item, qty in other.items.items():
            merged[item] = merged[item] + qty
        return merged

    def __mul__(self, factor):
        # Scale: all quantities multiplied by factor
        scaled = SmartCart()
        for item, qty in self.items.items():
            scaled[item] = qty * factor
        return scaled

    def __repr__(self):
        return f"SmartCart({self.items})"

    def save(self, cart_id):
        # Your code here
        # Table: cart_items (cart_id INTEGER, item TEXT, quantity INTEGER)
        pass

    @classmethod
    def load(cls, cart_id):
        # Your code here — return a SmartCart populated from SQLite
        pass


# --- Demo ---
cart1 = SmartCart()
cart1["apple"] = 3
cart1["mango"] = 2

cart2 = SmartCart()
cart2["mango"] = 1
cart2["banana"] = 4

merged = cart1 + cart2
print(merged)           # SmartCart({'apple': 3, 'mango': 3, 'banana': 4})

bulk = cart1 * 2
print(bulk)             # SmartCart({'apple': 6, 'mango': 4})

print("apple" in cart1)     # True
print("grape" in cart1)     # False
print(cart1["apple"])       # 3

cart1.save(cart_id=1)
restored = SmartCart.load(cart_id=1)
print(restored)             # SmartCart({'apple': 3, 'mango': 2})
```

---

## 🧪 Practice — Class 3: Operator Overloading

**Mental model reminder:** Operator overloading is not about being clever — it's about making domain objects speak Python naturally. A `Money` object should support `+` because you add money. A `Cart` should support `in` because you check membership. SQLite3 keeps these objects real across sessions.

---

### Intermediate

**Q1 — Money Class with Arithmetic**

Create a `Money` class (`amount`, `currency`). Implement `__add__`, `__sub__`, and `__mul__` (scalar). Raise `ValueError` if currencies don't match on add/subtract. Implement `__str__` and `__repr__`. Write `save(self)` that logs every Money object created into a `money_log` SQLite table (`amount REAL, currency TEXT`).

```python
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        # Your code here — raise ValueError if currencies differ
        pass

    def __sub__(self, other):
        # Your code here — raise ValueError if currencies differ
        pass

    def __mul__(self, scalar):
        # Your code here
        pass

    def __str__(self):
        # Your code here
        pass

    def __repr__(self):
        # Your code here
        pass

    def save(self):
        # Your code here — log to money_log table
        pass
```

**Q2 — Inventory with \_\_contains\_\_ and \_\_getitem\_\_**

Create an `Inventory` class backed by a SQLite `inventory` table (`product TEXT, stock INTEGER`). Implement `__contains__` (checks if product exists in DB), `__getitem__` (returns stock from DB), and `__setitem__` (upserts stock in DB). No in-memory dict — every operation hits SQLite directly.

```python
class Inventory:
    def __contains__(self, product):
        # Your code here — query SQLite, return True/False
        pass

    def __getitem__(self, product):
        # Your code here — return stock from SQLite
        pass

    def __setitem__(self, product, stock):
        # Your code here — INSERT or UPDATE in SQLite
        pass
```

---

### Advanced

**Q3 — Vector Library with Full Operator Suite**

Build a `Vector` class (`x`, `y`, `z` — 3D vector). Implement all five arithmetic dunder methods. Add `__eq__` (compare element-wise), `__abs__` (return magnitude using `math.sqrt`), and `__neg__` (negate all components). Write `save(self)` to a `vectors` SQLite table and `load_all()` classmethod. Find the vector with the largest magnitude from the database using `max()` with `key=abs`.

```python
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):       pass
    def __sub__(self, other):       pass
    def __mul__(self, scalar):      pass
    def __truediv__(self, scalar):  pass
    def __floordiv__(self, scalar): pass
    def __eq__(self, other):        pass
    def __abs__(self):              pass   # math.sqrt(x² + y² + z²)
    def __neg__(self):              pass   # return Vector(-x, -y, -z)
    def __repr__(self):             pass

    def save(self):
        # Your code here — insert into vectors.db
        pass

    @classmethod
    def load_all(cls):
        # Your code here — return list of Vector objects
        pass


# After saving several vectors:
# vectors = Vector.load_all()
# largest = max(vectors, key=abs)   ← uses __abs__
# print(largest)
```

---

## Self-Reflection Questions — All 3 Classes

Answer these after completing all 3 classes:

1. **Dunder Methods:** Without looking at notes — name 5 dunder methods and one real-world use case for each.

2. **ABC:** What is the practical difference between a class that raises `NotImplementedError` and one that uses `@abstractmethod`? Which would you choose for a team project and why?

3. **Operator Overloading:** When would operator overloading make code *harder* to read rather than easier? Give an example of overloading that would be confusing.

4. **Connection:** `__iter__` and `__next__` are dunder methods. How does this connect to what you learned about generators and iterators in Week 5?

5. **SQLite3 habit:** In all three classes, every object saved to SQLite. What would break in a real application if you skipped this and only kept objects in memory?

---

## Quick Reference — All 3 Classes

```
DUNDER METHODS
__str__          → print(obj)
__repr__         → repr(obj), REPL display
__len__          → len(obj)
__bool__         → bool(obj), if obj
__eq__           → obj == other
__lt__           → obj < other
__gt__           → obj > other
__iter__         → start of for loop
__next__         → each loop iteration, raise StopIteration to stop

ABSTRACT BASE CLASSES
from abc import ABC, abstractmethod
class MyABC(ABC):
    @abstractmethod
    def must_implement(self): pass

OPERATOR OVERLOADING
__add__          → obj + other
__sub__          → obj - other
__mul__          → obj * scalar
__truediv__      → obj / scalar
__floordiv__     → obj // scalar
__contains__     → item in obj
__getitem__      → obj[key]
__setitem__      → obj[key] = value
__abs__          → abs(obj)
__neg__          → -obj
```

---

**Next Step:** After completing these 3 classes → Week 8 (Type Hints, Code Quality & Git) → Path Selection (A or B).
