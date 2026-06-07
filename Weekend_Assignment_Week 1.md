# Weekend Assignment — Week 1
**Topic:** Sorting & Reversing  
**Push to:** GitHub (if already set up) or save locally  

---

## Ground Rules Before You Start

- No `sorted(key=...)` — figure out the sorting logic yourself
- No `Counter` from collections — build frequency manually
- Write your own comparison logic using functions
- Every question must handle edge cases — empty lists, single elements, ties
- Do not Google the solution directly. Search concepts only if stuck — not answers
- Use function while implementing logic

---

## Practice Questions

---

### Q1 — The Stubborn Leaderboard
**Difficulty:** Intermediate  
**Time estimate to code :** 45–60 minutes

---

#### What is being tested ?
You already know `.sort()` function, it sorts a list in ascending or descending order. But what happens when you need to sort by 
**multiple criteria at the same time** — and some go ascending while others go descending?

This question forces you to think about **how sorting decisions are actually made** when simple `.sort(reverse=True)` is not enough.

---

#### The Problem

You are given a list of student records. Each record is a list with three values :
```python
[name, score, age]
```

Sort the list by these rules **in this exact priority order:**

1. **Score — descending** (highest score comes first)
2. **If two students have the same score** → sort by age **ascending** (younger student comes first)
3. **If score AND age are both the same** → sort alphabetically by name **ascending** (A before Z)

---

#### Starting Data
```python
students = [
    ["Riya",  88, 17],
    ["Arjun", 92, 16],
    ["Meera", 88, 16],
    ["Kabir", 92, 16],
    ["Zara",  75, 17],
    ["Meera", 88, 17],
]
```

---

#### Expected Output : 
```python
['Arjun', 92, 16]
['Kabir', 92, 16]
['Meera', 88, 16]
['Riya',  88, 17]
['Meera', 88, 17]
['Zara',  75, 17]
```

---

#### Detailed Explanation — What Is Actually Happening

Look at the output carefully:

- Arjun and Kabir both scored 92. They have the same age (16). So they are sorted alphabetically → Arjun comes before Kabir.
- Meera (16), Riya (17), Meera (17) all scored 88. Among them, age decides first → Meera (16) comes first. Then Riya (17) and Meera (17) have the same age, so alphabetically Meera comes before Riya. Wait — check again: Riya and Meera (17) both scored 88 and both are age 17. Alphabetically M comes before R → Meera (17) before Riya (17).

This is exactly what a proper multi-criteria sort must handle. Your code must get all of this right automatically — not by hardcoding.

---

#### The Core Challenge

`.sort()` by default sorts by one value. To sort by multiple criteria, you need to write a **comparison function** — a function that takes two records and decides which one should come first.

A comparison function returns:
- A **negative number** if the first record should come before the second
- A **positive number** if the second record should come before the first  
- **Zero** if they are equal (and the next rule applies)

Python has a tool called `functools.cmp_to_key` that converts your comparison function into something `.sort()` can use. Look this up. Understand what it does. Then write the comparison function yourself.

---

#### Hints —

**Hint 1:** Your comparison function receives two records — call them `a` and `b`. First compare their scores. Since you want descending, think about what to return if `a`'s score is higher than `b`'s score.

**Hint 2:** Scores are equal — now compare ages. Ages go ascending, so think about what to return if `a`'s age is lower than `b`'s age.

**Hint 3:** Scores and ages are both equal — now compare names. Strings can be compared directly in Python using `<` and `>`. Alphabetical order works naturally.

**Hint 4:** Every `if` block in your comparison function must return something. If you miss a return path, Python returns `None` and your sort will behave strangely.

**Hint 5:** Look up `functools.cmp_to_key`. Read what it does. You do not need to understand its internals — just understand how to use it with `.sort()`.

---

#### Bonus Challenge
After sorting works correctly, print the leaderboard in a formatted table like this:
```
Rank  Name    Score  Age
1     Arjun   92     16
2     Kabir   92     16
...
```

---

---

### Q2 — Sort Without Sort
**Difficulty:** Intermediate  
**Time estimate:** 45 minutes

---

#### What is being tested
Every time you call `.sort()`, Python runs an algorithm internally. You have been using the result without understanding the process. This question makes you build the process yourself — specifically **Selection Sort**.

This matters because:
- DSA interviews ask you to implement sorting algorithms from scratch
- Understanding how sorting works internally makes you a better developer
- You will understand WHY `.sort()` is so much faster than naive approaches

---

#### The Problem

Implement a function called `selection_sort(lst)` that sorts a list **in-place** in ascending order.

**In-place** means: modify the original list directly. Return nothing — exactly like `.sort()` behaves.

