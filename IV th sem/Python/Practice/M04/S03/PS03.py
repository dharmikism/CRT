"""
====================================================================
STRINGS IN PYTHON - TUTORIAL WITH SYNTAX AND EXAMPLES
====================================================================
This file contains a complete tutorial on strings with runnable examples.
"""

# ====================================================================
# 1. WHAT ARE STRINGS?
# ====================================================================
# Strings are sequences of characters enclosed in quotes
# They are immutable (cannot be changed after creation)
# They are indexed just like lists (support slicing)

# ====================================================================
# 2. CREATING STRINGS
# ====================================================================

print("\n" + "="*60)
print("CREATING STRINGS")
print("="*60)

# Using single quotes
str1 = 'Hello'
print(f"Single quotes: {str1}")

# Using double quotes
str2 = "World"
print(f"Double quotes: {str2}")

# Both are equivalent
is_equal = 'Hello' == "Hello"
print(f"'Hello' == \"Hello\": {is_equal}")

# Multi-line strings with triple quotes (single or double)
str3 = '''This is a
multi-line string
using triple single quotes'''
print(f"Triple single quotes:\n{str3}")

str4 = """This is a
multi-line string
using triple double quotes"""
print(f"Triple double quotes:\n{str4}")

# Empty string
empty = ""
print(f"Empty string: '{empty}'")

# String from other types
str_from_int = str(42)
str_from_float = str(3.14)
str_from_bool = str(True)
print(f"str(42) = '{str_from_int}'")
print(f"str(3.14) = '{str_from_float}'")
print(f"str(True) = '{str_from_bool}'")

# ====================================================================
# 3. ACCESSING CHARACTERS (INDEXING)
# ====================================================================

print("\n" + "="*60)
print("ACCESSING CHARACTERS - INDEXING")
print("="*60)

text = "Python"
print(f"Text: '{text}'")

# Positive indexing (0-based, left to right)
print(f"\ntext[0] = '{text[0]}'")      # 'P'
print(f"text[1] = '{text[1]}'")       # 'y'
print(f"text[2] = '{text[2]}'")       # 't'
print(f"text[5] = '{text[5]}'")       # 'n'

# Negative indexing (right to left)
print(f"\ntext[-1] = '{text[-1]}'")    # 'n' (last character)
print(f"text[-2] = '{text[-2]}'")     # 'o' (second last)
print(f"text[-3] = '{text[-3]}'")     # 'h' (third last)

# Length
print(f"\nlen(text) = {len(text)}")

# Important: Strings are IMMUTABLE - cannot change a character
# text[0] = 'J'  # This would cause an ERROR

# ====================================================================
# 4. STRING SLICING
# ====================================================================

print("\n" + "="*60)
print("STRING SLICING - SYNTAX: string[start:end:step]")
print("="*60)

message = "HelloWorld"
print(f"Message: '{message}'")

# Basic slicing [start:end]
print(f"\nmessage[0:5] = '{message[0:5]}'")      # 'Hello'
print(f"message[5:10] = '{message[5:10]}'")     # 'World'
print(f"message[0:3] = '{message[0:3]}'")       # 'Hel'

# Omitting indices
print(f"\nmessage[:5] = '{message[:5]}'")        # 'Hello'
print(f"message[5:] = '{message[5:]}'")         # 'World'
print(f"message[:] = '{message[:]}'")           # 'HelloWorld'

# With step
print(f"\nmessage[::2] = '{message[::2]}'")      # Every 2nd character
print(f"message[::3] = '{message[::3]}'")       # Every 3rd character
print(f"message[1::2] = '{message[1::2]}'")     # Starting at 1, every 2nd

# Negative indices
print(f"\nmessage[-5:] = '{message[-5:]}'")      # Last 5 characters
print(f"message[:-5] = '{message[:-5]}'")       # All except last 5

# Reversing
print(f"\nmessage[::-1] = '{message[::-1]}'")    # Reverse entire string

# ====================================================================
# 5. STRING CONCATENATION
# ====================================================================

print("\n" + "="*60)
print("STRING CONCATENATION")
print("="*60)

first_name = "John"
last_name = "Doe"

# Using + operator
full_name = first_name + " " + last_name
print(f"Using +: '{full_name}'")

# Repeat string using * operator
dash = "-" * 10
print(f"Using * operator: '{dash}'")

