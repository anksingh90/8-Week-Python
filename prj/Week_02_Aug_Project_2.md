# Project 2: Library Management System

**Time needed:** 2–3 weeks, 1–2 hours a day
**What you already know that this uses:** Classes, inheritance, dunder methods, operator overloading, ABC (from Week 3 & 4)
**What's new in this project:** Saving data with SQLite3, so books and members don't disappear when you close the program

---

## 1. What Are We Building?

A program that runs a small library — like the one in your school, but digital.

You should be able to:
- Add new books to the library
- Add new members
- Issue a book to a member
- Return a book
- See which books are currently issued and to whom
- See overdue books
- Close the program and reopen it — everything is still saved (SQLite3 handles this)

---

## 2. Why This Project (Not Something Else)

- This project is a **classic** — almost every OOP course uses some version of it, because it naturally needs multiple classes working together, not just one
- It's a great way to practice **composition** (a Library "has" Books and Members, it isn't "a type of" them) — this is a concept you'll be asked about in interviews
- It gives you a clean place to practice **operator overloading**, which is one of your pending topics this week

---

## 3. The Real-World Analogy

Think of the actual library counter at your school.

- The **Book** is the physical book with a barcode (ISBN)
- The **Member** is a person with a library card
- The **Library** is the front desk — it doesn't "become" a book or a member, it just keeps track of all of them and manages the issue/return process
- The **register** (your SQLite database) is the log book that survives even after the librarian goes home

---

## 4. What You Need to Build — Step by Step

### Step 1: Design Your Classes

You'll need at least these classes:

```
Book
  - title
  - author
  - isbn (a unique ID for each book)
  - is_available (True/False)

Member
  - name
  - member_id
  - list of currently issued books

Library
  - holds all books and all members
  - handles issue_book() and return_book()
```

**Use what you already learned:**
- `__init__` for each class
- `__str__` so printing a book or member looks clean
- `__eq__` — two books are "equal" if they have the same ISBN, even if they're different Python objects. This is a great real use of operator overloading.
- If you finish ABC this week — you could make an abstract `LibraryItem` class, with `Book` as one implementation. This sets you up to add `Magazine` or `DVD` later without breaking existing code (this is optional — don't force it if it feels complicated).

**Important design point:** `Library` should use **composition**, not inheritance. A Library is not a "type of" Book or Member — it just holds and manages them. This is exactly the composition-vs-inheritance idea from Week 3's reflection question.

### Step 2: Add SQLite3 (New — but simple)

Same 4 basics as any SQLite project — connect, create table, insert, read:

```python
import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

# Books table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        isbn TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        is_available INTEGER DEFAULT 1
    )
""")

# Members table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        member_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

# Issued books table (this links a book to a member)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS issued_books (
        isbn TEXT,
        member_id INTEGER,
        issue_date TEXT,
        FOREIGN KEY (isbn) REFERENCES books(isbn),
        FOREIGN KEY (member_id) REFERENCES members(member_id)
    )
""")

connection.commit()
connection.close()
```

Note: `issued_books` links two tables together using their IDs. You don't need to fully understand SQL joins yet — you'll learn those properly in Week 9-A. For now, you can just write simple SELECT queries with a WHERE clause to check "which books does this member have."

### Step 3: Connect Your Classes to the Database

Same idea as before — your `Book` and `Member` objects need a way to save themselves and load themselves back.

Simple pattern to follow:
- `Library.add_book(book)` → saves a new row in the `books` table
- `Library.issue_book(isbn, member_id)` → checks if available, then adds a row to `issued_books` and updates `is_available` to 0
- `Library.return_book(isbn)` → removes the row from `issued_books`, sets `is_available` back to 1

### Step 4: Build the Menu

```
1. Add Book
2. Add Member
3. Issue Book
4. Return Book
5. View All Books
6. View Issued Books
7. Exit
```

---

## 5. Suggested Weekly Plan

**Week 1 (Days 1–5, ~1.5 hrs/day)**
- Write `Book`, `Member`, and `Library` classes fully — no database yet, all in memory using Python lists
- Add `__str__` and `__eq__`
- Test issue/return logic manually — make sure a book can't be issued twice

**Week 2 (Days 1–5, ~1.5 hrs/day)**
- Learn SQLite basics (connect, create table, insert, read) if not already comfortable
- Create your 3 tables (books, members, issued_books)
- Rewrite `add_book`, `add_member`, `issue_book`, `return_book` to actually save to the database instead of just an in-memory list

**Week 3 (Days 1–5, flexible, ~1–2 hrs/day)**
- Build the menu system
- Add the "view issued books" and "overdue books" features
- Handle errors — what if someone tries to issue a book that's already issued, or return a book that was never issued?
- Clean up, write the README, push to GitHub

---

## 6. What "Done" Looks Like (Checklist)

- [ ] Can add books and members, and they're saved permanently
- [ ] Can issue a book — it correctly becomes unavailable
- [ ] Can't issue the same book to two people at once (this must be blocked with a clear message)
- [ ] Can return a book — it becomes available again
- [ ] Can view a list of all currently issued books and who has them
- [ ] Program handles wrong input gracefully (no crashing)
- [ ] Code is on GitHub with a README

---

## 7. Stretch Goals (Only If You Finish Early)

- Add a due date when issuing a book, and a way to check which books are overdue
- Add a simple fine calculation (e.g., ₹5 per day overdue) — this is a nice small function to practice
- Add a search feature — find a book by title or author (partial match)

---

## 8. Operator Overloading Idea (Since It's a Pending Topic This Week)

Here's a natural way to use it in this exact project:

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __eq__(self, other):
        # Two books are the "same" if their ISBN matches
        return self.isbn == other.isbn

    def __str__(self):
        return f"{self.title} by {self.author}"
```

Now you can write `if book1 == book2:` and it compares the right thing — the ISBN — instead of comparing memory addresses. This is a clean, real example of why dunder methods matter.

---

## 9. Common Mistakes to Watch For

- Forgetting to update `is_available` when issuing or returning a book — this causes books to look "issued forever" or "always available"
- Not checking if a book is already issued before issuing it again
- Forgetting `connection.commit()` after any INSERT, UPDATE, or DELETE
- Trying to build the `issued_books` linking logic before the `books` and `members` tables are solid — get those two working perfectly first

---

**Next step:** Once this is on GitHub, Week 9-A will properly teach you SQL joins — you'll be able to rewrite your "view issued books" query the correct way, joining all three tables in one clean query instead of doing it manually in Python.