Then test it against all four cases:

```python
test_1 = [64, 25, 12, 22, 11]
test_2 = []
test_3 = [5]
test_4 = [3, 3, 3, 1, 1]
```

Expected outputs:
```python
[11, 12, 22, 25, 64]
[]
[5]
[1, 1, 3, 3, 3]
```

---

#### Detailed Explanation — How Selection Sort Works

Imagine you have a row of numbered cards face down. You want to arrange them from smallest to largest.

**Round 1:** You flip every card and find the smallest one. You swap it into position 0.  
**Round 2:** You ignore position 0 (already done). You flip every remaining card and find the smallest. You swap it into position 1.  
**Round 3:** Ignore positions 0 and 1. Find the smallest in the rest. Swap into position 2.

Repeat until the list is sorted.

**Visual example with** `[64, 25, 12, 22, 11]`:

```python
Start:      [64, 25, 12, 22, 11]

Round 1:    Minimum in [64,25,12,22,11] = 11 at index 4
            Swap index 0 and index 4
            → [11, 25, 12, 22, 64]

Round 2:    Minimum in [25,12,22,64] = 12 at index 2
            Swap index 1 and index 2
            → [11, 12, 25, 22, 64]

Round 3:    Minimum in [25,22,64] = 22 at index 3
            Swap index 2 and index 3
            → [11, 12, 22, 25, 64]

Round 4:    Minimum in [25,64] = 25 at index 3
            Already in place — no swap needed
            → [11, 12, 22, 25, 64]

Done.
```

---

#### The Core Challenge

You need **two nested loops:**
- The outer loop tracks which position you are currently filling (starting from 0)
- The inner loop scans everything after the current position to find the minimum

You also need to track **where** the minimum is (its index), not just what it is — because you need to swap using the index.

---

#### Hints — 

**Hint 1:** Your outer loop runs from index 0 to `len(lst) - 1`. Think about why it does not need to go all the way to the last element.

**Hint 2:** At the start of each outer loop iteration, assume the current position holds the minimum. Store that position as `min_index`. Then use your inner loop to check if anything after it is actually smaller.

**Hint 3:** Your inner loop starts from `outer_index + 1` and goes to the end of the list. If you find something smaller than `lst[min_index]`, update `min_index`.

**Hint 4:** After the inner loop finishes, swap `lst[outer_index]` with `lst[min_index]`. Python allows you to swap two values in one line without a temporary variable — figure out how.

**Hint 5:** Test with `test_2 = []` and `test_3 = [5]` first. If your code crashes on these, your loop boundaries have a bug.

**Hint 6:** The function returns nothing. After calling `selection_sort(test_1)`, print `test_1` — the original list should be modified.

---

#### Bonus Challenge
Count the number of swaps made while sorting `test_1`. Print the count alongside the sorted result.

Then think: for a list of length N, what is the maximum number of swaps selection sort can make? Can you figure out the formula?

---

---

### Q3 — The Frequency Sort
**Difficulty:** Advanced  
**Time estimate:** 60–90 minutes

---

#### What is being tested
This question has no single obvious path to the solution. You need to:
1. Build a frequency count from scratch using a dict
2. Figure out how to sort based on that frequency — which is not in the original list
3. Handle a tie-breaking rule that runs in the opposite direction to the main sort

This tests whether you can **combine multiple concepts** into one solution — dict manipulation, sorting logic, and tie-breaking.

---

#### The Problem

Given a list of integers, sort them by **how often they appear** — the most frequent element comes first.

**Tie-breaking rule:** If two elements appear the same number of times, the **smaller number** comes first.

```python
nums = [4, 6, 2, 6, 4, 4, 3, 2, 6, 1]
```

Expected output:
```python
[4, 4, 4, 6, 6, 6, 2, 2, 3, 1]
```

---

#### Detailed Explanation — Breaking Down the Expected Output

First, count how often each number appears in `nums`:

| Number | Count |
|--------|-------|
| 4      | 3     |
| 6      | 3     |
| 2      | 2     |
| 3      | 1     |
| 1      | 1     |

Now sort by count descending:
- Count 3: numbers 4 and 6 — tie. Smaller number first → 4 before 6
- Count 2: number 2
- Count 1: numbers 3 and 1 — tie. Smaller number first → 1 before 3

So the sorted order of unique numbers is: **4, 6, 2, 1, 3**

Now rebuild the final list by repeating each number by its count:
```
4 appears 3 times → 4, 4, 4
6 appears 3 times → 6, 6, 6
2 appears 2 times → 2, 2
1 appears 1 time  → 1
3 appears 1 time  → 3
```

