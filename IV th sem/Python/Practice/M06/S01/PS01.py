def linear_search(arr, target):
    """
    Linear Search: Traverse array from start to end until target is found.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List of elements (unsorted)
        target: Element to search for
    
    Returns:
        Index of target if found, else -1
    
    Example:
        >>> linear_search([3, 7, 2, 9, 1], 9)
        3
        >>> linear_search([3, 7, 2, 9, 1], 5)
        -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Binary Search: Search in sorted array by dividing into halves.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
    
    Returns:
        Index of target if found, else -1
    
    Example:
        >>> binary_search([1, 2, 3, 7, 9], 9)
        4
        >>> binary_search([1, 2, 3, 7, 9], 5)
        -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    # Test Linear Search
    arr = [3, 7, 2, 9, 1]
    target = 9
    print(f"Linear Search: Target {target} found at index {linear_search(arr, target)}")
    
    target = 5
    print(f"Linear Search: Target {target} found at index {linear_search(arr, target)}")
    
    # Test Binary Search
    sorted_arr = sorted(arr)
    target = 9
    print(f"Binary Search: Target {target} found at index {binary_search(sorted_arr, target)}")
    
    target = 5
    print(f"Binary Search: Target {target} found at index {binary_search(sorted_arr, target)}")
