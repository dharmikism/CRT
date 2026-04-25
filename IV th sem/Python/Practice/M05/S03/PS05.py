from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, curr):
            if index == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[index])
            backtrack(index + 1, curr)

            curr.pop()
            backtrack(index + 1, curr)

        backtrack(0, [])
        return res
    

'''
Example: nums = [1, 2, 3]
Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]'''

testcase = [1, 2, 3]    
solution = Solution()
print(solution.subsets(testcase))
'''

# Backtracking: Complete Guide

## Table of Contents
1. [What is Backtracking?](#what-is-backtracking)
2. [Key Concepts](#key-concepts)
3. [How It Works](#how-it-works)
4. [Backtracking Template](#backtracking-template)
5. [Common Problems](#common-problems)
6. [Examples with Explanations](#examples-with-explanations)
7. [Time & Space Complexity](#time--space-complexity)

---

## What is Backtracking?

**Backtracking** is a problem-solving algorithm that incrementally builds a solution and abandons it ("backtracks") as soon as it realizes the solution cannot be completed.

### Core Idea
- **Explore**: Make a choice and move forward
- **Check**: Verify if the choice leads to a valid solution
- **Backtrack**: Undo the choice if it doesn't lead to a solution
- **Repeat**: Try other choices

### When to Use Backtracking
- Finding all possible solutions (combinations, permutations, subsets)
- Constraint satisfaction problems
- Decision problems (N-Queens, Sudoku solver)
- Path-finding problems (maze solving)

---

## Key Concepts

### 1. **Decision Tree**
Backtracking explores a decision tree where:
- Each node represents a choice
- Each branch represents exploring that choice
- Leaves represent complete solutions

### 2. **Constraints**
- **Implicit constraints**: Properties that solutions must satisfy
- **Explicit constraints**: Conditions we define

### 3. **State Space**
The collection of all possible states (partial and complete solutions).

### 4. **Pruning**
Eliminating branches that cannot lead to a valid solution.

---

## How It Works

### Step-by-Step Process

```
1. START with an empty solution
2. Choose the next item to add to solution
3. Check if it's valid:
   - YES: Continue with remaining items
   - NO: Skip this item and try next
4. When you reach the end:
   - If valid: Record solution
5. BACKTRACK: Remove last item and try alternatives
6. Repeat until all possibilities explored
```

### Visual Example: Generating Subsets of [1, 2, 3]

```
                    []
                   /  \
                  /    \
                 /      \
              [1]        []
             /  \        /  \
           [1,2][1]    [2]   []
           / \   / \    / \   / \
       [1,2,3][1,2][1,3][1][2,3][2][3][]

Path to [1,2]: Include 1 → Include 2 → Don't include 3
Path to [1,3]: Include 1 → Don't include 2 → Include 3
```

---

## Backtracking Template

### Generic Pattern

```python
def backtrack(candidates, path, result):
    # BASE CASE: If we've processed all candidates or reached goal
    if is_solution(path):
        result.append(path[:])  # Add copy of path to result
        return
    
    # Try each next candidate
    for candidate in candidates:
        # Check if candidate is valid/valid at this position
        if is_valid(candidate, path):
            # CHOOSE: Add candidate to path
            path.append(candidate)
            
            # EXPLORE: Recursively solve with this choice
            backtrack(remaining_candidates, path, result)
            
            # UNCHOOSE: Remove candidate (backtrack)
            path.pop()

backtrack(initial_candidates, [], result)
```

### Key Elements
1. **Base Case**: When to stop recursion (found complete solution)
2. **Recursive Case**: Try each possibility
3. **Constraint Check**: Validate before exploring
4. **Backtrack**: Undo choice (`path.pop()`)
5. **Return**: Accumulate results

---

## Common Problems

### 1. **Subsets/Power Set**
- Generate all subsets of a list
- For each element: include it or don't
- Time: O(2^n)

### 2. **Permutations**
- Generate all orderings of elements
- All elements must be used
- Time: O(n!)

### 3. **Combinations**
- Generate k-sized combinations
- Order doesn't matter
- Time: O(C(n,k))

### 4. **N-Queens**
- Place N queens on N×N board
- No two queens can attack each other
- Time: O(N!)

### 5. **Sudoku Solver**
- Fill grid with numbers 1-9
- Each row/column/box has unique digits
- Time: O(9^(n²)) - highly pruned

### 6. **Word Search**
- Find if word exists in grid
- Can move up/down/left/right
- Time: O(N×M×4^L)

---

## Examples with Explanations

### Example 1: Subsets (PS05.py - Your Code)

```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all subsets of nums using backtracking.
        
        Example: nums = [1, 2, 3]
        Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
        """
        res = []
        
        def backtrack(index, curr):
            # BASE CASE: Processed all elements
            if index == len(nums):
                res.append(curr[:])  # Add a copy of current subset
                return
            
            # CHOICE 1: Include nums[index]
            curr.append(nums[index])
            backtrack(index + 1, curr)
            
            # CHOICE 2: Exclude nums[index] (BACKTRACK)
            curr.pop()
            backtrack(index + 1, curr)
        
        backtrack(0, [])
        return res
```

**How it works for [1, 2]:**
```
backtrack(0, [])
├─ Include 1: backtrack(1, [1])
│  ├─ Include 2: backtrack(2, [1,2])
│  │  └─ Base: Add [1,2] to result
│  └─ Exclude 2: backtrack(2, [1])
│     └─ Base: Add [1] to result
└─ Exclude 1: backtrack(1, [])
   ├─ Include 2: backtrack(2, [2])
   │  └─ Base: Add [2] to result
   └─ Exclude 2: backtrack(2, [])
      └─ Base: Add [] to result
```

**Result:** [[], [1], [1,2], [2]]

---

### Example 2: Permutations

```python
def permute(nums):
    """Generate all permutations of nums."""
    result = []
    
    def backtrack(curr, remaining):
        if not remaining:  # All numbers used
            result.append(curr[:])
            return
        
        for i in range(len(remaining)):
            # Choose
            curr.append(remaining[i])
            # Explore with remaining numbers (excluding current)
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(curr, new_remaining)
            # Unchoose
            curr.pop()
    
    backtrack([], nums)
    return result

# Example: permute([1, 2, 3])
# Returns: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

---

### Example 3: N-Queens Problem

```python
def solveNQueens(n):
    """
    Place n queens on n×n board so no two queens attack each other.
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check diagonal (top-right)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        if row == n:  # All queens placed
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return result
```

---

## Time & Space Complexity

### Time Complexity Patterns

| Problem | Time Complexity | Reason |
|---------|-----------------|--------|
| Subsets | O(2^n) | 2 choices per element |
| Permutations | O(n!) | n! possible orderings |
| Combinations | O(C(n,k)) | nCk combinations |
| N-Queens | O(N!) | Pruned exploration |
| Sudoku | O(9^(n²)) | Heavily pruned |

### Space Complexity

- **Recursion Stack**: O(n) to O(n!) depending on depth
- **Result Storage**: O(k) where k = number of solutions
- **Temporary Storage**: O(n) for current path

---

## Tips for Solving Backtracking Problems

### 1. **Identify the Problem Type**
   - Are we finding ALL solutions? → Backtracking
   - One solution? → DFS/BFS
   - Optimal solution? → DP

### 2. **Define the Decision Tree**
   - What are the choices at each step?
   - What are the constraints?

### 3. **Implement the Base Case**
   - When do we have a complete solution?
   - What to do when we reach it?

### 4. **Implement Constraints**
   - What makes a choice valid?
   - Use is_valid() function

### 5. **Implement the Recursive Case**
   - Try each valid choice
   - Recurse with updated state
   - Undo the choice (backtrack)

### 6. **Optimize with Pruning**
   - Skip branches that can't lead to solutions
   - Reduce search space significantly

---

## Common Mistakes

❌ **Forgetting to backtrack** → Get incorrect results
```python
# WRONG
path.append(candidate)
backtrack(...)
# Missing: path.pop()
```

❌ **Modifying original data** → Causes state issues
```python
# WRONG
backtrack(candidates[1:], ...)  # Creates new list each time
```

❌ **Not copying results** → All results point to same object
```python
# WRONG
result.append(path)  # Append reference
# CORRECT
result.append(path[:])  # Append copy
```

❌ **Wrong base case** → Infinite recursion or missing solutions
```python
# WRONG
if index > len(nums):  # Off by one error
```

---

## Practice Problems

1. **Subsets** - Generate all subsets ✓ (Your PS05.py)
2. **Permutations** - All orderings
3. **Combinations** - k-sized subsets
4. **Word Search** - Find word in grid
5. **Generate Parentheses** - Valid bracket combinations
6. **Palindrome Partitioning** - Partition into palindromes
7. **Rat in Maze** - Path finding
8. **Sudoku Solver** - Fill grid with constraints
9. **N-Queens** - Place queens safely
10. **Letter Case Permutation** - Toggle case combinations

---

## Conclusion

Backtracking is powerful for:
- **Exhaustive search**: Find ALL solutions
- **Constraint satisfaction**: Respect all rules
- **Optimization**: Prune impossible branches

Master the template, practice identifying problems, and backtracking becomes intuitive!

'''