Final: `[4, 4, 4, 6, 6, 6, 2, 2, 1, 3]`

---

#### The Core Challenge

You are **not** sorting the original list directly. That approach will not work here.

The real approach has three stages:
1. Build a frequency dict — count how many times each number appears
2. Get a list of unique numbers and sort that list using the frequency rules
3. Rebuild the final list by repeating each unique number by its count

Stage 2 is the hard part. You need to sort unique numbers by their frequency (which lives in a dict, not the list), with a tie-breaker. Without lambda and without `sorted(key=...)`, you need to write a comparison function — same technique as Q1.

---

#### Hints — No Code Given

**Hint 1:** Build the frequency dict yourself using a loop. For each number in `nums`, check if it already exists as a key in your dict. If yes, increment its count. If no, set it to 1.

**Hint 2:** Get the unique numbers by extracting the keys from your frequency dict into a list.

**Hint 3:** Now you need to sort that list of unique numbers. Write a comparison function that receives two numbers `a` and `b`. Look up their frequencies in your dict. The one with **higher frequency** should come first. If frequencies are equal, the **smaller number** should come first.

**Hint 4:** In your comparison function — be very careful about which direction means "comes first." When you want descending frequency, think about what sign to return when `freq[a] > freq[b]`.

**Hint 5:** Once you have your sorted unique numbers, build the final result list. Loop through the sorted unique numbers. For each one, add it to the result list exactly `freq[number]` times. You can use list multiplication for this — think about how `[x] * n` works.

**Hint 6:** Use `functools.cmp_to_key` again here, same as Q1.

---

#### Test Your Solution Against These Cases Too

```python
# All same frequency
nums_2 = [3, 1, 2]
# Expected: [1, 2, 3]  — all appear once, so alphabetical (smallest first)

# One dominant element
nums_3 = [5, 5, 5, 1, 2, 3]
# Expected: [5, 5, 5, 1, 2, 3]  — 5 appears 3 times, rest appear once

# All duplicates
nums_4 = [2, 2, 1, 1]
# Expected: [1, 1, 2, 2]  — both appear twice, smaller (1) comes first
```

---

---

## Mini-Project — The Cricket Scorecard Sorter
**Difficulty:** Intermediate (with one genuinely tricky part)  
**Time estimate:** 2–3 hours across Saturday and Sunday  
**Push to GitHub**

---

### The Real Skill Being Built Here

You are not just sorting data. You are building a program that produces **multiple different views of the same dataset** — without modifying the original data.

This is exactly what real software does. A leaderboard, a product catalog, a stock screener — they all hold one dataset and display it sorted in different ways depending on what the user wants.

The additional twist: one of the four views requires sorting by a **value that does not exist in the list** — you have to calculate it on the fly. This is the thinking part.

---

### Background

You are given the batting scorecard of a T20 cricket match. Each player record contains:

```Richard Pybus
[player_name, runs, balls_faced, fours, sixes]
```

---

### Starting Data

```python
scorecard = [
    ["Rohit",   72, 45, 6, 3],
    ["Virat",   55, 42, 4, 2],
    ["Rahul",   30, 28, 2, 1],
    ["Hardik",  48, 22, 3, 4],
    ["Jadeja",  20, 18, 1, 1],
    ["Dhoni",   36, 15, 2, 3],
    ["Shami",    8, 10, 0, 0],
    ["Bumrah",   4,  6, 0, 0],
]
```

---

### What to Build — Four Sorted Views

Your program must display the scorecard in **4 different sorted views**, one after another.

---

#### View 1 — Top Scorers
Sort by **runs descending** — highest scorer first.

**Tie-breaker:** If two players have the same runs, the one who faced fewer balls comes first (they scored the same runs more efficiently — they are the better batter in that situation).

**Output format:**
```python
--- Top Scorers ---
1. Rohit   | Runs: 72 | Balls: 45
2. Virat   | Runs: 55 | Balls: 42
3. Hardik  | Runs: 48 | Balls: 22
...
```

---

#### View 2 — Strike Rate Kings
**Strike rate** = `(runs / balls_faced) * 100`

Sort by **strike rate descending** — highest strike rate first. Round to 2 decimal places for display.

**This is the tricky view.** Strike rate is not stored in the list. You must calculate it during sorting. Without lambda and without `sorted(key=...)`, you need to figure out how to sort by a value you compute rather than a value you read.

**Think about this:** your comparison function receives two records. You can calculate strike rate inside the comparison function for each record and use that to decide which comes first.

**Output format:**
```python
--- Strike Rate Kings ---
1. Hardik  | SR: 218.18 | Runs: 48
2. Dhoni   | SR: 240.00 | Runs: 36
...
```

