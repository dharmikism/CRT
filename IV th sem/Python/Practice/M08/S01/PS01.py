"""
HASHING CONCEPTS - Complete Guide
==================================

Hashing is a technique to convert an input (key) into a fixed-size string of bytes.
The output, called a hash value or hash code, is used for fast lookups, indexing, and storage.
"""

# ============================================================================
# 1. BASIC HASH FUNCTION
# ============================================================================

def simple_hash(key, table_size):
    """
    Simple hash function: Maps a key to an index in a hash table.
    
    How it works:
        - Convert key to a number (if string, sum ASCII values)
        - Apply modulo operation to fit within table size
        - Result is the index where data should be stored
    
    Time Complexity: O(1) - constant time
    
    Args:
        key: The data to hash (string, int, etc.)
        table_size: Size of the hash table
    
    Returns:
        Hash value (index) in range [0, table_size-1]
    
    Example:
        >>> simple_hash("cat", 10)
        7  # (99+97+116) % 10 = 312 % 10 = 2
    """
    # For string keys: sum ASCII values of characters
    if isinstance(key, str):
        hash_value = sum(ord(char) for char in key)
    else:
        hash_value = hash(key)
    
    # Map to table size using modulo operation
    return hash_value % table_size


# ============================================================================
# 2. HASH TABLE (WITHOUT COLLISION HANDLING)
# ============================================================================

class SimpleHashTable:
    """
    Basic hash table without collision handling.
    
    NOTE: This is for educational purposes. Real hash tables handle collisions!
    
    Operations:
        - insert(key, value): O(1) average
        - search(key): O(1) average
        - delete(key): O(1) average
    """
    
    def __init__(self, size=10):
        """Initialize hash table with given size."""
        self.size = size
        self.table = [None] * size  # Array to store key-value pairs
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        Steps:
            1. Calculate hash value from key
            2. Find index using hash value
            3. Store (key, value) at that index
        """
        index = simple_hash(key, self.size)
        # Store as tuple (key, value) for collision detection
        self.table[index] = (key, value)
    
    def search(self, key):
        """
        Search for a value by key.
        
        Steps:
            1. Calculate hash value from key
            2. Check if data exists at that index
            3. Return value if found
        
        Returns:
            Value associated with key, or None if not found
        """
        index = simple_hash(key, self.size)
        if self.table[index] is not None:
            stored_key, value = self.table[index]
            if stored_key == key:
                return value
        return None
    
    def delete(self, key):
        """Remove key-value pair from hash table."""
        index = simple_hash(key, self.size)
        if self.table[index] is not None:
            self.table[index] = None


# ============================================================================
# 3. COLLISION HANDLING - CHAINING METHOD
# ============================================================================

class ChainedHashTable:
    """
    Hash table using CHAINING to handle collisions.
    
    Collision Handling Strategy: When two keys hash to the same index,
    store them in a linked list (chain) at that index.
    
    Advantages:
        - Simple to implement
        - No upper limit on elements
    
    Disadvantages:
        - Extra memory for pointers
        - Slower search if chain is long
    """
    
    def __init__(self, size=10):
        """Initialize with chains (lists) at each index."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Each slot is a list
    
    def insert(self, key, value):
        """
        Insert key-value pair. If collision occurs, add to chain.
        
        Steps:
            1. Hash the key to get index
            2. Check if key already exists in chain
            3. If exists: update value
            4. If not: append (key, value) tuple to chain
        
        Time Complexity:
            - Best: O(1) - empty chain
            - Worst: O(n) - all keys hash to same index
            - Average: O(1 + α) where α = load factor
        """
        index = simple_hash(key, self.size)
        
        # Check if key already exists (update scenario)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        # Key doesn't exist, add to chain
        self.table[index].append((key, value))
    
    def search(self, key):
        """
        Search for key in the hash table.
        
        Steps:
            1. Hash key to find index
            2. Traverse chain at that index
            3. Compare keys until found or chain ends
        
        Returns:
            Value if found, None otherwise
        """
        index = simple_hash(key, self.size)
        
        # Traverse the chain
        for k, v in self.table[index]:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        """Remove key-value pair from hash table."""
        index = simple_hash(key, self.size)
        
        # Find and remove from chain
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        
        return False


# ============================================================================
# 4. COLLISION HANDLING - LINEAR PROBING METHOD
# ============================================================================

