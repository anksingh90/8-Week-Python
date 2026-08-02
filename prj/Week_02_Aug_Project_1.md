# Project 1: Student Result Management System

**Time needed:** 2–3 weeks, 1–2 hours a day
**What you already know that this uses:** Classes, inheritance, dunder methods, ABC (from Week 3 & 4)
**What's new in this project:** Saving data with SQLite3, so your data doesn't disappear when you close the program

---

## 1. What Are We Building?

A program that manages student records and their marks — like a mini version of what your school uses to store report cards.

You should be able to:
- Add a new student
- Add subjects and marks for that student
- Calculate their total, percentage, and grade
- See a rank list of all students
- Look up any student's report card
- Close the program and reopen it later — all data is still there (this is where SQLite3 comes in)

---

## 2. Why This Project (Not Something Else)

- It uses **only what you've already learned** — no new syntax to panic about, except SQLite basics which are simple (just 5–6 commands)
- Every backend job — big or small — needs you to build something that stores and manages data like this. This is the core skill.
- It's a good GitHub piece because it shows you can design classes properly, not just write functions

---

## 3. The Real-World Analogy

Think of it like the school's exam office.

- Each **Student** is a file folder with their name and roll number on it
- Each **Subject** is a mark sheet inside that folder
- The **office register** (your SQLite database) is what keeps every folder safe even after the office closes for the day
- When you "calculate result," you're just adding up marks from all the sheets in that one folder

---

## 4. What You Need to Build — Step by Step

### Step 1: Design Your Classes (Week you already know)

You'll need at least these classes:

```
Student
  - name
  - roll_number
  - a way to store subjects and marks

Subject
  - subject_name
  - marks_obtained
  - max_marks

ResultCalculator (or a method inside Student)
  - calculates total, percentage, grade
```

**Use what you already learned:**
- `__init__` to set up each student and subject
- `__str__` or `__repr__` so printing a student looks clean, not like `<Student object at 0x7f...>`
- `__eq__` if you want to compare two students by roll number
- If you finish ABC this week — make an abstract `GradingStrategy` class, then a `StandardGrading` class that implements it. This lets you swap grading rules later without breaking anything.

### Step 2: Add SQLite3 (New — but simple)

You don't need to become a database expert. You need exactly 4 things:

1. **Connect to a database file** — this creates a `.db` file that holds your data
2. **Create a table** — a table to store students, another for subjects/marks
3. **Insert data** — save a student and their marks
4. **Read data** — fetch it back when needed

Here's the pattern you'll use for almost everything:

```python
import sqlite3

# Connect (creates the file if it doesn't exist)
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create a table (only needs to run once)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_number INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

# Insert a student
cursor.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (101, "Aditi"))
connection.commit()  # saves the change permanently

# Read all students
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)

connection.close()
```

That's genuinely most of what you need. You'll repeat this pattern for a `subjects` table too, linking each subject row to a student's roll number.

### Step 3: Connect Your Classes to the Database

This is the main new skill in this project — making your `Student` class **save itself** to the database and **load itself** back.

Simple approach:
- Add a `save_to_db()` method on your Student class
- Add a function (or class method) `load_student(roll_number)` that reads from the database and rebuilds a `Student` object

This is exactly what real backend applications do — objects in your code, rows in a database, and methods that move data between the two.

### Step 4: Build the Menu

A simple text menu the user sees when they run the program:

```
1. Add Student
2. Add Marks for a Student
3. View Report Card
4. View Rank List
5. Exit
```

Use a loop that keeps showing this menu until the user picks Exit.

---

## 5. Suggested Weekly Plan

**Week 1 (Days 1–5, ~1.5 hrs/day)**
- Design and write the `Student` and `Subject` classes fully — no database yet, just working in memory
- Add dunder methods (`__str__`, `__eq__`)
- Test that you can create students, add subjects, and calculate percentage correctly

**Week 2 (Days 1–5, ~1.5 hrs/day)**
- Learn the 4 SQLite basics above (connect, create table, insert, read) — practice on a throwaway test file first
- Create your `students` and `subjects` tables
- Write `save_to_db()` and `load_student()` 
- Connect this to your existing classes from Week 1

**Week 3 (Days 1–5, flexible, ~1–2 hrs/day)**
- Build the menu system that ties everything together
- Add the rank list feature (sort all students by percentage)
- Handle errors — what happens if someone enters a roll number that doesn't exist?
- Clean up, add comments, write the README, push to GitHub

---

## 6. What "Done" Looks Like (Checklist)

- [ ] Can add a new student and it's saved permanently (still there after closing the program)
- [ ] Can add multiple subjects with marks for one student
- [ ] Percentage and grade are calculated correctly
- [ ] Can view one student's full report card
- [ ] Can view a rank list of all students, sorted by percentage
- [ ] Program doesn't crash if you enter something wrong (like a roll number that doesn't exist)
- [ ] Code is on GitHub with a README explaining what it does and how to run it

---

## 7. Stretch Goals (Only If You Finish Early)

- Let a student have a "pass/fail" status based on a minimum marks rule per subject
- Export the rank list to a CSV file (you already know the `csv` module from Week 7)
- Add a search feature — find a student by name, not just roll number

---

## 8. Grading Strategy Idea (If You Want to Practice ABC This Week)

Since ABC is one of your pending topics, here's a natural way to use it in this exact project:

```python
from abc import ABC, abstractmethod

class GradingStrategy(ABC):
    @abstractmethod
    def get_grade(self, percentage):
        pass

class StandardGrading(GradingStrategy):
    def get_grade(self, percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        else:
            return "C"
```

Now your `Student` class can accept any `GradingStrategy` object and use it — this is a small taste of how real systems stay flexible.

---

## 9. Common Mistakes to Watch For

- Forgetting `connection.commit()` after INSERT — your data will disappear because it was never actually saved
- Opening a new connection every time instead of reusing one — works, but gets messy; keep it simple for this project
- Mixing up when you're working with a `Student` object (in Python) vs. a row (in the database) — keep the save/load functions clearly separated from your class logic

---

**Next step:** Once this is on GitHub, Week 9-A will teach you SQL joins and relationships properly — you'll be able to come back and make this project even better (like linking subjects across multiple years).
