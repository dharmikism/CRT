"""
PYTHON LISTS - COMPREHENSIVE GUIDE WITH EXAMPLES
==================================================

A list is a mutable (changeable), ordered collection that allows duplicate elements.
Lists are one of the most commonly used data structures in Python.
"""

# ============================================================================
# 1. CREATING LISTS
# ============================================================================

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with elements
fruits = ["Apple", "Banana", "Orange", "Mango"]
print(f"Fruits list: {fruits}")

# List with mixed data types
mixed_list = [10, "Hello", 3.14, True, None, [1, 2, 3]]
print(f"Mixed list: {mixed_list}")

# Using list() constructor
numbers = list(range(1, 6))
print(f"Numbers list: {numbers}")


# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================

fruits = ["Apple", "Banana", "Orange", "Mango"]

# Positive indexing (0-based)
print(f"\nFirst fruit (index 0): {fruits[0]}")
print(f"Second fruit (index 1): {fruits[1]}")

# Negative indexing (-1 is last element)
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second last fruit (index -2): {fruits[-2]}")

# Slicing: list[start:end:step]
print(f"First 2 fruits: {fruits[0:2]}")
print(f"From index 1 to end: {fruits[1:]}")
print(f"Every 2nd element: {fruits[::2]}")
print(f"Reversed list: {fruits[::-1]}")


# ============================================================================
# 3. MODIFYING LISTS
# ============================================================================

numbers = [1, 2, 3, 4, 5]

# Change single element
numbers[0] = 10
print(f"\nAfter changing first element: {numbers}")

# Change multiple elements (slicing)
numbers[1:3] = [20, 30]
print(f"After changing elements at index 1-2: {numbers}")

# Extend by adding elements
numbers.append(6)
print(f"After append(6): {numbers}")

# Add multiple elements
numbers.extend([7, 8, 9])
print(f"After extend([7, 8, 9]): {numbers}")

# Insert element at specific index
numbers.insert(2, 25)
print(f"After insert(2, 25): {numbers}")

# Remove specific element
numbers.remove(25)
print(f"After remove(25): {numbers}")

# Remove element by index (pop)
last_element = numbers.pop()
print(f"After pop(): {numbers}, popped: {last_element}")

# Remove by index
removed = numbers.pop(0)
print(f"After pop(0): {numbers}, removed: {removed}")

# Clear list
temp_list = [1, 2, 3]
temp_list.clear()
print(f"After clear(): {temp_list}")


# ============================================================================
# 4. LIST METHODS
# ============================================================================

# count() - count occurrences
items = [1, 2, 2, 3, 2, 4, 5]
print(f"\nCount of 2 in {items}: {items.count(2)}")

# index() - find first occurrence
index = items.index(2)
print(f"Index of first 2: {index}")

# sort() - sort in-place
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(f"After sort(): {numbers}")

# sort reverse
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() - returns new sorted list (original unchanged)
original = [5, 2, 8, 1, 9]
sorted_list = sorted(original)
print(f"Original: {original}, sorted: {sorted_list}")

# reverse() - reverse in-place
colors = ["Red", "Green", "Blue"]
colors.reverse()
print(f"After reverse(): {colors}")

# copy() - create a copy
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print(f"Original: {original}, Copy: {copy_list}")


# ============================================================================
# 5. LIST OPERATIONS
# ============================================================================

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"\nCombined {list1} + {list2} = {combined}")

# Repetition
repeated = [0] * 5
print(f"[0] * 5 = {repeated}")

# Membership (in/not in)
fruits = ["Apple", "Banana", "Orange"]
print(f"'Apple' in fruits: {'Apple' in fruits}")
print(f"'Mango' in fruits: {'Mango' in fruits}")

# Length
print(f"Length of {fruits}: {len(fruits)}")

# Min/Max
numbers = [5, 2, 8, 1, 9, 3]
print(f"Min of {numbers}: {min(numbers)}")
print(f"Max of {numbers}: {max(numbers)}")
print(f"Sum of {numbers}: {sum(numbers)}")


# ============================================================================
# 6. LIST COMPREHENSION
# ============================================================================

# Create list using comprehension
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares 1-5: {squares}")

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {evens}")

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3 multiplication table:\n{matrix}")

# Transformation
words = ["Hello", "World", "Python"]
lengths = [len(word) for word in words]
print(f"Words: {words}, Lengths: {lengths}")


# ============================================================================
# 7. ITERATING THROUGH LISTS
# ============================================================================

# Simple for loop
print("\nSimple loop:")
for fruit in ["Apple", "Banana", "Orange"]:
    print(f"  - {fruit}")

# With index (enumerate)
print("\nWith index:")
for index, fruit in enumerate(["Apple", "Banana", "Orange"]):
    print(f"  Index {index}: {fruit}")

# While loop
print("\nWhile loop:")
numbers = [1, 2, 3]
i = 0
while i < len(numbers):
    print(f"  {numbers[i]}")
    i += 1


# ============================================================================
# 8. NESTED LISTS
# ============================================================================

# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\nMatrix:\n{matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")

# Accessing all rows
for row in matrix:
    print(f"Row: {row}")


# ============================================================================
# 9. COMMON PATTERNS
# ============================================================================

# Filter elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [x for x in numbers if x > 5]
print(f"\nNumbers > 5 from {numbers}: {filtered}")

# Map/Transform
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")

# Find maximum/minimum with condition
numbers = [5, 2, 8, 1, 9, 3]
max_value = max(numbers)
min_value = min(numbers)
print(f"Max: {max_value}, Min: {min_value}")

# All vs Any
values = [True, True, True]
print(f"all([True, True, True]): {all(values)}")
print(f"any([False, False, True]): {any([False, False, True])}")

# Check if all elements satisfy condition
numbers = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in numbers)
print(f"All even in {numbers}: {all_even}")


# ============================================================================
# 10. PRACTICE EXAMPLES
# ============================================================================

# Example 1: Remove duplicates
items = [1, 2, 2, 3, 3, 3, 4]
unique_items = list(set(items))
print(f"\nOriginal: {items}")
print(f"Unique items: {unique_items}")

# Example 2: Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flat}")

# Example 3: Group elements
numbers = [1, 2, 3, 4, 5, 6]
pairs = [numbers[i:i+2] for i in range(0, len(numbers), 2)]
print(f"Original: {numbers}")
print(f"Pairs: {pairs}")

# Example 4: Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = [x for x in list1 if x in list2]
print(f"List1: {list1}, List2: {list2}")
print(f"Common elements: {common}")

# Example 5: Sort by specific criteria
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(f"\nStudents sorted by score (highest to lowest):")
for student in sorted_students:
    print(f"  {student['name']}: {student['score']}")

print("\n" + "="*70)
print("END OF LISTS GUIDE")
print("="*70)