class LinearProbingHashTable:
    """
    Hash table using LINEAR PROBING to handle collisions.
    
    Collision Handling Strategy: If a slot is occupied, look for the next
    empty slot by incrementing the index (with wraparound).
    
    Advantages:
        - No extra memory for pointers
        - Cache friendly
    
    Disadvantages:
        - Clustering: Adjacent occupied slots
        - Limited by table size
        - More complex search
    """
    
    def __init__(self, size=10):
        """Initialize hash table with None values."""
        self.size = size
        self.table = [None] * size
        self.keys = [None] * size
    
    def insert(self, key, value):
        """
        Insert key-value pair using linear probing.
        
        Steps:
            1. Hash key to get starting index
            2. If slot is empty: place item
            3. If slot is occupied:
               - If same key: update value
               - If different key: probe next slot (i+1) % size
            4. Repeat until empty slot found
        
        Time Complexity:
            - Best: O(1) - slot empty
            - Worst: O(n) - table nearly full
        """
        index = simple_hash(key, self.size)
        
        # Linear probing: find empty slot or same key
        probe_count = 0
        while probe_count < self.size:
            current_index = (index + probe_count) % self.size
            
            if self.keys[current_index] is None:
                # Empty slot found
                self.keys[current_index] = key
                self.table[current_index] = value
                return
            elif self.keys[current_index] == key:
                # Key already exists, update
                self.table[current_index] = value
                return
            
            probe_count += 1
    
    def search(self, key):
        """
        Search for key using linear probing.
        
        Steps:
            1. Hash key to starting index
            2. Compare key at current index
            3. If match: return value
            4. If empty slot: key not found
            5. If occupied but not match: probe next slot
        """
        index = simple_hash(key, self.size)
        
        probe_count = 0
        while probe_count < self.size:
            current_index = (index + probe_count) % self.size
            
            if self.keys[current_index] is None:
                # Empty slot, key not found
                return None
            elif self.keys[current_index] == key:
                # Key found
                return self.table[current_index]
            
            probe_count += 1
        
        return None
    
    def delete(self, key):
        """Remove key-value pair using linear probing."""
        index = simple_hash(key, self.size)
        
        probe_count = 0
        while probe_count < self.size:
            current_index = (index + probe_count) % self.size
            
            if self.keys[current_index] is None:
                return False
            elif self.keys[current_index] == key:
                self.keys[current_index] = None
                self.table[current_index] = None
                return True
            
            probe_count += 1
        
        return False


# ============================================================================
# 5. PYTHON'S BUILT-IN DICTIONARY (HashTable Implementation)
# ============================================================================

def demonstrate_python_dict():
    """
    Python's dictionary uses hashing internally.
    
    Key Properties:
        - O(1) average lookup, insertion, deletion
        - Uses hash() function on keys
        - Handles collisions internally
        - Keys must be hashable (immutable)
        - Values can be anything
    
    Example Usage:
    """
    
    # Create dictionary
    student = {}
    
    # Insert: O(1)
    student["name"] = "Dharmik"
    student["roll"] = 42
    student["gpa"] = 3.8
    
    # Search: O(1)
    print(student["name"])  # Output: Dharmik
    
    # Check existence: O(1)
    if "name" in student:
        print("Name found")
    
    # Delete: O(1)
    del student["gpa"]
    
    # Iterate: O(n)
    for key, value in student.items():
        print(f"{key}: {value}")


# ============================================================================
# 6. HASH SET (Using Hashing for Uniqueness)
# ============================================================================

class HashSet:
    """
    Hash Set: Collection with no duplicates.
    Uses hashing to ensure uniqueness.
    
    Operations:
        - add(element): O(1) average
        - remove(element): O(1) average
        - contains(element): O(1) average
    """
    
    def __init__(self, size=10):
        """Initialize hash set."""
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def add(self, value):
        """Add element to set (duplicate ignored)."""
        index = simple_hash(value, self.size)
        
        # Check if already exists
        for item in self.table[index]:
            if item == value:
                return  # Already exists, no duplicate
        
        # Add new element
        self.table[index].append(value)
    
    def remove(self, value):
        """Remove element from set."""
        index = simple_hash(value, self.size)
        
        for i, item in enumerate(self.table[index]):
            if item == value:
                self.table[index].pop(i)
                return True
        
        return False
    
    def contains(self, value):
        """Check if element exists in set."""
        index = simple_hash(value, self.size)
        
        for item in self.table[index]:
            if item == value:
                return True
        
        return False


# ============================================================================
# 7. IMPORTANT CONCEPTS
# ============================================================================

