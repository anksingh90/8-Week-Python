# Advanced Projects — Product Requirement Documents

**Course Context:** Advanced Python Course (Weeks 3–7 topics) — OOP Mastery + SQLite3 Integration  
**Purpose:** Portfolio-grade projects for GitHub, built for internship applications  
**Prerequisite Topics:** Classes & Objects, Inheritance, `super()`, Dunder Methods, `@property`, `@staticmethod`/`@classmethod`, Abstract Base Classes (ABC), Operator Overloading, Exception Handling, Context Managers, SQLite3 CRUD  

---

## How to Use This Document

Each project below is a full PRD — treat it like a real specification handed to a junior developer.  
Read the entire spec before writing any code. Build in the suggested phase order.  
Every project must end up on GitHub as its own repository with a professional README (see the GitHub Portfolio Guide for the template).

| Project | Recommended Timing | Core New Skill Emphasis |
|---|---|---|
| 1. Library Management System | After - OOP Part 1 & 2 | Composition, iteration protocol, relational SQL |
| 2. Student Result Management System | After - OOP Part 2 | Operator overloading, comparison protocol, SQL aggregation |
| 3. Inventory & Billing System | After - Exceptions/Stdlib | Custom exceptions, context managers, transactional integrity |

---

# PROJECT 1: Library Management System

<details>
  <summary>Project Details - </summary>

## 1.1 Overview

A command-line application that manages a library's book catalog, member registry, and borrowing/return transactions, backed by a persistent SQLite database.

### Problem Statement
Libraries need to track which books exist, who has borrowed them, when they're due, and calculate overdue fines. Doing this with in-memory Python lists (as in earlier mini-projects) loses all data when the program closes. This project upgrades that logic to a real, persistent, relational system.

### Target User
A librarian or library front-desk operator using a terminal-based tool — no GUI required.

---

## 1.2 Goals & Non-Goals

**Goals:**
- Persist all book, member, and transaction data across program restarts using SQLite3
- Demonstrate composition (a `Library` object owns and manages `Book` and `Member` objects)
- Demonstrate the iterator protocol (`Library` should be directly iterable)
- Demonstrate clean dunder method usage for readable object representations and equality checks
- Implement real business logic: due dates, fine calculation, borrow limits

**Non-Goals (explicitly out of scope):**
- No GUI or web interface — CLI only
- No multi-user authentication/login system
- No networked/multi-branch library support

---

## 1.3 Functional Requirements

### 1.3.1 Book Management
- Add a new book (title, author, ISBN, total copies, genre)
- Search books by title, author, or genre (partial match, case-insensitive)
- View all books with availability count (`available_copies`)
- Remove a book (only if zero copies are currently borrowed)

### 1.3.2 Member Management
- Register a new member (name, email, member ID auto-generated)
- View a member's current borrowed books and history
- Prevent duplicate registration by email

### 1.3.3 Borrowing & Returns
- Issue a book to a member:
  - Fails if no copies available (raise/handle gracefully, do not crash)
  - Fails if member already has 3 books borrowed (configurable max)
  - Sets a due date automatically (14 days from issue date)
- Return a book:
  - Calculates and displays fine if returned after due date (₹5/day late, configurable)
  - Updates `available_copies` back up
- View all currently overdue books across all members

### 1.3.4 Reports
- Most borrowed books (top 5, all-time)
- Currently borrowed books (all active transactions)
- Total fines collected (sum across returned transactions)

---

## 1.4 Object Model (OOP Design)

```
Book
 ├── attributes: isbn, title, author, genre, total_copies, available_copies
 ├── __str__     → "Title by Author (Available: X/Y)"
 ├── __repr__    → unambiguous debug representation
 └── __eq__      → two books equal if ISBN matches

Member
 ├── attributes: member_id, name, email, join_date
 ├── __str__     → "Member: Name (ID: X)"
 └── @property   → borrowed_count (computed, not stored)

Library
 ├── composes: list of Book, list of Member (backed by DB, not just in-memory)
 ├── __iter__ / __next__   → iterating over Library yields each Book
 ├── __len__               → total number of unique titles
 ├── add_book(), remove_book(), search_books()
 ├── register_member()
 ├── issue_book(), return_book()
 └── @classmethod  → Library.from_database(db_path) — alternate constructor
```

