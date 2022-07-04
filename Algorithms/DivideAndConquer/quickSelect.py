"""
Quick Select Algorithm - Is a selection algorithm to find the kth smallest element in an unordered list.
Avg Time Complexity: O(N)
Worst Time Complexity: O(N^2)
Space Complexity: O(1)
"""

def quick_select(lst, l, r, k):
    pivotIndex = len(lst)

    while pivotIndex != k-1:
        pivotIndex = partition(lst, l, r)
        if pivotIndex < k:
            l = pivotIndex + 1
        else:
            r = pivotIndex - 1

    return lst[pivotIndex]

def partition(lst, l, r):
    """
    Lomuto Parition - choose pivot as last elem (O(N^2) if array is sorted)
    """
    pivot = lst[r]
    i = l
    for j in range(l, r):
        if lst[j] < pivot:
            if i != j:
                lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[r] =  lst[r], lst[i] 
    return i

if __name__ == "__main__":
    lst = [5, 2, 1, 3, 4]
    print(quick_select(lst, 0, len(lst) - 1, 5))