Wait — recalculate. Check who actually has the highest strike rate in the dataset before assuming. Do the maths yourself first.

---

#### View 3 — Boundary Hitters
**Total boundaries** = `fours + sixes`

Sort by **total boundaries descending**. Tie-breaker: more sixes ranks higher (a six is harder to hit than a four).

**Output format:**
```python
--- Boundary Hitters ---
1. Rohit   | Boundaries: 9  (6 fours, 3 sixes)
2. Hardik  | Boundaries: 7  (3 fours, 4 sixes)
...
```

---

#### View 4 — Alphabetical
Sort player names **A to Z**.

No tie-breaking needed — names are unique.

**Output format:**
```python
--- Alphabetical ---
1. Bumrah
2. Dhoni
3. Hardik
...
```

---

### Rules — Read Carefully

**Rule 1 — Never modify the original list.**  
Every view must sort a **copy** of the scorecard. After all 4 views are printed, the original `scorecard` list must still be in its original order. If you modify the original, your program is wrong even if the output looks right.

To verify this, print the original scorecard at the very end of your program and confirm it matches the starting data.

**Rule 2 — No lambda. No `sorted(key=...)`. No Counter.**  
All sorting must use comparison functions with `functools.cmp_to_key`.

**Rule 3 — Strike rate must be computed, not stored.**  
Do not add a fifth element to each player record. Calculate strike rate only when needed — inside the comparison function or inside the display function.

**Rule 4 — Use a function for each view.**  
Your program must have at least these four functions:
- `show_top_scorers(data)`
- `show_strike_rate(data)`
- `show_boundary_hitters(data)`
- `show_alphabetical(data)`

Each function receives the scorecard, makes a copy, sorts the copy, and prints the result.

**Rule 5 — The main block only calls functions.**  
```python
if __name__ == "__main__":
    show_top_scorers(scorecard)
    show_strike_rate(scorecard)
    show_boundary_hitters(scorecard)
    show_alphabetical(scorecard)
    # Print original to verify it was never modified
```

---

### The Thinking Part — View 2 in Detail

This is the part most students get stuck on. Here is how to think through it:

You want to sort records by strike rate. Strike rate = (runs / balls) * 100.

Runs is at index 1. Balls is at index 2.

Your comparison function receives two full player records — let's call them `a` and `b`. Each is a list like `["Rohit", 72, 45, 6, 3]`.

Inside the comparison function, you can compute:
```python
strike_rate_a = a[1] / a[2] * 100
strike_rate_b = b[1] / b[2] * 100
```

Now compare them. You want descending, so if `strike_rate_a > strike_rate_b`, player A should come first.

That is it. The calculation happens inside the comparison function. The list never needs to store the strike rate.

**This is a fundamental idea in programming:** you do not always need to store computed values. You can compute them when needed and discard them.

---

### Suggested Approach — Do Not Skip This

**Appraoch 1:**
1. Write the starting data and the four empty functions
2. Get View 1 (Top Scorers) working completely — including the tie-breaker
3. Get View 4 (Alphabetical) working — it is the simplest
4. Verify the original list is untouched after both views run

**Appraoch 2:**
1. Tackle View 3 (Boundary Hitters) — you have a two-level tie-breaker here
2. Tackle View 2 (Strike Rate) last — it is the hardest conceptually
3. Polish the output formatting
4. Push to GitHub

Do not try to write all four functions at once. One at a time, tested properly.

---

### How to Copy a List for Sorting

You know from Section 11 (Copying Lists) that `b = a` is not a copy. It is two variables pointing to the same list.

To make a proper copy that you can sort without touching the original:

```python
copy = original[:]
# or
copy = original.copy()
```

Both work. Use whichever makes more sense to you.

---

### How Your GitHub Repo Should Look

```python
cricket-scorecard-sorter/
├── scorecard.py       ← your main file
└── README.md          ← what the project does, how to run it
```

README must include:
- What the project does (2–3 lines)
- How to run it (`python scorecard.py`)
- What each view shows

---

### Final Check Before Submitting

Run through this checklist yourself:

- [ ] All 4 views print in the correct sorted order
- [ ] View 2 (Strike Rate) shows correct values rounded to 2 decimal places
- [ ] The original `scorecard` list prints unchanged at the end
- [ ] No lambda anywhere in the file
- [ ] No `sorted(key=...)` anywhere in the file
- [ ] Four separate functions — one per view
- [ ] Pushed to GitHub with a README

---

*End of Weekend Assignment — Week 1*  
*Bring your working code to Monday's session. Bring your broken code too — both are useful.*