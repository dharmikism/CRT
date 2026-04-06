"""
====================================================================
ARRAYS IN PYTHON - TUTORIAL WITH SYNTAX AND EXAMPLES
====================================================================
This file contains a complete tutorial on arrays with runnable examples.
"""

# ====================================================================
# 1. WHAT ARE ARRAYS?
# ====================================================================
# Arrays are collections of elements stored in a single variable
# In Python, the most basic array is a LIST

# ====================================================================
# 2. CREATING ARRAYS (LISTS)
# ====================================================================

print("\n" + "="*60)
print("CREATING ARRAYS/LISTS")
print("="*60)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with elements
fruits = ['apple', 'banana', 'orange']
print(f"Fruits list: {fruits}")

numbers = [1, 2, 3, 4, 5]
print(f"Numbers list: {numbers}")

# Mixed data types
mixed = [1, 'hello', 3.14, True, None]
print(f"Mixed list: {mixed}")

# Using list() constructor
new_list = list()
print(f"Using list() constructor: {new_list}")

# Creating list from range
range_list = list(range(1, 6))  # 1 to 5
print(f"List from range(1, 6): {range_list}")

range_list2 = list(range(0, 10, 2))  # 0 to 9, step 2
print(f"List from range(0, 10, 2): {range_list2}")

# List with repeated elements
repeated = [0] * 5
print(f"Repeated elements [0] * 5: {repeated}")

# ====================================================================
# 3. ACCESSING ELEMENTS (INDEXING)
# ====================================================================

print("\n" + "="*60)
print("ACCESSING ELEMENTS - INDEXING")
print("="*60)

fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
print(f"Fruits: {fruits}")

# Positive indexing (left to right, 0-based)
print(f"\nfruits[0] = {fruits[0]}")  # First element
print(f"fruits[1] = {fruits[1]}")   # Second element
print(f"fruits[3] = {fruits[3]}")   # Fourth element

# Negative indexing (right to left, -1 is last)
print(f"\nfruits[-1] = {fruits[-1]}")   # Last element
print(f"fruits[-2] = {fruits[-2]}")   # Second last element
print(f"fruits[-3] = {fruits[-3]}")   # Third last element

# Index out of bounds (ERROR)
# print(fruits[10])  # This would cause an IndexError

# ====================================================================
# 4. ADDING ELEMENTS
# ====================================================================

print("\n" + "="*60)
print("ADDING ELEMENTS")
print("="*60)

vegetables = ['carrot', 'potato']
print(f"Original: {vegetables}")

# append() - adds single element at end
vegetables.append('tomato')
print(f"After append('tomato'): {vegetables}")

# insert() - adds element at specific position
vegetables.insert(1, 'broccoli')  # Insert at index 1
print(f"After insert(1, 'broccoli'): {vegetables}")

# extend() - adds multiple elements
vegetables.extend(['onion', 'garlic'])
print(f"After extend(['onion', 'garlic']): {vegetables}")

# Using + operator (concatenation)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"[1, 2, 3] + [4, 5, 6] = {combined}")

# ====================================================================
# 5. REMOVING ELEMENTS
# ====================================================================

print("\n" + "="*60)
print("REMOVING ELEMENTS")
print("="*60)

colors = ['red', 'blue', 'green', 'yellow', 'blue']
print(f"Original: {colors}")

# remove() - removes first occurrence of value
colors_copy = colors.copy()
colors_copy.remove('blue')
print(f"After remove('blue'): {colors_copy}")

# pop() - removes and returns element at index (default -1)
colors_copy = colors.copy()
removed = colors_copy.pop()  # Removes last element
print(f"After pop() [default]: {colors_copy}, removed: {removed}")

colors_copy = colors.copy()
removed = colors_copy.pop(1)  # Removes element at index 1
print(f"After pop(1): {colors_copy}, removed: {removed}")

# del keyword - removes element at index
colors_copy = colors.copy()
del colors_copy[0]
print(f"After del colors_copy[0]: {colors_copy}")

# clear() - removes all elements
colors_copy = colors.copy()
colors_copy.clear()
print(f"After clear(): {colors_copy}")

# ====================================================================
# 6. LENGTH, MIN, MAX, SUM, AVERAGE
# ====================================================================

print("\n" + "="*60)
print("LENGTH, MIN, MAX, SUM, AVERAGE")
print("="*60)

numbers = [5, 2, 8, 1, 9, 3, 7]
print(f"Numbers: {numbers}")

print(f"len(numbers) = {len(numbers)}")
print(f"min(numbers) = {min(numbers)}")
print(f"max(numbers) = {max(numbers)}")
print(f"sum(numbers) = {sum(numbers)}")
print(f"Average = {sum(numbers) / len(numbers)}")
print(f"Average (rounded) = {sum(numbers) / len(numbers):.2f}")

