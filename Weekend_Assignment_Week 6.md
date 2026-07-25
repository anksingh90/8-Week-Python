# Week 4 — Weekend Mini Project
## School Management System

**Topics Covered:** Classes & Objects · Class Methods & Self · Inheritance · Encapsulation · Polymorphism · SQLite3

---

## Overview

Build a School Management System that manages **students, teachers, and staff** in a single SQLite database.

All three are types of `Person` — but each behaves differently when asked what their role is, what they do, and how much they are paid.

---

## OOP Concepts Used

| Concept | Where It Appears |
|---|---|
| **Classes & Objects** | `Person`, `Student`, `Teacher`, `Staff` are classes. Every record created is an object with its own data |
| **Class Methods & Self** | `setup_db()` and `show_all()` use `@classmethod`. Every instance method uses `self` to access its own data |
| **Inheritance** | `Student`, `Teacher`, `Staff` all inherit from `Person` and get `name`, `age`, `save()`, `show_all()` for free |
| **Encapsulation** | `__age` in `Person` and `__salary` in `Teacher`/`Staff` are private with property setters that reject invalid values |
| **Polymorphism** | A single loop saves all 5 objects. `get_role()` and `get_details()` are overridden in every child class and return different output depending on which object calls them |

---

## Database Structure

**Database file:** `school_management.db`  
**Table:** `persons`

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-assigned row ID |
| `name` | TEXT | Person's name |
| `age` | INTEGER | Person's age |
| `role` | TEXT | Student / Teacher / Staff |
| `detail` | TEXT | Role-specific info |
| `salary` | REAL | 0 for students |

---

## What to Build

### Base Class — `Person`

- Attributes: `name`, `__age` (private)
- `age` property with setter — reject values below `5` and above `80`
- `get_role()` — returns `"Person"`
- `get_details()` — returns formatted string with name, age, role
- `save()` — inserts record into `school_management.db`, stores the assigned row ID
- `setup_db()` — class method, creates the table
- `show_all()` — class method, reads and prints all records from DB

---

### Child Class — `Student` (inherits from `Person`)

- Additional attributes: `student_id`, `grade`
- Override `get_role()` — returns `"Student"`
- Override `get_details()` — returns name, age, student ID, grade
- Salary stored as `0` in DB
- `promote()` — increases grade by 1, runs `UPDATE` query to sync to DB

---

### Child Class — `Teacher` (inherits from `Person`)

- Additional attributes: `subject`, `__salary` (private)
- `salary` property with setter — reject values below `10000`
- Override `get_role()` — returns `"Teacher"`
- Override `get_details()` — returns name, age, subject, salary
- `give_raise(amount)` — adds amount to salary, runs `UPDATE` query to sync to DB

---

### Child Class — `Staff` (inherits from `Person`)

- Additional attributes: `department`, `__salary` (private)
- `salary` property with setter — reject values below `8000`
- Override `get_role()` — returns `"Staff"`
- Override `get_details()` — returns name, age, department, salary
- `transfer(new_department)` — changes department, runs `UPDATE` query to sync to DB

---

## Steps to Follow

**Step 1** — Setup the database

**Step 2** — Create these objects:
- 2 Students
- 2 Teachers
- 1 Staff member

**Step 3** — Save all 5 objects to DB using a **single loop** — polymorphism in action. Every object calls `save()` but each stores its own role and details automatically.

**Step 4** — Print all records using `show_all()`

**Step 5** — Run these operations and sync each to DB:
- Promote one student
- Give a raise to one teacher
- Transfer the staff member to a new department

**Step 6** — Print all records again to confirm DB reflects all changes

---

## Expected Output

```
=== SCHOOL MANAGEMENT SYSTEM ===

Setting up database...

Creating records...
Saved: Student | Aarav    | Age 16 | Grade 10
Saved: Student | Priya    | Age 15 | Grade 9
Saved: Teacher | Mr. Sharma | Age 42 | Maths   | ₹45000
Saved: Teacher | Ms. Nair   | Age 35 | Science | ₹40000
Saved: Staff   | Ravi     | Age 38 | Administration | ₹15000

--- All Records ---
ID: 1 | Student  | Aarav      | Age 16 | Grade 10       | ₹0
ID: 2 | Student  | Priya      | Age 15 | Grade 9        | ₹0
ID: 3 | Teacher  | Mr. Sharma | Age 42 | Maths          | ₹45000
ID: 4 | Teacher  | Ms. Nair   | Age 35 | Science        | ₹40000
ID: 5 | Staff    | Ravi       | Age 38 | Administration | ₹15000

Running updates...
Aarav promoted to Grade 11. DB updated.
Mr. Sharma salary updated to ₹50000. DB updated.
Ravi transferred to Accounts. DB updated.

--- Updated Records ---
ID: 1 | Student  | Aarav      | Age 16 | Grade 11 | ₹0
ID: 2 | Student  | Priya      | Age 15 | Grade 9  | ₹0
ID: 3 | Teacher  | Mr. Sharma | Age 42 | Maths    | ₹50000
ID: 4 | Teacher  | Ms. Nair   | Age 35 | Science  | ₹40000
ID: 5 | Staff    | Ravi       | Age 38 | Accounts | ₹15000
```

---

## Submission Checklist

- [ ] `Person` base class with private `__age` and property setter
- [ ] All 3 child classes override `get_role()` and `get_details()`
- [ ] Single loop saves all 5 objects — no separate save calls per type
- [ ] `promote()`, `give_raise()`, `transfer()` all run `UPDATE` queries
- [ ] `show_all()` reads from DB — not from objects in memory
- [ ] `age` setter rejects values below 5 and above 80
- [ ] `salary` setters reject invalid values
- [ ] Code runs without errors
- [ ] Pushed to GitHub with a proper README

---

## Folder Structure for GitHub

```
school-management-system/
├── school_management.py
├── school_management.db      ← generated on run
└── README.md
```

---

## README Template

```
# School Management System

A CLI-based School Management System built with Python OOP and SQLite3.

## Topics Covered
- Classes and Objects
- Class Methods and Self
- Inheritance
- Encapsulation
- Polymorphism

## How to Run
python school_management.py

## Tech Stack
- Python 3.12
- SQLite3 (built-in)
```
