"""
Maximum sum subarray problem: task of finding a contiguous subarray with the largest sum, within a given one-dimensional array A[1...n] of numbers. 

Kadane's Algorithm is used to solve this problem in O(N) time and constant space.

The algorithm uses dynamic programming to keep track of the current sum at any point in the array.
"""

def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    if numbers == []:
        raise ValueError('Empty array has no nonempty subarrays')

    best_sum = float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