# Check length after concatenation
combined = "hello" + "world"
print(f"'{combined}' has length: {len(combined)}")

# Multiple concatenations
greeting = "Hello" + " " + "World" + " " + "!"
print(f"Multiple concatenations: '{greeting}'")

# ====================================================================
# 6. STRING FORMATTING
# ====================================================================

print("\n" + "="*60)
print("STRING FORMATTING")
print("="*60)

name = "Alice"
age = 25
height = 5.67

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
print(f"f-string: My name is {name}, I'm {age} years old")
print(f"f-string with expression: Next year I'll be {age + 1}")
print(f"f-string with formatting: Height: {height:.2f} ft")

# Method 2: format()
print("format(): My name is {}, I'm {} years old".format(name, age))
print("format(): My name is {0}, I'm {1} years old".format(name, age))
print("format(): My name is {n}, I'm {a} years old".format(n=name, a=age))

# Method 3: % operator (older style)
print("%% operator: My name is %s, I'm %d years old" % (name, age))

# Format specifications
price = 19.99
print(f"Price: ${price:.2f}")      # 2 decimal places
print(f"Percentage: {75:.1f}%")    # 1 decimal place
print(f"Padded: {age:05d}")        # Pad with zeros to width 5

# ====================================================================
# 7. COMMON STRING METHODS
# ====================================================================

print("\n" + "="*60)
print("COMMON STRING METHODS")
print("="*60)

text = "Hello World Python"

# Case methods
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"title(): '{text.title()}'")
print(f"swapcase(): '{text.swapcase()}'")

# Finding and replacing
print(f"\ntext.find('World'): {text.find('World')}")      # Returns index
print(f"text.find('xyz'): {text.find('xyz')}")            # Returns -1 if not found
print(f"text.count('l'): {text.count('l')}")              # Counts occurrences

# Replace
replaced = text.replace('Python', 'Java')
print(f"text.replace('Python', 'Java'): '{replaced}'")

replaced = text.replace('l', 'L', 2)  # Replace first 2 occurrences
print(f"text.replace('l', 'L', 2): '{replaced}'")

# ====================================================================
# 8. CHECKING STRING CONTENT
# ====================================================================

print("\n" + "="*60)
print("CHECKING STRING CONTENT")
print("="*60)

# Membership (in operator)
text = "Python Programming"
print(f"Text: '{text}'")

print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'Programming' in text: {'Programming' in text}")

# Checking string types
str1 = "12345"
str2 = "Hello123"
str3 = "   "

print(f"\nstr1 = '{str1}'")
print(f"str1.isdigit(): {str1.isdigit()}")          # All characters are digits
print(f"str1.isnumeric(): {str1.isnumeric()}")      # All characters are numeric

print(f"\nstr2 = '{str2}'")
print(f"str2.isalpha(): {str2.isalpha()}")          # All characters are alphabetic
print(f"str2.isalnum(): {str2.isalnum()}")          # All characters are alphanumeric

print(f"\nstr3 = '{str3}'")
print(f"str3.isspace(): {str3.isspace()}")          # All characters are whitespace

# ====================================================================
# 9. SPLITTING AND JOINING
# ====================================================================

print("\n" + "="*60)
print("SPLITTING AND JOINING")
print("="*60)

# Splitting strings
text = "apple,banana,orange,grape"
print(f"Text: '{text}'")

fruits = text.split(',')
print(f"split(','): {fruits}")

# Split with different separator
sentence = "The quick brown fox"
words = sentence.split()  # Split by whitespace (default)
print(f"\nSentence: '{sentence}'")
print(f"split(): {words}")

# Split with limit
limited = text.split(',', 2)  # Split into max 3 parts
print(f"split(',', 2): {limited}")

# Joining strings
print(f"\n' - '.join(['a', 'b', 'c']): {' - '.join(['a', 'b', 'c'])}")
print(f"','.join(['apple', 'banana', 'orange']): {','.join(['apple', 'banana', 'orange'])}")

# ====================================================================
# 10. STRIPPING WHITESPACE
# ====================================================================

print("\n" + "="*60)
print("STRIPPING WHITESPACE")
print("="*60)

text = "  Hello World  "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")        # Remove from both ends
print(f"lstrip(): '{text.lstrip()}'")      # Remove from left
print(f"rstrip(): '{text.rstrip()}'")      # Remove from right