**Design requirement:** `Library` must NOT inherit from `Book` or `Member`. This is a composition relationship — the Library *has* books and members, it *is not* a book or member. Explain this distinction in your README.

---

## 1.5 Database Schema (SQLite3)

```sql
CREATE TABLE books (
    isbn TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    total_copies INTEGER NOT NULL,
    available_copies INTEGER NOT NULL
);

CREATE TABLE members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    join_date TEXT NOT NULL
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn TEXT NOT NULL,
    member_id INTEGER NOT NULL,
    issue_date TEXT NOT NULL,
    due_date TEXT NOT NULL,
    return_date TEXT,          -- NULL until returned
    fine_amount REAL DEFAULT 0,
    FOREIGN KEY (isbn) REFERENCES books(isbn),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
```

**Required SQL techniques to demonstrate:**
- `JOIN` between `transactions` and `books`/`members` for readable reports
- `GROUP BY` + `COUNT` for "most borrowed books"
- `WHERE return_date IS NULL` to find currently borrowed / overdue books

---

## 1.6 Non-Functional Requirements

- All database writes wrapped in try/except — no unhandled `sqlite3.Error` should crash the program
- Every user-facing action prints a clear success/failure message (no silent failures)
- CLI menu-driven interface (numbered options, loop until exit)
- Code must have type hints on all function signatures
- Docstrings on every class and public method

---

## 1.7 Deliverables & Grading Rubric

| Deliverable | Weight |
|---|---|
| Book/Member/Library classes with correct dunder methods | 20% |
| SQLite schema + all CRUD operations working | 25% |
| Borrow/return logic (due dates, fines, limits) correct | 20% |
| Reports (most borrowed, overdue, fines) using proper SQL | 15% |
| Error handling (no crashes on bad input) | 10% |
| GitHub repo: README, requirements.txt, clean commit history | 10% |

**Pass criteria:** All 4 functional areas (1.3.1–1.3.4) work end-to-end without crashing, and `Library` is demonstrably iterable (`for book in library:` works).

---

## 1.8 Sample Interaction

```
=== LIBRARY MANAGEMENT SYSTEM ===
1. Add Book        4. Issue Book       7. Reports
2. Search Books     5. Return Book      8. Exit
3. Register Member 6. View Overdue

Choice: 4
Enter ISBN: 9780134685991
Enter Member ID: 3
✓ "Effective Python" issued to Priya Sharma. Due: 2026-08-08

Choice: 5
Enter Transaction ID: 12
✓ Book returned. 3 days late. Fine: ₹15
```

---

## 1.9 Stretch Goals (Optional, for stronger portfolio impact)

- Export overdue report to CSV
- Add a `Reservation` feature (queue when book unavailable)
- Add `__add__` on `Library` to merge two branch libraries (advanced operator overloading)

</details>

---

# PROJECT 2: Student Result Management System

<details>
  <summary>Project Details - </summary>

## 2.1 Overview

A system that manages student academic records — subjects, marks, and computed results — with full SQL-backed persistence and rich object comparison logic. This extends the existing "School Result Management System" mini-project from a proof-of-concept into a production-style tool.

### Problem Statement
Schools need to store marks per student per subject, compute aggregate results (percentage, grade, rank), and generate report cards. The original mini-project used in-memory dicts; this version must persist everything in SQLite and support querying/sorting via both Python object comparison and raw SQL aggregation.

### Target User
A school administrator or teacher generating report cards and rank lists at the end of a term.

---

## 2.2 Goals & Non-Goals

**Goals:**
- Model `Person` as an abstract base, with `Student` and `Teacher` as concrete subclasses
- Implement full comparison protocol (`__lt__`, `__gt__`, `__eq__`) so students can be sorted by result
- Implement `__add__` for meaningful domain logic (merging term-wise results)
- Use SQL aggregation (`AVG`, `SUM`, `GROUP BY`) for rank lists and subject-topper reports
- Demonstrate `@property` for computed, always-correct values (percentage, grade)

**Non-Goals:**
- No attendance tracking
- No parent/guardian portal
- No multi-school/multi-branch support

---

## 2.3 Functional Requirements

### 2.3.1 Student & Subject Management
- Add a new student (name, roll number, class/grade)
- Add subjects with max marks (default 100) for a given class
- Enter/update marks for a student in a subject

