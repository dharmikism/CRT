'''Recursion array sum'''
def array_sum(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n-1] + array_sum(arr, n-1)

# Example usage
arr = [1, 2, 3, 4, 5]
print(array_sum(arr, len(arr)))  # Output: 15

def Reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    Reverse_array(arr, start + 1, end - 1)

def reverse_string(s, start, end):
    if start >= end:
        return s
    s[start], s[end] = s[end], s[start]
    return reverse_string(s, start + 1, end - 1)