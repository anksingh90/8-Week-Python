# LeetCode Problems — Simple English Explanations

**For:** CBSE Class 12 → BTech Students  
**Purpose:** Understanding Interview problems in plain language before coding  
**Level:** Beginner to Intermediate DSA  

---

## Table of Contents

1. [Two Sum](#two-sum)
2. [Three Sum](#three-sum)
3. [Palindrome Number](#palindrome-number)

---

# 1. Two Sum

<details>  
**Difficulty:** Easy  
**Topics:** Hash Map, Arrays, List  

## What The Problem Is Asking

Imagine you have a list of numbers and a target sum. Your job is to find **exactly two different numbers** in that list that add up to the target. Then, return the **positions (indices)** of those two numbers.

**Key Rules:**
- You must find exactly 2 numbers
- They must be at different positions (cannot use the same number twice)
- There is always exactly one correct answer
- You can return the positions in any order

---

## Step-by-Step Breakdown

### Input (What you get)
- A list of numbers: `nums`
- A target sum: `target`

### Output (What you return)
- A list of 2 positions: `[position1, position2]`
- These positions point to the two numbers that add up to target

### Example Walkthrough

**Example 1:**
```
nums = [2, 7, 11, 15]
target = 9

Position:  0   1    2    3
Value:     2   7   11   15

Which two numbers add to 9?
- 2 + 7 = 9 ✓

Positions of 2 and 7? Position 0 and Position 1

Answer: [0, 1]
```

**Example 2:**
```
nums = [3, 2, 4]
target = 6

Position:  0  1  2
Value:     3  2  4

Which two numbers add to 6?
- 2 + 4 = 6 ✓

Positions of 2 and 4? Position 1 and Position 2

Answer: [1, 2]
```

**Example 3:**
```
nums = [3, 3]
target = 6

Position:  0  1
Value:     3  3

Which two numbers add to 6?
- 3 + 3 = 6 ✓ (position 0 and position 1 are different positions, so this is allowed)

Answer: [0, 1]
```

---

## Mental Model

Think of it like this:

**Scenario:** You're at a grocery store with a wallet. You have a list of items with prices and a total budget. You want to pick exactly 2 items whose prices add up to your budget.

```
Items:  Apple  Banana  Orange  Mango
Prices:  2      7       11      15
Budget: 9

Which 2 items cost exactly 9 total?
Apple (2) + Banana (7) = 9 ✓

Where are they in the shelf? Shelf positions 0 and 1.
```

---

## What NOT To Do

❌ Don't use the same position twice
```
nums = [5, 2, 3]
target = 10

WRONG: nums[0] + nums[0] = 5 + 5 = 10 (can't use position 0 twice!)
```

❌ Don't return the values themselves
```
nums = [2, 7, 11, 15]
target = 9

WRONG: [2, 7] ← These are VALUES
RIGHT: [0, 1] ← These are POSITIONS/INDICES
```

---

## Approach Hints (Without Spoiling)

**Naive Approach (Slow but works):**
- For each number, check every other number to see if they add to target
- Time: O(n²)

**Better Approach (Using a Helper Storage):**
- As you go through the list, remember the numbers you've already seen
- For each new number, ask: "Is the complement (target - current number) something I've already seen?"
- If yes → found the answer!
- Time: O(n)

---

## Edge Cases To Consider

1. **Negative numbers:** `nums = [-3, 5, 2], target = -1` → Answer: `[0, 1]` (because -3 + 2 = -1)
2. **Two identical numbers:** `nums = [3, 3], target = 6` → Answer: `[0, 1]` (different positions allowed)
3. **Large numbers:** `nums = [1000000, 2000000, 3000000], target = 3000000` → Answer: `[0, 1]`

---

## Template To Start Coding

```python
def twoSum(nums, target):
    """
    Args:
        nums: List of integers
        target: Target sum as integer
    
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    # Your code here
    pass

# Test with examples
print(twoSum([2, 7, 11, 15], 9))      # Expected: [0, 1]
print(twoSum([3, 2, 4], 6))           # Expected: [1, 2]
print(twoSum([3, 3], 6))              # Expected: [0, 1]
```

---

## Common Student Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Returning values `[2, 7]` instead of positions `[0, 1]` | Problem asks for positions, not values | Track positions, not values |
| Using same position twice | Rules say "may not use same element twice" | Check `i != j` |
| Returning `[1, 0]` when answer is `[0, 1]` | Problem says "any order" — both are correct! | Either order is fine |
| Only checking adjacent elements | Pair could be anywhere in the list | Check all combinations |

---

</details>

---

# 2. Three Sum

**LeetCode ID:** 15  
**Difficulty:** Medium  
**Topics:** Hash Map, Arrays, Sorting, Two Pointers  

## What The Problem Is Asking

You have a list of numbers. Your job is to find **all unique groups of exactly 3 numbers** that add up to **zero (0)**.

**Key Rules:**
- Find groups of 3 different numbers (at 3 different positions)
- The sum of these 3 numbers must equal 0
- No duplicate groups in your answer
- Order doesn't matter (`[-1, 0, 1]` is the same as `[0, 1, -1]`)

---

## Step-by-Step Breakdown

### Input (What you get)
- A list of integers: `nums` (can be positive, negative, or zero)

### Output (What you return)
- A list of lists, where each inner list is a triplet (3 numbers) that sum to 0
- No duplicate triplets allowed

### Example Walkthrough

**Example 1:**
```
nums = [-1, 0, 1, 2, -1, -4]

Let's find all triplets that sum to 0:

Triplet 1: -1 + 0 + 1 = 0 ✓
Triplet 2: -1 + (-1) + 2 = 0 ✓
Triplet 3: 0 + 1 + (-1) = 0 ✓  (but this is same as Triplet 1, just reordered)

Unique triplets: [[-1, -1, 2], [-1, 0, 1]]

(Note: [-1, -1, 2] and [-1, 0, 1] are the only unique combinations)
```

**Example 2:**
```
nums = [0, 1, 1]

Can we find any 3 numbers that sum to 0?
- 0 + 1 + 1 = 2 ✗ (not zero)

No valid triplets exist.

Answer: []
```

**Example 3:**
```
nums = [0, 0, 0]

Can we find triplets that sum to 0?
- 0 + 0 + 0 = 0 ✓

Only one unique triplet: [[0, 0, 0]]

Answer: [[0, 0, 0]]
```

---

## Mental Model

**Scenario:** You're organizing a team game where groups must have exactly 3 members with **zero net skill difference** (perfect balance).

```
Players and their skill levels:
Player A: -1
Player B:  0
Player C:  1
Player D:  2
Player E: -1
Player F: -4

Which groups of 3 have zero net skill?

Group 1: A (-1) + B (0) + C (1) = 0 ✓ (balanced!)
Group 2: A (-1) + D (2) + E (-1) = 0 ✓ (balanced!)
Group 3: E (-1) + B (0) + C (1) = 0 ✓ (but same members as Group 1, just different order)

Unique groups: [[-1, 0, 1], [-1, 2, -1]]
```

---

## What NOT To Do

❌ **Don't include duplicate triplets:**
```
nums = [-1, 0, 1, -1, 0, 1]

WRONG: [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]  (repeated 3 times)
RIGHT: [[-1, 0, 1]]  (include only once)
```

❌ **Don't confuse order:**
```
nums = [-1, 0, 1, 2, -1, -4]

[-1, 0, 1] and [0, 1, -1] and [1, -1, 0] are ALL THE SAME TRIPLET
Include it only ONCE.
```

❌ **Don't use the same position twice:**
```
nums = [0, 0, 0]

WRONG: Position 0 + Position 0 + Position 0 (can't reuse same position)
RIGHT: Position 0 + Position 1 + Position 2 (different positions)
```

---

## Approach Hints (Without Spoiling)

### Naive Approach (Very Slow):
- Check every combination of 3 numbers
- Time: O(n³)

### Better Approach (Two Pointers):
1. **Sort the array first**
2. **Fix one number** (outer loop)
3. **Use two pointers** (left and right) to find the other 2 numbers
   - Move pointers based on whether sum is too small or too large
4. **Skip duplicates** at each step
5. Time: O(n²)

---

## Step-by-Step Algorithm (Simple Version)

```
Step 1: Sort the array
Step 2: For each number in the array (fix it as first number)
        Step 3: Use two pointers to find 2 more numbers
                - Left pointer starts after current number
                - Right pointer starts at the end
                - If sum == 0, add to answer and skip duplicates
                - If sum < 0, move left pointer right (increase sum)
                - If sum > 0, move right pointer left (decrease sum)
Step 4: Return all unique triplets
```

---

## Detailed Walkthrough with Example 1

```
Original: nums = [-1, 0, 1, 2, -1, -4]

Step 1: Sort
nums = [-4, -1, -1, 0, 1, 2]
        0   1   2   3  4  5  (positions)

Step 2-3: Fix first number and find other two

i = 0 (fixed number = -4)
  Left pointer at i+1 = position 1 (-1)
  Right pointer at end = position 5 (2)
  
  Sum = -4 + (-1) + 2 = -3 (negative, less than 0)
  Move left pointer right
  
  Sum = -4 + (-1) + 2 = -3... (no valid triplet starting with -4)

i = 1 (fixed number = -1)
  Left pointer at position 2 (-1)
  Right pointer at position 5 (2)
  
  Sum = -1 + (-1) + 2 = 0 ✓ Found! Add [-1, -1, 2]
  
  Skip duplicate -1s and continue...
  
  Left pointer at position 3 (0)
  Right pointer at position 5 (2)
  
  Sum = -1 + 0 + 2 = 1 (greater than 0)
  Move right pointer left
  
  ... continue process

i = 2 (fixed number = -1)
  Left pointer at position 3 (0)
  Right pointer at position 5 (2)
  
  Sum = -1 + 0 + 1 = 0 ✓ Found! Add [-1, 0, 1]
  
  ... continue

Final Answer: [[-1, -1, 2], [-1, 0, 1]]
```

---

## Why Sorting Helps

**Without sorting:** Hard to avoid duplicates, slow to find pairs
```
[-1, 0, 1, 2, -1, -4]  ← messy, duplicates scattered
```

**With sorting:** Easy to skip duplicates, easy to find pairs with two pointers
```
[-4, -1, -1, 0, 1, 2]  ← sorted, duplicates grouped together
```

Duplicate detection becomes simple: `if nums[i] == nums[i-1]: skip`

---

## Common Pitfalls

| Pitfall | Why It Breaks | Solution |
|---------|---------------|----------|
| Forgetting to sort | Two-pointer technique won't work | Always sort first |
| Including duplicate triplets | Answer will be wrong | Skip duplicate numbers |
| Using same index twice | Violates the rules | Use different pointers/indices |
| Not handling negatives | Will miss valid triplets | Treat negatives same as positives |
| Only checking adjacent pairs | Will miss valid triplets far apart | Use two pointers, not adjacent loop |

---

## Edge Cases To Test

```python
# Case 1: All zeros
nums = [0, 0, 0, 0]
Expected: [[0, 0, 0]]

# Case 2: No solution
nums = [1, 2, 3]
Expected: []

# Case 3: Mix of positive and negative
nums = [-2, -1, 0, 1, 2]
Expected: [[-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

# Case 4: With duplicates
nums = [-1, -1, -1, 0, 1, 1, 1]
Expected: [[-1, 0, 1]]

# Case 5: Single valid triplet
nums = [-4, -2, 0, 2, 4]
Expected: [[-4, 0, 4], [-4, 2, 2], [-2, 0, 2]]
```

---

## Template To Start Coding

```python
def threeSum(nums):
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: List of integers
    
    Returns:
        List of lists, where each inner list is a triplet summing to 0
    """
    # Your code here
    pass

# Test with examples
print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(threeSum([0, 1, 1]))              # []
print(threeSum([0, 0, 0]))              # [[0, 0, 0]]
```

---

## Key Differences from 2 Sum

| Aspect | 2 Sum | 3 Sum |
|--------|-------|-------|
| Numbers to find | 2 | 3 |
| Target | Given | Always 0 |
| Duplicates | Not mentioned | Must avoid |
| Complexity | O(n) with hash map | O(n²) with sorting + two pointers |
| Approach | Hash map | Sort + Two pointers |

---

---

# 3. Palindrome Number

**LeetCode ID:** 9  
**Difficulty:** Easy  
**Topics:** Math, Strings (optional)  

## What The Problem Is Asking

Given a number, determine if it **reads the same forwards and backwards**.

**Key Rules:**
- Negative numbers are **never palindromes** (the `-` sign changes when reversed)
- Numbers ending in 0 are **never palindromes** (except 0 itself)
- You must check if the number is identical when reversed

---

## Step-by-Step Breakdown

### Input (What you get)
- An integer: `x` (can be positive, negative, or zero)

### Output (What you return)
- `True` if the number is a palindrome
- `False` if it is not

### Example Walkthrough

**Example 1:**
```
x = 121

Read left to right:  121
Read right to left:  121

Are they the same? YES ✓

Answer: True
```

**Example 2:**
```
x = -121

Read left to right:  -121
Read right to left:  121- (the minus sign moves to the right, doesn't make sense)

Are they the same? NO ✗

Also, any negative number with a "-" sign cannot be a palindrome.

Answer: False
```

**Example 3:**
```
x = 10

Read left to right:  10
Read right to left:  01 (which is just 1)

Are they the same? NO ✗

Also, numbers ending in 0 cannot be palindromes (the reversed form would start with 0).

Answer: False
```

---

## Mental Model

**Scenario: Phone Numbers or House Numbers**

Imagine a house number or phone number that reads the same forwards and backwards.

```
House Number 121:
- Reading left to right: 121
- Reading right to left: 121
- Perfect! It's a palindrome.

House Number -121:
- Reading left to right: -121
- The negative sign breaks the symmetry.
- Not a palindrome.

House Number 10:
- Reading left to right: 10
- Reading right to left: 01 (which drops the leading 0 and becomes 1)
- 10 ≠ 1, not a palindrome.
```

---

## More Examples To Build Intuition

```
✓ Palindromes:
  0      → 0 (reads same)
  7      → 7 (single digit always palindrome)
  11     → 11
  101    → 101
  1221   → 1221
  12321  → 12321

✗ NOT Palindromes:
  -1     → negative sign breaks it
  10     → reverses to 01 which is 1
  123    → reverses to 321
  1234   → reverses to 4321
```

---

## What NOT To Do

❌ **Don't forget about negative numbers:**
```
x = -121

WRONG: Think of it as just reversing to 121, ignoring the "-"
RIGHT: Negative numbers are NEVER palindromes
```

❌ **Don't ignore trailing zeros:**
```
x = 10

WRONG: Think "1" backwards is "1", so it's a palindrome
RIGHT: 10 reversed is 01 which equals 1, and 10 ≠ 1
```

❌ **Don't convert to string if you want to optimize:**
```
Converting to string works, but it uses extra memory.
This problem is often asked to test if you can solve it mathematically.
```

---

## Approach Hints (Without Spoiling)

### Approach 1: Convert to String (Easy but uses memory)
```
1. Convert number to string
2. Check if string == reversed string
3. Return True/False
```

### Approach 2: Reverse Mathematically (Optimized)
```
1. Handle negative numbers (return False immediately)
2. Handle trailing zeros (if x ends in 0 and x != 0, return False)
3. Reverse the number digit by digit
4. Compare original with reversed
```

### Approach 3: Two-Pointer On Digits (No reversal)
```
1. Extract digits from front and back
2. Compare them
3. Move inward until you've checked all pairs
```

---

## Detailed Walkthrough — Approach 2 (Optimized)

Let's manually reverse a number to understand the logic:

**Example: x = 121**

```
Original: 121
Reversed: ?

Extract digits from right to left:
- Last digit of 121 = 1
- Middle digit = 2
- First digit = 1

Reversed = 121

Are they equal? YES → Return True
```

**How to extract digits programmatically:**

```
x = 121
reversed_x = 0

Step 1:
  last_digit = 121 % 10 = 1
  reversed_x = 0 * 10 + 1 = 1
  x = 121 // 10 = 12

Step 2:
  last_digit = 12 % 10 = 2
  reversed_x = 1 * 10 + 2 = 12
  x = 12 // 10 = 1

Step 3:
  last_digit = 1 % 10 = 1
  reversed_x = 12 * 10 + 1 = 121
  x = 1 // 10 = 0

x is now 0, stop.
reversed_x = 121

Compare: 121 == 121? YES → Return True
```

**Example: x = 1221**

```
Original: 1221
Reversed: ?

Step 1: last_digit = 1, reversed_x = 1, x = 122
Step 2: last_digit = 2, reversed_x = 12, x = 12
Step 3: last_digit = 2, reversed_x = 122, x = 1
Step 4: last_digit = 1, reversed_x = 1221, x = 0

reversed_x = 1221
Compare: 1221 == 1221? YES → Return True
```

**Example: x = -121**

```
Is x < 0? YES
Return False immediately (negatives are never palindromes)
```

**Example: x = 10**

```
Is x < 0? NO
Does x end in 0 (x % 10 == 0) AND x != 0? YES
Return False immediately (trailing zeros mean not palindrome, except 0 itself)
```

---

## Step-by-Step Algorithm

```
Step 1: If x is negative, return False
        (Negative sign prevents palindrome property)

Step 2: If x ends in 0 and x != 0, return False
        (Reversed form would have leading 0, not equal to original)

Step 3: Reverse the number:
        - Extract last digit: digit = x % 10
        - Add to reversed: reversed = reversed * 10 + digit
        - Remove last digit from x: x = x // 10
        - Repeat until x becomes 0

Step 4: Compare original x with reversed
        If equal, return True
        Else, return False
```

---

## Edge Cases To Test

```python
# Case 1: Single digit (always palindrome)
x = 7
Expected: True

# Case 2: Negative (always not palindrome)
x = -121
Expected: False

# Case 3: Ends in zero (never palindrome except 0)
x = 120
Expected: False

# Case 4: Zero itself (special case)
x = 0
Expected: True

# Case 5: Large palindrome
x = 12345654321
Expected: True

# Case 6: Large non-palindrome
x = 12345678987654321
Expected: False

# Case 7: Two-digit palindrome
x = 22
Expected: True

# Case 8: Two-digit non-palindrome
x = 23
Expected: False
```

---

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| String conversion | O(log x) | O(log x) | Simple, easy to understand | Uses extra memory |
| Reverse mathematically | O(log x) | O(1) | Optimized, no extra space | Requires digit manipulation logic |
| Two-pointer on digits | O(log x) | O(log x) | Interesting technique | More complex code |

---

## Why Negative Numbers Don't Work

```
If x = -121:

Reversing mathematically gives 121 (without the negative).
But the original is -121.
-121 ≠ 121, so not a palindrome.

Also, conceptually:
"-121" reversed would be "121-" which doesn't make sense as a number.
```

---

## Why Trailing Zeros Don't Work

```
If x = 120:

Reversed mathematically: 021 = 21 (leading zeros are ignored)
But 120 ≠ 21, so not a palindrome.

Also, numbers ending in 0 can only be 0 itself.
(Any multiple of 10 reversed has a leading 0, which is invalid)
```

---

## Template To Start Coding

```python
def isPalindrome(x):
    """
    Check if an integer is a palindrome.
    
    Args:
        x: Integer to check
    
    Returns:
        True if palindrome, False otherwise
    """
    # Your code here
    pass

# Test with examples
print(isPalindrome(121))     # True
print(isPalindrome(-121))    # False
print(isPalindrome(10))      # False
print(isPalindrome(0))       # True
print(isPalindrome(7))       # True
```

---

## Common Student Mistakes

| Mistake | Why It's Wrong | Solution |
|---------|----------------|----------|
| Treating -121 as palindrome | The "-" sign breaks symmetry | Check for negative first, return False |
| Allowing 120 as palindrome | Reversed is 21, not 120 | Check trailing zeros |
| String conversion for large numbers | Works but inefficient | Learn mathematical reversal |
| Comparing strings "-121" and "121-" | Doesn't make sense as number | Negatives are always False |
| Forgetting to handle x = 0 | 0 is a valid single-digit palindrome | Allow 0 explicitly |

---

## Quick Reference

```
Always False:
- Any negative number
- Any number ending in 0 (except 0 itself)

Always True:
- Single digit numbers (0-9)
- Numbers that read same forwards and backwards (121, 1221, 12321)
```

---

---

## How to Use This Document

1. **Read the problem** in the "What The Problem Is Asking" section
2. **Work through examples** to understand the pattern
3. **Study the approach hints** (don't read full solutions yet)
4. **Attempt to code** using the template
5. **Test with edge cases** before finalizing
6. **Review common mistakes** to avoid them

---

## Next Steps

- Complete coding for each problem
- Test all edge cases
- Push solutions to GitHub with clear commit messages
- Move to the next set of problems (arrays, strings, linked lists)

---

**Document Version:** 1.0  
**Created:** June 2026  
**For:** Advanced Python Course — DSA Phase  
**Last Updated:** 2026