### 2.3.2 Result Computation
- Compute total marks, percentage, and letter grade per student (A+/A/B/C/F using standard cutoffs — document your cutoffs in the README)
- Compare two students directly using Python operators: `student1 > student2` should mean "scored higher percentage"
- Merge two term results for the same student using `+` (e.g., `term1_result + term2_result` produces an averaged/combined result object)

### 2.3.3 Reports (SQL-driven)
- Class rank list (highest to lowest percentage) — via SQL `ORDER BY`
- Subject-wise topper — via SQL `GROUP BY subject, MAX(marks)`
- Class average per subject — via SQL `AVG()`
- Full report card for one student (all subjects + total + grade)

---

## 2.4 Object Model (OOP Design)

```
Person (Abstract Base Class — abc module)
 ├── attributes: name, id_number
 ├── @abstractmethod  → get_role() -> str
 └── __str__          → shared representation logic

Student(Person)
 ├── attributes: roll_number, class_grade, marks (dict: subject -> score)
 ├── @property   → percentage (computed from marks dict, not stored)
 ├── @property   → grade (derived from percentage)
 ├── __lt__, __gt__, __eq__   → compare by percentage
 ├── __add__     → combine two Student result-snapshots (e.g., term-wise) into a merged result
 └── get_role()  → returns "Student"

Teacher(Person)
 ├── attributes: subject_taught, employee_id
 └── get_role()  → returns "Teacher"

ResultManager
 ├── owns the SQLite connection
 ├── add_student(), add_marks(), compute_report_card()
 ├── get_class_rank_list()     → uses SQL ORDER BY
 └── get_subject_topper(subj)  → uses SQL GROUP BY + MAX
```

**Design requirement:** `Person` must be a true ABC (`from abc import ABC, abstractmethod`) — attempting to instantiate `Person` directly must raise `TypeError`. This is the primary reason ABC exists in this project: to guarantee every subclass implements `get_role()`.

---

## 2.5 Database Schema (SQLite3)

```sql
CREATE TABLE students (
    roll_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class_grade TEXT NOT NULL
);

CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL UNIQUE,
    max_marks INTEGER DEFAULT 100
);

CREATE TABLE marks (
    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_number INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    term TEXT NOT NULL,          -- e.g., 'Term1', 'Term2'
    score REAL NOT NULL,
    FOREIGN KEY (roll_number) REFERENCES students(roll_number),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
```

**Required SQL techniques to demonstrate:**
- Multi-table `JOIN` (students + marks + subjects) to build a full report card
- `GROUP BY roll_number` + `SUM`/`AVG` for total and percentage per student
- `GROUP BY subject_id` + `MAX(score)` for subject topper
- `ORDER BY` for rank list generation

---

## 2.6 Non-Functional Requirements

- Grade cutoffs must be defined as class-level constants, not magic numbers scattered in code
- All comparison dunder methods must handle comparison against non-Student objects gracefully (return `NotImplemented`, not crash)
- Type hints required on all methods
- Marks entry must validate: score cannot exceed subject's `max_marks`, cannot be negative

---

## 2.7 Deliverables & Grading Rubric

| Deliverable | Weight |
|---|---|
| Person ABC + Student/Teacher subclasses correctly implemented | 20% |
| Comparison protocol (`__lt__`, `__gt__`, `__eq__`) working correctly | 20% |
| `__add__` for term merging implemented meaningfully | 15% |
| SQLite schema + all CRUD + SQL aggregation reports | 25% |
| Input validation (marks range, no duplicate students) | 10% |
| GitHub repo: README, requirements.txt, clean commits | 10% |

**Pass criteria:** `sorted(list_of_students)` works correctly using natural ordering by percentage, and all 3 SQL-driven reports produce correct output against a sample dataset of at least 10 students × 5 subjects.

---

## 2.8 Sample Interaction

```
=== STUDENT RESULT MANAGEMENT SYSTEM ===
1. Add Student      4. Generate Report Card    7. Exit
2. Add Marks        5. Class Rank List
3. View Student     6. Subject Topper

Choice: 5
--- CLASS 10-A RANK LIST ---
1. Aarav Mehta     — 94.2%  (A+)
2. Diya Kapoor     — 91.8%  (A+)
3. Priya Sharma    — 87.5%  (A)
...

Choice: 6
Enter subject: Mathematics
Topper: Aarav Mehta — 98/100
```

---

## 2.9 Stretch Goals (Optional)