"""
COLLISION:
    - Occurs when two different keys hash to the same index
    - Inevitable as number of keys > number of hash values
    - Must be handled for correctness
    
LOAD FACTOR (α):
    - α = number of elements / table size
    - High α (>0.7): Many collisions, poor performance
    - Low α: Wasted memory but good performance
    - Optimal: α ≈ 0.5 - 0.7
    
HASH FUNCTION PROPERTIES:
    1. Deterministic: Same input always produces same output
    2. Efficient: Compute hash in O(1) time
    3. Uniform Distribution: Keys distributed evenly
    4. Avalanche Effect: Small input change → Big hash change
    
COLLISION RESOLUTION METHODS:
    1. Chaining: Multiple values at one index (linked list/array)
    2. Open Addressing:
       - Linear Probing: Check next slot (i+1), (i+2)...
       - Quadratic Probing: Check (i+1²), (i+2²)...
       - Double Hashing: Use second hash function
    
HASHABLE vs NON-HASHABLE:
    Hashable (can be dict keys):    Immutable (int, str, tuple)
    Non-hashable (can't be keys):   Mutable (list, set, dict)

USE CASES:
    1. Dictionaries/Maps: Fast key-value lookup
    2. Sets: Check membership quickly
    3. Caching: Store computed results
    4. Database Indexing: Fast record retrieval
    5. Deduplication: Remove duplicates
    6. Checksums: Verify data integrity
    7. Cryptography: Security hashing (SHA, MD5)
"""

# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================

def count_frequencies(arr):
    """
    Use hash table to count frequency of elements.
    
    Time: O(n), Space: O(unique elements)
    """
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return freq

# Example: count_frequencies([1, 2, 1, 3, 2, 1])
# Output: {1: 3, 2: 2, 3: 1}


def find_duplicates(arr):
    """
    Find all duplicate elements in array.
    
    Time: O(n), Space: O(unique elements)
    """
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    
    return duplicates

# Example: find_duplicates([1, 2, 1, 3, 2, 1])
# Output: {1, 2}


def two_sum(arr, target):
    """
    Find two numbers that sum to target using hash table.
    
    Time: O(n), Space: O(n)
    
    Approach:
        1. Store each number in a set
        2. For each number, check if (target - number) exists
        3. If yes, return the pair
    """
    seen = set()
    
    for num in arr:
        complement = target - num
        
        if complement in seen:
            return (complement, num)
        
        seen.add(num)
    
    return None

# Example: two_sum([2, 7, 11, 15], 9)
# Output: (2, 7)


def longest_substring_without_repeating(s):
    """
    Find length of longest substring without repeating characters.
    
    Time: O(n), Space: O(min(n, charset_size))
    
    Approach:
        1. Use hash table to store last seen position of each character
        2. Use sliding window to track current substring
        3. When duplicate found, move left pointer
    """
    char_index = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example: longest_substring_without_repeating("abcabcbb")
# Output: 3 ("abc")


def group_anagrams(words):
    """
    Group anagrams together using hash table.
    
    Time: O(n * k log k) where n=words, k=average word length
    
    Approach:
        1. Sort characters in each word
        2. Use sorted word as key in hash table
        3. Group words by their sorted form
    """
    anagram_groups = {}
    
    for word in words:
        # Sort word to use as key
        sorted_word = ''.join(sorted(word))
        
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())

# Example: group_anagrams(["eat", "tea", "ate", "bat", "tab"])
# Output: [["eat", "tea", "ate"], ["bat", "tab"]]


# ============================================================================
# 9. COMPLEXITY COMPARISON
# ============================================================================

"""
OPERATION COMPLEXITIES:

                Linear Search    Binary Search    Hash Table
Search          O(n)             O(log n)         O(1) average
Insert          O(n)             O(n)             O(1) average
Delete          O(n)             O(n)             O(1) average
Space           O(1)             O(1)             O(n)

Hash Table Best For:
    - Frequent lookups
    - Unknown data size
    - Dynamic insertions/deletions
    
Use Binary Search when:
    - Data is sorted
    - Space is limited
    - Collision handling adds complexity
"""

# ============================================================================
# TEST & DEMONSTRATION
# ============================================================================

if __name__ == "__main__":
    print("=== HASH TABLE DEMONSTRATION ===\n")
    
    # Test Chained Hash Table
    print("1. Chained Hash Table:")
    ht = ChainedHashTable(5)
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("cherry", 30)
    print(f"Search 'banana': {ht.search('banana')}")  # 20
    print(f"Search 'grape': {ht.search('grape')}")    # None
    
    # Test Linear Probing Hash Table
    print("\n2. Linear Probing Hash Table:")
    lp = LinearProbingHashTable(5)
    lp.insert("cat", 100)
    lp.insert("dog", 200)
    print(f"Search 'cat': {lp.search('cat')}")  # 100
    
    # Test Practical Examples
    print("\n3. Practical Examples:")
    print(f"Frequencies: {count_frequencies([1, 2, 1, 3, 2, 1])}")
    print(f"Duplicates: {find_duplicates([1, 2, 1, 3, 2, 1])}")
    print(f"Two Sum: {two_sum([2, 7, 11, 15], 9)}")
    print(f"Longest substring: {longest_substring_without_repeating('abcabcbb')}")