# ====================================================================
# 7. FINDING ELEMENTS
# ====================================================================

print("\n" + "="*60)
print("FINDING ELEMENTS")
print("="*60)

animals = ['cat', 'dog', 'bird', 'cat', 'fish']
print(f"Animals: {animals}")

# index() - returns first index of element
index = animals.index('dog')
print(f"animals.index('dog') = {index}")

index = animals.index('cat')  # Finds first occurrence
print(f"animals.index('cat') = {index}")

# count() - counts occurrences
count = animals.count('cat')
print(f"animals.count('cat') = {count}")

# Check if element exists (in operator)
if 'bird' in animals:
    print("'bird' exists in animals")

if 'lion' not in animals:
    print("'lion' does not exist in animals")

# ====================================================================
# 8. SORTING AND REVERSING
# ====================================================================

print("\n" + "="*60)
print("SORTING AND REVERSING")
print("="*60)

numbers = [5, 2, 8, 1, 9, 3]
print(f"Original: {numbers}")

# sort() - sorts in place (modifies original)
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"After sort(): {numbers_copy}")

# sort in descending order
numbers_copy = numbers.copy()
numbers_copy.sort(reverse=True)
print(f"After sort(reverse=True): {numbers_copy}")

# sorted() - returns new sorted list (doesn't modify original)
result = sorted(numbers)
print(f"sorted(numbers): {result}")
print(f"Original still: {numbers}")

# reverse() - reverses in place
numbers_copy = numbers.copy()
numbers_copy.reverse()
print(f"After reverse(): {numbers_copy}")

# Using slicing to reverse (doesn't modify original)
reversed_list = numbers[::-1]
print(f"Using [::-1]: {reversed_list}")

# Sorting strings
words = ['zebra', 'apple', 'banana']
words.sort()
print(f"\nSorted words: {words}")

# ====================================================================
# 9. SLICING
# ====================================================================

print("\n" + "="*60)
print("SLICING - SYNTAX: list[start:end:step]")
print("="*60)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Basic slicing [start:end]
print(f"\nnumbers[0:5] = {numbers[0:5]}")        # Index 0 to 4
print(f"numbers[2:7] = {numbers[2:7]}")        # Index 2 to 6
print(f"numbers[5:9] = {numbers[5:9]}")        # Index 5 to 8

# Omitting start or end
print(f"\nnumbers[:5] = {numbers[:5]}")         # From beginning to index 4
print(f"numbers[5:] = {numbers[5:]}")          # From index 5 to end
print(f"numbers[:] = {numbers[:]}")            # Entire list

# With step [start:end:step]
print(f"\nnumbers[::2] = {numbers[::2]}")       # Every 2nd element
print(f"numbers[::3] = {numbers[::3]}")        # Every 3rd element
print(f"numbers[1::2] = {numbers[1::2]}")      # Starting at 1, every 2nd

# Negative indices in slicing
print(f"\nnumbers[-3:] = {numbers[-3:]}")       # Last 3 elements
print(f"numbers[:-3] = {numbers[:-3]}")        # All except last 3
print(f"numbers[-5:-2] = {numbers[-5:-2]}")    # Last 5 to last 2

# Reversing with slicing
print(f"\nnumbers[::-1] = {numbers[::-1]}")     # Reverse entire list
print(f"numbers[7:2:-1] = {numbers[7:2:-1]}")  # Reverse from index 7 to 3

# Slicing strings
text = "Python"
print(f"\n'{text}' slicing:")
print(f"  text[0:3] = {text[0:3]}")
print(f"  text[::2] = {text[::2]}")
print(f"  text[::-1] = {text[::-1]}")

# ====================================================================
# 10. COPYING LISTS
# ====================================================================

print("\n" + "="*60)
print("COPYING LISTS - IMPORTANT!")
print("="*60)

original = [1, 2, 3]
print(f"Original: {original}")

# WRONG - creates reference (both point to same list)
reference = original
reference.append(4)
print(f"\nWrong way (reference = original):")
print(f"  original: {original}")
print(f"  reference: {reference}")
print("  Both changed!")

# RIGHT methods - creates copy
original = [1, 2, 3]
print(f"\nOriginal: {original}")

# Method 1: copy()
copy1 = original.copy()
copy1.append(4)
print(f"Using copy(): {copy1}")
print(f"Original unchanged: {original}")

# Method 2: slicing [:]
original = [1, 2, 3]
copy2 = original[:]
copy2.append(4)
print(f"Using [:]: {copy2}")
print(f"Original unchanged: {original}")

# Method 3: list()
original = [1, 2, 3]
copy3 = list(original)
copy3.append(4)
print(f"Using list(): {copy3}")
print(f"Original unchanged: {original}")

# ====================================================================
# 11. ITERATION
# ====================================================================