# Strip specific characters
text2 = "***Hello World***"
print(f"\nOriginal: '{text2}'")
print(f"strip('*'): '{text2.strip('*')}'")

# ====================================================================
# 11. STARTSWITH AND ENDSWITH
# ====================================================================

print("\n" + "="*60)
print("STARTSWITH AND ENDSWITH")
print("="*60)

filename = "document.pdf"
url = "https://www.example.com"

print(f"Filename: '{filename}'")
print(f"filename.endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"filename.endswith('.doc'): {filename.endswith('.doc')}")

print(f"\nURL: '{url}'")
print(f"url.startswith('http'): {url.startswith('http')}")
print(f"url.startswith('ftp'): {url.startswith('ftp')}")
print(f"url.startswith(('http', 'ftp')): {url.startswith(('http', 'ftp'))}")

# ====================================================================
# 12. FINDING SUBSTRINGS
# ====================================================================

print("\n" + "="*60)
print("FINDING SUBSTRINGS")
print("="*60)

text = "Hello World Hello Python Hello"

# find() - returns first index or -1
print(f"Text: '{text}'")
print(f"find('Hello'): {text.find('Hello')}")       # 0
print(f"find('World'): {text.find('World')}")       # 6
print(f"find('Java'): {text.find('Java')}")         # -1 (not found)

# rfind() - finds from right
print(f"rfind('Hello'): {text.rfind('Hello')}")     # 26 (last occurrence)

# count() - counts occurrences
print(f"count('Hello'): {text.count('Hello')}")     # 3
print(f"count('l'): {text.count('l')}")             # 3

# index() - like find() but raises error if not found
print(f"index('World'): {text.index('World')}")     # 6
# text.index('Java')  # Would raise ValueError

# ====================================================================
# 13. COMPARING STRINGS
# ====================================================================

print("\n" + "="*60)
print("COMPARING STRINGS")
print("="*60)

str1 = "Hello"
str2 = "Hello"
str3 = "hello"
str4 = "World"

print(f"str1 = '{str1}'")
print(f"str2 = '{str2}'")
print(f"str3 = '{str3}'")
print(f"str4 = '{str4}'")

# Equality
print(f"\nstr1 == str2: {str1 == str2}")      # True
print(f"str1 == str3: {str1 == str3}")       # False (case sensitive)
print(f"str1 == str4: {str1 == str4}")       # False

# Case-insensitive comparison
print(f"str1.lower() == str3.lower(): {str1.lower() == str3.lower()}")  # True

# Inequality
print(f"\nstr1 != str4: {str1 != str4}")      # True

# Lexicographical ordering
print(f"\nstr1 < str4: {str1 < str4}")        # True (H comes before W)
print(f"str1 > str4: {str1 > str4}")         # False

# ====================================================================
# 14. CHECKING IF STRING IS EMPTY
# ====================================================================

print("\n" + "="*60)
print("CHECKING IF STRING IS EMPTY")
print("="*60)

empty = ""
not_empty = "Hello"
spaces_only = "   "

print(f"empty = '{empty}'")
print(f"len(empty) == 0: {len(empty) == 0}")
print(f"not empty: {not empty}")               # Pythonic way

print(f"\nnot_empty = '{not_empty}'")
print(f"len(not_empty) == 0: {len(not_empty) == 0}")
print(f"not not_empty: {not not_empty}")

print(f"\nspaces_only = '{spaces_only}'")
print(f"spaces_only.strip(): '{spaces_only.strip()}'")
print(f"len(spaces_only.strip()) == 0: {len(spaces_only.strip()) == 0}")

# ====================================================================
# 15. CONVERTING BETWEEN STRINGS AND LISTS
# ====================================================================

print("\n" + "="*60)
print("CONVERTING BETWEEN STRINGS AND LISTS")
print("="*60)

# String to list
text = "Hello"
char_list = list(text)
print(f"text = '{text}'")
print(f"list(text) = {char_list}")

# List to string
letters = ['H', 'e', 'l', 'l', 'o']
word = ''.join(letters)
print(f"letters = {letters}")
print(f"''.join(letters) = '{word}'")

# String to list of words
sentence = "The quick brown fox"
words = sentence.split()
print(f"\nsentence = '{sentence}'")
print(f"split() = {words}")

# List of words to string
word_list = ['One', 'two', 'three']
result = ' '.join(word_list)
print(f"\nword_list = {word_list}")
print(f"' '.join(word_list) = '{result}'")

# ====================================================================
# 16. ESCAPE SEQUENCES
# ====================================================================

print("\n" + "="*60)
print("ESCAPE SEQUENCES")
print("="*60)

# Newline
print("Line 1\nLine 2")

# Tab
print("Name\tAge")
print("John\t25")
print("Alice\t30")

# Quote escaping
print("He said \"Hello\"")
print('I can\'t do this')

# Backslash
print("Path: C:\\Users\\Python")

# Raw strings (r prefix) - don't process escape sequences
print(r"Raw string: C:\Users\Python")

# ====================================================================
# 17. STRING IMMUTABILITY
# ====================================================================

print("\n" + "="*60)
print("STRING IMMUTABILITY")
print("="*60)

text = "Hello"
print(f"Original: '{text}'")

# This doesn't change the original string
upper_text = text.upper()
print(f"upper(): '{upper_text}'")
print(f"Original still: '{text}'")

# This creates a new string
old_text = "old"
new_text = old_text.replace('old', 'new')
print(f"\nOriginal: '{old_text}'")
print(f"After replace: '{new_text}'")
print(f"Original still: '{old_text}'")

# ====================================================================
# 18. ADVANCED: STRING METHODS
# ====================================================================

print("\n" + "="*60)
print("ADVANCED STRING METHODS")
print("="*60)

# expandtabs() - replace tabs with spaces
text = "Name\tAge\tCity"
print(f"Original: '{text}'")
print(f"expandtabs(10): '{text.expandtabs(10)}'")

# center(), ljust(), rjust() - alignment
text = "Hello"
print(f"\ncenter(20): '{text.center(20)}'")
print(f"ljust(20): '{text.ljust(20)}'")
print(f"rjust(20): '{text.rjust(20)}'")

# zfill() - pad with zeros
num = "42"
print(f"\nnum = '{num}'")
print(f"zfill(5): '{num.zfill(5)}'")

# partition() - split into 3 parts
text = "Hello-World-Python"
print(f"\ntext = '{text}'")
print(f"partition('-'): {text.partition('-')}")

# ====================================================================
# 19. WORKING WITH MULTIPLE STRINGS
# ====================================================================

print("\n" + "="*60)
print("WORKING WITH MULTIPLE STRINGS")
print("="*60)

# Combining strings
first = "Hello"
middle = " "
last = "World"
result = first + middle + last
print(f"Concatenation: '{result}'")

# Using f-string to combine
name = "Alice"
age = 25
info = f"My name is {name} and I'm {age} years old"
print(f"f-string: '{info}'")

# Check if all strings meet condition
words = ["Python", "Java", "C++"]
all_uppercase = all(word.isupper() for word in words)
print(f"words = {words}")
print(f"All uppercase: {all_uppercase}")

# Check if any string meets condition
any_short = any(len(word) < 5 for word in words)
print(f"Any word shorter than 5: {any_short}")

# ====================================================================
# 20. QUICK REFERENCE TABLE
# ====================================================================

print("\n" + "="*60)
print("QUICK REFERENCE TABLE")
print("="*60)

reference = """
METHOD                  EXAMPLE                      RESULT
=====================   ===========================  ===========
upper()                 'hello'.upper()              'HELLO'
lower()                 'HELLO'.lower()              'hello'
capitalize()            'hello'.capitalize()         'Hello'
title()                 'hello world'.title()        'Hello World'
strip()                 '  hello  '.strip()          'hello'
replace()               'hi'.replace('i', 'u')       'hu'
split()                 'a,b,c'.split(',')           ['a', 'b', 'c']
join()                  ','.join(['a','b','c'])      'a,b,c'
find()                  'hello'.find('l')            2
startswith()            'hello'.startswith('he')     True
endswith()              'hello'.endswith('lo')       True
count()                 'hello'.count('l')           2
isdigit()               '123'.isdigit()              True
isalpha()               'abc'.isalpha()              True
isspace()               '   '.isspace()              True
len()                   len('hello')                 5
"""
print(reference)

print("="*60)
print("END OF STRINGS TUTORIAL")
print("="*60)