- Add `__sub__` to show improvement/decline between two terms
- Generate report cards as exported `.txt` or `.csv` files
- Add a `TeacherPortal` that lets a `Teacher` object only edit marks for their assigned subject

</details>

---

# PROJECT 3: Inventory & Billing System


<details>
  <summary>Project Details - </summary>


## 3.1 Overview

A point-of-sale style inventory and billing system for a small shop, combining abstract product hierarchies, custom exceptions, context managers, and transactional SQLite operations. **This project should be assigned after Week 7 (Exception Handling & Standard Library)** since it requires custom exception classes and context managers not yet covered before that point.

### Problem Statement
A small shop needs to track stock levels across different product types (perishable vs. electronic, which have different rules), process sales without ever overselling stock, and generate invoices — all while handling real-world failure cases (invalid product, insufficient stock, expired item) without the program crashing.

### Target User
A shopkeeper or billing counter operator running a terminal-based billing tool.

---

## 3.2 Goals & Non-Goals

**Goals:**
- Model an abstract `Product` base class with type-specific subclasses that behave differently
- Design and raise custom, meaningful exceptions instead of generic ones
- Use a context manager to guarantee database connections are always properly closed, even on error
- Guarantee transactional integrity: a sale either fully succeeds (stock updated + invoice recorded) or fully fails (nothing is partially written)

**Non-Goals:**
- No barcode scanner / hardware integration
- No multi-store or multi-till support
- No payment gateway integration (cash/manual entry only)

---

## 3.3 Functional Requirements

### 3.3.1 Product Management
- Add a product: name, category (`Perishable` or `Electronic`), price, quantity in stock
- `Perishable` products additionally track an expiry date
- `Electronic` products additionally track a warranty period (months)
- View all products with low-stock warning (below a configurable threshold, e.g. 5 units)
- Prevent adding a `Perishable` product with an expiry date in the past

### 3.3.2 Sales / Billing
- Create a new sale: add one or more products with quantities, compute subtotal, tax (configurable %), and grand total
- Reject the entire sale if any single item in the cart has insufficient stock — do not partially process
- Reject the sale if any `Perishable` item in the cart is already expired
- On successful sale: decrement stock for every item, store the sale + line items, print/generate an invoice

### 3.3.3 Reports
- Daily sales total
- Revenue by category (`Perishable` vs `Electronic`) via SQL `GROUP BY`
- Low-stock alert list
- Top 5 best-selling products (by quantity sold, all-time)

---

## 3.4 Custom Exception Hierarchy

```
InventoryError (base, inherits from Exception)
 ├── InsufficientStockError   → raised when requested qty > available stock
 ├── InvalidProductError      → raised when product ID doesn't exist
 ├── ExpiredProductError      → raised when attempting to sell an expired Perishable
 └── InvalidQuantityError     → raised when quantity <= 0 is requested
```

**Requirement:** Each custom exception must carry a useful message including the specific product/quantity involved (e.g., `InsufficientStockError: "Milk" requested 10, only 3 in stock`) — not a generic message.

**Requirement:** The billing flow must catch these specific exceptions (not a bare `except:`), and the CLI must display a clean, user-facing message for each — no raw tracebacks shown to the end user.

---

## 3.5 Object Model (OOP Design)

```
Product (Abstract Base Class)
 ├── attributes: product_id, name, price, quantity_in_stock
 ├── @abstractmethod  → is_valid_for_sale() -> bool
 ├── @property        → is_low_stock (computed against threshold)
 └── __str__

Perishable(Product)
 ├── attributes: expiry_date
 └── is_valid_for_sale()  → False if expiry_date < today

Electronic(Product)
 ├── attributes: warranty_months
 └── is_valid_for_sale()  → always True (no expiry concept)

DatabaseConnection (Context Manager)
 ├── __enter__   → opens sqlite3 connection, returns cursor
 ├── __exit__    → commits on success, rolls back on exception, always closes connection
 └── Must be usable as:  with DatabaseConnection(db_path) as cursor: ...

Sale
 ├── attributes: sale_id, items (list of (product, qty)), timestamp
 ├── @staticmethod  → calculate_tax(subtotal, tax_rate)
 ├── @classmethod   → Sale.from_cart(cart_items) — alternate constructor
 └── generate_invoice()  → formats a printable invoice string
```