print("\n" + "="*60)
print("ITERATION - LOOPING THROUGH LISTS")
print("="*60)

fruits = ['apple', 'banana', 'orange']

# Simple for loop
print("Simple loop:")
for fruit in fruits:
    print(f"  {fruit}")

# Loop with index using enumerate()
print("\nLoop with index (enumerate):")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# Loop using range and index
print("\nLoop using range and index:")
for i in range(len(fruits)):
    print(f"  Index {i}, Fruit: {fruits[i]}")

# While loop
print("\nWhile loop:")
i = 0
while i < len(fruits):
    print(f"  {fruits[i]}")
    i += 1

# ====================================================================
# 12. LIST COMPREHENSION
# ====================================================================

print("\n" + "="*60)
print("LIST COMPREHENSION")
print("="*60)

# Basic syntax: [expression for item in list]

# Transform each element
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Transform with condition: [expression for item in list if condition]
even_squared = [x**2 for x in numbers if x % 2 == 0]
print(f"Even numbers squared: {even_squared}")

# Filter elements
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")

# String operations
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
word_lengths = [len(word) for word in words]
print(f"Original words: {words}")
print(f"Uppercase: {upper_words}")
print(f"Lengths: {word_lengths}")

# ====================================================================
# 13. 2D ARRAYS (MATRICES)
# ====================================================================

print("\n" + "="*60)
print("2D ARRAYS (NESTED LISTS / MATRICES)")
print("="*60)

# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Accessing elements in 2D array
print(f"\nmatrix[0][0] = {matrix[0][0]}")  # First row, first column
print(f"matrix[0][1] = {matrix[0][1]}")   # First row, second column
print(f"matrix[1][2] = {matrix[1][2]}")   # Second row, third column
print(f"matrix[2][1] = {matrix[2][1]}")   # Third row, second column

# Get a row
print(f"\nFirst row (matrix[0]): {matrix[0]}")
print(f"Second row (matrix[1]): {matrix[1]}")

# Get a column (using list comprehension)
first_column = [matrix[i][0] for i in range(len(matrix))]
print(f"First column: {first_column}")

# Sum of all elements
total = sum([sum(row) for row in matrix])
print(f"Sum of all elements: {total}")

# ====================================================================
# 14. COMMON ARRAY METHODS
# ====================================================================

print("\n" + "="*60)
print("COMMON ARRAY/LIST METHODS")
print("="*60)

lst = [3, 1, 4, 1, 5]

print(f"Original list: {lst}")
print(f"len(lst) = {len(lst)}")
print(f"max(lst) = {max(lst)}")
print(f"min(lst) = {min(lst)}")
print(f"sum(lst) = {sum(lst)}")
print(f"lst.count(1) = {lst.count(1)}")
print(f"lst.index(4) = {lst.index(4)}")

# ====================================================================
# 15. JOINING AND SPLITTING LISTS
# ====================================================================

print("\n" + "="*60)
print("JOINING AND SPLITTING")
print("="*60)

# Join list into string
words = ['hello', 'world', 'python']
sentence = ' '.join(words)
print(f"Words: {words}")
print(f"Joined: '{sentence}'")

# Split string into list
text = "apple,banana,orange"
fruits = text.split(',')
print(f"\nText: '{text}'")
print(f"Split result: {fruits}")

text2 = "one two three four"
words = text2.split()
print(f"Text: '{text2}'")
print(f"Split result: {words}")

# ====================================================================
# 16. COMPARING LISTS
# ====================================================================

print("\n" + "="*60)
print("COMPARING LISTS")
print("="*60)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")

print(f"\nlist1 == list2: {list1 == list2}")      # True (same content)
print(f"list1 == list3: {list1 == list3}")       # False (different content)
print(f"list1 is list2: {list1 is list2}")       # False (different objects)

copy = list1.copy()
print(f"\nlist1 is copy: {list1 is copy}")         # False (different objects)
print(f"list1 == copy: {list1 == copy}")         # True (same content)

# ====================================================================
# 17. REMOVING DUPLICATES
# ====================================================================

print("\n" + "="*60)
print("REMOVING DUPLICATES")
print("="*60)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Original with duplicates: {numbers}")

# Method 1: Using set() - LOSES ORDER
unique1 = list(set(numbers))
print(f"Using set() [loses order]: {unique1}")

# Method 2: List comprehension with index check - KEEPS ORDER
unique2 = [x for i, x in enumerate(numbers) if x not in numbers[:i]]
print(f"Using list comprehension [keeps order]: {unique2}")

# Method 3: Using dict.fromkeys() - KEEPS ORDER (Python 3.7+)
unique3 = list(dict.fromkeys(numbers))
print(f"Using dict.fromkeys() [keeps order]: {unique3}")

print("\n" + "="*60)
print("END OF TUTORIAL")
print("="*60)
