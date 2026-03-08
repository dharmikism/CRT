"""
TIME COMPLEXITY ANALYSIS GUIDE

Big O notation is used to describe the performance or complexity of an algorithm. 
It gives an upper bound on the time taken by an algorithm in terms of the size of the input data.

Common Time Complexities (from best to worst):
    
    O(1) --> Constant time
            The algorithm takes the same amount of time regardless of the input size.
            Example: Accessing an array element by index
    
    O(log n) --> Logarithmic time
                 The algorithm's time increases logarithmically as the input size increases.
                 Example: Binary search in a sorted array
    
    O(n) --> Linear time
             The algorithm's time increases linearly with the input size.
             Example: Simple for loop iterating through all elements
    
    O(n log n) --> Linearithmic/Quasilinear time
                   The algorithm's time increases as n log n, common in efficient sorting algorithms.
                   Example: Merge sort, Quick sort
    
    O(n^2) --> Quadratic time
               The algorithm's time increases quadratically with the input size.
               Example: Nested loops, Bubble sort
    
    O(2^n) --> Exponential time
               The algorithm's time grows exponentially with input size.
               Example: Recursive fibonacci (naive), Power set generation
    
    O(n!) --> Factorial time
              The algorithm's time grows factorially with input size.
              Example: Generating permutations of n elements
"""


def constant_time(n):
    """
    O(1) - Constant Time Complexity
    
    Performs a simple arithmetic operation that takes the same time regardless of n.
    
    Args:
        n (int): Input number
    
    Returns:
        int: The double of n
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Simple multiplication - always takes same time regardless of n value
    return n * 2


def logarithmic_time(n):
    """
    O(log n) - Logarithmic Time Complexity
    
    Demonstrates logarithmic complexity through repeated division.
    Similar to binary search where we repeatedly halve the problem space.
    
    Args:
        n (int): Input number (must be positive)
    
    Returns:
        int: The number of times n can be divided by 2 until it reaches 1
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    # Base case: when n is 1 or less, stop recursion
    if n <= 1:
        return n
    else:
        # Divide n by 2 in each recursive call
        # This creates a logarithmic number of calls
        return logarithmic_time(n // 2)


def linear_time(n):
    """
    O(n) - Linear Time Complexity
    
    Iterates through n elements once. Time grows proportionally with input size.
    
    Args:
        n (int): Number of iterations
    
    Returns:
        None: Prints numbers from 0 to n-1
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Loop runs n times, so complexity is proportional to n
    for i in range(n):
        print(i)


def quadratic_time(n):
    """
    O(n^2) - Quadratic Time Complexity
    
    Nested loops that iterate n times each. Time grows with the square of input size.
    
    Args:
        n (int): Size of the matrix dimension
    
    Returns:
        list: A 2D list (matrix) of size n x n with product indices
    
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    # Outer loop runs n times
    matrix = []
    for i in range(n):
        row = []
        # Inner loop runs n times for each outer loop iteration
        for j in range(n):
            # This operation runs n*n times total
            row.append(i * j)
        matrix.append(row)
    return matrix


def linearithmic_time(arr):
    """
    O(n log n) - Linearithmic Time Complexity
    
    Demonstrates linearithmic complexity through merge sort algorithm.
    This is common in efficient sorting algorithms.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Time Complexity: O(n log n)
    Space Complexity: O(n) for the auxiliary arrays
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: Split array into two halves (log n levels)
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer: Recursively sort both halves
    left_sorted = linearithmic_time(left)
    right_sorted = linearithmic_time(right)
    
    # Merge: Combine sorted halves (n operations at each level)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Helper function for merge sort that combines two sorted lists.
    
    Args:
        left (list): First sorted list
        right (list): Second sorted list
    
    Returns:
        list: Merged sorted list
    
    Time Complexity: O(n)
    """
    result = []
    i = j = 0
    
    # Compare elements from left and right, add smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def exponential_time(n):
    """
    O(2^n) - Exponential Time Complexity
    
    Demonstrates exponential complexity through naive recursive fibonacci.
    WARNING: Very slow for large n values (avoid n > 35).
    
    Args:
        n (int): The fibonacci number to calculate (should be small)
    
    Returns:
        int: The nth fibonacci number
    
    Time Complexity: O(2^n) - exponential growth
    Space Complexity: O(n) for recursion stack
    """
    # Base cases for fibonacci sequence
    if n <= 1:
        return n
    
    # Each call spawns 2 recursive calls, creating exponential growth
    return exponential_time(n - 1) + exponential_time(n - 2)


# ============================================================================
# DEMONSTRATION AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TIME COMPLEXITY DEMONSTRATIONS")
    print("=" * 60)
    
    # Test constant time
    print("\n1. CONSTANT TIME - O(1):")
    print(f"   constant_time(10) = {constant_time(10)}")
    print(f"   constant_time(1000) = {constant_time(1000)}")
    print("   Same operation time regardless of input size\n")
    
    # Test logarithmic time
    print("2. LOGARITHMIC TIME - O(log n):")
    print(f"   logarithmic_time(16) = {logarithmic_time(16)}")
    print(f"   logarithmic_time(32) = {logarithmic_time(32)}")
    print("   Time grows slowly as input increases\n")
    
    # Test linear time
    print("3. LINEAR TIME - O(n):")
    print("   linear_time(5):")
    linear_time(5)
    print("   Time grows proportionally with input\n")
    
    # Test quadratic time
    print("4. QUADRATIC TIME - O(n^2):")
    matrix = quadratic_time(3)
    for row in matrix:
        print(f"   {row}")
    print("   Time grows with square of input\n")
    
    # Test linearithmic time
    print("5. LINEARITHMIC TIME - O(n log n):")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"   Original array: {arr}")
    sorted_arr = linearithmic_time(arr)
    print(f"   Sorted array:   {sorted_arr}")
    print("   Time grows faster than linear but slower than quadratic\n")
    
    # Test exponential time
    print("6. EXPONENTIAL TIME - O(2^n):")
    for i in range(10):
        print(f"   exponential_time({i}) = {exponential_time(i)}")
    print("   Time grows exponentially - very slow for large n\n")