**Design requirement:** `DatabaseConnection` must be written as a class-based context manager (using `__enter__`/`__exit__`), not the `@contextlib.contextmanager` decorator version — this project is specifically testing the class-based form. A stretch goal (3.9) allows adding the decorator version alongside it for comparison.

---

## 3.6 Database Schema (SQLite3)

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL CHECK(category IN ('Perishable', 'Electronic')),
    price REAL NOT NULL,
    quantity_in_stock INTEGER NOT NULL,
    expiry_date TEXT,          -- NULL for Electronic
    warranty_months INTEGER    -- NULL for Perishable
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_date TEXT NOT NULL,
    subtotal REAL NOT NULL,
    tax_amount REAL NOT NULL,
    grand_total REAL NOT NULL
);

CREATE TABLE sale_items (
    sale_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity_sold INTEGER NOT NULL,
    price_at_sale REAL NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

**Required SQL techniques to demonstrate:**
- Transaction handling: all writes for one sale (products stock update + sales + sale_items) must be wrapped so they commit together or not at all (this is exactly what the context manager's `__exit__` should guarantee)
- `GROUP BY category` with `SUM` for revenue-by-category report
- `JOIN` across `sale_items` + `products` for best-seller report

---

## 3.7 Non-Functional Requirements

- No sale may ever result in negative stock — this must be enforced at the database-write level, not just in Python logic (defense in depth)
- Every exception in section 3.4 must be tested with at least one deliberate failure case in your demo/`__main__` block
- Type hints required on all methods
- The `DatabaseConnection` context manager must be demonstrably safe: simulate an error mid-transaction and confirm no partial data was written

---

## 3.8 Deliverables & Grading Rubric

| Deliverable | Weight |
|---|---|
| Product ABC + Perishable/Electronic subclasses correct | 15% |
| Custom exception hierarchy, raised and handled correctly | 20% |
| Class-based context manager for DB connection, correctly rolls back on error | 20% |
| Sale/billing logic — no overselling, atomic transactions | 20% |
| SQL reports (revenue by category, best-sellers, low stock) | 15% |
| GitHub repo: README, requirements.txt, clean commits | 10% |

**Pass criteria:** Deliberately trigger each of the 4 custom exceptions in a demo and show the program handles all of them without crashing or corrupting the database. Prove atomicity by forcing a failure mid-sale and confirming stock was NOT decremented.

---

## 3.9 Sample Interaction

```
=== INVENTORY & BILLING SYSTEM ===
1. Add Product      4. New Sale         7. Reports
2. View Inventory    5. View Low Stock   8. Exit
3. Update Stock      6. Sales History

Choice: 4
Add to cart — Product ID: 12, Qty: 2
Add to cart — Product ID: 7, Qty: 15
✗ InsufficientStockError: "USB Cable" requested 15, only 8 in stock.
Sale cancelled. No changes made to inventory.

Choice: 4
Add to cart — Product ID: 12, Qty: 2
Add to cart — Product ID: 3, Qty: 1
--- INVOICE #045 ---
USB Cable x2        ₹598
Milk (1L) x1        ₹60
Subtotal:           ₹658
Tax (5%):           ₹32.90
Grand Total:        ₹690.90
✓ Sale recorded. Stock updated.
```

---

## 3.10 Stretch Goals (Optional, for stronger portfolio impact)

- Add the `@contextlib.contextmanager` decorator-based version of `DatabaseConnection` alongside the class-based one, and explain the tradeoffs in your README
- Add a `retry` decorator (from Week 6) around the sale-processing function for transient DB lock errors
- Export daily sales report to CSV automatically at end-of-day


</details>
---

# Common Requirements Across All 3 Projects

- **Language/Version:** Python 3.10+
- **Database:** `sqlite3` standard library module — no external ORM
- **Type hints:** required on all function/method signatures
- **Docstrings:** required on every class and public method
- **Git:** minimum 5 commits per project following the commit discipline in the GitHub Portfolio Guide (initial → core functionality → edge cases → tests/refactor → final + README)
- **README.md:** must include — what it does, tech stack, how to run, sample output/screenshot, features list
- **No hardcoded file paths** — use `pathlib` for any file operations
- **Demo block:** every project must have a `if __name__ == "__main__":` block that seeds sample data and demonstrates every major feature without requiring manual input, so a recruiter can run it immediately and see it work
